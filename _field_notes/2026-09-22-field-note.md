---
layout: field_note
title: "Field Note — September 22, 2026"
date: 2026-09-22
summary: "Zyxel and Veeam flaws are under active exploitation, and a Microsoft-signed driver is being weaponized to disable EDR before deploying the Rapuncel stealer."
---

## Today's Field Note
CISA added Zyxel GS1900 switch flaw CVE-2026-7273 (stack overflow, arbitrary OS command execution) to the KEV catalog alongside an actively exploited Veeam bug, with a Thursday deadline for federal agencies. Meanwhile a fake LastPass Authenticator installer on GitHub drops a kernel driver signed through Microsoft's own hardware-compatibility program, disables 145 security products, and runs the Rapuncel infostealer. The signed-driver angle is the part worth losing sleep over: it sailed past VirusTotal with zero detections and impersonates at least 40 brands, so your EDR being on is not the same as your EDR being alive. Separately, WordPress patched Click2Shell (CSRF to RCE) and Comment2Shell (CVE-2026-93485), both with public PoCs, in versions 7.1.x. None of this is exotic. All of it is being used now.

## Today's Action
- Patch Zyxel GS1900 switches for CVE-2026-7273 and the exploited Veeam flaw immediately, not by Thursday.
- Update WordPress Core to 7.1.1 or later to close Click2Shell and Comment2Shell (CVE-2026-93485); assume the PoCs are already in scanners.
- Hunt for the malicious signed driver used by the Rapuncel campaign, and add its hash and the impersonated LastPass installer to blocklists.
- Verify EDR agents are actually reporting and heartbeating, not just installed, and alert on driver-load and service-stop events on endpoints.
- Block cross-org sideloading of "authenticator" and "installer" binaries from GitHub via app allowlisting.

## Resources

Verified links for the CVEs mentioned above: official advisories, and a live search for public detection rules if any exist yet.

- **CVE-2026-7273**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-7273) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-7273)
- **CVE-2026-93485**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-93485) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-93485)

*Signed drivers do not mean signed off. Check the pulse, not the icon.*

## Related

- [AI Agents Left 18,000 Posts on a Dead German Wiki to Coordinate Their Escape](/itsalreadywhen/2026/09/06/issue-012/)
- [OpenAI's Own Models Broke Out of Their Sandbox and Hacked Hugging Face](/itsalreadywhen/2026/07/26/issue-006/)
- [700 OpenAI Agents Coordinated a Real Attack on Hugging Face](/itsalreadywhen/2026/08/30/issue-011/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*