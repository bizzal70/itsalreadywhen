---
layout: field_note
title: "Field Note — September 29, 2026"
date: 2026-09-29
summary: "Apple patched an actively exploited CoreGraphics zero-day (CVE-2026-86950) while thousands of Supabase databases sit wide open and the MCP Python SDK leaks OAuth secrets."
---

## Today's Field Note
Apple shipped emergency fixes for CVE-2026-86950, an out-of-bounds write in CoreGraphics reported by Meta and used in what Apple politely calls "extremely sophisticated" targeted attacks. That is the usual language for commercial spyware hitting a short list of high-value phones, so it matters most if you carry journalists, execs, or dissidents on your roster. Meanwhile the boring stuff keeps bleeding: researchers found over 16,000 misconfigured Supabase databases exposing PII, passwords, and auth tokens to anyone who asks. And the MCP Python SDK (fixed in 1.30.0) was shipping client secrets and PKCE keys to attacker-controlled token endpoints, which is the kind of supply-chain footgun that scales as fast as everyone's rush to bolt agents onto everything.

## Today's Action
- Push the Apple updates (iOS, iPadOS, macOS) to all managed devices now, and prioritize high-risk users first.
- Inventory any apps built on the MCP Python SDK and bump to 1.30.0 or later; rotate any OAuth client secrets that may have leaked.
- Audit your Supabase deployments: enforce Row Level Security, check for publicly readable tables, and rotate exposed service keys.
- Confirm your MDM can verify the CoreGraphics patch landed rather than just marking it "assigned."
- If you have targeted-attack risk (execs, journalists, activists), enable Lockdown Mode on their Apple devices.

## Resources

Verified links for the CVEs mentioned above: official advisories, and a live search for public detection rules if any exist yet.

- **CVE-2026-86950**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-86950) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-86950)

*Patch the phones, close the buckets, rotate the secrets. Same list, new day.*

## Related

- [ShinyHunters Hacked Clop, Then Robbed the Ransoms Twice](/itsalreadywhen/2026/09/27/issue-015/)
- [AI Agents Left 18,000 Posts on a Dead German Wiki to Coordinate Their Escape](/itsalreadywhen/2026/09/06/issue-012/)
- [The Week AI Broke Into OpenAI, Google, and a Spanish Company](/itsalreadywhen/2026/09/20/issue-014/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*