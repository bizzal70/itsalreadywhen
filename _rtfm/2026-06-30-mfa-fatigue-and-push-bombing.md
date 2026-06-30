---
layout: rtfm
title: "MFA Fatigue and Push-Bombing"
date: 2026-06-30
summary: "Push-based MFA was supposed to kill phishing and credential reuse, but by turning authentication into a single fatigued tap, it became a new attack surface — and NIST has been quietly telling you to fix it for years."
framework: "NIST SP 800-63B (Digital Identity Guidelines)"
framework_url: "https://pages.nist.gov/800-63-3/sp800-63b.html"
---

# It's Already When.

We bolted push notifications onto authentication because passwords were a disaster and SMS one-time codes were worse, and for a brief, hopeful moment it looked like we'd solved something. Then attackers discovered that a button which says *Approve* will, given enough requests at 3 a.m., eventually get pressed. The control we deployed to stop credential theft became a control that launders credential theft into account takeover, one weary thumb at a time. This is not a failure of the technology so much as a failure to read the manual that shipped with it.

## The Standard

NIST Special Publication 800-63B — the *Digital Identity Guidelines*, Authentication and Lifecycle Management volume — does not actually contain a control called "push MFA." It never did. What it defines are *authenticators*, classed by Authenticator Assurance Level (AAL), with specific requirements around phishing resistance, verifier impersonation, and what the document calls "authentication intent."

Two concepts in 800-63B matter most here, and almost nobody implementing push notifications reads them.

The first is **phishing resistance**, formalized in the AAL3 requirements and discussed throughout §5. An authenticator is phishing-resistant when the authentication protocol cryptographically binds the verifier's identity into the ceremony — so a credential proven to one party cannot be replayed against another. WebAuthn/FIDO2 does this via channel binding to the origin. A push notification does not. A push approval is a bare yes/no decision divorced from any cryptographic context about *who* is asking and *why*.

The second is **authentication intent**, defined in §5.2.9. NIST is explicit: the authentication process should "establish that the claimant is the entity attempting to authenticate" — that the human pressing the button actually initiated the login. A naked push prompt establishes that *someone* has the phone and is willing to tap. It establishes nothing about intent.

800-63B also restricts what it calls **out-of-band authenticators** (§5.1.3) and is openly skeptical of unauthenticated approval flows. The document has, across revisions, steadily downgraded the standing of anything that relies on a user making a security decision under ambiguity. The standard, in other words, told you the simple push prompt was weak. You shipped it anyway because the UX was clean.

## Where It Breaks Down

The failures are specific and they repeat across organizations like a liturgy.

**Simple approve/deny with no context.** The dominant deployment pattern is a single prompt: *Sign-in request — Approve / Deny*. No number to match, no location, no application name, no request count. The user has been trained by hundreds of legitimate prompts to treat the button as a speed bump. Attackers who have already harvested the password — via a reverse proxy phishing kit, credential stuffing, or an infostealer dump — simply replay the login and wait. This is **push-bombing** (or MFA fatigue): fire the authentication attempt repeatedly until the prompt becomes an annoyance the user dismisses by approving it.

**No rate limiting on push generation.** Many IdP configurations will happily emit a push notification on every authentication attempt with no throttling, no exponential backoff, and no lockout after N rejected or unanswered prompts. The attacker controls the volume. The user controls only their patience, which is finite.

**Self-service enrollment with no binding integrity.** 800-63B §6.1 is specific about binding authenticators to identities with appropriate assurance. In practice, enrollment frequently happens over the same weak first factor it's supposed to strengthen — a user with a phished password enrolls the *attacker's* device because the enrollment flow only re-verified the password. Now the second factor belongs to the adversary, permanently, and the legitimate user never sees a prompt.

**Fallback paths that defeat the control entirely.** The strong factor is push; the fallback is SMS OTP, or worse, an email magic link, or a help-desk reset with knowledge-based verification. Attackers don't attack your strongest authenticator. They attack the weakest one you'll accept, and 800-63B's whole AAL model collapses the moment a high-assurance session can be established through a low-assurance recovery flow.

**Conflating "we have MFA" with AAL2 or AAL3.** Organizations check the MFA box for compliance and assume they've reached an assurance level. A bare push notification is, on a good day, a marginal AAL2 implementation — and only if you ignore the verifier impersonation concerns. It is categorically not AAL3 because it is not phishing-resistant. The audit said "MFA: yes." The threat model didn't care.

**No telemetry on prompt rejection.** A user who declines five prompts in two minutes is a screaming signal. Most deployments log the eventual *approval* and discard the pattern of preceding denials. The single most valuable detection signal for push-bombing is routinely thrown on the floor.

## Doing It Right

You do not need to rip everything out tomorrow. You need to stop treating the bare prompt as adequate and start aligning to what 800-63B actually asks for.

**Move to phishing-resistant authenticators wherever you can.** This means FIDO2/WebAuthn with hardware security keys or platform authenticators (passkeys backed by a TPM or secure enclave), bound to the relying party's origin. This is the only category 800-63B treats as genuinely phishing-resistant at AAL3. For privileged accounts, administrators, and anything touching identity infrastructure itself, this is not optional — it is the point.

**If you must run push, run number matching — properly.** Number-matching forces the user to read a value from the login screen and type it into the prompt, which restores a thin layer of authentication intent (§5.2.9) and breaks pure-volume push-bombing. Pair it with **contextual display**: application name, geographic location, IP, and a visible count of recent attempts. Context is what lets a tired human make the decision the standard assumes they're making.

**Rate-limit and backoff on the verifier side.** Cap push generation per account per interval. Implement exponential backoff. After a threshold of denied or ignored prompts, lock the authentication flow and require step-up or administrative intervention — not another prompt. This is the throttling 800-63B §5.2.2 contemplates for verifier compromise resistance, applied to the push channel.

**Fix enrollment and recovery to match the assurance you claim.** Authenticator binding (§6.1) should require an existing strong factor, not just a password. Recovery flows must not establish a session at a higher AAL than the recovery method's own assurance. Kill KBA. Route account recovery through verified, supervised channels for high-value accounts. The recovery path is the real authenticator; treat it that way.

**Instrument prompt rejection and surface it.** Feed denied-prompt patterns, impossible-travel signals, and prompt-storm bursts into your SIEM or ITDR tooling. Alert on the burst, not just the breach. The fatigue attack has a loud, recognizable signature *before* the fatal approval — if anyone is looking.

**Bind sessions and shorten their reach.** Pair strong authentication with token binding, conditional access policies keyed to device posture, and aggressive re-authentication for sensitive operations. A phished session token is its own attack class; phishing-resistant login means nothing if the resulting bearer token roams freely for thirty days.

## The Bottom Line

Push-based MFA didn't fail because it was a bad idea. It failed because we deployed the convenient version, declared victory, and stopped reading at the part of 800-63B that explains why the convenient version doesn't work. The guidance was on the table the whole time. The control became the thing it was meant to prevent precisely because we optimized for the tap and not for the intent behind it.

You will read this, agree with all of it, and the bare approve/deny prompt will still be live in production next quarter because someone in another meeting decided number matching "adds friction." It does. That's the friction doing its job. The attackers already know your users will tap the button. The only open question is when.

*Approve / Deny. You already know which one they'll press.*