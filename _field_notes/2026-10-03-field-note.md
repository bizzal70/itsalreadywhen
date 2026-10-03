---
layout: field_note
title: "Field Note — October 03, 2026"
date: 2026-10-03
summary: "Warlock ransomware is actively exploiting SharePoint flaws against critical infrastructure while GitLab and Dell ship fixes for critical RCE and authentication bypass bugs."
---

## Today's Field Note
The China-linked Warlock crew is turning SharePoint into a doorway, hitting a water utility, a telecom, a regional government, and a university through on-prem SharePoint flaws (the ToolShell chain). If your SharePoint server is internet-facing and unpatched, you are already on the list, not waiting to be added. Meanwhile GitLab shipped fixes for a 9.9 AI Gateway RCE (patched in 19.2.4, 19.3.2, 19.4.1) affecting self-hosted gateways, and Dell dropped patches for Container Storage Modules including CVE-2026-63688, a CVSS 10.0 missing-authentication bug that hands attackers admin and root on Kubernetes nodes. Three different paths to the same outcome: someone else running code where you thought only you could.

## Today's Action
- Patch on-prem SharePoint against the ToolShell chain now, then hunt for webshells and rotate machine keys (an existing patch does not evict an attacker who already dropped a shell).
- If you host your own GitLab AI Gateway, upgrade to 19.2.4, 19.3.2, or 19.4.1 and audit Duo Agent Platform access while you are in there.
- Inventory Dell CSM deployments and apply the CSM updates; CVE-2026-63688 is unauthenticated and rated 10.0, so treat it as pre-patch compromise until proven otherwise.
- Review Warlock IOCs against your SharePoint and lateral-movement logs, with extra scrutiny if you run OT or critical infrastructure.
- Confirm SharePoint, GitLab, and storage control planes are not reachable from the open internet without need.

## Resources

Verified links for the CVEs mentioned above: official advisories, and a live search for public detection rules if any exist yet.

- **CVE-2026-63688**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-63688) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-63688)

*Patch Tuesday is a date. Exploitation is a timezone.*

## Related

- [ShinyHunters Hacked Clop, Then Robbed the Ransoms Twice](/itsalreadywhen/2026/09/27/issue-015/)
- [AI Agents Left 18,000 Posts on a Dead German Wiki to Coordinate Their Escape](/itsalreadywhen/2026/09/06/issue-012/)
- [An AI Test Model Broke Into Hugging Face and Nobody Noticed for a Weekend](/itsalreadywhen/2026/08/02/issue-007/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*