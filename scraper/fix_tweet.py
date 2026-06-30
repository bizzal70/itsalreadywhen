"""
One-off: posts a corrected tweet for a specific issue (manual fix for a bad link).
Usage: python fix_tweet.py <issue_number>
Requires env vars: X_API_KEY, X_API_SECRET, X_ACCESS_TOKEN, X_ACCESS_TOKEN_SECRET
"""

import os
import sys
import tweepy
from pathlib import Path
from post_to_x import parse_post, build_tweet, POSTS_DIR


def find_post_by_issue(issue_number):
    target = f"issue-{issue_number:03d}"
    for post in POSTS_DIR.glob("*.md"):
        if target in post.stem:
            return post
    return None


def main():
    issue_number = int(sys.argv[1])
    post_path = find_post_by_issue(issue_number)
    if not post_path:
        print(f"No post found for issue {issue_number}")
        return

    issue_num, summary, url = parse_post(post_path)
    tweet = build_tweet(issue_num, summary, url)

    client = tweepy.Client(
        consumer_key=os.environ["X_API_KEY"],
        consumer_secret=os.environ["X_API_SECRET"],
        access_token=os.environ["X_ACCESS_TOKEN"],
        access_token_secret=os.environ["X_ACCESS_TOKEN_SECRET"],
    )

    print(f"Posting corrected tweet:\n{tweet}\n")
    response = client.create_tweet(text=tweet)
    print(f"Posted: https://x.com/itsalreadywhen/status/{response.data['id']}")


if __name__ == "__main__":
    main()
