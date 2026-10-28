---
layout: rtfm
title: "Privileged Access Management Beyond the Vault"
date: 2026-10-28
summary: "Buying a privileged access management tool is not the same as running a privileged access program, and the gap between the two is where most organizations quietly live."
framework: "CIS Critical Security Control 5 — Account Management"
framework_url: "https://www.cisecurity.org/controls/cis-controls-list"
---

There is a particular kind of meeting that happens about eighteen months after a company buys a PAM product. Someone from audit asks how many privileged accounts are vaulted, and the room goes quiet, because the honest answer is "the ones we knew about when we ran the project." A vault is a product. A privileged access program is a discipline, and almost nobody buys the second one along with the first. The checkbox gets ticked, the invoice gets paid, and the actual problem, which is that too many identities can do too many irreversible things with too little friction, remains exactly where it was.

## The Standard

CIS Critical Security Control 5, Account Management, is deliberately unglamorous. It does not say "buy a vault." It says to establish and maintain an inventory of accounts, to use unique credentials, to disable dormant accounts, to restrict administrator privileges to dedicated accounts, and to maintain an inventory of service accounts. Control 5 pairs with Control 6, Access Control Management, which covers the grant, revoke, and review lifecycle, plus multi-factor authentication and the centralization of access control through a directory or SSO.

Read together, these controls describe a loop, not a purchase. You cannot manage what you have not inventoried. You cannot rotate what you have not inventoried. You cannot revoke access for a leaver whose entitlements you never mapped. The framework assumes you know every account that exists, what class it belongs to (user, administrator, service, non-human), where it can authenticate, and what it is entitled to do once it does. The vault is an implementation detail that sits inside this loop. It is the place you put secrets so humans stop pasting them into Slack. It is not the loop itself.

The distinction matters because Control 5 is explicit that administrator privileges belong to dedicated accounts, separate from the day-to-day identity a person uses to read email and attend meetings. That single requirement, taken seriously, reorganizes how an entire estate authenticates. Most organizations treat it as advice.

## Where It Breaks Down

The first failure is scope, and it is almost always the same shape. The PAM rollout covers domain administrators, a handful of named break-glass accounts, and maybe the root passwords for a few flagship Linux boxes. Meanwhile the actual privileged surface is enormous and lives everywhere the project did not look: local administrator accounts on ten thousand workstations sharing one password because an old imaging process baked it in, `sa` accounts on SQL Server instances with sysadmin and a password from 2016, SSH keys scattered across home directories with no passphrase and no expiry, API tokens in cloud IAM with wildcards in the policy document, and the service account that runs the backup job and happens to be a Domain Admin because that was the fastest way to make it work on a Friday.

The second failure is that service accounts and other non-human identities get waved through entirely. Control 5 calls them out specifically because they are the hardest. They cannot do interactive MFA. They authenticate constantly. They are owned by nobody and depended upon by everything, so nobody dares rotate them. A vault can store the credential, but if the application reads that credential once at startup and caches it in memory for ninety days, rotating it in the vault accomplishes nothing but the illusion of control. Kerberos service accounts with no managed service account configuration, OAuth client secrets hardcoded into CI pipelines, cloud instance roles with permissions that nobody has reviewed since provisioning: none of this is solved by onboarding a human-oriented password vault.

The third failure is standing privilege. The vault checks out a credential, the admin does their work, and the credential goes back in the box. Fine. But the account itself is still a permanent member of a privileged group. The access is standing; only the password is managed. An attacker who compromises an active session, steals a Kerberos ticket, or abuses a cached token does not need to visit your vault. The entire value proposition collapses if the identity retains its power twenty-four hours a day while the secret is merely rented out hourly.

The fourth failure is the broken lifecycle. Control 5 wants dormant accounts disabled and leaver access revoked. In practice the joiner-mover-leaver process is wired to HR for employee accounts and to nothing at all for the privileged, service, and contractor accounts that matter most. People change teams and accumulate entitlements forever because nothing ever removes the old ones. The access review, when it happens, is a spreadsheet emailed to managers who approve every line because reading it would take two hours they do not have.

The fifth failure is that the vault becomes the single most valuable target in the estate and is protected like a wiki. It federates to the same SSO as everything else, so a compromise of the identity provider is a compromise of the vault. Its own administrators are not themselves tiered. The break-glass procedure is a document nobody has tested, and the emergency credential is in a different, worse vault called "someone's password manager."

## Doing It Right

Start with discovery, not deployment. Before anything goes into a vault, run actual enumeration: query Active Directory for members of all privileged groups including nested ones, scan for local administrator accounts and shared local passwords, inventory SSH authorized_keys across your fleet, pull every IAM principal and role in your cloud accounts, and catalog service accounts by querying for SPNs and reviewing scheduled tasks and running services. You are building the inventory Control 5 demands. Treat anything you cannot attribute to a named owner and a documented purpose as a finding.

Adopt a tiered administration model. Microsoft's tier model is the canonical reference: Tier 0 is anything that controls identity (domain controllers, the PKI, the identity provider, and yes, the PAM system itself), Tier 1 is servers and applications, Tier 2 is workstations. Credentials from one tier never authenticate to a lower tier. This is what "dedicated administrator accounts" from Control 5 actually looks like when implemented. Admins get a separate, cloud-synced-or-not privileged identity that only ever touches privileged hosts, ideally from a Privileged Access Workstation that does not browse the web.

Move from standing access to just-in-time. The goal is zero standing privilege: accounts sit with no elevated membership by default, and privilege is granted for a bounded window, tied to an approval or a ticket, and automatically revoked. Pair this with session isolation so the credential is never exposed to the operator's endpoint, and with session recording for the privileged activity you cannot prevent.

Solve the local administrator problem with a managed solution like LAPS, which gives every machine a unique, rotated local admin password backed by the directory. For non-human identities, prefer platform-native constructs that remove the long-lived secret entirely: group managed service accounts for Windows, instance and workload identities in cloud, and short-lived certificate-based or OIDC-federated authentication for pipelines. A secret you never minted cannot be stolen or forgotten in a vault.

Wire the lifecycle to something authoritative. Deprovisioning must be event-driven off HR and ticketing, not quarterly cleanup. Make access reviews small, frequent, and scoped to entitlements that actually confer risk, and enforce automatic expiry on grants so the default state is revoked. Enforce phishing-resistant MFA (FIDO2, certificate-based) on every privileged authentication, and protect the PAM platform and your break-glass accounts as the Tier 0 assets they are, with tested recovery procedures stored offline.

## The Bottom Line

The vault was never the hard part. The hard part is admitting how many things in your environment can quietly become administrator, and accepting that managing their passwords is not the same as managing their power. You can spend a seven-figure budget and still have an estate full of standing privilege, orphaned service accounts, and a joiner-mover-leaver process that ends at the vault's edge. The tool will dutifully rotate the credentials you told it about and feel, warmly, like progress. The accounts you forgot are still out there, still privileged, still waiting. They were there before you bought anything, and they will be there long after the renewal.

*File under: things that were already true before you noticed.*

## Related

- [Least Privilege, Actually Enforced](/itsalreadywhen/rtfm/2026/07/01/least-privilege-actually-enforced/)
- [Change Management as a Security Control](/itsalreadywhen/rtfm/2026/10/07/change-management-as-a-security-control/)
- [Asset Inventory: You Can't Protect What You Don't Know You Have](/itsalreadywhen/rtfm/2026/09/02/asset-inventory-you-can-t-protect-what-you-don-t-know-you-have/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)
