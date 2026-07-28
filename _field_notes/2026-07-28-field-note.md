---
layout: field_note
title: "Field Note â€” July 28, 2026"
date: 2026-07-28
summary: "Two maximum-severity flaws under active exploitation (Arista VeloCloud CVE-2026-16812 and an unpatched Fastjson RCE), plus a critical unauthenticated TeamCity bug with a fix already out."
---

## Today's Field Note
Three things are on fire and only one has a full patch. Arista VeloCloud Orchestrator on-prem is being hit as a zero-day via CVE-2026-16812, a CVSS 10.0 OS command injection that hands attackers privileged internal functions. Separately, attackers are landing unauthenticated RCE against US firms through a Fastjson flaw that fires under the library's stock default config, and there is no patch yet. JetBrains also shipped fixes for CVE-2026-63077 (CVSS 9.8) in TeamCity On-Premises, an unauthenticated command execution path that will draw exploit attempts fast now that it is public. VeloCloud and TeamCity are classic pivot points into build pipelines and internal networks, so treat both as time-sensitive.

## Today's Action
- Patch Arista VeloCloud Orchestrator on-prem now; if you cannot, pull it off the internet and audit for command-injection artifacts and unexpected privileged calls.
- Update TeamCity On-Premises to 2025.11.7 or 2026.1.3 today, and check exposed instances for signs of pre-patch access.
- Inventory apps using Fastjson, disable autotype and any non-default deserialization, and restrict outbound connections from affected services until a fix lands.
- Hunt VeloCloud and TeamCity hosts for new accounts, webshells, and anomalous outbound traffic, not just presence of the patch.
- Assume internet-facing TeamCity has already been probed; rotate any credentials, tokens, and CI secrets those instances could reach.

## Resources

Verified links for the CVEs mentioned above: official advisories, and a live search for public detection rules if any exist yet.

- **CVE-2026-16812**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-16812) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-16812)
- **CVE-2026-63077**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-63077) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-63077)

*Two zero-days and a fresh CVSS 9.8. Patch the one you can, cage the two you can't.*

## Related

- [OpenAI's Own Models Broke Out of Their Sandbox and Hacked Hugging Face](/itsalreadywhen/2026/07/26/issue-006/)
- [Issue #004 — Week of July 12, 2026](/itsalreadywhen/2026/07/12/issue-004/)
- [The 11-byte packet that freezes an OpenSSL server for good](/itsalreadywhen/2026/07/19/issue-005/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*