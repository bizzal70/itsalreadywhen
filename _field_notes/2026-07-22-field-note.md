---
layout: field_note
title: "Field Note — July 22, 2026"
date: 2026-07-22
summary: "SharePoint CVE-2026-50522 and the wp2shell WordPress flaws are under active exploitation with machine-key theft and rapid webshell deployment, both post-patch persistence problems."
---

## Today's Field Note
Two live fires today, both of the "patching is not the finish line" variety. Microsoft SharePoint CVE-2026-50522 (CVSS 9.8, unauthenticated deserialization RCE, credited to DEVCORE) is being exploited in the wild following a public PoC, and watchTowr confirms attackers are pulling machine keys, which means they keep their access even after you patch. This is the fourth SharePoint bug burned in a month, so treat your servers as suspect, not clean. Meanwhile the wp2shell chain (CVE-2026-63030 and CVE-2026-60137) in WordPress Core is being exploited within hours of the fix dropping, dropping webshells and rogue plugins that outlive the update. In both cases the update stops the bleeding but does nothing about the intruder already inside.

## Today's Action
- Patch SharePoint against CVE-2026-50522 now, then rotate ASP.NET machine keys and restart IIS. A patch alone leaves stolen keys valid.
- Hunt SharePoint for unexpected .aspx files, w3wp child processes, and post-exploitation persistence. Assume compromise on any internet-facing instance.
- Patch WordPress Core against CVE-2026-63030 and CVE-2026-60137, then audit for unknown plugins, modified core files, and dropped webshells.
- Review outbound traffic and admin account changes on both platforms for signs the intruder already moved.
- Take internet-facing SharePoint offline until patched and keys rotated if you cannot do it same-day.

## Resources

Verified links for the CVEs mentioned above: official advisories, and a live search for public detection rules if any exist yet.

- **CVE-2026-50522**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-50522) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-50522)
- **CVE-2026-60137**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-60137) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-60137)
- **CVE-2026-63030**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-63030) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-63030)

*Patch the hole, then go find who already walked through it.*

## Related

- [Third-Party and Vendor Risk Management](/itsalreadywhen/rtfm/2026/07/22/third-party-and-vendor-risk-management/)
- [Field Note — July 21, 2026](/itsalreadywhen/field-notes/2026/07/21/field-note/)
- [Field Note — July 20, 2026](/itsalreadywhen/field-notes/2026/07/20/field-note/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*