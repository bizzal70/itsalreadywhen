---
layout: field_note
title: "Field Note — November 21, 2026"
date: 2026-11-21
summary: "CISA confirms active exploitation of VMware vCenter, Cisco Expressway, Apache Roller, and SAP NetWeaver flaws, with a China-nexus group tied to the vCenter zero-day."
---

## Today's Field Note
CISA added four bugs to KEV on evidence of active exploitation: CVE-2026-129448 (Apache Roller deserialization, CVSS 9.8) plus flaws in Cisco Expressway, SAP NetWeaver, and Broadcom VMware vCenter. Dark Reading ties the vCenter zero-day to a China-nexus group tracked as "Armory Castle," which reportedly had its next exploit staged before the last patch cycle even closed. This is the familiar vCenter pattern: compromise the hypervisor management plane, and the attacker owns everything hosted beneath it, quietly. If your vCenter is internet-reachable or sitting on a flat management network, assume you are already in scope. The espionage angle means dwell time matters more than smash-and-grab noise, so absence of alerts is not reassurance.

## Today's Action
- Patch vCenter, Cisco Expressway, SAP NetWeaver, and Apache Roller now against the four KEV CVEs; prioritize vCenter and the 9.8 Roller deserialization bug.
- Pull vCenter off any internet-facing path and restrict management access to a jump host or dedicated admin VLAN.
- Hunt vCenter for unexpected SSO accounts, new SSH sessions, modified vpxd logs, and rogue scheduled tasks dating back weeks, not days.
- Rotate vCenter and ESXi credentials and SSO service account secrets after confirming no active intrusion.
- Treat Armory Castle as a persistence-focused actor: review backups and snapshots for integrity before relying on them for recovery.

## Resources

Verified links for the CVEs mentioned above: official advisories, and a live search for public detection rules if any exist yet.

- **CVE-2026-129448**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-129448) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-129448)

*Patch the hypervisor or hand someone the keys to every VM you own.*

## Related

- [Stolen Fireworks AI Key Trojanized Anthropic's Official Claude Code Extension](/itsalreadywhen/2026/11/15/issue-021/)
- [North Korea's TraderTraitor Pulls Off a $6.43 Billion Binance Heist](/itsalreadywhen/2026/11/01/issue-019/)
- [ShinyHunters Hacked Clop, Then Robbed the Ransoms Twice](/itsalreadywhen/2026/09/27/issue-015/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*