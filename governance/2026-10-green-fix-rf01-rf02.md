# RF-01 / RF-02 Green Fix and repaired freeze record

Date: 2026-10-13 (Asia/Riyadh). Candidate: **1.0.0-rc2.1 — Owner-Authorized Repaired Frozen Candidate — Fresh Red Review Required — Not Yet Ratified**.

## Authority, source, and exact revision

Owner instruction in this conversation: “I authorize a narrowly scoped GREEN FIX for RF-01 and RF-02 only.” The owner also requires “a new repaired frozen candidate/revision suitable for fresh Red attack.” This is scoped repair/freeze authority, not general design reopening, execution of a new Red round, or ratification authority.

- Branch: `constitution/pre-ratification-working`.
- Starting HEAD: `9cf038a95ab85589ab5568a83c1480896ccbefa7`, verified clean.
- Prior frozen Red target: `e15191c1509facc3859b46c25cc8a1d1b7eaa12f`.
- Prior normative SHA-256: `3ca97cc27dde83575734a3ce4ea1f645ea0e5c31edfc277453ae1cf44ee08101`.
- The starting HEAD adds only the post-freeze revision receipt to that prior target; their constitutions are identical.
- **Repaired frozen review target:** the commit first introducing this immutable record together with the DEV-5/GOV-5 repairs and current status changes. Resolve its exact hash with `git log --diff-filter=A --format=%H -- governance/2026-10-green-fix-rf01-rf02.md`. Review that commit's constitution; do not substitute a later HEAD. This avoids inventing a self-referential commit hash. The final task report supplies the resulting exact hash.
- `1.0.0-rc2.1` identifies this repair of rc2, not a new policy-design cycle or ratified release.
- Repaired normative artifact SHA-256: `1c6471ab3ec5291b9cd4ec884912ccec10431d2e35e9e514ad29574b778b082d`. This identifies bytes, not correctness or independent authentication.

The original [freeze record](2026-10-plan-freeze.md), [revision receipt](2026-10-plan-freeze-revision.md), and original frozen commit remain unchanged and recoverable. Future findings or repair receipts must append separate records rather than rewrite this one.

## Historical Red report — preserved outcome, not a new review

The immediately preceding Red report in this conversation reviewed exact target `e15191c1509facc3859b46c25cc8a1d1b7eaa12f`. Its outcome was **0 BLOCKER, 0 MATERIAL, 2 NON-BLOCKING**, with rejected hypotheses classified NOT AN ISSUE across lenses A–P. It did not establish two-round convergence or ratify. Four separately tasked lens reviewers and the coordinating reviewer shared a model environment and inherited context; the report disclosed that these were not blind external reviews or two independent rounds.

The full report remains the unchanged conversation record; no repository Red-report file existed at the start of this repair. This section is a traceable outcome/finding summary, not a claimed verbatim copy or replacement of that report. All pre-existing repository review files remain byte-identical. No historical outcome is upgraded into a review of this repaired candidate.

| Finding | Original classification and confidence | Original issue and scenario | Authorized disposition |
|---|---|---|---|
| RF-01 — Pre-freeze research-code boundary | NON-BLOCKING; moderate confidence | DEV-5 gates implementation while DEV-6 recognizes prototype/experiment evidence. An executor may stop a bounded storage feasibility experiment needed to resolve architecture, or mislabel production construction as research. Existing acceptance/exception routes prevent an established deadlock. | ACCEPTED AND REPAIRED in DEV-5 only. |
| RF-02 — Clean residual-risk sentence scope | NON-BLOCKING; high confidence in ambiguity, moderate practical-error confidence | GOV-5 unconditionally said “State residual risk: No material defect was identified under the defined review battery.” A failed review could repeat that sentence while reporting material findings. Truthfulness rules and protocol context limit the damage but leave ambiguous reporting instructions. | ACCEPTED AND REPAIRED in GOV-5; operational protocol section 138 synchronized. |

There were no BLOCKER or MATERIAL findings to waive. NOT AN ISSUE hypotheses remain rejected historical hypotheses, not repair tasks. Neither finding authorizes broader planning, security, or review-policy changes.

