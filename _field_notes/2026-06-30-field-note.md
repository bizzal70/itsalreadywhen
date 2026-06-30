---
layout: field_note
title: "Field Note — June 30, 2026"
date: 2026-06-30
summary: "Active exploitation hits SimpleHelp (CVE-2026-48558) and Oracle EBS (CVE-2026-46817), while a public PoC drops for the libssh2 client flaw CVE-2026-55200."
---

## Today's Field Note
Three things worth your attention, all already in motion. Attackers are exploiting CVE-2026-48558 in SimpleHelp to drop Djinn Stealer, a cross-platform infostealer hitting Windows, macOS, and Linux — RMM tools remain a favorite because compromising one gets you everyone downstream. Separately, Oracle E-Business Suite's CVE-2026-46817 is now under active attack per Defused, the kind of financial-app flaw that doesn't stay quiet. And a public PoC just landed for CVE-2026-55200, a critical libssh2 client-side memory corruption bug (CVSS 9.2) where a malicious *server* can pop your *client* with no credentials and no interaction — every release through 1.11.1 is affected, which is a lot of embedded surface area.

## Today's Action
- Patch SimpleHelp immediately and hunt for Djinn Stealer indicators; review RMM logs for unexpected sessions and downstream deployments since disclosure.
- Apply Oracle's fix for CVE-2026-46817 on all EBS financial instances; if you can't patch today, restrict external access and watch for anomalous EBS activity.
- Inventory everything linking libssh2 ≤1.11.1 — including embedded and vendored copies — and prioritize updates for any client that connects to untrusted SSH endpoints.
- Treat outbound SSH from build agents, scanners, and automation as the new risk vector for CVE-2026-55200, not just inbound.
- Pull the SimpleHelp and Oracle CVEs into your emergency change queue; both have moved from disclosure to exploitation faster than a normal patch cycle tolerates.

## Resources

Verified links for the CVEs mentioned above — official advisories, and a live search for public detection rules if any exist yet.

- **CVE-2026-46817** — [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-46817) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-46817)
- **CVE-2026-48558** — [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-48558) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-48558)
- **CVE-2026-55200** — [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-55200) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-55200)

*It's already when. Patch like it.*