<a id="dev-10"></a>
### 31.10. DEV-10 — Phases as executable implementation specifications

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** planned implementation and conformance phases

Each phase MUST be sufficiently specified for bounded execution rather than a loose task list. Define as appropriate its objective, rationale, prerequisites, current and expected end states, files/components, interfaces/contracts, data structures, dependencies, tasks and ordering, invariants, files/systems that must not change, error behavior, edge cases, migration impact, security/privacy, tests, validation commands, expected results, completion evidence, stopping conditions, follow-up state, and next phase.

If major architecture must still be invented during execution, the phase is insufficiently specified and affected implementation MUST stop for planning resolution. A phase MUST distinguish delegated implementation choices from unresolved architectural decisions. Acceptance criteria and validation MUST describe outcomes that can actually be checked under [TEST-1](../13-%20Testing%20Debugging%20and%20Repairing/1301-%20Preparing%20the%20Complete%20Test%20Environment.md#test-1), not merely the presence of code.

Substantial phases MUST be decomposed into individually numbered, bounded subphases under [EXEC-1](802-%20Dividing%20Phases%20Into%20Subphases.md#exec-1), each carrying the concrete 33-field execution contract under [EXEC-2](803-%20Dividing%20Subphases%20Into%20Atomic%20Tasks.md#exec-2). The parent phase remains the governing specification and conformance boundary. Tiny phases may contain one numbered executable subphase in the same file without artificial folders; proportionate representations do not waive required fields, acceptance evidence, numerical order, or stop conditions.

The temporary emergency path in [DEV-17](../16-%20Maintaining%20Updating%20and%20Recovering/1603-%20Handling%20Incidents%20and%20Emergencies.md#dev-17) may defer only necessary normal planning steps; its durable emergency record and subsequent repair contract do not grant permission to invent unknown architecture.

Phase specifications MAY name relevant process skills for bounded loading, but MUST retain their actual project-specific specification under [SKILL-2](806-%20Selecting%20Compatible%20Skills%20for%20Each%20Task.md#skill-2). Substantial UI phase acceptance MUST include applicable rendered review under [UI-7](../5-%20Designing%20the%20UI%20and%20UX/510-%20Reviewing%20and%20Approving%20the%20Design.md#ui-7); “use frontend-design skill” alone is not a phase contract.

