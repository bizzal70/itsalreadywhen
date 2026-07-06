---
layout: field_note
title: "Field Note — July 06, 2026"
date: 2026-07-06
summary: "Opera GX patched a zero-click flaw that let malicious sites auto-install mods and exfiltrate page data, while Google and the FBI disrupted the NetNut residential proxy botnet."
---

## Today's Field Note
Opera GX shipped a fix for a flaw that let any malicious website silently install a browser add-on with zero clicks, then read specific data off the pages you visit. The researchers' proof of concept reconstructed a signed-in user's full Gmail address from a single visit, which tells you the primitive is real and not theoretical. Opera says it found no evidence of exploitation, but the PoC is public now and the gap between disclosure and adaptation is short. Separately, Google, the FBI, and partners took down NetNut, a residential proxy network riding on millions of hijacked consumer and IoT devices. Disruptions like this are temporary; the operators rebuild, and unpatched devices in your fleet are the raw material for whatever comes next.

## Today's Action
- Push the Opera GX update to every managed endpoint today and confirm the build number, do not trust auto-update to have run.
- Audit installed Opera GX mods and extensions across your fleet, flag anything installed without a recorded user action.
- Treat any Gmail or session data accessed on Opera GX in recent weeks as potentially exposed, rotate where practical.
- Pull outbound connections from IoT and consumer-grade devices on your network, hunt for residential proxy beaconing tied to NetNut infrastructure.
- Restrict browser extension installation via policy so a website cannot trigger it silently on any browser you support.

*The exploit was public before you finished reading the changelog.*