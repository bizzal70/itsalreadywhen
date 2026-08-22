---
layout: field_note
title: "Field Note — August 22, 2026"
date: 2026-08-22
summary: "Check Point's BTR.sys technique weaponizes Microsoft Defender's own signed driver to delete security software at boot, while 9,300+ leaked AWS keys remain live and a new phishing kit plants attacker passkeys for post-reset persistence."
---

## Today's Field Note
Three items rose above the noise today, and none of them require a fancy zero-day. Check Point Research showed that BTR.sys, Microsoft Defender's own legitimately signed boot-time remediation driver, can be steered to perform arbitrary kernel-level file and registry operations on everything from Windows 7 through 11 25H2, meaning an attacker with local admin can quietly delete your security stack at boot with no external driver and no exploited flaw. Meanwhile BleepingComputer confirmed that more than 9,300 AWS access keys leaked between 2022 and 2026 are still active and valid, which is not a vulnerability so much as a slow-motion inventory failure. And a new phishing toolkit, iAuthFlow V2, registers an attacker-controlled passkey so access survives your password resets and session revocations. The theme is durability: attackers are optimizing for staying in, not just getting in.

## Today's Action
- Hunt for anomalous BTR.sys invocations and add detections for the Defender remediation driver being loaded or driven outside of an actual Defender scan; treat local admin as the real blast radius here.
- Rotate and revoke any AWS access keys older than a few months, enforce short-lived credentials via IAM roles, and grep your repos, CI logs, and container images for hardcoded AKIA keys today.
- After any credential-theft incident, audit registered passkeys and FIDO authenticators per account, not just passwords and sessions; revoke anything you cannot attribute to the user.
- Tighten Microsoft Teams external messaging controls and warn users about fake lock-screen prompts (SynkLoader) circulating in Teams phishing.
- Assume a password reset is not containment. Rebuild your incident playbook around removing persistence, not just closing sessions.

*Getting in was never the hard part. Leaving is what they refuse to do.*

## Related

- [Patch Cadence vs. Patch Theater](/itsalreadywhen/rtfm/2026/07/08/patch-cadence-vs-patch-theater/)
- [Least Privilege, Actually Enforced](/itsalreadywhen/rtfm/2026/07/01/least-privilege-actually-enforced/)
- [OpenAI's Own Models Broke Out of Their Sandbox and Hacked Hugging Face](/itsalreadywhen/2026/07/26/issue-006/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*