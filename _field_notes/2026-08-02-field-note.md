---
layout: field_note
title: "Field Note — August 02, 2026"
date: 2026-08-02
summary: "A firmware PRNG flaw in Coldcard hardware wallets enabled a $70M Bitcoin sweep across 1,196 addresses in 41 minutes."
---

## Today's Field Note
Galaxy Research tied a 41-minute, $70.2 million Bitcoin sweep on July 30 to a March 2021 firmware integration error in Coinkite's Coldcard wallet. The bug routed seed generation to a deterministic software PRNG instead of true entropy, meaning every affected wallet's keys were predictable to anyone who reconstructed the seed space. This is not a phishing event or a lost passphrase. It is the entire premise of a hardware wallet (unpredictable, air-gapped key generation) failing silently for years. If your seed was generated on vulnerable firmware, the money was gone the moment you funded the address, and 1,196 holders just found that out in under an hour.

## Today's Action
- Identify any Coldcard wallet whose seed was generated on firmware from the March 2021 window, and treat those seeds as compromised regardless of current balance.
- Do not "move funds to safety" using the same seed. Generate a fresh seed on patched, verified firmware and sweep to entirely new addresses.
- Verify firmware authenticity and version directly against Coinkite's published advisory before trusting any device that held value.
- Audit organizational crypto custody: inventory every hardware wallet, its make, model, and firmware provenance, not just its current balance.
- Watch for opportunistic phishing impersonating Coinkite "recovery" or "migration" support in the coming days.

*Cold storage is only as cold as its worst random number.*

## Related

- [An AI Test Model Broke Into Hugging Face and Nobody Noticed for a Weekend](/itsalreadywhen/2026/08/02/issue-007/)
- [Third-Party and Vendor Risk Management](/itsalreadywhen/rtfm/2026/07/22/third-party-and-vendor-risk-management/)
- [Logging Without Anyone Reading the Logs](/itsalreadywhen/rtfm/2026/07/15/logging-without-anyone-reading-the-logs/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*