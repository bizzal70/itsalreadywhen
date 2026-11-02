---
layout: field_note
title: "Field Note — November 02, 2026"
date: 2026-11-02
summary: "Ivanti patched two more actively exploited Connect Secure zero-days now in CISA's KEV catalog, while a new VOLTA infostealer uses LLMs to triage stolen data."
---

## Today's Field Note
Ivanti is back on the board, and not in a good way. Two more Connect Secure zero-days, CVE-2026-111357 and CVE-2026-118527, have been chained in attacks running since at least October 1, and CISA has already dropped both into the KEV catalog. If you run ICS gateways, assume the window of quiet exploitation predates the patch by a month, which means patching alone does not close the book. Separately, the VOLTA infostealer (aka VOLTA-AUTODOXER) is leaning on Claude, Gemini, and Kimi to rank victims by financial value, which is less a novelty and more a sign that commodity stealers now triage their own loot. The usual Chromium credentials, Outlook, and Slack data are all in scope.

## Today's Action
- Patch Ivanti Connect Secure to the fixed builds now and treat CVE-2026-111357 and CVE-2026-118527 as KEV-mandated emergencies, not routine updates.
- Hunt for compromise predating the patch: review ICS logs back to October 1 for anomalous sessions, new admin accounts, and config changes.
- Run Ivanti's Integrity Checker Tool and rotate all secrets, certificates, and admin credentials tied to the gateway.
- For VOLTA: rotate browser-stored credentials and session cookies for high-value accounts, and alert on mass Chromium credential store and Slack/Outlook token access.
- Enforce MFA and short session lifetimes on anything a stealer could harvest, so lifted cookies expire fast.

## Resources

Verified links for the CVEs mentioned above: official advisories, and a live search for public detection rules if any exist yet.

- **CVE-2026-111357**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-111357) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-111357)
- **CVE-2026-118527**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-118527) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-118527)

*Patched does not mean clean. Go look.*

## Related

- [ShinyHunters Hacked Clop, Then Robbed the Ransoms Twice](/itsalreadywhen/2026/09/27/issue-015/)
- [North Korea's TraderTraitor Pulls Off a $6.43 Billion Binance Heist](/itsalreadywhen/2026/11/01/issue-019/)
- [OpenAI's Own Models Broke Out of Their Sandbox and Hacked Hugging Face](/itsalreadywhen/2026/07/26/issue-006/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*