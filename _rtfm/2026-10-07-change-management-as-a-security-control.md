---
layout: rtfm
title: "Change Management as a Security Control"
date: 2026-10-07
summary: "Nearly every outage and most breaches trace back to a change nobody reviewed, yet change management remains the control everyone claims to have and almost nobody actually runs."
framework: "NIST SP 800-53 Rev. 5 — CM Family (Configuration Management)"
framework_url: "https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final"
---

Ask any engineer to name the last time they caused an outage, and the honest ones will tell you the same story: a change. Not an attacker, not a zero-day, not some cinematic nation-state operation. A firewall rule. A DNS record. A "quick" config push on a Friday. Change management is the most boring control in the catalog and the one that would have prevented more incidents than every EDR license your organization has ever bought. It is ignored precisely because it is boring, and because it feels like process for the sake of process, right up until the moment production is on fire and nobody can say what changed.

## The Standard

NIST SP 800-53 Rev. 5 does not treat configuration management as hygiene. It treats it as a security control family, CM, with seventeen base controls and a pile of enhancements. The thesis is simple: if you cannot describe the state your systems are supposed to be in, you cannot defend them, and you cannot detect when they drift away from it.

The load-bearing controls are worth knowing by their numbers because practitioners quote them to auditors and then quietly fail to implement them.

**CM-2 (Baseline Configuration)** requires a documented, current baseline of your systems: the approved software, versions, network topology, and configuration settings. This is the "known good" that everything else references.

**CM-3 (Configuration Change Control)** is the actual control under discussion. It requires that you define the types of changes that are configuration-controlled, review proposed changes, explicitly approve or deny them with consideration of security and privacy impact, document decisions, and retain records. The enhancement CM-3(2) wants you to test and validate changes before implementation. CM-3(4) wants a Configuration Control Board, a named group of humans accountable for the decision.

**CM-4 (Impact Analysis)** requires analyzing the security and privacy impact of a change *before* it ships. Not after the postmortem.

**CM-5 (Access Restrictions for Change)** requires that you limit who can make changes, and that you log and audit them. **CM-6 (Configuration Settings)** wants mandatory, documented settings using established benchmarks. **CM-7 (Least Functionality)** says turn off what you do not use. **CM-8 (System Component Inventory)** says you have to know what you own.

Read as a system, the CM family says one thing: changes to production are deliberate, reviewed, tested, authorized, and recorded, performed by a constrained set of people against a known baseline. That is the whole game.

## Where It Breaks Down

The failure is almost never the absence of a change process. Nearly every organization has a Jira project called "Change Management" and a wiki page describing an approval workflow. The failure is the gap between the documented process and what actually happens at the keyboard.

**Emergency change as a permanent loophole.** CM-3 reasonably allows for emergency changes. In practice the emergency path becomes the default path. Someone discovers that selecting "Emergency" skips the review queue, and within a quarter sixty percent of changes are flagged emergency. The control is still "in place." It is simply routed around by everyone who touches production.

**The infrastructure that is not covered.** The change process governs application deployments and nothing else. Meanwhile the real blast radius lives in the layers nobody put under control: BGP route advertisements, DNS zone edits, TLS certificate rotation, IAM policy changes in your cloud account, security group and NACL modifications, Terraform state manipulated by hand, Kubernetes RBAC bindings, and the CI/CD pipeline configuration itself. A single overly permissive S3 bucket policy or an IAM role with a wildcard `Action` is a change. It is rarely treated as one.

**Click-ops drift.** CM-2 presumes a baseline exists and is current. In reality the baseline was documented at go-live and has been fiction ever since. Someone made a change in the AWS console at 2 a.m. to resolve an incident and never codified it. Now the Terraform says one thing and the account says another, and the next `terraform apply` either reverts a critical fix or errors out. Nobody runs `terraform plan` in a scheduled drift-detection job, so nobody knows. The "infrastructure as code" is aspirational.

**Reviews that review nothing.** CM-3 requires review by someone who can assess impact. What you get instead is a pull request approved in nine seconds by a teammate who did not read it, or a CAB meeting where forty changes are rubber-stamped in thirty minutes because saying "no" slows people down and nobody wants to be that person. A review that cannot result in a rejection is not a review. It is theater with a ticket number.

