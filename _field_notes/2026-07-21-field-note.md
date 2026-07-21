---
layout: field_note
title: "Field Note — July 21, 2026"
date: 2026-07-21
summary: "Three flaws are under active exploitation this week: WordPress wp2shell (CVE-2026-63030 + CVE-2026-60137), ServiceNow AI Platform CVE-2026-6875, and the Palo Alto GlobalProtect bypass now driving Qilin ransomware."
---

## Today's Field Note
The theme today is speed. WordPress wp2shell (CVE-2026-63030 chained with CVE-2026-60137) went from disclosure to mass exploitation in roughly three days, and with millions of sites in scope, "later" is not a plan. ServiceNow's CVE-2026-6875 (CVSS 9.5, unauthenticated RCE via sandbox escape) is following the same curve, in-the-wild exploitation confirmed by Defused Cyber days after patches shipped. Meanwhile Qilin has adopted the critical PAN-OS GlobalProtect auth bypass, so your edge VPN is now a ransomware on-ramp per Arctic Wolf. None of these are theoretical, and all three sit on internet-facing surfaces that attackers scan by default.

## Today's Action
- Patch WordPress plugin/core to close CVE-2026-63030 and CVE-2026-60137 now, then hunt for web shells and unexpected admin users on any site not patched before the weekend.
- Apply the ServiceNow fix for CVE-2026-6875 and audit AI Platform access logs for anomalous script execution since disclosure.
- Confirm PAN-OS GlobalProtect is patched against the auth bypass, and check for Qilin precursors (new accounts, lateral movement, staged encryptors) if your appliance was exposed.
- Pull edge appliances off the open internet where you can; management interfaces on VPN gear should not be reachable from anywhere.
- Prioritize by exposure, not CVSS alone: internet-facing WordPress, ServiceNow, and Palo Alto instances go to the front of the queue today.

## Resources

Verified links for the CVEs mentioned above: official advisories, and a live search for public detection rules if any exist yet.

- **CVE-2026-60137**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-60137) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-60137)
- **CVE-2026-63030**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-63030) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-63030)
- **CVE-2026-6875**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-6875) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-6875)

*Disclosure is the starting gun, not the deadline. Move accordingly.*

## Related

- [Field Note — July 20, 2026](/itsalreadywhen/field-notes/2026/07/20/field-note/)
- [The 11-byte packet that freezes an OpenSSL server for good](/itsalreadywhen/2026/07/19/issue-005/)
- [Field Note — July 19, 2026](/itsalreadywhen/field-notes/2026/07/19/field-note/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*