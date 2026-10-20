---
layout: field_note
title: "Field Note — October 20, 2026"
date: 2026-10-20
summary: "Four live supply-chain compromises (OVHcloud CLI, Rank Math PRO, AOMEI, Plex2Shell) plus active ClickFix exploitation of a Siemens DLL flaw mean trusted updaters are the attack surface today."
---

## Today's Field Note
The theme today is the update channel turning hostile. Attackers hijacked a contributor's GitHub account to poison five OVHcloud CLI releases (live 94 minutes, long enough), backdoored the Rank Math PRO WordPress plugin with a self-restoring implant between Oct 15-16, and tampered with AOMEI Backupper's update servers to push a RAT. Separately, CVE-2026-110936 (CVSS 8.4) in Siemens Software Center is under active exploitation via ClickFix lures pairing a signed binary with a malicious DLL, and Plex2Shell exploitation began one day after the PoC dropped. The common thread: the signed, trusted thing you auto-update is the delivery vehicle. Assume anything pulled through these channels in the affected windows is tainted until proven otherwise.

## Today's Action
- Audit any machine that ran the OVHcloud CLI pulled Oct 19 (12:47-14:21 UTC); rotate every secret on that disk, those downloads were secret-stealers.
- Treat any WordPress site that installed Rank Math PRO 3.0.123 (Oct 15 20:02 to Oct 16 07:12 UTC) as compromised: pull it, hunt for the backdoor, rotate admin and DB creds.
- Reimage hosts that updated AOMEI Backupper in the tampering window; the RAT grants remote access, cleanup is not enough.
- Patch Siemens Software Center for CVE-2026-110936 now and hunt for rogue DLLs sideloaded next to the signed binary; brief staff on ClickFix "paste this command" lures.
- Patch Plex Media Server against the Plex2Shell chain today; PoC is public and exploitation is live.

## Resources

Verified links for the CVEs mentioned above: official advisories, and a live search for public detection rules if any exist yet.

- **CVE-2026-110936**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-110936) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-110936)

*Your updater has a login. Someone else used it.*

## Related

- [ShinyHunters Hacked Clop, Then Robbed the Ransoms Twice](/itsalreadywhen/2026/09/27/issue-015/)
- [An AI Test Model Broke Into Hugging Face and Nobody Noticed for a Weekend](/itsalreadywhen/2026/08/02/issue-007/)
- [AI Agents Left 18,000 Posts on a Dead German Wiki to Coordinate Their Escape](/itsalreadywhen/2026/09/06/issue-012/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*