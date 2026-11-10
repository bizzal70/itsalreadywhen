---
layout: field_note
title: "Field Note — November 10, 2026"
date: 2026-11-10
summary: "Active exploitation hits Barracuda ESG, OpenSSH (SSHole), and Chrome's eighth zero-day of the year, while N-able pulls N-central offline after 33 PoC-backed bugs drop."
---

## Today's Field Note
Four separate fires today, and all of them already have flames at the door. Attackers are exploiting two patched Barracuda ESG flaws for root, and CISA's KEV additions now include the "SSHole" OpenSSH bug (CVE-2026-123158) being used live to run commands, steal creds, and dig in. Google shipped its eighth Chrome zero-day of 2026 (CVE-2026-125350, a use-after-free in XML, reported anonymously November 6 and already in the wild). Meanwhile N-able yanked its hosted N-central offline and told on-prem customers to shut servers down after a researcher dropped 33 PoC-backed bugs ("Able2Shell") including full takeover. None of this is theoretical, and the N-able situation means your RMM is now an inbound vector.

## Today's Action
- Patch Barracuda ESG immediately and hunt for root-level command execution and new accounts; assume compromise if exposed and unpatched.
- Apply OpenSSH fixes for CVE-2026-123158 (SSHole) now, then review auth logs and authorized_keys for persistence and credential theft.
- Force-update Chrome/Chromium to the build fixing CVE-2026-125350 and confirm restarts actually applied; this is being exploited.
- If you run N-central on-prem, shut it down per N-able guidance until patched; treat the box as fully reachable until you verify otherwise.
- Cross-check today's four KEV additions (GPUStack, FreeSWITCH, IBM Aspera Faspex, OpenSSH) against your inventory and meet the three-day federal clock even if you're not federal.

## Resources

Verified links for the CVEs mentioned above: official advisories, and a live search for public detection rules if any exist yet.

- **CVE-2026-123158**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-123158) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-123158)
- **CVE-2026-125350**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-125350) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-125350)

*Four doors, all already open. Pick the one closest to your crown jewels and start there.*

## Related

- [ShinyHunters Hacked Clop, Then Robbed the Ransoms Twice](/itsalreadywhen/2026/09/27/issue-015/)
- [North Korea's TraderTraitor Pulls Off a $6.43 Billion Binance Heist](/itsalreadywhen/2026/11/01/issue-019/)
- [AI Agents Left 18,000 Posts on a Dead German Wiki to Coordinate Their Escape](/itsalreadywhen/2026/09/06/issue-012/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*