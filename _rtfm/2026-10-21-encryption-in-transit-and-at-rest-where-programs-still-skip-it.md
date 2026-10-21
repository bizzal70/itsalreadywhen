---
layout: rtfm
title: "Encryption in Transit and at Rest — Where Programs Still Skip It"
date: 2026-10-21
summary: "Encryption at the edge is mostly solved, but most organizations still hand off plaintext the moment traffic crosses an internal boundary they decided to call 'trusted.'"
framework: "NIST SP 800-53 Rev. 5 — SC Family (System and Communications Protection)"
framework_url: "https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final"
---

Everyone encrypts the front door now. TLS on the public endpoint, a padlock in the browser, an A+ on the SSL test, and a slide in the architecture review that says "data encrypted in transit." Then the request crosses the load balancer and spends the rest of its life as plaintext, hopping between microservices, replicating to a standby database, and getting written to a backup volume that nobody has thought about since the migration. The uncomfortable truth is that encryption in most organizations stops precisely where someone drew a box on a diagram and labeled it "internal."

## The Standard

NIST SP 800-53 Rev. 5 does not share your optimism about trusted networks. The System and Communications Protection (SC) family is explicit, and it is not written with an "except where inconvenient" clause.

**SC-8 (Transmission Confidentiality and Integrity)** requires that the system protect the confidentiality and integrity of transmitted information. Read the control enhancements and the discussion text carefully: it does not say "transmitted over the public internet." It says transmitted, full stop. SC-8(1) specifically calls for cryptographic mechanisms to prevent unauthorized disclosure and detect changes during transmission "unless otherwise protected by physical safeguards." That physical-safeguard carve-out is doing a lot of load-bearing work in a lot of audits, and almost none of the environments citing it actually qualify. A shared cloud VPC is not a physically protected distribution system. Neither is your east-west traffic inside a Kubernetes cluster.

**SC-28 (Protection of Information at Rest)** covers the other half: confidentiality and integrity of information while it is stored. SC-28(1) names cryptographic protection explicitly, and the discussion is clear that "at rest" means databases, logs, backups, scratch space, caches, and the pile of temp files your batch job leaves behind, not just the one production volume you remembered to flag.

Backing these are **SC-12 (Cryptographic Key Establishment and Management)** and **SC-13 (Cryptographic Protection)**, which require that the cryptography actually be managed and that it use approved algorithms. Encryption with keys stored next to the ciphertext, or with a self-signed cert nobody validates, technically satisfies a checkbox and satisfies nothing else.

The framework's position, in plain language: encrypt it in motion, encrypt it at rest, manage the keys like they matter, and stop pretending the network perimeter is a cryptographic boundary. It never was.

## Where It Breaks Down

The failures are predictable and they cluster in the same places every time.

**TLS termination at the edge, plaintext behind it.** The load balancer or reverse proxy terminates TLS and forwards cleartext HTTP to the backend pool. This is the single most common gap. The justification is always latency or operational simplicity, and the result is that anyone with a tap on the internal segment, a compromised sidecar, or a misrouted mirror session reads everything. In cloud environments this plaintext hop crosses availability zones and sometimes physical data centers on infrastructure you do not control.

**Service-to-service calls over bare HTTP.** Internal APIs, gRPC between microservices, message queue traffic, and health-check endpoints routinely run unencrypted because "they're on the same VPC." Service meshes are deployed and then mTLS is left in permissive mode indefinitely, which means encryption is optional and the services happily accept plaintext. Permissive mode is a migration state, not a destination, and it has a way of becoming permanent.

**Database connections in the clear.** The application connects to PostgreSQL, MySQL, MongoDB, or Redis without TLS, or with `sslmode=prefer` instead of `require` or `verify-full`, which means it will silently fall back to plaintext and accept any certificate. Replication streams between primary and replica are frequently unencrypted entirely. Your most sensitive data moves across the network in the one protocol nobody inspects.

