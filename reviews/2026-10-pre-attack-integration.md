# Pre-attack integration — 1.0.0-working.1

- Status: **Pre-Ratification Working Candidate — Not Yet Ratified**
- Baseline: `1.0.0-rc1`, `d9fc392ceddad5f760e0d4a71070bbc723609f77`
- Working branch: `constitution/pre-ratification-working`
- Authority: owner's pre-attack integration instructions in this conversation
- Scope: this governance repository only; integration and document validation, not an adversarial attack

## Integrated policy coverage

All links below refer to the primary constitution; this report adds no requirements.

| Owner requirement | Integrated location and disposition |
|---|---|
| Preserve successful rc1 corrections | Existing rule IDs and classifications retained; new policies extend their authority, storage, consistency, privacy, recovery, and exception contracts. |
| Product Platform Scope | [PORT-3](../UNIVERSL%20RULES%20FOR%20ALL%20APPS.md#port-3): Desktop, Mobile, Universal Device Application, Web; Arch Linux, CachyOS, Ubuntu LTS first-class Linux baselines; adaptive mobile/tablet scope; declared versions and honest support evidence. |
| One shared Rust core | [CORE-1](../UNIVERSL%20RULES%20FOR%20ALL%20APPS.md#core-1): all listed domain, canonical-state, model, validation, sync, conflict, migration, authorization, AI-enforcement, and durable behavior responsibilities; documented technical exceptions. |
| Two UI strategies | [UI-1](../UNIVERSL%20RULES%20FOR%20ALL%20APPS.md#ui-1): platform-appropriate UIs preferred when resources allow; shared cross-platform UI is a first-class alternative; Rust language exceptions remain scoped. |
| Code reuse priority | [UI-2](../UNIVERSL%20RULES%20FOR%20ALL%20APPS.md#ui-2): shared core, beneficial UI reuse, materially appropriate platform experience, adaptive presentation rather than identical layouts. |
| Local-first device operation | [OFFLINE-3](../UNIVERSL%20RULES%20FOR%20ALL%20APPS.md#offline-3): applicable personal capabilities remain local without a permanent NAS/cloud/Internet dependency; appropriate working copies and truthful remote limitations. |
| Device sync without NAS | [SYNC-2](../UNIVERSL%20RULES%20FOR%20ALL%20APPS.md#sync-2): direct or explicitly selected local-first continuity without mandatory permanent central cloud. |
| Device sync with NAS | [SYNC-3](../UNIVERSL%20RULES%20FOR%20ALL%20APPS.md#sync-3): suitable, user-enabled NAS as primary shared hub; applicable retained/shared data, local working copies, reconnection, declared consistency. |
| Distinct NAS roles | [NAS-1](../UNIVERSL%20RULES%20FOR%20ALL%20APPS.md#nas-1): hub topology, storage service, backup destination, hosting distinguished while preserving all five access/deployment modes. |
| Safe topology transition | [SYNC-4](../UNIVERSL%20RULES%20FOR%20ALL%20APPS.md#sync-4): non-destructive NAS addition, local access during loss/removal, deliberate data transfer, explicit authority reconciliation. |
| Vector source assets | [ASSET-1](../UNIVERSL%20RULES%20FOR%20ALL%20APPS.md#asset-1): genuine SVG geometry for naturally vector assets, including reconstruction from raster references; raster wrappers do not qualify. |
| Raster exceptions and packaging | [ASSET-1](../UNIVERSL%20RULES%20FOR%20ALL%20APPS.md#asset-1): intrinsically raster content retained appropriately; generated platform raster icons/containers allowed with preferred vector source. |
| Third-party brand assets | [ASSET-2](../UNIVERSL%20RULES%20FOR%20ALL%20APPS.md#asset-2): official permitted assets and applicable brand requirements; no inaccurate screenshot redraws. |
| SVG security | [ASSET-3](../UNIVERSL%20RULES%20FOR%20ALL%20APPS.md#asset-3): external content trust boundaries and script/resource/embedded-content handling; owned assets avoid unnecessary executable/external content. |
| Hermes safety | [HERMES-1](../UNIVERSL%20RULES%20FOR%20ALL%20APPS.md#hermes-1): optional layer, core independent, bounded validated writes, local availability, no sole opaque AI data store. |
| Small-model retrieval direction | [HERMES-2](../UNIVERSL%20RULES%20FOR%20ALL%20APPS.md#hermes-2): approximate 1B-model design target, deterministic scoped discovery, rebuildable indexes where appropriate, user-adaptable organization; detailed blueprint not invented. |
| Working version and review gate | [GOV-4](../UNIVERSL%20RULES%20FOR%20ALL%20APPS.md#gov-4) and [section 30](../UNIVERSL%20RULES%20FOR%20ALL%20APPS.md#s30): no frozen rc2 or attack until explicit owner policy-completion confirmation; separate ratification decision. |
| Preserve historical verification | [RC1 outcome record](2026-10-rc1-verification-outcome.md), unchanged earlier review files, and changelog distinguish reviewed rc1 from subsequent integration. |

## Existing RC1 clarifications

| ID | Disposition |
|---|---|
| N1 | Integrated in [LANG-1](../UNIVERSL%20RULES%20FOR%20ALL%20APPS.md#lang-1) and ADR-0001: authored components versus dependencies/artifact roles; component/standing exceptions; no per-generated-file exception ceremony. |
| N2 | Integrated in [GOV-3](../UNIVERSL%20RULES%20FOR%20ALL%20APPS.md#gov-3), README, and ADR-0001: expiry/material-change triggers, renewal/replacement/supersession/withdrawal, no silent renewal or arbitrary periodic bureaucracy. |
| N3 | Integrated in [NAS-2](../UNIVERSL%20RULES%20FOR%20ALL%20APPS.md#nas-2): ordinary multi-process shared coordination wording; no all-WAL claim; Mode 4 remains supported-configuration/evidence based. |
| N4 | Integrated in [DATA-1](../UNIVERSL%20RULES%20FOR%20ALL%20APPS.md#data-1): no automatic equivalence/inference without an explicit justified rule; valid dimension relationships allowed. |

## Direct integration conflicts resolved

| Tension | Resolution |
|---|---|
| PORT-1 and old section 30 rejected one global platform matrix | Scoped product matrices now govern; architecture, buildability, testing, official support, versions, and exceptions remain distinct. |
| ARCH-3 allowed duplication while the new product policy requires shared core | CORE-1 expressly governs shared product behavior; feature modularity and process boundaries remain valid. |
| Non-Rust native UIs versus Rust-first | UI exceptions are component-scoped; both UI strategies retain the shared Rust core. |
| NAS hub versus offline operation, five modes, and distributed authority | Hub is an opt-in topology role with local copies and reconciliation; it implies neither raw database sharing nor automatic ownership transfer. |
| All applicable shared data on NAS versus privacy/data minimization | Sync scope respects user selection, authority, retention, and privacy; excluded data is not silently uploaded. |
| NAS removal/local access versus partial working copies | Locally retained data remains accessible; deliberate removal has a preservation/transfer path, with truthful limits for unavailable remote-only content. |
| Optional Hermes versus generic AI-native capability language | Hermes-independent core behavior is explicit; unrelated inherently AI-native functions retain truthful dependency contracts. |
| No sole opaque AI store versus technology-neutral DATA-1 | The rule addresses opacity and dependency on Hermes, not a ban on vector databases containing independently accessible authoritative originals. |
| Prior immediate review/ratification plan versus new owner decisions | New working version and gated sequence replace that plan; rc1 review remains historical evidence only. |

These are direct integration reconciliations, not new adversarial findings or a ratification recommendation.

## Pending and continuation plan

**Hermes / User-Adaptable File Structure Blueprint — PENDING FINAL DESIGN — DO NOT INVENT OR FREEZE YET.** Await the owner's final comparative analysis and blueprint. Mosaic, LMS, Accounting-and-Money, and Read-and-Watch repositories and their implementation details were not inspected.

No additional unresolved universal-policy question was identified in this pass. The owner may add further policies. Product-specific implementations and support evidence remain product responsibilities, not silently invented ecosystem decisions.

Continue from this integrated working candidate: receive missing design input, integrate only new decisions, update this progress record, and validate the changed documentation. Do not repeat completed rc1 work or perform an attack while policy design is open. After the owner explicitly confirms **“There is nothing else left to add.”**, freeze the final candidate and proceed to the final attack; ratification remains a separate owner action.

## Validation and repository record

Executed document integrity and preservation checks:

- All 262 local Markdown links across nine Markdown files resolve, including fragment anchors.
- All 70 rule IDs are unique, anchored, and have type/origin/applicability metadata; 30 numbered sections remain sequential.
- All 57 rc1 rule IDs and classifications remain present; 13 new rules were added. Existing rule-body changes are limited to LANG-1, DATA-1, PORT-1, NAS-1, NAS-2, GOV-3, and GOV-4.
- The original adversarial review, rc1 integration disposition, and initial-generation provenance are byte-identical to the reviewed baseline. The rc1 branch still points to the reviewed commit.
- `git diff --check` passed for this integration's tracked changes.
- Policy coverage and direct integration conflicts were checked against the owner's instructions. No new adversarial attack, application inspection, runtime test, or ratification was performed.

These checks provide no application runtime, platform-support, NAS-safety, or adversarial verification claim. This documentation-only repository requires no application runtime, dependency installation, or reusable environment setup changes for this workflow.

- Modified: `UNIVERSL RULES FOR ALL APPS.md`, `README.md`, `CHANGELOG.md`, `decisions/ADR-0001-rust-first.md`.
- Created: `reviews/2026-10-rc1-verification-outcome.md`, this integration report.
- Prior review/provenance files and reviewed rc1 branch retained unchanged.
- Commits for this pass are on `constitution/pre-ratification-working`; use Git history after baseline `d9fc392ceddad5f760e0d4a71070bbc723609f77` for their immutable IDs. The final conversation report records the resulting HEAD without creating a self-referential commit hash in this file.

**NOT READY FOR FINAL ADVERSARIAL ATTACK UNTIL THE OWNER CONFIRMS ALL POLICY DESIGN IS COMPLETE.**
