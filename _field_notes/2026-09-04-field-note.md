---
layout: field_note
title: "Field Note — September 04, 2026"
date: 2026-09-04
summary: "Chrome V8 zero-day CVE-2026-85046 is under active exploitation while attackers hammer WordPress Elementor Pro and Super Forms RCE flaws with over 440,000 attempts."
---

## Today's Field Note
Three things need patching before you clock out. Google shipped a fix for CVE-2026-85046, a type confusion bug in V8 already exploited in the wild, which means every unpatched Chrome and Chromium-derived browser in your fleet is a live entry point. Meanwhile Wordfence is watching over 440,000 exploit attempts against two WordPress plugins: CVE-2026-14894 (CVSS 9.8) in Super Forms and CVE-2026-32475 in Elementor Pro, the latter confirmed dropping webshells and running arbitrary commands. Separately, Coder's Cloudflare infrastructure was compromised to serve malicious Terraform modules with credential-stealing code, so if you pulled Coder modules recently, assume those creds are gone. None of this is theoretical. It is all being used right now.

## Today's Action
- Push Chrome/Chromium to 152.0.7977.82 or later across the fleet today, and force-restart browsers so the patch actually loads.
- Update Elementor Pro and Super Forms immediately; hunt for unexpected files in upload directories and web shells before you assume you patched in time.
- If you use Coder, rotate any credentials touched by Terraform runs and audit registry sources for unauthorized servers added via the Cloudflare compromise.
- Check WAF and web logs for the 440,000-plus exploit attempts pattern against WordPress endpoints; block and investigate hits.
- Pull Chrome telemetry to confirm real deployment, not just policy push.

## Resources

Verified links for the CVEs mentioned above: official advisories, and a live search for public detection rules if any exist yet.

- **CVE-2026-14894**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-14894) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-14894)
- **CVE-2026-32475**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-32475) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-32475)
- **CVE-2026-85046**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-85046) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-85046)

*You patch tonight or you incident-respond next week. Same work, worse hours.*

## Related

- [OpenAI's Own Models Broke Out of Their Sandbox and Hacked Hugging Face](/itsalreadywhen/2026/07/26/issue-006/)
- [An AI Test Model Broke Into Hugging Face and Nobody Noticed for a Weekend](/itsalreadywhen/2026/08/02/issue-007/)
- [SIM Cards, Gym Bots, and a Polish Turbine That Stopped Turning](/itsalreadywhen/2026/08/16/issue-009/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*