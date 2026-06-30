"""
Posts a tweet announcing the latest Field Note.
Called automatically by the daily-field-note GitHub Actions workflow.
Requires env vars: X_API_KEY, X_API_SECRET, X_ACCESS_TOKEN, X_ACCESS_TOKEN_SECRET
"""

import os
import glob
import re
import tweepy
from pathlib import Path

NOTES_DIR = Path(__file__).parent.parent / "_field_notes"
BLOG_URL = "https://bizzal70.github.io/itsalreadywhen"


def get_latest_note():
    notes = sorted(glob.glob(str(NOTES_DIR / "*.md")), reverse=True)
    return Path(notes[0]) if notes else None


def parse_note(path):
    content = path.read_text(encoding="utf-8")
    summary = re.search(r'summary:\s*"(.+)"', content)
    date = re.search(r"date:\s*(\d{4}-\d{2}-\d{2})", content)

    summary_text = summary.group(1) if summary else ""
    note_date = date.group(1) if date else ""

    slug = re.sub(r"^\d{4}-\d{2}-\d{2}-", "", path.stem)
    url = f"{BLOG_URL}/field-notes/{note_date.replace('-', '/')}/{slug}/" if note_date else BLOG_URL

    return summary_text, url


def build_tweet(summary, url):
    header = "It's Already When. — Field Note"
    tweet = f"{header}\n\n{summary}\n\n{url}\n\n#CyberSecurity #BlueTeam"
    if len(tweet) > 280:
        max_summary = 280 - len(f"{header}\n\n\n\n{url}\n\n#CyberSecurity #BlueTeam") - 3
        summary = summary[:max_summary] + "..."
        tweet = f"{header}\n\n{summary}\n\n{url}\n\n#CyberSecurity #BlueTeam"
    return tweet


def main():
    client = tweepy.Client(
        consumer_key=os.environ["X_API_KEY"],
        consumer_secret=os.environ["X_API_SECRET"],
        access_token=os.environ["X_ACCESS_TOKEN"],
        access_token_secret=os.environ["X_ACCESS_TOKEN_SECRET"],
    )

    note_path = get_latest_note()
    if not note_path:
        print("No Field Note found to tweet.")
        return

    summary, url = parse_note(note_path)
    tweet = build_tweet(summary, url)

    print(f"Posting tweet:\n{tweet}\n")
    response = client.create_tweet(text=tweet)
    print(f"Tweet posted: https://x.com/itsalreadywhen/status/{response.data['id']}")


if __name__ == "__main__":
    main()
