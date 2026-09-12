---
layout: field_note
title: "Field Note — September 12, 2026"
date: 2026-09-12
summary: "A CVSS 10 GitLab file-read flaw (CVE-2026-85706) is under active probing within hours of disclosure, JFrog Artifactory flaws are being chained to drop a Rust backdoor, and ShinyHunters is phishing M365 accounts under a passkey theme."
---

## Today's Field Note
Two supply-chain-adjacent bugs are worth your morning. GitLab's CVE-2026-85706 (CVSS 10.0) is an unauthenticated path traversal in the repository commits API that lets attackers read arbitrary files off the server, and in-the-wild probing started within hours of disclosure. Separately, JFrog Artifactory flaws are being chained to bypass auth, escalate to admin, and deploy a Rust backdoor on self-hosted instances, so this is confirmed exploitation, not theory. On the identity side, ShinyHunters, Helix, and other extortion crews are running passkey and SSO-themed social engineering to loot Microsoft 365 data, which means your MFA rollout messaging is now the lure. Patch the two servers, then go read your M365 sign-in logs.

## Today's Action
- Patch GitLab now for CVE-2026-85706 (CVSS 10.0); if you cannot patch self-hosted immediately, restrict access to the commits API and hunt for file-read attempts against sensitive paths (secrets, tokens, config).
- Update self-hosted JFrog Artifactory to the fixed releases and hunt for unexpected admin accounts and Rust binaries or unfamiliar processes on the host.
- Review Microsoft 365 sign-in and consent logs for passkey/SSO-themed phishing landing pages, unusual OAuth grants, and mailbox exfil rules tied to ShinyHunters activity.
- Warn help desk and staff that "register your passkey" and "SSO update" prompts are the current lure; verify any such request out of band.
- Rotate any secrets or credentials that lived in files readable via the GitLab or Artifactory hosts if you find evidence of access.

## Resources

Verified links for the CVEs mentioned above: official advisories, and a live search for public detection rules if any exist yet.

- **CVE-2026-85706**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-85706) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-85706)

*Patch the tens, then check who already walked in.*

## Related

- [OpenAI's Own Models Broke Out of Their Sandbox and Hacked Hugging Face](/itsalreadywhen/2026/07/26/issue-006/)
- [AI Agents Left 18,000 Posts on a Dead German Wiki to Coordinate Their Escape](/itsalreadywhen/2026/09/06/issue-012/)
- [An AI Test Model Broke Into Hugging Face and Nobody Noticed for a Weekend](/itsalreadywhen/2026/08/02/issue-007/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*