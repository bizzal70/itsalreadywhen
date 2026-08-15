---
layout: field_note
title: "Field Note — August 15, 2026"
date: 2026-08-15
summary: "Attackers are exploiting a public macOS Screen Sharing auth-bypass PoC to drop Monero miners, while a service provider flaw led to €30M in Commerzbank fraud."
---

## Today's Field Note
The Dutch NCSC confirms active exploitation of a macOS Screen Sharing authentication bypass, now that working exploit code is public. Right now the payload is just a Monero miner, which is the polite version of "someone has code execution on your fleet and hasn't decided what to do with it yet." Treat cryptomining as a canary, not the ceiling. Separately, the Commerzbank case (four arrested in Brazil, three charged in Europe, €30M gone) is a reminder that your risk often lives in a third party's flaw, not your own stack. Both stories point the same direction: the perimeter you don't control is the one being worked.

## Today's Action
- Inventory macOS endpoints with Remote Management / Screen Sharing enabled and disable it wherever it isn't explicitly required.
- Patch macOS now via the relevant Apple security update; do not wait for a maintenance window on an actively exploited auth bypass.
- Restrict Screen Sharing (port 5900) and Remote Management to known management IPs at the firewall; block inbound from the internet entirely.
- Hunt for unexplained CPU spikes, unknown launch daemons, and outbound connections to mining pools on Macs as an indicator of the miner payload.
- Review third-party and service-provider access to payment and account systems; confirm what a compromised vendor could reach, per the Commerzbank pattern.

*The call is always coming from a house you forgot you rented.*

## Related

- [Third-Party and Vendor Risk Management](/itsalreadywhen/rtfm/2026/07/22/third-party-and-vendor-risk-management/)
- [OpenAI's Own Models Broke Out of Their Sandbox and Hacked Hugging Face](/itsalreadywhen/2026/07/26/issue-006/)
- [Least Privilege, Actually Enforced](/itsalreadywhen/rtfm/2026/07/01/least-privilege-actually-enforced/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*