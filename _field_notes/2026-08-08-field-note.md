---
layout: field_note
title: "Field Note — August 08, 2026"
date: 2026-08-08
summary: "A CVSS 10.0 Metabase SQLi zero-day is being exploited to steal customer data, Progress Kemp LoadMaster's CVE-2026-8037 hit CISA KEV after nearly 800 exploit attempts, and N-able N-central attackers are persisting on managed systems."
---

## Today's Field Note
Three actively exploited flaws are worth your morning, and none of them care about your patch window. Metabase is bleeding: a maximum-severity, unauthenticated SQL injection zero-day (CVSS 10.0, no CVE assigned yet) is being used in the wild to breach instances and steal data, with Framework and Tally already named as victims. CISA added Progress Kemp LoadMaster's CVE-2026-8037 (CVSS 9.6, command injection) to KEV after roughly 792 recorded exploit attempts, so this is spray-and-pray, not theory. And N-able shipped N-central Hotfix 2 precisely because attackers are already inside managed systems and adapting faster than the first round of fixes. RMM compromise means downstream customers, so treat N-central like it is on fire until proven otherwise.

## Today's Action
- Apply the emergency Metabase update immediately, or pull the instance off the internet if you cannot patch today. Hunt for anomalous SQL and outbound data transfers going back several weeks.
- Patch Progress Kemp LoadMaster against CVE-2026-8037 now. If exposed to the internet, review logs for command injection attempts and unexpected admin activity.
- Deploy N-able N-central Hotfix 2 and assume compromise: audit for new accounts, rogue scheduled tasks, and persistence on both the N-central server and managed endpoints.
- For all three, rotate credentials and API tokens that touched the affected systems. SQLi and RMM access both mean stolen secrets.
- Check whether you are downstream of Framework, Tally, or an MSP running N-central, and start the customer-notification conversation before it starts itself.

## Resources

Verified links for the CVEs mentioned above: official advisories, and a live search for public detection rules if any exist yet.

- **CVE-2026-8037**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-8037) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-8037)

*The patch window closed while you were reading the changelog.*

## Related

- [OpenAI's Own Models Broke Out of Their Sandbox and Hacked Hugging Face](/itsalreadywhen/2026/07/26/issue-006/)
- [Issue #004 — Week of July 12, 2026](/itsalreadywhen/2026/07/12/issue-004/)
- [An AI Test Model Broke Into Hugging Face and Nobody Noticed for a Weekend](/itsalreadywhen/2026/08/02/issue-007/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*