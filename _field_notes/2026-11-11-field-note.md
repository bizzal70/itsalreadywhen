---
layout: field_note
title: "Field Note — November 11, 2026"
date: 2026-11-11
summary: "CISA adds actively exploited Cisco BroadWorks and Openwave flaws to KEV, Xen Orchestra auth bypass is under attack, and Microsoft ships an exploited Outlook zero-day in a record patch drop."
---

## Today's Field Note
Three things are already in motion. CISA added CVE-2026-20320 (Cisco BroadWorks, XXE, CVSS 7.5) and CVE-2026-111793 (Openwave Webtop Media Transcoder) to the KEV catalog with confirmed exploitation, both leaking config and sensitive data. Separately, Vates VMS confirmed active exploitation of a Xen Orchestra auth bypass (VSA-2026-062, no CVE yet) where REST cookie parsing turns `authenticationToken=j:%7B%7D` into an empty object and hands over admin, which means full takeover of XCP-ng virtualization hosts. Finally, Microsoft's November Patch Tuesday is the usual firehose (over 1,200 flaws) but the one that counts is the exploited Outlook zero-day CVE-2026-124194, which can expose NTLMv2 hashes. Prioritize the exploited handful and ignore the volume theater.

## Today's Action
- Patch Cisco BroadWorks for CVE-2026-20320 and Openwave Webtop for CVE-2026-111793 now; both are confirmed in-the-wild and KEV-listed. Treat exposed instances as suspect and hunt for config/data exfil.
- Update Xen Orchestra immediately per VSA-2026-062; if internet-facing, assume compromise, pull it behind VPN, rotate admin credentials, and review XCP-ng host access logs.
- Deploy CVE-2026-124194 (Outlook) first from this Patch Tuesday, then block outbound SMB/NTLM at the egress to blunt NTLMv2 hash leakage.
- Upgrade Git to 2.56.1 (or the backported 2.50.2 through 2.55.1) for CVE-2026-111760 on any build box or developer host that runs recursive clones.
- Rotate stored AI provider and cloud API keys if you use Railway or Fireworks AI; both confirmed secret theft, and Railway reported roughly $740K in fraudulent usage.

*The patch notes are a novel; the exploit list is

## Resources

Verified links for the CVEs mentioned above: official advisories, and a live search for public detection rules if any exist yet.

- **CVE-2026-111760**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-111760) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-111760)
- **CVE-2026-111793**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-111793) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-111793)
- **CVE-2026-124194**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-124194) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-124194)
- **CVE-2026-20320**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-20320) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-20320)


## Related

- [ShinyHunters Hacked Clop, Then Robbed the Ransoms Twice](/itsalreadywhen/2026/09/27/issue-015/)
- [Hundreds of AI Agents Broke Into 440 PaperCut Servers in One Campaign](/itsalreadywhen/2026/09/13/issue-013/)
- [North Korea's TraderTraitor Pulls Off a $6.43 Billion Binance Heist](/itsalreadywhen/2026/11/01/issue-019/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*