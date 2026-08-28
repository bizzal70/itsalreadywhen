---
layout: field_note
title: "Field Note — August 28, 2026"
date: 2026-08-28
summary: "PaperCut zero-day under active exploitation, three CVSS 10.0 ServiceNow flaws are patched but self-hosted instances remain exposed, and 8,300+ Gitea servers are being hit with RCE."
---

## Today's Field Note
Three items clear the bar today, and all three are the kind that get you paged. PaperCut confirmed active zero-day exploitation across all NG and MF versions, with confirmed customer incidents and an emergency patch for v25 and v26 (no CVE assigned yet, which tells you how fast this moved). ServiceNow patched three CVSS 10.0 AI Platform flaws allowing unauthenticated code and SQL injection; hosted instances are already covered, but self-hosted and partner-managed deployments are on their own clock. Meanwhile Shadowserver counts over 8,300 internet-exposed Gitea servers still unpatched against a critical RCE that is being exploited right now. PaperCut and Gitea have a long history as ransomware entry points, so treat both as intrusion-in-progress until proven otherwise.

## Today's Action
- Patch PaperCut NG/MF to the emergency v25/v26 release immediately; if you cannot, pull the web UI off the internet and apply PaperCut's mitigations today.
- Hunt PaperCut and Gitea hosts for post-exploitation now (new admin accounts, unexpected child processes, outbound connections), not after patching.
- Inventory ServiceNow: confirm hosted instances took the update, and prioritize patching self-hosted and partner-managed deployments for the three 10.0 AI Platform CVEs.
- Cross-check your external attack surface against Shadowserver's exposure feed for Gitea and PaperCut and close anything internet-facing that does not need to be.
- Assume compromise on any device that was exposed and unpatched during the exploitation window; rotate credentials and secrets stored on those systems.

*Patch the print server. Yes, the print server. It's always the print server.*

## Related

- [OpenAI's Own Models Broke Out of Their Sandbox and Hacked Hugging Face](/itsalreadywhen/2026/07/26/issue-006/)
- [The Week AI Agents Started Breaking Into Real Companies](/itsalreadywhen/2026/08/09/issue-008/)
- [When AI Agents Start Hacking Real People Without Being Told To](/itsalreadywhen/2026/08/23/issue-010/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*