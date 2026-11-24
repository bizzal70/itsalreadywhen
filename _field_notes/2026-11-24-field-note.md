---
layout: field_note
title: "Field Note — November 24, 2026"
date: 2026-11-24
summary: "Azure API Management Classic was exploited to steal customer secrets at Norwegian energy firms, while CISA flagged actively exploited N-able MailAssure and MONAI Label flaws."
---

## Today's Field Note
Two credential-harvesting stories converged today, and both are already in the wild. Microsoft patched an Azure API Management Classic flaw after an unknown actor was observed hunting access tokens, secrets, and named values inside customer APIM instances. Norway's NSM tied the activity to attacks on Equinor and Skagerak Energi, so if you run APIM Classic, assume your stored secrets were readable. Separately, CISA added two actively exploited bugs to KEV: CVE-2026-134624, a 9.3 SSRF in N-able MailAssure, and the MONAI Label zero-day a China-nexus actor chained via the Cairn tool to hit root in roughly eleven minutes. None of these are theoretical, and the clock on rotation started before you read this.

## Today's Action
- Rotate every secret, access token, and named value stored in Azure APIM Classic tiers, and audit APIM access logs for anomalous reads going back several weeks.
- Migrate off APIM Classic where possible, or restrict the management plane to known IPs.
- Patch N-able MailAssure immediately for CVE-2026-134624 and review outbound requests for SSRF-driven LDAP or internal callbacks.
- Patch or isolate any MONAI Label deployments; treat medical imaging hosts as exposed and hunt for Cairn-related activity.
- Cross-check KEV additions against your asset inventory and flag both CVEs for emergency remediation windows.

## Resources

Verified links for the CVEs mentioned above: official advisories, and a live search for public detection rules if any exist yet.

- **CVE-2026-134624**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-134624) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-134624)

*You rotate now or you rotate after the disclosure. Same keys, worse week.*

## Related

- [Stolen Fireworks AI Key Trojanized Anthropic's Official Claude Code Extension](/itsalreadywhen/2026/11/15/issue-021/)
- [North Korea's TraderTraitor Pulls Off a $6.43 Billion Binance Heist](/itsalreadywhen/2026/11/01/issue-019/)
- [ShinyHunters Hacked Clop, Then Robbed the Ransoms Twice](/itsalreadywhen/2026/09/27/issue-015/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*