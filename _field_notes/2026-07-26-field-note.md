---
layout: field_note
title: "Field Note — July 26, 2026"
date: 2026-07-26
summary: "The SourTrade malvertising campaign has browsers assemble malware in memory to dodge URL-based detection, while ClickFix cryptominer lures hit Steam forums."
---

## Today's Field Note
Two campaigns worth your morning. Confiant detailed SourTrade on July 23: a malvertising operation running since late 2024 that impersonates TradingView, Solana, and Luno to hit retail traders. The novelty is delivery. Instead of serving one complete payload from a fixed URL, the browser fetches fragments and assembles the final Windows executable in memory, using the legitimate Bun runtime as a base. That defeats static URL blocklists and single-file signature detection, which is the whole point. Separately, ClickFix lures are back on Steam discussion forums, posing as fixes for game problems and dropping XMRig cryptominers via the usual paste-this-into-Run social engineering. Neither is exotic, but both route around network-layer controls and lean on user execution, so your endpoint and behavior telemetry are doing the real work here.

## Today's Action
- Alert on Bun runtime (`bun.exe`) executing from user-writable paths or spawned by a browser process, then hunt for it in your fleet.
- Block or restrict the Windows Run dialog and `powershell.exe`/`mshta.exe` launched from clipboard-paste workflows to blunt ClickFix.
- Add Confiant's SourTrade IOCs and the impersonated domains (fake TradingView, Solana, Luno lookalikes) to blocklists, but do not rely on URL blocking alone.
- Hunt for sustained CPU spikes and outbound mining-pool connections tied to XMRig on endpoints used by gamers or BYOD.
- Remind users that no legitimate site or forum post asks them to paste commands into Run or a terminal.

*The malware stopped shipping whole. Now your browser does the assembly.*

## Related

- [OpenAI's Own Models Broke Out of Their Sandbox and Hacked Hugging Face](/itsalreadywhen/2026/07/26/issue-006/)
- [The 11-byte packet that freezes an OpenSSL server for good](/itsalreadywhen/2026/07/19/issue-005/)
- [Issue #004 — Week of July 12, 2026](/itsalreadywhen/2026/07/12/issue-004/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*