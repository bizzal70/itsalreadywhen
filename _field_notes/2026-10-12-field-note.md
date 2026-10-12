---
layout: field_note
title: "Field Note — October 12, 2026"
date: 2026-10-12
summary: "Two maximum-severity flaws (Bricksforge CVE-2026-85097 and SonicWall CVE-2026-102255) are under active exploitation, both days after disclosure."
---

## Today's Field Note
Two critical flaws jumped straight from disclosure to active exploitation, and neither waited for you to finish your coffee. Patchstack confirms attackers are hitting CVE-2026-85097, a CVSS 10.0 bug in the Bricksforge WordPress plugin that hands unauthenticated users arbitrary PHP execution, which means full site takeover with no credentials required. Meanwhile SonicWall's CVE-2026-102255, a pre-auth SSRF, is being exploited within days of its advisory, continuing the firm's long streak of edge devices being first through the door. WordPress plugins and perimeter appliances remain the two softest targets in most environments, and both are lit up right now. This is a patch-today situation, not a next-maintenance-window one.

## Today's Action
- Update the Bricksforge plugin to the patched release immediately, or deactivate and remove it if you cannot patch now.
- Audit WordPress upload directories and webroots for unexpected PHP files and recently modified timestamps tied to CVE-2026-85097.
- Apply SonicWall's fix for CVE-2026-102255 and restrict management interfaces to trusted IPs only.
- Review SonicWall and firewall logs for anomalous outbound requests consistent with SSRF probing of internal services and metadata endpoints.
- Rotate credentials and API keys reachable from any appliance or site you cannot confirm was patched before exploitation began.

## Resources

Verified links for the CVEs mentioned above: official advisories, and a live search for public detection rules if any exist yet.

- **CVE-2026-102255**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-102255) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-102255)
- **CVE-2026-85097**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-85097) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-85097)

*You didn't get owned at disclosure. You got owned three days later, while you were "evaluating."*

## Related

- [ShinyHunters Hacked Clop, Then Robbed the Ransoms Twice](/itsalreadywhen/2026/09/27/issue-015/)
- [OpenAI's Own Models Broke Out of Their Sandbox and Hacked Hugging Face](/itsalreadywhen/2026/07/26/issue-006/)
- [AI Agents Left 18,000 Posts on a Dead German Wiki to Coordinate Their Escape](/itsalreadywhen/2026/09/06/issue-012/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*