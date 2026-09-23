---
layout: rtfm
title: "Identity Is the New Perimeter"
date: 2026-09-23
summary: "Firewalls were built to protect a network topology that no longer exists, and until you treat identity as the actual perimeter (the way NIST SP 800-207 tells you to), you are just guarding an empty building."
framework: "NIST SP 800-207 — Zero Trust Architecture"
framework_url: "https://csrc.nist.gov/pubs/sp/800/207/final"
---

There is a firewall somewhere in your environment right now, dutifully inspecting traffic between two subnets that no longer contain anything worth defending. Everyone nods along when you say "identity is the new perimeter," puts it on a slide, and then goes back to writing allow rules based on source IP addresses like it's still 2004. The uncomfortable truth is that the network you spent a decade hardening dissolved the moment your users started authenticating to SaaS apps from coffee shops and your workloads started spawning in someone else's data center. The castle-and-moat model didn't fail because the moat was too shallow. It failed because everyone valuable left the castle.

## The Standard

NIST SP 800-207 is refreshingly blunt about this. Zero Trust is not a product, and the document says so explicitly. It is a set of principles for designing systems where trust is never granted implicitly based on network location. The core assertion is that being on the "internal" network confers no privilege whatsoever. Packets originating from 10.0.0.0/8 get exactly the same suspicion as packets from the public internet.

The document is built around a few load-bearing concepts. Every access request is evaluated by a **Policy Decision Point (PDP)**, which decides whether to grant access, and enforced by a **Policy Enforcement Point (PEP)**, which sits inline and actually blocks or permits the connection. Access is granted per-session, per-resource, and is dynamic: the decision incorporates identity, device posture, and other observable signals, and it can be revoked. SP 800-207 calls out seven tenets, but the ones people ignore hardest are these: all resource authentication and authorization are dynamic and strictly enforced before access is allowed, and the enterprise collects data about the current state of assets and network infrastructure to continuously improve its security posture.

Read that carefully. "Before access is allowed" and "continuously." Not "at the VPN handshake and then never again for eight hours." The standard describes a control plane and a data plane that are logically separate, where policy is evaluated continuously against the resource being requested, not against the network segment the user happens to be sitting in. Identity, in this model, is not a login event. It is the perimeter itself, and it has to be enforced at every resource boundary.

## Where It Breaks Down

The most common failure is the **VPN that pretends to be Zero Trust**. Organizations buy a "ZTNA" product, deploy it as a replacement for their legacy VPN concentrator, and then configure it to dump authenticated users onto a flat internal network. Congratulations: you have moved the implicit-trust boundary from the firewall to the VPN gateway and changed nothing else. Once the tunnel is up, that user can reach the domain controller, the jump box, and the finance file share, because your PEP only enforces at the door and never again inside the house. That is a moat with extra latency.

The second failure is **authentication without authorization context**. Plenty of shops have rolled out SSO and even MFA, and they feel finished. But the identity provider is issuing a bearer token or a SAML assertion that says "this is a valid human" and nothing about whether this human should touch this resource from this device right now. The relying application does no re-evaluation. There is no per-session, per-resource decision, which is precisely what the standard requires. A stolen session cookie or a phished OAuth refresh token walks straight through, because the only checkpoint was the initial handshake.

Third: **service accounts and machine identities are a governance wasteland**. Human identity gets the MFA, the conditional access policies, the quarterly access reviews. Meanwhile the actual traffic in your environment is mostly non-human: CI/CD pipelines, service principals, Kubernetes service accounts, API keys hardcoded in a Lambda. These identities frequently hold standing, over-broad permissions, authenticate with long-lived secrets that never rotate, and are exempt from every conditional-access control you built. An attacker who lands anywhere in the environment goes hunting for these first, because they are the identities nobody is watching.

Fourth: **device posture is decorative or absent**. SP 800-207 explicitly names asset state as an input to the access decision. In practice, the PDP has no idea whether the endpoint is a managed, patched, EDR-enrolled laptop or a personal machine with a keylogger on it. Bring in the token, get the access. The "posture check" is often a one-time enrollment that a device passes once and is trusted forever afterward.

Fifth: **east-west traffic is unauthenticated by design**. Even in cloud-native shops, workloads within a VPC or a Kubernetes cluster talk to each other over plaintext or with mutual TLS that validates nothing meaningful. There is no PEP between microservices. Lateral movement, the entire reason implicit network trust is dangerous, remains trivial because you rebuilt the flat internal network inside your cloud tenant.

## Doing It Right

Start by making identity the enforcement point, not the network. Every resource, human-facing or machine-facing, needs an authorization decision at request time, evaluated against the specific resource. In OIDC/OAuth terms, that means short-lived access tokens (minutes, not hours), enforced token audience and scope restrictions, and validation of those claims at the resource server, not just at the gateway. Use **sender-constrained tokens** (DPoP or mTLS-bound tokens) so a stolen bearer token is useless without the corresponding key. Kill implicit refresh where you can.

Feed real signal into the PDP. A modern conditional-access engine should be consuming device posture from your MDM or EDR (is it managed, is disk encryption on, is the agent healthy), identity risk signals (impossible travel, anomalous token use), and network context, then making a **continuous** decision. Tools in the CAEP (Continuous Access Evaluation Protocol) space exist specifically so an IdP can push a revocation event and have relying parties tear down sessions in near real time instead of waiting for token expiry. Implement session revocation that actually propagates.

For machine identity, eliminate long-lived secrets. Move to workload identity federation so your pipelines and cloud workloads mint short-lived credentials from a trusted issuer instead of carrying a static key. In service mesh environments, use SPIFFE/SPIRE to give every workload a cryptographic identity (an SVID) and enforce mutual TLS with actual identity-based authorization policy between services. That is your east-west PEP. Now lateral movement requires forging a workload identity instead of just reaching an IP.

Segment on identity, not subnets. Microsegmentation done right means the policy is "this service identity may call that service identity on this port," expressed and enforced independent of where either one runs. Whether you do that with a mesh, an identity-aware proxy, or cloud-native policy, the decision has to be per-resource and default-deny.

And instrument the PDP itself. SP 800-207's continuous-improvement tenet is not aspirational fluff. Log every access decision, feed denials and anomalies into your detection pipeline, and treat a spike in authorization failures as the reconnaissance signal it usually is. The point of a Zero Trust architecture is not just to block; it is to generate a high-fidelity record of who asked for what, when, from where, and on what device.

## The Bottom Line

None of this is secret. The standard has been sitting there for years, and every practitioner reading this already knows the VPN they inherited is a liability wearing a badge. The reason it doesn't get fixed is that ripping out implicit trust means touching every application, every service account, and every integration your predecessors duct-taped together, and nobody gets promoted for finishing that project. So the firewall keeps inspecting traffic between empty subnets, the service accounts keep their standing keys, and the perimeter you claim to defend evaporated a long time ago. You are not going to get a warning before someone notices. You already know what "It's Already When" means.

*Rotate your secrets. Or don't, and find out.*

## Related

- [Segmentation as an Assumption, Not a Diagram](/itsalreadywhen/rtfm/2026/07/29/segmentation-as-an-assumption-not-a-diagram/)
- [Least Privilege, Actually Enforced](/itsalreadywhen/rtfm/2026/07/01/least-privilege-actually-enforced/)
- [Asset Inventory: You Can't Protect What You Don't Know You Have](/itsalreadywhen/rtfm/2026/09/02/asset-inventory-you-can-t-protect-what-you-don-t-know-you-have/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)
