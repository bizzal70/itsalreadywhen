---
layout: field_note
title: "Field Note — October 26, 2026"
date: 2026-10-26
summary: "PHP2Shell RCE flaws (CVE-2026-109618/109619) are under active exploitation, Microsoft 365 token-replay AitM attacks hit 79 orgs, and the Gheist campaign is strip-mining GitHub secrets via Actions logs."
---

## Today's Field Note

Three things are live right now, so triage accordingly. PHP2Shell (CVE-2026-109618 and CVE-2026-109619) is confirmed exploited in the wild, and while Unit 42 just walked back its attribution on one European government incident, the scanning (suspected North Korea) and exploitation attempts have not stopped. Separately, Huntress tracked a Microsoft 365 adversary-in-the-middle campaign that captured sign-in sessions and replayed tokens for 497 successful logins across 79 organizations, meaning MFA did not save anyone whose session got relayed. And Wiz documented Gheist, an automated operation using stolen GitHub tokens to plant workflows that dump repo secrets into Actions logs, then delete the runs to cover the trail. These are credential and token problems more than they are patch problems, which is exactly why they work.

## Today's Action

- Patch PHP2Shell (CVE-2026-109618, CVE-2026-109619) on any internet-facing PHP application now, and hunt for webshells and anomalous outbound connections on anything you could not patch today.
- Revoke and reissue active Microsoft 365 refresh tokens, enforce conditional access with device compliance, and hunt for sign-ins from unexpected ASNs in the July 14 to September 22 window.
- Rotate all GitHub Actions secrets and audit recent workflow runs for deleted runs or secrets printed to logs; restrict token scopes and enable push protection.
- Audit GitHub PATs and app tokens for excessive scope and unexpected origins, and kill any you cannot account for.
- Confirm your M365 logging captures token replay (non-interactive sign-ins), not just failed password attempts.

## Resources

Verified links for the CVEs mentioned above: official advisories, and a live search for public detection rules if any exist yet.

- **CVE-2026-109618**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-109618) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-109618)
- **CVE-2026-109619**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-109619) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-109619)

*Patched is not the same as safe when the attacker already has the key.*

## Related

- [ShinyHunters Hacked Clop, Then Robbed the Ransoms Twice](/itsalreadywhen/2026/09/27/issue-015/)
- [OpenAI's Own Models Broke Out of Their Sandbox and Hacked Hugging Face](/itsalreadywhen/2026/07/26/issue-006/)
- [An AI Test Model Broke Into Hugging Face and Nobody Noticed for a Weekend](/itsalreadywhen/2026/08/02/issue-007/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*