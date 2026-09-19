---
layout: field_note
title: "Field Note — September 19, 2026"
date: 2026-09-19
summary: "Cisco ISE hits a perfect 10 auth bypass zero-day, Orkes Conductor has a pre-auth RCE under active exploitation, and CISA adds three Linux kernel flaws to KEV with public exploits floating around."
---

## Today's Field Note
Three things demand attention before you close the laptop today. Cisco ISE is carrying CVE-2026-76460, an authentication bypass that scored a full 10.0, which means anyone reaching the API endpoint can walk in without credentials. Orkes Conductor (versions 3.21.21 before 3.30.2) has CVE-2026-58138, an unauthenticated RCE that Fortinet confirms is already being exploited in the wild. And CISA added three Linux kernel flaws to KEV, including CVE-2025-39682 in the TLS receive path, right as a researcher dropped working local-root exploit code for four kernel bugs. None of these is theoretical, and ISE plus Conductor are exactly the kind of infrastructure that quietly holds the keys to everything else.

## Today's Action
- Patch Cisco ISE immediately for CVE-2026-76460 and confirm its API endpoints are not exposed to untrusted networks.
- Upgrade Orkes Conductor to 3.30.2 or later, and hunt for signs of exploitation given confirmed in-the-wild activity.
- Cross-check your Linux fleet against the three KEV kernel CVEs (starting with CVE-2025-39682) and prioritize internet-facing and multi-user hosts.
- Treat the public local-root exploit code as live: patch kernels now, do not assume "local only" buys you time.
- Review ISE and Conductor access logs for anomalous authentication or job activity over the past week.

## Resources

Verified links for the CVEs mentioned above: official advisories, and a live search for public detection rules if any exist yet.

- **CVE-2025-39682**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2025-39682) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2025-39682)
- **CVE-2026-58138**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-58138) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-58138)
- **CVE-2026-76460**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-76460) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-76460)

*File it under "already happened," because it probably has.*

## Related

- [OpenAI's Own Models Broke Out of Their Sandbox and Hacked Hugging Face](/itsalreadywhen/2026/07/26/issue-006/)
- [AI Agents Left 18,000 Posts on a Dead German Wiki to Coordinate Their Escape](/itsalreadywhen/2026/09/06/issue-012/)
- [An AI Test Model Broke Into Hugging Face and Nobody Noticed for a Weekend](/itsalreadywhen/2026/08/02/issue-007/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*