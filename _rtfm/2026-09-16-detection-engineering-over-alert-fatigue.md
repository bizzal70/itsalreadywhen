---
layout: rtfm
title: "Detection Engineering Over Alert Fatigue"
date: 2026-09-16
summary: "A SIEM drowning in noise provides the same security value as no SIEM at all, and the fix is disciplined detection engineering grounded in MITRE ATT&CK rather than more log volume."
framework: "MITRE ATT&CK"
framework_url: "https://attack.mitre.org/"
---

Everybody agrees, in principle, that alerts should be actionable. Everybody nods along when you say that a detection nobody investigates is worse than no detection at all, because at least the absence of a rule doesn't lull you into thinking you're covered. And then everybody goes back to shipping every log source they can find into the SIEM, cranking the correlation rules up to maximum sensitivity, and wondering why the SOC has a burnout problem and a 4,000-alert backlog. This is not a hard problem intellectually. It is a hard problem culturally, because noise feels like diligence and silence feels like negligence, and nobody ever got fired for ingesting too much data.

## The Standard

There is no single control that says "thou shalt not drown thy analysts," but the closest thing the industry has to a coherent doctrine is detection engineering built on **MITRE ATT&CK**. ATT&CK is a knowledge base of adversary behavior organized into tactics (the "why," such as Persistence, Lateral Movement, Exfiltration) and techniques (the "how," such as T1053 Scheduled Task/Job, T1021 Remote Services, T1567 Exfiltration Over Web Service). The point of the framework is not to give you a bingo card of things to fear. The point is to give you a shared vocabulary for describing what you can and cannot see.

Detection engineering treats detections as software. A detection has a hypothesis (what adversary behavior am I trying to catch), a data source (what telemetry proves or disproves it), a logic definition (the query or rule), a fidelity expectation (how often will this fire, and how often will it be right), and a response expectation (what a human does when it fires). ATT&CK's own guidance, through the **Data Sources** and **Data Components** model, ties each technique to the specific telemetry required to observe it. T1021.001 (Remote Desktop Protocol) maps to Logon Session and Network Traffic data components. If you don't collect Windows Security Event ID 4624 with the right logon types, or you don't have network flow visibility on 3389, you cannot detect that technique, and no amount of clever correlation invents the data you failed to collect.

The standard, stated plainly: know which techniques you care about, know what data proves them, write detections against that data with a measured false-positive tolerance, and measure your coverage honestly. Everything else is theater.

## Where It Breaks Down

The first failure is **ingestion as strategy**. Teams license a SIEM by data volume, then spend the budget proving they got their money's worth by piping in DNS logs, DHCP, every firewall deny, proxy logs, and full endpoint verbose auditing, all at once, with no detection plan attached to any of it. You end up paying to store terabytes of Sysmon Event ID 1 (process creation) that nothing queries. The data is there. Nobody looks at it. It is a very expensive tape backup.

The second failure is **vendor default rules run wide open**. Every SIEM and EDR ships with a "content pack" of hundreds of out-of-the-box detections. Most of them are written for a hypothetical average environment that does not exist. The default "PowerShell downloaded a file" rule fires 900 times a day because your patch management tooling, your software deployment agent, and half your legitimate admin scripts all use `Invoke-WebRequest`. Nobody tunes it. Nobody disables it. It just runs, generating noise that gets auto-closed or ignored, and the one time it catches something real, that alert is sitting in a queue behind 3,000 identical false positives.

The third failure is **correlation without baselines**. Rules like "impossible travel" or "unusual login volume" require a statistical model of normal. Implemented naively, they treat a VPN concentrator, a mail server doing service-account authentication, and a jump host as if they were individual human users. The result is a chronic low-grade fever of anomaly alerts that mean nothing because "normal" was never defined per-entity.

The fourth failure is **the coverage lie**. Someone builds an ATT&CK Navigator heatmap, colors in every technique with at least one detection, presents it to leadership, and declares victory. But a single low-fidelity rule tagged T1059 does not mean you "cover" Command and Scripting Interpreter. Coverage is not binary. A detection that fires on 2 percent of real instances of a technique and buries them in false positives is functionally zero coverage, but it lights up green on the map.

