"""
Posts a tweet announcing the latest weekly digest, with a 1200x675 thumbnail card.
Called automatically by the weekly-digest GitHub Actions workflow.
Requires env vars: X_API_KEY, X_API_SECRET, X_ACCESS_TOKEN, X_ACCESS_TOKEN_SECRET
"""

import os
import glob
import re
import tempfile
import tweepy
from pathlib import Path

POSTS_DIR = Path(__file__).parent.parent / "_posts"
BLOG_URL = "https://bizzal70.github.io/itsalreadywhen"


def get_latest_post():
    posts = sorted(glob.glob(str(POSTS_DIR / "*.md")), reverse=True)
    for post in posts:
        if "issue-000" not in post:
            return Path(post)
    return None


def parse_post(path):
    content = path.read_text(encoding="utf-8")
    issue = re.search(r'issue:\s*"?(\d+)"?', content)
    summary = re.search(r'summary:\s*"(.+)"', content)
    date = re.search(r"date:\s*(\d{4}-\d{2}-\d{2})", content)

    issue_num = int(issue.group(1)) if issue else 0
    summary_text = summary.group(1) if summary else ""
    post_date = date.group(1) if date else ""

    slug = re.sub(r"^\d{4}-\d{2}-\d{2}-", "", path.stem)
    url = f"{BLOG_URL}/{post_date.replace('-', '/')}/{slug}/" if post_date else BLOG_URL

    return issue_num, summary_text, post_date, url


def build_tweet(issue_num, summary, url):
    tweet = f"It's Already When. — Issue #{issue_num:03d}\n\n{summary}\n\n{url}\n\n#CyberSecurity #ThreatIntel"
    if len(tweet) > 280:
        overhead = len(f"It's Already When. — Issue #{issue_num:03d}\n\n\n\n{url}\n\n#CyberSecurity #ThreatIntel") + 3
        summary = summary[: max(0, 280 - overhead)] + "..."
        tweet = f"It's Already When. — Issue #{issue_num:03d}\n\n{summary}\n\n{url}\n\n#CyberSecurity #ThreatIntel"
    return tweet


def main():
    api_key = os.environ["X_API_KEY"]
    api_secret = os.environ["X_API_SECRET"]
    access_token = os.environ["X_ACCESS_TOKEN"]
    access_token_secret = os.environ["X_ACCESS_TOKEN_SECRET"]

    post_path = get_latest_post()
    if not post_path:
        print("No post found to tweet.")
        return

    issue_num, summary, post_date, url = parse_post(post_path)
    tweet = build_tweet(issue_num, summary, url)

    # Build thumbnail
    thumb_path = None
    try:
        from x_thumbnail import render
        fm = {"issue": str(issue_num), "summary": summary, "date": post_date}
        thumb_path = render("when", fm)
    except Exception as e:
        print(f"[x_thumbnail] WARNING: thumbnail generation failed ({e}); posting without image")

    # Auth
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

    # Clean up temp file
    if thumb_path:
        try:
            os.unlink(thumb_path)
        except Exception:
            pass


if __name__ == "__main__":
    main()
