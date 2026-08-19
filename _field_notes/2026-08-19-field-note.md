---
layout: field_note
title: "Field Note — August 19, 2026"
date: 2026-08-19
summary: "CISA flags active exploitation of a critical Windows IKE RCE while Clop's Windchill web shell and MLflow SSRF attacks show the mass-exploitation crews are already inside."
---

## Today's Field Note
CISA added a critical Windows IKE Service Extensions RCE to the KEV list, and it is being exploited now, which means the IPsec stack you assumed was boring is a live entry point. Meanwhile Clop is running true to form: ReliaQuest and BleepingComputer both confirm a purpose-built JSP web shell for PTC Windchill and FlexPLM that decrypts stored credentials, maps vaults, and stages files for extortion. On the AI/ML side, watchTowr and VulnCheck report active scanning and exploitation of an MLflow SSRF flaw being used to lift cloud credentials, so your data-science sandbox is now a cloud-takeover vector. None of these are theoretical. All three have attackers on the keyboard today.

## Today's Action
- Patch the Windows IKE Extensions RCE across all IPsec/VPN endpoints per CISA KEV timelines; if you cannot patch immediately, restrict IKE (UDP 500/4500) exposure at the edge.
- Hunt PTC Windchill and FlexPLM servers for unexpected JSP files, then rotate every credential those systems could decrypt or reach.
- Update MLflow and place it behind authentication; audit outbound requests from MLflow hosts and rotate any cloud keys or instance-metadata-derived credentials it could touch.
- Push Chrome (two critical buffer overflows) and Apple iOS/iPadOS/macOS Tahoe (image-processing RCE) updates to managed fleets now, not next cycle.
- If you run self-managed GitLab, track CVE-2026-19478; detection is hard, so prioritize upgrading over hoping to spot the zero-click.

## Resources

Verified links for the CVEs mentioned above: official advisories, and a live search for public detection rules if any exist yet.

- **CVE-2026-19478**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-19478) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-19478)

*The stack you called boring is the one they logged into first.*

## Related

- [OpenAI's Own Models Broke Out of Their Sandbox and Hacked Hugging Face](/itsalreadywhen/2026/07/26/issue-006/)
- [SIM Cards, Gym Bots, and a Polish Turbine That Stopped Turning](/itsalreadywhen/2026/08/16/issue-009/)
- [An AI Test Model Broke Into Hugging Face and Nobody Noticed for a Weekend](/itsalreadywhen/2026/08/02/issue-007/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*