**"Encrypted at rest" that means one thing and not the others.** The production database has transparent data encryption enabled, so the box is checked. Meanwhile the nightly backups land on an object store bucket or an NFS share with no encryption, the write-ahead logs and binlogs are plaintext, the application logs full of PII sit on an unencrypted volume, and the analytics pipeline copied everything into a data lake that nobody configured. At-rest encryption gets applied to the asset you were thinking about and nothing downstream of it.

**Keys that defeat the purpose.** Full-disk or volume encryption where the key is automatically provided at boot by the same platform that stores the disk protects you against exactly one threat: someone physically stealing a drive. It does nothing against a compromised host, a cloud account takeover, or an over-permissioned IAM role, which are the threats you actually face. If the attacker who can read the data can also read the key, you have encrypted nothing.

**Internal CA and cert management that nobody wants to touch.** Encryption of internal traffic requires certificates, which requires a certificate authority, rotation, and validation. Because this is annoying, teams disable certificate verification (`InsecureSkipVerify: true`, `rejectUnauthorized: false`, `curl -k` baked into a script), which gives them the TLS handshake and none of the authentication, leaving them wide open to anyone who can get in the path.

## Doing It Right

None of this is novel. It is just work that keeps getting deferred.

**Encrypt east-west traffic, not just north-south.** If you run a service mesh (Istio, Linkerd, Consul), enable mTLS in STRICT mode and enforce it with a policy that rejects plaintext, then verify it with a packet capture rather than trusting the dashboard. If you do not run a mesh, terminate TLS at the service, not only at the edge, or re-originate TLS from the proxy to the backend. "Last mile" plaintext is still plaintext.

**Require TLS on every datastore connection, and validate the certificate.** Set PostgreSQL to `sslmode=verify-full`, MySQL to `REQUIRE SSL` with CA verification, and enable TLS on Redis, MongoDB, Kafka, and your message brokers. Encrypt replication traffic explicitly; it is a separate setting and it is almost always off by default. Treat any client flag that disables verification as a production-blocking defect, not a convenience.

**Separate the encryption from the key custody.** Use a KMS or an HSM-backed key service so the key is not retrievable by the same identity that reads the data. Scope key-usage permissions tightly with IAM, enable automatic rotation, and audit key-access logs. The goal is that compromising the storage layer does not hand over the keys. Envelope encryption with per-dataset data keys wrapped by a KMS master key is the baseline pattern, not an advanced one.

**Make "at rest" mean the whole data lifecycle.** Inventory every place the data lands: primary store, replicas, backups, snapshots, WAL/binlogs, caches, temp files, log aggregation, and downstream analytics. Encrypt each of them, and specifically verify backups, because the backup is the copy an attacker most wants and the one least likely to be protected.

**Enforce with policy, not intentions.** Use admission controllers, OPA/Gatekeeper policies, Terraform `deny` rules, or cloud config rules to reject unencrypted volumes, buckets, and plaintext listeners at provisioning time. A control that depends on an engineer remembering is not a control. Run continuous checks that flag any port speaking cleartext internally and any datastore accepting an unverified connection.

## The Bottom Line

The encryption gap on internal traffic survives not because it is hard but because it is invisible. It never shows up in the browser, never fails the external scan, and never generates a complaint until the day someone is already inside and quietly reading the wire you decided to trust. SC-8 and SC-28 have been telling you this for years, in plain language, and the carve-out you have been leaning on almost certainly does not apply to your cloud. The perimeter you encrypted is not where the breach happens. The soft, plaintext interior you labeled "trusted" is.

*Draw the box wherever you like. The attacker does not respect your diagram.*

## Related

- [Change Management as a Security Control](/itsalreadywhen/rtfm/2026/10/07/change-management-as-a-security-control/)
- [Backup Integrity vs. Backup Existence](/itsalreadywhen/rtfm/2026/08/12/backup-integrity-vs-backup-existence/)
- [Segmentation as an Assumption, Not a Diagram](/itsalreadywhen/rtfm/2026/07/29/segmentation-as-an-assumption-not-a-diagram/)

More: [Issues](/itsalreadywhen/) · [Field Notes](/itsalreadywhen/field-notes/) · [RTFM](/itsalreadywhen/rtfm/)
