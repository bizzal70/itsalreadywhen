---
layout: field_note
title: "Field Note — October 28, 2026"
date: 2026-10-28
summary: "CISA confirms active exploitation of the Node2Shell Brotli flaw and Adobe Commerce PolyShell bugs, while Tailscale patches wormable root-access SSH flaws disclosed before a fix existed."
---

## Today's Field Note
Three things are live and worth your afternoon. CISA added the Brotli "Node2Shell" flaw (also tracked as Broccoli2Shell and HTTP2Shell) to KEV, and honeypots are already logging hits, including one actor fumbling a broken exploit. Alongside it, CVE-2026-111497 in Adobe Commerce/Magento is behind the "PolyShell" campaign that has already breached hundreds of stores, so this is confirmed impact, not probing. Separately, Tailscale shipped 1.104.4 after someone dropped the "Tailworm" SSH flaws over the weekend before any patch existed; a compromised node can abuse the root-privileged Tailscale daemon to reach files and services on other machines. The uncoordinated disclosure means attackers and defenders got the details at the same moment, which is never the fair fight you want.

## Today's Action
- Patch Tailscale to 1.104.4 now on every node running Tailscale SSH, and audit SSH ACLs for over-broad node access.
- Inventory anything decoding Brotli (reverse proxies, Node services, HTTP/2 stacks) and apply vendor fixes for the Node2Shell flaw; treat KEV timelines as the deadline.
- Patch Adobe Commerce/Magento for CVE-2026-111497 immediately, then hunt for PolyShell web shells and unexpected admin accounts given hundreds of confirmed breaches.
- Pull honeypot and WAF logs for Brotli and Magento exploit patterns over the last week; assume probing predates the KEV listing.
- Flag Oracle EBS (CVE-2026-101767) and PeopleSoft (CVE-2026-35273) for this week's patch cycle before they graduate from "probing" to "owned."

## Resources

Verified links for the CVEs mentioned above: official advisories, and a live search for public detection rules if any exist yet.

- **CVE-2026-101767**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-101767) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-101767)
- **CVE-2026-111497**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-111497) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-111497)
- **CVE-2026-35273**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-35273) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-35273)

*You didn't get a head start on this one. Move like it.*

## Related

- [ShinyHunters Hacked Clop, Then Robbed the Ransoms Twice](/itsalreadywhen/2026/09/27/issue-015/)
- [AI Agents Left 18,000 Posts on a Dead German Wiki to Coordinate Their Escape](/itsalreadywhen/2026/09/06/issue-012/)
- [Hundreds of AI Agents Broke Into 440 PaperCut Servers in One Campaign](/itsalreadywhen/2026/09/13/issue-013/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*