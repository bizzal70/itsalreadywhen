---
layout: rtfm
title: "Application Security Basics: Input Validation Still Matters"
date: 2026-09-09
summary: "Injection flaws have topped security lists for decades not because we lack solutions, but because developers keep treating data as code and trusting input that was never trustworthy."
framework: "OWASP Top 10"
framework_url: "https://owasp.org/www-project-top-ten/"
---

Injection has been on the OWASP Top 10 since there was an OWASP Top 10. It topped the list for over a decade, and when it finally slid down to third place in the 2021 revision, that was not a victory. It was a reshuffle. The bug did not get rarer; the field just got more crowded. The uncomfortable truth is that we have known exactly how to prevent injection since before some of your engineers were born, and we still ship it, in new code, every single day. This is not a knowledge problem. It is a discipline problem.

## The Standard

The OWASP Top 10 category A03:2021-Injection covers a family of flaws that share one root cause: untrusted data gets interpreted as part of a command or query. SQL injection is the poster child, but the category is broader. It includes NoSQL injection, OS command injection, LDAP injection, XPath and XML injection, ORM injection, expression language and OGNL injection, and (folded in during the 2021 revision) cross-site scripting, which is really just injection into an HTML or JavaScript interpreter.

The requirement is not complicated. Data from any source you do not control must never be concatenated into an interpreter's grammar. That means user input, but it also means data from upstream services, message queues, cached values, and the database itself (second-order injection is a real and underappreciated variant). The controls OWASP prescribes have been stable for years:

- Use a safe API that avoids the interpreter entirely or provides a parameterized interface. For SQL, that means prepared statements with bound parameters, not string building.
- Use positive server-side input validation (allowlisting) as defense in depth, not as the primary control.
- Escape special characters using the correct syntax for the specific interpreter when a parameterized API is genuinely unavailable.
- Use LIMIT and other query controls to reduce the blast radius of a successful injection.

Notice the hierarchy. Parameterization is the control. Validation and escaping are backup. OWASP has been consistent about this for a long time, and it is worth reading carefully, because a lot of teams get the order exactly backwards.

## Where It Breaks Down

The failures are boringly consistent across organizations, which is what makes them worth naming.

**Validation masquerading as prevention.** Teams write a regex to strip single quotes or reject the word `SELECT`, declare the endpoint "sanitized," and move on. Blocklists are a losing game. There are too many encodings, too many interpreter quirks, too many ways to say the same thing. Unicode normalization, double URL-encoding, comment injection (`SEL/**/ECT`), and case variation all defeat naive filters. Validation belongs in your stack, but if it is the only thing standing between input and your interpreter, you have already lost.

**Parameterization that isn't.** Developers reach for prepared statements, then discover that identifiers (table names, column names, `ORDER BY` targets) cannot be bound as parameters. So they concatenate those in. Dynamic sorting, dynamic column selection, and dynamic `IN` clauses are where injection lives in codebases that otherwise "use prepared statements everywhere." An ORM does not save you here either. Most ORMs expose a raw query escape hatch, and the moment someone uses `.raw()` or drops into a `whereRaw` with an interpolated string, the abstraction's protection evaporates.

**Stored procedures assumed safe.** A stored procedure is not automatically parameterized. If the procedure body builds dynamic SQL with `EXEC` or `sp_executesql` and concatenates its arguments, you have simply relocated the injection point to the database engine, where it is harder to see and often runs with elevated privileges.

**The non-SQL interpreters nobody guards.** SQL injection gets attention because everyone was taught it. Meanwhile, `os.system`, `subprocess` with `shell=True`, `Runtime.exec` with a concatenated string, and shelling out to run a report or resize an image are wide open. NoSQL document stores accept query objects, and passing user-controlled JSON straight into a query lets an attacker inject operators like `$ne`, `$gt`, or `$where`, the last of which can execute JavaScript on the server. LDAP filters built from a login form let attackers rewrite the filter logic. XPath queries over uploaded XML do the same for document stores.

**Client-side validation counted as validation.** The JavaScript that checks a field before submission is a UX feature, not a security control. Anyone with an intercepting proxy sends whatever they like straight to your endpoint. Validation that does not run server-side does not exist.

**Second-order blindness.** Data gets validated on the way in, stored, and then trusted forever after. Later, a different code path reads that stored value and concatenates it into a query, assuming it is clean because it "came from our database." The injection payload was patient. This is the failure mode that survives the security review, because the sink and the source are in different files, different services, sometimes different teams.

## Doing It Right

Make parameterization the default and the path of least resistance. If your developers have to fight the framework to write a safe query, they will lose sometimes. Wrap data access behind libraries and query builders that make string concatenation awkward. When you genuinely need dynamic identifiers, do not escape them. Validate them against an allowlist of known-good values (an explicit set of permitted column names, an enum of sort directions) and map user input to those values rather than passing it through.

Handle the interpreters you forgot about. For OS commands, avoid the shell entirely. Use the array form of process execution (`subprocess.run([...])` without `shell=True`, `ProcessBuilder` with an argument list) so the OS never parses a command string. For NoSQL, cast and type-check input before it reaches the query, and reject objects where you expect scalars. For LDAP and XPath, use the escaping functions your library provides, and prefer parameterized query interfaces where they exist.

Treat input validation as a real, layered control, and do it right. Validate on the server. Validate for type, length, format, and range using positive allowlists (an email matches an email grammar, a UUID matches a UUID, a quantity is an integer within bounds). Normalize encoding before you validate so that canonicalization tricks do not slip past you. This will not stop injection on its own, and it is not supposed to. It shrinks the attack surface and catches the malformed input that has no business reaching your logic in the first place.

Enforce least privilege at the data layer. The application's database account should not own the schema, should not have `DROP`, and often should not have `DELETE` on tables it only reads. If injection happens anyway (and you should assume it eventually will), a constrained account limits what an attacker can do with it. Same principle for the OS: the service account running your web tier should not be able to write outside its working directories.

Push detection left and keep it there. Static analysis (SAST) tools flag concatenated queries and dangerous sinks; wire them into CI and fail the build on new findings rather than letting a report rot in a dashboard. Add dynamic testing (DAST) and fuzzing against your endpoints in a staging environment. Neither catches everything, and both produce noise, but the alternative is finding out in production. A parameterized-query linter in your pre-commit hook costs almost nothing and catches the obvious mistakes before they ship.

## The Bottom Line

None of this is new. The prepared statement predates most of your infrastructure. The advice in this article was true twenty years ago and will be true twenty years from now, which is precisely the problem. Injection persists not because it is hard to prevent but because prevention requires doing the correct, slightly less convenient thing on every single query, in every service, forever, and humans under deadline do not do that reliably. Tooling helps. Defaults help more. But the flaw sits at the exact point where a developer decided that just this once, concatenation was fine.

It usually is fine. Right up until it isn't.

*Parameterize your queries. Or don't, and read about it later in Issues.*

## Related

- [Least Privilege, Actually Enforced](/itsalreadywhen/rtfm/2026/07/01/least-privilege-actually-enforced/)
- [Default Credentials and Configuration Drift](/itsalreadywhen/rtfm/2026/08/19/default-credentials-and-configuration-drift/)
- [Asset Inventory: You Can't Protect What You Don't Know You Have](/itsalreadywhen/rtfm/2026/09/02/asset-inventory-you-can-t-protect-what-you-don-t-know-you-have/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)
