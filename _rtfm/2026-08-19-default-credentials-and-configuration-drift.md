---
layout: rtfm
title: "Default Credentials and Configuration Drift"
date: 2026-08-19
summary: "The admin/admin problem never dies; it just migrates to whatever new class of infrastructure you weren't watching, and CIS Control 4 is the map you keep refusing to read."
framework: "CIS Critical Security Control 4 — Secure Configuration Management"
framework_url: "https://www.cisecurity.org/controls/cis-controls-list"
---

There is no vulnerability class older than the default credential, and none more reliably fatal. We have known about `admin/admin` since before most of your fleet was manufactured, yet every generation of infrastructure arrives factory-loaded with the same gift: a known username, a known password, and a documentation PDF that helpfully publishes both. The problem was never that we didn't understand it. The problem is that "change the default" is a task with no owner, no deadline, and no dopamine, so it doesn't happen. And configuration, left alone, does not stay put. It drifts.

## The Standard

CIS Critical Security Control 4, Secure Configuration of Enterprise Assets and Software, exists because the industry needed to write down a thing everyone already claimed to know. The control has two intertwined halves, and most organizations do neither well.

The first half is establishing and maintaining a secure baseline. Safeguard 4.1 asks you to document a hardened configuration for every asset class you operate: workstations, servers, network devices, mobile, cloud instances. Not aspirationally. In writing, versioned, reviewed. The control leans on published hardening references (the CIS Benchmarks, DISA STIGs, vendor security baselines) precisely so you don't have to invent "secure" from scratch.

The second half is the part that gets skipped: maintaining it. Safeguard 4.2 wants that baseline enforced continuously, not stamped once during provisioning and abandoned. Safeguards 4.6 and 4.7 address the credential problem directly: securely manage the configuration of enterprise assets, and, explicitly, manage default accounts. Disable them. Rename them where you can. Change every default password before the asset touches a production network.

The control's underlying thesis is unglamorous and correct. A system's security posture is not a property of its purchase. It is a property of its ongoing configuration state, and configuration state decays. Control 4 is the discipline of measuring that decay and correcting it before someone else measures it for you.

## Where It Breaks Down

The failure is almost never the flagship server. Your domain controllers get hardened. Your internet-facing web tier gets hardened, usually twice, because two teams argued about it. The default-credential problem has simply migrated to the infrastructure nobody has decided is their job.

Start with the network fabric itself. Switches, routers, and wireless controllers ship with default enable passwords and SNMP community strings, and `public`/`private` are still live on more read-write SNMP interfaces than any conference talk will admit. An attacker who can read your switch config via SNMP `public` doesn't need a zero-day. They need `snmpwalk` and patience.

Then the out-of-band layer, which is where this gets genuinely dangerous. Every server has a lights-out management processor: iDRAC, iLO, IPMI, a BMC by whatever name. These devices are full computers with their own network stack, their own web UI, their own default credentials, and total physical-equivalent control over the host. They are routinely racked, cabled to a management VLAN that turns out to be flatter than anyone believed, and never touched again. The host OS gets patched monthly. The BMC still answers to `ADMIN`/`ADMIN` and runs firmware from the year it was manufactured.

Now consider everything that is technically a computer but nobody calls one. IP cameras, badge controllers, environmental sensors, printers (which happily leak LDAP bind credentials from their address-book config if you ask the embedded web server nicely), UPS management cards, PDUs, KVM-over-IP units, industrial gateways. This is the class where "change the default" reliably dies, because the device was bought by facilities, installed by a contractor, and inherited by no one.

The cloud didn't fix this. It relocated it. Default configurations now live in Terraform modules and vendor Helm charts, and an insecure default copied into version control is a secure baseline's evil twin: consistent, reproducible, and wrong at scale. Managed database services still spin up with permissive default network ACLs. Kubernetes clusters run with default service account tokens automounted into every pod and dashboard components deployed with bindings that would make a 1998 network admin blush. The RabbitMQ container in your dev namespace still has `guest`/`guest`, and dev talks to prod because someone was in a hurry.

