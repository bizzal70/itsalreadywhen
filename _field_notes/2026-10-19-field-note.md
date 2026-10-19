---
layout: field_note
title: "Field Note — October 19, 2026"
date: 2026-10-19
summary: "Broadcom Wi-Fi root RCE with public PoC, active exploitation of a SiteGuard WAF command injection flaw, and an OpenCode breach that may have leaked customers' AI provider API keys."
---

## Today's Field Note
Three things worth your attention. Quentin Kaiser disclosed an unpatched flaw in Broadcom's Wi-Fi setup software on October 16: an attacker in radio range runs code as root on Broadcom-based routers with no password and no pairing, demonstrated live against home gateways from three Belgian ISPs. Separately, attackers are actively exploiting an OS command injection bug in SiteGuard Server Edition to run commands as root or SYSTEM, the kind of flaw that turns your WAF into the breach. And OpenCode confirmed an intruder reached a legacy system on the night of October 16, potentially exposing the OpenAI, Anthropic, and Google API keys users stored in OpenCode Console. Keys do not patch themselves, so treat every one as burned.

## Today's Action
- If you run OpenCode Console, rotate every OpenAI, Anthropic, and Google API key stored there now, and review provider billing and usage logs for unfamiliar calls.
- Inventory Broadcom-based routers and ISP gateways, disable WPS/Wi-Fi setup services where you can, and segment untrusted wireless from management networks until a patch ships.
- Patch SiteGuard Server Edition immediately; if you cannot, restrict management access and scan for signs of root/SYSTEM command execution.
- Hold or stage this month's Windows Server security updates on Exchange hosts until you have verified OWA sign-in and mail flow, per Microsoft's confirmed regression.
- Pull provider-side API key scoping and rate limits tighter across the board, breach or not.

*Your WAF had one job, and now the attacker has root.*

## Related

- [Asset Inventory: You Can't Protect What You Don't Know You Have](/itsalreadywhen/rtfm/2026/09/02/asset-inventory-you-can-t-protect-what-you-don-t-know-you-have/)
- [Default Credentials and Configuration Drift](/itsalreadywhen/rtfm/2026/08/19/default-credentials-and-configuration-drift/)
- [Least Privilege, Actually Enforced](/itsalreadywhen/rtfm/2026/07/01/least-privilege-actually-enforced/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*