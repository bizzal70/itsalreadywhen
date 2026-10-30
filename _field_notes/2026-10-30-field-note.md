---
layout: field_note
title: "Field Note — October 30, 2026"
date: 2026-10-30
summary: "CISA confirms active exploitation of a max-severity GitLab RCE (CVE-2026-97229) while a compromised Claude Code extension on Open VSX planted SSH backdoors on developer machines."
---

## Today's Field Note
Two items deserve your attention before coffee gets cold. CISA added CVE-2026-97229, a CVSS 10.0 integer overflow in GitLab CE/EE, to the KEV catalog with confirmed exploitation granting unauthenticated RCE (seen against Alpine Linux infrastructure), alongside an actively exploited Cisco firewall DoS flaw. Separately, the official Anthropic Claude Code extension was trojanized on the Open VSX registry via a Cursor Marketplace compromise, dropping a persistent SSH backdoor on developer hosts before being pulled. The pattern is the usual one: your CI/CD and your developers' laptops are the soft underbelly, and attackers know it. GitLab sits at the center of both your source and your pipeline, so an unauthenticated RCE there is a full-stack problem, not an app bug.

## Today's Action
- Patch GitLab CE/EE now for CVE-2026-97229; if you cannot, restrict network exposure of the instance and hunt for anomalous processes and new runner registrations.
- Apply the Cisco firewall update CISA flagged and confirm KEV compliance deadlines against your inventory.
- Audit every developer host for the compromised Claude Code extension pulled from Open VSX; check for unauthorized SSH keys in authorized_keys and unexpected sshd config changes.
- Rotate SSH credentials and GitLab tokens for any host or account that touched the affected versions.
- Pull and review GitLab access logs for unauthenticated requests hitting the vulnerable endpoint over the past two weeks.

## Resources

Verified links for the CVEs mentioned above: official advisories, and a live search for public detection rules if any exist yet.

- **CVE-2026-97229**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-97229) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-97229)

*Your pipeline is production. Patch it like it is.*

## Related

- [ShinyHunters Hacked Clop, Then Robbed the Ransoms Twice](/itsalreadywhen/2026/09/27/issue-015/)
- [AI Agents Left 18,000 Posts on a Dead German Wiki to Coordinate Their Escape](/itsalreadywhen/2026/09/06/issue-012/)
- [OpenAI's Own Models Broke Out of Their Sandbox and Hacked Hugging Face](/itsalreadywhen/2026/07/26/issue-006/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*