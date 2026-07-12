---
layout: field_note
title: "Field Note — July 12, 2026"
date: 2026-07-12
summary: "A compromised jscrambler 8.14.0 npm release runs a Rust infostealer on install across Windows, macOS, and Linux."
---

## Today's Field Note
The jscrambler npm package shipped a poisoned 8.14.0 release on July 11 with a `preinstall` hook that drops and executes a native Rust infostealer, one binary per platform. This is not a runtime problem you can lint your way around later. Running `npm install` was enough to detonate it, which means any developer machine or CI runner that touched that version during the window is already compromised, not potentially compromised. Socket caught it six minutes after publish, which is fast, but six minutes of a popular package is still a lot of pipelines. Treat every credential that lived on an affected host as burned.

## Today's Action
- Pin and audit: grep lockfiles and CI configs for jscrambler 8.14.0, block that exact version, and force resolution back to a known-good release.
- Hunt install-time execution: search build logs and endpoint telemetry for `preinstall` activity and unexpected native binary drops around July 11.
- Rotate anything the infostealer could reach: npm tokens, cloud keys, SSH keys, and env secrets on any dev or CI host that ran the install.
- Isolate and reimage confirmed-affected runners rather than cleaning in place. Native stealers do not deserve the benefit of the doubt.
- Enforce install-time controls going forward: disable lifecycle scripts by default (`npm config set ignore-scripts true`) where your builds tolerate it.

*The exploit runs before you finish typing the version number.*