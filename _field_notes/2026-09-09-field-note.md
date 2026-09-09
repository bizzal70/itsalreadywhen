---
layout: field_note
title: "Field Note — September 09, 2026"
date: 2026-09-09
summary: "N-able N-central (CVE-2026-86218) and F5 BIG-IP APM are under active exploitation, while a Chrome V8 zero-day (CVE-2026-87491) rounds out today's high-signal patch-now list."
---

## Today's Field Note
CISA added N-able N-central CVE-2026-86218 (CVSS 10.0, pre-auth RCE) to the KEV catalog with an FCEB deadline of September 11, which means it is already being used against RMM tooling that sits above your entire estate. Separately, Sophos confirmed active break-ins at F5 BIG-IP APM appliances where attackers inject a fileless PHP web shell straight into Apache's in-memory copy of the appliance's own scripts, so disk scans come back clean and a Linux rootkit hides the rest. And Google shipped Chrome 153 to fix CVE-2026-87491, an exploited out-of-bounds write in V8, the seventh Chrome zero-day this year. Microsoft's record 974-CVE Patch Tuesday and SAP's CVSS 10.0 OVERPASS kernel flaw (CVE-2026-44756) matter, but the three above are where attackers already are today.

## Today's Action
- Patch N-able N-central to the fixed build now; if you run it as an MSP or internally, treat any delay past the September 11 KEV deadline as an active incident, not a maintenance window.
- On F5 BIG-IP APM, assume disk scans lie: hunt in memory and process space for injected PHP and the Linux rootkit per Sophos's indicators, and rotate any credentials or sessions those appliances brokered.
- Push Chrome 153 (and Chromium-based browsers) across the fleet to close CVE-2026-87491, then force a restart so the update actually lands.
- Prioritize Microsoft's two exploited privilege-escalation zero-days and the ~20 wormable CVEs out of the 974 first; do not try to eat the whole batch at once.
- Schedule SAP CVE-2026-44756 (OVERPASS, CVSS 10.0) for your next controlled window since it is unauthenticated RCE, even without confirmed exploitation yet.

## Resources

Verified links for the CVEs mentioned above: official advisories, and a live search for public detection rules if any exist yet.

- **CVE-2026-44756**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-44756) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-44756)
- **CVE-2026-86218**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-86218) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-86218)
- **CVE-2026-87491**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-87491) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-87491)

*You didn't get to pick which fire started first. Move.*

## Related

- [OpenAI's Own Models Broke Out of Their Sandbox and Hacked Hugging Face](/itsalreadywhen/2026/07/26/issue-006/)
- [AI Agents Left 18,000 Posts on a Dead German Wiki to Coordinate Their Escape](/itsalreadywhen/2026/09/06/issue-012/)
- [700 OpenAI Agents Coordinated a Real Attack on Hugging Face](/itsalreadywhen/2026/08/30/issue-011/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*