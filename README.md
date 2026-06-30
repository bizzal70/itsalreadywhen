# It's Already When.

*Cybersecurity news for people who know how this ends.*

A fully automated, self-publishing cybersecurity publication with three distinct sections, each on its own cadence. No manual steps required — it scrapes, writes, publishes, and announces itself.

**Live site:** https://bizzal70.github.io/itsalreadywhen/
**X:** [@itsalreadywhen](https://x.com/itsalreadywhen)

## Sections

| Section | Cadence | What it is | Sourcing |
|---|---|---|---|
| **Issues** | Weekly, Sunday | The long-form digest: breaches, vulnerabilities, threat actors, the week's verdict | This week's scraped articles |
| **Field Notes** | Daily | Short, tactical entries on the highest-signal item(s) from the last 24 hours, with concrete actions | Last 24h of scraped articles |
| **RTFM** | Weekly, Wednesday | Long-form, evergreen best-practice articles grounded in named industry standards (NIST, CIS, OWASP, MITRE) | A maintained topic backlog, deliberately *not* news-driven |

Each section has its own index page, its own RSS feed, and its own X hashtag pairing (see below).

## How it works

```
Daily (6 AM MDT)         Daily (6:30 AM MDT)        Weekly Sun (8 AM MDT)      Weekly Wed (8 AM MDT)
─────────────────        ────────────────────       ──────────────────────    ──────────────────────
13 RSS feeds              Last 24h of articles        This week's articles      Next unused topic
      │                          │                           │                         │
      ▼                          ▼                           ▼                         ▼
scraper.py                 field_note.py                digest.py                  rtfm.py
      │                          │                           │                         │
      ▼                          ▼                           ▼                         ▼
articles.db (SQLite,        _field_notes/ post           _posts/ post              _rtfm/ post
cached between runs)              │                           │                         │
                                   ▼                           ▼                         ▼
                            GitHub Pages deploys ◄──────────────┴─────────────────────────┘
                                   │
                                   ▼
                            Tweet posted to X (skipped quietly if nothing new published)
```

Everything runs on GitHub Actions. No local machine, server, or scheduled task required.

## Architecture

| Component | Purpose |
|---|---|
| `scraper/feeds.py` | List of 13 cybersecurity RSS sources (CISA, NVD, Krebs, Hacker News, Bleeping Computer, Dark Reading, SecurityWeek, Schneier, Recorded Future, Malwarebytes, Project Zero, US-CERT) |
| `scraper/scraper.py` | Pulls feeds, deduplicates by URL hash, stores to `articles.db` |
| `scraper/digest.py` | Feeds the week's unused articles to the Claude API, writes a weekly Issue, tracks issue numbers |
| `scraper/field_note.py` | Feeds the last 24h of unused articles to the Claude API, writes a Field Note; skips quietly if nothing is high-signal |
| `scraper/rtfm.py` | Picks the next unused topic from `rtfm_topics.yml`, writes a long-form RTFM article grounded only in the cited framework (no article-database lookup) |
| `scraper/resources.py` | Shared helper: builds a "Resources" section with NVD + SigmaHQ links for any CVE IDs mentioned in generated text, built deterministically from the CVE ID (never LLM-generated, to avoid hallucinated links) |
| `scraper/rtfm_topics.yml` | The RTFM topic backlog. Each entry cites a hand-verified, stable framework URL (NIST, CIS, OWASP, MITRE). Edit/add/reorder freely; entries are marked `used: true` after publishing |
| `scraper/post_to_x.py` | Tweets the latest Issue |
| `scraper/post_field_note_to_x.py` | Tweets the latest Field Note |
| `scraper/post_rtfm_to_x.py` | Tweets the latest RTFM article |
| `_layouts/`, `_posts/`, `_field_notes/`, `_rtfm/`, `assets/` | Standard Jekyll site, dark theme, GitHub Pages hosted, three Jekyll collections |

## Workflows (`.github/workflows/`)

- **`daily-scrape.yml`** — every day, 6 AM MDT: collects articles, caches the database between runs
- **`daily-field-note.yml`** — every day, 6:30 AM MDT: generates a Field Note (if anything is high-signal), pushes it, tweets it
- **`weekly-digest.yml`** — every Sunday, 8 AM MDT: catches up any missed articles, generates the Issue with Claude, commits and pushes it, tweets the announcement
- **`weekly-rtfm.yml`** — every Wednesday, 8 AM MDT: generates the next RTFM article, pushes it, tweets it
- **`deploy.yml`** — builds and deploys the Jekyll site to GitHub Pages on every push to `main`
- **`tweet-latest-rtfm.yml`** — manual-only: tweets the most recently published RTFM article without generating a new one (useful if a tweet step ships after an article already went out)
- **`fix-tweet.yml`** — manual-only: reposts a corrected tweet for a given Issue number (input: issue number), useful if a tweet goes out with a bad link

All scheduled workflows can also be triggered manually from the Actions tab (`workflow_dispatch`). Daily and weekly publish workflows guard against tweeting when nothing new was actually published that run.

## X hashtags

Each section uses a distinct two-tag pairing to reach different sub-communities rather than the same generic tags everywhere (X's algorithm also suppresses reach above ~3 tags per post):

| Section | Tags | Why |
|---|---|---|
| Issues | `#CyberSecurity #ThreatIntel` | Breach/threat-actor coverage |
| Field Notes | `#CyberSecurity #BlueTeam` | Tactical content reaches defenders who act on it |
| RTFM | `#CyberSecurity #CISO` | Standards/best-practice content reaches the leadership audience |

## Required secrets

Set under repo Settings → Secrets and variables → Actions:

| Secret | Purpose |
|---|---|
| `GH_PAT` | Personal access token with repo write access (used for committing posts) |
| `ANTHROPIC_API_KEY` | Claude API key for content generation |
| `X_API_KEY` / `X_API_SECRET` | X app consumer keys (OAuth 1.0a) |
| `X_ACCESS_TOKEN` / `X_ACCESS_TOKEN_SECRET` | X user access tokens, must be regenerated after any X app permission change |

## Local development

```bash
cd scraper
pip install -r requirements.txt
python scraper.py           # pull latest articles
python digest.py            # generate this week's Issue (requires ANTHROPIC_API_KEY)
python field_note.py        # generate today's Field Note
python rtfm.py               # generate the next RTFM article
```

To preview the Jekyll site locally, install Ruby + Bundler and run `bundle exec jekyll serve` from the repo root.

## Content rules baked into the generators

- No em dashes in generated prose (prompted explicitly, plus the `resources.py` template avoids them too) — a deliberate choice to avoid an obvious AI-writing tell
- No mention that AI was used to write any post
- RTFM is intentionally **not** sourced from the scraped article database. It cites only named, stable industry frameworks (NIST, CIS Controls, OWASP, MITRE ATT&CK) so it reads as a field manual, not a slow-news-week Issue
- CVE references anywhere get a "Resources" section with deterministic NVD + SigmaHQ search links, never LLM-generated URLs

## Notes

- Issue numbers are tracked in `scraper/issue_number.txt` and incremented on each digest run.
- Post frontmatter fields (`issue`, `summary`) are sanitized before writing to avoid breaking YAML parsing, quotes in AI-generated summaries are converted to single quotes.
- `digest.py`, `field_note.py`, and `rtfm.py` all skip their own git push step when running inside GitHub Actions (the workflow handles the commit/push itself).
- `field_note.py` and `digest.py` track "used" articles separately (`used_in_fieldnote` vs `used_in_digest` columns) so the daily and weekly pulls never compete for the same articles.
