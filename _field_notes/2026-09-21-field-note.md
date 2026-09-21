---
layout: field_note
title: "Field Note — September 21, 2026"
date: 2026-09-21
summary: "Colorado water utilities had OT settings tampered with, and CISA flagged three actively exploited Linux kernel flaws."
---

## Today's Field Note
Two things move today. First, attackers reached into Colorado water utilities and changed real equipment settings, disabled remote access and alarms, and altered pumping cycles. This is not reconnaissance, it is hands on the controls, and the disabled alarms mean the operators may not have seen it in real time. Second, CISA is warning on three actively exploited Linux kernel vulnerabilities enabling denial of service, memory disclosure, and memory modification, which puts a lot of unglamorous fleet infrastructure in scope. Neither is theoretical. Both have a clock on them.

## Today's Action
- Pull OT remote access to your SCADA and pumping systems back behind VPN with MFA, and verify every alarm and remote-access path is actually enabled and reporting.
- Review OT engineering-workstation and HMI logs for unauthorized setpoint, pump-cycle, or alarm-configuration changes going back 30 days.
- Cross-check the three CISA-flagged Linux kernel CVEs against your inventory and prioritize patching internet-adjacent and multi-tenant hosts first.
- Where kernel patches cannot land today, restrict local access and monitor for the DoS and memory-disclosure behavior described.
- Confirm you have current, tested backups of OT configurations so you can restore known-good setpoints if tampering is found.

*Someone already turned the alarms off. Go check yours.*

## Related

- [Least Privilege, Actually Enforced](/itsalreadywhen/rtfm/2026/07/01/least-privilege-actually-enforced/)
- [Backup Integrity vs. Backup Existence](/itsalreadywhen/rtfm/2026/08/12/backup-integrity-vs-backup-existence/)
- [Asset Inventory: You Can't Protect What You Don't Know You Have](/itsalreadywhen/rtfm/2026/09/02/asset-inventory-you-can-t-protect-what-you-don-t-know-you-have/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*