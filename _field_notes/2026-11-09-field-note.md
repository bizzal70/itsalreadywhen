---
layout: field_note
title: "Field Note — November 09, 2026"
date: 2026-11-09
summary: "CISA adds an actively exploited SonicWall SonicOS MFA bypass (CVE-2026-19868) to KEV, while LNbits tells all operators to pull their Lightning wallet servers offline amid live theft."
---

## Today's Field Note
Two items demand hands on keyboard today. CISA added CVE-2026-19868, a SonicWall SonicOS MFA bypass (CVSS 7.1/7.5), to the KEV catalog citing reports of real-world exploitation. An authentication reinforcement flaw on an edge firewall is exactly the kind of thing that gets turned into initial access before anyone finishes reading the advisory, so treat the KEV listing as a clock already running. Separately, the LNbits project has told every operator to shut down their Bitcoin Lightning wallet servers now, after at least one operator watched roughly 0.023 BTC walk out via an exploit on new accounts, with fixes still pending. When upstream says power it off rather than patch it, they mean it.

## Today's Action
- Inventory SonicWall SonicOS appliances and apply the vendor fix for CVE-2026-19868; if you cannot patch today, restrict management and SSLVPN exposure to known IPs.
- Pull SonicOS auth and VPN logs for anomalous MFA-less logins and new sessions from unexpected geographies.
- If you run LNbits, shut the server down now and keep it offline until the project ships its pending fixes, then audit new account activity and withdrawals.
- Confirm your SonicWall is covered by a current KEV-driven patch SLA; federal timelines are a reasonable floor for everyone else.
- Add SonicWall edge devices to your priority list for the week, not just today's firefight.

## Resources

Verified links for the CVEs mentioned above: official advisories, and a live search for public detection rules if any exist yet.

- **CVE-2026-19868**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-19868) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-19868)

*The alarm is not the fire. The fire started earlier.*

## Related

- [ShinyHunters Hacked Clop, Then Robbed the Ransoms Twice](/itsalreadywhen/2026/09/27/issue-015/)
- [North Korea's TraderTraitor Pulls Off a $6.43 Billion Binance Heist](/itsalreadywhen/2026/11/01/issue-019/)
- [AI Agents Left 18,000 Posts on a Dead German Wiki to Coordinate Their Escape](/itsalreadywhen/2026/09/06/issue-012/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*