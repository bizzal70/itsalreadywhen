---
layout: field_note
title: "Field Note — August 24, 2026"
date: 2026-08-24
summary: "CISA orders a three-day patch on an actively exploited Zimbra flaw, while Iran-linked actors took a UK power plant offline for four days."
---

## Today's Field Note
CISA added an actively exploited Zimbra Collaboration Suite (ZCS) flaw to the KEV catalog and gave federal agencies a three-day clock to patch, which is the shortest fuse they hand out and means real attacks are landing now, not theoretically. Zimbra is the usual soft target: internet-facing mail, slow patch cycles, and a long history of webmail RCE and XSS chains being strung together for account takeover. Separately, Iran-linked operators kept a UK power plant offline for four days, a reminder that OT disruption is no longer hypothetical and distributed energy infrastructure is squarely in scope. And UAT-10147, a Chinese-speaking crew, is hitting exposed Windows and Linux web servers globally with SPECTRE malware carrying EDR bypass and a Linux rootkit. Three different pressures, all pointing at your exposed edge.

## Today's Action
- Patch Zimbra ZCS to the latest release today, per the CISA KEV directive, and treat the three-day federal deadline as your own regardless of sector.
- Hunt for post-exploitation on Zimbra hosts: review webmail logs, check for rogue filters/forwarders, unexpected admin sessions, and web shells in the ZCS web root.
- For UAT-10147: audit internet-facing web servers, verify EDR agent integrity on both Windows and Linux, and check Linux hosts for rootkit indicators (hidden processes, tampered kernel modules).
- OT and energy operators: confirm segmentation between IT and control networks, review remote access paths into distributed generation assets, and validate manual-operation fallback given the UK plant outage.
- Confirm you can actually receive Zimbra patches and that these boxes are in your asset inventory before you assume you are covered.

*Three days to patch means someone already had three weeks in.*

## Related

- [Issue #004 — Week of July 12, 2026](/itsalreadywhen/2026/07/12/issue-004/)
- [OpenAI's Own Models Broke Out of Their Sandbox and Hacked Hugging Face](/itsalreadywhen/2026/07/26/issue-006/)
- [When AI Agents Start Hacking Real People Without Being Told To](/itsalreadywhen/2026/08/23/issue-010/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*