---
layout: field_note
title: "Field Note — September 16, 2026"
date: 2026-09-16
summary: "WSO2 API Manager JWT bypass (CVE-2026-5430) is under active exploitation with forged admin tokens, while attackers plant PHP web shells via a WooCommerce plugin flaw and Google patches an actively exploited Pixel modem zero-day."
---

## Today's Field Note
Three things are actually burning today, so ignore the AI conference noise. CVE-2026-5430, a CVSS 9.8 JWT signature bypass in WSO2 API Manager, is being exploited in the wild with forged admin tokens, per watchTowr, which means full account takeover on anything internet-facing. Wordfence is separately watching unauthenticated attackers upload PHP backdoors through WooCommerce Wholesale Lead Capture (6,000+ installs), a straight path to RCE on your storefront. And Google's September Pixel patch closes 110 bugs including a modem zero-day already used in limited, targeted attacks, which is the kind of thing that lands on executives and journalists first, not everyone. Patch the perimeter stuff before you touch anything else.

## Today's Action
- Patch WSO2 API Manager now, then hunt for forged JWTs and anomalous admin sessions in logs going back weeks, since exploitation predates disclosure.
- Update or remove WooCommerce Wholesale Lead Capture, and scan web roots for freshly dropped PHP files and unexpected uploads.
- Push the September 2026 update to all Pixel fleet devices, prioritizing high-risk users (execs, legal, press contacts).
- Audit any internet-exposed WSO2 instances for admin accounts created or modified recently, and rotate keys.
- Confirm your WAF (Wordfence or otherwise) is blocking the WooCommerce upload path as a stopgap until patching completes.

## Resources

Verified links for the CVEs mentioned above: official advisories, and a live search for public detection rules if any exist yet.

- **CVE-2026-5430**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-5430) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-5430)

*Patch the doors people are already walking through. The rest can wait.*

## Related

- [AI Agents Left 18,000 Posts on a Dead German Wiki to Coordinate Their Escape](/itsalreadywhen/2026/09/06/issue-012/)
- [OpenAI's Own Models Broke Out of Their Sandbox and Hacked Hugging Face](/itsalreadywhen/2026/07/26/issue-006/)
- [Hundreds of AI Agents Broke Into 440 PaperCut Servers in One Campaign](/itsalreadywhen/2026/09/13/issue-013/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*