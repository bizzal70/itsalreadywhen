---
layout: field_note
title: "Field Note â€” July 30, 2026"
date: 2026-07-30
summary: "Cisco FMC static-credential zero-day (CVE-2026-20316) is in CISA KEV, Russia's Void Blizzard is riding an OWA zero-day for persistent mailbox access, and 30-plus Minnesota water utilities got hit in a coordinated OT attack."
---

## Today's Field Note
Three things are actually on fire today, the rest is AI think-pieces. Cisco's Secure FMC has a static-credential flaw, CVE-2026-20316, exploited in the wild and now sitting in CISA's KEV catalog. It lets an unauthenticated remote attacker log straight into your firewall management plane, which is exactly the box you do not want owned. Meanwhile Void Blizzard (Laundry Bear) is exploiting a Microsoft Exchange OWA zero-day to drop the OWAReaper backdoor and keep mailbox access after you rotate credentials, so your usual reset playbook does not evict them. And more than 30 Minnesota community water systems were hit in a coordinated OT attack, a reminder that small utilities remain soft targets.

## Today's Action
- Patch Cisco Secure FMC now for CVE-2026-20316 and confirm the management interface is not reachable from untrusted networks. Hunt logs for unexpected admin logins.
- Apply Microsoft's OWA fix and hunt for OWAReaper artifacts and rogue mailbox rules or persistence that survived a password reset. Rotating credentials alone will not clear Void Blizzard.
- If you run VMware, patch vCenter for CVE-2026-59309 (auth bypass, CVSS 9.8) while you are in the change window.
- Water and OT operators: verify remote-access paths to control systems, enforce MFA, and confirm manual failover works without the network.
- Review privileged account activity across firewall, mail, and OT management planes for the last two weeks.

## Resources

Verified links for the CVEs mentioned above: official advisories, and a live search for public detection rules if any exist yet.

- **CVE-2026-20316**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-20316) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-20316)
- **CVE-2026-59309**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-59309) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-59309)

*The credentials were static. The attackers were not.*

## Related

- [OpenAI's Own Models Broke Out of Their Sandbox and Hacked Hugging Face](/itsalreadywhen/2026/07/26/issue-006/)
- [Issue #004 — Week of July 12, 2026](/itsalreadywhen/2026/07/12/issue-004/)
- [The 11-byte packet that freezes an OpenSSL server for good](/itsalreadywhen/2026/07/19/issue-005/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*