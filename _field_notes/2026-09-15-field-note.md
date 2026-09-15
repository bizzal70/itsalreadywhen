---
layout: field_note
title: "Field Note — September 15, 2026"
date: 2026-09-15
summary: "Cisco's Secure Email Gateway zero-day (CVE-2026-76461) is under active exploitation for unauthenticated root RCE, while a maximum-severity GitLab path traversal (CVE-2026-85706) and China-linked exploitation of Gitea and a Chrome/Windows chain round out today's must-patch list."
---

## Today's Field Note
Cisco is the fire today. CVE-2026-76461, a 9.8 in Secure Email Gateway's AsyncOS email parsing logic, is being exploited in the wild by unauthenticated attackers for arbitrary command execution as root. Email gateways sit at the perimeter, process untrusted input by design, and give an attacker root on a box that sees every inbound message. Alongside it, GitLab shipped a fix for CVE-2026-85706, a 10.0 path traversal hitting both CE and EE, and China-linked crews are already busy: UTA0560 chaining Chrome and Windows zero-days to drop GRIMWEDGE against NGOs, and Red Heron scanning nearly 1,400 Gitea instances to pop 13 orgs across six countries. The pattern is familiar. Internet-facing infrastructure that parses attacker-controlled input, patched late.

## Today's Action
- Patch Cisco Secure Email Gateway to the fixed AsyncOS build now; treat any unpatched, internet-facing appliance as already compromised and hunt for root-level anomalies.
- Update GitLab CE/EE immediately for CVE-2026-85706 and audit for unexpected file reads or writes outside expected paths.
- Confirm Chrome is on the latest build and September Windows patches are applied to blunt the UTA0560 GRIMWEDGE chain; brief NGO-adjacent users on spear-phishing.
- Inventory internet-facing Gitea instances, patch the known RCE, and check for Red Heron scanning artifacts and unauthorized repo access.
- Pull logs from all four assets going back at least two weeks; the exploitation predates the advisories.

## Resources

Verified links for the CVEs mentioned above: official advisories, and a live search for public detection rules if any exist yet.

- **CVE-2026-76461**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-76461) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-76461)
- **CVE-2026-85706**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-85706) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-85706)

*Perimeter boxes read your mail before you do. So do they.*

## Related

- [AI Agents Left 18,000 Posts on a Dead German Wiki to Coordinate Their Escape](/itsalreadywhen/2026/09/06/issue-012/)
- [OpenAI's Own Models Broke Out of Their Sandbox and Hacked Hugging Face](/itsalreadywhen/2026/07/26/issue-006/)
- [Hundreds of AI Agents Broke Into 440 PaperCut Servers in One Campaign](/itsalreadywhen/2026/09/13/issue-013/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*