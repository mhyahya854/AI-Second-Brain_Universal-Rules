# Remaining owner decisions — development-governance integration

- Status: **1.0.0-working.1 — Pre-Ratification Working Candidate**, unratified.
- Branch: `constitution/pre-ratification-working`.
- Expected earlier HEAD supplied by owner: `237b643f6830d3207377a688c1a819b7c65458e5`.
- Actual clean starting HEAD verified before edits: `337e3b95f9685f79121b5e572a86e7f583cd1900` — includes the intervening Linux Mint policy commit.
- Authority: owner's “Integrate All Remaining Owner Decisions” instructions in this conversation.
- Scope: governance documentation in this repository only. No new application implementation, unrelated app assessment, Hermes comparative research, final attack, ratification, merge, or release is performed by this pass.

This is a policy-integration and progress record, not a hostile review or a replacement for historical rc1 evidence. Rule links identify the primary normative source; this report adds no obligations. The working version remains open, with exact revisions identified by Git.

## Owner-decision coverage

| Owner sections | Integrated rules and disposition |
|---|---|
| 1 — Core purpose | Introduction and [DEV-1](../UNIVERSL%20RULES%20FOR%20ALL%20APPS.md#dev-1): longevity, maintainability, understanding, recovery, portability, evolution, AI continuity, user control, coherent app-specific design; blueprint/development system rather than identical products. |
| 2 — Refine before code | [DEV-2](../UNIVERSL%20RULES%20FOR%20ALL%20APPS.md#dev-2): interrogate the idea and all listed product, data, platform, offline/NAS, AI, privacy, lifetime, and failure dimensions before implementation. |
| 3 — Research before freeze | [DEV-3](../UNIVERSL%20RULES%20FOR%20ALL%20APPS.md#dev-3): relevant repositories, mature apps, standards, libraries, papers/docs, failures, competing approaches; deliberate adoption or retention with evidence. |
| 4 — Strongest planning | [DEV-4](../UNIVERSL%20RULES%20FOR%20ALL%20APPS.md#dev-4): strongest reasonably available model for substantial planning, durable outputs, no continuing cloud/provider dependency. |
| 5 — Plan attack/freeze | [DEV-5](../UNIVERSL%20RULES%20FOR%20ALL%20APPS.md#dev-5): candidate-plan Attack/Fix cycles across listed risks, material issues resolved or explicitly accepted, evidence-based Plan Freeze Gate before implementation. |
| 6–7 — Root and APP Plan blueprint | [DEV-6](../UNIVERSL%20RULES%20FOR%20ALL%20APPS.md#dev-6): discoverable APP Plan/Codebase separation and all eight planning responsibilities; adaptable names, proportional records. |
| 8 — Master Plan | [DEV-7](../UNIVERSL%20RULES%20FOR%20ALL%20APPS.md#dev-7): current intended product authority and all applicable specification areas, distinct from brainstorming and actual implementation status. |
| 9–10 — Research and decisions | [DEV-8](../UNIVERSL%20RULES%20FOR%20ALL%20APPS.md#dev-8): comparative evidence and individually discoverable choices, adopted/rejected alternatives and rationale. |
| 11 — Project State | [DEV-9](../UNIVERSL%20RULES%20FOR%20ALL%20APPS.md#dev-9): concise machine/human-readable current execution entry point, all required status fields, next authoritative action and active phase location. |
| 12 — Phase specification | [DEV-10](../UNIVERSL%20RULES%20FOR%20ALL%20APPS.md#dev-10): executable implementation specifications including contracts, boundaries, error/edge behavior, validation, evidence, stop conditions and next state. |
| 13–15 — Full-build continuity and safety | [DEV-11](../UNIVERSL%20RULES%20FOR%20ALL%20APPS.md#dev-11): entire app phase-by-phase with a sufficiently capable small local model; zero-chat resumption; bounded execution, no guessing or implicit authority. |
| 16 — Done Phases | [DEV-12](../UNIVERSL%20RULES%20FOR%20ALL%20APPS.md#dev-12): completed specification, actual work, deviations, decisions, validation, revisions, evidence, and follow-ups; complements Git. |
| 17–18, 22 — Phase gates and verification | [DEV-13](../UNIVERSL%20RULES%20FOR%20ALL%20APPS.md#dev-13): Universal Rules / Master Plan / Phase Contract gate after every phase, actual-artifact verification by AI/humans/automation, repair before progression and explicit exceptions for debt. |
| 19–21 — Brownfield | [DEV-14](../UNIVERSL%20RULES%20FOR%20ALL%20APPS.md#dev-14): pause features, inspect authorized app, update plan, assess inherited work, classify all listed categories, repair through Conformance Phases, verify then resume; preserve compliant code. |
| 23 — Linux targets | [PORT-3](../UNIVERSL%20RULES%20FOR%20ALL%20APPS.md#port-3): Arch Linux, CachyOS, Ubuntu LTS, Linux Mint (current stable Ubuntu-based release), equal support/validation expectations including permissions and native/system integration; other distributions best-effort unless promoted. |
| 24–25 — Product core/UI | [CORE-1](../UNIVERSL%20RULES%20FOR%20ALL%20APPS.md#core-1), [UI-1](../UNIVERSL%20RULES%20FOR%20ALL%20APPS.md#ui-1), [UI-2](../UNIVERSL%20RULES%20FOR%20ALL%20APPS.md#ui-2): applicable desktop/mobile/tablet/web-associated native clients share Rust domain truth; both UI strategies preserve canonical behavior. |
| 26–27 — Local-first and NAS | [OFFLINE-3](../UNIVERSL%20RULES%20FOR%20ALL%20APPS.md#offline-3), [SYNC-2](../UNIVERSL%20RULES%20FOR%20ALL%20APPS.md#sync-2), [SYNC-3](../UNIVERSL%20RULES%20FOR%20ALL%20APPS.md#sync-3), [NAS-1](../UNIVERSL%20RULES%20FOR%20ALL%20APPS.md#nas-1): mandatory applicable no-NAS local-first continuity, user-enabled NAS shared hub, local copies, reconciliation, distinct NAS roles. |
| 28–30 — Hermes direction/safety | [HERMES-1](../UNIVERSL%20RULES%20FOR%20ALL%20APPS.md#hermes-1), [HERMES-2](../UNIVERSL%20RULES%20FOR%20ALL%20APPS.md#hermes-2), [section 30](../UNIVERSL%20RULES%20FOR%20ALL%20APPS.md#s30): pending four-source comparison, discoverability rather than uniform user hierarchy, approximate 1B target and deterministic query/catalog/ID/resource direction, bounded validated writes, provenance/audit/privacy. |
| 31–32 — Longevity and memory | [DEV-15](../UNIVERSL%20RULES%20FOR%20ALL%20APPS.md#dev-15): explicit years-later continuation test and durable repository memory without chat, provider, developer, or machine dependence. |
| 33–34 — Gate and classifications | [GOV-4](../UNIVERSL%20RULES%20FOR%20ALL%20APPS.md#gov-4) and section 31: owner policy status explicit; no final constitutional attack triggered by app-plan review policy. |
| 35–36 — Validation/report | Consistency outcomes and repository records below; final conversation report supplies committed HEAD and state. |

## Governance and classification

All fifteen DEV rules are **ECOSYSTEM POLICY**, **Origin: USER POLICY**, with scoped applicability and inherited **CANDIDATE** status. MUST/MUST NOT express mandatory lifecycle outcomes and gates; SHOULD retains adaptable conceptual structure and design preferences; MAY permits equivalent representations or verification actors. No literal directory tree, specific model provider, file format, or verifier identity is promoted to a universal invariant.

Existing CORE-1, PORT-3, HERMES-1/2, SYNC-2, and GOV-2/4 remain ecosystem policies. Existing AI authorization, truthful results, privacy, storage, exception governance, proportional testing, and recovery contracts remain governing constraints. SYNC-2 now expressly requires a local-first mechanism when cross-device continuity is required.

## Direct conflicts resolved

| Tension | Resolution |
|---|---|
| Expected HEAD excludes intervening Mint commit | Used actual `337e3b9` baseline and retained the change. |
| Fixed-looking APP Plan blueprint versus flexible feature/user-data structure | Mandated discoverable development responsibilities, adaptable names; explicitly separate from the pending user-data/Hermes blueprint. |
| General proportional/optional machine-readable documentation versus required Project State | GOV-2 now references DEV-9's specific mandatory current-state capability; concise combined artifacts remain possible. |
| Strongest-model planning versus local-first implementation | Planning uses reasonably available capability and records durable outputs; no named provider, permanent cloud, or continued strongest-model dependency. |
| Weak-model full-build target versus bounded AI authority | Full-build readiness concerns artifacts and phase contracts, not unrestricted execution; missing/contradictory information stops affected work. |
| Plan acceptance versus unresolved defects or constitutional exceptions | Material issues require resolution or explicit documented authorized acceptance; constitutional departures still require GOV-3. |
| Brownfield conformity versus rebuilding everything/future roadmap | Preserve compliant/reusable work; repair inherited implemented scope and its obligations before features; unbuilt planned features do not force premature whole-product completion. |
| Conformance failure versus permission to repair | Scoped repair proceeds to resolve documented failures; ordinary feature progression waits for conformance. |
| Done Phases versus Git | Preserve understandable specification/outcome evidence with revision links; Git is complementary, not the only memory or a replacement for phase evidence. |
| Master Plan versus Project State | Master Plan owns current intended product specification; Project State owns current execution status/navigation; Done Phases owns completed evidence. |
| Broad app research versus restricted Hermes comparison | DEV-3 governs general app planning; pending Hermes blueprint remains limited to the four owner-named plans/discussions. |
| App-plan hostile review versus prohibited constitutional attack | DEV-5 explicitly defers constitutional timing to GOV-4 and the pending owner sequence; this pass performs integration checks only. |

## Remaining pending design and next action

**Hermes / User-Adaptable File Structure Blueprint — PENDING FINAL DESIGN — DO NOT INVENT OR FREEZE YET.** Its source comparison is limited to Mosaic, LMS, Accounting-and-Money, and Read-and-Watch, including their strongest historical plans and relevant prior discussions. No such repositories or discussions were inspected during this pass.

The next authoritative design action is to finish that separate comparison and receive the owner-supplied blueprint, then integrate it and discuss any remaining missing universal policies. Owner policy-completion review remains outstanding. Only explicit **“There is nothing else left to add.”** confirmation permits the subsequent candidate freeze and final attack. Ratification remains a separate owner decision; this task grants no merge/tag authority.

No additional specific unresolved universal-policy design question was identified. This does not declare the rules complete or imply that the pending owner review has occurred. Resume from this integration and do not repeat completed rc1 work.

## Validation and repository record

Executed document-integrity checks passed: 318 local Markdown links across ten files resolve; all 85 rules have unique IDs, anchors, and type/origin/applicability metadata; all 31 numbered sections are sequential. All 70 prior rule IDs and classifications remain present, with fifteen new owner-policy DEV rules. Existing rule-body changes are limited to CORE-1, PORT-3, HERMES-1, HERMES-2, SYNC-2, GOV-2, and GOV-4. `git diff --check` passed. Existing review, provenance, and ADR files are byte-identical to the actual starting revision; the rc1 branch still points to its reviewed commit.

The owner's requested direct-consistency checks were also completed:

| Check | Result |
|---|---|
| Linux Mint included; no stale active baseline list | PASS — active lists include all four targets; changelog identifies earlier additions as history and also states the complete current set. |
| New-app lifecycle | PASS — idea refinement precedes research and plan completion; candidate review and Plan Freeze Gate precede implementation. |
| Brownfield lifecycle | PASS — pause features, assess, plan conformance repairs, verify, then resume. |
| Phase completion gates | PASS — all three applicable layers precede completion/progression; failure permits repair, not feature bypass. |
| Full-build weak-model goal versus AI safety | PASS — durable artifacts enable bounded execution; missing information stops affected work; authority is not expanded. |
| Strongest planning versus cloud dependence | PASS — reasonably available planning capability, durable outputs, local execution continuity, no permanent provider dependency. |
| APP Plan / Codebase terminology | PASS — logical planning-memory versus implementation roles consistently distinguished; exact folders adaptable. |
| Project State responsibility | PASS — one current execution/navigation responsibility, separate from product specification and completed evidence. |
| Done Phases versus Git | PASS — readable evidence with revision references complements version history. |
| Existing-app repair versus unnecessary rewrites | PASS — preserve compliant work, repair gaps, replace only where necessary. |
| Continuous conformance | PASS — new features cannot bypass repair or an explicit approved exception; current-scope requirements distinguished from future roadmap. |
| Pending Hermes detail | PASS — marker retained, only four named comparative inputs, no user-data structure frozen. |
| Constitutional attack gate | PASS — application review rules explicitly do not trigger the final attack; Hermes integration and owner completion review remain outstanding. |

These are documentation and direct-consistency checks, not an adversarial review or implementation certification. No application runtime or Linux-distribution validation was claimed or performed.

- Modified: primary constitution, README, CHANGELOG.
- Created: this integration report.
- Existing historical reviews and provenance are retained without rewriting their findings.
- Commit IDs are available in branch history after the actual baseline above; final HEAD is reported in the conversation to avoid a self-referential commit identifier.

**NOT READY FOR FINAL ADVERSARIAL ATTACK — HERMES / FILE-STRUCTURE BLUEPRINT AND OWNER POLICY COMPLETION REVIEW REMAIN OUTSTANDING.**
