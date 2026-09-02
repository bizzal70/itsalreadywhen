---
layout: rtfm
title: "Asset Inventory: You Can't Protect What You Don't Know You Have"
date: 2026-09-02
summary: "You cannot defend infrastructure you've never counted, and the assets that get you owned are almost always the ones nobody remembered existed."
framework: "CIS Critical Security Control 1 — Inventory and Control of Enterprise Assets"
framework_url: "https://www.cisecurity.org/controls/cis-controls-list"
---

Every incident postmortem eventually arrives at the same quiet admission: nobody knew the box was there. Not the attacker's clever pivot, not the zero-day, but a forgotten VM running an unpatched service on a subnet somebody stood up for a demo in 2019 and never tore down. Asset inventory is the most boring control in security and the one that quietly determines whether every other control you own actually applies to anything. We all nod along that you can't protect what you don't know you have, and then we go right back to protecting the fraction of the estate we happen to remember.

## The Standard

CIS Critical Security Control 1, "Inventory and Control of Enterprise Assets," sits at number one for a reason that is not accidental. The Center for Internet Security put it first because everything downstream (vulnerability management, access control, logging, incident response) is scoped by what you believe you own. Get the denominator wrong and every percentage you report is fiction.

The control asks for something deceptively simple: actively manage a complete, accurate, and continuously updated inventory of all enterprise assets with the potential to store or process data. That includes end-user devices (both fixed and portable), network devices, IoT and OT, servers, and (critically) assets connected to the infrastructure physically, virtually, remotely, and in cloud environments. It explicitly covers assets not under your control that regularly connect, which is where BYOD and contractor laptops live.

The safeguards escalate in maturity. At Implementation Group 1 you are expected to maintain a detailed inventory with, at minimum, network address, hardware address, machine name, asset owner, department, and approval status. You are expected to address unauthorized assets when discovered, either removing them, denying them network access, or quarantining them. At IG2 and IG3 the control expects active discovery tooling running on a schedule, passive discovery via traffic analysis, and DHCP logging fed into the inventory to catch things the moment they request an address. The word that matters throughout the control text is "continuously." A spreadsheet updated during last year's audit is not an inventory. It is a historical document.

## Where It Breaks Down

The failure is almost never that an organization has no inventory. It is that they have four of them and none of them agree.

The CMDB, lovingly maintained by an ITSM team, reflects assets that went through a change ticket. The cloud provider's console reflects what is running in the accounts anyone remembered to enroll in the org. The vulnerability scanner reflects whatever is in its target ranges, ranges that were defined once and never revisited. The DNS zone files reflect a decade of accreted subdomains. These four data sets have massive non-overlapping regions, and the gaps between them are precisely where you get owned.

Consider the concrete failure modes.

**Shadow IT provisioned with a credit card.** A marketing team spins up a landing page in a SaaS platform or a personal cloud account. It never touches your procurement process, never gets an entry in the CMDB, never enters a scanner's scope. It sits outside your identity provider entirely, authenticating with a shared password in a shared inbox. Your entire security program has no idea it exists until it appears in a breach notification from the provider.

**Forgotten subdomains and dangling DNS.** DNS is where dead assets go to haunt you. A CNAME points `promo.yourcompany.com` at a cloud storage bucket or a PaaS app that was decommissioned. The backing resource is gone but the DNS record remains, which means anyone who can re-register that resource name inherits a hostname on your domain. Subdomain takeover is a direct consequence of an inventory that tracks servers but never reconciles the DNS layer that points to them. Wildcard records make this worse, resolving names for infrastructure that was never inventoried because it was never explicitly created.

**The server nobody remembers provisioning.** Someone cloned a golden image for a load test, exempted it from the patch window "temporarily," and left the company. It is still running, still listening on 3389 or 5985 or a database port, still holding cached credentials, and it has fallen out of every reconciliation loop because nothing actively looks for hosts that stopped checking in with the config management agent. Agent-based inventory has a fatal blind spot: it only sees hosts running the agent. The box that matters is the one where the agent died six months ago and nobody noticed the missing telemetry.

