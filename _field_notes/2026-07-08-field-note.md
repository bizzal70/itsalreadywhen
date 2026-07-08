---
layout: field_note
title: "Field Note — July 08, 2026"
date: 2026-07-08
summary: "Active exploitation of max-severity ColdFusion (CVE-2026-48282), Langflow, and Gitea (CVE-2026-20896) flaws, plus GhostLock (CVE-2026-43499), a 15-year-old Linux root escape hitting every mainstream distro."
---

## Today's Field Note
CISA added four exploited flaws to KEV with a Friday deadline, and two of them earn the attention: Adobe ColdFusion CVE-2026-48282 (CVSS 10.0, path traversal to RCE) and the Langflow auth bypass, both under active exploitation. Separately, Gitea CVE-2026-20896 is being hit in the wild via a single HTTP header that bypasses auth and hands over repos and secrets, which is the same self-hosted-dev-infra blast radius we keep watching burn. And GhostLock (CVE-2026-43499) is a 15-year-old Linux kernel local privilege escalation shipped by default in essentially every mainstream distro since 2011: no special permissions, no network, straight to root. None of this is theoretical today. The internet-facing web apps and your own build infrastructure are the fastest paths in, and attackers already have the maps.

## Today's Action
- Patch Adobe ColdFusion for CVE-2026-48282 immediately, or take exposed instances offline until you can. Do not wait for Friday.
- Apply the Langflow update and pull any Langflow admin interfaces off the public internet behind auth.
- Patch Gitea against CVE-2026-20896 now, then rotate every secret, token, and deploy key stored in those repos, because header-based auth bypass leaves no useful login trail.
- Roll GhostLock (CVE-2026-43499) kernel updates across your Linux fleet, prioritizing multi-user and shared-access hosts where any local account equals root.
- Grep ColdFusion, Gitea, and Langflow logs for anomalous requests and new admin activity going back at least two weeks; assume compromise on anything internet-exposed and unpatched.

## Resources

Verified links for the CVEs mentioned above: official advisories, and a live search for public detection rules if any exist yet.

- **CVE-2026-20896**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-20896) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-20896)
- **CVE-2026-43499**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-43499) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-43499)
- **CVE-2026-48282**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-48282) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-48282)

*Patch by Friday means someone already had since Tuesday.*