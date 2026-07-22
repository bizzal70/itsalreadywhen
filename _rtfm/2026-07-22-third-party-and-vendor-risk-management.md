---
layout: rtfm
title: "Third-Party and Vendor Risk Management"
date: 2026-07-22
summary: "Your vendors inherit your trust and export their weaknesses to you, and NIST's GV.SC exists precisely because almost nobody manages that relationship past the initial questionnaire."
framework: "NIST Cybersecurity Framework — Supply Chain Risk Management (GV.SC)"
framework_url: "https://www.nist.gov/cyberframework"
---

Every organization has a security program it built, and a security program it inherited. The one it built gets the budget, the war room, the tabletop exercises. The one it inherited arrives quietly through a procurement portal, gets a checkbox on a SOC 2 review, and then runs in production for six years while nobody looks at it again. You do not have a security posture. You have the weighted average of every vendor you decided to trust, and most of them were chosen by someone in procurement who wanted the demo to end.

## The Standard

The NIST Cybersecurity Framework 2.0 elevated supply chain risk management into its own Govern function category: **GV.SC (Cybersecurity Supply Chain Risk Management)**. This was not decoration. Putting it under Govern rather than Identify or Protect is an explicit statement that vendor risk is an organizational governance problem, not a technical control you can bolt on later.

GV.SC lays out ten outcomes, and they read like a checklist nobody finishes. **GV.SC-01** wants a supply chain risk management program that is established, agreed upon by stakeholders, and actually managed. **GV.SC-02** wants roles and responsibilities defined, internally and with your suppliers, so it is clear who owns what when something goes wrong. **GV.SC-03** wants supply chain risk integrated into your broader cybersecurity and enterprise risk management, not sitting in a spreadsheet a compliance analyst maintains alone.

The middle outcomes get concrete. **GV.SC-04** requires you to prioritize suppliers by criticality. **GV.SC-05** requires contractual requirements to address cybersecurity, meaning the security expectations are written into the agreement, not implied. **GV.SC-06** covers due diligence *before* you enter the relationship. **GV.SC-07** is the one everyone skips: understanding, recording, and monitoring supplier risk *throughout the relationship*, not just at onboarding. **GV.SC-08** pulls suppliers into your incident planning and response. **GV.SC-09** extends security practices across the technology lifecycle. **GV.SC-10** covers what happens at the end: offboarding, contract termination, data return or destruction.

In plain language: know who you depend on, rank them by how badly they can hurt you, write the rules down before you sign, keep watching after you sign, plan for them getting breached, and clean up properly when it ends. None of this is exotic. All of it is ignored.

## Where It Breaks Down

The failure is rarely ignorance of the standard. It is that the standard describes a continuous process and organizations implement a one-time event.

**The questionnaire is the program.** Most vendor risk "programs" are a 300-question spreadsheet sent once, filled out by the vendor's sales engineering team, and filed. The answers are self-attested, unverified, and stale the moment they are submitted. Nobody reconciles the vendor's claim that they enforce MFA against any evidence. A SOC 2 Type II report gets accepted at face value even though its scope carves out the exact system you integrate with, its exceptions section is never read, and its audit period ended nine months before you saw it. GV.SC-06 due diligence becomes a document collection exercise.

**Criticality is never scored, so everything is medium.** GV.SC-04 asks you to prioritize. In practice every vendor lands in the same undifferentiated pile. The payroll SaaS with direct database access to your HR records gets the same review cadence as the company that ships branded coffee mugs. Because everything is treated the same, nothing is treated seriously.

**The fourth party is invisible.** You review your CDN. You do not review the DNS provider your CDN depends on, or the object storage its logging pipeline writes to, or the observability vendor with a persistent OAuth token into your ticketing system. Concentration risk hides here: fifteen of your "independent" vendors all sit behind the same IdP, the same three cloud regions, the same handful of managed database providers. GV.SC-07 monitoring stops at the first hop.

