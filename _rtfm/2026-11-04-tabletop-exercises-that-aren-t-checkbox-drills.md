---
layout: rtfm
title: "Tabletop Exercises That Aren't Checkbox Drills"
date: 2026-11-04
summary: "A tabletop exercise that everyone leaves feeling good about accomplished nothing; if your scenario didn't expose a gap that made someone uncomfortable, you ran a meeting, not a test."
framework: "NIST SP 800-84 — Guide to Test, Training, and Exercise Programs"
framework_url: "https://csrc.nist.gov/pubs/sp/800/84/final"
---

There is a particular kind of tabletop exercise that exists only to be survived. Everyone knows their lines, the scenario is a gentle fiction, and the after-action report writes itself: "Communication was effective. Teams performed well. Minor improvements identified." You have all been to this meeting. It is theater, and the only thing it tests is your collective ability to sit in a conference room for ninety minutes without saying anything true. If nobody walked out of your exercise uncomfortable, you did not run an exercise. You ran a status update with catering.

## The Standard

NIST SP 800-84, the *Guide to Test, Training, and Exercise Programs for IT Plans and Capabilities*, is remarkably clear about what a tabletop exercise is supposed to do, and most people who cite it have not read past the title. The document distinguishes carefully between **tests** (pass/fail evaluations of a specific component against expected results), **training** (building individual skills), and **exercises** (evaluating the interaction of people and plans under simulated conditions). Tabletop exercises fall into that third category, and 800-84 is explicit that their purpose is discussion-based validation of plans, roles, and decision-making, not confirmation that everyone already knows what to do.

The standard lays out a real program structure around this. You define a **scope** and measurable **objectives** before you write anything. You build a **scenario** with a documented timeline of injects, the pieces of new information introduced over the course of the exercise to drive discussion and force decisions. You assign a **facilitator** who is not a participant and whose job is to keep pressure on. You designate **evaluators** against predefined success criteria. And critically, 800-84 treats the **after-action report** and the resulting **improvement plan** as the actual deliverable. The exercise is not the product. The list of things you found broken is the product.

Section 3.1 is blunt about the point of the whole enterprise: exercises exist to identify gaps in plans and capabilities. If your exercise is not designed to surface gaps, it is not conforming to the standard regardless of how many boxes you ticked. The discomfort is not a side effect. It is the deliverable.

## Where It Breaks Down

The first failure is the **pre-negotiated scenario**. Someone circulates the inject timeline to participants a week in advance "so people can prepare." Now you are testing rehearsal, not response. In a real incident nobody gets the runbook emailed to them before the pager goes off. The entire value of a tabletop is watching people reason under uncertainty, and you have deleted the uncertainty to protect everyone's feelings.

The second failure is **scoping the scenario around systems you already handle well**. Teams reflexively build exercises around ransomware on a Windows file server, because they have EDR, immutable backups, and a tested restore procedure for exactly that. The exercise confirms what you knew. Meanwhile nobody tabletops the scenario that actually keeps you up: your SSO provider is down and you cannot authenticate to the very consoles you need to run the response, or your logging pipeline is the thing that got compromised so your forensic timeline has a hole in it precisely where the attacker was. You exercise the thing with a playbook and avoid the thing without one.

The third failure is the **"and then the tool catches it" assumption**. Injects are written so that your SIEM correlation rule fires, your DLP flags the exfil, your NDR appliance surfaces the beacon. Real exercises assume controls fail. What happens when the attacker is living off the land, using signed binaries and valid credentials, and nothing fires at all? What happens when your detection depends on logs from an endpoint that got wiped? If every inject resolves because a product does its job, you are exercising the marketing slide, not the incident.

The fourth failure is **letting participants answer in the future tense**. "We would isolate the host." Would you? With what? Name the tool, name the person with console access, name what happens when that person is on a plane. "We'd pull the logs." From where? Are they still in retention? Is the retention window shorter than the dwell time you just discovered? A facilitator who accepts aspirational answers is running a brainstorm, not an exercise.

The fifth failure is **excluding the people who make it uncomfortable**. The tabletop is staffed entirely by the security team, so every decision is clean and technical. Nobody from Legal is there to ask whether you have a notification obligation and a clock already running. Nobody from Comms is there to draft the external statement under time pressure. No executive is there to decide whether you pay, whether you take the production system offline during business hours, whether you call law enforcement. These are the decisions that actually stall during a real incident, and they are exactly the ones a security-only tabletop never touches.

The sixth failure is the **report that laundered the findings**. The exercise surfaced that only one engineer knows how to fail over the primary database, that the incident bridge invite went to a stale distribution list, that nobody could locate the current contact at the upstream provider. By the time it reaches the after-action report, this has become "opportunities to enhance cross-team coordination." You found a single point of failure and a dead runbook, and you wrote them down as a vibe.

## Doing It Right

Write **measurable objectives first**, then reverse-engineer the scenario to stress them. Not "test our incident response," but "determine whether we can establish a forensically sound timeline when the primary log source is unavailable," or "measure time-to-decision on customer notification when Legal is in the room." If you cannot state how you would know you failed, you have not written an objective.

Keep the inject timeline **sealed**. The facilitator holds it. Participants see each inject only when it drops. Build injects that **remove capabilities** rather than confirm them: the on-call lead is unreachable, the backup you were about to restore is also encrypted, the credential you need was rotated and nobody documented the new one, the cloud console requires MFA through a device that is part of the compromise. Model the second-order problems, because that is where real incidents actually go sideways.

Assign a facilitator whose explicit job is to **refuse aspirational answers**. Every "we would" gets met with "show me." Pull up the actual runbook during the exercise. If the document references a server that was decommissioned eighteen months ago, you just found a finding, in the room, in real time. That is worth more than the rest of the meeting combined.

Put **Legal, Comms, and an actual decision-maker** in the room and give them injects of their own: a regulator inquiry, a press query, a ransom deadline with a countdown. Run a real clock. Incident response is a time-pressure discipline and a tabletop with no clock is missing the only variable that matters.

Write the after-action report in **specifics with owners and dates**. Not "improve coordination," but "DB failover is a single point of knowledge (owner: X); document and cross-train by Q3." Then do the thing 800-84 actually requires and feed those findings into a tracked **improvement plan**. An exercise whose findings never change a runbook was an expensive way to feel prepared.

## The Bottom Line

The uncomfortable exercise is the cheap one. You get to discover that your log retention is shorter than your attacker's patience while the stakes are a conference room and a whiteboard, instead of a regulator's letter and a disclosure clock. Nobody enjoys the tabletop that goes badly, which is precisely why the ones that go well are worthless. The attacker is not going to email you the inject timeline a week in advance, and when the real thing arrives, the only question that matters is whether you already found the gap or whether it is about to find you. It is already when.

*Run it until it hurts, or don't bother running it at all.*

## Related

- [Incident Response Plans Nobody Has Run](/itsalreadywhen/rtfm/2026/08/05/incident-response-plans-nobody-has-run/)
- [Change Management as a Security Control](/itsalreadywhen/rtfm/2026/10/07/change-management-as-a-security-control/)
- [Backup Integrity vs. Backup Existence](/itsalreadywhen/rtfm/2026/08/12/backup-integrity-vs-backup-existence/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)
