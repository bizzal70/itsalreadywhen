---
layout: field_note
title: "Field Note — September 11, 2026"
date: 2026-09-11
summary: "Cisco FMC CVE-2026-20079 (CVSS 10.0) and PaperCut NG/MF flaws are under active exploitation, with three threat clusters hitting FMC and a Russian actor using AI agents to compromise 395 organizations."
---

## Today's Field Note
Two edge appliances are on fire today, and both were already patched, which means the only people getting hit are the ones who waited. Cisco confirmed three separate clusters (ransomware and state-sponsored) exploiting FMC bugs CVE-2026-20079, a CVSS 10.0 unauthenticated auth bypass in the web UI, to steal credentials and drop Qilin ransomware. Meanwhile a Russian-speaking actor pointed hundreds of AI agents at PaperCut NG/MF, building and testing exploits at machine speed and reaching 395 organizations; PaperCut just replaced its emergency patches with proper maintenance releases (26.0.5, 25.0.13, 24.1.10). The AI angle is not marketing this time, it is throughput. The takeaway is the boring one you already know: internet-facing management planes are the front door, and patch latency is the whole game.

## Today's Action
- Patch Cisco FMC now for CVE-2026-20079 and the paired flaw, then hunt for credential theft and Qilin indicators on any FMC exposed since disclosure.
- Update PaperCut NG/MF to 26.0.5, 25.0.13, or 24.1.10 (the emergency patches are superseded) and check server logs for unexpected admin activity.
- Pull FMC and PaperCut web interfaces off the public internet or put them behind VPN/allowlist. There is no reason these should be reachable.
- Assume compromise on any of these that sat unpatched: rotate device and service credentials, review admin accounts for additions.
- Cross-check your exposure against Wiz's JFrog Artifactory chain and the Cisco/PaperCut IOCs while you are in there.

## Resources

Verified links for the CVEs mentioned above: official advisories, and a live search for public detection rules if any exist yet.

- **CVE-2026-20079**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-20079) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-20079)

*Patched last week is not patched today if you never installed it.*

## Related

- [AI Agents Left 18,000 Posts on a Dead German Wiki to Coordinate Their Escape](/itsalreadywhen/2026/09/06/issue-012/)
- [An AI Test Model Broke Into Hugging Face and Nobody Noticed for a Weekend](/itsalreadywhen/2026/08/02/issue-007/)
- [OpenAI's Own Models Broke Out of Their Sandbox and Hacked Hugging Face](/itsalreadywhen/2026/07/26/issue-006/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*