## RF-01 correction and regression boundary

[DEV-5](../UNIVERSL%20RULES%20FOR%20ALL%20APPS.md#dev-5) now expressly allows authorized, bounded evidence-gathering experiments before Plan Freeze for material planning questions. Each needs a question/hypothesis, evidence-bounded scope, results/limitations, and explicit experimental/disposable or otherwise non-authoritative code/data status. The label does not authorize deletion of retained source data or required evidence.

The clarification includes architectural spikes, compatibility tests, storage/performance benchmarks, migration rehearsals, and crash/recovery experiments through their planning purposes. Small research scripts do not need a full production phase solely for evidence gathering. Actual authority, security/privacy, safe execution, and truthful evidence still apply.

Deliberate adoption into the product requires the normal Plan Freeze, phase, conformance, security, testing, and evidence requirements. Substantial production scope cannot bypass planning under a prototype label, and existing code cannot silently become canonical architecture. DEV-2 remains meaningful because DEV-5 explicitly distinguishes research from adopted implementation for both rules. DEV-6/8 evidence remains usable; DEV-11 stopping and DEV-13 completion remain intact. DEV-17 emergency maintenance is unchanged.

## RF-02 correction and regression boundary

[GOV-5](../UNIVERSL%20RULES%20FOR%20ALL%20APPS.md#gov-5) requires every Red report to disclose that review does not prove absolute correctness, security, completeness, or immunity to future unknown conditions. Only a review with zero BLOCKER and zero MATERIAL findings must use the clean-result sentence. A report with either class must not assert that sentence as its outcome; it must report the findings and acknowledge that other defects may remain and the attack does not prove exhaustive discovery.

The [operational protocol](green-red-protocol.md) section 138 expresses the same condition. Its original wording remains recoverable at the prior frozen revision. The 16 lenses, classifications, independence limits, explicit prior dispositions, regression/structural/factuality/proportionality checks, two consecutive independent clean rounds, and separate owner ratification authority remain unchanged.

## Validation and limits

Validation checks the narrowly authorized changes and their interaction with existing gates; it is not a new hostile Red review.

- Stable inventory: 113 unique rule IDs; 33 numbered sections; 33 Skill families. No new IDs or classifications/applicability changes. All 839 local links across 21 Markdown files and their applicable anchors passed. All 16 pre-existing files outside the four edited current documents remain byte-identical to the starting HEAD.
- Exactly two normative rule bodies changed: DEV-5 and GOV-5. Every other complete body is byte-identical to the prior frozen target, including DEV-2/6/8/11/13/17.
- Research cases: a bounded compatibility/benchmark/migration/recovery experiment can gather evidence before freeze; research status cannot authorize production rollout, retained-data destruction, architecture adoption, or bypassed conformance. Missing facts still stop affected execution.
- Reporting cases: zero BLOCKER/MATERIAL requires the qualified clean statement; either nonzero class prohibits asserting the clean outcome and requires truthful material findings plus residual uncertainty. NON-BLOCKING findings alone do not prohibit the qualified clean statement.
- All classifications, applicability, rule references, section/rule anchors, and local Markdown links checked. Existing history, original freeze files, research, ADRs, review files, and prior changelog entries preserved byte-for-byte.
- Whitespace and full patch review checked; current metadata identifies the repaired frozen/unratified candidate and invalidated prior convergence. Structural checks establish documentation consistency, not runtime behavior or absolute semantic correctness.

## Convergence and next action

**The previous Red Flag result is preserved historically but does not satisfy post-repair convergence. The repaired candidate requires two consecutive independent clean Red Flag rounds with zero BLOCKER and zero MATERIAL findings before ratification may be considered.**

Post-repair clean Red rounds completed: **0**. The next review must inspect the exact repaired frozen revision identified above. Every further normative repair resets convergence again under GOV-5. This task performs no new Red attack and does not claim either repair has passed independent adversarial verification.

## Boundary

Only RF-01 and RF-02 were repaired. No general policy brainstorming, unrelated policy, new Red attack, ratification, push, merge, tag, release, history rewrite, or inspection of other applications. Local commit authority follows the owner's GREEN FIX invocation and GOV-5.
