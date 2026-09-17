---
layout: field_note
title: "Field Note — September 17, 2026"
date: 2026-09-17
summary: "Cisco patches an actively exploited max-severity ISE auth-bypass zero-day while a hard-coded credential flaw in Issabel PBX (CVE-2026-89026) is under attack."
---

## Today's Field Note

Two unauthenticated remote flaws are live in the wild today, and neither waits for your change window. Cisco shipped an emergency patch for a maximum-severity Identity Services Engine zero-day that lets remote attackers bypass authentication with crafted requests. ISE sits at the center of network access control, so a bypass there is a foothold into everything downstream. Separately, The Hacker News reports active exploitation of CVE-2026-89026 (CVSS 9.8), a hard-coded credential in the Issabel PBX framework that hands attackers unauthenticated OS command execution. VoIP boxes rarely get patched on time, which is exactly why they get owned.

## Today's Action

- Patch Cisco ISE immediately using the emergency fixed release. Do not wait for a maintenance window on an auth-bypass with confirmed exploitation.
- Pull ISE admin and API logs and hunt for anomalous or unauthenticated requests, then rotate any credentials or certs that touched the box.
- Inventory Issabel and any exposed PBX or unified comms frameworks. Get them off the public internet or behind a VPN today.
- Patch or isolate Issabel against CVE-2026-89026, and review outbound connections and shell activity from those hosts for signs of command execution.
- Confirm ISE and PBX management interfaces are not internet-facing, and restrict them to a management VLAN.

## Resources

Verified links for the CVEs mentioned above: official advisories, and a live search for public detection rules if any exist yet.

- **CVE-2026-89026**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-89026) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-89026)

*Two RCEs before lunch. It's already when.*

## Related

- [OpenAI's Own Models Broke Out of Their Sandbox and Hacked Hugging Face](/itsalreadywhen/2026/07/26/issue-006/)
- [An AI Test Model Broke Into Hugging Face and Nobody Noticed for a Weekend](/itsalreadywhen/2026/08/02/issue-007/)
- [Hundreds of AI Agents Broke Into 440 PaperCut Servers in One Campaign](/itsalreadywhen/2026/09/13/issue-013/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*