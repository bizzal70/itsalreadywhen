---
layout: field_note
title: "Field Note — July 14, 2026"
date: 2026-07-14
summary: "CISA flags active exploitation of Joomla iCagenda and Balbooa Forms RCE flaws, while a Jscrambler npm supply chain compromise and ShinyHunters OAuth abuse of Salesforce show trusted code and connections remain the soft entry."
---

## Today's Field Note
CISA added Joomla extension flaws in iCagenda and Balbooa Forms to KEV, with attackers using arbitrary file uploads to reach remote code execution on public-facing sites right now. Meanwhile the supply chain keeps eating its own: a threat actor poisoned several Jscrambler npm package versions to drop a cross-platform credential stealer, downloaded roughly 1,500 times before disclosure. And Microsoft's writeup on a year of ShinyHunters activity confirms what the receipts already showed, that the group walks into Salesforce environments through OAuth trust rather than any platform bug. None of this requires a novel exploit. It requires you trusting something you installed, connected, or forgot to patch.

## Today's Action
- Patch or pull the iCagenda and Balbooa Forms Joomla extensions immediately, and audit upload directories for planted webshells and unexpected PHP files.
- Pin and audit your Jscrambler npm dependencies against the known-bad versions, then rotate any developer or CI credentials that touched an affected build.
- Enumerate OAuth apps connected to your Salesforce org, revoke anything unrecognized or unused, and lock down connected-app permissions and IP ranges.
- Hunt for infostealer indicators on developer workstations that ran npm installs recently, treating stored tokens and browser secrets as already exposed.
- Treat third-party OAuth grants as standing access, and put them on the same review cadence as user accounts.

*Nobody breaks the door when you keep handing out keys.*

---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*