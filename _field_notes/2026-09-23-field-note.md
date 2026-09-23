---
layout: field_note
title: "Field Note — September 23, 2026"
date: 2026-09-23
summary: "F5, Check Point, and Arista are all patching zero-days under active exploitation, and your perimeter security appliances are the target."
---

## Today's Field Note
Three network edge vendors dropped zero-day fixes on the same day, and all three are being exploited right now. F5's CVE-2026-94127 gives unauthenticated RCE on BIG-IP APM boxes configured as OAuth authorization servers, which means the thing issuing your access tokens is the thing getting owned. Check Point's CVE-2026-93616 lets an attacker run scripts on the Security Management Server (the box that controls your firewall policies) without logging in, exploited in targeted attacks since July 23. Arista is separately urging immediate patching of an exploited VCO zero-day for privileged internal access. The pattern is old and tired: the appliances you bought to defend the perimeter are the perimeter's softest entry point, and attackers know your patch cycle for them is slow.

## Today's Action
- Patch F5 BIG-IP for CVE-2026-94127 now if APM runs as an OAuth authorization server; F5 shipped engineering hotfixes. Rotate any tokens that box issued.
- Apply Check Point's emergency hotfix for CVE-2026-93616 on Security Management Servers, then audit for unauthorized script execution since July 23.
- Patch Arista VCO against the exploited zero-day and restrict management-plane access to known admin sources.
- Pull management interfaces of all three off any internet-facing or broadly reachable network segment.
- Hunt logs on these appliances for anomalous auth events and outbound connections, not just confirm the patch landed.

## Resources

Verified links for the CVEs mentioned above: official advisories, and a live search for public detection rules if any exist yet.

- **CVE-2026-93616**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-93616) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-93616)
- **CVE-2026-94127**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-94127) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-94127)

*The castle wall was always the door.*

## Related

- [OpenAI's Own Models Broke Out of Their Sandbox and Hacked Hugging Face](/itsalreadywhen/2026/07/26/issue-006/)
- [AI Agents Left 18,000 Posts on a Dead German Wiki to Coordinate Their Escape](/itsalreadywhen/2026/09/06/issue-012/)
- [Issue #004 — Week of July 12, 2026](/itsalreadywhen/2026/07/12/issue-004/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*