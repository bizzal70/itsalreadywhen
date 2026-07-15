---
layout: rtfm
title: "Logging Without Anyone Reading the Logs"
date: 2026-07-15
summary: "Everyone collects logs; almost nobody reads them, and the gap between compliance logging and operational detection is where breaches live undetected for months."
framework: "CIS Critical Security Control 8 — Audit Log Management"
framework_url: "https://www.cisecurity.org/controls/cis-controls-list"
---

Every organization logs. Almost none of them read the logs. This is the oldest open secret in the industry: a SIEM humming in the corner, ingesting a few terabytes a day, generating dashboards nobody opens, firing alerts nobody triages, and satisfying an auditor who checked a box that said "audit logging: enabled." The comforting fiction is that collection equals visibility. It doesn't. Collection is storage. Detection is work. And the distance between the two is measured in the number of days an attacker gets to operate before anyone notices, which industry data has kept pinned in the triple digits for the better part of a decade.

## The Standard

CIS Critical Security Control 8, Audit Log Management, exists precisely because "we have logs" and "we can detect anything" are unrelated claims. The control breaks into eight safeguards, and it is worth reading them in order because the order is the point.

It starts with 8.1, establishing an audit log management process, and 8.2, collecting audit logs. Fine, table stakes. But 8.3 requires you to *ensure adequate audit log storage*, because logs that roll over in three days are logs you can't investigate an incident with. 8.4 mandates *time synchronization*, because correlation across sources is impossible when your firewall, your domain controller, and your web tier disagree about what time it is. 8.5 pushes for *detailed audit logging*, capturing source, destination, timestamp, user, and event outcome, not just "something happened." 8.6 and 8.7 extend collection to DNS and URL/command-line activity. And 8.9 through 8.11 get to the part everyone skips: *centralize* the logs, *retain* them for a defined period (CIS suggests a minimum of 90 days, ideally longer), and *conduct reviews*.

Read that last one again. The control does not say "collect logs." It says review them. The entire framework is constructed to funnel you toward the act of looking. Most implementations stop at 8.2 and declare victory.

## Where It Breaks Down

The failures are specific and depressingly consistent.

**Logging the wrong things, verbosely.** Teams turn on everything the vendor offers and then drown. A domain controller with full Kerberos and NTLM auditing enabled but no tuning will bury a golden-ticket anomaly under a million routine 4624 and 4634 logon events. Windows Event ID 4688 (process creation) is enormously valuable, but only if you also enabled the command-line auditing GPO, which is off by default. Most environments log that a process started and never capture *what it was invoked with*, which is the one field that turns "powershell.exe ran" into "powershell.exe ran a base64-encoded download cradle."

**The endpoints that never talk.** Domain controllers ship logs. The Linux jump host someone stood up in 2019 does not. Cloud control planes are their own dark continent: CloudTrail exists, but management events and data events are separately configured and separately billed, so data events (the S3 object-level reads that actually reveal exfiltration) are frequently disabled to save money. Kubernetes audit logging is off unless you explicitly wrote an audit policy and wired it into the API server flags. Every one of these gaps is a place where an attacker operates with zero telemetry.

**Ingestion without parsing.** A log that arrives as an unparsed blob is a log that cannot be queried, correlated, or alerted on. Syslog dumped into an index with no field extraction is a haystack with no magnet. If your `user`, `src_ip`, and `action` fields aren't normalized to a schema (ECS, OCSF, whatever you've chosen), then a query for "all failed authentications by this account across all sources" returns nothing useful, and nobody writes the detection because writing it is miserable.

**Alerts with no owner and no triage.** The SIEM ships with a thousand correlation rules enabled out of the box. They fire constantly. Within a month the analysts have muted the noisy ones, and within a quarter they've stopped looking at the channel entirely. This is alert fatigue, and it is not a personal failing; it is the predictable outcome of deploying detection content nobody tuned against a baseline nobody established.

**Retention that quietly lies.** Someone configured 90 days of hot retention, then the ingestion volume tripled, the storage tier filled, and the index started aging out at eleven days. Nobody noticed, because nobody was querying anything older than yesterday. The 90-day number still lives in the compliance document.

**No time discipline.** NTP is "probably fine." Then an incident happens, you pull logs from four systems, and their timestamps span a nine-minute spread with two different time zones and one host stuck in local time with no offset recorded. Correlation collapses. This is Safeguard 8.4, ignored, and it poisons everything downstream.

## Doing It Right

Start from the question, not the source. Detection engineering means deciding *what you want to catch* and then working backward to the telemetry that would reveal it. Map your desired detections to a framework like MITRE ATT&CK, identify the data sources each technique requires, and only then decide what to collect. This inverts the usual order and immediately tells you that you don't need debug-level logs from everything; you need specific, high-fidelity events from the right places.

Fix the plumbing before the analytics:

- **Time first.** Enforce NTP from a common, trusted source across every host. Log in UTC everywhere and record the offset. Nothing else works until this does.
- **Centralize with structure.** Ship to a central store (a SIEM, or a log pipeline built on something like the Elastic stack, OpenSearch, Loki, or a managed platform) and normalize to a schema at ingest. Use a pipeline layer (Cribl, Logstash, Vector, Fluent Bit) to parse, enrich, and drop noise *before* indexing, which also controls the cost that drives the retention lies.
- **Log the fields that matter.** Enable command-line process auditing (Event ID 4688 with the GPO, or Sysmon Event ID 1 with a curated config such as the widely used community baseline). Turn on PowerShell script block logging (Event ID 4104). Enable CloudTrail data events for sensitive buckets, and a Kubernetes audit policy scoped to writes and exec.

Then do the part the control actually asks for: review. Build a small set of high-signal detections you trust and tune them against your real baseline until the false-positive rate is livable. A dozen reliable alerts beat a thousand ignored ones. Write them as code, version them, test them, and treat them like software (detection-as-code). Run periodic threat hunts against the centralized data for the things too subtle to alert on: anomalous service-account logons, first-time parent/child process pairs, outbound connections from servers that should never initiate them.

And validate. Run atomic tests, generate the event you claim to detect, and confirm it (a) was collected, (b) was parsed, and (c) fired. An untested detection is a hypothesis, not a control. The number of "enabled" alerts that silently broke when a log source changed format would embarrass the entire profession if anyone measured it.

## The Bottom Line

Nobody gets fired for buying a SIEM. Plenty of people get breached behind one. The logs were there the whole time, dutifully collected, faithfully retained, gloriously unread, and the forensics team will find the smoking gun three weeks after the attacker left, in an index everyone had access to and no one had opened. Collection is a purchase order. Detection is a discipline, and disciplines require someone whose job is to actually look. Until then you don't have a security control, you have a very expensive write-only database and a clean audit report to bury with it.

*Your logs already saw it. That was never the problem.*