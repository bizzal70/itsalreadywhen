---
layout: field_note
title: "Field Note — November 17, 2026"
date: 2026-11-17
summary: "The Optimizely supply chain hack planted card skimmers and iOS exploit kits on 178 sites, while ScreenConnect and a Fireworks AI breach keep the attack surface hot."
---

## Today's Field Note

Someone turned Optimizely Web Experimentation into a delivery truck. By abusing a flaw in the experimentation platform, an attacker planted malicious code inside the scripts that customer sites load from Optimizely, hitting visitors to at least 178 organizations including CNN, Fox News, BBC, Zoom, Salesforce, GitLab, and Equifax yesterday. The payload skimmed cards, stole crypto, and dropped iOS exploit kits, so this is live client-side compromise, not a theoretical advisory. Meanwhile ConnectWise confirms ScreenConnect attacks continue against on-prem environments where third-party extensions stay enabled (patch to 26.6.5+), and the Fireworks AI breach has now rippled into Uber (150,000 drivers) and a poisoned Cursor/Claude Code extension. The common thread is dependency. You are exposed through things you did not build and cannot patch.

## Today's Action

- Audit every third-party script loaded from Optimizely/Optimizely Web Experimentation. Pull or pin it, and check Report URI or your own logs for the injected code served yesterday.
- Deploy or tighten Content Security Policy and Subresource Integrity on checkout and login pages so unexpected external scripts cannot execute.
- Update ScreenConnect technician clients to 26.6.5 or later and disable unused third-party extensions on on-prem instances now.
- Rotate any credentials, API keys, or OAuth tokens tied to Fireworks AI, Cursor, or Claude Code extensions, and review recent extension installs.
- Hunt your card-entry pages for skimmer indicators and scan payment logs for anomalous outbound beacons over the last 48 hours.

*You own the risk you inherit, even when you never signed for it.*

## Related

- [Stolen Fireworks AI Key Trojanized Anthropic's Official Claude Code Extension](/itsalreadywhen/2026/11/15/issue-021/)
- [Patch Cadence vs. Patch Theater](/itsalreadywhen/rtfm/2026/07/08/patch-cadence-vs-patch-theater/)
- [North Korea's TraderTraitor Pulls Off a $6.43 Billion Binance Heist](/itsalreadywhen/2026/11/01/issue-019/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*