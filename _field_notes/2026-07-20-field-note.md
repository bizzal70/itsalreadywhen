---
layout: field_note
title: "Field Note — July 20, 2026"
date: 2026-07-20
summary: "ServiceNow CVE-2026-6875 and WordPress WP2Shell flaws are under active exploitation, while a critical unauthenticated NGINX RCE (CVE-2026-42533) sits one crafted request away from your edge."
---

## Today's Field Note
Three items cleared the bar today, and two of them are already being fired at live targets. Attackers are exploiting CVE-2026-6875 in the ServiceNow AI Platform for code execution (per Defused), so if you run ServiceNow, assume it is on someone's list. The WP2Shell pair, CVE-2026-60137 and CVE-2026-63030, went from disclosure to in-the-wild exploitation with the usual WordPress speed. And F5's NGINX flaw, CVE-2026-42533, is an unauthenticated heap overflow reachable with crafted HTTP requests: crash today, likely RCE tomorrow, and it sits on the exact boxes facing the internet. None of these wait for your change window.

## Today's Action
- Patch ServiceNow AI Platform for CVE-2026-6875 now and review logs for unexpected code execution or new integration/script activity.
- Update NGINX to 1.30.4 (stable) or 1.31.3 (mainline), and NGINX Plus to 37.0.3.1, prioritizing internet-facing instances.
- Audit WordPress installs for the plugin/theme tied to WP2Shell (CVE-2026-60137, CVE-2026-63030), patch, and hunt for dropped web shells.
- Pull WAF and access logs for anomalous POSTs and malformed HTTP requests against these three surfaces from the last two weeks.
- Confirm your NGINX worker processes are not silently crash-looping, an early signal someone is testing the overflow.

## Resources

Verified links for the CVEs mentioned above: official advisories, and a live search for public detection rules if any exist yet.

- **CVE-2026-42533**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-42533) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-42533)
- **CVE-2026-60137**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-60137) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-60137)
- **CVE-2026-63030**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-63030) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-63030)
- **CVE-2026-6875**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-6875) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-6875)

*You do not get to schedule the exploit, so stop scheduling the patch.*

## Related

- [The 11-byte packet that freezes an OpenSSL server for good](/itsalreadywhen/2026/07/19/issue-005/)
- [Field Note — July 19, 2026](/itsalreadywhen/field-notes/2026/07/19/field-note/)
- [Field Note — July 18, 2026](/itsalreadywhen/field-notes/2026/07/18/field-note/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*