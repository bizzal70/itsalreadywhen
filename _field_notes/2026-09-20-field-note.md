---
layout: field_note
title: "Field Note — September 20, 2026"
date: 2026-09-20
summary: "Researchers chained flaws to take over OpenAI staff accounts, while the BragJack PoC hijacks AI browser agents through a single malicious extension."
---

## Today's Field Note
Two items today, both pointing at the same soft underbelly: the AI tooling we bolted on faster than we secured. Hacktron researchers chained a bug in OpenAI's public help forum software with a weakness in OpenAI's login system to take over ChatGPT and Codex accounts of OpenAI employees, then reached an internal code repository. Separately, Gal Weizman's BragJack PoC uses one malicious extension and a "Prompt Forcing" technique to hijack AI assistants in Chrome, Edge, Opera Neon, Perplexity Comet, and Claude in Chrome (two CVEs, over $20,000 in bounties). Neither is a nation-state campaign, but both are working chains against production systems, and browser-agent hijacking is exactly the kind of thing that gets weaponized once the PoC is public. The pattern is the reminder: your identity plane and your browser extensions are attack surface, AI or not.

## Today's Action
- Inventory AI browser agents in use (Comet, Neon, Claude in Chrome, Copilot/Edge) and confirm patch status against the two BragJack CVEs.
- Lock down extension installs via enterprise policy: allowlist only, block sideloading, review currently installed extensions for anything unvetted.
- Audit federated login and OAuth flows for your SaaS estate, particularly account-linking between a public-facing property and an internal identity system.
- Treat any account that can reach a code repository as tier-zero: enforce phishing-resistant MFA and review recent access logs.
- Warn users that AI assistants can be steered by page content and extensions; they should not paste secrets into browser agents.

*The robots are helpful. So are the people breaking into your repo.*

## Related

- [Least Privilege, Actually Enforced](/itsalreadywhen/rtfm/2026/07/01/least-privilege-actually-enforced/)
- [Issue #004 — Week of July 12, 2026](/itsalreadywhen/2026/07/12/issue-004/)
- [AI Agents Left 18,000 Posts on a Dead German Wiki to Coordinate Their Escape](/itsalreadywhen/2026/09/06/issue-012/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*