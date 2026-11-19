---
layout: field_note
title: "Field Note — November 19, 2026"
date: 2026-11-19
summary: "Multiple unauthenticated RCE paths went live at once (nginx2root, Apache Roller under active exploitation, Java4Shell probing), and Microsoft's own Agent Framework PyPI package was trojanized."
---

## Today's Field Note

It's a bad day to run anything that listens. F5 shipped fixes for nginx2root (CVE-2026-123007), a decade-old HTTP/2 RCE in NGINX since 1.9.5, and PoCs are already public. Apache Roller's CVE-2026-129448 (CVSS 9.8, unauthenticated XML-RPC deserialization) is under active exploitation per the ASF, while Java4Shell exploitation attempts against OpenJDK are already showing up in GreyNoise, WatchTowr and Cloudflare telemetry. Separately, Microsoft's official Agent Framework package on PyPI was compromised with two trojanized versions built to lift cloud credentials from developer machines, so your build pipeline is now part of the attack surface too. None of these need a login, and the scanners do not care that you are busy.

## Today's Action

- Patch NGINX to 1.31.9 or 1.30.7 now (or disable HTTP/2 where you cannot), and treat any internet-facing NGINX with HTTP/2 as a priority given public PoCs for CVE-2026-123007.
- Take Apache Roller's XML-RPC endpoint offline or block it, then patch CVE-2026-129448 immediately; it is being exploited right now.
- Audit recent pip installs for the compromised Microsoft Agent Framework versions, pin to known-good releases, and rotate any cloud credentials that touched affected developer or CI hosts.
- Hunt for Java4Shell probing against OpenJDK runtimes using GreyNoise and WatchTowr indicators, and apply vendor advisories from Cisco, Elastic, Red Hat and Siemens as they land.
- Pull the four new CISA KEV entries (Synology DSM, LiteLLM, Apache Axis, REDCap) and confirm none are exposed on your perimeter.

## Resources

Verified links for the CVEs mentioned above: official advisories, and a live search for public detection rules if any exist yet.

- **CVE-2026-123007**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-123007) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-123007)
- **CVE-2026-129448**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-129448) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-129448)

*Everything's unauthenticated until proven otherwise. Patch accordingly.*

## Related

- [Stolen Fireworks AI Key Trojanized Anthropic's Official Claude Code Extension](/itsalreadywhen/2026/11/15/issue-021/)
- [North Korea's TraderTraitor Pulls Off a $6.43 Billion Binance Heist](/itsalreadywhen/2026/11/01/issue-019/)
- [ShinyHunters Hacked Clop, Then Robbed the Ransoms Twice](/itsalreadywhen/2026/09/27/issue-015/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*