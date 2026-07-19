---
layout: field_note
title: "Field Note — July 19, 2026"
date: 2026-07-19
summary: "Public exploits are live for WordPress Core 'wp2shell' RCE, and 7-Zip patched a malicious-archive RCE in 26.02."
---

## Today's Field Note
Two things worth your attention before lunch. First, public exploits for the WordPress Core "wp2shell" RCE chain are now circulating, which means the window between "critical advisory" and "mass scanning" has already closed. WordPress runs a nontrivial slice of the internet, so assume automated exploitation against unpatched Core installs is already in motion. Second, 7-Zip shipped 26.02 to fix an RCE triggered by opening a crafted archive, the kind of bug that pairs nicely with a phishing lure and a curious user. Neither is exotic, both are the sort of thing that turns into an incident because someone deferred a patch.

## Today's Action
- Patch WordPress Core immediately to the fixed release across every site you run, including the forgotten staging and marketing installs.
- Hunt for "wp2shell" indicators now: unexpected PHP files in web roots, new admin users, and outbound connections from web hosts.
- Push 7-Zip 26.02 to all endpoints and build systems, and check for the older versions bundled inside other software.
- Remind users not to open archives from untrusted senders, and detonate suspicious ones in a sandbox instead.
- Review web-facing logs for the scanning uptick that follows any public PoC release.

*Patch the WordPress boxes first. The scanners already found them.*

## Related

- [The 11-byte packet that freezes an OpenSSL server for good](/itsalreadywhen/2026/07/19/issue-005/)
- [Field Note — July 18, 2026](/itsalreadywhen/field-notes/2026/07/18/field-note/)
- [Field Note — July 17, 2026](/itsalreadywhen/field-notes/2026/07/17/field-note/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*