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


# A small, low-risk set of topic keywords -> an extra, more specific hashtag.
# Supplements (never replaces) the two static tags. Kept intentionally simple.
_TOPIC_TAGS = [
    ("ransomware", "#Ransomware"),
    ("zero-day", "#ZeroDay"),
    ("zero day", "#ZeroDay"),
    ("breach", "#DataBreach"),
    ("phishing", "#Phishing"),
    ("supply chain", "#SupplyChain"),
    ("malware", "#Malware"),
    (" ai ", "#AISecurity"),
    ("cloud", "#CloudSecurity"),
    ("wallet", "#CryptoSecurity"),
]


def extract_topic_tag(text):
    low = f" {text.lower()} "
    for kw, tag in _TOPIC_TAGS:
        if kw in low:
            return tag
    return None


def build_tweet(title, summary, url):
    """Two-part post: a link-free hook tweet (X's ranking suppresses reach on
    posts with outbound links) plus a reply carrying the link. RTFM titles are
    already descriptive hooks on their own, so this leads with title+summary
    directly instead of a brand+'RTFM:' prefix eating the preview text."""
    topic_tag = extract_topic_tag(f"{title} {summary}")
    tags = "#CyberSecurity #CISO" + (f" {topic_tag}" if topic_tag else "")
    main = f"{title}\n\n{summary}\n\n{tags}"
    if len(main) > 280:
        overhead = len(f"{title}\n\n\n\n{tags}") + 3
        summary = summary[: max(0, 280 - overhead)] + "..."
        main = f"{title}\n\n{summary}\n\n{tags}"
    reply = f"Full RTFM: {url}"
    return main, reply


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
    tweet, reply_tweet = build_tweet(title, summary, url)

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
    tweet_id = response.data["id"]
    print(f"Tweet posted: https://x.com/itsalreadywhen/status/{tweet_id}")

    print(f"Posting link reply:\n{reply_tweet}\n")
    reply_response = client.create_tweet(text=reply_tweet, in_reply_to_tweet_id=tweet_id)
    print(f"Reply posted: https://x.com/itsalreadywhen/status/{reply_response.data['id']}")


if __name__ == "__main__":
    main()
