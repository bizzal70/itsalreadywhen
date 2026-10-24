---
layout: field_note
title: "Field Note — October 24, 2026"
date: 2026-10-24
summary: "CISA confirms active exploitation of critical flaws in Collabora Online and Arista VeloCloud, while PHP ships only mitigations for an unpatched RCE."
---

## Today's Field Note
CISA added two critical bugs to KEV on confirmed in-the-wild exploitation: CVE-2026-110447 (CVSS 9.2) in Collabora Online's built-in CODE Server, and a companion flaw in Arista VeloCloud Orchestrator. Both are edge-adjacent, internet-facing systems that tend to live outside normal patch cycles, which is exactly why attackers like them. Meanwhile the PHP security team shipped mitigation guidance but no patch for a new RCE affecting non-default configurations, so the usual "just update" reflex does not apply here. KEV entries carry federal remediation deadlines, but the reason to move today is that exploitation is already happening, not the paperwork. Inventory first, because you cannot patch what you forgot you were running.

## Today's Action
- Patch Collabora Online CODE Server for CVE-2026-110447 immediately, or pull exposed instances off the public internet until you can.
- Update Arista VeloCloud Orchestrator to the fixed release and audit VCO access logs for signs of prior compromise.
- Review your PHP deployments for the non-default configurations flagged in the new RCE advisory and apply the PHP team's mitigations, since no patch exists yet.
- Cross-check both new KEV CVEs against your external attack surface scans and confirm nothing is sitting exposed and unpatched.
- Hunt backward on the above systems for post-exploitation artifacts, not just forward patching, assuming you were already in scope.

## Resources

Verified links for the CVEs mentioned above: official advisories, and a live search for public detection rules if any exist yet.

- **CVE-2026-110447**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-110447) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-110447)

*The deadline on the KEV is for auditors. The attackers do not wait for it.*

## Related

- [ShinyHunters Hacked Clop, Then Robbed the Ransoms Twice](/itsalreadywhen/2026/09/27/issue-015/)
- [AI Agents Left 18,000 Posts on a Dead German Wiki to Coordinate Their Escape](/itsalreadywhen/2026/09/06/issue-012/)
- [700 OpenAI Agents Coordinated a Real Attack on Hugging Face](/itsalreadywhen/2026/08/30/issue-011/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*