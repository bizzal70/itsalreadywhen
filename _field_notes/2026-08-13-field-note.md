---
layout: field_note
title: "Field Note — August 13, 2026"
date: 2026-08-13
summary: "Lazarus is burning a Windows zero-day (CVE-2026-68820) against defense firms while SharePoint (CVE-2026-55040) falls to public PoC exploitation."
---

## Today's Field Note
Two active-exploitation stories worth your morning. Lazarus Group is using a Windows privilege-escalation zero-day (CVE-2026-68820) in fresh Operation Dream Job activity, per Check Point, dropping a new backdoor on defense and aerospace targets across France, Germany, Brazil, and India. It was patched this Patch Tuesday, so the window to close it is now. Separately, CVE-2026-55040 (CVSS 9.1), the SharePoint auth-bypass Microsoft fixed back in July, is now being exploited in the wild after a public PoC dropped, exactly the outcome CISA warned about. If you deferred either patch, that decision has expired. Also keep an eye on CVE-2026-59310, the critical vCenter directory-traversal RCE now drawing attacker interest.

## Today's Action
- Deploy this month's Windows cumulative update to patch CVE-2026-68820; prioritize defense, aerospace, and any internet-adjacent workstations.
- Apply the July SharePoint update for CVE-2026-55040 to all on-prem Server and Subscription Edition instances; audit auth logs for anomalous access since the PoC dropped.
- Hunt for Operation Dream Job indicators (spearphish-to-job-lure delivery, unexpected SYSTEM shells, new backdoor persistence) using Check Point's published IOCs.
- Patch vCenter for CVE-2026-59310 and confirm management interfaces are off the public internet.
- For SharePoint, if patching lags, restrict external access and rotate machine keys after remediation.

## Resources

Verified links for the CVEs mentioned above: official advisories, and a live search for public detection rules if any exist yet.

- **CVE-2026-55040**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-55040) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-55040)
- **CVE-2026-59310**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-59310) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-59310)
- **CVE-2026-68820**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-68820) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-68820)

*Nobody defers a patch on purpose. They just run out of tomorrows.*

## Related

- [OpenAI's Own Models Broke Out of Their Sandbox and Hacked Hugging Face](/itsalreadywhen/2026/07/26/issue-006/)
- [An AI Test Model Broke Into Hugging Face and Nobody Noticed for a Weekend](/itsalreadywhen/2026/08/02/issue-007/)
- [The 11-byte packet that freezes an OpenSSL server for good](/itsalreadywhen/2026/07/19/issue-005/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*