"""
Shared helper for building verified resource links (NVD, SigmaHQ) from CVE IDs
found in generated text. Links are constructed programmatically from the CVE ID
itself, never LLM-generated, to avoid hallucinated URLs.
"""

import re
from pathlib import Path

CVE_PATTERN = re.compile(r"CVE-\d{4}-\d{4,7}")

# GitHub Pages baseurl for this blog. Hardcoded (not `{{ site.baseurl }}`) so the
# internal links don't depend on Liquid being rendered inside post bodies.
_BASEURL = "/itsalreadywhen"
_FNAME_RE = re.compile(r"(\d{4})-(\d{2})-(\d{2})-(.+)\.md$")
# collection dir -> URL prefix (Issues have no prefix; the others are namespaced).
_COLLECTIONS = [("_posts", ""), ("_field_notes", "/field-notes"), ("_rtfm", "/rtfm")]


# --- topical "Related" ranking -------------------------------------------------
# Related used to be the 3 most-RECENT posts, which dead-ends readers on unrelated
# content. Now prior posts are ranked by keyword overlap with the current post
# (shared TITLE terms weighted), with recency only as a tiebreaker and to
# back-fill so the section is never short. Deterministic: reads real files.
_STOP = set(
    "the a an and or of to in on at for is are was were be been by from as with "
    "that this it its you your their they them we our not but if how why what "
    "which when while then than into about over after before more most some any "
    "all can will just like one two new today week weekly daily field note notes "
    "issue rtfm read follow subscribe rss related resources here there also only "
    "very much many made make using used".split()
)
_MD_LINK = re.compile(r"\[([^\]]+)\]\([^)]+\)")


def _keywords(text: str) -> dict:
    text = _MD_LINK.sub(r"\1", text or "")          # keep link text, drop URLs
    text = re.sub(r"`[^`]*`", " ", text)            # drop code spans
    out: dict = {}
    for w in re.findall(r"[a-zA-Z][a-zA-Z0-9\-']{2,}", text.lower()):
        w = w.strip("-'")
        if len(w) < 3 or w in _STOP:
            continue
        out[w] = out.get(w, 0) + 1
    return out


def _relevance(cur: dict, cand_title: str, cand_body: str) -> int:
    cb = _keywords(cand_body)
    for t in set(_keywords(cand_title)):
        cb[t] = cb.get(t, 0) + 2                     # a shared TITLE term counts more
    return sum(cb.get(t, 0) for t in cur if t in cb)


def _post_text(path: Path):
    """(title, body) for a post file; body is the markdown minus front-matter."""
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return "", ""
    m = re.search(r'^title:\s*"(.+?)"', text, re.M)
    title = m.group(1) if m else ""
    body = re.sub(r"^---\n.*?\n---\n", "", text, count=1, flags=re.S)
    return title, body


def build_related_section(root, current_filename: str, limit: int = 3,
                          current_text: str = "") -> str:
    """Link the `limit` most RELEVANT prior posts across every collection, plus
    the section indexes, so a reader has a path deeper into the site.

    Ranked by keyword overlap with `current_text` (the post being written);
    recency is the tiebreaker and back-fill. With no `current_text` this reduces
    to the old most-recent behavior. Deterministic: reads real files on disk, so
    no URL is ever invented.
    """
    root = Path(root)
    cur = _keywords(current_text)
    entries = []  # (score, filename_sortkey, url, title)
    for coll, prefix in _COLLECTIONS:
        try:
            files = list((root / coll).glob("*.md"))
        except OSError:
            files = []
        for p in files:
            if p.name == current_filename:
                continue
            m = _FNAME_RE.match(p.name)
            if not m:
                continue
            y, mo, d, slug = m.groups()
            url = f"{_BASEURL}{prefix}/{y}/{mo}/{d}/{slug}/"
            title, body = _post_text(p)
            title = title or slug.replace("-", " ").strip().capitalize()
            score = _relevance(cur, title, body) if cur else 0
            entries.append((score, p.name, url, title))

    if not entries:
        return ""
    # topical first (score desc), then recency (filename is date-prefixed).
    entries.sort(key=lambda e: (e[0], e[1]), reverse=True)
    picked = entries[:limit]

    out = ["## Related", ""]
    out += [f"- [{t}]({u})" for _, _, u, t in picked]
    out += [
        "",
        f"More: [Issues]({_BASEURL}/) · [Field Notes]({_BASEURL}/field-notes/) · [RTFM]({_BASEURL}/rtfm/)",
    ]
    return "\n".join(out) + "\n"


def build_resources_section(content, heading="## Resources"):
    cves = sorted(set(CVE_PATTERN.findall(content)))
    if not cves:
        return ""

    lines = [f"{heading}\n", "Verified links for the CVEs mentioned above: official advisories, and a live search for public detection rules if any exist yet.\n"]
    for cve in cves:
        nvd_url = f"https://nvd.nist.gov/vuln/detail/{cve}"
        sigma_url = f"https://github.com/SigmaHQ/sigma/search?q={cve}"
        lines.append(f"- **{cve}**: [NVD advisory]({nvd_url}) · [Search Sigma for detection rules]({sigma_url})")

    return "\n".join(lines) + "\n"


def insert_before_signoff(content, resources):
    """Inserts the resources block before a trailing italicized sign-off line, if present."""
    if not resources:
        return content
    body_lines = content.splitlines()
    if body_lines and body_lines[-1].strip().startswith("*") and body_lines[-1].strip().endswith("*"):
        sign_off = body_lines.pop()
        return "\n".join(body_lines).rstrip() + "\n\n" + resources + "\n" + sign_off
    return content + "\n\n" + resources
