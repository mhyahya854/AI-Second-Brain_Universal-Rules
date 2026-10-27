<a id="dev-10"></a>
### 31.10. DEV-10 — Phases as executable implementation specifications

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** planned implementation and conformance phases

Each phase MUST be sufficiently specified for bounded execution rather than a loose task list. Define as appropriate its objective, rationale, prerequisites, current and expected end states, files/components, interfaces/contracts, data structures, dependencies, tasks and ordering, invariants, files/systems that must not change, error behavior, edge cases, migration impact, security/privacy, tests, validation commands, expected results, completion evidence, stopping conditions, follow-up state, and next phase.

If major architecture must still be invented during execution, the phase is insufficiently specified and affected implementation MUST stop for planning resolution. A phase MUST distinguish delegated implementation choices from unresolved architectural decisions. Acceptance criteria and validation MUST describe outcomes that can actually be checked under [TEST-1](#test-1), not merely the presence of code.

Substantial phases MUST be decomposed into individually numbered, bounded subphases under [EXEC-1](#exec-1), each carrying the concrete 33-field execution contract under [EXEC-2](#exec-2). The parent phase remains the governing specification and conformance boundary. Tiny phases may contain one numbered executable subphase in the same file without artificial folders; proportionate representations do not waive required fields, acceptance evidence, numerical order, or stop conditions.

The temporary emergency path in [DEV-17](#dev-17) may defer only necessary normal planning steps; its durable emergency record and subsequent repair contract do not grant permission to invent unknown architecture.

Phase specifications MAY name relevant process skills for bounded loading, but MUST retain their actual project-specific specification under [SKILL-2](#skill-2). Substantial UI phase acceptance MUST include applicable rendered review under [UI-7](#ui-7); “use frontend-design skill” alone is not a phase contract.

