---
layout: field_note
title: "Field Note — October 01, 2026"
date: 2026-10-01
summary: "Cisco Catalyst SD-WAN Manager zero-day (CVE-2026-76504) is under active exploitation and now in CISA KEV, while Citrix NetScaler post-exploitation activity and a MikroTik RouterOS pre-auth RCE round out a rough day for edge gear."
---

## Today's Field Note
Your network edge is the problem again. Cisco confirmed active exploitation of CVE-2026-76504, a CVSS 9.8 auth bypass in Catalyst SD-WAN Manager that hands an unauthenticated remote attacker the admin API, and CISA has already dropped it into KEV. No workaround exists, so patching is the only move. Meanwhile LevelBlue's THOR team is tracking Citrix NetScaler post-exploitation (web shells creating superusers and hiding behind CSS-like URLs), and CISA is warning on a critical pre-auth RCE in MikroTik RouterOS. Three separate pieces of internet-facing infrastructure, all reachable, all being poked at right now.

## Today's Action
- Patch Cisco Catalyst SD-WAN Manager immediately for CVE-2026-76504. There is no workaround, so treat this as emergency change.
- Audit SD-WAN Manager admin accounts and API logs for unauthorized access predating the patch. Assume compromise if it was exposed.
- Hunt your NetScaler boxes for new superuser accounts and web shells mapped to CSS-like URL paths, per LevelBlue's THOR findings.
- Apply the MikroTik RouterOS fix and pull management interfaces off the public internet.
- Rotate credentials and session tokens on any of these appliances that faced the internet unpatched.

## Resources

Verified links for the CVEs mentioned above: official advisories, and a live search for public detection rules if any exist yet.

- **CVE-2026-76504**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-76504) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-76504)

*Patch the edge or someone else administers it for you.*

## Related

- [ShinyHunters Hacked Clop, Then Robbed the Ransoms Twice](/itsalreadywhen/2026/09/27/issue-015/)
- [OpenAI's Own Models Broke Out of Their Sandbox and Hacked Hugging Face](/itsalreadywhen/2026/07/26/issue-006/)
- [AI Agents Left 18,000 Posts on a Dead German Wiki to Coordinate Their Escape](/itsalreadywhen/2026/09/06/issue-012/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*