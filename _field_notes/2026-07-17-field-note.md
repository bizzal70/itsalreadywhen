---
layout: field_note
title: "Field Note — July 17, 2026"
date: 2026-07-17
summary: "A critical SharePoint RCE (CVE-2026-58644) is under active exploitation with a CISA July 19 deadline, while CISA also flags two exploited Fortinet FortiSandbox flaws."
---

## Today's Field Note
Two edge-facing platforms are burning at once. Microsoft SharePoint Server has CVE-2026-58644, a critical deserialization RCE (CVSS 9.8) that CISA added to the KEV catalog with an FCEB patch deadline of July 19, and it was exploited soon after disclosure. On the network side, CISA ordered agencies to patch two actively exploited Fortinet FortiSandbox flaws by Sunday. SharePoint remains a favorite because it sits internet-facing, holds sensitive documents, and organizations are chronically slow to patch it (see the ToolShell mess). The clock CISA set for federal agencies is the clock you should be running against too, deadlines are not a suggestion when a public exploit is already in play.

## Today's Action
- Patch SharePoint Server for CVE-2026-58644 now. If you cannot patch today, restrict external access and rotate machine keys.
- Hunt SharePoint for post-exploitation: unexpected w3wp.exe child processes, new .aspx files in LAYOUTS, and outbound connections from the SharePoint host.
- Apply Fortinet FortiSandbox updates for the two KEV-listed flaws before Sunday, then audit management interface exposure.
- Pull FortiSandbox and SharePoint logs for signs of authenticated access from unfamiliar accounts or IPs predating the patch.
- Confirm your SharePoint instances are actually in your asset inventory. The one you forgot about is the one that gets hit.

## Resources

Verified links for the CVEs mentioned above: official advisories, and a live search for public detection rules if any exist yet.

- **CVE-2026-58644**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-58644) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-58644)

*Patch by Sunday, or explain by Monday.*

## Related

- [Field Note — July 16, 2026](/itsalreadywhen/field-notes/2026/07/16/field-note/)
- [Logging Without Anyone Reading the Logs](/itsalreadywhen/rtfm/2026/07/15/logging-without-anyone-reading-the-logs/)
- [Field Note — July 15, 2026](/itsalreadywhen/field-notes/2026/07/15/field-note/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*