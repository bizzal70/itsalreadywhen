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
    api_key = os.environ["X_API_KEY"]
    api_secret = os.environ["X_API_SECRET"]
    access_token = os.environ["X_ACCESS_TOKEN"]
    access_token_secret = os.environ["X_ACCESS_TOKEN_SECRET"]

    note_path = get_latest_note()
    if not note_path:
        print("No Field Note found to tweet.")
        return

    summary, url = parse_note(note_path)
    tweet = build_tweet(summary, url)

    # Build thumbnail (same card Priced/Written attach; field notes have no issue
    # number, so the card renders "ISSUE #?" exactly as those blogs' cards do).
    thumb_path = None
    try:
        from x_thumbnail import render
        fm = {"summary": summary, "date": note_path.stem[:10]}
        thumb_path = render("when", fm)
    except Exception as e:
        print(f"[x_thumbnail] WARNING: thumbnail generation failed ({e}); posting without image")

    # Auth: v1 is required for media_upload, v2 Client for create_tweet.
    auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
    v1 = tweepy.API(auth)
    client = tweepy.Client(
        consumer_key=api_key,
        consumer_secret=api_secret,
        access_token=access_token,
        access_token_secret=access_token_secret,
    )

    # Upload media if thumbnail was generated
    media_ids = None
    if thumb_path:
        try:
            media = v1.media_upload(thumb_path)
            media_ids = [media.media_id]
            print(f"[x_thumbnail] media_id={media.media_id}")
        except Exception as e:
            print(f"[x_post] WARNING: media upload failed ({e}); posting without image")

    print(f"Posting tweet:\n{tweet}\n")
    kwargs = {"text": tweet}
    if media_ids:
        kwargs["media_ids"] = media_ids
    response = client.create_tweet(**kwargs)
    print(f"Tweet posted: https://x.com/itsalreadywhen/status/{response.data['id']}")


if __name__ == "__main__":
    main()
