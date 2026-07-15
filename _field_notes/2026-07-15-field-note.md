---
layout: field_note
title: "Field Note — July 15, 2026"
date: 2026-07-15
summary: "Two SonicWall SMA1000 zero-days (CVE-2026-15409/15410) and three actively exploited SharePoint flaws are under attack right now, while Microsoft ships a record 570-plus patch load."
---

## Today's Field Note
The perimeter appliances are on fire again. SonicWall confirmed two SMA1000 zero-days under active exploitation: CVE-2026-15409, an unauthenticated SSRF rated 10.0, and CVE-2026-15410, which chains toward arbitrary command execution as admin. In parallel, CISA added three on-prem SharePoint Server flaws to KEV with attackers already hitting internet-exposed instances. All of this lands on the same day Microsoft dumped a record 570-plus fixes including two more zero-days under attack (Active Directory and SharePoint), so your triage queue is now a bidding war. Patch the things attackers can reach from the internet first, then everything else.

## Today's Action
- Patch SonicWall SMA1000 appliances immediately for CVE-2026-15409 and CVE-2026-15410; if you cannot patch today, pull them off the public internet.
- Apply the CISA-flagged SharePoint Server patches on all internet-exposed on-prem instances, then hunt for webshells and anomalous IIS worker process activity.
- Prioritize the two actively exploited zero-days in Microsoft's July release (AD and SharePoint) ahead of the other 500-plus CVEs.
- Review SMA and SharePoint logs for SSRF probes, unexpected admin commands, and post-exploitation persistence going back several weeks, not just today.
- Rotate credentials and tokens exposed to any appliance you suspect was reachable before patching.

## Resources

Verified links for the CVEs mentioned above: official advisories, and a live search for public detection rules if any exist yet.

- **CVE-2026-15409**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-15409) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-15409)
- **CVE-2026-15410**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-15410) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-15410)

*Patch what the internet can touch, then argue about the rest.*

---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*