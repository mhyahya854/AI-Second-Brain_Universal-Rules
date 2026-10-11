# Universal Rules

This repository defines a governance constitution for software in this ecosystem. The primary normative document is [Universal Rules for All Apps](UNIVERSL%20RULES%20FOR%20ALL%20APPS.md). Its original filename is retained for continuity.

**Version: 1.0.0-rc1**

**Status: V1.0 Ratification Candidate — Not Yet Ratified**

The candidate integrates the completed adversarial review of the original draft. It still needs a further adversarial verification and an explicit ratification decision by the repository owner/user. A commit, merge, or AI review does not itself ratify it. No governed application has been inspected or certified by this integration.

## How to read the constitution

Universal invariants describe defensible engineering outcomes such as truthful operation results and enforced authority. Ecosystem policies are deliberate choices: they need not be laws of computer science. Defaults, conditional requirements, recommendations, and prohibitions have distinct strengths and applicability. Every candidate rule has a stable ID, provenance, and applicability; all inherit CANDIDATE status.

The principal ecosystem choices are:

- **Rust-first:** Rust is presumptive for new software. Non-Rust components need a concrete technical justification and scoped policy approval. Rust is not proof of correctness. See [LANG-1](UNIVERSL%20RULES%20FOR%20ALL%20APPS.md#lang-1) and [ADR-0001](decisions/ADR-0001-rust-first.md).
- **Feature-first:** Applications with multiple meaningful capabilities organize around deliberate responsibility and state ownership. No universal folder ceremony is required. A modular monolith is the ordinary default, with justified process/service boundaries permitted. See [architecture](UNIVERSL%20RULES%20FOR%20ALL%20APPS.md#s06).
- **NAS support:** Applicable applications support declared, tested modes needed for their workflow. Hosting, service clients, ordinary shared files, raw transactional database access, and backup destinations are different modes. Docker or backups alone do not establish every mode. See [NAS-1](UNIVERSL%20RULES%20FOR%20ALL%20APPS.md#nas-1).
- **Local operation and data portability:** Preserve useful local capabilities and practicable exits for retained data while representing genuine remote dependencies honestly.

## Decisions and exceptions

The owner/user is the ultimate authority unless explicitly delegated. Formal policy exceptions record the rule, scope, technical reason, risks, mitigations, duration or review trigger, and approving authority with evidence. Ordinary default alternatives need a proportionate rationale; recommendations need no exception. Read [GOV-3](UNIVERSL%20RULES%20FOR%20ALL%20APPS.md#gov-3) before treating a difference as a policy violation.

ADRs in [decisions/](decisions/) preserve significant decisions and rationale. The constitution remains primary; supporting documents cannot silently add stronger rules.

## Review and change process

1. Identify the current base commit, affected rules, and applicable user decisions.
2. Make proposed changes on a reviewable branch and preserve historical evidence.
3. Record findings and their disposition, validate links and normative consistency, and distinguish documentation validation from runtime evidence.
4. Obtain the further review and owner ratification required for adoption. Do not infer authority to inspect, migrate, or enforce rules in other repositories.

Rule anchors are preferred over old section numbers. Historical review section references refer to the recorded original commit, not this renumbered candidate.

## Repository records

- [Constitution](UNIVERSL%20RULES%20FOR%20ALL%20APPS.md): candidate normative source.
- [Changelog](CHANGELOG.md): known history and integration changes.
- [Rust-first ADR](decisions/ADR-0001-rust-first.md): decision rationale and exceptions.
- [Pre-ratification adversarial review](reviews/2026-10-astra-adversarial-review.md): preserved historical report.
- [Integration disposition and validation](reviews/2026-10-rc1-integration-disposition.md): finding-by-finding outcomes, coverage, and checks.
- [Initial-generation provenance](provenance/initial-generation-boundary.md): original drafting attestation, retained as historical claims rather than current rules.

This is a documentation repository; it defines no application build or runtime test suite. Documentation checks do not certify future implementations, supported NAS configurations, or the truth of every possible guarantee. The remaining candidate review is explicit in [section 30](UNIVERSL%20RULES%20FOR%20ALL%20APPS.md#s30).
