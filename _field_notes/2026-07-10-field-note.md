---
layout: field_note
title: "Field Note — July 10, 2026"
date: 2026-07-10
summary: "Okta and Bleeping Computer detail active vishing-driven Entra passkey enrollment attacks (O-UNC-066, Helix) hitting Microsoft 365, while attackers actively exploit the 'Ill Bloom' wallet flaw and a poisoned Injective npm package to drain crypto."
---

## Today's Field Note
The phone is the vulnerability again. Okta is tracking O-UNC-066 running a panel-driven phishing kit that calls Microsoft 365 users and walks them through enrolling a rogue Entra passkey, giving the attacker a durable, MFA-resistant credential for data extortion. A separate crew, Helix, is using the same vishing and device-code playbook against SharePoint tenants. Meanwhile the crypto side is bleeding: Coinspect's "Ill Bloom" flaw (weak recovery-phrase randomness) has already funded at least one coordinated sweep, and a compromised Injective Labs GitHub repo pushed a malicious npm package that lifts private keys and seed phrases. None of this is clever. It is people trusting a voice and a package name.

## Today's Action
- Hunt Entra ID sign-in and audit logs for unexpected passkey (FIDO2) registration events; alert on any new credential added outside your enrollment workflow.
- Lock down passkey enrollment to managed devices or supervised sessions, and require help-desk callback verification before any MFA method reset.
- Brief staff that no legitimate IT call will walk them through enrolling a security key or reading a device code aloud; make hanging up the default.
- Audit dependencies for the compromised Injective Labs npm package, purge it, and rotate any wallet keys or seed phrases handled on affected build hosts.
- Move to npm 12 where feasible and confirm install scripts default to off in CI.

*Attackers no longer break the door down. They call and ask you to open it.*