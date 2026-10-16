---
layout: field_note
title: "Field Note — October 16, 2026"
date: 2026-10-16
summary: "Armory Castle exploited BeyondTrust Remote Support zero-day CVE-2026-102764 since August, and attackers are actively backdooring Nextcloud servers via Collabora RCE CVE-2026-110447."
---

## Today's Field Note
Two items demand your attention before the end of the day. BeyondTrust confirmed CVE-2026-102764 (CVSS 9.3), an improper origin validation flaw in Remote Support (the product formerly known as Bomgar), which the China-nexus group Armory Castle (UNC5221/Warp Panda) has been running as a zero-day since late August. They are not smashing and grabbing: custom tooling, log deletion, artifact cleanup. Assume your window of visibility was already small. Separately, attackers are actively exploiting CVE-2026-110447 in the Collabora Online CODE Server app for Nextcloud to drop backdoors, and privileged remote-support and file-sync boxes are exactly where adversaries like to live quietly.

## Today's Action
- Patch BeyondTrust Remote Support immediately per the vendor advisory for CVE-2026-102764. Prioritize internet-facing appliances.
- Hunt for Armory Castle activity on RS hosts: look for deleted or gapped logs, unexpected outbound connections, and unknown binaries. Assume patching does not equal eviction.
- Rotate credentials and secrets accessible to any BeyondTrust appliance you cannot prove was clean, including session recordings and vaulted creds.
- Update the Collabora Online (richdocumentscode) app on all Nextcloud instances to the fixed release for CVE-2026-110447, then check for web shells and unexpected cron entries.
- Pull privileged remote-access and file-sync systems off direct internet exposure where possible, and tighten allowlists on the rest.

## Resources

Verified links for the CVEs mentioned above: official advisories, and a live search for public detection rules if any exist yet.

- **CVE-2026-102764**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-102764) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-102764)
- **CVE-2026-110447**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-110447) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-110447)

*Patch the box, then assume someone already had the keys.*

## Related

- [ShinyHunters Hacked Clop, Then Robbed the Ransoms Twice](/itsalreadywhen/2026/09/27/issue-015/)
- [An AI Test Model Broke Into Hugging Face and Nobody Noticed for a Weekend](/itsalreadywhen/2026/08/02/issue-007/)
- [OpenAI's Own Models Broke Out of Their Sandbox and Hacked Hugging Face](/itsalreadywhen/2026/07/26/issue-006/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*