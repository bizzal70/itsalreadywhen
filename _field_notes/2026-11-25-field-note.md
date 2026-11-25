---
layout: field_note
title: "Field Note — November 25, 2026"
date: 2026-11-25
summary: "Drupal RCE is in active exploitation and on CISA KEV with a three-day patch deadline, while attackers chained Palo Alto's Fragnesia flaw to root firewalls."
---

## Today's Field Note
Two edge-facing problems are live right now. The Drupal security team confirms active exploitation of a critical RCE (the Anthropic-scanner find) since at least Thursday, CISA has added it to KEV, and federal agencies are on a three-day clock. Separately, Palo Alto Networks patched Fragnesia after a China-linked group chained it with PHP2Shell to root firewalls across 25 servers in AI-assisted attacks. Both target the gear that sits in front of everything else, which is exactly where you cannot afford an unauthenticated foothold. Patch cadence here is measured in hours, not maintenance windows.

## Today's Action
- Patch Drupal core to the fixed release now and treat any unpatched public site as already touched. Review logs back to Thursday.
- Apply the Palo Alto Networks Fragnesia fix on all PAN-OS firewalls and audit for PHP2Shell artifacts and unexpected root shells.
- Pull both CVEs against your KEV-tracking process; the federal three-day deadline is a reasonable bar for everyone.
- For compromised-suspect Drupal hosts, hunt for webshells, new admin users, and modified cron entries, not just the patch gap.
- Rotate any credentials or API keys reachable from an exposed firewall or CMS host before you call it closed.

*It's not if the edge gets hit. It's whether you noticed before CISA did.*

## Related

- [Stolen Fireworks AI Key Trojanized Anthropic's Official Claude Code Extension](/itsalreadywhen/2026/11/15/issue-021/)
- [AI agents found a medical-software zero-day and rooted the server themselves](/itsalreadywhen/2026/11/22/issue-022/)
- [North Korea's TraderTraitor Pulls Off a $6.43 Billion Binance Heist](/itsalreadywhen/2026/11/01/issue-019/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*