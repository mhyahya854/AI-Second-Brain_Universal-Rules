# Changelog

Dates use the available commit evidence or this conversation's integration date. Unknown earlier drafting dates and model identities are not inferred. The candidate remains unratified.

## 1.0.0-working.1 — Pre-Ratification Working Candidate — 2026-10-11

Baseline: reviewed rc1 `d9fc392ceddad5f760e0d4a71070bbc723609f77`. Working branch: `constitution/pre-ratification-working`. This is an integration pass, not a new adversarial review, frozen rc2, ratification, merge, or release.

### Raw intake and native ClamAV policy delta — 2026-10-12

Verified clean starting HEAD: `ec0d03a117bc56c97bcbb031d48851e53dc5e602`, on `constitution/pre-ratification-working`. Candidate remains `1.0.0-working.1`, unfrozen and unratified.

- Added IO-2 for the preferred logical Raw/Intake boundary, untrusted content, required promotion gates, quarantine rather than automatic source destruction, and retained originals.
- Added IO-3 for background startup validity evaluation of every Raw object, safe incremental verdict reuse, prompt new/changed-object scanning, explicit non-Boolean outcomes, receipts, signature maintenance/rescan policy, unobtrusive status, failure recovery, and deliberate sync/NAS trust.
- Added SEC-6 for a generic replaceable malware-scanning capability with ClamAV preferred where suitable, local scanning, protected process/IPC preference, justified library alternatives, no untrusted unauthenticated daemon exposure, cross-platform adapters, source provenance, and actual GPLv2/distribution verification before shipping.
- All three new rules are ECOSYSTEM POLICY / USER POLICY / CANDIDATE. Existing IO-1, HERMES-1, and DEV-7 connect the contracts without changing core mutation authority or weakening prior defense-in-depth, backup, timezone, privacy, and lifecycle requirements.
- No engine was installed, source archive evaluated, application implementation certified, or licensing compliance claimed. The [integration report](reviews/2026-10-raw-intake-clamav-integration.md) records coverage and documentation validation. No final attack, owner completion review, freeze, ratification, push, merge, tag, or release candidate was performed.

### Final policy-gap and follow-up owner integration — 2026-10-12

Verified clean starting HEAD: `cd06a629fb370b4c08684ec9470151c4d4ca88f8`, on `constitution/pre-ratification-working`. The preceding read-only owner policy-completion review identified seven lifecycle gaps; the owner authorized their integration and supplied an additional timezone/malware-protection delta during this pass. The working version remains `1.0.0-working.1`, not frozen or ratified.

- Added SEC-5 (release reconstruction/critical-dependency continuity), DEV-16 (lifetime growth and lifecycle validation), DEV-17 (bounded emergency maintenance and reconciliation), UI-3 (accessible interaction), DATA-4 (locale-independent meaning), and DATA-5 (universal timezone planning and explicit temporal semantics). All six are applicability-declared ECOSYSTEM POLICY / USER POLICY with inherited CANDIDATE status.
- Strengthened RECOVER-1 for recovery without normal startup, uncertainty-preserving repair, and safe malware recovery. Expanded SEC-1/3, IO-1, SYNC-1, BACKUP-1/2, NAS-1, and AI-1 for hostile-input boundaries, least privilege, parser isolation, compromise/suspicious-sync containment, backup separation/validation, authorized intact updates, encryption limits, and retrieved content as data rather than authority.
- Linked applicable lifecycle/security contracts through DEV-7; timezone planning is mandatory in every App Plan, even without scheduling. Timezone-free concepts remain timezone-free; no all-UTC rule, universal complex temporal schema, scanner, backup topology, SBOM, cloud build, or enterprise security system is imposed.
- Reconciled DEV-5/10/13 with DEV-17: urgent repair may temporarily precede complete planning within actual authority, with durable evidence and a post-emergency Three-Layer Conformance Gate before normal features resume. No permanent bypass or broadened AI authority.
- Preserved all 94 prior rule IDs/classifications and all historical reports/provenance/ADR files. The four-app blueprint remains integrated as candidate policy; the prior rc1 verdict is not applied to this expanded revision.
- Added the [dedicated integration report](reviews/2026-10-final-policy-gap-integration.md). No final owner completion review, adversarial attack, ratification, freeze, push, merge, tag, or release candidate was performed. One final owner policy-completion review remains before Plan Freeze.

### Four-app blueprint integration — 2026-10-11

Verified clean starting HEAD: `d52e5cb112d637e96cc6a9cc6223fd762784a0bb`. The owner supplied generalized principles from the completed comparative design analysis of Mosaic, LMS / Studies, Accounting & Money, and Read & Watch. Those applications are design provenance, not normative sources or dependencies; none of their repositories was inspected in this pass.

