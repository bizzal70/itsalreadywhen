---
layout: field_note
title: "Field Note — October 09, 2026"
date: 2026-10-09
summary: "Citrix NetScaler (CVE-2026-107406) and AhsayCBS (CVE-2026-105133/105134) are the day's edge-device priorities, with AhsayCBS already under active exploitation."
---

## Today's Field Note
Edge boxes are the story again, because they always are. Citrix is urging immediate patching of CVE-2026-107406, a memory overflow in NetScaler ADC and Gateway that can reach RCE or DoS under certain SAML configurations. Meanwhile, two unpatched AhsayCBS backup flaws (CVE-2026-105133, an auth bypass, and CVE-2026-105134, OS command injection) are already being exploited in the wild, which is the exact combination that turns a backup server into an attacker's foothold. Add Cisco's batch of critical NX-OS bugs allowing root-level code execution on Nexus switches, and the pattern is clear: the perimeter and the fabric behind it are both in play this week. Patch availability is not the same as patch applied, and attackers know the gap.

## Today's Action
- Inventory all internet-facing NetScaler ADC and Gateway instances, confirm SAML usage, and apply the CVE-2026-107406 fix now. Rotate sessions and check for post-exploit persistence given NetScaler's history.
- Treat AhsayCBS as compromised until proven otherwise. No vendor patch exists for CVE-2026-105133/105134, so restrict management access to trusted IPs and hunt for anomalous OS commands and new accounts.
- Prioritize the Cisco NX-OS critical advisories on your Nexus switches; schedule emergency maintenance for anything reachable from untrusted segments.
- Pull external exposure reports for all three product families and confirm what is actually listening, not what you think is listening.
- Verify backup integrity and isolation specifically, since AhsayCBS sits directly in the recovery path.

## Resources

Verified links for the CVEs mentioned above: official advisories, and a live search for public detection rules if any exist yet.

- **CVE-2026-105133**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-105133) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-105133)
- **CVE-2026-105134**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-105134) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-105134)
- **CVE-2026-107406**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-107406) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-107406)

*You patched the firewall; the backup server let them in anyway.*

## Related

- [ShinyHunters Hacked Clop, Then Robbed the Ransoms Twice](/itsalreadywhen/2026/09/27/issue-015/)
- [AI Agents Left 18,000 Posts on a Dead German Wiki to Coordinate Their Escape](/itsalreadywhen/2026/09/06/issue-012/)
- [The Week AI Broke Into OpenAI, Google, and a Spanish Company](/itsalreadywhen/2026/09/20/issue-014/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*