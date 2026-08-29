---
layout: field_note
title: "Field Note — August 29, 2026"
date: 2026-08-29
summary: "PaperCut ships a second emergency patch after attackers bypass the first, GiveWP hits max severity with unauthenticated RCE, and CISA adds an actively exploited ownCloud flaw to the KEV catalog."
---

## Today's Field Note
Three things worth your attention, all of them being exploited right now. PaperCut released a second emergency patch for NG and MF after researchers found multiple bypasses of the first fix; attackers are chaining two flaws to hit trusted configuration and run arbitrary Java without authentication. If you patched PaperCut last week, you are not done. Separately, a maximum-severity bug in the GiveWP WordPress donation plugin gives unauthenticated attackers command execution on the host, and CISA just added ownCloud CVE-2023-49105 (CVSS 9.8) to the KEV catalog after a Chinese-speaking actor used it to steal nuclear research data from a Philippine body. Old CVEs do not retire; they wait.

## Today's Action
- Apply the latest PaperCut NG/MF emergency update immediately. The prior patch does not cover the known bypasses.
- If PaperCut is internet-facing, pull it behind a VPN or IP allowlist now and review admin config for unauthorized changes.
- Update the GiveWP plugin on every WordPress install, or disable it until you can. Scan hosts for signs of command execution.
- Patch or decommission any ownCloud instance exposed to CVE-2023-49105; check WebDAV logs for phpinfo/pre-signed URL abuse.
- Inventory these three across your estate before you assume you are unaffected. Assume exposed instances were already reached.

## Resources

Verified links for the CVEs mentioned above: official advisories, and a live search for public detection rules if any exist yet.

- **CVE-2023-49105**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2023-49105) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2023-49105)

*The patch you shipped Friday is the bypass you read about Monday.*

## Related

- [OpenAI's Own Models Broke Out of Their Sandbox and Hacked Hugging Face](/itsalreadywhen/2026/07/26/issue-006/)
- [An AI Test Model Broke Into Hugging Face and Nobody Noticed for a Weekend](/itsalreadywhen/2026/08/02/issue-007/)
- [Issue #004 — Week of July 12, 2026](/itsalreadywhen/2026/07/12/issue-004/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*