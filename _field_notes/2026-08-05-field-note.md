---
layout: field_note
title: "Field Note — August 05, 2026"
date: 2026-08-05
summary: "CISA confirms active exploitation of Langflow, Tomcat, and N-central flaws while the self-propagating ChainDrop worm rips through npm and CVE-2026-59774 hands unauthenticated file reads on Gitea."
---

## Today's Field Note

Three fires worth your attention today. CISA added CVE-2026-9198 (Langflow, unauthenticated RCE, CVSS 9.8), a Tomcat EncryptInterceptor bypass, and an N-central auth bypass to the KEV catalog with confirmed in-the-wild exploitation, so the federal deadline is your deadline. Meanwhile the ChainDrop worm has self-propagated through more than 1,300 npm packages (2 billion monthly downloads combined) using stolen npm and GitHub credentials to spread on its own, which means yesterday's clean build is not today's clean build. And CVE-2026-59774 lets an unauthenticated attacker read any file the Gitea service account can touch in versions 1.22.1 through 1.27.0, with a crafted Org-mode file in a public repo as the only ammunition needed. None of these are theoretical.

## Today's Action

- Patch Langflow, Apache Tomcat, and N-central now per the KEV entries (CVE-2026-9198 and companions); if you cannot, pull them off the internet today.
- Upgrade Gitea to 1.27.1 immediately and audit service account file permissions to limit blast radius from CVE-2026-59774.
- Freeze npm installs, pin lockfiles, and rebuild from a known-good state; scan your dependency tree for ChainDrop indicators before any new deploy.
- Rotate npm and GitHub tokens and enforce 2FA on those accounts, since ChainDrop spreads on stolen credentials, not a single package.
- Confirm Langflow and N-central are not exposed to the public internet, and hunt for post-exploitation activity going back at least a week.

## Resources

Verified links for the CVEs mentioned above: official advisories, and a live search for public detection rules if any exist yet.

- **CVE-2026-59774**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-59774) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-59774)
- **CVE-2026-9198**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-9198) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-9198)

*Patch fast or explain slow. Pick one.*

## Related

- [An AI Test Model Broke Into Hugging Face and Nobody Noticed for a Weekend](/itsalreadywhen/2026/08/02/issue-007/)
- [OpenAI's Own Models Broke Out of Their Sandbox and Hacked Hugging Face](/itsalreadywhen/2026/07/26/issue-006/)
- [Issue #004 — Week of July 12, 2026](/itsalreadywhen/2026/07/12/issue-004/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*