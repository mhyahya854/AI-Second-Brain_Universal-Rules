<a id="dev-6"></a>
### 31.6. DEV-6 — Discoverable planning and implementation responsibilities

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** substantial application repositories, with proportionate representations for smaller applications

Substantial applications SHOULD conceptually separate `Application/Master Plan/` from `Application/Codebase/`, using the complete detailed default in [BLUEPRINT-1](../6-%20Writing%20the%20Complete%20Master%20Plan/608-%20Finalizing%20the%20Project%20Folder%20Structure.md#blueprint-1). The implementation belongs to Codebase; Master Plan holds durable specification, intelligence, state, decisions, and the roadmap. These logical responsibilities MUST remain clear and discoverable. Physical names/layout MAY be adapted when sound engineering or framework compatibility requires it, with an explicit navigation mapping; smaller projects may combine concise records without dropping applicable lifecycle gates. Historical references to “APP Plan” denote this planning responsibility, not a second required folder.

The APP Plan blueprint MUST support these discoverable responsibilities, directly or by clear references:

| Area | Responsibility |
|---|---|
| Master Plan | Current authoritative intended product specification under [DEV-7](../6-%20Writing%20the%20Complete%20Master%20Plan/601-%20Defining%20All%20Project%20Requirements.md#dev-7). |
| Project State | Concise current execution status and authoritative next action under [DEV-9](../17-%20Preserving%20Memory%20and%20Learning/1701-%20Recording%20Current%20Project%20State.md#dev-9). |
| Research | Important comparative evidence, including adopted/rejected alternatives. |
| Evidence | Supporting benchmark/prototype results, compatibility tests, GitHub comparisons, architecture experiments, migration rehearsals, and citations, directly or by stable references without needless large-artifact duplication. |
| Decisions | Individually discoverable architectural choices and rationale. |
| Phases | Active and planned executable implementation specifications. |
| Done Phases | Completed specifications, actual outcomes, and evidence. |
| Reviews | Candidate-plan attacks, conformance verification, findings, and dispositions. |
| Existing App Assessment | Inherited implementation assessment when adopting the rules for a brownfield app. |
| UI design, where relevant | Product value/flows/information hierarchy, brief, identity/references/design system, platform/accessibility, states, adaptation, anti-slop and rendered QA under [UI-4](../5-%20Designing%20the%20UI%20and%20UX/501-%20Understanding%20the%20Desired%20Experience.md#ui-4), [UI-5](../5-%20Designing%20the%20UI%20and%20UX/506-%20Building%20the%20Design%20System.md#ui-5), [UI-6](../11-%20Building%20the%20Frontend/1106-%20Implementing%20Loading%20Empty%20and%20Error%20States.md#ui-6), [UI-7](../5-%20Designing%20the%20UI%20and%20UX/510-%20Reviewing%20and%20Approving%20the%20Design.md#ui-7). |
| Agent Skill metadata, where relevant | Universal/project workflows, trusted revisions/provenance, modifications/permissions and reliable references under [SKILL-1](../0-%20Start%20Here%20and%20Universal%20Rules/006-%20Global%20Skills%20and%20Always-On%20Rules.md#skill-1), [SKILL-2](../8-%20Dividing%20the%20Project%20Into%20Executable%20Steps/806-%20Selecting%20Compatible%20Skills%20for%20Each%20Task.md#skill-2), [SKILL-3](../7-%20Attacking%20and%20Freezing%20the%20Master%20Plan/706-%20Checking%20Skills%20Dependencies%20and%20Conflicts.md#skill-3). |

This is a development-artifact blueprint, distinct from the runtime user-data/workspace contract in [section 32](../5-%20Designing%20the%20UI%20and%20UX/503-%20Designing%20Information%20Architecture%20and%20Flows.md#s32). Organized APP Plan records do not establish that product data is discoverable, and a navigable runtime hierarchy does not replace a proper APP Plan. Evidence, Research, and completed execution records may share storage/references while retaining their distinct responsibilities. Equivalent domain-appropriate representations are allowed; names do not establish compliance.

