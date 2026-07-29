---
layout: field_note
title: "Field Note â€” July 29, 2026"
date: 2026-07-29
summary: "Active exploitation of a Check Point SmartConsole auth bypass (CVE-2026-16232) now has a public PoC, while coordinated OT intrusions hit Minnesota water utilities and Gitea/vBulletin ship critical RCE fixes."
---

## Today's Field Note
The Check Point SmartConsole authentication bypass (CVE-2026-16232, CVSS 9.3) was already under active exploitation, and now Rapid7 has published a working PoC, so the window between "aware" and "compromised" just closed for anyone still running unpatched Security Management or MDS servers. Separately, dozens of Minnesota water and wastewater utilities were hit in coordinated OT intrusions that disrupted automated controls, which is the kind of thing the fresh CISA/ACSC isolation guidance exists to survive. Two more critical pre-auth RCEs landed with public exploits: Gitea (CVE-2026-60004, 9.8) lets any repo writer plant a Git hook, and vBulletin allows unauthenticated PHP execution via template rendering. None of these are theoretical. Pick your patch order and move.

## Today's Action
- Patch Check Point Security Management and MDS to a fixed build for CVE-2026-16232 now, then hunt SmartConsole login logs for anomalous auth events predating the fix.
- Upgrade Gitea to 1.27.1 to close CVE-2026-60004, and audit which accounts hold repository write access.
- Patch internet-facing vBulletin instances and review web server logs for suspicious template rendering requests.
- If you run OT, pull the CISA/ACSC isolation guidance and confirm you can actually operate segments in manual/isolated mode, not just on paper.
- Assume PoC availability means mass scanning within hours; prioritize any of the above that are internet-exposed.

## Resources

Verified links for the CVEs mentioned above: official advisories, and a live search for public detection rules if any exist yet.

- **CVE-2026-16232**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-16232) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-16232)
- **CVE-2026-60004**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-60004) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-60004)

*Patch the exploited ones first. The theoretical ones can wait for coffee.*

## Related

- [OpenAI's Own Models Broke Out of Their Sandbox and Hacked Hugging Face](/itsalreadywhen/2026/07/26/issue-006/)
- [Issue #004 — Week of July 12, 2026](/itsalreadywhen/2026/07/12/issue-004/)
- [The 11-byte packet that freezes an OpenSSL server for good](/itsalreadywhen/2026/07/19/issue-005/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*