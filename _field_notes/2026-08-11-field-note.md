---
layout: field_note
title: "Field Note — August 11, 2026"
date: 2026-08-11
summary: "SonicWall SMA1000 flaws are under active ransomware exploitation, Gunra ransomware is chaining Fortinet and Schneider Electric bugs against critical infrastructure, and a maximum-severity Metabase SQL zero-day still has no CVE."
---

## Today's Field Note
Three items rose above the noise, and all three are already being used against people, not theorized about. CISA confirms ransomware crews are exploiting two SonicWall SMA1000 flaws, including a maximum-severity SSRF (CVE-2025-23006), which means your remote-access appliance is now the front door. Separately, US and South Korean agencies flagged Gunra ransomware hitting healthcare, finance, and government by chaining known Fortinet and Schneider Electric vulnerabilities, the usual story of unpatched edge gear becoming a beachhead. And Metabase has a maximum-severity SQL zero-day granting remote admin access with no CVE assigned yet, so your detection tooling has nothing to key on and the blast radius reaches every downstream data source it touches.

## Today's Action
- Patch SonicWall SMA1000 appliances against CVE-2025-23006 immediately, and hunt for SSRF indicators and unexpected outbound requests from the device.
- Cross-check your Fortinet and Schneider Electric inventory against the Gunra advisory and confirm the referenced CVEs are actually remediated, not just scheduled.
- Restrict Metabase to internal networks or behind VPN until a fix lands; assume the admin console is reachable equals compromised, and rotate any database credentials it holds.
- Pull logs for anomalous admin activity across all three (new accounts, off-hours queries, config changes) rather than trusting that patching alone closes the loop.
- Prioritize edge and remote-access gear in your patch queue this week over internal, less-exposed systems.

## Resources

Verified links for the CVEs mentioned above: official advisories, and a live search for public detection rules if any exist yet.

- **CVE-2025-23006**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2025-23006) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2025-23006)

*Nobody breaks down the door when you leave the appliance unlocked.*

## Related

- [Issue #004 — Week of July 12, 2026](/itsalreadywhen/2026/07/12/issue-004/)
- [OpenAI's Own Models Broke Out of Their Sandbox and Hacked Hugging Face](/itsalreadywhen/2026/07/26/issue-006/)
- [An AI Test Model Broke Into Hugging Face and Nobody Noticed for a Weekend](/itsalreadywhen/2026/08/02/issue-007/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*