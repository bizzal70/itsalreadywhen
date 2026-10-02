---
layout: field_note
title: "Field Note — October 02, 2026"
date: 2026-10-02
summary: "Fortinet FortiMail zero-day CVE-2026-104286 is under active exploitation and in CISA KEV, while Warlock continues hitting critical infrastructure through SharePoint flaws."
---

## Today's Field Note
CVE-2026-104286, a CVSS 9.8 path traversal in Fortinet FortiMail, is being exploited in the wild to write arbitrary files as an unauthenticated attacker, which is a short hop to code execution. CISA added it to KEV on Thursday, so the federal deadline clock is already running and you should treat it the same way regardless of sector. FortiMail sits at the edge, handles mail, and tends to be internet-facing, which is exactly the profile attackers prefer. Meanwhile China-based Warlock keeps grinding away at SharePoint vulnerabilities (the ToolShell lineage) against critical infrastructure since July 2025, so if you run on-prem SharePoint you are still in scope. Separately, Sucuri documented a self-healing WordPress backdoor (SC) that rebuilds from files, database, and shared memory, meaning a partial cleanup just buys the attacker time.

## Today's Action
- Patch FortiMail to the fixed build per Fortinet's advisory today; if you cannot, restrict management and admin interfaces and pull them off the public internet.
- Hunt FortiMail for unexpected files, new admin accounts, and config changes, and assume compromise on any exposed instance that was unpatched this week.
- Confirm your on-prem SharePoint carries the full ToolShell patch set and check IIS and web root for webshells tied to Warlock activity.
- For WordPress, do not trust a single-pass cleanup of SC: rotate all secrets, inspect the database and shared memory, and rebuild from known-good where feasible.
- Verify your KEV remediation workflow actually flagged CVE-2026-104286 and that edge appliances are inside that workflow, not outside it.

## Resources

Verified links for the CVEs mentioned above: official advisories, and a live search for public detection rules if any exist yet.

- **CVE-2026-104286**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-104286) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-104286)

*Edge appliances are not infrastructure. They are someone else's foothold with your logo on it.*

## Related

- [ShinyHunters Hacked Clop, Then Robbed the Ransoms Twice](/itsalreadywhen/2026/09/27/issue-015/)
- [OpenAI's Own Models Broke Out of Their Sandbox and Hacked Hugging Face](/itsalreadywhen/2026/07/26/issue-006/)
- [AI Agents Left 18,000 Posts on a Dead German Wiki to Coordinate Their Escape](/itsalreadywhen/2026/09/06/issue-012/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*