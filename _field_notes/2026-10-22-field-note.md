---
layout: field_note
title: "Field Note — October 22, 2026"
date: 2026-10-22
summary: "PHP2Shell (CVE-2026-109618/109619) is under active exploitation across ~70% of websites, GitLab ships a CVSS 10.0 unauthenticated RCE fix, and LiteLLM's pipeline was compromised to push a credential-stealing package."
---

## Today's Field Note
Three things are on fire today, and PHP2Shell is the biggest. CVE-2026-109618 and CVE-2026-109619 hit the PHP core that roughly 70% of the web runs, working exploits are public, and exploitation started October 17 (four days before disclosure), caught in Amazon's MadPot honeypot from a commercial anonymization network. Patches are out, mass scanning followed within hours, and expect a lot of 404s today as admins pull sites offline to patch. Separately, GitLab shipped a CVSS 10.0 unauthenticated RCE affecting every self-managed version back to 7.0 (2014), and the October 12 fix only covered 19.2+, so a second bump is required even if you patched nine days ago. And LiteLLM 1.107.0 was compromised on PyPI and Docker Hub with a credential stealer and backdoor, likely via a leaked GitHub token in AI gateway logs.

## Today's Action
- Patch PHP now to the fixed releases for CVE-2026-109618 and CVE-2026-109619; if you cannot patch immediately, take exposed apps offline rather than leave them reachable.
- Grep web and WAF logs back to October 17 for exploitation attempts; assume probing, not just scanning, on anything internet-facing.
- Update self-managed GitLab to the new fixed versions one patch above the October 12 release; patching on the 12th is not sufficient.
- Pull LiteLLM 1.107.0 from your environments (PyPI and Docker), rotate any credentials that touched those hosts, and audit GitHub tokens exposed in AI gateway or LLM logs.
- Treat Plex (Plex2Shell, now on CISA's radar) as next in line and confirm Plex Media Server is patched.

## Resources

Verified links for the CVEs mentioned above: official advisories, and a live search for public detection rules if any exist yet.

- **CVE-2026-109618**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-109618) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-109618)
- **CVE-2026-109619**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-109619) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-109619)

*Patch the thing everyone runs first. The exotic bugs can wait.*

## Related

- [ShinyHunters Hacked Clop, Then Robbed the Ransoms Twice](/itsalreadywhen/2026/09/27/issue-015/)
- [AI Agents Left 18,000 Posts on a Dead German Wiki to Coordinate Their Escape](/itsalreadywhen/2026/09/06/issue-012/)
- [OpenAI's Own Models Broke Out of Their Sandbox and Hacked Hugging Face](/itsalreadywhen/2026/07/26/issue-006/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*