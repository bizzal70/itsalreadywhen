---
layout: field_note
title: "Field Note — August 06, 2026"
date: 2026-08-06
summary: "JetBrains TeamCity CVE-2026-63077 is under active exploitation, CISA added Langflow, N-central, and Apache Tomcat flaws to KEV with a 3-day fix deadline, and a Zbtlink router backdoor ships unauthenticated root shells."
---

## Today's Field Note
Three things demand attention before you close the laptop today. CISA confirms JetBrains TeamCity CVE-2026-63077 (CVSS 9.8, unauthenticated deserialization RCE) is being exploited in the wild, and TeamCity servers are CI/CD crown jewels that hand attackers your build pipeline and signing keys. Separately, CISA gave federal agencies a three-day deadline to fix actively exploited flaws in IBM Langflow, N-central, and Apache Tomcat, so those belong on your KEV triage list regardless of whether you wear a federal badge. And VulnCheck found a factory-shipped backdoor in at least 21 Zbtlink router firmware images spanning two years, beaconing to Chinese infrastructure and opening unauthenticated root shells, which is not a patch problem so much as a rip-and-replace one.

## Today's Action
- Patch on-prem JetBrains TeamCity to the fixed release now, and hunt for anomalous build agents, new admin tokens, and outbound connections from the server.
- Triage the new KEV entries: apply vendor fixes for IBM Langflow, N-central, and Apache Tomcat, or take exposed instances offline until you can.
- Inventory your edge for Zbtlink routers (including white-labeled OEM units) and pull anything you find from production paths.
- Treat CI/CD credentials as potentially exposed: rotate signing keys and API tokens on any TeamCity instance that was internet-facing.
- Block and alert on outbound beacons to the Zbtlink C2 infrastructure listed in VulnCheck's report while you plan replacements.

## Resources

Verified links for the CVEs mentioned above: official advisories, and a live search for public detection rules if any exist yet.

- **CVE-2026-63077**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-63077) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-63077)

*The vulnerability was never the surprise. The uptime was.*

## Related

- [An AI Test Model Broke Into Hugging Face and Nobody Noticed for a Weekend](/itsalreadywhen/2026/08/02/issue-007/)
- [OpenAI's Own Models Broke Out of Their Sandbox and Hacked Hugging Face](/itsalreadywhen/2026/07/26/issue-006/)
- [The 11-byte packet that freezes an OpenSSL server for good](/itsalreadywhen/2026/07/19/issue-005/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*