---
layout: field_note
title: "Field Note — October 04, 2026"
date: 2026-10-04
summary: "ShinyHunters suspect 'Rey' detained in Jordan and cooperating with the FBI, while China-aligned TA419 runs AitM phishing against U.S. AI policy experts."
---

## Today's Field Note
Two things worth your attention, both human-shaped rather than CVE-shaped. A suspected ShinyHunters member known as "Rey" (Saif al-Din Khader) was reportedly detained in Jordan on September 29 and is now helping the FBI identify other members. Cooperating informants mean leaked chat logs, reused infrastructure, and operator aliases are suddenly in play, so expect attribution and possibly more arrests to follow. Separately, China-aligned TA419 is running Microsoft Adversary-in-the-Middle (AitM) phishing against AI policy experts at U.S. think tanks, universities, and legal orgs, impersonating named economists and even an Anthropic employee. AitM defeats basic MFA by relaying your session token in real time, so if your threat model includes AI governance or policy work, treat inbound "colleague" mail with suspicion.

## Today's Action
- Audit your org against ShinyHunters TTPs: review Salesforce/Snowflake-style SaaS access logs and rotate any credentials tied to prior exposure.
- Move high-risk users (policy, research, legal, exec) to phishing-resistant MFA (FIDO2/passkeys) that AitM proxies cannot replay.
- Enforce Conditional Access with device compliance and session binding in Entra ID to blunt stolen token reuse.
- Hunt for anomalous sign-ins: impossible travel, new OAuth grants, and sessions from reverse-proxy infrastructure (Evilginx-style patterns).
- Brief staff working AI policy topics specifically: TA419 is impersonating known names, so verify unexpected outreach out-of-band.

*Informants talk and session tokens travel. Assume both.*

## Related

- [Identity Is the New Perimeter](/itsalreadywhen/rtfm/2026/09/23/identity-is-the-new-perimeter/)
- [Least Privilege, Actually Enforced](/itsalreadywhen/rtfm/2026/07/01/least-privilege-actually-enforced/)
- [AI Agents Learned to Pick Locks This Week, and Nobody Taught Them](/itsalreadywhen/2026/10/04/issue-016/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*