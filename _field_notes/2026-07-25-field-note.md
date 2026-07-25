---
layout: field_note
title: "Field Note â€” July 25, 2026"
date: 2026-07-25
summary: "A public PoC for an authenticated RCE in self-managed GitLab lands the same day as an active hotel Wi-Fi DNS campaign harvesting Microsoft 365 credentials."
---

## Today's Field Note
Yuhang Wu at depthfirst dropped a working PoC for an authenticated RCE in self-managed GitLab 18.11.3. No admin rights, no CI runner access, no victim interaction: an ordinary user commits two crafted Jupyter notebooks, requests the diff, and runs commands as `git`. That is every internal repo server with self-registration turned on. Separately, attackers are rewriting DNS on hotel and conference-center Wi-Fi to serve fake Microsoft 365 login pages, so your traveling execs are the soft target this week. Neither of these waits for your patch window.

## Today's Action
- Inventory self-managed GitLab instances, confirm versions, and apply the fixed release now. Do not trust "internal only" as mitigation.
- Disable open self-registration on GitLab and audit recently created accounts and any new Jupyter notebook commits with diff requests.
- Remind traveling staff: never authenticate to Microsoft 365 through a captive portal or unexpected login prompt on hotel Wi-Fi. Route them through VPN.
- Enforce phishing-resistant MFA (FIDO2/passkeys) on M365 so a cloned login page nets nothing usable.
- Hunt for anomalous M365 sign-ins from hospitality-area IPs and impossible-travel patterns over the last two weeks.

*Two ways in today, and neither of them knocked.*

## Related

- [Least Privilege, Actually Enforced](/itsalreadywhen/rtfm/2026/07/01/least-privilege-actually-enforced/)
- [The 11-byte packet that freezes an OpenSSL server for good](/itsalreadywhen/2026/07/19/issue-005/)
- [MFA Fatigue and Push-Bombing](/itsalreadywhen/rtfm/2026/06/30/mfa-fatigue-and-push-bombing/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*