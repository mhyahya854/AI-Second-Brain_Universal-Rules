<a id="s41"></a>
## 41. Exact execution, limited repair, and evidence-bearing completion

*Section 41 rules across lifecycle files: [EXEC-1](#exec-1), [EXEC-2](803-%20Dividing%20Subphases%20Into%20Atomic%20Tasks.md#exec-2), [EXEC-3](../13-%20Testing%20Debugging%20and%20Repairing/1309-%20Repairing%20Issues%20Without%20Regressions.md#exec-3), [EXEC-4](../0-%20Start%20Here%20and%20Universal%20Rules/008-%20Continuing%20Previous%20Work.md#exec-4), [EXEC-5](../14-%20Reviewing%20the%20Entire%20Application/1409-%20Performing%20Independent%20Final%20Reviews.md#exec-5), [EXEC-6](809-%20Allocating%20Context%20and%20Memory%20Budgets.md#exec-6).*

<a id="exec-1"></a>
### 41.1. EXEC-1 — Strict numerical phases and subphases

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** planned application implementation and conformance execution

Phases MUST execute in ascending numerical order; subphases MUST execute in ascending numerical order within their parent phase. An executor MUST NOT skip unfinished required work, jump from `001.002` to `001.005`, or begin a later phase before the current phase passes its completion gate. A substantial phase MUST have a parent Markdown specification, individually numbered subphase specifications, explicit dependencies, evidence references, and completion status in its folder. Keep phases meaningfully verifiable and subphases independently understandable, bounded tasks. Tiny phases may use one numbered executable subphase in the same file rather than artificial folders; the execution contract still applies.

When a newly discovered dependency or necessary repair changes the sequence, stop affected progression and revise the authorized plan through [DEV-5](../7-%20Attacking%20and%20Freezing%20the%20Master%20Plan/710-%20Freezing%20the%20Approved%20Master%20Plan.md#dev-5), [DEV-7](../6-%20Writing%20the%20Complete%20Master%20Plan/601-%20Defining%20All%20Project%20Requirements.md#dev-7), and [GOV-3](../0-%20Start%20Here%20and%20Universal%20Rules/003-%20Rule%20Priority%20and%20Authority.md#gov-3). Preserve old identifiers and evidence through a supersession/mapping record, assign unambiguous numerical execution order to the revised unfinished sequence, and reconcile Project State before resuming. The executor MUST NOT invent a new order. Bounded in-subphase repair is governed by [EXEC-3](../13-%20Testing%20Debugging%20and%20Repairing/1309-%20Repairing%20Issues%20Without%20Regressions.md#exec-3). [DEV-17](../16-%20Maintaining%20Updating%20and%20Recovering/1603-%20Handling%20Incidents%20and%20Emergencies.md#dev-17)'s urgent containment path is the existing narrowly scoped exception to ordinary scheduling, not a way to mark skipped work done or resume ordinary features before reconciliation.

