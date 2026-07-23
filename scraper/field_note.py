"""
Daily Field Note generator â€” pulls today's highest-signal articles from SQLite,
sends to Claude API, writes a short tactical Jekyll post to _field_notes/.

Run: python field_note.py
Requires: ANTHROPIC_API_KEY environment variable
"""

import os
import sqlite3
import subprocess
from datetime import datetime, timezone, timedelta
from zoneinfo import ZoneInfo
from pathlib import Path
import re
import anthropic
from resources import build_resources_section, insert_before_signoff, build_related_section
from scraper import init_db
from note_quality import assess

# Concrete-specificity signals for a cyber Field Note: a CVE id or any number.
_CONCRETE = re.compile(r"CVE-\d{4}-\d{4,7}|\b\d[\d.,]*\b")


def _quality_problems(content: str) -> list:
    """Deterministic substance floor: the two sections, enough substance, at
    least one concrete ref, and no hedge-filler."""
    return assess(content, min_words=90,
                  require=["## Today's Field Note", "## Today's Action"],
                  concrete_re=_CONCRETE, need_specifics=1)


DB_PATH = Path(__file__).parent / "articles.db"
NOTES_DIR = Path(__file__).parent.parent / "_field_notes"
MT = ZoneInfo("America/Denver")


def get_todays_articles(conn):
    since = (datetime.now(timezone.utc) - timedelta(hours=24)).isoformat()
    rows = conn.execute("""
        SELECT title, url, source, category, summary, published_at
        FROM articles
        WHERE published_at >= ? AND used_in_fieldnote = 0
        ORDER BY published_at DESC
        LIMIT 60
    """, (since,)).fetchall()
    return rows


def mark_used(conn, urls):
    for url in urls:
        conn.execute("UPDATE articles SET used_in_fieldnote = 1 WHERE url = ?", (url,))
    conn.commit()


def build_prompt(articles):
    lines = []
    for title, url, source, category, summary, published_at in articles:
        lines.append(f"[{category.upper()}] {source}\nTitle: {title}\nURL: {url}\nSummary: {summary}\n")

    articles_text = "\n---\n".join(lines)

    return f"""You are the anonymous author of "It's Already When." â€” a cybersecurity digest. This is a "Field Note": a short, tactical daily entry, distinct from the weekly Issue. Same dry, world-weary, authoritative voice â€” but tighter and more operational, like a note scrawled between incidents rather than a full dossier.

Below are today's cybersecurity articles. Pick the 1-3 highest-signal items (active exploitation, a CVE with a public PoC, a confirmed breach with real impact â€” skip vendor PR and low-signal noise). Write a Field Note in Markdown with exactly this structure:

## Today's Field Note
One tight paragraph (3-5 sentences) in voice covering what happened and why it matters right now.

## Today's Action
A short list (3-5 items) of concrete, specific things a defender should do today in response.

Rules:
- Name vendors, threat actors, and CVE IDs specifically
- No fear-mongering, no vendor PR language
- Keep the whole thing under 300 words
- Do not mention that you used AI to write this
- Do not use em dashes (â€”) anywhere in the text. Use periods, commas, or parentheses instead
- End with a single italicized one-line sign-off that fits the brand voice

Also provide, on the very first line before the content, a one-sentence summary (for the blog index) prefixed with "SUMMARY:" â€” this will be stripped from the post.

If nothing in today's articles is genuinely high-signal, write SUMMARY: SKIP and nothing else.

---

TODAY'S ARTICLES:

{articles_text}
"""


def write_note(title, summary, content):
    today = datetime.now(MT).strftime("%Y-%m-%d")
    slug = "field-note"
    filename = NOTES_DIR / f"{today}-{slug}.md"

    safe_summary = summary.replace('"', "'")
    frontmatter = f"""---
layout: field_note
title: "{title}"
date: {today}
summary: "{safe_summary}"
---

"""
    cta = (
        "\n\n---\n\n*Daily field notes, weekly Issues. Follow "
        "[@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*"
    )
    NOTES_DIR.mkdir(exist_ok=True)
    related = build_related_section(NOTES_DIR.parent, filename.name, current_text=f"{title} {content}")
    filename.write_text(
        frontmatter + content + ("\n\n" + related if related else "") + cta,
        encoding="utf-8",
    )
    print(f"Field Note written: {filename}")
    return filename


def git_push(filepath):
    repo_root = Path(__file__).parent.parent
    subprocess.run(["git", "add", str(filepath)], cwd=repo_root, check=True)
    subprocess.run(
        ["git", "commit", "-m", f"Add {filepath.name}"],
        cwd=repo_root, check=True
    )
    subprocess.run(["git", "push"], cwd=repo_root, check=True)
    print("Pushed to GitHub â€” GitHub Actions will deploy in ~60 seconds.")


def main():
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        raise SystemExit("ERROR: Set the ANTHROPIC_API_KEY environment variable.")

    conn = sqlite3.connect(DB_PATH)
    init_db(conn)
    articles = get_todays_articles(conn)

    if not articles:
        print("No new articles today. Skipping Field Note.")
        conn.close()
        return

    print(f"Generating Field Note from {len(articles)} articles...")

    client = anthropic.Anthropic(api_key=api_key)
    response = client.messages.create(
        model="claude-opus-4-8",
        max_tokens=800,
        messages=[{"role": "user", "content": build_prompt(articles)}]
    )

    raw = response.content[0].text.strip()

    summary = ""
    content_lines = []
    for line in raw.splitlines():
        if line.startswith("SUMMARY:"):
            summary = line.replace("SUMMARY:", "").strip()
        else:
            content_lines.append(line)
    content = "\n".join(content_lines).strip()

    urls = [a[1] for a in articles]
    mark_used(conn, urls)
    conn.close()

    if summary == "SKIP" or not content:
        print("Nothing high-signal today. Skipping Field Note.")
        return

    # Editorial substance floor: regenerate a thin/generic note once, stricter,
    # and skip it rather than publish filler.
    problems = _quality_problems(content)
    if problems:
        print(f"Field Note below the floor {problems}; regenerating once, stricter.")
        strict = build_prompt(articles) + (
            "\n\nYour previous draft fell short: " + "; ".join(problems) +
            ". Rewrite it far more specific and tactical: name exact vendors, CVE "
            "IDs, versions, and concrete defender actions. Keep both sections and "
            "stay under 300 words.")
        retry = client.messages.create(
            model="claude-opus-4-8", max_tokens=800,
            messages=[{"role": "user", "content": strict}])
        raw2 = retry.content[0].text.strip()
        s2, lines2 = "", []
        for line in raw2.splitlines():
            if line.startswith("SUMMARY:"):
                s2 = line.replace("SUMMARY:", "").strip()
            else:
                lines2.append(line)
        c2 = "\n".join(lines2).strip()
        if c2 and s2 != "SKIP" and not _quality_problems(c2):
            content, summary = c2, (s2 or summary)
            print("  retry cleared the floor.")
        else:
            print("  retry still below the floor; skipping today's Field Note.")
            return

    content = insert_before_signoff(content, build_resources_section(content, heading="## Resources"))

    today_fmt = datetime.now(MT).strftime("%B %d, %Y")
    title = f"Field Note â€” {today_fmt}"

    filepath = write_note(title, summary, content)

    if not os.environ.get("GITHUB_ACTIONS"):
        git_push(filepath)


if __name__ == "__main__":
    main()
