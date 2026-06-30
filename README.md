# It's Already When.

*Cybersecurity news for people who know how this ends.*

A fully automated, self-publishing weekly cybersecurity digest. No manual steps required — it scrapes, writes, publishes, and announces itself.

**Live site:** https://bizzal70.github.io/itsalreadywhen/
**X:** [@itsalreadywhen](https://x.com/itsalreadywhen)

## How it works

```
Daily (6 AM MDT)              Weekly, Sunday (8 AM MDT)
─────────────────             ──────────────────────────
13 RSS feeds                  Pull week's articles from SQLite
      │                              │
      ▼                              ▼
scraper.py                    Claude API writes the digest
      │                              │
      ▼                              ▼
articles.db (SQLite,           Jekyll post committed to _posts/
cached between runs)                  │
                                       ▼
                               GitHub Pages deploys
                                       │
                                       ▼
                               Tweet posted to X
```

Everything runs on GitHub Actions. No local machine, server, or scheduled task required.

## Architecture

| Component | Purpose |
|---|---|
| `scraper/feeds.py` | List of 13 cybersecurity RSS sources (CISA, NVD, Krebs, Hacker News, Bleeping Computer, Dark Reading, SecurityWeek, Schneier, Recorded Future, Malwarebytes, Project Zero, US-CERT) |
| `scraper/scraper.py` | Pulls feeds, deduplicates by URL hash, stores to `articles.db` |
| `scraper/digest.py` | Feeds the week's unused articles to the Claude API, writes a Jekyll post, tracks issue numbers |
| `scraper/post_to_x.py` | Finds the latest post, builds a tweet (≤280 chars), posts via the X API |
| `_layouts/`, `_posts/`, `assets/` | Standard Jekyll site, dark theme, GitHub Pages hosted |

## Workflows (`.github/workflows/`)

- **`daily-scrape.yml`** — runs every day at 6 AM MDT, collects articles, caches the database between runs
- **`weekly-digest.yml`** — runs every Sunday at 8 AM MDT: catches up any missed articles, generates the digest with Claude, commits and pushes the new post, tweets the announcement
- **`deploy.yml`** — builds and deploys the Jekyll site to GitHub Pages on every push to `main`

All three can also be triggered manually from the Actions tab (`workflow_dispatch`).

## Required secrets

Set under repo Settings → Secrets and variables → Actions:

| Secret | Purpose |
|---|---|
| `GH_PAT` | Personal access token with repo write access (used for committing posts) |
| `ANTHROPIC_API_KEY` | Claude API key for digest generation |
| `X_API_KEY` / `X_API_SECRET` | X app consumer keys (OAuth 1.0a) |
| `X_ACCESS_TOKEN` / `X_ACCESS_TOKEN_SECRET` | X user access tokens — must be generated *after* the X app has Read+Write permissions |

## Local development

```bash
cd scraper
pip install -r requirements.txt
python scraper.py           # pull latest articles
python digest.py            # generate this week's issue (requires ANTHROPIC_API_KEY)
```

To preview the Jekyll site locally, install Ruby + Bundler and run `bundle exec jekyll serve` from the repo root.

## Notes

- Issue numbers are tracked in `scraper/issue_number.txt` and incremented on each digest run.
- Post frontmatter fields (`issue`, `summary`) are sanitized before writing to avoid breaking YAML parsing — quotes in AI-generated summaries are converted to single quotes.
- `digest.py` skips its own git push step when running inside GitHub Actions (the workflow handles the commit/push itself).
