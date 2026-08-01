---
layout: field_note
title: "Field Note — August 01, 2026"
date: 2026-08-01
summary: "CISA warns of active PLC attacks on U.S. water utilities, Adform's ad script was poisoned to swap crypto wallet addresses, and Adobe patched a CVSS 10.0 auth flaw in Campaign Classic."
---

## Today's Field Note
Three items worth your attention. CISA is warning of a real uptick in attacks on internet-exposed PLCs across U.S. water and wastewater systems, and Minnesota is investigating incidents officials are tying to Iranian actors with a track record here. This is the same default-credential, exposed-HMI story we keep telling, except the targets treat water. Separately, ad-tech firm Adform got its JavaScript poisoned on July 27 in a clipboard-swap supply chain attack that rewrote copied crypto wallet addresses on any site loading the script, a reminder that third-party JS is code you run without reading. And Adobe patched CVE-2026-48449, a CVSS 10.0 incorrect-authorization flaw in Campaign Classic allowing code execution without user interaction, so treat any internet-facing ACC instance as urgent.

## Today's Action
- Inventory internet-exposed PLCs and HMIs in OT (water utilities especially), pull them off the public internet or behind VPN, and kill default and shared credentials per CISA's guidance.
- Patch Adobe Campaign Classic now for CVE-2026-48449, prioritizing any internet-reachable ACC instance, and review authorization logs for anomalous access.
- If you loaded Adform's ad script on July 27, notify users who may have copied wallet addresses, and audit any crypto transactions from that window.
- Add Subresource Integrity (SRI) or CSP controls on third-party scripts, particularly ad-tech, so a poisoned file cannot silently execute.
- Watch for Iranian-nexus OT TTPs in water-sector telemetry and enable alerting on unauthorized PLC logic changes.

## Resources

Verified links for the CVEs mentioned above: official advisories, and a live search for public detection rules if any exist yet.

- **CVE-2026-48449**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-48449) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-48449)

*The pipes were exposed long before the water got dirty.*

## Related

- [OpenAI's Own Models Broke Out of Their Sandbox and Hacked Hugging Face](/itsalreadywhen/2026/07/26/issue-006/)
- [Issue #004 — Week of July 12, 2026](/itsalreadywhen/2026/07/12/issue-004/)
- [The 11-byte packet that freezes an OpenSSL server for good](/itsalreadywhen/2026/07/19/issue-005/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*