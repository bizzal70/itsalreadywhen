---
layout: field_note
title: "Field Note — October 25, 2026"
date: 2026-10-25
summary: "A new UEFI bootkit called BlackX is exploiting the old Baton Drop (CVE-2022-21894) flaw to bypass Secure Boot in an active espionage campaign."
---

## Today's Field Note
BlackX is a fresh UEFI bootkit caught in an espionage campaign in early 2026, and it is not using anything new to get in. It rides Baton Drop (CVE-2022-21894), a Secure Boot bypass that Microsoft patched back in 2022, which means the vulnerable bootloaders are still trusted on machines that never applied the revocations. Once resident, BlackX loads a malicious driver built to interfere with Kaspersky and Avast protections, giving attackers persistence that survives reinstalls and sits below your EDR. The lesson is boring and familiar: a four-year-old bug is still good enough when nobody updated the DBX. Firmware-level persistence is expensive to detect after the fact, so the cheap win is denying the entry point now.

## Today's Action
- Apply the Secure Boot DBX revocation updates (KB5025885 and the subsequent rollups) to revoke the vulnerable bootloaders abused by Baton Drop (CVE-2022-21894).
- Confirm Secure Boot is actually enabled and enforcing across your fleet, not just present in firmware, and flag any machines where it is disabled.
- Hunt for tampering with Kaspersky and Avast agents: unexpected service stops, driver load failures, or missing telemetry are your early signals.
- Pull firmware and boot integrity measurements where you have TPM attestation, and compare against known-good baselines for high-value hosts.
- Prioritize remediation on endpoints that have never received post-2022 DBX updates, since those are the ones still trusting the old shim.

## Resources

Verified links for the CVEs mentioned above: official advisories, and a live search for public detection rules if any exist yet.

- **CVE-2022-21894**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2022-21894) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2022-21894)

*The vulnerability was patched in 2022. The patch, apparently, was optional.*

## Related

- [ShinyHunters Hacked Clop, Then Robbed the Ransoms Twice](/itsalreadywhen/2026/09/27/issue-015/)
- [AI Agents Left 18,000 Posts on a Dead German Wiki to Coordinate Their Escape](/itsalreadywhen/2026/09/06/issue-012/)
- [An AI Test Model Broke Into Hugging Face and Nobody Noticed for a Weekend](/itsalreadywhen/2026/08/02/issue-007/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*