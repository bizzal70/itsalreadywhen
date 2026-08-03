# CLAUDE.md

## Project Overview
"It's Already When." — a solo, anonymous-voice cybersecurity blog on Jekyll + GitHub Pages, live at https://bizzal70.github.io/itsalreadywhen/. Fully automated: an RSS scraper feeds a SQLite DB, Claude (via the `anthropic` SDK) writes three content types on their own schedules, and each is auto-tweeted. **This is live and actively publishing, not a scaffold** — as of this check it had shipped 7 weekly issues, 34 daily field notes, and 6 RTFM articles, all on schedule.

Three content types, each a separate collection with its own generator and cadence:
- **Weekly Issue** (`_posts/`, Sunday) — digest of the week's highest-signal security news, 6-section structure.
- **Daily Field Note** (`_field_notes/`, daily, two-cron catch-up design) — short tactical post from the last 24h of articles, or skipped entirely if nothing clears the substance floor.
- **Weekly RTFM** (`_rtfm/`, Wednesday) — long-form (1000-1500 word) evergreen piece grounded in a cited framework (NIST/CIS/OWASP), deliberately NOT sourced from current news.

## Tech Stack
- Jekyll (via `github-pages` gem) + GitHub Pages, deployed by `actions/jekyll-build-pages` + `actions/deploy-pages`
- Claude API (`anthropic` SDK, model string `claude-opus-4-8` as currently set in code — verify against the live model catalog before assuming this is current) for all three generators
- `feedparser` — RSS ingestion from ~12-13 security feeds (`scraper/feeds.py`)
- SQLite (`scraper/articles.db`, committed binary, restored via Actions cache)
- `tweepy` (OAuth 1.0a) — auto-posts each new item to X
- Pillow — tweet thumbnail cards, shared style module across this blog + its two sister blogs (itsalreadywritten, itsalreadypriced)
- `smtplib`/Gmail SMTP — emails a LinkedIn draft of each weekly Issue (not auto-posted to LinkedIn)

## Commands
No local dev loop — this is a cloud-only repo (no persistent local clone). Validate via `workflow_dispatch`; every scheduled workflow supports it.
```bash
# Manually run the scraper
gh workflow run daily-scrape.yml

# Manually generate today's Field Note
gh workflow run daily-field-note.yml

# Manually generate this week's Issue
gh workflow run weekly-digest.yml

# Manually generate this week's RTFM
gh workflow run weekly-rtfm.yml

# Redeploy the site
gh workflow run deploy.yml

# Fix a bad tweet for a specific issue
gh workflow run fix-tweet.yml -f issue_number=<N>
```

## Code Style
- No em dashes in generated post copy (deliberate anti-AI-tell rule, baked into all 3 Claude prompts).
- Never mention AI authorship in generated copy (same three prompts).
- CVE/resource links (NVD, SigmaHQ) must be constructed programmatically from the CVE ID string, never emitted by the LLM — `scraper/resources.py` exists specifically to prevent hallucinated URLs.
- `_BASEURL` in `resources.py` is intentionally hardcoded (not `{{ site.baseurl }}`) so internal links work even when Liquid isn't rendered inside a post body.

