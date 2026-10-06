---
layout: field_note
title: "Field Note — October 06, 2026"
date: 2026-10-06
summary: "Rejetto HFS servers are under active scanning for CVE-2026-61500, Atlassian ships a 9.3 pre-auth file read bug across 8 products, and Microsoft patches an out-of-band Exchange privilege escalation."
---

## Today's Field Note
Three patch-now items surfaced today, and one is already past the theoretical stage. Attackers are actively scanning for CVE-2026-61500 in Rejetto HFS, a weak signing key flaw that enables session forgery, account takeover, and RCE. Scanning is the warmup; HFS boxes tend to sit exposed and forgotten, which is exactly the profile that gets owned. Alongside that, Atlassian disclosed CVE-2026-21589 (CVSS 9.3), an unauthenticated file read across eight self-hosted Data Center products, and Microsoft pushed an out-of-band fix for CVE-2026-96940, a weak-authorization privilege escalation in Exchange Server that lets an authenticated attacker reach other users' mailboxes. None of these need novel tradecraft. They need you to still be unpatched.

## Today's Action
- Patch or take offline any internet-facing Rejetto HFS instance now; rotate signing keys and invalidate sessions after CVE-2026-61500 remediation.
- Inventory self-hosted Atlassian Data Center products (Jira, Confluence, et al.) and apply the CVE-2026-21589 fix; restrict web root exposure where patching lags.
- Apply Microsoft's out-of-band update for CVE-2026-96940 on Exchange Server, prioritizing externally reachable and admin-adjacent accounts.
- Pull web logs on HFS and Atlassian hosts for anomalous requests to known file paths and forged-session activity predating the patch.
- Confirm no leftover exposed HFS servers exist via external scan; the forgotten ones are the ones that bite.

## Resources

Verified links for the CVEs mentioned above: official advisories, and a live search for public detection rules if any exist yet.

- **CVE-2026-21589**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-21589) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-21589)
- **CVE-2026-61500**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-61500) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-61500)
- **CVE-2026-96940**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-96940) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-96940)

*File it, patch it, forget you ever had free time.*

## Related

- [ShinyHunters Hacked Clop, Then Robbed the Ransoms Twice](/itsalreadywhen/2026/09/27/issue-015/)
- [AI Agents Left 18,000 Posts on a Dead German Wiki to Coordinate Their Escape](/itsalreadywhen/2026/09/06/issue-012/)
- [An AI Test Model Broke Into Hugging Face and Nobody Noticed for a Weekend](/itsalreadywhen/2026/08/02/issue-007/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*