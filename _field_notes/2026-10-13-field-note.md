---
layout: field_note
title: "Field Note — October 13, 2026"
date: 2026-10-13
summary: "GitLab's CVSS 10.0 unauth RCE, an actively exploited SonicWall SMA 1000 SSRF, and a real-world Danfoss refrigeration controller attack lead today's signal."
---

## Today's Field Note

Two patch-now items and one reminder that OT is not hypothetical. GitLab shipped fixes for a CVSS 10.0 flaw in CE and EE allowing an unauthenticated user to run arbitrary code via a crafted regex in CI/CD processing, which is as bad as it reads for anyone self-hosting. Meanwhile a maximum-severity SSRF in SonicWall SMA 1000 appliances is under active attack, putting internet-facing SonicWall edge gear back in the familiar crosshairs. And attackers reached into Danfoss refrigeration controllers at hundreds of French supermarkets (reportedly via remote maintenance access) and warmed the units until stores dumped the stock. The through-line: your attack surface includes the vendor's remote management path and your source-control server, not just the firewall.

## Today's Action

- Patch self-hosted GitLab immediately to the fixed CE/EE releases; if you cannot, restrict CI/CD exposure and audit pipeline logs for anomalous regex-triggered jobs.
- Treat SonicWall SMA 1000 as compromised until proven otherwise: apply SonicWall's fix, review access logs for SSRF-style internal requests, and rotate credentials behind the appliance.
- Inventory every device reachable through third-party remote maintenance (Danfoss controllers, BMS, HVAC) and confirm who holds that access, with MFA and IP allowlisting on those paths.
- Verify Progress MarkLogic Server is on 11.3.7 or 12.1.0 and review delegated management role assignments for privilege-escalation paths (two critical flaws among 31).
- Pull edge-appliance and source-control systems into your "assume active exploitation" monitoring tier for the week, not the monthly review.

*It was already when you read the changelog.*

## Related

- [Least Privilege, Actually Enforced](/itsalreadywhen/rtfm/2026/07/01/least-privilege-actually-enforced/)
- [The 11-byte packet that freezes an OpenSSL server for good](/itsalreadywhen/2026/07/19/issue-005/)
- [Anthropic Killed Claude's Internet After It Attacked Real Websites](/itsalreadywhen/2026/10/11/issue-017/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*