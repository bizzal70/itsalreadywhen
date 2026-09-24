---
layout: field_note
title: "Field Note — September 24, 2026"
date: 2026-09-24
summary: "WordPress CVE-2026-87902, Check Point VPN CVE-2026-85102, and MikroTik's MikroTrick chain are all under active exploitation with unauthenticated RCE."
---

## Today's Field Note
Three unauthenticated RCE stories collided today, and all three are already being worked. WordPress CVE-2026-87902 (CVSS 9.2, path traversal to RCE) went from disclosure to mass exploitation in hours, with attackers now writing shell-execution files to disk. Check Point confirmed active exploitation of CVE-2026-85102, a pre-auth RCE in the Security Gateway VPN certificate handler, which means the box guarding your perimeter is the way in. And CERT Polska's MikroTrick chain (CVE-2026-67279 plus CVE-2026-86060) gives full admin over internet-exposed RouterOS boxes with no password, no key, and logs going back weeks, so assume the routers were owned before you read this. Edge and web infrastructure is the target set right now, not the endpoint.

## Today's Action
- Patch WordPress against CVE-2026-87902 immediately, then hunt for newly written .php files in template and upload paths and check web logs for path-traversal include attempts.
- Apply Check Point's fix for CVE-2026-85102 on Security Gateway; if you cannot patch now, restrict VPN certificate-handling exposure and review authentication logs for anomalies.
- Update MikroTik RouterOS to close CVE-2026-67279 and CVE-2026-86060, disable internet-facing SSH, and treat any exposed router as compromised: rotate credentials and inspect scripts, scheduler, and firewall rules.
- Cross-check all three against CISA KEV and prioritize any internet-exposed instances over internal ones today.
- Pull external attack-surface data and confirm you actually know every WordPress site, VPN gateway, and MikroTik device facing the internet.

## Resources

Verified links for the CVEs mentioned above: official advisories, and a live search for public detection rules if any exist yet.

- **CVE-2026-67279**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-67279) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-67279)
- **CVE-2026-85102**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-85102) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-85102)
- **CVE-2026-86060**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-86060) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-86060)
- **CVE-2026-87902**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-87902) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-87902)

*The perimeter was never a wall. It was a door with your name on the lock.*

## Related

- [OpenAI's Own Models Broke Out of Their Sandbox and Hacked Hugging Face](/itsalreadywhen/2026/07/26/issue-006/)
- [AI Agents Left 18,000 Posts on a Dead German Wiki to Coordinate Their Escape](/itsalreadywhen/2026/09/06/issue-012/)
- [Hundreds of AI Agents Broke Into 440 PaperCut Servers in One Campaign](/itsalreadywhen/2026/09/13/issue-013/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*