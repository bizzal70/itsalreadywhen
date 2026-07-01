---
layout: field_note
title: "Field Note — July 01, 2026"
date: 2026-07-01
summary: "Active exploitation of Langflow RCE (CVE-2026-33017) and an ongoing Azure CLI password spray dominate today, alongside a batch of max-severity Adobe ColdFusion patches."
---

## Today's Field Note

Three things worth your attention today, and none of them are the Chrome 382-fix pile-on (patch it, move on). First, Langflow's unauthenticated RCE (CVE-2026-33017, CVSS 9.3) is under active exploitation, with attackers scanning exposed AI app endpoints and dropping Monero miners. That is the entry-level payload, so assume the crypto miner is just the tenant who showed up first. Second, Huntress is tracking a live Azure CLI password spray out of LSHIY LLC infrastructure (2a0a:d683::/32, AS32167): 81 million-plus attempts, at least 78 accounts already compromised between June 12 and 26. Third, Adobe shipped seven max-severity (10/10) fixes for ColdFusion and Campaign Classic, all arbitrary code execution. ColdFusion is a perennial ransomware on-ramp, and the PoC gap on these never lasts long.

## Today's Action

- Inventory internet-facing Langflow instances now and patch to a fixed release; if you cannot patch today, pull them behind auth or off the internet entirely.
- Block the LSHIY range 2a0a:d683::/32 (AS32167) at the edge, then audit Azure sign-in logs for successful auth from that space and force resets on any hit.
- Enforce MFA and conditional access on all Azure/Entra accounts, and disable legacy or CLI-based auth paths where you can.
- Apply the Adobe ColdFusion and Campaign Classic patches for the seven CVSS 10 flaws; ColdFusion goes to the front of the queue.
- Hunt Langflow hosts for XMRig and unexpected outbound Monero traffic before assuming the miner was the only guest.

## Resources

Verified links for the CVEs mentioned above: official advisories, and a live search for public detection rules if any exist yet.

- **CVE-2026-33017**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-33017) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-33017)

*Patch the front door before you argue about the drapes.*