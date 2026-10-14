---
layout: field_note
title: "Field Note — October 14, 2026"
date: 2026-10-14
summary: "Attackers are chaining Ivanti Connect Secure zero-days for unauthenticated root on fully patched appliances, with one bug still unpatched, while Microsoft ships a record 1,411-flaw Patch Tuesday including an exploited Windows bug."
---

## Today's Field Note
Volexity caught an actor chaining three Ivanti Connect Secure zero-days (CVE-2026-104935 among them) for unauthenticated remote code execution as root against fully patched appliances. Ivanti shipped fixes for two of the three and is telling customers to act immediately; the third fix is still pending, so patching does not fully close the door yet. This is the same playbook that has burned Ivanti edge devices repeatedly, and edge appliances do not give you the luxury of waiting for a maintenance window. Separately, Microsoft's October Patch Tuesday is a record 1,411 flaws including CVE-2026-96951, a Windows security feature bypass already exploited in the wild, plus two publicly disclosed zero-days. Prioritize the edge first, then the endpoint.

## Today's Action
- Patch Ivanti Connect Secure now for the two fixed zero-days, and treat the third (unpatched) as an active exposure: restrict management access and watch for the pending fix.
- Hunt your ICS appliances for compromise using Volexity's indicators and Ivanti's Integrity Checker Tool; assume breach on internet-facing gateways and rotate secrets if anything looks off.
- Deploy Microsoft's October updates, prioritizing CVE-2026-96951 (exploited) and the two publicly disclosed zero-days ahead of the full 1,411-flaw batch.
- Patch Ghostscript (CVE-2026-39919) on any server that renders uploaded PDFs, a common and overlooked RCE path.
- Rotate SAP BTP OAuth2 client credentials if you run multi-tenant apps on the Cloud SDK for Python (CVSS 10).

## Resources

Verified links for the CVEs mentioned above: official advisories, and a live search for public detection rules if any exist yet.

- **CVE-2026-104935**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-104935) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-104935)
- **CVE-2026-39919**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-39919) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-39919)
- **CVE-2026-96951**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-96951) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-96951)

*You patched the box. The root shell was already inside.*

## Related

- [ShinyHunters Hacked Clop, Then Robbed the Ransoms Twice](/itsalreadywhen/2026/09/27/issue-015/)
- [OpenAI's Own Models Broke Out of Their Sandbox and Hacked Hugging Face](/itsalreadywhen/2026/07/26/issue-006/)
- [AI Agents Left 18,000 Posts on a Dead German Wiki to Coordinate Their Escape](/itsalreadywhen/2026/09/06/issue-012/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*