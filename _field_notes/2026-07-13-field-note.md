---
layout: field_note
title: "Field Note — July 13, 2026"
date: 2026-07-13
summary: "CISA adds two max-severity Joomla extension flaws (CVE-2026-48939 and iCagenda) to KEV after zero-day exploitation, while Progress tells ShareFile customers to shut down servers over a credible threat."
---

## Today's Field Note
Two Joomla extension flaws, iCagenda and Balbooa Forms, are on CISA's KEV as of today, both CVSS 10.0, both exploited as zero-days for remote code execution (CVE-2026-48939 among them). These are unauthenticated RCE bugs in third-party extensions, which means the vulnerable surface is exactly the sort of thing that never made it into your asset inventory. Separately, Progress is telling ShareFile customers to manually power off their Storage Zone Controllers over a "credible threat," which is the kind of guidance vendors only issue when they already know something bad is in flight. Neither of these waits for your patch window.

## Today's Action
- Inventory every Joomla install for the iCagenda and Balbooa Forms extensions, then patch or remove them immediately; treat unpatched instances as already-touched.
- Pull web and application logs for those extensions and hunt for anomalous POSTs and unexpected file writes since exploitation predates the KEV listing.
- Follow Progress guidance and shut down ShareFile Storage Zone Controllers now if you run them, pending their investigation; do not wait for a formal patch.
- Review the Lexfo Evilginx findings and check M365 sign-in logs for adversary-in-the-middle session token theft against your tenant.
- Confirm your externally facing routers are patched and hardened per the joint US-and-allies advisory on Russian state targeting of misconfigured edge devices.

## Resources

Verified links for the CVEs mentioned above: official advisories, and a live search for public detection rules if any exist yet.

- **CVE-2026-48939**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-48939) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-48939)

*Your inventory is a lie by omission; the attackers already read the appendix.*