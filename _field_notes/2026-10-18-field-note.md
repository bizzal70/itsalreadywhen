---
layout: field_note
title: "Field Note — October 18, 2026"
date: 2026-10-18
summary: "ConnectWise disabled seven application identities after attackers used them to compromise Microsoft 365 tenants, and Drupal patched two critical RCE flaws."
---

## Today's Field Note
ConnectWise pulled the plug on its Cloud Backup service (formerly SkyKick) after unknown actors got hold of application identities and used them to breach customer Microsoft 365 tenants. Seven app identities are now disabled, including ConnectWise Cloud Backup (506e08f9-6e9a-4da4-942b-a099a03644ae). This is the supply-chain pattern that keeps working: compromise the trusted third party, inherit its OAuth consent, skip the login screen entirely. Meanwhile Drupal shipped fixes for two critical RCE flaws affecting all supported versions, with maintainers openly warning exploits are likely soon. No PoC yet, but "patches landed, exploits coming" is a short runway, so treat it as a clock already running.

## Today's Action
- In Entra ID, audit service principals and OAuth grants for the seven disabled ConnectWise app identities (starting with 506e08f9-6e9a-4da4-942b-a099a03644ae) and revoke any lingering consent or tokens.
- Pull Microsoft 365 sign-in and audit logs for activity tied to those app identities and flag any unexpected mail rules, data access, or admin changes.
- If you run ConnectWise Cloud Backup / SkyKick, assume exposure until proven otherwise and rotate affected tenant secrets.
- Patch all Drupal installs to the fixed releases now, before a PoC lands, and prioritize internet-facing sites.
- Review any other vendor-owned app registrations in your tenant and strip unused or over-permissioned consent.

*The trusted third party is just your attack surface with an invoice.*

## Related

- [ShinyHunters Hacked Clop, Then Robbed the Ransoms Twice](/itsalreadywhen/2026/09/27/issue-015/)
- [The 11-byte packet that freezes an OpenSSL server for good](/itsalreadywhen/2026/07/19/issue-005/)
- [SIM Cards, Gym Bots, and a Polish Turbine That Stopped Turning](/itsalreadywhen/2026/08/16/issue-009/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*