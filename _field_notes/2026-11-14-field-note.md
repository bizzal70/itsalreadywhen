---
layout: field_note
title: "Field Note — November 14, 2026"
date: 2026-11-14
summary: "Check Point gateways are being exploited via PHP2Shell to wipe ESXi hosts, and PostgreSQL patched a 22-year-old RCE bug with a public CVE."
---

## Today's Field Note
Two items worth your attention before you clock out. Attackers are hitting vulnerable Check Point Security Gateways with PHP2Shell, landing on the appliance, then pivoting to VMware ESXi hosts to deploy a wiper. This is not ransomware with a payment path, it is destruction, so there is no negotiation and no decryptor waiting at the end. Separately, PostgreSQL shipped fixes for 52 flaws including CVE-2026-6460 (CVSS 8.8), a type-confusion bug that lets any user who can create objects run code with the OS rights of the database process, a latent problem sitting quietly for 22 years. The Check Point activity is the one that ends your week badly if you ignore it.

## Today's Action
- Confirm your Check Point Security Gateways are patched to current and audit for PHP2Shell indicators and unexpected web shells on gateway appliances.
- Treat ESXi as a blast radius: verify management interfaces are isolated, lockdown mode is on, and you have tested, offline backups of VM datastores.
- Patch PostgreSQL to the fixed release now, and remember CVE-2026-6460 is not fully closed until you rebuild any C-language extensions on the server.
- Revoke unnecessary CREATE privileges on PostgreSQL instances to shrink the set of users who can trigger the flaw.
- Review gateway-to-hypervisor network paths and kill any route that lets a compromised perimeter device reach ESXi directly.

## Resources

Verified links for the CVEs mentioned above: official advisories, and a live search for public detection rules if any exist yet.

- **CVE-2026-6460**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-6460) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-6460)

*Wipers do not send invoices. Patch like you believe that.*

## Related

- [ShinyHunters Hacked Clop, Then Robbed the Ransoms Twice](/itsalreadywhen/2026/09/27/issue-015/)
- [North Korea's TraderTraitor Pulls Off a $6.43 Billion Binance Heist](/itsalreadywhen/2026/11/01/issue-019/)
- [AI Agents Left 18,000 Posts on a Dead German Wiki to Coordinate Their Escape](/itsalreadywhen/2026/09/06/issue-012/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*