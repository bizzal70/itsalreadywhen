---
layout: field_note
title: "Field Note — September 10, 2026"
date: 2026-09-10
summary: "Cisco FMC CVE-2026-20079 and WatchGuard Firebox are under active exploitation, and four spy groups are burning the same Chrome/Windows BlueMoon exploit chain."
---

## Today's Field Note
Two firewall management planes are on fire at once. Cisco confirmed CVE-2026-20079, a max-severity (CVSS 10.0) authentication bypass in Secure Firewall Management Center, is being actively exploited, while CISA reports ransomware crews have now folded the critical WatchGuard Firebox RCE into their operations. Both are the box that manages your other boxes, so a bypass here is a bypass everywhere downstream. Separately, THN documents BlueMoon, an undocumented Chrome and Windows exploit chain that four separate espionage clusters (starting with China-aligned APT31) were running within a single week, which tells you this kit leaked or was shared, not built four times over. Patch the perimeter management planes first, then get Chrome and Windows current.

## Today's Action
- Patch Cisco Secure FMC for CVE-2026-20079 now, and pull management interfaces off any internet-facing path.
- Apply the WatchGuard Firebox fix and hunt for ransomware precursors (new admin accounts, config exports) on any box that was exposed.
- Force current Chrome and September Windows updates across the fleet to close the BlueMoon chain, prioritizing internet-facing and high-value users.
- Review FMC and Firebox authentication logs for anomalous admin sessions and config changes going back several weeks, not just today.
- Treat both firewall admin planes as potentially already touched: rotate credentials and validate rule sets against a known-good baseline.

## Resources

Verified links for the CVEs mentioned above: official advisories, and a live search for public detection rules if any exist yet.

- **CVE-2026-20079**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-20079) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-20079)

*Your firewall guards the door. Who's guarding the firewall.*

## Related

- [AI Agents Left 18,000 Posts on a Dead German Wiki to Coordinate Their Escape](/itsalreadywhen/2026/09/06/issue-012/)
- [OpenAI's Own Models Broke Out of Their Sandbox and Hacked Hugging Face](/itsalreadywhen/2026/07/26/issue-006/)
- [An AI Test Model Broke Into Hugging Face and Nobody Noticed for a Weekend](/itsalreadywhen/2026/08/02/issue-007/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*