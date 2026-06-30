"""
Posts a tweet announcing the latest weekly digest.
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

    return issue_num, summary_text, url


def build_tweet(issue_num, summary, url):
    tweet = f"It's Already When. — Issue #{issue_num:03d}\n\n{summary}\n\n{url}\n\n#CyberSecurity #ThreatIntel #InfoSec"
    if len(tweet) > 280:
        max_summary = 280 - len(f"It's Already When. — Issue #{issue_num:03d}\n\n\n\n{url}\n\n#CyberSecurity #ThreatIntel #InfoSec") - 3
        summary = summary[:max_summary] + "..."
        tweet = f"It's Already When. — Issue #{issue_num:03d}\n\n{summary}\n\n{url}\n\n#CyberSecurity #ThreatIntel #InfoSec"
    return tweet


def main():
    api_key = os.environ["X_API_KEY"]
    api_secret = os.environ["X_API_SECRET"]
    access_token = os.environ["X_ACCESS_TOKEN"]
    access_token_secret = os.environ["X_ACCESS_TOKEN_SECRET"]

    client = tweepy.Client(
        consumer_key=api_key,
        consumer_secret=api_secret,
        access_token=access_token,
        access_token_secret=access_token_secret
    )

    post_path = get_latest_post()
    if not post_path:
        print("No post found to tweet.")
        return

    issue_num, summary, url = parse_post(post_path)
    tweet = build_tweet(issue_num, summary, url)

    print(f"Posting tweet:\n{tweet}\n")
    response = client.create_tweet(text=tweet)
    print(f"Tweet posted: https://x.com/itsalreadywhen/status/{response.data['id']}")


if __name__ == "__main__":
    main()
