---
layout: field_note
title: "Field Note â€” July 31, 2026"
date: 2026-07-31
summary: "Iran-linked actors hit 30-plus Minnesota water systems while unauthenticated RCE flaws land in TeamCity and VMware, both prime targets for the same playbook."
---

## Today's Field Note
Three things worth your attention, and they rhyme. A likely Iran-backed actor compromised more than 30 community water systems in Minnesota by hitting internet-exposed PLCs, and CISA is now telling the whole water sector to get their controllers off the public internet. Meanwhile JetBrains patched CVE-2026-63077, an unauthenticated RCE in TeamCity On-Premises exploitable through the agent polling protocol, and Broadcom shipped fixes for three critical VMware flaws (auth bypass, RCE, and VM escape) across vCenter, ESX, Workstation, and Fusion. Build servers and hypervisors are exactly what ransomware crews go for after initial access, and exposed OT is exactly what nation-state actors go for. None of this needs a novel technique. It needs you to have left something facing the internet.

## Today's Action
- Inventory internet-exposed OT now: PLCs, HMIs, and any water/wastewater controllers. Pull them behind a VPN or firewall and change default credentials per CISA's guidance.
- Patch TeamCity On-Premises for CVE-2026-63077 today, and if it was internet-facing, treat it as potentially compromised (audit agents, tokens, and build artifacts).
- Apply Broadcom's VMware updates to vCenter, ESX, Workstation, and Fusion; prioritize any management interface reachable outside your admin network.
- Separately, brief helpdesk and staff on the Microsoft Teams vishing to Chaos ransomware pattern: no one grants remote access off an inbound Teams call.
- Hunt for the fake-update lure family (AtlasRAT, DPRK macOS Contagious Interview) in proxy and EDR logs.

## Resources

Verified links for the CVEs mentioned above: official advisories, and a live search for public detection rules if any exist yet.

- **CVE-2026-63077**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-63077) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-63077)

*Nothing here was clever. That's the part that should bother you.*

## Related

- [OpenAI's Own Models Broke Out of Their Sandbox and Hacked Hugging Face](/itsalreadywhen/2026/07/26/issue-006/)
- [Issue #004 — Week of July 12, 2026](/itsalreadywhen/2026/07/12/issue-004/)
- [The 11-byte packet that freezes an OpenSSL server for good](/itsalreadywhen/2026/07/19/issue-005/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*