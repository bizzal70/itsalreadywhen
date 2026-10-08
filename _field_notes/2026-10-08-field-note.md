---
layout: field_note
title: "Field Note — October 08, 2026"
date: 2026-10-08
summary: "FortiBleed attackers are actively locking admins out of FortiGate VPNs, SonicWall shipped a CVSS 10.0 pre-auth fix for SMA1000, and LMCache has an unpatched RCE with no fix available."
---

## Today's Field Note
The FBI is confirming what the telemetry already showed: FortiBleed operators are inside exposed FortiGate SSL VPNs, creating accounts and deleting legitimate ones to lock admins out of their own gear. If you run Fortinet edge and you are waiting for a maintenance window, you have already lost that argument. Meanwhile SonicWall patched a pre-auth SSRF in SMA1000 rated CVSS 10.0 (no confirmed exploitation yet, but that is a before, not a never), and LMCache (the cache layer in front of vLLM and friends) has an unauthenticated RCE over its ZeroMQ multiprocess mode with no fixed version shipped. The last one matters because nobody treats their LLM accelerator as attack surface, which is exactly why it is attack surface.

## Today's Action
- Audit FortiGate admin and local user accounts now for unknown additions or deletions, and pull SSL VPN auth logs for the last 30 days. Assume compromise on anything internet-facing and unpatched.
- Rotate FortiGate admin credentials and VPN secrets, enforce MFA on admin access, and restrict management interfaces to known IPs.
- Apply the SonicWall SMA1000 hotfixes covering the CVSS 10.0 SSRF and the three accompanying flaws before weekend drift sets in.
- For LMCache: pull multiprocess mode off any network-reachable interface, bind ZeroMQ to localhost only, and firewall the cache server until a fix lands.
- Confirm your edge devices actually log somewhere you can read them, not just locally where an attacker can wipe them.

*Patch the box before someone else changes the locks.*

## Related

- [Default Credentials and Configuration Drift](/itsalreadywhen/rtfm/2026/08/19/default-credentials-and-configuration-drift/)
- [Logging Without Anyone Reading the Logs](/itsalreadywhen/rtfm/2026/07/15/logging-without-anyone-reading-the-logs/)
- [Change Management as a Security Control](/itsalreadywhen/rtfm/2026/10/07/change-management-as-a-security-control/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*