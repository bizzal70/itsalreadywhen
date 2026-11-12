---
layout: field_note
title: "Field Note — November 12, 2026"
date: 2026-11-12
summary: "N-able N-central zero-days, Apache HTTP/2 RCE, and a GitHub CI secret-stealer are all live threats demanding action today."
---

## Today's Field Note
Three things are already in motion. N-able pulled N-central offline after a researcher dropped 30-plus zero-days, and attackers started swinging at the unauthenticated ones before the hotfix landed, so RMM is once again the soft underbelly of every MSP downstream. Apache patched CVE-2026-119618, a critical mod_http2 RCE reachable by any unauthenticated attacker on versions 2.4.55 through 2.4.70 (fixed in 2.4.71), which ships inside RHEL whether you remember installing it or not. And an attacker burned 4,837 hijacked GitHub accounts to plant a CI secret-stealer across at least 1,806 repositories, meaning your cloud credentials may have walked out through a workflow you trust by default. None of this waits for your change window.

## Today's Action
- Patch Apache httpd to 2.4.71 now; if you cannot, disable mod_http2 or turn off HTTP/2 on internet-facing servers until you can.
- Apply N-able's N-central hotfix, confirm the platform is not internet-exposed, and hunt for admin-takeover indicators before trusting it again.
- Rotate every secret and cloud credential reachable from GitHub Actions CI, audit recent workflow runs, and enforce phishing-resistant MFA on all developer accounts.
- Review GitHub org audit logs for unexpected writes since Tuesday and revoke sessions/tokens on any account you cannot vouch for.
- Pull affected GitHub repos' commit history for injected workflow steps, not just the obvious ones.

## Resources

Verified links for the CVEs mentioned above: official advisories, and a live search for public detection rules if any exist yet.

- **CVE-2026-119618**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-119618) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-119618)

*Patch the thing that ships by default; that's the one they're counting on.*

## Related

- [ShinyHunters Hacked Clop, Then Robbed the Ransoms Twice](/itsalreadywhen/2026/09/27/issue-015/)
- [North Korea's TraderTraitor Pulls Off a $6.43 Billion Binance Heist](/itsalreadywhen/2026/11/01/issue-019/)
- [OpenAI's Own Models Broke Out of Their Sandbox and Hacked Hugging Face](/itsalreadywhen/2026/07/26/issue-006/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*