**Integrations outlive the review.** Someone approved a marketing tool three years ago. It still holds a `client_credentials` grant with `read:all` scope. The employee who owned it left. The vendor got acquired. Nobody revoked the token because token lifecycle is not part of anyone's job, and OAuth grants do not expire on their own if the vendor set them not to. This is the GV.SC-07 and GV.SC-10 gap made real: no continuous monitoring, no offboarding.

**Contracts have security language written by people who do not do security.** GV.SC-05 asks for cybersecurity requirements in the contract. What actually ships is a boilerplate clause promising "industry-standard security" with no defined SLA for breach notification, no right to audit, no requirement to notify on subprocessor changes, and no data destruction obligation on termination. When the vendor is compromised, you find out from a press release, forty-five days late, because the contract never obligated them to tell you faster.

**Incident response stops at your perimeter.** Your runbooks assume the breach is yours. When the breached asset is a vendor holding your data or holding a credential into your environment, nobody knows who to call, what the vendor's notification obligation is, or how to force a token rotation on their side. GV.SC-08 exists precisely because vendor incidents are your incidents, and almost nobody has practiced one.

## Doing It Right

Start by mapping dependencies, not vendors. A vendor list is an accounting artifact. What you need is a dependency graph: which vendors touch which data classes, which hold what OAuth scopes and API keys, which have network paths inward, and which vendors *those* vendors depend on. Pull this from real sources, not surveys: your IdP's list of authorized OAuth applications, your cloud provider's IAM role trust policies and cross-account roles, your egress logs, your SSO application inventory. The infrastructure already knows who you trust. Ask it.

Score criticality on impact, not vendor size. A three-person startup with a write scope into your production database outranks a Fortune 100 vendor that sends you PDF invoices. Tier by data sensitivity, access level, and recoverability. Reserve deep review for the top tiers and stop pretending you can meaningfully assess all of them.

Verify instead of trusting attestation. Read the actual scope section and exceptions of the SOC 2, not the logo on the cover. For anything internet-facing, run passive external checks: certificate transparency logs, TLS configuration, exposed services, DNS hygiene. For anything holding a credential into your environment, enforce your own controls: scope OAuth grants to least privilege, set token expiry, require the connection to originate from known ranges, and put every vendor integration behind logging you own and can alert on.

Make the contract enforce the requirements. Define a breach notification window in hours, not "promptly." Require notification of subprocessor changes. Reserve a right to audit or a right to receive current attestation. Mandate data return and cryptographic destruction on termination with written confirmation. If the vendor will not agree to these, that refusal *is* your risk assessment.

Automate continuous monitoring. Quarterly re-review the OAuth grant inventory and kill orphaned tokens. Alert on new IAM trust relationships. Track vendor certificate expiry and posture drift. This is a job for TPRM tooling and CASB-style OAuth governance, not a spreadsheet.

Practice a vendor incident. Run a tabletop where the compromised asset is a vendor's token into your environment. Find out now, in the exercise, that you have no contact, no rotation procedure, and no notification clause. Then fix all three.

## The Bottom Line

You will not review every vendor. You will not read every SOC 2. Somewhere in your environment right now is a forgotten OAuth token with more access than the intern you fired for having a forgotten OAuth token. The point of GV.SC is not to achieve perfect visibility, because you will not. The point is to know which of your dependencies can end you, to write the rules down before you need them, and to keep watching the ones that matter. Everything you trust is an attack surface you did not build and cannot fully see. Trust accordingly, which is to say, less.

*You are only as secure as the vendor whose name you can no longer remember.*

## Related

- [Field Note — July 21, 2026](/itsalreadywhen/field-notes/2026/07/21/field-note/)
- [Field Note — July 20, 2026](/itsalreadywhen/field-notes/2026/07/20/field-note/)
- [The 11-byte packet that freezes an OpenSSL server for good](/itsalreadywhen/2026/07/19/issue-005/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)