## Testing
- No test suite — validate by running the relevant `workflow_dispatch` and reading the actual generated post / tweet.
- Field Note quality is gated by a **deterministic** substance-floor checker (`scraper/note_quality.py`): min word count, required section markers, a minimum count of concrete regex matches (CVE IDs/numbers), hedge-phrase detection. This exists because an LLM quality judge over-flagged and produced false SKIPs elsewhere in this project — don't reintroduce an LLM-scored gate here without checking that history first.
- Digest generation hard-fails (`raise SystemExit`) rather than publish if the model hits `max_tokens` mid-response — a real truncation bug (Issue #002 shipped cut off mid-sentence) is the reason this check exists. Don't relax it without addressing the underlying token budget.

## Repository Etiquette
- No `docs/` directory — `README.md` is the closest thing to a runbook (architecture diagram, workflow table, content rules, secrets table) and is largely accurate; the one confirmed stale point is noted in Boundaries below.
- Content licensing is split: code is MIT, published post content is CC BY-NC 4.0 (`LICENSE-CONTENT.md`) — keep that distinction in mind if repurposing content elsewhere.

## Architecture Notes
- `scraper/scraper.py` — pulls RSS, dedupes by `sha256(url)[:16]`, writes to `articles.db`
- `scraper/field_note.py` / `digest.py` / `rtfm.py` — the three generators; each has its own Claude prompt and gating logic
- `scraper/note_quality.py` — deterministic substance-floor gate for Field Notes (see Testing)
- `scraper/resources.py` — deterministic CVE/resource link builder + keyword-overlap "Related posts" ranker (replaced an earlier recency-only version that dead-ended readers)
- `scraper/x_thumbnail.py` — shared thumbnail renderer across all three "It's Already *" blogs (style dict keyed `when`/`written`/`priced`)
- `scraper/post_to_x.py`, `post_field_note_to_x.py`, `post_rtfm_to_x.py` — per-collection tweet posters; thumbnail render and media upload are each wrapped in try/except so a rendering failure still lets the tweet post (text-only fallback)
- `scraper/fix_tweet.py` — manual one-off fix for a bad tweet; matches on the post's `issue:` frontmatter first (not the filename, which can go stale after a renumbering)
- `scraper/linkedin_draft.py` — generates a LinkedIn-voice draft from the latest Issue and emails it for manual posting; not automated end-to-end
- The issue counter is **derived by scanning `_posts/*.md` frontmatter** for the highest `issue:` value, not a standalone counter file — see Boundaries, this replaced a broken file-based counter.

## Boundaries — What NOT To Do
- **Cloud-only, no exceptions** — no persistent local clone of this repo exists or should exist; work via `gh api` / `gh workflow run` only.
- **Never publish a partial or thin post.** Both the digest (max_tokens truncation guard) and the Field Note (quality-floor retry-then-skip) are designed to fail loudly / skip a day rather than ship filler. Don't relax either safety net to "just get something out."
- **Never let an LLM generate a CVE/resource URL directly** — always route through `resources.py`'s programmatic construction. This was a deliberate design decision to prevent hallucinated links, not an oversight to "simplify."
- **Don't reintroduce a standalone issue-counter file.** `scraper/issue_number.txt` used to exist and caused issues #002-#004 to all ship mislabeled "002" because CI never committed the counter back. The current scan-based approach is self-healing by design — the README still describes the old file-based approach in its "Site structure" section; that part of the README is stale, trust the code.
- **RTFM must never be sourced from current news/the article DB** — it's explicitly evergreen, framework-grounded content. Don't wire it into the RSS pipeline "for consistency."
- **Never disclose AI authorship or use em dashes in generated copy** — both are explicit, deliberate style rules across all three prompts, not accidental gaps.

## Workflow Preferences
- For anything touching a live generator prompt or a publish/tweet path, validate via manual `workflow_dispatch` and read the actual output (post file or tweet) before trusting a change — no local way to dry-run this.
- One fix at a time; this pipeline auto-commits and auto-tweets on every scheduled run, so a bad change ships fast.

## Environment / Secrets
- `GH_PAT` — PAT with repo write access; required because a bot commit pushed with the default `GITHUB_TOKEN` would not itself trigger `deploy.yml`
- `ANTHROPIC_API_KEY` — Claude API calls (digest/field_note/rtfm generators)
- `X_API_KEY` / `X_API_SECRET` — X app OAuth 1.0a consumer keys
- `X_ACCESS_TOKEN` / `X_ACCESS_TOKEN_SECRET` — X user OAuth 1.0a access tokens
- `GMAIL_APP_PASSWORD` — Gmail SMTP app password, used only to email the LinkedIn draft (weekly-digest.yml step)
