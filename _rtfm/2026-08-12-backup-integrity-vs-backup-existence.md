---
layout: rtfm
title: "Backup Integrity vs. Backup Existence"
date: 2026-08-12
summary: "Every organization claims it has backups, but far fewer can prove those backups restore under pressure, and ransomware crews have built a business model on the difference."
framework: "NIST Cybersecurity Framework — Recover (RC.RP)"
framework_url: "https://www.nist.gov/cyberframework"
---

Every organization has backups. That is the claim, and it is technically true right up until the moment someone needs one. The distance between "we run backups" and "we recovered production from backups in four hours" is where entire companies quietly die, and it is a gap that ransomware operators understand better than most CISOs do. They are not betting that you lack backups. They are betting that you have never actually restored one.

## The Standard

The NIST Cybersecurity Framework places recovery under the Recover function, specifically the Recovery Planning category (RC.RP). The language is deliberately unglamorous. RC.RP calls for recovery processes and procedures to be maintained and tested so that timely restoration of systems and assets affected by an incident is possible. Read that again. Not "maintained." Maintained *and tested*. The framework does not congratulate you for owning backup software. It asks whether the recovery path works.

CSF 2.0 sharpened this by pulling recovery into its own explicit outcomes: RC.RP-01 (the recovery plan is executed), RC.RP-04 (critical mission functions and cybersecurity risk are considered when establishing post-incident operational norms), and RC.RP-05, which is the one everyone skips: the *integrity of backups and other restoration assets is verified before using them for restoration.* That is the whole ballgame in a single control. NIST is telling you, in plain regulatory prose, that a backup you have not verified is not a backup. It is a hope with a timestamp.

The companion guidance in NIST SP 800-34 (Contingency Planning) and SP 800-184 (Guide to Recovering from Ransomware and Other Destructive Events) goes further, describing recovery tiers, backup rotation, offline copies, and the expectation that you test restoration on a defined cadence, not the day you find out you needed to.

## Where It Breaks Down

The failures are boringly consistent across every environment I have seen, and they cluster in a few places.

**The backup job succeeds and the data is garbage.** Your backup software reports green. What it verified was that it wrote bytes to a target. It did not verify that those bytes reconstitute a bootable, consistent system. Application-consistent backups require quiescing the workload (VSS on Windows, pre/post-freeze scripts on hypervisors, flushing buffers on databases). When that quiescing silently fails, you get a crash-consistent image of a database mid-write. It backs up fine. It restores into an unrecoverable state. Nobody notices because nobody restored it.

**Restore was never tested end to end.** Teams "test backups" by restoring a single file to a temp directory and calling it a day. That validates almost nothing. It does not exercise bare-metal recovery, it does not validate that your restore depends on a domain controller that is itself encrypted, and it does not measure how long a full environment rebuild actually takes against your stated RTO. The RTO on the spreadsheet is aspirational. The real RTO is whatever the restore actually clocks in at, and you have never measured it.

**The backups are online and writable from the same identity plane as production.** This is the one the ransomware crews eat for breakfast. If your backup server is domain-joined, if the backup repository is a mounted SMB or NFS share, if the backup service account is a Domain Admin (and it is, do not lie), then the same credential that owns production owns your recovery. Modern intrusion playbooks target the backup infrastructure *first*: enumerate Veeam/Commvault/NetBackup servers, dump their credentials, delete or encrypt the repositories, *then* detonate. Your 3-2-1 strategy becomes 0-0-0 in a single lateral movement.

**Snapshots are mistaken for backups.** SAN snapshots, VM snapshots, and cloud volume snapshots living in the same fault and trust domain as the source are not backups. They are convenient rollback points that share the blast radius. An attacker with hypervisor or storage-array access deletes them alongside everything else.

**Retention does not survive dwell time.** Attackers sit in networks for weeks. If your retention is fourteen days and dwell time was thirty, every backup you hold contains the implant. You restore, you get reinfected, and now you have burned your only clean copies discovering it.

**Immutability is claimed, not enforced.** "Immutable" object storage configured without an actual retention lock, or with a root/admin key that can shorten the lock, is immutable the way a screen door is a vault. If a single credential can disable versioning or object lock, it is not immutable.

**Encryption keys and recovery documentation live inside the thing you are recovering.** The runbook is on the file share that got encrypted. The disk encryption recovery keys are in the AD-integrated key management that is down. The backup catalog is on the backup server whose OS is bricked. Recovery has a circular dependency and nobody drew the graph.

## Doing It Right

Start by treating RC.RP-05 as literal. Verification is a control, not a vibe.

**Automate integrity verification, not just job success.** Use checksum verification on backup data at rest and periodic restore-and-validate jobs. Tools in this category (Veeam SureBackup, or equivalent scripted restores into an isolated sandbox) will actually boot the restored VM, run heartbeat and application checks, and prove it comes back. For databases, restore to a scratch instance and run consistency checks (DBCC CHECKDB, `pg_verify_checksums`, integrity checks appropriate to the engine). If you are not booting it, you have not verified it.

**Break the trust plane.** The backup infrastructure must not authenticate against the same identity provider as production. Separate credentials, separate directory, MFA on the backup console, and no Domain Admin service accounts. Follow the 3-2-1-1-0 model: three copies, two media types, one offsite, one offline or immutable, and zero verification errors. The offline copy is the point. Tape still exists for a reason, and an air gap an attacker cannot script around is worth more than any product feature.

**Enforce immutability at the storage layer.** Use object lock in compliance mode (not governance mode, which admins can override), WORM-configured repositories, or hardened Linux repositories with immutability flags set outside the reach of the backup service account. Verify that no single credential can shorten or remove the retention lock. Test this by attempting deletion with your most privileged account and confirming it fails.

**Extend retention past realistic dwell time.** Hold backups long enough to reach a provably clean point. Ninety days of recoverable history is a reasonable floor for the copies that matter, with immutability across that window.

**Test full recovery on a schedule and time it.** Run a real disaster recovery exercise at least quarterly for tier-one systems. Rebuild into an isolated network. Recover the domain controllers first, because everything else depends on them, and validate that you *can* stand up authentication from nothing. Record the actual elapsed time and compare it to your stated RTO. When they diverge, fix the RTO or fix the process, but stop lying to the auditor.

**Store recovery dependencies out of band.** Runbooks, backup catalogs, KMS recovery keys, and network diagrams belong somewhere that survives the primary environment being gone. Printed, offline, or in an isolated tenant. If recovering the runbook requires the thing the runbook recovers, you have already lost.

## The Bottom Line

Nobody gets fired for the backups that ran every night for three years. They get fired the one afternoon those backups do not come back, and that afternoon always arrives when the network is on fire and the RTO clock is running against an audience of very unhappy executives. The framework has told you the answer for years: verify integrity before you need it. It is not a hard control. It is just a thankless one, which is why it stays undone until the day it becomes the only thing that matters.

You do not have backups. You have a hypothesis. Go test it before someone else does it for you.

*Restore it now, or explain later why you couldn't.*

## Related

- [Segmentation as an Assumption, Not a Diagram](/itsalreadywhen/rtfm/2026/07/29/segmentation-as-an-assumption-not-a-diagram/)
- [Least Privilege, Actually Enforced](/itsalreadywhen/rtfm/2026/07/01/least-privilege-actually-enforced/)
- [Incident Response Plans Nobody Has Run](/itsalreadywhen/rtfm/2026/08/05/incident-response-plans-nobody-has-run/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)
