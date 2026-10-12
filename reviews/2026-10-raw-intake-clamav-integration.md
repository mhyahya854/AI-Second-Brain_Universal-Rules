# Raw intake and native ClamAV candidate-policy integration

- Date: 2026-10-12 (owner/client date).
- Branch: `constitution/pre-ratification-working`.
- Verified starting HEAD: `ec0d03a117bc56c97bcbb031d48851e53dc5e602`.
- Starting working tree: clean; 100 existing normative IDs.
- Candidate remains `1.0.0-working.1 — Pre-Ratification Working Candidate`, unfrozen and unratified.
- Authority: owner's “FOLLOW-UP OWNER POLICY — RAW INTAKE AND NATIVE CLAMAV SECURITY” in this conversation.

This delta supplements the preceding lifecycle/timezone/malware integration. It is documentation integration and direct consistency validation, not a new policy-completion or adversarial review. Prior records remain unchanged. The owner reports possessing a ClamAV source archive; no archive was supplied or evaluated in this task, and no source version, digest, runtime suitability, or legal compliance is inferred.

## Integrated rules and classification

Three focused additions within existing families, each **ECOSYSTEM POLICY / USER POLICY / CANDIDATE** with explicit applicability:

- [IO-2](../UNIVERSL%20RULES%20FOR%20ALL%20APPS.md#io-2): logical Raw intake, untrusted originals, promotion gates, quarantine and authorized deletion.
- [IO-3](../UNIVERSL%20RULES%20FOR%20ALL%20APPS.md#io-3): incremental scan validity, outcomes/evidence, signatures, status, failure recovery, and cross-device trust.
- [SEC-6](../UNIVERSL%20RULES%20FOR%20ALL%20APPS.md#sec-6): replaceable local scanner capability, ClamAV preference, protected execution, cross-platform scope, provenance and licensing verification.

Existing IO-1, HERMES-1, and DEV-7 gain cross-references and enforcement/planning connections. No prior IDs or type/origin classifications change. Section 30, README, and CHANGELOG record the new delta while retaining the owner gate. SHOULD expresses the Raw/ClamAV/process preferences; MUST expresses applicable trust, promotion, evidence, and security contracts. A suitable replacement scanner can be chosen with documented rationale rather than a formal exception merely for replacing the preferred implementation.

## Owner requirement coverage

| Owner sections | Disposition |
|---|---|
| 1–2 | IO-2 prefers a logical Raw/Intake/Staging area; `Raw/` is a preferred name, not a mandatory physical directory. All entering content starts untrusted; data-tree placement grants no trust. |
| 3 | SEC-6 prefers evaluating ClamAV when platform, license, distribution, performance, and threat model fit. Core uses a generic capability; engine-specific details stay in the adapter. |
| 4 | SEC-6 requires incorporated-source version/upstream/revision where available/digest/license/notices/date/modifications/build configuration/update strategy and modification history. Actual integration/redistribution must be verified against applicable GPLv2 and bundled-component obligations before distribution; no legal conclusion is presumed. SEC-4/5 remain governing provenance/build contracts. |
| 5–7 | SEC-6 prefers device or authorized local infrastructure, optional expressly authorized cloud scanning, constrained scanner process/protected IPC where practical, and justified direct-library alternatives. Unauthenticated daemon TCP exposure to public/untrusted networks is prohibited; locality alone is not authorization. |
| 8–10 | IO-3 evaluates every Raw object's validity on start/open through a preferred non-blocking background workflow. Safe prior verdicts may be reused; new/materially changed files queue promptly while running. Unestablished required validity gates affected content rather than blocking unrelated UI startup. |
| 11–13 | IO-3 represents all named conceptual states, failure versus clean, bounded CLEAN meaning, and content-bound scan receipts. Transient progress is not automatically canonical. Parser/format/resource/active-content defenses remain after a clean verdict. |
| 14–15 | IO-3 includes local signature maintenance via freshclam or equivalent, current/stale/unavailable/update-failed status, and risk-based rescan policy accounting for file, engine, signature, policy, age, threat intelligence, and cost. No automatic full-library rescan for every minor update. |
| 16–17 | IO-3 requires platform-appropriate non-blocking progress/protection/pending/detection/unavailable/completion status, unobtrusive routine success, and proportionate escalation. No literal status-bar requirement; headless structured status and accessible UI are supported. |
| 18–19 | IO-2 prefers real quarantine/isolation rather than automatic destruction based solely on detection. No execution, ordinary trusted parsing, automatic promotion, or false clean status; restricted authorized inspection/recovery may remain. Quarantine naming alone is insufficient; platform-appropriate controls are planned. Legitimate deletion/privacy/security duties remain. |
| 20–21 | IO-2 defines applicable scan/format/security/identity/provenance/core/adoption gates without forcing every step on every input. Promotion binds to verified content/current policy; originals may remain retained and untrusted. Canonical authority is distinct from malware safety. |
| 22 | IO-3 requires explicit decisions for unscanned bytes, quarantine state, verdict propagation, receiving-device rescans, and engine/version differences. A remote CLEAN result supplies no permanent universal trust. Existing NAS/sync/privacy/containment contracts remain. |
| 23–24 | IO-3 follows DEV-16 using incremental inventory, bounded queues, backpressure, resumability, new/unverified priority, safe validity evidence, and truthful failure/retry without core corruption. No mandatory blocking multi-terabyte startup scan. |
| 25 | HERMES-1 explicitly enforces the same intake/security pipeline as native UI, with no model/provider exception or additional mutation authority. |
| 26–27 | SEC-6 preserves declared platforms behind generic typed operations; no universal Linux-only on-access dependency. IO-2 exempts irrelevant apps from empty folders or malware infrastructure while preserving the preferred file-intake design. LANG-1 still distinguishes imported foreign-language dependencies from authored product components. |
| 28 | Direct checks and documentation validation recorded below; no final adversarial attack. |

## Direct reconciliations and proportionality

- **Startup versus complete coverage:** every Raw object's validity is evaluated on open; evaluation may proceed incrementally in the background. No blocking full-byte historical rescan is required, and pending validity does not pass a required promotion gate.
- **Offline availability versus stale/unavailable protection:** independent local functions remain useful, but affected intake gates remain enforced and degraded protection is reported honestly.
- **ClamAV preference versus replaceability/Rust-first:** the engine is an adapter dependency, not canonical product authority; alternatives and justified library integration are permitted. No engine source is vendored by this documentation task.
- **Generic safeguards versus specific intake policy:** IO-1 remains risk-scoped; IO-2/3 define the preferred file-intake workflow without forcing file ingestion, scanning infrastructure, or empty directories onto irrelevant tiny tools.
- **Retention versus detections:** a positive verdict triggers isolation by default, not unconditionally destructive deletion. Authorized erasure/security duties remain; original preservation grants no execution trust.
- **Scan evidence versus canonical truth:** receipts support the relevant promotion decision under DATA-1/PRIV-1; progress is not automatically retained canonical state. CLEAN is a bounded observation, not factual perfection or trust for all future devices.
- **Process boundaries versus legal/security claims:** protected process execution is preferred where practical, not universally required or proof of license compliance or total containment. Actual platform, license, privacy, and privilege requirements remain applicable.
- **Sync versus global trust:** replicas may carry untrusted content only under declared policy, without implicit promotion. Receiver security policy determines verdict reuse/rescans.

## Validation

Executed structural and history checks:

- **PASS:** 538 local Markdown links across 13 files resolve, including fragment anchors.
- **PASS:** 103 unique normative IDs have anchors and type/origin/applicability metadata; all 32 section anchors and section numbering remain intact.
- **PASS:** all 100 prior rule IDs and type/origin classifications remain; IO-2, IO-3, and SEC-6 are the only new IDs, all ECOSYSTEM POLICY / USER POLICY with inherited CANDIDATE status.
- **PASS:** existing rule-body comparison identifies only IO-1, HERMES-1, and DEV-7 as changed, ignoring separator whitespace. Other existing bodies, including all earlier malware, backup, sync, timezone, core-authority, and lifecycle requirements, are unchanged.
- **PASS:** all nine pre-existing historical review/ADR/provenance files are byte-identical to the starting revision; rc1 and local origin/main references are unchanged.
- **PASS:** candidate version, unfrozen/unratified status, integrated Hermes marker, and explicit owner-confirmation gate remain. No stale active pending-blueprint marker or instruction to begin the final attack was introduced.
- **PASS:** `git diff --check` and `git diff --cached --check`, including the newly created report.

Owner-requested direct integration checks:

| Check | Result |
|---|---|
| Raw preferred, not irrelevant folder ceremony | PASS — logical boundary and preferred name; no empty directory or scanner infrastructure for irrelevant apps. |
| Untrusted Raw and explicit promotion gates | PASS — location grants no trust; required pipeline succeeds for actual content/current policy before risky processing or promotion. |
| Native/local default and replaceable ClamAV | PASS — generic boundary and justified alternatives; cloud upload only optional and explicitly authorized. |
| Non-blocking startup with every-object validity evaluation | PASS — background/incremental coverage, pending objects gated, no full historical byte-rescan requirement. |
| Safe reuse and prompt arrival/change handling | PASS — explicit evidence/assumptions, staleness and rescan policy, prompt runtime queueing. |
| Failed/stale/unavailable state versus clean | PASS — explicit states, truthful degraded status, bounded CLEAN meaning, continued parser/security defenses. |
| Visible status without constant alarms | PASS — platform-appropriate desktop/mobile/headless status and relevant escalation; no mandated bottom bar. |
| Quarantine rather than automatic source destruction | PASS — actual isolation controls, restricted inspection, no ordinary trusted processing, authorized deletion/privacy exceptions. |
| Receipts, signatures, and rescan confidence | PASS — content-bound evidence and retention, local signature maintenance/freshness, risk-based invalidation without mandatory full-library scans on minor updates. |
| Core and Hermes authority | PASS — scanner failure cannot grant mutation authority; Hermes uses the same deterministic gates without provider/model bypass. |
| Cross-platform scanner integration | PASS — existing Windows/macOS/four first-class Linux baselines remain; no universal Linux-only on-access dependency. |
| Sync/NAS trust | PASS — explicit transfer and receiver policies; remote CLEAN does not confer permanent universal trust. |
| Lifetime-scale and offline operation | PASS — incremental inventory, bounded queues/backpressure, resumability, priority, and DEV-16 budgets; independent local functions remain available without bypassing intake gates. |
| Provenance and licensing | PASS — archive identity, modification history, build/update strategy and actual pre-distribution verification required; no supplied archive or distribution was certified. |

This repository has no application build/runtime suite. These are documentation and direct integration checks, not the final adversarial attack; they do not establish ClamAV behavior, scan performance, licensing compliance, or supported application platforms.

## Repository record and next action

- Modified: `UNIVERSL RULES FOR ALL APPS.md`, `README.md`, `CHANGELOG.md`.
- Created: this report.
- Historical reports, ADR, and provenance are preserved unchanged; all earlier malware/data protections and universal timezone policy remain.
- Resulting local commit/HEAD and working-tree state are supplied in the final conversation response, avoiding a self-referential hash here.
- No application repository, ClamAV archive, or scanner runtime was inspected or changed. No final owner completion review, adversarial attack, freeze, ratification, push, merge, tag, or release candidate was performed.

No specific unresolved universal-policy question was identified during this integration. Scanner selection, archive provenance, integration licensing, supported-platform behavior, and performance remain application/component implementation decisions requiring actual evidence. One final owner policy-completion review remains before Plan Freeze; explicit owner confirmation still gates candidate freeze and the final attack.

**RAW INTAKE AND NATIVE CLAMAV POLICY INTEGRATED AS CANDIDATE POLICY. NOT FROZEN OR RATIFIED. FINAL ADVERSARIAL ATTACK NOT PERFORMED.**
