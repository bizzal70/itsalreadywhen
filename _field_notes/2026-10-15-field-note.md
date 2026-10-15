---
layout: field_note
title: "Field Note — October 15, 2026"
date: 2026-10-15
summary: "Two actively exploited edge-device zero-days land the same day: PAN-OS management interface RCE (CVE-2026-0322) and a Cisco Secure Email Gateway root-RCE, both with vendor-confirmed in-the-wild abuse."
---

## Today's Field Note
Two internet-facing appliances, two zero-days, one bad Wednesday. Palo Alto Networks confirmed limited exploitation of CVE-2026-0322 (CVSS 8.6), an RCE in the PAN-OS management interface, and has published IoCs. In parallel, Cisco warns that attackers are hitting its Secure Email Gateway with an unauthenticated flaw that writes files to the OS and runs commands as root, no login required, just a crafted attachment through the mail pipe. These are the devices sitting at your perimeter deciding what gets in, which is exactly why they get hit first and why "patch next cycle" is the wrong answer. If your firewall management plane or your SEG is reachable, assume someone is already knocking.

## Today's Action
- Patch PAN-OS for CVE-2026-0322 now; until then, restrict the management interface to a jump host or internal-only and pull it off the internet entirely.
- Apply Cisco's Secure Email Gateway fix immediately and hunt for unexpected files, cron jobs, or processes running as root on the appliance.
- Run Palo Alto's published IoCs against firewall logs and check for anomalous admin sessions or config changes on the management plane.
- On the SEG, inspect recent inbound mail with crafted attachments and review web/app logs for write activity preceding the patch.
- Confirm no management or admin interfaces (PAN-OS, Cisco SEG, or otherwise) are exposed externally; close what is.

## Resources

Verified links for the CVEs mentioned above: official advisories, and a live search for public detection rules if any exist yet.

- **CVE-2026-0322**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-0322) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-0322)

*Your perimeter box is someone else's entry point. Patch like you believe that.*

## Related

- [ShinyHunters Hacked Clop, Then Robbed the Ransoms Twice](/itsalreadywhen/2026/09/27/issue-015/)
- [OpenAI's Own Models Broke Out of Their Sandbox and Hacked Hugging Face](/itsalreadywhen/2026/07/26/issue-006/)
- [An AI Test Model Broke Into Hugging Face and Nobody Noticed for a Weekend](/itsalreadywhen/2026/08/02/issue-007/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*