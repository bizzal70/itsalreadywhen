---
layout: rtfm
title: "The Human Factor: Security Awareness That Isn't Theater"
date: 2026-08-26
summary: "Annual phishing-quiz compliance training teaches people to pass quizzes, not to resist attacks, and CIS Control 14 asks for something far harder: role-specific skills that hold up under pressure."
framework: "CIS Critical Security Control 14 — Security Awareness and Skills Training"
framework_url: "https://www.cisecurity.org/controls/cis-controls-list"
---

Every organization runs security awareness training, and almost none of them do security awareness. What they do is compliance theater: a fifteen-minute e-learning module with a cartoon fish, a quiz you can pass by clicking the obviously wrong answers in reverse, and a completion certificate that exists solely so someone in GRC can point to a green checkbox during an audit. The dirty secret is that everyone involved knows it does nothing, and the ritual continues anyway because measuring completion is easy and measuring behavior is hard. We have built an entire industry around the metric that matters least.

## The Standard

CIS Critical Security Control 14, "Security Awareness and Skills Training," is more demanding than most people who cite it have actually read. It has nine safeguards, and only one of them (14.1) is about establishing a program at all. The rest are specific. Control 14.2 wants training on recognizing social engineering, including phishing, pretexting, and tailgating. Control 14.3 addresses authentication best practices, meaning MFA, password composition, and credential management. Control 14.4 covers data handling: how to identify, store, transfer, and dispose of sensitive data. Controls 14.5 and 14.6 deal with the causes of unintentional data exposure and recognizing and reporting security incidents. Control 14.7 is about keeping software and hardware updated. Control 14.8 covers the dangers of connecting to and transmitting data over insecure networks. Control 14.9 asks for role-specific security awareness and skills training.

Read that list again and notice what is not there. Nowhere does Control 14 say "run an annual module and record completion." It describes a set of competencies the workforce is supposed to actually possess, calibrated to the roles people hold. A developer, a finance clerk, a helpdesk technician, and a domain administrator face different threats and need different skills. The control is a specification for behavior under real conditions, not a specification for attendance. The framework understood the assignment. Most implementations did not.

## Where It Breaks Down

The first failure is treating awareness as a knowledge problem when it is a behavior problem. People know they should not click links from strangers. They click anyway, because the email arrives at 4:55 PM on a Friday, appears to come from their manager, references a real project, and asks for something plausible. Cognitive load, time pressure, and authority cues override the tidy multiple-choice knowledge captured by the quiz. Testing recall in a calm environment tells you nothing about performance in an adversarial one.

The second failure is the phishing simulation program run as a gotcha. Organizations buy a simulated-phishing platform, blast identical lures to the entire company, and then punish the people who click. This produces three predictable outcomes: employees warn each other over Slack the moment the campaign lands (destroying your measurement), the security team gets treated as an internal adversary (destroying your reporting culture), and the click-rate metric gets gamed downward without any change in actual resilience. Worse, poorly run simulations train people to be suspicious of exactly the wrong things. If your lures always have spelling errors and urgent tones, you are teaching staff that real threats look sloppy, when modern pretexting is clean, contextual, and often uses a legitimate compromised internal account.

The third failure is ignoring the reporting pipeline entirely. The single most valuable behavior you can cultivate is fast reporting: a user who forwards a suspicious message to the SOC within two minutes gives you a chance to pull the same lure from every other inbox before it detonates. But if reporting means composing an email to a shared mailbox nobody monitors, or if reports vanish into a ticketing void with no acknowledgment, you have engineered the behavior out of existence. Most "awareness" programs measure who clicked. Almost none measure who reported, how fast, and what happened next.

The fourth failure is the total absence of role-specific content that Safeguard 14.9 explicitly requires. The developer who commits an AWS key to a public repository, the sysadmin who reuses a domain admin password across tiers, the finance approver who wires funds on a spoofed executive request: none of these are addressed by the generic module. Privileged users are the highest-value targets and receive the least tailored training. A single generic annual course cannot cover secure coding, credential tiering, and business-email-compromise verification workflows, and pretending it does is how these gaps persist.

The fifth failure is cadence. Annual training assumes attention is durable for twelve months. It is not. Awareness decays within weeks. A once-a-year event is optimized for the audit calendar, not for human memory.

## Doing It Right

Start by inverting your primary metric. Stop optimizing click rate and start optimizing report rate and, more importantly, time-to-report. Deploy a one-click report button in your mail client (the native "Report Phishing" add-in for your mail platform, or an equivalent that pipes directly into your SOAR or ticketing system). Instrument it. A healthy program sees report rates climb well above click rates, and sees median time-to-report drop into single-digit minutes. That is a behavior that measurably shortens attacker dwell time, which is the entire point.

Run phishing simulations, but run them as training instruments, not traps. Vary the difficulty. Segment your campaigns so that different departments receive lures relevant to their actual threat model: invoice fraud for accounts payable, fake code-review requests for engineering, credential-harvest pages mimicking your real SSO portal for everyone. When someone clicks, the response should be an immediate, non-punitive, context-specific micro-lesson delivered in the moment, not a disciplinary note. The teachable moment is the click itself, and it lasts about thirty seconds before defensiveness sets in.

Make the training technical and specific to the control's safeguards. For authentication (14.3), do not lecture about password length; roll out phishing-resistant MFA (FIDO2/WebAuthn hardware keys or passkeys) and teach people why push-notification fatigue attacks work, so they recognize an unrequested prompt as an incident rather than an annoyance to dismiss. For data handling (14.4), tie training to your actual DLP tooling and classification labels so people understand the system they live inside. For insecure networks (14.8), stop saying "avoid public WiFi" and instead ensure your always-on VPN or ZTNA client makes the safe path the default, then explain what it does.

Build the process for business-email-compromise verification into workflow, not memory. A hard rule that any change to payment details or any wire above a threshold requires out-of-band verification (a callback to a known number, not the number in the email) removes the human judgment call under pressure. The best awareness control is often a procedure that makes the wrong action structurally harder.

Address privileged users separately and seriously. Give administrators and developers dedicated, hands-on training tied to their tooling: secrets management, credential tiering, the difference between their daily-driver account and their privileged one, and how attackers pivot. This is Safeguard 14.9, and it is where your real risk concentrates.

Finally, change the cadence. Short, frequent, varied touches beat the annual marathon. Continuous simulation, quarterly micro-modules, and just-in-time nudges keep the signal above the decay curve.

## The Bottom Line

None of this is secret. CIS Control 14 has said it plainly for years, and the practitioners who care already know their annual module is a placebo. The reason it persists is that theater is auditable and behavior is not, and organizations reliably choose the thing that is easy to document over the thing that actually works. So the fish will keep swimming across the screen, the certificates will keep printing, and somewhere a user under deadline pressure will do exactly what you spent your budget failing to prevent. You cannot patch people. But you can stop pretending a quiz did.

*Train for the 4:55 PM Friday, because that's when it happens.*

## Related

- [Default Credentials and Configuration Drift](/itsalreadywhen/rtfm/2026/08/19/default-credentials-and-configuration-drift/)
- [Least Privilege, Actually Enforced](/itsalreadywhen/rtfm/2026/07/01/least-privilege-actually-enforced/)
- [Third-Party and Vendor Risk Management](/itsalreadywhen/rtfm/2026/07/22/third-party-and-vendor-risk-management/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)
