---
layout: field_note
title: "Field Note — July 18, 2026"
date: 2026-07-18
summary: "WordPress core wp2shell RCE has a public PoC and Inc ransomware is chaining SonicWall SMA zero-days for root, both under active or imminent exploitation."
---

## Today's Field Note
Two things are burning today, and neither waits for your change window. The wp2shell flaws in WordPress core (6.9 and 7.0) now have CVE IDs, a published mechanism, and a working PoC: an unauthenticated HTTP request runs code on a bare install, no plugins required. Separately, Inc ransomware is chaining two SonicWall SMA zero-days to reach root on mobile access appliances, which is the kind of edge box that fronts your whole environment. WordPress is the largest attack surface on the internet and SMA appliances are internet-facing by design, so both of these are being sprayed at scale right now. Patch state is your only real signal here.

## Today's Action
- Patch WordPress core to the fixed release immediately on every 6.9/7.0 host; if you run a persistent object cache, confirm the fix covers that condition and flush after updating.
- Hunt WordPress logs for anonymous POST requests to core endpoints and unexpected PHP writes to uploads or theme directories.
- Apply SonicWall's SMA fixes now; if you cannot patch today, pull the appliance's management interface off the public internet and restrict access.
- Check SMA appliances for Inc ransomware indicators: unexpected root shells, new admin accounts, and outbound connections you did not authorize.
- Rotate credentials and certs that transited any recently exposed SonicWall SMA, and treat root compromise as full-appliance compromise.

*The request was anonymous. So was the shell.*

## Related

- [Field Note — July 17, 2026](/itsalreadywhen/field-notes/2026/07/17/field-note/)
- [Field Note — July 16, 2026](/itsalreadywhen/field-notes/2026/07/16/field-note/)
- [Logging Without Anyone Reading the Logs](/itsalreadywhen/rtfm/2026/07/15/logging-without-anyone-reading-the-logs/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*