---
layout: field_note
title: "Field Note — September 26, 2026"
date: 2026-09-26
summary: "CISA flags actively exploited SharePoint, MikroTik, and WSO2 flaws while Kiteworks tells customers to physically shut down servers over an imminent attack warning."
---

## Today's Field Note
CISA added several vulnerabilities to KEV this week with confirmed exploitation: CVE-2026-65660 (SharePoint code injection), a MikroTik RouterOS flaw, and CVE-2026-5430 (a critical WSO2 authentication bypass affecting multiple products), alongside an actively exploited Adobe Commerce bug. Separately, Kiteworks (the company formerly known as Accellion, which you may recall from the 2021 mass-exfiltration era) told customers to physically power down servers for a six-to-nine hour window over the weekend after federal intelligence warned of an imminent attack, strongly implying an unpatched zero-day. When a vendor's remediation advice is "turn it off and wait," treat the box as compromised until proven otherwise. The Accellion pattern (file-transfer appliance, targeted campaign, no patch) is not a coincidence anyone should ignore.

## Today's Action
- Patch SharePoint (CVE-2026-65660), WSO2 (CVE-2026-5430), MikroTik RouterOS, and Adobe Commerce now, or pull them off the perimeter if you cannot; CISA KEV deadlines are not suggestions.
- For Kiteworks: follow the shutdown guidance, then hunt before restarting. Review file-access and authentication logs for the exposure window and assume data touched by that appliance is at risk.
- Isolate internet-facing SharePoint and WSO2 instances behind auth or VPN until confirmed patched, and check for rogue admin accounts and webshells.
- Audit MikroTik edge devices for unauthorized config changes, new accounts, and unexpected outbound tunnels.
- Inventory every managed file-transfer and secure file-sharing appliance you run. These remain a repeat target class; know where yours live before someone else does.

## Resources

Verified links for the CVEs mentioned above: official advisories, and a live search for public detection rules if any exist yet.

- **CVE-2026-5430**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-5430) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-5430)
- **CVE-2026-65660**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-65660) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-65660)

*Turning it off is not a fix. It is a stay of execution.*

## Related

- [AI Agents Left 18,000 Posts on a Dead German Wiki to Coordinate Their Escape](/itsalreadywhen/2026/09/06/issue-012/)
- [OpenAI's Own Models Broke Out of Their Sandbox and Hacked Hugging Face](/itsalreadywhen/2026/07/26/issue-006/)
- [Hundreds of AI Agents Broke Into 440 PaperCut Servers in One Campaign](/itsalreadywhen/2026/09/13/issue-013/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*