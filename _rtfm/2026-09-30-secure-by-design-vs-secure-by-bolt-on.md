---
layout: rtfm
title: "Secure by Design vs. Secure by Bolt-On"
date: 2026-09-30
summary: "Retrofitted security controls cost more and catch less than designed-in ones, and CISA's Secure by Design framework explains why the bolt-on habit persists despite everyone knowing better."
framework: "CISA Secure by Design"
framework_url: "https://www.cisa.gov/securebydesign"
---

Everybody agrees, in the abstract, that security should be built in rather than bolted on. It is the kind of thing people nod along to in architecture reviews right before they approve a design with authentication deferred to "phase two." The gap between believing in secure-by-design and actually practicing it is not a knowledge gap. It is an incentive gap, a scheduling gap, and a willful refusal to treat security as a property of the system rather than a product you can purchase and deploy in front of it.

## The Standard

CISA's Secure by Design initiative is less a control framework than a statement of philosophy with teeth. Its core claim is that the burden of security should sit with the software manufacturer, not the customer, and that this burden must be discharged during design and development rather than pushed downstream into deployment and operations. The document articulates three principles: take ownership of customer security outcomes, embrace radical transparency and accountability, and build organizational structure and leadership that make secure design a business priority rather than a compliance afterthought.

In practice the guidance points at concrete engineering behaviors. Memory-safe languages where feasible. Secure defaults that ship in the hardened configuration rather than the convenient one. Elimination of entire vulnerability classes through design choices, such as parameterized queries to kill SQL injection categorically, rather than input sanitization applied case by case. Multi-factor authentication as a default rather than an opt-in feature buried three menus deep. The recurring theme is that a control designed into the system's structure removes a class of problem, while a control applied afterward can only detect or mitigate instances of it.

That distinction is the entire argument. Secure by design is preventive at the architectural level. Bolt-on security is compensating at the perimeter. One changes the shape of the attack surface. The other watches it.

## Where It Breaks Down

The failure modes are depressingly consistent across organizations, and they are almost never a failure to buy tools.

The first is authentication and authorization retrofitted onto systems that assumed trust. A service written to talk to another service over an internal network, with no mutual authentication, no token validation, no notion of caller identity, does not become zero-trust because you put a service mesh in front of it. The mesh gives you mTLS between sidecars, which is real and useful, but the application behind the sidecar still trusts anything that reaches it. You have encrypted the transport and authenticated the proxy while leaving the actual authorization decision unmade. The design assumed a trust boundary that no longer exists, and no amount of infrastructure tooling relocates that assumption out of the code.

The second is the WAF-as-remediation pattern. An application is vulnerable to injection or deserialization attacks, and rather than fix the parsing and query construction, someone writes signature rules on a web application firewall. This is bolt-on security in its purest form. The vulnerability still exists. The WAF is now a pattern-matcher racing against every encoding trick, every parser differential, every case the rule author did not anticipate. It catches the payloads that look like the payloads it was told about and misses the ones that do not. Meanwhile the rules accumulate, false positives generate tickets, and eventually someone loosens a rule to unblock a legitimate request and quietly reopens the hole.

The third is logging and monitoring bolted onto systems that emit nothing useful. Detection engineering can only work with the telemetry the system produces. When authentication, authorization, and state-changing operations were never instrumented, because the design never treated them as security-relevant events, the SIEM ingests noise. You get web server access logs and no application-level audit trail, so you can see that a request arrived but not what identity made it or what it changed. Teams then spend enormous effort in the log pipeline trying to reconstruct intent from artifacts, which is archaeology, not detection.

The fourth is secrets and identity management grafted onto applications that were written with credentials in config files. Introducing a secrets manager does not help if the application reads a static credential at startup and holds it in memory for its entire lifetime with no rotation, no short-lived tokens, and no scoping. You have moved the secret into a nicer box and changed nothing about the blast radius when it leaks.

The fifth, and the most expensive, is the insecure default that ships and then must be undone by every customer forever. A product that defaults to an open listener, a permissive CORS policy, a database with no authentication, or an admin account with a known password creates a security cost that is paid thousands of times over across the install base. Every hardening guide, every CIS benchmark, every "please remember to disable this" note in the docs is evidence of a default that was chosen wrong at design time and is now a permanent tax on operations.

The common thread is that in each case the fix at design time was cheaper and more complete than the compensating control, and the organization chose the compensating control because it was faster to ship and did not require touching code that already "worked."

## Doing It Right

Start by making security requirements first-class in the design phase, which means they exist before the first line of code and they block the design review the same way a missing scalability requirement would. Threat model the system while it is still a diagram. STRIDE against a data flow diagram costs an afternoon and surfaces the trust boundaries you are about to get wrong. This is where you decide that services authenticate each other, that authorization is enforced at the resource, and that every state change is an auditable event, rather than discovering those needs after deployment.

Eliminate vulnerability classes structurally rather than defending against instances. Use parameterized queries and ORMs that do not permit raw string concatenation, so injection is not a bug you can introduce. Use memory-safe languages for new development where performance permits, because that removes an entire category of exploitation rather than mitigating it with stack canaries and ASLR after the fact. Adopt output encoding libraries that are contextual by default so cross-site scripting is a framework guarantee, not a code review hope.

Ship secure defaults and make the insecure configuration the one that requires deliberate effort. Bind to localhost unless told otherwise. Require authentication with no bypass. Enforce TLS with modern cipher suites and no downgrade path. Make MFA the default enrollment. The correct posture should be the path of least resistance.

Instrument for detection at the source. Emit structured, security-relevant events (authentication outcomes, authorization denials, privilege changes, and state mutations) with the identity and context attached, in a format your detection pipeline can consume without reconstruction. Design identity as short-lived and scoped from the start using workload identity federation and automatically rotated credentials rather than static secrets, so that a compromised token is a small, brief problem instead of a standing liability.

Finally, treat the software bill of materials and dependency provenance as design inputs, not audit outputs. Know what you ship, sign what you build, and verify what you consume.

## The Bottom Line

None of this is secret. The economics have been understood for decades, the framework spells it out in plain language, and every practitioner reading this could recite the argument in their sleep. It gets ignored anyway, because designing security in delays a release and bolting it on delays a breach, and only one of those shows up on this quarter's roadmap. So the compensating controls pile up, the WAF rules metastasize, the SIEM chews through noise, and everyone agrees at the postmortem that they should have built it in from the start. They will say the same thing at the next one.

*Build it in now, or explain later why you didn't.*

## Related

- [Identity Is the New Perimeter](/itsalreadywhen/rtfm/2026/09/23/identity-is-the-new-perimeter/)
- [Default Credentials and Configuration Drift](/itsalreadywhen/rtfm/2026/08/19/default-credentials-and-configuration-drift/)
- [Application Security Basics: Input Validation Still Matters](/itsalreadywhen/rtfm/2026/09/09/application-security-basics-input-validation-still-matters/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)
