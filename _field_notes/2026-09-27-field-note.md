---
layout: field_note
title: "Field Note — September 27, 2026"
date: 2026-09-27
summary: "Two unpatched Citrix NetScaler RCE zero-days are under active exploitation, SharePoint CVE-2026-65660 hit CISA's KEV, and ShinyHunters found a WAF bypass for the PeopleSoft flaw."
---

## Today's Field Note
Three things demand your attention, and none of them are optional. watchTowr flagged two unpatched Citrix NetScaler ADC and Gateway RCE zero-days under active exploitation, with no Citrix confirmation and no fix, which is why some admins are already pulling appliances offline rather than pray. Separately, CISA added SharePoint CVE-2026-65660 to KEV with a September 28 federal deadline, meaning it is confirmed in-the-wild and your clock is nearly out. And ShinyHunters, ever resourceful, is using a simple URL-encoding trick to slip past the WAF rules everyone deployed to mitigate Oracle PeopleSoft CVE-2026-35273, so your "compensating control" has already been compensated for. The pattern here is familiar: the mitigations you leaned on are the ones getting bypassed.

## Today's Action
- Treat internet-facing Citrix NetScaler ADC and Gateway as compromised until proven otherwise; consider taking them offline or fronting them with access controls, and hunt for post-exploitation artifacts and webshells now.
- Patch SharePoint against CVE-2026-65660 today, ahead of the September 28 KEV deadline, and review SharePoint logs for exploitation indicators.
- Do not rely on your WAF rule for PeopleSoft CVE-2026-35273; apply the actual Oracle patch and add detection for URL-encoded variants of the exploit path.
- Rotate NetScaler session secrets and credentials, and terminate active sessions once you have contained the appliances.
- Watch vendor advisories for the Citrix zero-days and stage patches so you can deploy the moment they ship.

## Resources

Verified links for the CVEs mentioned above: official advisories, and a live search for public detection rules if any exist yet.

- **CVE-2026-35273**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-35273) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-35273)
- **CVE-2026-65660**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-65660) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-65660)

*Nobody ever got breached by the vulnerability they patched.*

## Related

- [ShinyHunters Hacked Clop, Then Robbed the Ransoms Twice](/itsalreadywhen/2026/09/27/issue-015/)
- [AI Agents Left 18,000 Posts on a Dead German Wiki to Coordinate Their Escape](/itsalreadywhen/2026/09/06/issue-012/)
- [OpenAI's Own Models Broke Out of Their Sandbox and Hacked Hugging Face](/itsalreadywhen/2026/07/26/issue-006/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*