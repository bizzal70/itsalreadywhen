---
layout: field_note
title: "Field Note — October 31, 2026"
date: 2026-10-31
summary: "Three active-exploitation items: chained Ivanti Connect Secure flaws (now in CISA KEV), PHP2Shell attacks rooting Palo Alto firewalls, and a malicious Claude Code extension on Cursor that planted SSH backdoors."
---

## Today's Field Note
It is an edge-device day, and not a good one. CISA added two Ivanti Connect Secure flaws (including CVE-2026-111357, CVSS 8.8) to the KEV catalog after attackers chained three bugs into unauthenticated root. Meanwhile PHP2Shell is weaponizing the critical PHP CGI flaws to root Palo Alto firewalls across a pool of over 22 million exposed instances, and it has been running for more than a week. Separately, a trojanized Claude Code extension sat in Cursor's marketplace for roughly 11 hours on October 29, planting persistent SSH backdoors on up to 5,000 developer machines. Your perimeter and your developers both got hit this week, so triage accordingly.

## Today's Action
- Patch Ivanti Connect Secure now per the vendor advisory, then hunt for root-level webshells and anomalous admin sessions. Assume compromise if you were exposed and unpatched.
- Confirm your PHP/PHP-CGI builds are patched and that Palo Alto management and GlobalProtect interfaces are not internet-facing. Check PAN-OS logs for PHP2Shell indicators.
- Audit any machine that installed the Claude Code extension on Cursor around October 29. Inspect `~/.ssh/authorized_keys` for unknown keys and rotate affected credentials.
- Apply the WordPress Core RCE patch (versions 4.7 through 7.1.3) immediately. Nearly 63,000 attack attempts landed within 24 hours of disclosure.
- Pull your edge devices (Ivanti, Palo Alto, TeamViewer) into a focused asset inventory and verify every one is on a supported, patched build.

## Resources

Verified links for the CVEs mentioned above: official advisories, and a live search for public detection rules if any exist yet.

- **CVE-2026-111357**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-111357) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-111357)

*The castle wall was always the softest part. Patch it like you believe that.*

## Related

- [ShinyHunters Hacked Clop, Then Robbed the Ransoms Twice](/itsalreadywhen/2026/09/27/issue-015/)
- [AI Agents Left 18,000 Posts on a Dead German Wiki to Coordinate Their Escape](/itsalreadywhen/2026/09/06/issue-012/)
- [OpenAI's Own Models Broke Out of Their Sandbox and Hacked Hugging Face](/itsalreadywhen/2026/07/26/issue-006/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*