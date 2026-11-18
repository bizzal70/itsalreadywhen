---
layout: field_note
title: "Field Note — November 18, 2026"
date: 2026-11-18
summary: "Java4Shell (CVE-2026-114938) and the Perforce Puppet RCE (CVE-2026-115731) are both under active exploitation, while a supply-chain poisoning of Microsoft's agent-framework PyPI package steals cloud creds on every Python start."
---

## Today's Field Note

Two pre-auth RCEs are already being worked in the wild, and they hit things you almost certainly run. CVE-2026-114938 (Java4Shell, CVSS 8.1) is an OpenJDK out-of-bounds write that Calif demonstrated against Jira, Jenkins, Confluence, and Keycloak on AVX-512 VBMI capable x86-64 chips. VulnCheck notes real-world RCE takes per-target work, but CISA already added it to KEV and so did they for CVE-2026-115731, the Perforce Puppet flaw (CVSS 9.4) where any CA-signed agent cert yields code execution on the server. Separately, Microsoft's agent-framework PyPI package was trojanized (versions 1.26.1 and 1.26.2, pushed 33 minutes apart on Nov 17) to run a credential stealer on every Python start. Patch the two, purge the third.

## Today's Action

- Patch Java4Shell per vendor: update Jira, Confluence, Jenkins, and Keycloak now, and inventory any JDK 17.0.6+ on AVX-512 VBMI hardware. OpenJDK fixes are out.
- Apply the Perforce Puppet update for CVE-2026-115731 and rotate/revoke agent certificates issued by your CA; treat any CA-signed cert as a potential foothold.
- Pin agent-framework below 1.26.1, rip out 1.26.1/1.26.2 from any environment, and rotate every cloud credential reachable from hosts that installed them.
- Hunt for outbound beacons from CI/build boxes and Python runtime starts post-Nov 17; the stealer fires on import, not just execution.
- Confirm both CVEs against your KEV-driven remediation deadlines before patch windows slip past the weekend.

## Resources

Verified links for the CVEs mentioned above: official advisories, and a live search for public detection rules if any exist yet.

- **CVE-2026-114938**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-114938) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-114938)
- **CVE-2026-115731**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-115731) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-115731)

*It's not whether the cert was trusted. It's who you trusted to sign it.*

## Related

- [Stolen Fireworks AI Key Trojanized Anthropic's Official Claude Code Extension](/itsalreadywhen/2026/11/15/issue-021/)
- [ShinyHunters Hacked Clop, Then Robbed the Ransoms Twice](/itsalreadywhen/2026/09/27/issue-015/)
- [An AI Test Model Broke Into Hugging Face and Nobody Noticed for a Weekend](/itsalreadywhen/2026/08/02/issue-007/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*