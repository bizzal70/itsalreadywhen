---
layout: field_note
title: "Field Note — September 06, 2026"
date: 2026-09-06
summary: "An unpatched StyleSmuggler zero-day is backdooring Magento and Adobe Commerce stores, MikroTik routers are being hijacked over exposed SSH, and JetBrains got breached through its own unpatched TeamCity."
---

## Today's Field Note
Three unauthenticated pre-auth problems land on the same day, and none of them wait for your change window. Sansec's StyleSmuggler is an unpatched zero-day in Magento Open Source and Adobe Commerce that runs code on the storefront server with no login, with active exploitation since September 4 and no vendor fix yet. CERT Polska separately warns that internet-exposed MikroTik SSH is being taken over for full admin with no authentication, hits confirmed from September 2. And JetBrains, the people who make TeamCity, got breached through their own unpatched TeamCity and are now telling Cadence users to rotate every credential, which is a useful reminder that "we shipped the patch" and "we applied the patch" are different sentences.

## Today's Action
- Magento/Adobe Commerce: apply Sansec's StyleSmuggler mitigations now, hunt for unexpected admin users, injected template code, and new files under app/ and pub/ since September 4.
- MikroTik: pull SSH off the public internet immediately, restrict to management VLAN or VPN, then audit for unknown admin accounts, scripts, and scheduled tasks.
- TeamCity: confirm you are actually patched against the recently disclosed critical flaw, not just downloaded it, and check exposure to the internet.
- If you run Cadence or any TeamCity-driven pipeline, revoke and rotate all credentials and secrets, especially AWS keys, per JetBrains' guidance.
- Log every one of these external services and diff against a known-good baseline before you trust a clean scan.

*Patched and applied are two different words. Check which one you actually did.*

## Related

- [OpenAI's Own Models Broke Out of Their Sandbox and Hacked Hugging Face](/itsalreadywhen/2026/07/26/issue-006/)
- [AI Agents Left 18,000 Posts on a Dead German Wiki to Coordinate Their Escape](/itsalreadywhen/2026/09/06/issue-012/)
- [When AI Agents Start Hacking Real People Without Being Told To](/itsalreadywhen/2026/08/23/issue-010/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*