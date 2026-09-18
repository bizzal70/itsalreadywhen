---
layout: field_note
title: "Field Note — September 18, 2026"
date: 2026-09-18
summary: "Two critical unauthenticated RCE bugs (Check Point management servers and Orkes Conductor, the latter already exploited) plus a Brevo supply-chain compromise pushing ClickFix to 100k sites lead today's stack."
---

## Today's Field Note
Three things are burning today. Check Point patched a critical unauthenticated RCE (via LivePatch) in its Security Management and Log Servers, meaning the box that holds your firewall policy and admin access is the target. Orkes Conductor's CVE-2026-58138, an unauthenticated RCE through inline workflow definitions, is already being exploited in the wild, so treat any internet-facing Conductor as compromised until proven otherwise. And Brevo got its Cloudflare API key stolen, which attackers used to inject ClickFix scripts into JavaScript served across roughly 100,000 customer sites. This is the boring, effective pattern: one stolen key, downstream everywhere. None of it requires a novel technique, just a slow patch cycle and a trusted third party.

## Today's Action
- Apply the Check Point LivePatch fix to all Security Management and Log Servers now, and audit management-plane access logs for anomalous root activity.
- Patch Orkes Conductor immediately; if internet-exposed, pull it behind auth or offline and hunt for malicious inline workflow definitions given active exploitation of CVE-2026-58138.
- If you use Brevo, rotate any shared API keys, review the JavaScript embedded on your sites for injected ClickFix content, and check user endpoints for ClickFix-delivered payloads.
- Rotate and scope down any Cloudflare API keys held by third parties; enforce least privilege and IP restrictions on worker deployment.
- Patch Docker Sandboxes on macOS (CVE-2026-77179) if developers use it, since guest code can read and modify host files.

## Resources

Verified links for the CVEs mentioned above: official advisories, and a live search for public detection rules if any exist yet.

- **CVE-2026-58138**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-58138) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-58138)
- **CVE-2026-77179**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-77179) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-77179)

*Someone else's stolen key is now your incident.*

## Related

- [AI Agents Left 18,000 Posts on a Dead German Wiki to Coordinate Their Escape](/itsalreadywhen/2026/09/06/issue-012/)
- [OpenAI's Own Models Broke Out of Their Sandbox and Hacked Hugging Face](/itsalreadywhen/2026/07/26/issue-006/)
- [An AI Test Model Broke Into Hugging Face and Nobody Noticed for a Weekend](/itsalreadywhen/2026/08/02/issue-007/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*