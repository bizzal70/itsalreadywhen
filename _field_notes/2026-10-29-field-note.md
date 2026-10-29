---
layout: field_note
title: "Field Note — October 29, 2026"
date: 2026-10-29
summary: "Active exploitation of a second Cisco ASA/FTD VPN zero-day, Palo Alto PHP2Shell management-interface attacks, and Volt Typhoon's Silent Train network driving multiple zero-day campaigns dominate today."
---

## Today's Field Note
Edge devices are the front line again, and today it is a pile-up. Attackers are hitting a second Cisco ASA/FTD Remote Access SSL VPN zero-day since August, this one letting unauthenticated attackers force a reload (read: denial of service, and likely a precursor to worse). Palo Alto confirmed active exploitation of the PHP2Shell flaws against internet-exposed management interfaces, with one chain rooting 25 servers and breaching a US government-affiliated network. Underneath it all, Lumen and Cisco Talos tied Volt Typhoon's "Silent Train" network to four zero-day campaigns, including KeyDrift malware stealing SD-WAN encryption keys via the February Catalyst flaw. The through-line is simple: your perimeter management planes are being treated as the actual target, not the moat.

## Today's Action
- Audit every Cisco ASA/FTD running Remote Access SSL VPN; apply Cisco's latest fixes immediately and disable the web VPN service where it is not required.
- Pull Palo Alto management interfaces off the public internet now, restrict to a jump host or management VLAN, and verify PHP2Shell patches are applied.
- Confirm Cisco Catalyst SD-WAN is patched against the February flaw; if it was exposed historically, assume KeyDrift may have touched it and rotate SD-WAN encryption keys.
- Hunt for Volt Typhoon living-off-the-land and Silent Train infrastructure: check SOHO/IoT egress patterns and anomalous management-plane logins against Lumen's IOCs.
- Treat any unexplained firewall reload as a signal, not a glitch, and preserve logs before they roll.

*The moat was never the point. They came for the gatehouse.*

## Related

- [Identity Is the New Perimeter](/itsalreadywhen/rtfm/2026/09/23/identity-is-the-new-perimeter/)
- [Asset Inventory: You Can't Protect What You Don't Know You Have](/itsalreadywhen/rtfm/2026/09/02/asset-inventory-you-can-t-protect-what-you-don-t-know-you-have/)
- [Segmentation as an Assumption, Not a Diagram](/itsalreadywhen/rtfm/2026/07/29/segmentation-as-an-assumption-not-a-diagram/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*