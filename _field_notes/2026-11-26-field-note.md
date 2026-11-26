---
layout: field_note
title: "Field Note — November 26, 2026"
date: 2026-11-26
summary: "Drupal, Palo Alto PAN-OS, and GeoServer are all under active exploitation right now, and 1Password confirmed a GitHub-based backend breach."
---

## Today's Field Note
Three live fires today. Drupal's earlier Fail2Install patch (CVE-2026-132165) left a gap, and the follow-up CVE-2026-136716 is already being exploited for site takeover, so if you patched once you are likely still exposed. Palo Alto is warning that attackers are chaining PHP2Shell and Fragnesia against PAN-OS boxes with internet-facing management interfaces, which is the oldest mistake in the book and still working. Two GeoServer flaws are being probed for unauthenticated RCE when chained. Separately, 1Password confirmed an attacker used a compromised employee GitHub account to push malicious code to backend services and exfiltrate customer records. Vaults were reportedly untouched, but source code and customer data walking out via a developer account is the supply chain story that keeps repeating.

## Today's Action
- Apply Drupal's latest core update for CVE-2026-136716 even if you already deployed the Fail2Install fix, then check logs for signs of takeover.
- Pull PAN-OS management interfaces off the public internet immediately and hunt for PHP2Shell and Fragnesia chaining indicators.
- Patch or isolate internet-facing GeoServer instances and review access logs for RCE probing.
- Audit GitHub for employee accounts with write access to production or CI pipelines, enforce phishing-resistant MFA, and review recent commits to backend repos.
- Cross-reference the new CISA KEV additions (Mitel MiCollab, Juniper, Vates, Danfoss) against your asset inventory and prioritize the exposed ones.

## Resources

Verified links for the CVEs mentioned above: official advisories, and a live search for public detection rules if any exist yet.

- **CVE-2026-132165**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-132165) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-132165)
- **CVE-2026-136716**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-136716) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-136716)

*Patch the patch. It's already when.*

## Related

- [North Korea's TraderTraitor Pulls Off a $6.43 Billion Binance Heist](/itsalreadywhen/2026/11/01/issue-019/)
- [ShinyHunters Hacked Clop, Then Robbed the Ransoms Twice](/itsalreadywhen/2026/09/27/issue-015/)
- [Stolen Fireworks AI Key Trojanized Anthropic's Official Claude Code Extension](/itsalreadywhen/2026/11/15/issue-021/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*