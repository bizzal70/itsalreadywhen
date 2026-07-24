---
layout: field_note
title: "Field Note â€” July 24, 2026"
date: 2026-07-24
summary: "Russia's Laundry Bear exploited a Zimbra zero-click flaw to loot Western mailboxes, Redis shipped seven fixes after public authenticated RCE PoCs dropped, and NodeBB patched eight high-severity bugs with exploit code already live."
---

## Today's Field Note
Three items worth your attention, all with real teeth. Laundry Bear (aka Void Blizzard) spent months reading Western and Ukrainian mailboxes via a Zimbra webmail zero-click that fires on preview alone, exfiltrating the last 90 days of mail, the full directory, browser-saved passwords, and 2FA recovery codes. NSA, CISA and partners have published, so this is confirmed and joint-attributed. Separately, Redis shipped seven releases on July 23 after researchers dropped authenticated RCE PoCs against stock 6.2.22, 7.4.9, 8.6.4 and 8.8.0, all requiring RESTORE. And NodeBB patched eight high-severity flaws (fixed in 4.14.2) with working exploit code public the same day. The common thread: PoCs and nation-state operators are already moving, so treat these as active, not theoretical.

## Today's Action
- Patch Zimbra Collaboration to the fixed release now, then assume compromise on any exposed instance: hunt for anomalous webmail activity and mass directory reads over the last several months.
- For every Zimbra org, rotate 2FA recovery codes and browser-stored credentials that could have been scraped, and force password resets on affected mailboxes.
- Upgrade Redis to 6.2.23, 7.2.15, 7.4.10 or the equivalent 8.x fix; restrict or disable RESTORE, EVAL and XGROUP for untrusted accounts and get Redis off the public internet.
- Move NodeBB instances to 4.14.2 today; anything below 4.14.0 is exploitable with published code.
- Block preview-pane rendering where you can and prioritize Zimbra egress monitoring, since opening the message was enough.

*Preview panes count as clicks now. Plan accordingly.*

## Related

- [The 11-byte packet that freezes an OpenSSL server for good](/itsalreadywhen/2026/07/19/issue-005/)
- [Issue #004 — Week of July 12, 2026](/itsalreadywhen/2026/07/12/issue-004/)
- [Patch Cadence vs. Patch Theater](/itsalreadywhen/rtfm/2026/07/08/patch-cadence-vs-patch-theater/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*