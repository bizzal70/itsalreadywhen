---
layout: rtfm
title: "Data Classification Before Data Protection"
date: 2026-10-14
summary: "You cannot apply the right controls to data you have never bothered to label, which is why data classification remains the unglamorous prerequisite that every protection program skips and every incident response team pays for later."
framework: "NIST Cybersecurity Framework — Identify (ID.AM)"
framework_url: "https://www.nist.gov/cyberframework"
---

Everyone agrees data classification matters. They agree the way people agree that they should floss, or read the license agreement, or rotate the backups they have never once tested. It is the single most deferred activity in security, because it produces no demo, generates no dashboard worth screenshotting, and cannot be purchased as a box with blinking lights. And so organizations skip straight to protection, buying DLP and encryption and access controls they then point at a data estate nobody has bothered to understand, and act surprised when it accomplishes nothing.

## The Standard

The NIST Cybersecurity Framework puts this in the Identify function, under the Asset Management category (ID.AM). The framework is blunt about sequencing: you identify before you protect. ID.AM-05, in the current framework language, requires that assets be prioritized based on classification, criticality, and business value. The older subcategory numbering phrased it as data and software being "classified based on sensitivity," but the intent has never changed. You are expected to know what data you hold, where it lives, who owns it, and how much it matters, and you are expected to encode that knowledge in a way machines and humans can both act on.

This is not a NIST invention. ISO/IEC 27001 Annex A has carried an information classification control for years. NIST SP 800-60 exists solely to map information types to impact levels. The entire apparatus of FIPS 199, with its low/moderate/high impact ratings across confidentiality, integrity, and availability, assumes you have already sorted your data into categories before you decide how hard to defend each one.

The logic is simple and the framework does not pretend otherwise. Controls cost money and friction. You cannot afford to apply your strongest controls to everything, and if you try, users will route around them. Classification is the function that lets you spend your control budget where it matters: a test fixture of synthetic records and a production table of unredacted personal data are not the same risk, and treating them identically means you are either overspending on the first or underspending on the second. Usually both.

## Where It Breaks Down

The failure is rarely a missing policy document. The failure is that the policy document exists, defines four tidy tiers (Public, Internal, Confidential, Restricted, pick your synonyms), and then nothing downstream ever reads it.

The first break is that classification is treated as a human labeling exercise at document creation time, and humans do not label. If your scheme depends on an analyst selecting "Confidential" from a dropdown in an Office sensitivity-label plugin every time they save a file, your actual classification coverage will asymptotically approach zero. People default to whatever requires no decision. Worse, they over-classify to cover themselves, so everything becomes "Restricted," the label stops carrying information, and your DLP policies either block everything or get disabled by week two.

The second break is scope. Classification programs get written for documents (the Word files, the PDFs, the SharePoint libraries) because that is where the GUI tooling lives. Meanwhile the sensitive data that actually gets exfiltrated is in structured stores: Postgres and MySQL tables, S3 buckets, DynamoDB, Parquet files in a data lake, Kafka topics, message queues, and the forty Snowflake schemas nobody has looked at since the migration. None of that has a sensitivity dropdown. A classification scheme that only knows how to label files is blind to most of your crown jewels.

The third break is drift and copies. You classify the golden source correctly, and then an ETL job dumps it into a reporting database with no labels, a developer pulls a production snapshot into a staging environment to debug something, a CSV gets emailed, and an analyst joins it into a spreadsheet on a laptop. Classification is a property of data, not of a location, and the moment data moves, your carefully labeled original has spawned a dozen unlabeled children. Without propagation, your map describes a territory that no longer exists.

The fourth break is that classification is never connected to a control decision. This is the quiet killer. Organizations run a discovery scan, generate a beautiful report showing where the PII and PHI and cardholder data live, present it to the audit committee, and then file it. The classification exists as a document. It is not wired into IAM policy, not driving S3 bucket policies or object tags, not feeding the DLP engine's detection rules, not informing retention and deletion schedules, not tiering what gets encrypted with customer-managed keys versus default keys. Classification that does not change a single technical control is just expensive cartography.

The fifth break is ownership. ID.AM presumes every asset has an owner. In practice the "owner" of a data store is a service account, a defunct team, or a vendor integration whose Slack channel has been archived. Nobody can tell you what the business impact of its compromise would be, so nobody can classify it, so it sits at the default tier, which is usually the loosest one.

## Doing It Right

Start by abandoning the fantasy that users will classify manually at scale. Manual labeling has exactly one legitimate use: the small set of documents where a human genuinely knows context a scanner cannot infer. Everything else should be classified by automated discovery and inference.

Point data discovery and classification tooling (the category sometimes called DSPM, sometimes just data classification engines) at your actual stores, not just your file shares. That means database connectors, cloud storage scanning, and content inspection that runs pattern matching and, where justified, trained classifiers against real schemas and objects. Luhn-check the candidate card numbers, regex and validate the national ID formats, detect the health-record vocabularies. Sample rows, profile columns, and classify at the column and object level, not the vague "this bucket might contain something" level.

Keep the scheme small. Three or four tiers, each with a crisp, testable definition tied to impact. If you cannot write a rule that decides which tier a given column belongs in, the tier is useless. Map each tier explicitly to the FIPS 199 confidentiality/integrity/availability impact model so the classification feeds a real risk statement rather than a vibe.

Then do the part everyone skips: wire classification into enforcement. Make the label machine-readable and attach it where controls can read it. In AWS, that means object tags and resource tags that bucket policies, SCPs, and IAM conditions actually reference. In a database, that means a data catalog (think the catalog-and-lineage tooling category) that tags columns and that your access-governance layer consumes. Drive your DLP detection rules from the classification output instead of maintaining a parallel, divergent set of patterns. Make encryption key tiering, retention schedules, logging verbosity, and network egress controls all functions of the tier. The test is simple: changing a datum's classification should automatically change how it is protected. If it does not, you have a label, not a control.

Handle propagation with lineage. Catalog tools that track column-level lineage let an inherited classification follow data from source through ETL into the warehouse and the reporting layer. For unstructured sprawl, tagging that survives copy operations (sensitivity labels embedded in the file, not stored in a side database) at least gives you a fighting chance.

Finally, assign owners as a hard requirement, not an aspiration. Every data store gets a named human owner and a reviewed classification, or it gets quarantined into a restricted-by-default zone until someone claims it. Default-deny for unowned data is the only thing that scales.

## The Bottom Line

You already know you should do this. It has been in every framework for two decades, it is the literal prerequisite the standards put before the word "Protect," and you have skipped it anyway, because it is tedious and nobody gets promoted for a clean data inventory. The incident response team will eventually build your classification for you, retroactively, under deadline, while counsel asks which records were in the breached table and you realize you have no idea. Do it now on your schedule, or do it later on an attacker's. The data does not care which, but you will.

*Label it now, or let the forensics firm label it for you.*

## Related

- [Asset Inventory: You Can't Protect What You Don't Know You Have](/itsalreadywhen/rtfm/2026/09/02/asset-inventory-you-can-t-protect-what-you-don-t-know-you-have/)
- [Change Management as a Security Control](/itsalreadywhen/rtfm/2026/10/07/change-management-as-a-security-control/)
- [Third-Party and Vendor Risk Management](/itsalreadywhen/rtfm/2026/07/22/third-party-and-vendor-risk-management/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)
