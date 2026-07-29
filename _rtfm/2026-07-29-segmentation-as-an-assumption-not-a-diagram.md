---
layout: rtfm
title: "Segmentation as an Assumption, Not a Diagram"
date: 2026-07-29
summary: "Segmentation isn't a diagram you draw once and file away, it's an assumption you have to prove every time it matters, and flat networks that pass audits still collapse the moment an attacker gets a foothold."
framework: "NIST SP 800-207 — Zero Trust Architecture"
framework_url: "https://csrc.nist.gov/pubs/sp/800/207/final"
---

Everyone has a network diagram with tidy colored boxes and confident arrows, and almost none of those diagrams describe how packets actually move. Segmentation gets treated as an architectural decision made once, drawn in Visio, and forgotten, when it is really a claim you are making about attacker movement that has to hold up under adversarial pressure. The diagram survives the audit. The assumption dies the first time someone phishes a helpdesk account. If your segmentation only exists as documentation, you do not have segmentation, you have a story you tell auditors.

## The Standard

NIST SP 800-207 (Zero Trust Architecture) is often reduced to a marketing slogan, but the document itself is disciplined and worth reading on its own terms. Its central premise is that you should stop treating network location as a proxy for trust. The old model granted implicit trust to anything inside the perimeter: get past the firewall, and you were effectively an insider. 800-207 rejects that outright. Its tenets state that all resources are authenticated and authorized on a per-session basis, that access is granted per-request, and that trust is never conferred simply because a device sits on a particular subnet.

Read carefully, this is a direct assault on the flat network. The standard describes a Policy Decision Point and Policy Enforcement Point (the PDP/PEP model) that sit in the path of every access request and evaluate it dynamically against identity, device posture, and other signals. The key phrase, repeated in various forms, is that the enterprise should "assume breach." You are meant to design as though the attacker is already inside, because eventually they will be.

Segmentation is how you operationalize "assume breach" at the network layer. It is not the whole of zero trust, but it is the part that decides whether a single compromised host is an incident or a catastrophe. 800-207 does not tell you to buy a product. It tells you to make trust explicit, per-session, and enforced at as fine a granularity as you can sustain. Everything else is implementation detail.

## Where It Breaks Down

The failures are boringly consistent across organizations, and they are almost never about the perimeter firewall, which usually works fine. They are about what happens after.

**VLANs mistaken for segmentation.** A VLAN is a broadcast domain, not a security boundary. Plenty of shops carve the network into a dozen VLANs, feel accomplished, and then route freely between all of them at a single core switch or firewall with an `any/any` allow rule buried in the config. Layer 2 separation with unrestricted Layer 3 routing is not segmentation. It is the same flat network with extra steps and a false sense of security.

**East-west traffic nobody inspects.** Most enforcement lives north-south, between the inside and the internet. Traffic between two internal hosts, the workstation and the file server, the app tier and the domain controller, traverses the switching fabric untouched. An attacker who lands on one endpoint can enumerate SMB shares, hit LDAP, spray credentials over Kerberos, and pivot via RDP or WinRM without ever crossing a device that logs, let alone blocks, the attempt.

**The management plane as a flat superhighway.** Even organizations with decent workload segmentation leave their out-of-band and management interfaces wide open. IPMI, iDRAC, iLO, vCenter, the hypervisor management network, switch SSH, and the backup infrastructure frequently share reachability with general-purpose subnets. Compromise one jump box and the entire estate is addressable. Backup networks are especially damning: unsegmented backup access is how a single foothold becomes an unrecoverable event.

**Identity systems reachable from everywhere.** Active Directory is the crown jewel, and yet Tier 0 assets (domain controllers, ADFS, PKI, the accounts that manage them) routinely accept authentication and management traffic from any workstation in the building. Without a tiered administration model enforced at the network as well as in AD itself, credential theft on a laptop leads straight to Domain Admin. The diagram shows DCs in a special zone. The routing table disagrees.

