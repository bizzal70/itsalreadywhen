---
layout: rtfm
title: "Least Privilege, Actually Enforced"
date: 2026-07-01
summary: "Everyone writes a least-privilege policy and almost no one enforces it; here's the gap between the document and an access review that actually revokes something."
framework: "CIS Critical Security Control 6 — Access Control Management"
framework_url: "https://www.cisecurity.org/controls/cis-controls-list"
---

Everyone has a least-privilege policy. It lives in a Confluence page nobody has opened since the last audit, it uses the word "shall" a lot, and it has approximately zero effect on who can read the payroll database at 2 a.m. Least privilege is the security principle most universally endorsed and least frequently enforced, because writing the policy costs a meeting and enforcing it costs you the goodwill of every engineer who has ever been granted `sudo` "just to unblock a deploy." The uncomfortable truth is that access accretes. It only ever accretes. And the access review that was supposed to prune it back is, in most shops, a spreadsheet that gets rubber-stamped once a year by a manager who has no idea what any of the entitlements mean.

## The Standard

CIS Critical Security Control 6, Access Control Management, is not subtle about what it wants. The control covers the full lifecycle of access: granting, using, revoking, and reviewing. The parts practitioners skip are Safeguards 6.1 and 6.2 (a documented process to grant and to revoke access), 6.7 (centralizing access control through a directory or SSO where feasible), and above all 6.8, which asks you to "define and maintain role-based access control" by determining and documenting the access rights necessary for each role and reviewing them.

The word doing the heavy lifting there is *maintain*. Anyone can define an access model on a whiteboard. CIS is asking for the boring, recurring, adversarial work of confirming that the access people actually hold still matches the access they are supposed to hold. Control 5, Account Management, is the sibling you cannot ignore: an inventory of accounts, disabling dormant ones, and managing service accounts. Least privilege is meaningless if you do not know the accounts exist, and Control 6 quietly assumes you have already done Control 5. Most organizations have not.

Read together, the two controls describe a closed loop: you know every identity, you grant each identity the minimum entitlements its role requires, you have a mechanism that revokes those entitlements when the role changes, and you periodically verify that reality matches intent. It is a loop. The failure is almost always that it is not closed.

## Where It Breaks Down

The first break is that "role-based" access control is aspirational fiction in most environments. What you actually have is entitlement-based access control with a role-shaped label glued on top. Someone requests access to a specific S3 bucket, a specific Jira project, a specific `pg_hba.conf` line, and it gets granted directly to their principal. The "Developer" role in your IdP maps to three group memberships; the other forty things a developer can touch were granted one ticket at a time. When you go looking for "what does this role grant," there is no answer, because the role was never the unit of provisioning.

The second break is standing access to everything, all the time. AWS IAM policies with `"Action": "*"` on `"Resource": "*"` because scoping them was hard and the deadline was Friday. Kubernetes `ClusterRoleBinding` to `cluster-admin` because someone could not figure out which `verbs` on which `resources` the CI runner needed. Domain accounts in `Domain Admins` because a vendor's installer asked for it in 2019. Every one of these is a permanent grant for an intermittent need, and permanence is the enemy.

The third break is the machines. Service accounts, CI/CD tokens, OAuth client credentials, and cloud instance roles now outnumber human identities by a wide margin, and they are almost never reviewed. A human at least leaves the company and triggers an offboarding checklist. A service account lives forever, its secret rotated never, its permissions granted by whoever stood up the integration and understood by no one. The static AWS access key checked into a Terraform state file five years ago still works, and it can still assume a role that can delete production.

The fourth break is the review itself, which is theater. The classic failure mode is the annual "user access review" where a system exports a list of usernames and entitlement codes to a spreadsheet, and line managers are asked to certify them. The manager sees `APP_FIN_RW_PROD` next to an employee's name, has no idea what it grants, knows that clicking "revoke" might break something and generate a support ticket with their name on it, and clicks "approve all." Certification rates of 99 percent are not a sign of clean access. They are a sign that nobody read anything. A review that never revokes anything is not a control. It is a compliance artifact.

The fifth break is that even when someone wants to revoke, the revocation path does not exist. Access was granted directly in the resource, out of band from the IdP, so there is no central place to pull it. Nested group memberships mean removing someone from one group does nothing because they inherit the same rights through two others. Access granted through a break-glass account has no owner to notify. You end up with orphaned entitlements that no automated process will ever clean up because no automated process knows they are there.

## Doing It Right

Start by making the identity provider the source of truth, per Safeguard 6.7. If access can be granted outside your SSO/IdP, you cannot review it and you cannot revoke it. Federate everything that speaks SAML or OIDC. For the systems that do not, put them behind SCIM provisioning or, at minimum, a documented provisioning pipeline that flows through the IdP. The goal is a single point where deprovisioning actually deprovisions.

Then attack standing privilege directly. The single highest-leverage change is moving from persistent grants to just-in-time access. Human access to production should be requested, time-boxed, and expired automatically. This is what PAM tooling and cloud-native mechanisms like AWS IAM Identity Center permission sets with session policies, or Azure PIM eligible assignments, exist to do. An entitlement that expires in eight hours does not need an annual review. It reviews itself.

For what cannot be made ephemeral, scope it. Replace wildcard IAM policies with explicit actions and resource ARNs, and use conditions (`aws:SourceIp`, `aws:PrincipalTag`) to constrain further. Replace `cluster-admin` bindings with `Roles` scoped to a namespace and the specific `verbs` the workload needs. Read your cloud provider's access analyzer output, which tells you which granted permissions were never used, and delete them.

Treat service accounts as first-class review targets. Every non-human identity needs a named human owner, a documented purpose, an expiry or rotation schedule, and a place in the same review cycle as humans. Prefer short-lived, workload-identity-federated credentials (OIDC-based, IRSA, workload identity) over long-lived static keys so there is nothing to leak and nothing to review.

Finally, fix the review so it can say no. Do not certify entitlement codes; certify against a defined role model, so the reviewer's question is "should this person be a Developer" instead of "what is `APP_FIN_RW_PROD`." Feed the review with usage data: an entitlement not exercised in 90 days is a revocation candidate by default, and the burden is on the owner to justify keeping it. Make revocation the cheap path and retention the one that requires effort. Track your revocation rate as the actual metric. A review cycle that revokes nothing is broken by definition, regardless of how many boxes got ticked.

## The Bottom Line

Least privilege is not a policy problem. It is a garbage-collection problem, and you have never once run the collector. The document that says "users shall have minimum necessary access" is true the moment it is written and false by the end of the week, because access is granted continuously and reclaimed approximately never. The organizations that get breached through over-permissioned accounts are not the ones without a policy. They all have a policy. They are the ones whose access review approved everything, forever, because saying no was harder than saying yes. Close the loop or stop pretending you have one.

*Access granted is access forever, unless you go take it back. You won't.*