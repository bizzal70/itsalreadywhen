---
layout: field_note
title: "Field Note — July 11, 2026"
date: 2026-07-11
summary: "Progress tells ShareFile admins to power off Storage Zone Controllers over a credible threat, Gitea's Docker auth bypass is under active exploitation, and a compromised Injective Labs npm package is stealing wallet keys."
---

## Today's Field Note

Three things need your hands today, not your calendar. Progress Software is telling ShareFile customers to physically shut down Windows Storage Zone Controllers over a "credible external security threat," which is the kind of language a vendor only uses when they have already seen it in the wild. Separately, attackers are actively exploiting a critical auth bypass in the official Gitea Docker image that lets anyone impersonate any account, admins included, so your self-hosted Git is a full-takeover target right now. And @injectivelabs/sdk-ts@1.20.21 shipped from a compromised GitHub repo with telemetry that quietly exfiltrates crypto wallet keys and seed phrases. Two of these are supply-chain and one is a vendor waving a red flag. All three are already downstream of "patch when convenient."

## Today's Action

- ShareFile: power off on-prem Storage Zone Controllers now per Progress guidance, then hunt for anomalous access before you bring anything back online.
- Gitea: if you run the official Docker image, patch to the fixed release immediately and audit admin accounts and recent logins for impersonation.
- npm: pin away from @injectivelabs/sdk-ts@1.20.21, purge it from lockfiles and CI caches, and rotate any wallet keys or seed phrases touched by affected builds.
- Grep build logs and package manifests across repos for the malicious Injective version; a lockfile is not the same as your runtime.
- Treat any dev machine that pulled that package as compromised for credential theft, not just crypto.

*It was never "when." It was already.*