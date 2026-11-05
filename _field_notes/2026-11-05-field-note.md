---
layout: field_note
title: "Field Note — November 05, 2026"
date: 2026-11-05
summary: "Zyxel's GS1900 patch didn't close the actively exploited zero-day (CVE-2026-107441), APT29 is running iOS/Android watering-hole exploit chains via a hijacked Ukrainian analytics script, and a Debian/Ubuntu APT flaw lets MitM attackers run code as root."
---

## Today's Field Note
The Zyxel GS1900 situation is the one to watch: CVE-2026-107441 is an unauthenticated out-of-bounds write reachable via the web management interface, actively exploited against nearly 1,000 switches to steal configs and credentials, and the vendor's first fix (the 2.90 patch) did not actually close it. Binarly confirmed the earlier firmware was still exploitable, so if you patched and walked away, you are still exposed until the new round of firmware is applied. Separately, APT29 is back with a watering-hole campaign that hijacked the Plerdy SEO Tracker analytics script to serve iOS and Android exploit chains, mostly against Ukraine, the US, and Europe. And a freshly disclosed APT flaw in Debian and Ubuntu lets a MitM attacker swap a verified package and run code as root on retried downloads, which is default behavior from Debian 12 onward.

## Today's Action
- Pull any internet-facing Zyxel GS1900 switch management interface off the public internet now, then apply the newest firmware (not the 2.90 patch) for all 10 affected models.
- Rotate credentials and review configs on any Zyxel switch that was reachable, assuming compromise if it was exposed.
- Patch APT on Debian and Ubuntu immediately, and until then avoid package installs over untrusted or unencrypted networks.
- Hunt for Plerdy SEO Tracker script references in your web properties and check mobile endpoints (iOS/Android) for the APT29 exploit indicators from Sekoia's report.
- Block and monitor outbound traffic to the fake domains tied to the watering-hole campaign.

## Resources

Verified links for the CVEs mentioned above: official advisories, and a live search for public detection rules if any exist yet.

- **CVE-2026-107441**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-107441) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-107441)

*Patched is not the same as fixed. Go check which one you actually did.*

## Related

- [North Korea's TraderTraitor Pulls Off a $6.43 Billion Binance Heist](/itsalreadywhen/2026/11/01/issue-019/)
- [ShinyHunters Hacked Clop, Then Robbed the Ransoms Twice](/itsalreadywhen/2026/09/27/issue-015/)
- [OpenAI's Own Models Broke Out of Their Sandbox and Hacked Hugging Face](/itsalreadywhen/2026/07/26/issue-006/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*