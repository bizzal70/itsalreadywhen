---
layout: field_note
title: "Field Note — October 05, 2026"
date: 2026-10-05
summary: "Two actively exploited bugs today: Citrix NetScaler zero-day CVE-2026-88779 and Rejetto HFS session-forgery flaw CVE-2026-61500, both with real-world attacks underway."
---

## Today's Field Note
Two internet-facing problems are live right now. Citrix is patching CVE-2026-88779, a memory overflow in NetScaler ADC and Gateway exploited as a zero-day, and SecurityWeek confirms attacks hitting appliances that were patched only days earlier for the previous round. That means NetScaler operators who thought they were current may not be. Separately, VulnCheck reports active exploitation of CVE-2026-61500 (CVSS 9.3) in Rejetto HFS, where a weak PRNG makes the session-cookie signing key predictable, handing attackers admin access and RCE. If you run HFS exposed to the internet, assume it is a target, not a maybe.

## Today's Action
- Apply Citrix emergency updates for CVE-2026-88779 on all NetScaler ADC and Gateway instances, including boxes you patched last week.
- Review NetScaler and SAML authentication logs for crashes, restarts, or anomalous sessions; terminate and rotate active sessions after patching.
- Patch or pull Rejetto HFS from internet exposure immediately; if public-facing HFS is non-essential, take it offline until fixed.
- Rotate HFS session-signing keys and invalidate existing admin sessions, since CVE-2026-61500 lets attackers forge them.
- Add both CVEs to your emergency-patch tracking and confirm closure, not just ticket creation.

## Resources

Verified links for the CVEs mentioned above: official advisories, and a live search for public detection rules if any exist yet.

- **CVE-2026-61500**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-61500) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-61500)
- **CVE-2026-88779**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-88779) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-88779)

*Patched days ago is not the same as patched today.*

## Related

- [ShinyHunters Hacked Clop, Then Robbed the Ransoms Twice](/itsalreadywhen/2026/09/27/issue-015/)
- [AI Agents Left 18,000 Posts on a Dead German Wiki to Coordinate Their Escape](/itsalreadywhen/2026/09/06/issue-012/)
- [OpenAI's Own Models Broke Out of Their Sandbox and Hacked Hugging Face](/itsalreadywhen/2026/07/26/issue-006/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*