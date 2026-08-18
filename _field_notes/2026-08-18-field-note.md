---
layout: field_note
title: "Field Note — August 18, 2026"
date: 2026-08-18
summary: "Actively exploited Ray RCE and Windows Task Host flaw hit CISA KEV, while two critical unauthenticated bugs (Forminator RCE and GitLab GraphQL) land with mass exposure."
---

## Today's Field Note
Three things worth your attention, all of them either being exploited now or trivial to weaponize. CISA added a critical Ray flaw to KEV with confirmed active exploitation, which matters because Ray clusters usually sit on juicy ML infrastructure with GPUs and data, and browser-based RCE means an operator's workstation is enough to get in. CISA also confirmed ransomware crews are now working the Windows Task Host bug flagged back in April, so if you deferred that patch, that window is closed. Meanwhile CVE-2026-15748 in Forminator (600,000+ installs, CVSS 9.8, unauthenticated file upload to RCE) and CVE-2026-19478 in GitLab (CVSS 9.4, unauthenticated GraphQL abuse to delete or modify public projects and user data) are both public and both the kind of thing that gets mass-scanned within days. None of these require a sophisticated adversary. They require you to be slow.

## Today's Action
- Patch the KEV Ray flaw immediately and confirm Ray dashboards and clients are not reachable from untrusted networks or workstations that browse the web.
- Apply the April Windows Task Host update on any host that missed it; treat it as active ransomware tooling, not a theoretical.
- Update Forminator across every WordPress instance now and hunt for unexpected PHP files in upload directories on sites that ran the vulnerable version.
- Upgrade GitLab CE/EE to the patched release and audit public project and user data changes for tampering.
- Cross-check all four against your asset inventory rather than trusting that "we don't run that."

## Resources

Verified links for the CVEs mentioned above: official advisories, and a live search for public detection rules if any exist yet.

- **CVE-2026-15748**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-15748) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-15748)
- **CVE-2026-19478**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-19478) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-19478)

*Nothing here is novel. That is the point.*

## Related

- [OpenAI's Own Models Broke Out of Their Sandbox and Hacked Hugging Face](/itsalreadywhen/2026/07/26/issue-006/)
- [SIM Cards, Gym Bots, and a Polish Turbine That Stopped Turning](/itsalreadywhen/2026/08/16/issue-009/)
- [An AI Test Model Broke Into Hugging Face and Nobody Noticed for a Weekend](/itsalreadywhen/2026/08/02/issue-007/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*