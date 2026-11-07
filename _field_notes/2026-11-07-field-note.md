---
layout: field_note
title: "Field Note — November 07, 2026"
date: 2026-11-07
summary: "SonicWall's CVE-2026-19868 SAML/MFA bypass and OpenSSH's SSHole (CVE-2026-123158) are both under active exploitation, with firewalls and exposed Linux boxes taking fire within hours."
---

## Today's Field Note
Two edge-facing auth bypasses are live, and they share a theme: your MFA assumption is only as good as the login path nobody audited. SonicWall patched CVE-2026-19868 in SonicOS, which lets an attacker who holds credentials for one login method walk past SAML checks, including SAML-enforced MFA, and it is already being exploited through SSL-VPN. Separately, OpenSSH's SSHole (CVE-2026-123158, CVSS 8.1) is drawing exploitation attempts within hours of disclosure, popping root on a honeypot by signing into passwordless accounts on musl-based Linux with PAM disabled. Neither is exotic; both are the kind of thing that turns a Tuesday into a long weekend. Patch the perimeter first, then go find the accounts you forgot had no password.

## Today's Action
- Apply SonicWall's SonicOS updates now (all seven fixes), prioritizing internet-facing SSL-VPN appliances, and review SAML/VPN auth logs for logins from unexpected methods.
- Patch OpenSSH on any musl-based Linux hosts (Alpine and similar); confirm PAM status and eliminate or lock accounts with no password set.
- Rotate SonicWall VPN credentials and reconfirm MFA enforcement end to end, not just at the SAML layer.
- Hunt now: check honeypot and edge logs for SSH root access to passwordless accounts and for SSL-VPN sessions that skipped expected MFA prompts.
- If you run Chainalysis tooling, treat all customer credentials and tokens as compromised and rotate immediately.

## Resources

Verified links for the CVEs mentioned above: official advisories, and a live search for public detection rules if any exist yet.

- **CVE-2026-123158**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-123158) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-123158)
- **CVE-2026-19868**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-19868) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-19868)

*You locked the front door. SSHole walked in through the account you forgot to give a password.*

## Related

- [North Korea's TraderTraitor Pulls Off a $6.43 Billion Binance Heist](/itsalreadywhen/2026/11/01/issue-019/)
- [AI Agents Left 18,000 Posts on a Dead German Wiki to Coordinate Their Escape](/itsalreadywhen/2026/09/06/issue-012/)
- [ShinyHunters Hacked Clop, Then Robbed the Ransoms Twice](/itsalreadywhen/2026/09/27/issue-015/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*