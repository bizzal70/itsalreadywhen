---
layout: field_note
title: "Field Note — September 03, 2026"
date: 2026-09-03
summary: "CISA flags seven exploited flaws including a 10.0 SonicWall SMA 1000 SSRF zero-day, while JFrog Artifactory and Sangoma Switchvox are under active exploitation."
---

## Today's Field Note
The edge is on fire again, same as always. CISA added seven bugs to KEV, led by CVE-2026-83548, a CVSS 10.0 SSRF in SonicWall SMA 1000 that unauthenticated attackers are using for RCE, the third round of SMA 1000 zero-days this summer alone. Separately, CVE-2026-82329 in JFrog Artifactory is being exploited to forge admin tokens, meaning your build pipeline and artifact repo may already belong to someone else. And CVE-2026-9586 in Sangoma Switchvox, an unauthenticated SQLi, is dropping reverse shells on VoIP boxes right now. None of these need credentials, all three are internet-facing, and the patches exist. This is a triage day, not a planning day.

## Today's Action
- Patch SonicWall SMA 1000 immediately for CVE-2026-83548, and hunt for SSRF-driven RCE indicators before assuming you were fast enough.
- Update JFrog Artifactory against CVE-2026-82329, then audit admin tokens and access tokens for anything you did not create.
- Patch Sangoma Switchvox for CVE-2026-9586 and review VoIP hosts for reverse shells and unexpected outbound connections.
- Work the full CISA KEV additions from Wednesday, not just the three named here, and confirm none of the seven touch your edge.
- Pull internet-facing management interfaces (SonicWall, Artifactory, Switchvox) off the open internet or behind a VPN where feasible.

## Resources

Verified links for the CVEs mentioned above: official advisories, and a live search for public detection rules if any exist yet.

- **CVE-2026-82329**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-82329) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-82329)
- **CVE-2026-83548**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-83548) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-83548)
- **CVE-2026-9586**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-9586) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-9586)

*Patch the edge or the edge patches you.*

## Related

- [OpenAI's Own Models Broke Out of Their Sandbox and Hacked Hugging Face](/itsalreadywhen/2026/07/26/issue-006/)
- [An AI Test Model Broke Into Hugging Face and Nobody Noticed for a Weekend](/itsalreadywhen/2026/08/02/issue-007/)
- [700 OpenAI Agents Coordinated a Real Attack on Hugging Face](/itsalreadywhen/2026/08/30/issue-011/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*