**Cloud accounts outside the organization.** In AWS, Azure, and GCP, individual engineers create standalone accounts and projects that never get pulled into the management org or landing zone. There is no Config aggregator, no Cloud Asset Inventory export, no central billing to even flag them. Ephemeral compute makes the timescale brutal: containers and serverless functions live for minutes, and a nightly scan will never see the thing that was exploited at 2 a.m.

**Scope defined by IP range in a DHCP world.** Scanners configured against static CIDR blocks miss everything that got a lease outside the assumed range, every VLAN added after the config was written, and every asset that lives on an address the scanner was never told about.

## Doing It Right

Start by accepting that no single tool sees everything, and build for reconciliation instead of a single source of truth.

**Run at least two independent discovery methods and diff them.** Active discovery (authenticated scans, ARP sweeps, SNMP walks against network gear) tells you what responds. Passive discovery tells you what talks. Feed a passive traffic monitor or your NDR the span/tap data and let it fingerprint hosts by their protocol behavior. The assets that appear in passive discovery but not in your active scope are your highest-value findings, because they are, by definition, things you did not know to scan.

**Make DHCP and DNS first-class inventory sources.** Ship DHCP lease logs into your SIEM or inventory pipeline so a new lease triggers reconciliation against the known set. Pull authoritative DNS zones (all of them, including internal split-horizon zones) on a schedule and resolve every record. Any A/AAAA/CNAME whose target no longer resolves, or resolves to third-party infrastructure you do not own, is a dangling-record candidate. Cross-reference CNAME targets against your cloud resource inventory to catch takeover exposure before someone else does.

**Instrument the cloud at the org level, not the account level.** Use AWS Organizations with Config aggregators, Azure Resource Graph across all subscriptions under the tenant, and GCP Cloud Asset Inventory exported to a central sink. Enforce that new accounts and subscriptions cannot exist outside the management hierarchy using service control policies and management group governance. Consolidated billing is itself a discovery signal: an account you are paying for that is not in your inventory is a finding.

**Treat missing telemetry as an event.** Do not just alert on new assets. Alert on assets that stopped reporting. A host that vanished from EDR heartbeats but still answers on the network is not gone, it is unmanaged. Reconcile your agent census against your network-layer discovery continuously and generate a ticket for every delta.

**Enforce enrollment at the network edge.** 802.1X with NAC gives you the IG1 mandate to deny or quarantine unauthorized assets by default. An asset that cannot authenticate to the port lands in a remediation VLAN, which converts your inventory from a passive list into an active gate. Require ownership metadata (owner, department, approval status) as a condition of full network access, not as a field somebody fills in later.

**Assign an owner to everything, and expire it.** Every asset record gets a named human owner and a review date. Records that pass their review date without reconfirmation get flagged for decommission. This is how you kill the demo box before it becomes the pivot point.

## The Bottom Line

Nobody gets promoted for finding the forgotten server, and nobody gets a budget line for reconciling DNS against cloud resources. So it doesn't happen, and the estate keeps quietly growing appendages nobody is watching. The attacker's job is not to defeat your best control on your best-known asset. It is to find the one thing you forgot you had, and it is a target-rich environment because you will always forget something. The only question is whether you find it first, on a schedule, with two tools that disagree, or whether you find out from someone else, later, in a room with lawyers in it.

*Count everything, twice, or someone else will count it for you.*

## Related

- [Default Credentials and Configuration Drift](/itsalreadywhen/rtfm/2026/08/19/default-credentials-and-configuration-drift/)
- [Patch Cadence vs. Patch Theater](/itsalreadywhen/rtfm/2026/07/08/patch-cadence-vs-patch-theater/)
- [Least Privilege, Actually Enforced](/itsalreadywhen/rtfm/2026/07/01/least-privilege-actually-enforced/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)
