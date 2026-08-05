"""
Posts a tweet announcing the latest weekly digest, with a 1200x675 thumbnail card.
Called automatically by the weekly-digest GitHub Actions workflow.
Requires env vars: X_API_KEY, X_API_SECRET, X_ACCESS_TOKEN, X_ACCESS_TOKEN_SECRET
"""

import os
import glob
import re
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


# A small, low-risk set of topic keywords -> an extra, more specific hashtag.
# Supplements (never replaces) the two static tags. X's ranking leans far more
# on engagement velocity than hashtag matching, so this is a minor assist, not
# a primary lever -- kept intentionally simple.
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


def build_tweet(issue_num, summary, url):
    """Two-part post: a link-free hook tweet (X's ranking suppresses reach on
    posts with outbound links, and this account's tiny follower count means
    nearly all views come from algorithmic distribution, not the timeline) plus
    a reply carrying the link. Leads with the actual hook instead of a brand+
    issue-number prefix, which used to burn the pre-"Show more" preview text
    on branding rather than the scroll-stopping content."""
    topic_tag = extract_topic_tag(summary)
    tags = "#CyberSecurity #ThreatIntel" + (f" {topic_tag}" if topic_tag else "")
    main = f"{summary}\n\n{tags}"
    if len(main) > 280:
        overhead = len(f"\n\n{tags}") + 3
        summary = summary[: max(0, 280 - overhead)] + "..."
        main = f"{summary}\n\n{tags}"
    reply = f"Full breakdown (Issue #{issue_num:03d}): {url}"
    return main, reply


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
    tweet, reply_tweet = build_tweet(issue_num, summary, url)

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
    tweet_id = response.data["id"]
    print(f"Tweet posted: https://x.com/itsalreadywhen/status/{tweet_id}")

    print(f"Posting link reply:\n{reply_tweet}\n")
    reply_response = client.create_tweet(text=reply_tweet, in_reply_to_tweet_id=tweet_id)
    print(f"Reply posted: https://x.com/itsalreadywhen/status/{reply_response.data['id']}")

    # Clean up temp file
    if thumb_path:
        try:
            os.unlink(thumb_path)
        except Exception:
            pass


if __name__ == "__main__":
    main()
