# Universal Rules

This repository defines a governance constitution for software in this ecosystem. The primary normative document is [Universal Rules for All Apps](UNIVERSL%20RULES%20FOR%20ALL%20APPS.md). Its original filename is retained for continuity.

**Version: 1.0.0-working.1**

**Status: Pre-Ratification Working Candidate — Not Yet Ratified**

The reviewed `1.0.0-rc1` at `d9fc392ceddad5f760e0d4a71070bbc723609f77` received **RATIFY WITH NON-BLOCKING ISSUES**, with no blockers and four clarifications. This expanded working candidate integrates those clarifications and subsequent owner policy decisions. The prior verdict does not verify the new revision. No new attack, final release-candidate freeze, or ratification is part of this pass. A new attack must wait until the owner explicitly confirms **“There is nothing else left to add.”** No governed application has been inspected or certified by this integration.

## How to read the constitution

Universal invariants describe defensible engineering outcomes such as truthful operation results and enforced authority. Ecosystem policies are deliberate choices: they need not be laws of computer science. Defaults, conditional requirements, recommendations, and prohibitions have distinct strengths and applicability. Every candidate rule has a stable ID, provenance, and applicability; all inherit CANDIDATE status.

The principal ecosystem choices are:

- **Rust-first:** Rust is presumptive for new software. Non-Rust components need a concrete technical justification and scoped policy approval. Rust is not proof of correctness. See [LANG-1](UNIVERSL%20RULES%20FOR%20ALL%20APPS.md#lang-1) and [ADR-0001](decisions/ADR-0001-rust-first.md).
- **Feature-first:** Applications with multiple meaningful capabilities organize around deliberate responsibility and state ownership. No universal folder ceremony is required. A modular monolith is the ordinary default, with justified process/service boundaries permitted. See [architecture](UNIVERSL%20RULES%20FOR%20ALL%20APPS.md#s06).
- **NAS support:** Applicable applications support declared, tested modes needed for their workflow. Hosting, service clients, ordinary shared files, raw transactional database access, and backup destinations are different modes. Docker or backups alone do not establish every mode. See [NAS-1](UNIVERSL%20RULES%20FOR%20ALL%20APPS.md#nas-1).
- **Local operation and data portability:** Preserve useful local capabilities and practicable exits for retained data while representing genuine remote dependencies honestly.
- **Product Platform Scope:** Declare Desktop, Mobile, Universal Device Application, and/or Web scope. First-class tested Desktop Linux baselines are Arch Linux, CachyOS, Ubuntu LTS, and Linux Mint (current stable Ubuntu-based release), with equal applicable support and validation expectations. Ubuntu or Mint testing does not establish support for other distributions; other mainstream distributions remain best-effort unless explicitly promoted. Browser support is distinct from native support. See [PORT-3](UNIVERSL%20RULES%20FOR%20ALL%20APPS.md#port-3).
- **One shared Rust core:** Product clients share domain and durable behavior where technically practical. Platform-appropriate UIs are preferred when resources allow; shared cross-platform UI is also a first-class option. Adapt presentation to desktop, phone, and tablet. See [CORE-1](UNIVERSL%20RULES%20FOR%20ALL%20APPS.md#core-1) and [UI strategy](UNIVERSL%20RULES%20FOR%20ALL%20APPS.md#ui-1).
- **Device continuity:** Preserve ordinary local operation without a permanent server. Applicable products support local-first device synchronization, an opt-in NAS hub, and safe topology transitions. See [synchronization](UNIVERSL%20RULES%20FOR%20ALL%20APPS.md#s20).
- **Visual assets:** Prefer genuine SVG source artwork for naturally vector assets; retain raster content where appropriate, permit generated platform icons, respect official brand assets, and enforce SVG trust boundaries. See [ASSET-1](UNIVERSL%20RULES%20FOR%20ALL%20APPS.md#asset-1).
- **Hermes:** Optional bounded local intelligence and structured small-model retrieval direction are included. The **Hermes / User-Adaptable File Structure Blueprint** is **PENDING FINAL DESIGN — DO NOT INVENT OR FREEZE YET**. See [HERMES-1](UNIVERSL%20RULES%20FOR%20ALL%20APPS.md#hermes-1) and the [pending plan](UNIVERSL%20RULES%20FOR%20ALL%20APPS.md#s30).

## Decisions and exceptions

The owner/user is the ultimate authority unless explicitly delegated. Formal policy exceptions record the rule, scope, technical reason, risks, mitigations, duration or review trigger, and approving authority with evidence. Expiry or material changes to assumptions, rationale, or scope trigger reconsideration; exceptions may be renewed, replaced, superseded, or withdrawn without arbitrary periodic bureaucracy. Ordinary default alternatives need a proportionate rationale; recommendations need no exception. Read [GOV-3](UNIVERSL%20RULES%20FOR%20ALL%20APPS.md#gov-3) before treating a difference as a policy violation.

ADRs in [decisions/](decisions/) preserve significant decisions and rationale. The constitution remains primary; supporting documents cannot silently add stronger rules.

## Review and change process

1. Identify the current base commit, affected rules, and applicable user decisions.
2. Make proposed changes on a reviewable branch and preserve historical evidence.
3. Record findings and their disposition, validate links and normative consistency, and distinguish documentation validation from runtime evidence.
4. Receive and integrate the owner-supplied Hermes blueprint and any further policies. Keep the working candidate open until the owner explicitly says **“There is nothing else left to add.”**
5. Only after that confirmation, freeze the final candidate and conduct its final adversarial review. Ratification requires a separate owner decision. Do not infer authority to inspect, migrate, or enforce rules in other repositories, merge into `main`, or tag `1.0.0`.

Rule anchors are preferred over old section numbers. Historical review section references refer to the recorded original commit, not this renumbered candidate.

## Repository records

- [Constitution](UNIVERSL%20RULES%20FOR%20ALL%20APPS.md): candidate normative source.
- [Changelog](CHANGELOG.md): known history and integration changes.
- [Rust-first ADR](decisions/ADR-0001-rust-first.md): decision rationale and exceptions.
- [Pre-ratification adversarial review](reviews/2026-10-astra-adversarial-review.md): preserved historical report.
- [Integration disposition and validation](reviews/2026-10-rc1-integration-disposition.md): finding-by-finding outcomes, coverage, and checks.
- [RC1 verification outcome](reviews/2026-10-rc1-verification-outcome.md): historical verdict, reviewed revision, and four non-blocking clarifications.
- [Pre-attack integration report](reviews/2026-10-pre-attack-integration.md): current policy coverage, direct conflicts resolved, validation, and remaining work.
- [Initial-generation provenance](provenance/initial-generation-boundary.md): original drafting attestation, retained as historical claims rather than current rules.

This is a documentation repository; it defines no application build or runtime test suite. Documentation checks do not certify future implementations, supported NAS configurations, or the truth of every possible guarantee. The remaining design and gated review sequence are explicit in [section 30](UNIVERSL%20RULES%20FOR%20ALL%20APPS.md#s30).
