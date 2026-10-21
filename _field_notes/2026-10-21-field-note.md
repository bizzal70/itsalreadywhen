---
layout: field_note
title: "Field Note — October 21, 2026"
date: 2026-10-21
summary: "PHP2Shell (CVE-2026-109618/109619) details leaked ahead of patch, a FortiSIEM RCE PoC is public, and Qilin/INC are actively exploiting Palo Alto CVE-2026-0257 to bypass MFA."
---

## Today's Field Note
Three things worth your morning. PHP shipped an out-of-cycle fix for two unauthenticated RCE bugs (CVE-2026-109618 and CVE-2026-109619, CVSS 9.2) after the details leaked early, so the window between disclosure and mass scanning is effectively closed. Separately, a public PoC now exists for the FortiSIEM path traversal (CVE-2026-106173, CVSS 9.4), meaning unauthenticated code execution against your logging stack is in reach of anyone. And Palo Alto confirms Qilin and INC ransomware crews are still exploiting CVE-2026-0257 to stand up rogue VPN connections and skip MFA, a bug patched back in May that plenty of shops never closed. None of these are theoretical. The PHP flaw hits anything running the stack, and the Fortinet and PAN-OS issues sit on exactly the boxes attackers love.

## Today's Action
- Patch PHP to the out-of-cycle release immediately on all internet-facing hosts; audit for unexpected processes spawned by php-fpm or webserver accounts.
- Apply the FortiSIEM fix for CVE-2026-106173 now, and restrict management interface access to trusted networks until confirmed patched.
- Verify PAN-OS and Prisma Access are patched for CVE-2026-0257, then review GlobalProtect logs for unauthorized or newly created VPN sessions.
- Check for forged certificates tied to the eight revoked eMudhra intermediate CA keys and push browser/OS updates that block them.
- If you run UpdraftPlus/UpdraftCentral, rotate connection keys and scan connected WordPress sites for planted backdoors.

## Resources

Verified links for the CVEs mentioned above: official advisories, and a live search for public detection rules if any exist yet.

- **CVE-2026-0257**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-0257) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-0257)
- **CVE-2026-106173**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-106173) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-106173)
- **CVE-2026-109618**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-109618) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-109618)
- **CVE-2026-109619**: [NVD advisory](https://nvd.nist.gov/vuln/detail/CVE-2026-109619) · [Search Sigma for detection rules](https://github.com/SigmaHQ/sigma/search?q=CVE-2026-109619)

*The patch was ready. You just hadn't applied May's yet.*

## Related

- [OpenAI's Own Models Broke Out of Their Sandbox and Hacked Hugging Face](/itsalreadywhen/2026/07/26/issue-006/)
- [ShinyHunters Hacked Clop, Then Robbed the Ransoms Twice](/itsalreadywhen/2026/09/27/issue-015/)
- [AI Agents Left 18,000 Posts on a Dead German Wiki to Coordinate Their Escape](/itsalreadywhen/2026/09/06/issue-012/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)


---

*Daily field notes, weekly Issues. Follow [@itsalreadywhen](https://x.com/itsalreadywhen) or subscribe via RSS.*