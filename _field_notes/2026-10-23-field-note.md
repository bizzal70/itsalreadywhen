---
layout: field_note
title: "Field Note — October 23, 2026"
date: 2026-10-23
summary: "Arista's VeloCloud Orchestrator is under active exploitation via a critical SQL injection zero-day (the third in four months), China's Storm-0940 is using an AI pentest tool to hit ConnectWise tenants at scale, and the LiteLLM release pipeline was hijacked to push credential-stealing packages."
---

## Today's Field Note
Three live fires worth your attention. Arista disclosed a critical SQL injection zero-day in VeloCloud Orchestrator, exploited in the wild, that lets any authenticated user (down to a read-only customer account) escalate to operator, the top tier of control. This is the third VeloCloud Orchestrator zero-day in four months, which tells you something about where attention is going and where patch hygiene is lagging. Meanwhile Microsoft tied China's Storm-0940 to the ConnectWise supply chain compromise, where an AI-enabled pentest tool called Artex automated the attack across more than 2,200 tenants, and the LiteLLM release pipeline was hijacked via stolen GitHub CLI OAuth tokens to push credential-stealing packages to PyPI and Docker. The common thread: trusted management planes and build pipelines are doing the attacker's lateral movement for them.

## Today's Action
- Patch VeloCloud Orchestrator On-Prem now per Arista's October 22 advisory, then audit VCO accounts (including read-only customer logins) for unexpected operator escalation.
- If you run ConnectWise, hunt for Storm-0940 activity across all tenants, review privileged access grants, and rotate any credentials touched during the window.
- Pin and verify LiteLLM package and Docker image hashes, pull any versions from the compromised window, and rotate secrets and environment variables exposed to those builds.
- Rotate GitHub CLI OAuth tokens and audit which tokens can push or approve packages; enforce protected branches and required reviews on release pipelines.
- Check VeloCloud and ConnectWise logs for anomalous privilege changes and outbound connections, not just known IOCs.

*File this one under things you already own but haven't looked at lately.*

## Related

- [An AI Test Model Broke Into Hugging Face and Nobody Noticed for a Weekend](/itsalreadywhen/2026/08/02/issue-007/)
- [Least Privilege, Actually Enforced](/itsalreadywhen/rtfm/2026/07/01/least-privilege-actually-enforced/)
- [Change Management as a Security Control](/itsalreadywhen/rtfm/2026/10/07/change-management-as-a-security-control/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*