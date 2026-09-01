---
layout: field_note
title: "Field Note — September 01, 2026"
date: 2026-09-01
summary: "PaperCut NG/MF zero-days (CVE-2026-82078, CVE-2026-81578) are now in CISA KEV and driving data theft, while JFrog Artifactory auth bypass CVE-2026-82329 is under active exploitation days after disclosure."
---

## Today's Field Note

Two print servers and a package registry are the story today, and all three are the kind of software that sits quietly in the middle of everything. PaperCut NG and MF zero-days (CVE-2026-82078 and CVE-2026-81578) have escalated from patched flaws to active intrusions with confirmed data theft, and CISA has added both to the KEV catalog. Separately, JFrog Artifactory's authentication bypass CVE-2026-82329 is being exploited in the wild, exploitation starting just days after public disclosure, which is roughly how long it takes attackers to read a changelog. Artifactory is a supply-chain chokepoint: a foothold there means access to your build artifacts and credentials, not just one box. None of this is exotic, which is exactly why it works.

## Today's Action

- Patch PaperCut NG/MF now and treat any unpatched instance as already compromised; hunt for reverse-tunnel activity and unexpected admin sessions before you close the door.
- Upgrade JFrog Artifactory to the fixed release addressing CVE-2026-82329, and rotate any tokens, API keys, or CI/CD credentials that instance could reach.
- Confirm both PaperCut CVEs against your KEV-driven remediation SLA; the federal deadline is your excuse to move today.
- Pull PaperCut and Artifactory management interfaces off the public internet entirely, then verify with an external scan rather than a config review.
- Review build pipeline logs for anomalous artifact pulls or new service accounts created around the disclosure window.

## Resources

Verified links for the CVEs mentioned above: official advisories, and a live search for public detection rules if any exist yet.

- **CVE-2026-81578**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-81578) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-81578)
- **CVE-2026-82078**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-82078) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-82078)
- **CVE-2026-82329**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-82329) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-82329)

*Patch Tuesday is a schedule; exploitation is not.*

## Related

- [OpenAI's Own Models Broke Out of Their Sandbox and Hacked Hugging Face](/itsalreadywhen/2026/07/26/issue-006/)
- [Issue #004 — Week of July 12, 2026](/itsalreadywhen/2026/07/12/issue-004/)
- [An AI Test Model Broke Into Hugging Face and Nobody Noticed for a Weekend](/itsalreadywhen/2026/08/02/issue-007/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*