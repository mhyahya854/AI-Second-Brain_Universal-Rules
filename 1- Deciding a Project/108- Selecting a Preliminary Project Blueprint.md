<a id="dev-6"></a>
### 31.6. DEV-6 — Discoverable planning and implementation responsibilities

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** substantial application repositories, with proportionate representations for smaller applications

Substantial applications SHOULD conceptually separate `Application/Master Plan/` from `Application/Codebase/`, using the complete detailed default in [BLUEPRINT-1](#blueprint-1). The implementation belongs to Codebase; Master Plan holds durable specification, intelligence, state, decisions, and the roadmap. These logical responsibilities MUST remain clear and discoverable. Physical names/layout MAY be adapted when sound engineering or framework compatibility requires it, with an explicit navigation mapping; smaller projects may combine concise records without dropping applicable lifecycle gates. Historical references to “APP Plan” denote this planning responsibility, not a second required folder.

The APP Plan blueprint MUST support these discoverable responsibilities, directly or by clear references:

| Area | Responsibility |
|---|---|
| Master Plan | Current authoritative intended product specification under [DEV-7](#dev-7). |
| Project State | Concise current execution status and authoritative next action under [DEV-9](#dev-9). |
| Research | Important comparative evidence, including adopted/rejected alternatives. |
| Evidence | Supporting benchmark/prototype results, compatibility tests, GitHub comparisons, architecture experiments, migration rehearsals, and citations, directly or by stable references without needless large-artifact duplication. |
| Decisions | Individually discoverable architectural choices and rationale. |
| Phases | Active and planned executable implementation specifications. |
| Done Phases | Completed specifications, actual outcomes, and evidence. |
| Reviews | Candidate-plan attacks, conformance verification, findings, and dispositions. |
| Existing App Assessment | Inherited implementation assessment when adopting the rules for a brownfield app. |
| UI design, where relevant | Product value/flows/information hierarchy, brief, identity/references/design system, platform/accessibility, states, adaptation, anti-slop and rendered QA under [UI-4](#ui-4)–[UI-7](#ui-7). |
| Agent Skill metadata, where relevant | Universal/project workflows, trusted revisions/provenance, modifications/permissions and reliable references under [SKILL-1](#skill-1)–[SKILL-3](#skill-3). |

This is a development-artifact blueprint, distinct from the runtime user-data/workspace contract in [section 32](#s32). Organized APP Plan records do not establish that product data is discoverable, and a navigable runtime hierarchy does not replace a proper APP Plan. Evidence, Research, and completed execution records may share storage/references while retaining their distinct responsibilities. Equivalent domain-appropriate representations are allowed; names do not establish compliance.

