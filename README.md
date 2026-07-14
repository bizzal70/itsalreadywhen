# It's Already When.

*Cybersecurity news for people who know how this ends.*

A fully automated, self-publishing cybersecurity publication. It scrapes, writes, publishes, and posts to X — no manual steps required.

**Live site:** https://bizzal70.github.io/itsalreadywhen  
**X:** [@itsalreadywhen](https://x.com/itsalreadywhen)

---

## Three sections, three cadences

| Section | Cadence | What it is |
|---|---|---|
| **Issues** | Weekly, Sunday 8am MT | Long-form digest: breaches, vulnerabilities, threat actors, the week's verdict |
| **Field Notes** | Daily, 6:30am MT | Short tactical entries on the highest-signal item(s) from the last 24 hours |
| **RTFM** | Weekly, Wednesday 8am MT | Evergreen best-practice articles grounded in NIST, CIS, OWASP, MITRE — not news-driven |

Each section has its own index page, RSS feed, and X hashtag pairing.

---

## How it works

```
6:00 AM MT daily          6:30 AM MT daily         Sunday 8 AM MT           Wednesday 8 AM MT
─────────────────         ─────────────────         ──────────────           ─────────────────
13 RSS feeds              Last 24h articles          Week's articles          Next unused topic
      │                         │                         │                         │
      ▼                         ▼                         ▼                         ▼
  scraper.py              field_note.py              digest.py                  rtfm.py
      │                         │                         │                         │
      ▼                         ▼                         ▼                         ▼
 articles.db              _field_notes/ post          _posts/ post             _rtfm/ post
                                │                         │                         │
                                └─────────────────────────┴─────────────────────────┘
                                                          │
                                                          ▼
                                              deploy.yml → GitHub Pages
                                                          │
                                                          ▼
                                          X card thumbnail generated (Pillow)
                                                          │
                                                          ▼
                                                  Tweet posted to X
```

Everything runs on GitHub Actions. No local machine, server, or cron required.

---

## Workflows

| Workflow | Schedule | What it does |
|---|---|---|
| `daily-scrape.yml` | 6:00am MT daily | Pulls 13 RSS feeds, deduplicates by URL hash, caches to `articles.db` |
| `daily-field-note.yml` | 6:30am MT daily | Generates a Field Note if anything is high-signal; pushes it; tweets with card |
| `weekly-digest.yml` | Sunday 8am MT | Catches up missed articles; generates the Issue with Claude; pushes; tweets with card |
| `weekly-rtfm.yml` | Wednesday 8am MT | Picks next RTFM topic; generates article; pushes; tweets |
| `deploy.yml` | On every push to `main` | Builds + deploys Jekyll site to GitHub Pages |
| `tweet-latest-rtfm.yml` | Manual | Tweets the most recent RTFM article (use if tweet step missed a publish) |
| `fix-tweet.yml` | Manual | Reposts a corrected tweet for a given Issue number |

All scheduled workflows support `workflow_dispatch` for manual runs. Publish workflows skip the tweet silently if nothing new was generated.

---

## Scraper components

| File | Purpose |
|---|---|
| `scraper/feeds.py` | 13 RSS sources: CISA, NVD, Krebs, Hacker News, Bleeping Computer, Dark Reading, SecurityWeek, Schneier, Recorded Future, Malwarebytes, Project Zero, US-CERT |
| `scraper/scraper.py` | Pulls feeds, deduplicates, stores to `articles.db` |
| `scraper/digest.py` | Generates weekly Issue from this week's unused articles via Claude API |
| `scraper/field_note.py` | Generates daily Field Note from last 24h of unused articles; skips if nothing high-signal |
| `scraper/rtfm.py` | Picks next unused topic from `rtfm_topics.yml`; generates evergreen RTFM article |
| `scraper/resources.py` | Builds deterministic NVD + SigmaHQ links for any CVE IDs in generated text — never LLM-generated URLs |
| `scraper/rtfm_topics.yml` | RTFM topic backlog. Each entry cites a stable, hand-verified framework URL. Entries are marked `used: true` after publishing |
| `scraper/x_thumbnail.py` | Generates 1200×675 X card image (Pillow) from post front matter: dark theme, red accent, blog name + issue + summary |
| `scraper/post_to_x.py` | Tweets weekly Issue announcement with thumbnail card attached |
| `scraper/post_field_note_to_x.py` | Tweets Field Note announcement |
| `scraper/post_rtfm_to_x.py` | Tweets RTFM announcement |

---

## X strategy

Each section uses a distinct two-tag pairing. X suppresses reach above ~3 tags per post, and different sub-communities follow each topic:

| Section | Tags | Audience |
|---|---|---|
| Issues | `#CyberSecurity #ThreatIntel` | Threat intel and IR teams |
| Field Notes | `#CyberSecurity #BlueTeam` | Defenders who act on tactical content |
| RTFM | `#CyberSecurity #CISO` | Leadership and compliance audience |

Every Issue tweet includes a generated 1200×675 card image: dark background, red accent, issue number and summary pulled from post front matter.

---

## Content rules

- **No em dashes** — a deliberate choice to avoid an obvious AI-writing tell
- **No AI disclosure** in post copy
- **RTFM is not news-driven** — it cites only stable framework documents (NIST, CIS, OWASP, MITRE ATT&CK), never the scraped article DB
- **CVE links are deterministic** — `resources.py` builds NVD + SigmaHQ URLs from the CVE ID directly; never hallucinated
- **Articles are tracked separately** — `used_in_fieldnote` and `used_in_digest` columns prevent daily and weekly generators from competing for the same articles

---

## Required secrets

Settings → Secrets and variables → Actions:

| Secret | Purpose |
|---|---|
| `GH_PAT` | Personal access token with repo write access (used for committing posts) |
| `ANTHROPIC_API_KEY` | Claude API for content generation |
| `X_API_KEY` / `X_API_SECRET` | X app consumer keys (OAuth 1.0a) |
| `X_ACCESS_TOKEN` / `X_ACCESS_TOKEN_SECRET` | X user access tokens |

---

## Site structure

```
_posts/           Weekly Issues
_field_notes/     Daily Field Notes
_rtfm/            Evergreen RTFM articles
_layouts/         Jekyll templates
assets/           CSS, fonts, images
scraper/          All automation scripts
.github/workflows/ GitHub Actions workflows
```

Issue numbers are tracked in `scraper/issue_number.txt` and incremented on each digest run.

---

## Adding an RTFM topic

Open `scraper/rtfm_topics.yml` and add an entry:

```yaml
- title: "Your topic title"
  framework: "NIST SP 800-53"
  url: "https://csrc.nist.gov/publications/detail/sp/800-53/rev-5/final"
  used: false
```

The next Wednesday run picks the first unused entry in the list.
## License

- **Code** (generators, workflows, templates, config): [MIT](LICENSE)
- **Written content** (posts, articles, field notes): [CC BY-NC 4.0](LICENSE-CONTENT.md) — attribution required, non-commercial reuse only.
