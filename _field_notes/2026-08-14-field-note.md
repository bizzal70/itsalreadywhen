---
layout: field_note
title: "Field Note — August 14, 2026"
date: 2026-08-14
summary: "Two active exploitation campaigns dominate today: VMware vCenter CVE-2026-59310 is being used for reverse SSH persistence, while an unpatched GeoServer SQLi zero-day is under attack."
---

## Today's Field Note
Two things are being exploited in the wild right now, and both reward speed. CVE-2026-59310, a critical RCE in the VMware vCenter Syslog Server, is being hit in a global campaign that drops a reverse SSH tool for persistence, which means patching alone will not evict an attacker who already landed. Separately, an unpatched GeoServer zero-day (SQL injection leading to RCE) is under active exploitation with no fix yet, so anything internet-facing running it is a live target. Add the Akira affiliate trick of rebooting into Safe Mode with Networking to kill EDR before they act, and the theme of the day is simple: assume the patch is late and the persistence is already in place.

## Today's Action
- Patch VMware vCenter for CVE-2026-59310 now, then hunt for reverse SSH connections, new SSH keys, and unexpected outbound sessions from vCenter hosts. Patching is not enough if they are already in.
- Inventory internet-facing GeoServer instances, restrict access, and monitor for SQLi and RCE indicators until a vendor fix ships. Consider taking exposed instances offline.
- Configure EDR with tamper protection and Safe Mode monitoring, and alert on unexpected reboots into Safe Mode with Networking to counter the Akira technique.
- For orgs touched by RingCentral or ShipMonk/Trezor breaches: force credential resets where relevant and warn users to expect targeted phishing using leaked names, addresses, and phone numbers.
- Review third-party logistics and CRM vendors (Beacon's leaked AWS key came from public JS build artifacts) and scan your own build outputs for exposed secrets.

## Resources

Verified links for the CVEs mentioned above: official advisories, and a live search for public detection rules if any exist yet.

- **CVE-2026-59310**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-59310) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-59310)

*The patch is the start of the investigation, not the end of it.*

## Related

- [OpenAI's Own Models Broke Out of Their Sandbox and Hacked Hugging Face](/itsalreadywhen/2026/07/26/issue-006/)
- [An AI Test Model Broke Into Hugging Face and Nobody Noticed for a Weekend](/itsalreadywhen/2026/08/02/issue-007/)
- [The Week AI Agents Started Breaking Into Real Companies](/itsalreadywhen/2026/08/09/issue-008/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*