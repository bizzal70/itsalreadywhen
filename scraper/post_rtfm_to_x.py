"""
Posts a tweet announcing the latest RTFM article.
Called automatically by the weekly-rtfm GitHub Actions workflow.
Requires env vars: X_API_KEY, X_API_SECRET, X_ACCESS_TOKEN, X_ACCESS_TOKEN_SECRET
"""

import os
import glob
import re
import tweepy
from pathlib import Path

RTFM_DIR = Path(__file__).parent.parent / "_rtfm"
BLOG_URL = "https://bizzal70.github.io/itsalreadywhen"


def get_latest_article():
    articles = sorted(glob.glob(str(RTFM_DIR / "*.md")), reverse=True)
    return Path(articles[0]) if articles else None


def parse_article(path):
    content = path.read_text(encoding="utf-8")
    title = re.search(r'title:\s*"(.+)"', content)
    summary = re.search(r'summary:\s*"(.+)"', content)
    date = re.search(r"date:\s*(\d{4}-\d{2}-\d{2})", content)

    title_text = title.group(1) if title else "RTFM"
    summary_text = summary.group(1) if summary else ""
    article_date = date.group(1) if date else ""

    slug = re.sub(r"^\d{4}-\d{2}-\d{2}-", "", path.stem)
    url = f"{BLOG_URL}/rtfm/{article_date.replace('-', '/')}/{slug}/" if article_date else BLOG_URL

    return title_text, summary_text, url


def build_tweet(title, summary, url):
    header = f"It's Already When. — RTFM: {title}"
    tweet = f"{header}\n\n{summary}\n\n{url}\n\n#CyberSecurity #CISO"
    if len(tweet) > 280:
        max_summary = 280 - len(f"{header}\n\n\n\n{url}\n\n#CyberSecurity #CISO") - 3
        summary = summary[:max_summary] + "..."
        tweet = f"{header}\n\n{summary}\n\n{url}\n\n#CyberSecurity #CISO"
    return tweet


def main():
    api_key = os.environ["X_API_KEY"]
    api_secret = os.environ["X_API_SECRET"]
    access_token = os.environ["X_ACCESS_TOKEN"]
    access_token_secret = os.environ["X_ACCESS_TOKEN_SECRET"]

    article_path = get_latest_article()
    if not article_path:
        print("No RTFM article found to tweet.")
        return

    title, summary, url = parse_article(article_path)
    tweet = build_tweet(title, summary, url)

    # Build thumbnail (same card Priced/Written attach; RTFM has no issue number,
    # so the card renders "ISSUE #?" exactly as those blogs' RTFM cards do).
    thumb_path = None
    try:
        from x_thumbnail import render
        fm = {"summary": summary, "date": article_path.stem[:10]}
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
