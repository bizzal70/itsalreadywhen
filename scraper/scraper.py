"""
Daily scraper — pulls RSS feeds and stores new articles to SQLite.
Run: python scraper.py
"""

import sqlite3
import hashlib
import feedparser
from datetime import datetime, timezone
from dateutil import parser as dateparser
from pathlib import Path
from feeds import FEEDS

DB_PATH = Path(__file__).parent / "articles.db"


def init_db(conn):
    conn.execute("""
        CREATE TABLE IF NOT EXISTS articles (
            id TEXT PRIMARY KEY,
            title TEXT NOT NULL,
            url TEXT NOT NULL,
            source TEXT NOT NULL,
            category TEXT NOT NULL,
            summary TEXT,
            published_at TEXT NOT NULL,
            fetched_at TEXT NOT NULL,
            used_in_digest INTEGER DEFAULT 0,
            used_in_fieldnote INTEGER DEFAULT 0
        )
    """)
    conn.commit()
    # Backfill for DBs created before this column existed
    cols = [row[1] for row in conn.execute("PRAGMA table_info(articles)")]
    if "used_in_fieldnote" not in cols:
        conn.execute("ALTER TABLE articles ADD COLUMN used_in_fieldnote INTEGER DEFAULT 0")
        conn.commit()


def article_id(url):
    return hashlib.sha256(url.encode()).hexdigest()[:16]


def parse_date(entry):
    for field in ("published", "updated"):
        val = getattr(entry, field, None)
        if val:
            try:
                return dateparser.parse(val).astimezone(timezone.utc).isoformat()
            except Exception:
                pass
    return datetime.now(timezone.utc).isoformat()


def fetch_feed(feed_meta):
    print(f"  Fetching {feed_meta['name']}...")
    try:
        parsed = feedparser.parse(feed_meta["url"])
        articles = []
        for entry in parsed.entries:
            url = entry.get("link", "")
            if not url:
                continue
            summary = entry.get("summary", "") or entry.get("description", "")
            # strip basic html tags from summary
            import re
            summary = re.sub(r"<[^>]+>", "", summary).strip()[:1000]
            articles.append({
                "id": article_id(url),
                "title": entry.get("title", "Untitled").strip(),
                "url": url,
                "source": feed_meta["name"],
                "category": feed_meta["category"],
                "summary": summary,
                "published_at": parse_date(entry),
                "fetched_at": datetime.now(timezone.utc).isoformat(),
            })
        return articles
    except Exception as e:
        print(f"    ERROR: {e}")
        return []


def save_articles(conn, articles):
    new_count = 0
    for a in articles:
        try:
            conn.execute("""
                INSERT OR IGNORE INTO articles
                (id, title, url, source, category, summary, published_at, fetched_at)
                VALUES (:id, :title, :url, :source, :category, :summary, :published_at, :fetched_at)
            """, a)
            if conn.execute("SELECT changes()").fetchone()[0]:
                new_count += 1
        except Exception as e:
            print(f"    DB error: {e}")
    conn.commit()
    return new_count


def main():
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M')}] Starting daily scrape...")
    conn = sqlite3.connect(DB_PATH)
    init_db(conn)

    total_new = 0
    for feed in FEEDS:
        articles = fetch_feed(feed)
        new = save_articles(conn, articles)
        print(f"    +{new} new articles from {feed['name']}")
        total_new += new

    conn.close()
    print(f"Done. {total_new} new articles saved to {DB_PATH}")


if __name__ == "__main__":
    main()
