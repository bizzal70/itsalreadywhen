"""
Weekly digest generator — pulls this week's articles from SQLite,
sends to Claude API, writes a Jekyll post, and pushes to GitHub.

Run: python digest.py
Requires: ANTHROPIC_API_KEY environment variable
          GIT configured with push access to the repo
"""

import os
import sqlite3
import subprocess
from datetime import datetime, timezone, timedelta
from pathlib import Path
import anthropic

DB_PATH = Path(__file__).parent / "articles.db"
POSTS_DIR = Path(__file__).parent.parent / "_posts"
ISSUE_TRACKER = Path(__file__).parent / "issue_number.txt"


def get_issue_number():
    if ISSUE_TRACKER.exists():
        n = int(ISSUE_TRACKER.read_text().strip()) + 1
    else:
        n = 1
    ISSUE_TRACKER.write_text(str(n))
    return n


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

    return f"""You are the anonymous author of "It's Already When." — a weekly cybersecurity intelligence digest written for a general but informed audience. Your voice is dry, world-weary, and authoritative. You've been in the industry for decades. You have no patience for hype, vendor PR, or fear-mongering. You call things what they are.

Below are this week's cybersecurity news articles and advisories. Write the weekly digest post in Markdown.

Structure the post with these sections (use ## for section headers):
1. **This Week's Verdict** — 2-3 sentence opening that captures the week's overall theme with your signature dry wit
2. **The Breaches** — Notable incidents and what they reveal
3. **Vulnerabilities Worth Your Attention** — CVEs and advisories that actually matter, with plain-English impact
4. **Threat Actors & Campaigns** — Who's active, what they're doing
5. **The Bigger Picture** — One or two trends or analysis points that connect the week's dots
6. **Patch. Now.** — A short actionable list of the most critical things defenders should do this week

Rules:
- Write for someone who knows what a CVE is but doesn't need jargon for its own sake
- Be specific — name the vendors, name the threat actors, name the CVE IDs
- No bullet-point soup. Mix prose and lists naturally
- Keep it under 1200 words
- Do not mention that you used AI to write this
- End with a single italicized sign-off line that fits the brand voice

Also provide, on the very first line before the post content, a one-sentence summary (for the blog index) prefixed with "SUMMARY:" — this will be stripped from the post.

---

ARTICLES THIS WEEK:

{articles_text}
"""


def write_post(issue_number, title, summary, content):
    today = datetime.now().strftime("%Y-%m-%d")
    slug = f"issue-{issue_number:03d}"
    filename = POSTS_DIR / f"{today}-{slug}.md"

    frontmatter = f"""---
layout: post
title: "Issue #{issue_number:03d} — {title}"
date: {today}
issue: "{issue_number}"
summary: "{summary}"
---

"""
    filename.write_text(frontmatter + content, encoding="utf-8")
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
    print("Pushed to GitHub — GitHub Actions will deploy in ~60 seconds.")


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
        max_tokens=2000,
        messages=[{"role": "user", "content": build_prompt(articles)}]
    )

    raw = response.content[0].text.strip()

    # Extract summary line
    summary = ""
    content_lines = []
    for line in raw.splitlines():
        if line.startswith("SUMMARY:"):
            summary = line.replace("SUMMARY:", "").strip()
        else:
            content_lines.append(line)
    content = "\n".join(content_lines).strip()

    issue_number = get_issue_number()
    today_fmt = datetime.now().strftime("%B %d, %Y")
    title = f"Week of {today_fmt}"

    filepath = write_post(issue_number, title, summary, content)

    urls = [a[1] for a in articles]
    mark_used(conn, urls)
    conn.close()

    if not os.environ.get("GITHUB_ACTIONS"):
        git_push(filepath)


if __name__ == "__main__":
    main()
