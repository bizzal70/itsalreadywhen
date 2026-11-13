---
layout: field_note
title: "Field Note — November 13, 2026"
date: 2026-11-13
summary: "N-able N-central zero-day 4EverAble2Shell is under active exploitation within hours of PoC release, while Check Point gateways face destructive root-level attacks via PHP2Shell and CVE-2026-123039."
---

## Today's Field Note
Two edge-device stories are converging into the same bad week. N-able's N-central dropped a pair of flaws (4EverAble2Shell, Agent2Shell), and attackers were exploiting 4EverAble2Shell within hours of the PoC, hitting at least 21 servers, 19 of them already running Hotfix 2. That last detail matters: patching did not save them, and N-able is now restricting features and integrations as a stopgap, which tells you how confident they are in the fix. Separately, Check Point confirmed a zero-day chained with PHP2Shell and CVE-2026-123039 for root on Gaia OS, used in destructive attacks against Israeli organizations that wiped ESXi files. These are internet-facing boxes that run your remote management and your perimeter. Treat both as assume-breach until you have eyes on them.

## Today's Action
- Inventory every N-central server now, confirm Hotfix 2 status, and hunt for cryptominer activity and unexpected root processes even on patched systems.
- Honor N-able's feature and integration restrictions rather than re-enabling them for convenience; they exist because the fix is not fully trusted.
- Apply Check Point's emergency hotfixes for the Gaia OS root flaw and PHP2Shell, then review gateways for TSGA backdoor artifacts and signs of ESXi file tampering.
- Pull and preserve logs from both platforms before rotating any credentials or tokens tied to the management plane.
- Given MSP targeting (see also SCKit in ScreenConnect), isolate management consoles from general network access and enforce MFA on all technician accounts.

## Resources

Verified links for the CVEs mentioned above: official advisories, and a live search for public detection rules if any exist yet.

- **CVE-2026-123039**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-123039) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-123039)

*Your patch cadence assumes the vendor got it right. These two didn't.*

## Related

- [ShinyHunters Hacked Clop, Then Robbed the Ransoms Twice](/itsalreadywhen/2026/09/27/issue-015/)
- [North Korea's TraderTraitor Pulls Off a $6.43 Billion Binance Heist](/itsalreadywhen/2026/11/01/issue-019/)
- [Hundreds of AI Agents Broke Into 440 PaperCut Servers in One Campaign](/itsalreadywhen/2026/09/13/issue-013/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*