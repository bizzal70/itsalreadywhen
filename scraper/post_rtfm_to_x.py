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
    client = tweepy.Client(
        consumer_key=os.environ["X_API_KEY"],
        consumer_secret=os.environ["X_API_SECRET"],
        access_token=os.environ["X_ACCESS_TOKEN"],
        access_token_secret=os.environ["X_ACCESS_TOKEN_SECRET"],
    )

    article_path = get_latest_article()
    if not article_path:
        print("No RTFM article found to tweet.")
        return

    title, summary, url = parse_article(article_path)
    tweet = build_tweet(title, summary, url)

    print(f"Posting tweet:\n{tweet}\n")
    response = client.create_tweet(text=tweet)
    print(f"Tweet posted: https://x.com/itsalreadywhen/status/{response.data['id']}")


if __name__ == "__main__":
    main()
