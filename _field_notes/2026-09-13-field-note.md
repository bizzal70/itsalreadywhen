---
layout: field_note
title: "Field Note — September 13, 2026"
date: 2026-09-13
summary: "CISA flags five actively exploited flaws in Artifactory, ScreenConnect, and RouterOS, while the Dutch NCSC warns of imminent exploitation against two critical Check Point VPN bugs."
---

## Today's Field Note
Two things demand attention before the coffee cools. CISA added five bugs to KEV under confirmed active exploitation, spanning JFrog Artifactory, ConnectWise ScreenConnect, and MikroTik RouterOS (starting with CVE-2026-42016, an authorization bypass). ScreenConnect and RouterOS are perennial favorites for initial access and persistence, so treat those as live intrusions in progress until proven otherwise. Separately, the Dutch NCSC says exploitation of two critical Check Point VPN flaws, CVE-2026-85102 and CVE-2026-85103, is imminent, which in NCSC-speak means someone already has working exploit code and the clock is public. Internet-facing gateways and remote-access tooling are the theme today, and none of these wait for your change-management window.

## Today's Action
- Patch Check Point VPN gateways for CVE-2026-85102 and CVE-2026-85103 now, or restrict management and VPN portals to known IPs if you cannot patch immediately.
- Update ConnectWise ScreenConnect and MikroTik RouterOS to fixed versions; both appear in the new KEV additions with active exploitation.
- Patch JFrog Artifactory for CVE-2026-42016 and audit for unauthorized package pulls or pushes that predate the fix.
- Hunt for compromise on all four products: review ScreenConnect access logs, RouterOS scheduler and user accounts, and VPN auth logs for anomalous sessions before you patched.
- Pull any exposed management interfaces for these devices off the public internet as a standing rule, not a one-off.

## Resources

Verified links for the CVEs mentioned above: official advisories, and a live search for public detection rules if any exist yet.

- **CVE-2026-42016**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-42016) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-42016)
- **CVE-2026-85102**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-85102) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-85102)
- **CVE-2026-85103**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-85103) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-85103)

*The exploits shipped before your ticket did.*

## Related

- [Hundreds of AI Agents Broke Into 440 PaperCut Servers in One Campaign](/itsalreadywhen/2026/09/13/issue-013/)
- [AI Agents Left 18,000 Posts on a Dead German Wiki to Coordinate Their Escape](/itsalreadywhen/2026/09/06/issue-012/)
- [OpenAI's Own Models Broke Out of Their Sandbox and Hacked Hugging Face](/itsalreadywhen/2026/07/26/issue-006/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*