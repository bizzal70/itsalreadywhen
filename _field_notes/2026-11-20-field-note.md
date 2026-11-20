---
layout: field_note
title: "Field Note — November 20, 2026"
date: 2026-11-20
summary: "China-linked Armory Castle exploited VMware vCenter CVE-2026-123890 as a zero-day since September, F5 shipped emergency BIG-IP RCE patches, and critical NGINX 'nginx2root' bugs now have a public root chain."
---

## Today's Field Note
The big one is VMware vCenter. CVE-2026-123890 (CVSS 9.8) is an auth bypass in the Directory Service that Google attributes to Armory Castle (formerly UNC5221), who have been quietly riding it as a zero-day since early September 2026. vCenter is the keys to the whole virtual estate, so "unauthorized admin access" means ESXi hosts, snapshots, and every VM you run. Broadcom has patches out and lists no workaround, which means patching is the plan. Alongside it, F5 pushed emergency fixes for five critical BIG-IP RCE/DoS flaws, and researchers published a chained "nginx2root" exploit (two critical NGINX bugs plus a Linux kernel bug) that lands unauthenticated remote code execution and escalates to root.

## Today's Action
- Patch VMware vCenter to Broadcom's fixed branch today. There is no workaround, so treat internet-facing or broadly reachable vCenter as compromised until proven otherwise.
- Hunt vCenter for signs of exploitation back to early September: anomalous admin logins, new accounts, and unexpected vpxd/Directory Service activity tied to Armory Castle (UNC5221) TTPs.
- Apply F5's emergency BIG-IP updates for the five critical flaws and restrict management interface access to a trusted network only.
- Inventory NGINX builds and patch against the nginx2root pair; a public chain to root now exists, so prioritize external-facing servers.
- Isolate management planes (vCenter, BIG-IP, NGINX admin) from general network reachability and confirm MFA on all admin paths.

## Resources

Verified links for the CVEs mentioned above: official advisories, and a live search for public detection rules if any exist yet.

- **CVE-2026-123890**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-123890) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-123890)

*Attackers had your hypervisor since September. The patch is just you catching up.*

## Related

- [North Korea's TraderTraitor Pulls Off a $6.43 Billion Binance Heist](/itsalreadywhen/2026/11/01/issue-019/)
- [Stolen Fireworks AI Key Trojanized Anthropic's Official Claude Code Extension](/itsalreadywhen/2026/11/15/issue-021/)
- [ShinyHunters Hacked Clop, Then Robbed the Ransoms Twice](/itsalreadywhen/2026/09/27/issue-015/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*