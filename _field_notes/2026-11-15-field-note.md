---
layout: field_note
title: "Field Note — November 15, 2026"
date: 2026-11-15
summary: "A stolen Fireworks AI key let attackers trojanize Anthropic's official Claude Code extension on Cursor's marketplace, and the US disrupted a North Korean crypto theft op."
---

## Today's Field Note
The supply chain for AI tooling just took a predictable hit. Cursor confirmed an attacker used an access key exposed in a breach at Fireworks AI to copy data from a read-only store and push a trojanized version of Anthropic's official Claude Code extension through Cursor's marketplace. This is the second-order blast radius we keep warning about: one vendor's leaked credential becomes another vendor's malicious package becomes your developers' endpoints running attacker code with full IDE context. Separately, the US disrupted a North Korean social engineering campaign (tracked as FaceStealer) tied to over $400 million in crypto theft, a reminder that DPRK operators are still running the long con through fake identities and job lures. Treat your AI extensions like any other third-party dependency, because that is exactly what they are.

## Today's Action
- Audit installed Cursor extensions, confirm the Claude Code extension version and pull any copy sourced during the compromise window.
- Rotate any API keys or tokens that passed through developer IDEs running the trojanized extension, and check egress logs for unexpected outbound calls.
- Inventory your exposure to Fireworks AI, revoke and reissue any access keys you have issued to or shared with them.
- Treat marketplace extensions as code dependencies: pin versions, review publisher integrity, and alert on unexpected updates.
- Refresh hiring and contractor identity checks against DPRK FaceStealer tradecraft (fake personas, remote-work lures, crypto wallet targeting).

*Your IDE is now part of your attack surface. It always was.*

## Related

- [Stolen Fireworks AI Key Trojanized Anthropic's Official Claude Code Extension](/itsalreadywhen/2026/11/15/issue-021/)
- [Least Privilege, Actually Enforced](/itsalreadywhen/rtfm/2026/07/01/least-privilege-actually-enforced/)
- [Privileged Access Management Beyond the Vault](/itsalreadywhen/rtfm/2026/10/28/privileged-access-management-beyond-the-vault/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*