---
layout: field_note
title: "Field Note — September 07, 2026"
date: 2026-09-07
summary: "Three active-exploitation problems today: N-able N-central RCE, MikroTik RouterOS router hijacks, and an unpatched ConnectWise ScreenConnect flaw."
---

## Today's Field Note
RMM season continues. N-able shipped its fourth N-central hotfix in five weeks, this time for a max-severity unauthenticated RCE, and the incident notice says it is being exploited in the wild (the release notes hedge, which tells you everything). If you missed it: everything below build 2026.3.1.14 needs Hotfix 4, including boxes you patched to Hotfix 3 yesterday. Meanwhile ConnectWise is warning of a new ScreenConnect flaw with no patch until later this week (mitigations only for now), and attackers are chaining two MikroTik RouterOS bugs to hijack routers with SSH exposed to the internet. The common thread is the same as always: the tools you use to manage everything are the tools they use to own everything.

## Today's Action
- Patch on-prem N-able N-central to Hotfix 4 (build 2026.3.1.14 or later) now, even if you applied Hotfix 3. Assume anything below that is a target.
- Treat any N-central server that was internet-facing and unpatched as potentially compromised. Hunt, do not just patch.
- Apply ConnectWise's interim ScreenConnect mitigations today and schedule the patch the moment it lands this week. Restrict admin access in the meantime.
- Get MikroTik RouterOS off the public internet: kill exposed SSH, apply the latest firmware, and rotate credentials on anything that was reachable.
- Audit all remote management and RMM exposure across your estate. If it does not need to face the internet, it should not.

*The blast radius of a management tool is the whole environment. Patch accordingly.*

## Related

- [OpenAI's Own Models Broke Out of Their Sandbox and Hacked Hugging Face](/itsalreadywhen/2026/07/26/issue-006/)
- [Issue #004 — Week of July 12, 2026](/itsalreadywhen/2026/07/12/issue-004/)
- [700 OpenAI Agents Coordinated a Real Attack on Hugging Face](/itsalreadywhen/2026/08/30/issue-011/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*