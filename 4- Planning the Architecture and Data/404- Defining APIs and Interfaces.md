<a id="arch-3"></a>
### 6.3. ARCH-3 — Contracts and shared code

**Type:** DEFAULT | **Origin:** ARCHITECTURAL DECISION | **Applies:** modular codebases

Modules SHOULD communicate through explicit interfaces and avoid unnecessary dependency cycles. Build-time cycles and runtime conversations differ. Shared code SHOULD have cohesive responsibility and ownership; substantial shared domain kernels may be appropriate. Choose duplication or reuse by consistency needs and change coupling, not line counts or folder names.

Examples: typed application functions, query ports, commands, events, actor messages, callbacks, streams, and plugin protocols. A feature may contain domain logic, adapters, presentation, tests, and documentation without needing every category. An event bus can conceal coupling and does not by itself prove modularity.

<a id="ai-2"></a>
### 16.2. AI-2 — Enforced tool contracts

**Type:** CONDITIONAL | **Origin:** DERIVED ENGINEERING RULE | **Applies:** AI tools, skills, plugins, and capability adapters

A natural-language skill or tool description is not a security boundary. Enforced boundaries MUST provide appropriate validation, authorization, scope restrictions, resource limits, effect constraints, output handling, and relevant accountability. Critical enforceable permissions/integrity rules MUST NOT depend solely on prompt obedience.

Machine-readable contracts SHOULD be used where useful for enforcement or interoperability; JSON Schema/OpenAPI are options, not universal requirements. Structured returns SHOULD expose actionable results and uncertainty; they do not make AI deterministic. Schema-valid intent can still be harmful, requiring semantic policy and effect limits.

<a id="s48"></a>
## 48. Trusted AI entry and bounded navigation

<a id="workspace-ai-1"></a>
### 48.1. WORKSPACE-AI-1 — One discoverable primary application Skill

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** AI-accessible applications with retained-user-data workspaces

<a id="ai-entry-contract"></a>
#### 48.1.1. Primary Skill navigation and operation contract

Expose one clearly named discoverable primary trusted application Skill, for example `Menemora/SKILL.md`. It MUST explain application purpose, approved workspace location/discovery, entry point, folders, record discovery, bounded retrieval, schema/revision interpretation, edit requests, source-data versus instruction boundaries, approval requirements, enforced permissions, error/ambiguity handling, change verification, objects never directly modified, and reporting of uncertain/blocked outcomes. It MAY route to justified bounded subordinate Skills/documentation; one primary entry does not prohibit specialized expertise.

<a id="ai-entry-trust"></a>
#### 48.1.2. Trusted registration and enforced permissions

Trust and invocation MUST follow [SKILL-1](../0-%20Start%20Here%20and%20Universal%20Rules/006-%20Global%20Skills%20and%20Always-On%20Rules.md#skill-1)–[SKILL-3](../7-%20Attacking%20and%20Freezing%20the%20Master%20Plan/706-%20Checking%20Skills%20Dependencies%20and%20Conflicts.md#skill-3). An editable workspace file, including a file named SKILL.md, cannot authenticate itself or elevate authority. Trusted registration/revision and enforced permission boundaries remain separate from its text. AI application operations MUST use approved permission-enforced application interfaces; the Skill alone grants no direct filesystem mutation, credential access, deletion, production or other elevated authority. Existing separately delegated coding/scratch capabilities remain scoped under [AI-1](406-%20Planning%20Security%20and%20Permissions.md#ai-1) and do not bypass runtime data protections. Human workspace documentation MUST remain usable without the Skill.

