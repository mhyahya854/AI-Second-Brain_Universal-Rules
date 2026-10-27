<a id="s41"></a>
## 41. Exact execution, limited repair, and evidence-bearing completion

<a id="exec-1"></a>
### 41.1. EXEC-1 — Strict numerical phases and subphases

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** planned application implementation and conformance execution

Phases MUST execute in ascending numerical order; subphases MUST execute in ascending numerical order within their parent phase. An executor MUST NOT skip unfinished required work, jump from `001.002` to `001.005`, or begin a later phase before the current phase passes its completion gate. A substantial phase MUST have a parent Markdown specification, individually numbered subphase specifications, explicit dependencies, evidence references, and completion status in its folder. Keep phases meaningfully verifiable and subphases independently understandable, bounded tasks. Tiny phases may use one numbered executable subphase in the same file rather than artificial folders; the execution contract still applies.

When a newly discovered dependency or necessary repair changes the sequence, stop affected progression and revise the authorized plan through [DEV-5](#dev-5), [DEV-7](#dev-7), and [GOV-3](#gov-3). Preserve old identifiers and evidence through a supersession/mapping record, assign unambiguous numerical execution order to the revised unfinished sequence, and reconcile Project State before resuming. The executor MUST NOT invent a new order. Bounded in-subphase repair is governed by [EXEC-3](#exec-3). [DEV-17](#dev-17)'s urgent containment path is the existing narrowly scoped exception to ordinary scheduling, not a way to mark skipped work done or resume ordinary features before reconciliation.