The fifth failure is **no feedback loop**. Detections are written once, deployed, and never revisited. When an analyst closes an alert as a false positive, that disposition goes into a ticket and dies there. The rule is never adjusted. Log formats drift, a source stops sending, a field gets renamed in an agent upgrade, and the detection silently breaks. Nobody notices, because a detection that stops firing looks exactly like a quiet network.

## Doing It Right

Start by inverting the process. Do not ask "what data can we collect." Ask "what behaviors matter here, given our actual threat model and our actual crown jewels." Pick a bounded set of ATT&CK techniques prioritized by relevance to your environment (public tools like the **Center for Threat-Informed Defense's** prioritization work and the **DeTT&CT** framework help here). A domain-joined Windows shop with a lot of RDP and service accounts cares about T1078 (Valid Accounts), T1021, T1550 (Use of Alternate Authentication Material), and T1003 (OS Credential Dumping) far more than it cares about obscure macOS persistence.

For each prioritized technique, do a **data source audit** before you write a single rule. Confirm the telemetry exists, arrives reliably, and is parsed correctly. Detecting T1003.001 (LSASS Memory) realistically requires Sysmon Event ID 10 (ProcessAccess) with a tuned config, or equivalent EDR API telemetry. If you don't have it, that's a collection gap ticket, not a detection.

Treat detections as code. Put them in version control. Adopt a portable format like **Sigma** so your logic is not welded to one vendor's query language, and use its pipelines to compile to your backend. Every detection gets metadata: the ATT&CK technique ID, the data source it depends on, an owner, and a documented false-positive profile. Wherever possible, validate detections with adversary emulation. **Atomic Red Team** gives you per-technique test cases; run them, confirm the detection fires, and record it. This turns "we think we cover T1021" into "we have a repeatable test that proves it."

Set and enforce a fidelity budget. A production alert should have a defensible expectation of being worth a human's time. If a rule's precision is unacceptable, you have three honest options: enrich it (add context so the logic is tighter), demote it (send it to a correlation layer or a hunting dataset instead of the analyst queue), or delete it. "Leave it firing and ignore it" is not on the menu. Use tiered outputs: high-fidelity detections page a human, medium-fidelity ones aggregate into risk-scored entities (the model behind risk-based alerting), and low-fidelity signals become searchable context, not tickets.

Close the loop mechanically. Alert dispositions must feed back into detection tuning on a schedule. Track precision per rule over time. Build **detection health monitoring**: alert when a rule that normally fires goes silent, or when a log source's volume drops off a cliff, because a broken detection is the most dangerous kind. The absence of alerts should itself be an alert.

## The Bottom Line

None of this is secret. It is written down in more places than anyone reads. The uncomfortable truth is that a SIEM full of noise and a SIEM turned off produce the same outcome during an actual intrusion: nobody responds in time, because the signal that mattered was indistinguishable from the 3,000 that didn't. Volume is not visibility, a green heatmap is not coverage, and a detection nobody trusts is a liability you pay to maintain. You will not build your way out of this with a bigger license. You build out of it with restraint, with honesty about what you can actually see, and with the discipline to delete the rules that lie to you. Most shops won't. That's fine. The adversaries are counting on it, and so far they've been right.

*Log everything, watch nothing, and act surprised. It's already when.*

## Related

- [Logging Without Anyone Reading the Logs](/itsalreadywhen/rtfm/2026/07/15/logging-without-anyone-reading-the-logs/)
- [Asset Inventory: You Can't Protect What You Don't Know You Have](/itsalreadywhen/rtfm/2026/09/02/asset-inventory-you-can-t-protect-what-you-don-t-know-you-have/)
- [Default Credentials and Configuration Drift](/itsalreadywhen/rtfm/2026/08/19/default-credentials-and-configuration-drift/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)
