# Changelog

Dates use the available commit evidence or this conversation's integration date. Unknown earlier drafting dates and model identities are not inferred. The candidate remains unratified.

## 1.0.0-rc1 — V1.0 Ratification Candidate — 2026-10-11

Integration baseline: `c2fd9e3d8ac8c41a2ec1e336d2ec097314ef80a5` on GitHub `main`, verified before editing. Work is prepared on `constitution/v1.0.0-rc1`; this entry is not a statement of publication, merge, or ratification.

- Replaced the mixed classification model with independent status, rule type, origin, applicability, and normative strength; added stable rule anchors.
- Integrated Rust-first policy and [ADR-0001](decisions/ADR-0001-rust-first.md), with component-level technical exceptions and lifecycle considerations.
- Retained feature-first policy and modular-monolith preference while removing directory ceremony and single-process impossibility tests.
- Defined five NAS modes and corrected SQLite WAL, locking, leases, flushing, permissions, latency, and preflight claims.
- Added truthful operation outcomes, uncertainty, principals, actors, mechanisms, and delegation.
- Corrected AI authority, read risk, capability enforcement, bounded autonomy, preview binding, memory, and provider assumptions.
- Required recoverable coupling of mutation and required audit evidence; separated accountable history from permanent sensitive-payload retention.
- Corrected canonical authority, factual verification, derivation, regeneration, and backup treatment.
- Reworked external editing, offline capabilities, storage contracts, concurrency, retries, recovery, backup, import/export, and migration safety.
- Separated portability, tested support, deployment options, and runtime lifecycle; made evidence proportional to actual claims.
- Clarified owner governance, exception approval, and reviewable ratification; converted anti-patterns to a non-normative index.
- Preserved the [historical adversarial review](reviews/2026-10-astra-adversarial-review.md) and moved original generation claims to [provenance](provenance/initial-generation-boundary.md).
- Rebuilt the README and recorded [finding dispositions and validation](reviews/2026-10-rc1-integration-disposition.md).

## Adversarial review — 2026-10-11 conversation

The review returned **MATERIAL ARCHITECTURAL FLAWS**, identifying unsafe mechanisms, contradictory classifications, overbroad guarantees, privacy conflicts, and missing outcome/delegation semantics. It did not edit the original constitution or inspect governed implementations. The complete available report is preserved in [reviews/](reviews/2026-10-astra-adversarial-review.md); its wording and original section references remain historical.

## Initial draft — 2026-10-11 commit evidence

- `83754ed6893fa5ea1f59ec05cd4f88913a1b61b6` — `Initial commit`, 2026-10-11T09:14:52+03:00: initial repository/README.
- `c2fd9e3d8ac8c41a2ec1e336d2ec097314ef80a5` — `Add files via upload`, 2026-10-11T09:15:27+03:00: original exhaustive constitution present.

These timestamps establish repository history, not the original drafting session's date. No independently verified earlier drafting history is available here.
