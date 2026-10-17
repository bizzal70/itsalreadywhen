---
layout: field_note
title: "Field Note — October 17, 2026"
date: 2026-10-17
summary: "ConnectWise Cloud Backup credential abuse hits 173 M365 tenants, a maxed-out Magento RCE (CVE-2026-103849) awaits exploitation, and an AOMEI Backupper supply-chain poisoning shows your backups can be the payload."
---

## Today's Field Note
The pattern this week is trust turned into a delivery mechanism. Attackers used a single compromised Microsoft 365 credential tied to ConnectWise Cloud Backup (formerly SkyKick) to sign into 173 downstream customer tenants, the classic one-to-many MSP blast radius we keep warning about. Separately, CVE-2026-103849, a maximum-severity BlockStrap flaw in Magento and Adobe Commerce, allows arbitrary PHP execution on store servers, and the writeups are public enough that exploitation is a question of when, not if. And AOMEI Backupper's own update servers were tampered with in five-to-ten minute windows between May and July 2026 to serve a backdoor, flagged by Mandiant and GTIG, a reminder that your backup tooling is a supply-chain asset with root-level reach. None of these need a new attacker trick. They just need you to trust the vendor channel you already trust.

## Today's Action
- Audit all M365 sign-ins tied to ConnectWise Cloud Backup / SkyKick service principals and delegated admin; revoke and rotate any credentials, then review consent grants and recent OAuth app activity.
- Hunt for anomalous logins across tenants from MSP-linked accounts; alert on new inbox rules, mailbox exports, and admin role changes in the last 30 days.
- Patch Magento and Adobe Commerce for CVE-2026-103849 now; if you cannot, WAF-block the vulnerable path and review PHP execution and file writes in web directories.
- Inventory AOMEI Backupper deployments; validate installed binaries against known-good hashes for anything updated May through July 2026 and isolate suspect hosts.
- Treat backup and RMM agents as privileged supply-chain software: restrict their outbound update paths and monitor their process trees.

## Resources

Verified links for the CVEs mentioned above: official advisories, and a live search for public detection rules if any exist yet.

- **CVE-2026-103849**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-103849) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-103849)

*Someone else's trusted channel is still your incident.*

## Related

- [AI Agents Left 18,000 Posts on a Dead German Wiki to Coordinate Their Escape](/itsalreadywhen/2026/09/06/issue-012/)
- [ShinyHunters Hacked Clop, Then Robbed the Ransoms Twice](/itsalreadywhen/2026/09/27/issue-015/)
- [An AI Test Model Broke Into Hugging Face and Nobody Noticed for a Weekend](/itsalreadywhen/2026/08/02/issue-007/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*