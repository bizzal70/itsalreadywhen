---
layout: rtfm
title: "Patch Cadence vs. Patch Theater"
date: 2026-07-08
summary: "A patching policy is a document; patching is a measurable outcome, and the gap between the two is where most organizations quietly live."
framework: "CIS Critical Security Control 7 — Continuous Vulnerability Management"
framework_url: "https://www.cisecurity.org/controls/cis-controls-list"
---

Every organization has a patching policy. Almost none of them can tell you, with a straight face and real data, what percentage of their exploitable assets got patched within the window that policy promises. These are not the same claim, and the distance between them is where breaches actually happen. "We have a patching policy" is a statement about a PDF. "We patch" is a statement about the world, and the world is considerably less cooperative than a PDF.

## The Standard

CIS Critical Security Control 7, Continuous Vulnerability Management, is refreshingly unromantic about what it wants. It asks you to do four things and to keep doing them: establish and maintain a documented vulnerability management process (7.1), establish and maintain a remediation process with defined timelines by risk (7.2), perform automated operating system patch management (7.3) and automated application patch management (7.4), and perform authenticated vulnerability scanning on both internal and external-facing assets (7.5 through 7.7).

The word doing the heavy lifting is "continuous." Control 7 does not describe a project. It describes a loop: discover assets, scan them with credentials, prioritize what you find against actual risk, remediate within a defined SLA, and then verify the fix landed by scanning again. The verification step is not decorative. A vulnerability you believe you remediated but never confirmed is still an open vulnerability, plus a false sense of security, which is strictly worse.

Note also that Control 7 leans on Controls 1 and 2. You cannot patch what you do not know you own. The control assumes you have an asset inventory and a software inventory, because remediation timelines are meaningless if the denominator, the total set of things that need patching, is unknown. Most "patch coverage" numbers are lies of omission: 98% of the assets we know about, and we do not talk about the ones we do not.

## Where It Breaks Down

The failures are boringly consistent across organizations of every size.

**Unauthenticated scanning masquerading as vulnerability management.** A network scan that fingerprints a service banner over the wire tells you what a port looks like from outside. It does not tell you the patch level of the installed package, the version of a statically linked library buried in an application, or whether a kernel is running a version different from the one on disk because nobody rebooted. Control 7.5 says *authenticated* for a reason. Credentialed scans read the actual package database, the registry, the installed build numbers. If your scanner is not authenticating, you are measuring the paint, not the structure.

**Patch coverage metrics that hide the reboot gap.** Package managers are happy to report a patch as "installed" the moment the new binary is on disk. But a running process is still executing the old code loaded into memory. `apt` will happily update `glibc` while every long-running daemon on the box keeps the vulnerable version mapped until restart. The kernel is the obvious case, but shared libraries are the silent one. Tools like `needrestart` or `checkrestart` exist precisely because "patched" and "no longer running the vulnerable code" are different states, and most patch dashboards conflate them.

**SLA timelines measured from the wrong clock.** A policy that says "critical vulnerabilities patched within 7 days" sounds firm until you ask: seven days from when? From vendor disclosure? From when your scanner detected it? From when a ticket was opened? Each choice can differ by weeks. Organizations quietly reset the clock to the moment of internal detection, which conveniently excludes the discovery latency that is often the largest part of exposure.

**The long tail nobody owns.** OS patching gets automated because Windows Update, WSUS, `dnf-automatic`, and MDM profiles make it tractable. Control 7.4, application patching, is where it collapses. The Java runtime embedded in a vendor appliance. The OpenSSL statically compiled into an internal Go binary from three teams ago. The npm dependency tree of a service whose owner left the company. Container base images pinned to a tag and never rebuilt. These do not show up in the OS patch report, and no automated updater touches them.

**Prioritization by CVSS base score alone.** Control 7.2 asks you to prioritize by risk. A CVSS base score is not risk. It ignores whether the vulnerability is on an internet-facing asset, whether a public exploit exists, whether the affected component is actually reachable or loaded, and whether compensating controls apply. Treating a 9.8 on an isolated internal test box the same as a 7.5 on an exposed VPN concentrator is how remediation queues become undifferentiated backlogs of tens of thousands of "criticals" that no human triages.

**Ephemeral and cloud assets outrunning the scan cycle.** A weekly scan cadence assumes assets live longer than a week. Autoscaling groups, spot instances, and short-lived containers appear and vanish between scans, so they are either never assessed or assessed after they no longer exist. Meanwhile the *image* they were built from, the actual unit of remediation, sits unscanned in a registry.

## Doing It Right

Start by refusing to report a coverage percentage without stating the denominator. Reconcile your vulnerability scanner's asset list against your CMDB, your cloud provider's inventory APIs, your EDR console, and your DHCP or NAC logs. The assets that appear in one source and not another are your actual attack surface. This reconciliation is tedious and permanent. Automate it or it will not happen.

Run authenticated scans. Provision least-privilege scan credentials (read-only, no interactive login, source-IP restricted, rotated) and confirm authentication success rates per scan, not just aggregate findings. A credentialed scan that silently fell back to unauthenticated is a common and dangerous failure mode; alert on the auth-success rate dropping.

Instrument the reboot gap explicitly. On Linux, incorporate `needrestart` output or check `/var/run/reboot-required` into your compliance reporting. On Windows, track pending-reboot registry keys. Report two numbers: "patch applied" and "patch active." The delta is your real exposure and the metric your leadership has never seen.

Measure your SLA from detection, and separately measure detection latency itself (time from public availability to when your program first saw it). If discovery latency dominates your exposure window, no amount of fast remediation fixes it, and you need more frequent or continuous scanning rather than a faster ticket queue.

Prioritize with exploitability context, not base score. Enrich findings with exploit-availability feeds (something like a known-exploited catalog), internet-exposure data from your own external scanning, and asset criticality from your inventory. Feed these into remediation SLAs so that an exposed, actively exploited flaw gets a 48-hour clock while an internal, unreachable one gets a routine cycle. This is how you make the backlog triageable by humans.

For the application long tail, shift the unit of remediation upstream. Scan container images in the registry and fail builds on unremediated criticals rather than scanning running containers after deployment. Adopt software composition analysis (SCA) to enumerate embedded and transitive dependencies that OS package managers cannot see. Generate and retain an SBOM per build so that when a component turns out to be vulnerable, you can answer "where do we run this" in minutes rather than in an all-hands archaeology project.

Finally, close the loop with verification. Every remediation ticket should be closed by a subsequent authenticated scan confirming the finding is gone, not by a human asserting the patch was pushed. If your ticketing system lets an engineer close a vuln without rescan evidence, your process has a hole shaped exactly like human optimism.

## The Bottom Line

Nobody gets compromised through the vulnerabilities in their policy document. They get compromised through the ones in the gap: the asset that was not in the inventory, the library that was patched on disk but running in memory, the appliance nobody owned, the scan that quietly fell back to unauthenticated in March and has been lying ever since. A patching policy is a promise you make to an auditor. Patching is a promise you keep to an attacker, and the attacker is the only one checking your work.

You will not close the gap entirely. You will only ever make it smaller, and knowable, and honest. That is the whole job. The organizations that survive are not the ones that patch fastest. They are the ones that know, to the asset, what they have not patched yet.

*File under: things you already knew, filed anyway.*