---
layout: field_note
title: "Field Note — August 26, 2026"
date: 2026-08-26
summary: "CISA confirms active exploitation of a critical Gitea RCE (CVE-2026-60004) as attackers drop miner payloads, and a new SLEEPWALKER Windows backdoor waits silently for a single crafted packet before executing."
---

## Today's Field Note
CISA added Gitea's CVE-2026-60004 (CVSS 9.8) to the exploited-vulnerabilities pile, and it is being hit in the wild. The catch that should worry you: it only takes ordinary write access to a repo to land shell commands as the Gitea user, so a single low-privilege contributor account or a stale bot token is your entry point. Patched in 1.27.1 back in late July, which means the window to patch quietly has closed and you are now racing the miners. Separately, an independent researcher documented SLEEPWALKER, an unsigned 64-bit DLL side-loaded and left inert in memory until a specific crafted packet wakes it, then it runs its own 23-instruction bytecode. Passive backdoors that never beacon do not show up in your egress logs, so do not expect the usual C2 noise to save you.

## Today's Action
- Upgrade Gitea to 1.27.1 or later now. If you cannot, restrict repo write access and rotate any bot or CI tokens.
- Audit Gitea accounts with write access and kill stale, service, or over-permissioned users.
- Check Gitea and adjacent hosts for unexpected miner processes, cron entries, and outbound pool connections.
- Hunt for unsigned side-loaded DLLs in odd application directories and inventory inbound packets to hosts that should not be listening (SLEEPWALKER wakes on a single crafted packet, not on beaconing).
- Add CVE-2026-60004 to your patch SLA tracker and confirm exposure of any internet-facing Gitea instances.

## Resources

Verified links for the CVEs mentioned above: official advisories, and a live search for public detection rules if any exist yet.

- **CVE-2026-60004**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-60004) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-60004)

*Passive backdoors don't call home. Go find them.*

## Related

- [OpenAI's Own Models Broke Out of Their Sandbox and Hacked Hugging Face](/itsalreadywhen/2026/07/26/issue-006/)
- [An AI Test Model Broke Into Hugging Face and Nobody Noticed for a Weekend](/itsalreadywhen/2026/08/02/issue-007/)
- [The Week AI Agents Started Breaking Into Real Companies](/itsalreadywhen/2026/08/09/issue-008/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*