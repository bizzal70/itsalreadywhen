---
layout: field_note
title: "Field Note — October 27, 2026"
date: 2026-10-27
summary: "CISA confirms active exploitation of two critical PHP2Shell RCE flaws while a related Brotli bug (HTTP2Shell/Broccoli2Shell) forces emergency patches across PHP, Node.js, and .NET."
---

## Today's Field Note
CISA put both PHP2Shell flaws (CVE-2026-109618 and its sibling, each CVSS 9.2) on the KEV list, which means unauthenticated RCE is no longer theoretical, it is happening. Siemens, Schneider Electric, and ABB have already confirmed affected products, so this bleeds straight into OT where patching is slow and attackers know it. Running parallel to this is a Brotli decoder bug (CVE-2026-111497, variously branded HTTP2Shell, Broccoli2Shell, and Node2Shell) that has triggered emergency fixes across PHP for Windows, Node.js, and .NET. The same compression library landing in three ecosystems at once means your exposure is wider than your inventory probably shows. Federal agencies have a Thursday deadline on PHP2Shell; treat that as your own.

## Today's Action
- Patch PHP2Shell (CVE-2026-109618 and sibling) on all internet-facing PHP deployments now, ahead of CISA's Thursday deadline, and check vendor advisories from Siemens, Schneider, and ABB for embedded instances.
- Apply the Brotli fixes (CVE-2026-111497) across PHP 8.2 to 8.5 Windows builds, Node.js, and .NET runtimes; rebuild containers that bundle these.
- Hunt for exploitation of PHP2Shell: review web server logs for anomalous requests and OOM crashes on affected endpoints before you assume you patched in time.
- Audit where Brotli decompression is reachable, particularly cURL with automatic HTTP response decompression enabled, and confirm defaults have not been overridden.
- Inventory OT and industrial systems for bundled PHP; assume anything you cannot patch today needs network isolation.

## Resources

Verified links for the CVEs mentioned above: official advisories, and a live search for public detection rules if any exist yet.

- **CVE-2026-109618**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-109618) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-109618)
- **CVE-2026-111497**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-111497) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-111497)

*You can't patch what you forgot you shipped.*

## Related

- [ShinyHunters Hacked Clop, Then Robbed the Ransoms Twice](/itsalreadywhen/2026/09/27/issue-015/)
- [OpenAI's Own Models Broke Out of Their Sandbox and Hacked Hugging Face](/itsalreadywhen/2026/07/26/issue-006/)
- [700 OpenAI Agents Coordinated a Real Attack on Hugging Face](/itsalreadywhen/2026/08/30/issue-011/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*