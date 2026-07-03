---
layout: field_note
title: "Field Note — July 03, 2026"
date: 2026-07-03
summary: "Anubis affiliates are exploiting Citrix Bleed 2 (CVE-2025-5777) for ransomware access while FortiBleed actors monetize thousands of compromised Fortinet firewalls with a Nextcloud zero-day."
---

## Today's Field Note
Citrix is the story again, and it is the same story it always is. Anubis ransomware affiliates are exploiting Citrix Bleed 2 (CVE-2025-5777) for initial access, pairing memory disclosure with legitimate RMM tooling and hands-on-keyboard lateral movement. Separately, a fresh CitrixBleed variant on NetScaler is being exploited immediately after disclosure using public PoC code that pulls arbitrary memory from HTTP responses. On the perimeter's other flank, the FortiBleed crew has parked in thousands of Fortinet firewalls and is now selling that access to Inc and Lynx, stacking on a Nextcloud zero-day for good measure. If your edge is Citrix or Fortinet, assume someone is already reading your memory.

## Today's Action
- Patch NetScaler ADC/Gateway for CVE-2025-5777 and the newly disclosed variant now, then terminate all active sessions to kill tokens grabbed before you patched.
- Hunt for FortiBleed indicators on Fortinet firewalls: unexpected admin sessions, config changes, and new local accounts. Rotate all firewall and VPN credentials.
- Audit RMM tooling (AnyDesk, ScreenConnect, Atera, and similar) for unauthorized installs, a known Anubis pattern.
- Patch your Nextcloud instances and review logs for anomalous access tied to the zero-day being chained by these actors.
- Treat any Citrix or Fortinet box that was exposed pre-patch as compromised until proven otherwise, and check for staged exfil.

## Resources

Verified links for the CVEs mentioned above: official advisories, and a live search for public detection rules if any exist yet.

- **CVE-2025-5777**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2025-5777) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2025-5777)

*Your edge device is not a perimeter. It is a doorway with your name on the deed.*