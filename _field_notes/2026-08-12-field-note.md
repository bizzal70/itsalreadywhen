---
layout: field_note
title: "Field Note — August 12, 2026"
date: 2026-08-12
summary: "Active exploitation of VMware vCenter (CVE-2026-59310) and Cisco ASA/FTD (CVE-2026-20349), plus a Windows afd.sys zero-day (CVE-2026-68820) in this month's Patch Tuesday."
---

## Today's Field Note
Two edge-facing bugs are already being turned against people, and both sit in the boxes you use to keep others out. QUIRSO reports active exploitation of CVE-2026-59310, the 9.8 directory-traversal RCE in Broadcom VMware vCenter, giving attackers persistent remote access to the thing that controls your entire virtual estate. Cisco confirms CVE-2026-20349 in ASA and FTD is being used in the wild to crash firewalls remotely without authentication, so treat it as a live availability threat, not a theoretical one. Meanwhile Microsoft's August load buries one that matters: CVE-2026-68820, a use-after-free in afd.sys already exploited for SYSTEM. Ignore the 400-CVE headline and patch the three things attackers are actually touching.

## Today's Action
- Patch VMware vCenter for CVE-2026-59310 now, then hunt for traversal-based access and unexpected persistence, since exploitation predates your patch window.
- Apply Cisco's ASA and FTD fix for CVE-2026-20349; if you cannot patch immediately, watch for repeated device crashes and restrict HTTP-facing management exposure.
- Deploy August's Windows updates prioritizing CVE-2026-68820 (afd.sys) on internet-adjacent and high-value hosts first.
- Segregate and monitor vCenter and firewall management interfaces so they are not reachable from general network space or the internet.
- Note the ShieldBreak PoC (CVE-2026-50656 bypass) and SharePoint CVE-2026-55040; confirm your Defender and SharePoint builds are current before those move from PoC to payload.

## Resources

Verified links for the CVEs mentioned above: official advisories, and a live search for public detection rules if any exist yet.

- **CVE-2026-20349**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-20349) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-20349)
- **CVE-2026-50656**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-50656) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-50656)
- **CVE-2026-55040**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-55040) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-55040)
- **CVE-2026-59310**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-59310) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-59310)
- **CVE-2026-68820**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-68820) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-68820)

*Patch the three they're touching, not the four hundred they're not.*

## Related

- [OpenAI's Own Models Broke Out of Their Sandbox and Hacked Hugging Face](/itsalreadywhen/2026/07/26/issue-006/)
- [An AI Test Model Broke Into Hugging Face and Nobody Noticed for a Weekend](/itsalreadywhen/2026/08/02/issue-007/)
- [Issue #004 — Week of July 12, 2026](/itsalreadywhen/2026/07/12/issue-004/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*