**No link between change and detection.** CM-5 wants change logging. Organizations collect the logs and never correlate them. When a config suddenly shifts (a security group opening `0.0.0.0/0` on port 22, a new IAM user with console access, a GPO modified) there is no alert tying that observed change back to an approved change record. So the malicious change and the authorized change look identical in the audit trail, which means the audit trail tells you nothing.

**Least functionality as a fiction.** CM-7 is almost universally ignored. Default installs ship with services, ports, agents, and sample applications nobody uses. Every one is attack surface that was never a deliberate decision, because turning things off requires knowing what is on, and CM-8 inventory is a spreadsheet last updated two reorgs ago.

## Doing It Right

You do not fix this with a bigger CAB meeting. You fix it by making the correct path the easy path and the wrong path impossible.

**Put everything under version control, then enforce it.** All infrastructure (network, DNS, IAM, firewall, Kubernetes manifests) lives in a repository. The change *is* the pull request. This gives you CM-3 review, CM-4 impact analysis, and CM-5 access restriction in one artifact, with a built-in record. Require branch protection, mandatory reviews from a `CODEOWNERS` file that routes security-relevant paths (IAM, networking, secrets config) to people qualified to assess them, and signed commits so the author is not forgeable.

**Make click-ops structurally impossible, or detect it instantly.** Remove standing write access to production consoles. Humans get read-only; changes flow through the pipeline using a deployment identity. Where you cannot remove console access entirely, run scheduled drift detection: `terraform plan` on a cron, AWS Config rules, or a policy engine comparing live state to declared state, and alert on any delta. A change that appears in production but not in the repo is either an incident or an unapproved change. Both deserve a page.

**Automate impact analysis in the pipeline.** CM-4 does not have to be a human reading a diff. Policy-as-code tools (OPA/Rego, Sentinel, cloud-native policy frameworks) can block a merge that opens SSH to the world, grants a wildcard IAM action, disables logging, or deploys an unapproved image. Static analysis of IaC catches the class of mistake that causes most cloud exposure before it ever reaches an account.

**Wire change records to detection.** Feed your approved-change log and your observed-change telemetry (CloudTrail, config history, GPO audit logs, netflow for new flows) into the same place. Build the correlation: observed change with no matching approval equals alert. This is the single highest-value thing most teams skip, and it converts your change process from paperwork into a tripwire.

**Define emergency changes narrowly and review them after.** Emergency means production is down, not "I am in a hurry." Every emergency change gets a mandatory retroactive review within a fixed window. Track the ratio of emergency to standard changes as a metric and treat a rising ratio as a process failure, because that is exactly what it is.

**Baseline with benchmarks, enforce least functionality.** CM-6 and CM-7 become tractable when the baseline is a hardened image (CIS Benchmarks, STIGs) built in the pipeline and deployed immutably. You do not patch the running host; you rebuild and replace it. Drift is deleted by definition, not remediated by hand.

## The Bottom Line

The uncomfortable truth is that you do not need an adversary to suffer a security incident. You will provision one yourself, on a Tuesday, with full authorization and the best intentions. The CM family is NIST quietly pointing out that the call is coming from inside the house, and that the fix is not clever, it is disciplined. Nobody gets promoted for the outage that did not happen, which is why the review that would have caught it keeps getting skipped. Do it anyway. The change you do not review is the one you will be explaining in the postmortem.

*It was never a question of if something would change. It was only ever a question of whether you were watching when it did.*

## Related

- [Least Privilege, Actually Enforced](/itsalreadywhen/rtfm/2026/07/01/least-privilege-actually-enforced/)
- [Asset Inventory: You Can't Protect What You Don't Know You Have](/itsalreadywhen/rtfm/2026/09/02/asset-inventory-you-can-t-protect-what-you-don-t-know-you-have/)
- [Default Credentials and Configuration Drift](/itsalreadywhen/rtfm/2026/08/19/default-credentials-and-configuration-drift/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)
