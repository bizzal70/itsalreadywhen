---
layout: field_note
title: "Field Note — July 02, 2026"
date: 2026-07-02
summary: "Three active-exploitation items lead today: SharePoint RCE CVE-2026-45659 hits CISA KEV, Cisco confirms Unified CM exploitation, and an unpatched Argo CD flaw threatens full Kubernetes cluster takeover."
---

## Today's Field Note
Three things are burning at once, and two of them have patches you should have applied already. CISA added Microsoft SharePoint RCE CVE-2026-45659 (CVSS 8.8, deserialization of untrusted data) to KEV after confirmed exploitation, and Cisco finally admitted attackers are hitting the Unified CM flaw it patched back in early June, a bug with a public PoC out since disclosure. The new one has no fix: Synacktiv's unpatched Argo CD repo-server RCE lets an unauthenticated attacker who can reach the internal port take over an entire Kubernetes cluster, no CVE assigned yet. If your SharePoint and Unified CM boxes are still on old builds, assume you are already in someone's queue. Meanwhile ChocoPoC is trojanizing GitHub PoC repos to hit the researchers reading this, so watch what you clone.

## Today's Action
- Patch Microsoft SharePoint Server for CVE-2026-45659 now, then hunt for w3wp.exe spawning cmd or PowerShell and unexpected ASPX writes.
- Confirm Cisco Unified CM is on the June or later build; if it lagged, treat as potentially compromised and review admin and CLI access logs.
- Restrict Argo CD repo-server network exposure: block the internal port at the network layer and isolate it from untrusted segments until a fix lands.
- Detonate any GitHub PoC in a throwaway VM before running it; ChocoPoC steals browser creds, cookies, and drops a shell.
- Cross-check FortiGate credential hygiene given FortiBleed feeding INC and Lynx: rotate exposed creds and enforce MFA on VPN.

## Resources

Verified links for the CVEs mentioned above: official advisories, and a live search for public detection rules if any exist yet.

- **CVE-2026-45659**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-45659) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-45659)

*It's not if your SharePoint is exposed, it's already when.*