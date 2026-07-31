---
layout: field_note
title: "Field Note — July 27, 2026"
date: 2026-07-27
summary: "A threat actor is hijacking public Wi-Fi captive portals to phish Microsoft 365 credentials from traveling staff, while healthcare breaches at DentaQuest and MCBS expose over 24 million people."
---

## Today's Field Note
The interesting one today is quiet: a threat actor has compromised public Wi-Fi gateway appliances and is using the captive portal login flow to harvest Microsoft 365 credentials from traveling employees. This is the airport lounge and hotel lobby coming home to your tenant, and it sails right past anyone who trusts "the network prompted me to sign in." Meanwhile the healthcare data keeps pouring out: DentaQuest lost personal and dental records on potentially 23 million people, and the PEAR group claims 3 TB from MCBS affecting 1.2 million more. None of this needs a novel exploit, just users who type passwords into whatever asks and identity controls that permit it.

## Today's Action
- Enforce phishing-resistant MFA (FIDO2 or certificate-based) on Microsoft 365 so a harvested password alone is useless.
- Brief traveling staff now: captive portals never ask for corporate credentials, only for accepting terms.
- Hunt Entra sign-in logs for M365 auths from hotel, airport, and conference ISP ranges paired with unusual geovelocity.
- Confirm your vendor and BAA inventory covers DentaQuest and MCBS-style third parties, and check for downstream exposure notices.
- Push VPN-always-on or Zero Trust access for remote staff so untrusted local gateways never see auth traffic.

*The network asked politely, and that was the whole trick.*

## Related

- [Third-Party and Vendor Risk Management](/itsalreadywhen/rtfm/2026/07/22/third-party-and-vendor-risk-management/)
- [Least Privilege, Actually Enforced](/itsalreadywhen/rtfm/2026/07/01/least-privilege-actually-enforced/)
- [MFA Fatigue and Push-Bombing](/itsalreadywhen/rtfm/2026/06/30/mfa-fatigue-and-push-bombing/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*