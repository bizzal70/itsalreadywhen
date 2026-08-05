---
layout: rtfm
title: "Incident Response Plans Nobody Has Run"
date: 2026-08-05
summary: "A ready incident response plan that has never been exercised isn't a capability at all, just a document waiting to fail you in the worst possible way."
framework: "NIST SP 800-61 — Computer Security Incident Handling Guide"
framework_url: "https://csrc.nist.gov/pubs/sp/800/61/r2/final"
---

Every organization has an incident response plan. Almost none of them have run it. The plan lives in a wiki, or a PDF on a shared drive, or a binder that someone printed for an audit three years ago, and it will remain there, pristine and unread, until the day it is needed, at which point everyone will discover simultaneously that it does not survive contact with reality. This is not a failure of documentation. It is a failure to understand that a plan you have never executed is a hypothesis, not a procedure.

## The Standard

NIST SP 800-61, the *Computer Security Incident Handling Guide*, is refreshingly blunt about this. It defines the incident response life cycle in four phases: Preparation; Detection and Analysis; Containment, Eradication, and Recovery; and Post-Incident Activity. The interesting part, the part everyone skips, is that Preparation is not a one-time event that ends when you finish writing the plan. It is a continuous phase, and 800-61 explicitly calls out exercises as part of it.

The guide recommends that organizations conduct exercises to test and improve their incident handling capability. It talks about tabletop exercises and functional drills. It emphasizes that the incident response team needs the right skills, the right tools, and, critically, the muscle memory that only comes from practice. Section 2.4 discusses team models and staffing precisely because the standard understands that IR is a human activity performed under stress, not a checklist executed by a machine.

The document is equally clear that a plan is a living artifact. It should be reviewed, updated, and validated. The mission statement, the metrics, the escalation criteria, the communication trees: all of it is supposed to be tested against scenarios and revised based on what the testing reveals. The word "capability" appears throughout 800-61 for a reason. A capability is something you can demonstrably do. A document is something you can demonstrably print.

## Where It Breaks Down

The plan gets written by one person, usually a security engineer or a compliance analyst, during a quarter when someone above them decided IR maturity needed to go on a slide. It is comprehensive, well-formatted, and completely theoretical. It names roles that no longer exist. It references an on-call rotation that migrated to a different tool eighteen months ago. It lists a PagerDuty escalation policy that points to a distribution list that bounces.

Contact information rots faster than anything else. The plan says to call the general counsel, but it lists their old cell number. It says to engage the cyber insurance carrier, but nobody knows where the policy PDF lives or what the notification deadline is (it is usually 72 hours, and the clock does not care about your weekend). The forensics retainer everyone assumes exists was never actually signed, or expired, or covers a scope that does not include the cloud environment where all your workloads actually run.

Then there are the technical assumptions that only reveal themselves under load. The plan says to isolate the affected host. Fine: through which mechanism? If your answer is "pull the network cable," you have not accounted for the fact that your endpoints are laptops on a VPN and half your fleet is in a datacenter you can only reach through a jump host whose credentials are in a vault you are now not sure is compromised. The plan says to preserve logs. From where? If your SIEM retention is 30 days and the attacker's dwell time was 90, the evidence you need aged out before you knew you needed it. If your cloud audit logs (CloudTrail, Azure Activity, GCP Audit) were never centralized, you are about to spend the first six hours of an active incident fighting IAM permissions instead of the adversary.

Communication breaks in ways nobody rehearsed. The plan assumes Slack and email work. If the incident involves identity compromise or ransomware touching the mail server, your primary comms channel is now untrusted, and you have no out-of-band bridge because nobody set up a Signal group or a separate conference line ahead of time. Decision authority is undefined: who actually gets to disconnect the production database, pull the company offline, or pay a ransom? In an untested plan, the honest answer is "an argument between three VPs that starts at 2 a.m."

And the roles collapse under the reality of headcount. The RACI chart assumes an incident commander, a scribe, a forensics lead, a comms lead, and a legal liaison. Your actual security team is four people, two of whom are on the incident, one of whom is asleep, and one of whom left last month. The plan was written for an organization that does not exist.

None of this is discovered during a real incident because you have time. It is discovered because you have run out of it.

## Doing It Right

Start with a tabletop, because it is cheap and it exposes the most failures per hour invested. Get the actual humans in a room (or a call): security, IT, legal, comms, an executive sponsor, and whoever owns your critical systems. Present a realistic scenario and walk it in real time. Do not narrate the happy path. Inject complications: the primary IC is unreachable, the backup domain controller is also affected, the press has already called. The goal is not to feel good. The goal is to find the gaps while they are free to find.

Write down every question that nobody could answer immediately. "Who has the insurer's number?" "How do we image a host in the cloud?" "Is our retainer active?" Each of those is an action item, and the tabletop is worthless if it does not produce a list of things to fix. 800-61's Post-Incident Activity phase applies to exercises too: run a lessons-learned session and actually update the plan.

Then graduate to functional exercises. Do not just talk about pulling a host off the network; do it in a staging environment. Restore a backup and time it, because "we have backups" and "we can recover in the RTO we promised the board" are different claims, and only one of them is testable. Practice standing up your out-of-band comms channel from a cold start. Rotate a credential and watch what breaks. Pull EDR telemetry and confirm you can actually build a timeline from it.

Fix the boring infrastructure that IR depends on. Centralize logs with retention that exceeds plausible dwell time (a year of authentication and audit logs is not extravagant). Maintain an offline, updated contact roster with personal numbers for the people who matter. Pre-stage forensic tooling and access so you are not provisioning a jump box during hour one. Keep the runbooks specific: exact commands, exact console paths, exact isolation procedures per platform, not "contain the threat."

Schedule the exercises on a cadence and treat them as non-optional. Quarterly tabletops, an annual functional drill. Rotate who plays incident commander so the capability does not live in one person's head, because that person will inevitably be on vacation when it matters. Version-control the plan and date the last exercise on its front page, so anyone reading it knows whether they are holding a capability or an artifact.

## The Bottom Line

You will have an incident. That part is not in question. The only variable is whether the first time your team executes the plan is during a drill you designed or during a breach the adversary designed. One of those you get to pause, rewind, and learn from. The other one has lawyers, deadlines, and an audience.

An untested plan is a comforting fiction, and comforting fictions are exactly the kind of thing that gets you at 2 a.m. Run the plan before it runs you.

*File under: things you will wish you had done last quarter.*

## Related

- [Least Privilege, Actually Enforced](/itsalreadywhen/rtfm/2026/07/01/least-privilege-actually-enforced/)
- [Logging Without Anyone Reading the Logs](/itsalreadywhen/rtfm/2026/07/15/logging-without-anyone-reading-the-logs/)
- [Segmentation as an Assumption, Not a Diagram](/itsalreadywhen/rtfm/2026/07/29/segmentation-as-an-assumption-not-a-diagram/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)
