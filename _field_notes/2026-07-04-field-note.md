---
layout: field_note
title: "Field Note — July 04, 2026"
date: 2026-07-04
summary: "A local-root Linux kernel flaw (CVE-2026-46242) now has a fix and hits Android, while North Korea's npm typosquats keep bleeding developer secrets."
---

## Today's Field Note
Two things earned attention today, and both are the kind that turn into someone else's bad week. Bad Epoll (CVE-2026-46242) is a Linux kernel local privilege escalation that takes an unprivileged user to root across desktops, servers, and Android. A patch exists, which means the clock started the moment it dropped, and privilege escalation is the second half of nearly every intrusion chain you will investigate this quarter. Separately, JFrog flagged more North Korea-linked npm typosquats ("rollup-packages-polyfill-core" and "rollup-runtime-polyfill-core") cloning "rollup-plugin-polyfill-node" down to the metadata, aimed squarely at developer credentials and CI secrets. The kernel bug is your infrastructure exposure; the npm packages are your supply chain exposure. Handle both before someone chains them.

## Today's Action
- Inventory Linux and Android assets, then prioritize CVE-2026-46242 patching on multi-user hosts, build servers, and anything exposing shell access to untrusted users.
- Where you cannot patch immediately, tighten local access and watch for unexpected privilege transitions and abnormal epoll-related activity.
- Block and purge "rollup-packages-polyfill-core" and "rollup-runtime-polyfill-core" from registries, lockfiles, and developer machines; confirm you use "rollup-plugin-polyfill-node".
- Rotate any developer, npm token, and CI secrets on machines that touched the malicious packages, and review outbound connections from build agents.
- Add both malicious package names to your dependency allowlist/denylist controls so they cannot reappear in a future install.

## Resources

Verified links for the CVEs mentioned above: official advisories, and a live search for public detection rules if any exist yet.

- **CVE-2026-46242**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-46242) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-46242)

*Root is just a bug someone else patched slower than you.*