---
layout: field_note
title: "Field Note — November 27, 2026"
date: 2026-11-27
summary: "Drupal and Cacti RCE flaws are under active exploitation or have public PoCs, and NFS2ROOT (CVE-2026-99362) gives remote root on Linux."
---

## Today's Field Note
Three stack-level problems landed at once. Drupal's security team confirms a second critical access-bypass flaw is being exploited in the wild to hijack unpatched sites, so this is not theoretical and your public CMS footprint is the target. Cacti has an unauthenticated zero-day (tracked publicly as 4HTTP2SHELL / 4HTTP2ROOT, no CVE yet) that goes from a fresh HTTP session to RCE in four requests via guest access, with a working PoC already circulating. And CVE-2026-99362, dubbed NFS2ROOT, is a 12-year-old Linux kernel NFS server bug that lets remote attackers gain root, meaning any exposed NFS export is now a privilege-escalation path. None of these need credentials. All of them hit infrastructure you probably forgot you were running.

## Today's Action
- Patch Drupal core to the latest release now across every site, and audit for new admin accounts, unexpected files, and modified nodes as compromise indicators.
- For Cacti, disable guest/anonymous access immediately (set the Guest user to disabled), block external access to the Cacti web UI, and watch for unexpected child processes from the web server pending a vendor fix.
- Inventory Linux hosts running kernel NFS (nfsd) and apply the CVE-2026-99362 (NFS2ROOT) kernel patch from your distro; if no patch yet, restrict NFS exports to trusted hosts and firewall ports 111/2049 from untrusted networks.
- Check SAP exposure: rotate any SAP-related GitHub tokens and review repo access given the confirmed token-theft and source-code tampering incident.
- Hunt for the GoodGuys phishing kit (fake paid-interview lures spoofing Google, Nvidia, Okta) by alerting on new OAuth grants and credential-harvest domains impersonating those brands.

## Resources

Verified links for the CVEs mentioned above: official advisories, and a live search for public detection rules if any exist yet.

- **CVE-2026-99362**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-99362) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-99362)

*Three unauthenticated paths to root before lunch. Patch like you mean it.*

## Related

- [ShinyHunters Hacked Clop, Then Robbed the Ransoms Twice](/itsalreadywhen/2026/09/27/issue-015/)
- [Stolen Fireworks AI Key Trojanized Anthropic's Official Claude Code Extension](/itsalreadywhen/2026/11/15/issue-021/)
- [OpenAI's Own Models Broke Out of Their Sandbox and Hacked Hugging Face](/itsalreadywhen/2026/07/26/issue-006/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*