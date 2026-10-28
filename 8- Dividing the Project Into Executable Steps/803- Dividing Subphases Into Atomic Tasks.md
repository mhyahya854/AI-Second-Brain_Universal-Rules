<a id="exec-2"></a>
### 41.2. EXEC-2 — Mandatory 33-field executable subphase contract

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** every executable application subphase

Each executable subphase MUST contain these numbered headings with concrete task-specific details. Explicitly explain inapplicability where a field has no relevant content; omission, unexplained placeholders, or “implement correctly” do not satisfy the contract. Additional meaningful headings MAY be added.

1. **Objective.** The exact bounded outcome.
2. **Purpose and rationale.** Why the work is needed and its intended value.
3. **Preconditions.** Required authority, environment, prior evidence, tools, and dependencies.
4. **Previous required subphase.** Exact predecessor and verified completion requirement, or explicit first-task status.
5. **Exact repository starting state.** Branch/revision or resolvable baseline, relevant dirty state, and conditions that must be checked before editing.
6. **Exact files to read.** Paths and relevant sections/symbols, with a bounded navigation route.
7. **Exact files to create.** Paths and ownership/responsibility.
8. **Exact files to modify.** Paths and permitted regions or interfaces.
9. **Files forbidden from modification.** Protected files, systems, data, and boundaries.
10. **Related Master Plan sections.** Exact governing numbered sections/anchors.
11. **Relevant existing implementation.** Reusable components, current behavior, and gaps assessed from actual code.
12. **Required inputs.** Types, examples, provenance, and validity constraints.
13. **Required outputs.** Artifacts, values, observable behavior, and persistence expectations.
14. **Exact implementation steps.** Ordered concrete actions and any expressly delegated ordinary choices.
15. **Required interfaces and signatures.** Names, types, contracts, callers, and compatibility constraints.
16. **Relevant data types and schemas.** Structures, identifiers, versioning, and applicable migrations.
17. **State transitions and side effects.** Preconditions, mutations, external effects, atomicity, and acknowledgement boundaries.
18. **Validation.** Input/domain/state validation and required invariants.
19. **Error handling.** Failure classes, truthful reporting, safe interruption, and recovery behavior.
20. **Security and authorization.** Effective principals, permissions, trust boundaries, privacy, and secret handling.
21. **Edge cases.** Applicable empty, invalid, duplicate, large, concurrent, interrupted, and platform cases.
22. **No-fallback restrictions.** Selected implementation and the prohibited substitutions relevant to this task.
23. **Required comments and file headers.** Applicable explanations and exact documentation updates under [DOC-1](../12-%20Connecting%20and%20Completing%20the%20Application/1203-%20Integrating%20Complete%20Features.md#doc-1).
24. **Connected files and dependencies.** Actual connection paths and affected maps under [DOC-2](../12-%20Connecting%20and%20Completing%20the%20Application/1201-%20Reviewing%20the%20Integration%20Map.md#doc-2).
25. **Required tests.** Relevant existing/new test cases and their actual claims; justified inapplicability where appropriate.
26. **Exact validation commands.** Working directory, commands, prerequisites, fixtures, and necessary environment details without disclosing secrets.
27. **Expected results.** Checkable outputs, acceptance conditions, and justified tolerances rather than invented future results.
28. **Repair scope.** Permitted correction areas plus finite attempt/time bounds and escalation threshold.
29. **Conditions requiring escalation.** Missing contracts, authority, incompatible evidence, architectural changes, repeated failure, and other specific stop conditions.
30. **Completion checklist.** All acceptance conditions and applicable conformance checks.
31. **Evidence recording.** Where to record actual changes, commands, outcomes, errors, repairs, unresolved issues, and tested revision.
32. **Project State update.** Exact status, paths, evidence pointers, and next-action changes required.
33. **Next subphase.** Exact next authorized identifier/path, or the parent completion gate when this is the last subphase.

The planning capability MUST resolve major architecture beforehand and provide concrete contracts, examples, expected outputs, and verified commands wherever possible. Distinguish a proposed command from one already executed successfully; commands requiring a future environment must identify that prerequisite. If required information is missing, contradictory, or cannot safely be established, the execution model MUST stop affected work and record the precise unresolved issue. A stronger planning/review process must resolve material ambiguity; an executor MUST NOT invent interfaces, widen permissions, silently change requirements, or guess architecture under [DEV-11](808-%20Creating%20Small%20Model%20Execution%20Packets.md#dev-11).

