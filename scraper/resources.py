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


def _post_title(path: Path) -> str | None:
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return None
    m = re.search(r'^title:\s*"(.+?)"', text, re.M)
    return m.group(1) if m else None


def build_related_section(root, current_filename: str, limit: int = 3) -> str:
    """Link the `limit` most recent prior posts across every collection, plus the
    section indexes, so a reader has a path deeper into the site.

    Deterministic: reads the actual files on disk, so no URL is ever invented.
    URLs are built per collection (Issues `/…`, Field Notes `/field-notes/…`,
    RTFM `/rtfm/…`). Returns "" if there are no prior posts.
    """
    root = Path(root)
    entries = []  # (filename_sortkey, url, title)
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
            title = _post_title(p) or slug.replace("-", " ").strip().capitalize()
            entries.append((p.name, url, title))

    entries.sort(key=lambda e: e[0], reverse=True)  # filename is date-prefixed
    picked = entries[:limit]
    if not picked:
        return ""

    out = ["## Related", ""]
    out += [f"- [{t}]({u})" for _, u, t in picked]
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
