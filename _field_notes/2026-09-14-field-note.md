---
layout: field_note
title: "Field Note — September 14, 2026"
date: 2026-09-14
summary: "ConnectWise ScreenConnect, GitLab, and JFrog Artifactory are all under active exploitation right now, and the ScreenConnect flaw is spreading worm-like."
---

## Today's Field Note

Three exploited-in-the-wild items landed together, so triage accordingly. ConnectWise patched a ScreenConnect flaw already being used in worm-like attacks, letting an attacker push and execute files over an active remote session, which is exactly the kind of thing that turns one compromised endpoint into a fleet. CISA added a max-severity GitLab vulnerability to its exploited list, and three JFrog Artifactory flaws (auth bypass plus privilege escalation to admin) are being chained to drop backdoors into your build pipeline. Meanwhile Microsoft's record 972-CVE September patch is breaking RDS and USB audio on Windows Server, so the usual "just patch everything" advice gets complicated this month. Exploited RMM and CI/CD infrastructure is not a nuisance, it is a direct path to your software supply chain.

## Today's Action

- Patch ScreenConnect immediately; if you cannot, restrict access and hunt for unexpected file transfers or child processes spawned from active sessions.
- Apply the JFrog Artifactory fixes and audit admin accounts, tokens, and any recently deployed artifacts for backdoors.
- Cross-check your GitLab version against the CISA KEV entry and patch or isolate exposed instances today.
- Stage the September Windows updates in a test ring before broad deployment; watch specifically for RDS failures and dead USB audio on Server hosts.
- Treat RMM and CI/CD platforms as tier-zero: enforce MFA, rotate service tokens, and log every remote session.

*The build pipeline is production. Defend it like one.*

## Related

- [Issue #004 — Week of July 12, 2026](/itsalreadywhen/2026/07/12/issue-004/)
- [Hundreds of AI Agents Broke Into 440 PaperCut Servers in One Campaign](/itsalreadywhen/2026/09/13/issue-013/)
- [AI Agents Left 18,000 Posts on a Dead German Wiki to Coordinate Their Escape](/itsalreadywhen/2026/09/06/issue-012/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*