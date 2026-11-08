---
layout: field_note
title: "Field Note — November 08, 2026"
date: 2026-11-08
summary: "A supply chain compromise at a service provider enabled $133M in fraudulent transactions against French bank Crédit Mutuel Arkéa."
---

## Today's Field Note
Crédit Mutuel Arkéa, a French cooperative bank, got hit for up to $133 million in fraudulent transactions, and the way in was not the bank itself but one of its service providers. This is the familiar pattern: your perimeter holds, your vendor's does not, and the attacker rides a trusted connection straight into money movement. The bank's response was to suspend systems, which tells you the fraud was moving faster than their controls could reconcile. If a third party can initiate or approve transactions on your behalf, that third party is your attack surface, full stop. Expect fewer details than you want and more copycats than you expect.

## Today's Action
- Inventory every third party with the ability to initiate, approve, or reconcile financial transactions, and confirm what authentication sits in front of that access.
- Pull transaction logs for anomalous volume or off-hours activity routed through service provider accounts, not just internal users.
- Verify that large or batched transfers require out-of-band approval that a compromised vendor credential alone cannot satisfy.
- Review and tighten the blast radius of vendor API keys and service accounts: scope, IP allowlisting, and expiry.
- Rehearse the kill switch. Know exactly which systems you can suspend without taking the whole institution dark, before you need to.

*Your perimeter was never the point. Theirs was.*

## Related

- [Privileged Access Management Beyond the Vault](/itsalreadywhen/rtfm/2026/10/28/privileged-access-management-beyond-the-vault/)
- [Least Privilege, Actually Enforced](/itsalreadywhen/rtfm/2026/07/01/least-privilege-actually-enforced/)
- [Third-Party and Vendor Risk Management](/itsalreadywhen/rtfm/2026/07/22/third-party-and-vendor-risk-management/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*