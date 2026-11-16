---
layout: field_note
title: "Field Note — November 16, 2026"
date: 2026-11-16
summary: "NoisyTCP (11-year-old Linux kernel flaw) lets attackers remote-crash default Nginx/Apache/SSH servers, BO Team is still exploiting Log4Shell in the wild against vCenter, and the FBI flags the ARTEX AI framework tied to a ConnectWise supply-chain breach."
---

## Today's Field Note
Three things worth your attention. NoisyTCP is an 11-year-old Linux kernel bug that reaches almost every distro and lets a remote attacker crash servers running Nginx, Apache, and SSH in default configs. No RCE, but a reliable DoS against your front door is still a bad day. Meanwhile BO Team (aka Black Owl) is still landing Log4Shell in VMware vCenter and walking it all the way to a code-signing server, proving that 2021's headline CVE never actually left. And the FBI is warning that the ARTEX AI pentest framework is automating real intrusions, including a ConnectWise supply-chain breach that reached Microsoft 365 tenants. The tooling is getting faster; your patch cadence is not.

## Today's Action
- Apply the NoisyTCP kernel patches as your distros ship them, and prioritize internet-facing Nginx, Apache, and SSH hosts.
- Hunt for Log4Shell (CVE-2021-44228) in VMware vCenter and any Java-stack you assumed was patched; validate, do not trust the asset inventory.
- Treat code-signing infrastructure as crown-jewel: isolate it, rotate signing keys if BO Team IOCs match, and audit recent signing activity.
- Review ConnectWise and other RMM/supply-chain connectors into your M365 tenant; revoke stale app consents and check sign-in logs.
- Watch for ARTEX-style automated recon in your edge logs: fast, broad, scripted probing is the tell.

## Resources

Verified links for the CVEs mentioned above: official advisories, and a live search for public detection rules if any exist yet.

- **CVE-2021-44228**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2021-44228) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2021-44228)

*Old bugs don't retire. They just wait for you to forget them.*

## Related

- [Stolen Fireworks AI Key Trojanized Anthropic's Official Claude Code Extension](/itsalreadywhen/2026/11/15/issue-021/)
- [ShinyHunters Hacked Clop, Then Robbed the Ransoms Twice](/itsalreadywhen/2026/09/27/issue-015/)
- [North Korea's TraderTraitor Pulls Off a $6.43 Billion Binance Heist](/itsalreadywhen/2026/11/01/issue-019/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*