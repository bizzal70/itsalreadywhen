---
layout: field_note
title: "Field Note — September 08, 2026"
date: 2026-09-08
summary: "Adobe's max-severity Magento zero-day (CVE-2026-75650, StyleSmuggler) is under active exploitation, MikroTik RouterOS is being taken over via exposed SSH, and N-able N-central patched an exploited zero-day."
---

## Today's Field Note
The queue is thick with active exploitation today, so triage accordingly. Adobe's CVE-2026-75650 ("StyleSmuggler," CVSS 10.0) hits every version of Magento and Adobe Commerce, and Sansec traced in-the-wild abuse back to September 4, with attackers dropping a Rust backdoor, PHP web shells, and a Linux implant. In parallel, MikroTik RouterOS boxes with SSH exposed to the internet are being taken over without a password, and N-able quietly patched a critical N-central zero-day, telling admins to hunt for unfamiliar user accounts. Two of these three are your edge and your management plane, which is exactly where you do not want a foothold you missed.

## Today's Action
- Patch Adobe Commerce/Magento for CVE-2026-75650 now; if you cannot, apply Adobe's mitigation and treat any instance internet-facing since September 4 as potentially compromised.
- Hunt Magento hosts for the StyleSmuggler indicators: unexpected Rust binaries, new PHP files in web roots, and outbound connections consistent with the reported backdoor.
- Pull MikroTik RouterOS off the internet-facing SSH port, update to fixed firmware, and rotate credentials; assume compromise on any box that had SSH exposed.
- Apply N-able's N-central patch and audit for newly created or unrecognized admin accounts, then review recent job/task history for tampering.
- Given the shared theme, sweep all remote-management tooling (RMM, network gear, e-commerce admin) for anomalous accounts and sessions.

## Resources

Verified links for the CVEs mentioned above: official advisories, and a live search for public detection rules if any exist yet.

- **CVE-2026-75650**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-75650) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-75650)

*Your edge is somebody's foothold. Check it before they do.*

## Related

- [AI Agents Left 18,000 Posts on a Dead German Wiki to Coordinate Their Escape](/itsalreadywhen/2026/09/06/issue-012/)
- [OpenAI's Own Models Broke Out of Their Sandbox and Hacked Hugging Face](/itsalreadywhen/2026/07/26/issue-006/)
- [An AI Test Model Broke Into Hugging Face and Nobody Noticed for a Weekend](/itsalreadywhen/2026/08/02/issue-007/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*