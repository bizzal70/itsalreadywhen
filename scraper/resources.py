"""
Shared helper for building verified resource links (NVD, SigmaHQ) from CVE IDs
found in generated text. Links are constructed programmatically from the CVE ID
itself, never LLM-generated, to avoid hallucinated URLs.
"""

import re

CVE_PATTERN = re.compile(r"CVE-\d{4}-\d{4,7}")


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
