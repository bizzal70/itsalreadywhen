"""
Weekly digest generator â€” pulls this week's articles from SQLite,
sends to Claude API, writes a Jekyll post, and pushes to GitHub.

Run: python digest.py
Requires: ANTHROPIC_API_KEY environment variable
          GIT configured with push access to the repo
"""

import os
import re
import sqlite3
import subprocess
from datetime import datetime, timezone, timedelta
from pathlib import Path
import anthropic
from resources import build_resources_section, insert_before_signoff, build_related_section

DB_PATH = Path(__file__).parent / "articles.db"
POSTS_DIR = Path(__file__).parent.parent / "_posts"

ISSUE_FRONTMATTER_RE = re.compile(r'^issue:\s*"?(\d+)"?\s*$', re.MULTILINE)


def get_issue_number():
    """Return the next issue number, derived from existing posts.

    We scan the ``issue:`` frontmatter of every post in ``_posts`` and add one
    to the highest we find. This replaces the old ``issue_number.txt`` counter,
    which was never committed back by the CI workflow (it only staged
    ``_posts/``), so every run re-read the same stale value and republished the
    same number â€” that is how issues #002, #003, and #004 all shipped as "002".
    Deriving from the posts themselves is self-healing and can't desync.
    """
    highest = -1
    if POSTS_DIR.exists():
        for post in POSTS_DIR.glob("*.md"):
            match = ISSUE_FRONTMATTER_RE.search(post.read_text(encoding="utf-8"))
            if match:
                highest = max(highest, int(match.group(1)))
    return highest + 1


def get_weeks_articles(conn):
    since = (datetime.now(timezone.utc) - timedelta(days=7)).isoformat()
    rows = conn.execute("""
        SELECT title, url, source, category, summary, published_at
        FROM articles
        WHERE published_at >= ? AND used_in_digest = 0
        ORDER BY published_at DESC
        LIMIT 150
    """, (since,)).fetchall()
    return rows


def mark_used(conn, urls):
    for url in urls:
        conn.execute("UPDATE articles SET used_in_digest = 1 WHERE url = ?", (url,))
    conn.commit()


def build_prompt(articles):
    lines = []
    for title, url, source, category, summary, published_at in articles:
        date_str = published_at[:10]
        lines.append(f"[{category.upper()}] {date_str} | {source}\nTitle: {title}\nURL: {url}\nSummary: {summary}\n")

    articles_text = "\n---\n".join(lines)

    return f"""You are the anonymous author of "It's Already When." â€” a weekly cybersecurity intelligence digest written for a general but informed audience. Your voice is dry, world-weary, and authoritative. You've been in the industry for decades. You have no patience for hype, vendor PR, or fear-mongering. You call things what they are.

Below are this week's cybersecurity news articles and advisories. Write the weekly digest post in Markdown.

Structure the post with these sections (use ## for section headers):
1. **This Week's Verdict** â€” 2-3 sentence opening that captures the week's overall theme with your signature dry wit
2. **The Breaches** â€” Notable incidents and what they reveal
3. **Vulnerabilities Worth Your Attention** â€” CVEs and advisories that actually matter, with plain-English impact
4. **Threat Actors & Campaigns** â€” Who's active, what they're doing
5. **The Bigger Picture** â€” One or two trends or analysis points that connect the week's dots
6. **Patch. Now.** â€” A short actionable list of the most critical things defenders should do this week

Rules:
- Write for someone who knows what a CVE is but doesn't need jargon for its own sake
- Be specific â€” name the vendors, name the threat actors, name the CVE IDs
- No bullet-point soup. Mix prose and lists naturally
- Keep it under 1200 words
- Do not mention that you used AI to write this
- Do not use em dashes (â€”) anywhere in the text. Use periods, commas, or parentheses instead
- End with a single italicized sign-off line that fits the brand voice

Also provide, before the post content, these two lines (both will be stripped from the post):
- "HEADLINE: <a specific, curiosity-driving headline for this week's issue, 40 to 70 characters, no issue number, no date, no clickbait lies; lead with the week's single most interesting concrete thing>"
- "SUMMARY: <one dry sentence for the blog index>"

---

ARTICLES THIS WEEK:

{articles_text}
"""


def write_post(issue_number, headline, summary, content, week_label):
    today = datetime.now().strftime("%Y-%m-%d")
    slug = f"issue-{issue_number:03d}"
    filename = POSTS_DIR / f"{today}-{slug}.md"

    safe_summary = summary.replace('"', "'")
    # Promote the hook (headline, else summary) into the title; the issue number
    # and week move to a kicker line above the body. CTA lands after the sign-off.
    hook = (headline or summary).strip().strip('"').rstrip(".")
    title = (hook or f"Issue #{issue_number:03d} â€” {week_label}").replace('"', "'")
    kicker = f"*Issue #{issue_number:03d} Â· {week_label}*"
    cta = (
        "\n\n---\n\n*New Issue every week. Follow "
        "[@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS "
        "so the next patch list lands before your SOC needs it.*"
    )
    frontmatter = f"""---
layout: post
title: "{title}"
date: {today}
issue: "{issue_number}"
summary: "{safe_summary}"
description: "{safe_summary}"
---

"""
    related = build_related_section(POSTS_DIR.parent, filename.name, current_text=f"{headline} {content}")
    filename.write_text(
        frontmatter + kicker + "\n\n" + content
        + ("\n\n" + related if related else "") + cta,
        encoding="utf-8",
    )
    print(f"Post written: {filename}")
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
    articles = get_weeks_articles(conn)

    if not articles:
        print("No new articles this week. Run scraper.py first.")
        conn.close()
        return

    print(f"Generating digest from {len(articles)} articles...")

    client = anthropic.Anthropic(api_key=api_key)
    response = client.messages.create(
        model="claude-opus-4-8",
        # A ~1200-word post across six sections plus a sign-off runs well past
        # 2000 tokens; that cap silently truncated Issue #002 mid-sentence.
        max_tokens=4000,
        messages=[{"role": "user", "content": build_prompt(articles)}]
    )

    # Never publish a partial digest. If the model hit the token ceiling the
    # post will be cut off mid-sentence, so fail loudly instead of shipping it.
    if response.stop_reason == "max_tokens":
        raise SystemExit(
            "ERROR: Claude response hit the max_tokens limit; the digest is "
            "truncated. Raise max_tokens and re-run. Refusing to publish a "
            "partial post."
        )

    raw = response.content[0].text.strip()

    # Extract headline + summary lines
    headline = ""
    summary = ""
    content_lines = []
    for line in raw.splitlines():
        if line.startswith("HEADLINE:"):
            headline = line.replace("HEADLINE:", "").strip()
        elif line.startswith("SUMMARY:"):
            summary = line.replace("SUMMARY:", "").strip()
        else:
            content_lines.append(line)
    content = "\n".join(content_lines).strip()

    content = insert_before_signoff(content, build_resources_section(content))

    issue_number = get_issue_number()
    today_fmt = datetime.now().strftime("%B %d, %Y")
    week_label = f"Week of {today_fmt}"

    filepath = write_post(issue_number, headline, summary, content, week_label)

    urls = [a[1] for a in articles]
    mark_used(conn, urls)
    conn.close()

    if not os.environ.get("GITHUB_ACTIONS"):
        git_push(filepath)


if __name__ == "__main__":
    main()
