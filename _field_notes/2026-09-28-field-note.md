---
layout: field_note
title: "Field Note — September 28, 2026"
date: 2026-09-28
summary: "Citrix confirms two actively exploited NetScaler RCE zero-days now in CISA's KEV, while ShinyHunters retools its Oracle PeopleSoft exploit."
---

## Today's Field Note
Citrix has confirmed two NetScaler ADC and Gateway zero-days, CVE-2026-88771 (CVSS 9.5, unauthenticated) and CVE-2026-88772, both under active exploitation and now sitting in CISA's KEV with a Wednesday deadline for federal agencies. Admins were pulling appliances offline before patches even landed, which tells you how this is trending. Internet-facing NetScaler remains the perennial soft target, and RCE plus unauthenticated is the combination that turns a slow weekend into an incident bridge. Separately, ShinyHunters has retooled its exploit for the Oracle PeopleSoft flaw CVE-2026-35273, so if you run PeopleSoft, you are already in scope for an extortion crew that follows through. Patch the edge first, then go look for what already walked in.

## Today's Action
- Apply Citrix's NetScaler updates for CVE-2026-88771 and CVE-2026-88772 now; if you cannot patch immediately, take affected appliances offline as Citrix advised.
- Assume compromise on any NetScaler that was internet-facing and unpatched: kill and rotate all sessions, terminate active tokens, and hunt for webshells and unexpected admin activity.
- Patch Oracle PeopleSoft against CVE-2026-35273 and review logs for ShinyHunters-style data staging and exfiltration.
- Rotate NetScaler and PeopleSoft service credentials, secrets, and certificates that may have been exposed during the exposure window.
- Confirm your KEV tracking flags both Citrix CVEs and validate patch status against the CISA Wednesday deadline, whether or not you are a federal agency.

## Resources

Verified links for the CVEs mentioned above: official advisories, and a live search for public detection rules if any exist yet.

- **CVE-2026-35273**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-35273) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-35273)
- **CVE-2026-88771**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-88771) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-88771)
- **CVE-2026-88772**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-88772) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-88772)

*Shut it down now, read the logs later. The logs will still be there. The uptime won't matter.*

## Related

- [ShinyHunters Hacked Clop, Then Robbed the Ransoms Twice](/itsalreadywhen/2026/09/27/issue-015/)
- [AI Agents Left 18,000 Posts on a Dead German Wiki to Coordinate Their Escape](/itsalreadywhen/2026/09/06/issue-012/)
- [OpenAI's Own Models Broke Out of Their Sandbox and Hacked Hugging Face](/itsalreadywhen/2026/07/26/issue-006/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*