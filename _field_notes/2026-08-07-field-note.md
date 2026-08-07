---
layout: field_note
title: "Field Note — August 07, 2026"
date: 2026-08-07
summary: "Cisco patches three 9.9-severity SD-WAN/IOS XE bugs, Switzerland confirms a SharePoint breach, and the Microsoft 365 AitM phishing campaign is actively hijacking finance-team inboxes."
---

## Today's Field Note
Three items worth your attention, all with live implications. Cisco shipped fixes for 12 flaws in Catalyst SD-WAN and IOS XE, including three rated 9.9 CVSS, and the SD-WAN issues hit regardless of configuration. Meanwhile Switzerland's federal IT office confirmed attackers exploited SharePoint vulnerabilities to compromise roughly 200 government accounts, a reminder that on-prem SharePoint is still being worked hard after this year's ToolShell wave. And there is an active adversary-in-the-middle campaign against Microsoft 365, using residential proxies to blend malicious sign-ins into consumer traffic while it hunts for payroll and finance personnel. None of these are theoretical. Patch the edge, watch the mailboxes, assume the SharePoint box is a target.

## Today's Action
- Patch Cisco Catalyst SD-WAN and IOS XE now for the three 9.9 CVSS bugs. The SD-WAN flaws apply regardless of device config, so do not assume you are exempt.
- Audit on-prem SharePoint: confirm current patch level, check for webshells and unexpected service accounts, and rotate machine keys if you have not since the ToolShell disclosures.
- Hunt Microsoft 365 sign-in logs for AitM indicators: token replay, impossible-travel logins, and sign-ins from residential proxy IP ranges targeting finance and payroll users.
- Enforce phishing-resistant MFA (FIDO2/passkeys) for finance and payroll staff; conditional-access token binding blunts AitM session theft.
- Review inbox rules on high-value finance mailboxes for auto-forwarding or hidden filter rules planted post-compromise.

*The edge, the inbox, the file server. Same three doors, every day.*

## Related

- [Issue #004 — Week of July 12, 2026](/itsalreadywhen/2026/07/12/issue-004/)
- [An AI Test Model Broke Into Hugging Face and Nobody Noticed for a Weekend](/itsalreadywhen/2026/08/02/issue-007/)
- [OpenAI's Own Models Broke Out of Their Sandbox and Hacked Hugging Face](/itsalreadywhen/2026/07/26/issue-006/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*