**Segmentation that exists but is never validated.** Someone configured ACLs and security groups two years ago. Since then, a hundred change requests have punched holes for "temporary" troubleshooting, application migrations, and vendor access that never got cleaned up. Nobody re-tests the boundary, so the segmentation slowly rots into permissiveness. The policy is real. The enforcement it was supposed to provide is gone.

**Cloud security groups treated as the whole answer.** In cloud environments, teams lean on security groups and NACLs but leave them broad (0.0.0.0/0 on internal ports, or security groups that reference each other so loosely that the entire VPC is effectively one trust zone). East-west lateral movement inside a VPC or across peered VPCs is just as viable as it is on-premises when the rules are written for convenience.

## Doing It Right

Start by abandoning the diagram as your source of truth and treat segmentation as a hypothesis you have to test. The controlling question is not "how is the network drawn" but "from this compromised host, what can I reach, and who would know."

**Map real reachability, not intended reachability.** Use flow data. NetFlow, IPFIX, VPC flow logs, or a microsegmentation platform's discovery mode will show you the actual east-west conversations happening in your environment. You will find traffic you did not know existed. Build policy from observed flows, then progressively deny what should not be there.

**Enforce at the workload, not just the network.** Host-based firewalls (Windows Filtering Platform via GPO, nftables/iptables on Linux) and identity-aware microsegmentation agents let you write allow-lists per workload that survive the host moving between subnets. This is the practical expression of 800-207's per-session model: the app server accepts 1433 from exactly two application hosts and nothing else, regardless of what the VLAN would otherwise permit.

**Build a tiered administration model and enforce it in the network.** Domain controllers and other Tier 0 systems should accept management only from dedicated Privileged Access Workstations on a segment that ordinary endpoints cannot route to. Combine network ACLs with authentication policy silos and the Protected Users group in AD so that a stolen workstation credential is useless against the identity plane.

**Isolate the management and backup planes hard.** Out-of-band interfaces (IPMI, iLO, iDRAC, hypervisor management, switch and firewall management) belong on a physically or logically separate network reachable only through an audited jump host with MFA. Backup infrastructure should be reachable only from the systems it backs up, on the ports it needs, ideally with immutable or offline copies that no compromised production credential can touch.

**Default deny east-west, then allow deliberately.** The goal state is that lateral movement requires crossing a Policy Enforcement Point that authenticates the request. SMB, RDP, WinRM, LDAP, and Kerberos between arbitrary endpoints should be blocked by default. Workstation-to-workstation SMB has almost no legitimate business use and is a primary lateral-movement vector.

**Test the boundary continuously.** Segmentation that is not validated is decaying. Run periodic reachability tests, purple-team exercises, and automated checks that assert "host A must not reach host B on port C." Alert on violations of your own model. If you cannot detect a segmentation policy that quietly broke, you do not really have a policy.

## The Bottom Line

Segmentation is not a thing you have. It is a thing you keep proving, over and over, against people who are actively trying to disprove it. The flat network passes the audit because the audit reads the diagram, and the diagram is a work of optimistic fiction. The incident does not read the diagram. It reads the routing table, the firewall state, and every `any/any` rule someone added at 2 a.m. and forgot. You will not know which story your network is telling until the day it matters, and by then the answer is already written. Assume breach was never a slogan. It was a warning about the version of you that will be reading the logs afterward.

*Draw all the boxes you like. The packets will go where the config lets them.*

## Related

- [Least Privilege, Actually Enforced](/itsalreadywhen/rtfm/2026/07/01/least-privilege-actually-enforced/)
- [Logging Without Anyone Reading the Logs](/itsalreadywhen/rtfm/2026/07/15/logging-without-anyone-reading-the-logs/)
- [Third-Party and Vendor Risk Management](/itsalreadywhen/rtfm/2026/07/22/third-party-and-vendor-risk-management/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)