- Integrated the Universal Information Architecture Blueprint through INFO-1–INFO-4: storage-independent logical structure, discoverable workspace entry, durable identity independent of organization, relationships, and context-aware precise anchors.
- Added DATA-3 for originals/derivatives/annotations, EVID-1 for provenance/evidence/uncertainty, OPS-1 for scoped operation identity and recovery receipts, HERMES-3 for core resolution/ambiguity/errors, and SEC-4 for vendored/forked foundation provenance. All new rules are USER POLICY / ECOSYSTEM POLICY with CANDIDATE status.
- Reconciled LIFE-2, CORE-1, DATA-2, RETRY-1, HERMES-1/2, RECOVER-2, IO-1, and MIGRATE-2 in place, retaining crash, audit, privacy, authority, and truthful-outcome contracts. No universal filesystem, database, Markdown, content-addressing, OCR, vector-store, or trash-directory requirement was introduced.
- Extended DEV-3/6/8/10/11/12 with foundation evaluation, Evidence responsibility, research claim status, bounded tasks, distinct small-model use/development goals, and execution evidence supporting Done Phases. The Three-Layer Conformance Gate remains unchanged.
- Changed the current **Hermes / User-Adaptable File Structure Blueprint** status from pending design to **integrated as candidate policy**. Prior pending-status reports remain unchanged; history below records the earlier stages.
- Preserved all platform scopes, Arch Linux/CachyOS/Ubuntu LTS/Linux Mint baselines, Rust-first, feature-first, local-first, peer-sync, and NAS policies. Owner policy-completion review still gates candidate freeze and final attack. No attack, ratification, merge, push, or tag was performed.
- Added the [four-app blueprint integration report](reviews/2026-10-four-app-blueprint-integration.md). No specific pending universal-policy item identified by this integration. Owner policy-completion review remains required.

### Earlier development-governance integration — historical stage

Subsequent development-governance integration starts from actual HEAD `337e3b95f9685f79121b5e572a86e7f583cd1900`, which includes the Linux Mint addition after the owner's previously expected `237b643f6830d3207377a688c1a819b7c65458e5`. The working label remains `1.0.0-working.1`; Git revisions distinguish these integrations.

- Added DEV-1 through DEV-15 as intentional owner ecosystem/development-governance policy: longevity purpose, idea refinement before implementation, comparative research, strongest reasonably available planning, iterative plan review and Plan Freeze Gate, logical APP Plan/Codebase responsibilities, current Master Plan, research/decision records, machine/human-readable Project State, executable phase contracts, full-build small-model continuity, safe zero-conversation resumption, Done Phases evidence, continuous three-layer conformance, and brownfield assessment/repair before features.
- Preserved all four Linux baselines: Arch Linux, CachyOS, Ubuntu LTS, and Linux Mint (current stable Ubuntu-based release); made permissions and native/system integration explicit.
- Strengthened shared-core client coverage, UI canonical consistency, no-NAS local-first sync, and Hermes validation/privacy-aware retrieval. General application research does not broaden the pending Hermes comparison beyond its four named sources.
- Preserved the owner gate: finish Hermes comparison, integrate its blueprint, discuss remaining policies, receive explicit policy-completion confirmation, freeze the candidate, and only then conduct the final attack. No attack or ratification was performed.
- Recorded coverage, direct reconciliations, and validation in the [development-governance integration report](reviews/2026-10-development-governance-integration.md).

Earlier integration history (retained below):

- Integrated N1–N4: Rust artifact scope, exception lifecycle, qualified SQLite WAL coordination, and explicitly justified relationships between independent data dimensions.
- Initially added declared Desktop, Mobile, Universal Device Application, and Web product scopes with three Linux baselines; the subsequent Linux Mint addition below expanded the current set to Arch Linux, CachyOS, Ubuntu LTS, and Linux Mint (current stable Ubuntu-based release).
- Subsequent owner addition: promoted Linux Mint's current stable Ubuntu-based release to the same first-class tested baseline status. Clarified equal applicable packaging/installation, launch, updates, filesystem, core-feature, native-integration, and automated/manual validation expectations across all four baselines. Ubuntu/Mint testing does not prove other distributions compatible; other mainstream distributions remain best-effort unless explicitly promoted.
- Added one shared Rust core across product clients, with technical exceptions, platform-appropriate or shared UI strategies, and adaptive presentation/reuse priorities.
- Added personal device-local operation, no-NAS local-first continuity, opt-in NAS synchronization hub, and safe topology transitions while retaining authority, consistency, privacy, and recovery contracts.
- Added genuine SVG source policy, raster exceptions, generated platform icon packaging, third-party brand fidelity, and SVG trust boundaries.
- Preserved optional bounded Hermes operation and added structured small-model retrieval direction. The **Hermes / User-Adaptable File Structure Blueprint** remains **PENDING FINAL DESIGN — DO NOT INVENT OR FREEZE YET**.
- Replaced the immediate-review plan with an owner-gated integration sequence. The final attack and final candidate freeze wait for **“There is nothing else left to add.”** Ratification remains a separate decision.
- Preserved prior review files unchanged; added a [historical rc1 outcome record](reviews/2026-10-rc1-verification-outcome.md) and [current integration report](reviews/2026-10-pre-attack-integration.md).

## RC1 final adversarial verification — 2026-10-11 conversation

Reviewed revision: `d9fc392ceddad5f760e0d4a71070bbc723609f77`, branch `constitution/v1.0.0-rc1`. Verdict: **RATIFY WITH NON-BLOCKING ISSUES**. No blockers were found; four non-blocking clarifications were identified. This was a recommendation, not owner ratification. Subsequent owner policy decisions required another integration phase before ratification. The outcome is preserved [separately](reviews/2026-10-rc1-verification-outcome.md); the prior review has not been rewritten or applied to the expanded candidate.

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