And underneath all of it: drift. Even where a baseline was applied correctly on day one, entropy takes over. An engineer disables a firewall rule to debug something at 2 a.m. and never re-enables it. A GPO gets a "temporary" exception. A config management run fails silently for three weeks and nobody watches the exit codes. The gap between the documented baseline and the live configuration widens continuously, and the organizations that get burned are the ones who mistook the day-one snapshot for a permanent condition.

## Doing It Right

Treat this as two separate engineering problems: enforcing a known-good state, and detecting deviation from it. You need both, because either one alone lets you lie to yourself.

**Enumerate before you harden.** You cannot secure the configuration of assets you don't know you have. This is where Control 4 leans on Controls 1 and 2 (asset and software inventory). Actively scan for management interfaces, not just hosts. A discovery sweep for IPMI (UDP 623), SNMP (UDP 161), Redfish and vendor BMC web ports, Telnet (still, somehow, 23), and unauthenticated Redis, MongoDB, and Elasticsearch will find things that are not in anyone's CMDB. Those are your real perimeter.

**Codify the baseline, don't document it.** A hardening standard that lives in a Confluence page is decoration. Encode it as configuration-as-code: Ansible roles, Puppet manifests, DSC, Terraform with policy-as-code guardrails (OPA/Conftest, Sentinel). Start from a published benchmark rather than inventing your own, then version it and gate changes through review. The CIS Benchmarks ship as machine-readable content for exactly this reason.

**Kill defaults programmatically, at provisioning time.** Default credentials should be rotated as a build step, not a checklist item. Integrate a secrets manager (Vault, a cloud KMS-backed store, whatever you already run) so that provisioning generates a unique credential per device, stores it, and the human-typed default never survives first boot. For BMCs and network gear where automation is painful, at minimum enforce it through an onboarding runbook that is not "complete" until a scan confirms the default is dead. Disable local default accounts entirely where the platform supports central auth; bind management interfaces to RADIUS/TACACS+ or your IdP so there's one place to revoke access.

**Measure drift continuously and treat the delta as an alert.** This is the safeguard everyone skips. Run configuration assessment on a schedule (CIS-CAT, OpenSCAP against SCAP content, or your CSPM tooling for cloud) and diff the live state against the codified baseline. Any deviation is either an approved exception with an expiry date or an incident. If your config management runs in enforcing mode rather than reporting-only, drift gets corrected automatically and the alert tells you who tried to change it. Reporting-only mode is how you find out you drifted six months ago.

**Segment the management plane and assume the defaults you missed are still there.** You will not get every device. Put BMCs, switch management, and IPMI on a genuinely isolated network reachable only through a bastion, with default-deny egress. Segmentation is the control that survives your own incompleteness.

## The Bottom Line

The default credential is not a technical problem. We solved the technical problem decades ago: change the password, disable the account, rotate the key. It is an organizational problem, which is why it is immortal. Every new tier of infrastructure arrives with the same defect, gets adopted by a team that doesn't own security, and joins the growing pile of things that are "probably fine." The `admin/admin` you patched in 2009 didn't disappear. It got a BMC, then a Helm chart, then a managed service dashboard, and it is sitting on a management VLAN right now waiting for someone who runs `snmpwalk` for a living.

CIS Control 4 is not hard. It is just relentless, and relentless is the one thing organizations reliably fail to be. You will implement it once, feel accomplished, and drift will begin the same afternoon.

*Somewhere on your network, a device is still answering to its factory password. It always is.*

## Related

- [Segmentation as an Assumption, Not a Diagram](/itsalreadywhen/rtfm/2026/07/29/segmentation-as-an-assumption-not-a-diagram/)
- [Least Privilege, Actually Enforced](/itsalreadywhen/rtfm/2026/07/01/least-privilege-actually-enforced/)
- [Third-Party and Vendor Risk Management](/itsalreadywhen/rtfm/2026/07/22/third-party-and-vendor-risk-management/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)
