---
layout: field_note
title: "Field Note — September 25, 2026"
date: 2026-09-25
summary: "Roundcube CVE-2026-48842 and CISA KEV additions for WSO2 and Adobe Commerce are all under active exploitation, and North Korea drained $351.6M from Bitget."
---

## Today's Field Note

Three separate confirmed-exploitation events landed at once, so triage accordingly. The Canadian Centre for Cyber Security flagged CVE-2026-48842, a pre-auth SQL injection in the Roundcube virtuser_query plugin (1.6.x before 1.6.16, 1.7.x before 1.7.1), being hit in the wild. CISA added two more to KEV on evidence of active attacks: CVE-2026-5430, a 9.8 path traversal in WSO2 API Control Plane, and an Adobe Commerce/Magento flaw. Meanwhile suspected North Korean actors drained $351.6M from Bitget hot and warm wallets after a backend compromise, a reminder that DPRK crews are still funding the regime through exchange infrastructure, not just phishing. None of this is theoretical today.

## Today's Action

- Patch Roundcube to 1.6.16 or 1.7.1 immediately; if you cannot, disable the virtuser_query plugin and check webmail logs for anomalous SQL error patterns and auth bypass attempts.
- Apply the WSO2 API Control Plane fix for CVE-2026-5430 and audit for path-traversal file reads; treat any internet-exposed WSO2 instance as a priority.
- Patch Adobe Commerce/Magento per the KEV entry and hunt for webshells and unexpected admin accounts on storefronts.
- Confirm both KEV items are logged against your BOD 22-01 remediation clock and report status.
- If you touch exchange or custody infrastructure, review backend service accounts and hot-wallet signing paths for the Bitget compromise pattern.

## Resources

Verified links for the CVEs mentioned above: official advisories, and a live search for public detection rules if any exist yet.

- **CVE-2026-48842**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-48842) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-48842)
- **CVE-2026-5430**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-5430) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-5430)

*Patch the three that are already being used against you; admire the rest later.*

## Related

- [AI Agents Left 18,000 Posts on a Dead German Wiki to Coordinate Their Escape](/itsalreadywhen/2026/09/06/issue-012/)
- [OpenAI's Own Models Broke Out of Their Sandbox and Hacked Hugging Face](/itsalreadywhen/2026/07/26/issue-006/)
- [SIM Cards, Gym Bots, and a Polish Turbine That Stopped Turning](/itsalreadywhen/2026/08/16/issue-009/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*