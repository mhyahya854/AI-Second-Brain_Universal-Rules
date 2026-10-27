<a id="dev-11"></a>
### 31.11. DEV-11 — Full-build small-model continuity and safe resumption

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** application plans, phase execution, and AI-assisted continuation

Plans and repositories MUST be designed so that a sufficiently capable small local model can build the entire application phase by phase using APP Plan and Codebase, without hidden conversation history or continuous rescue by a stronger model. Shift complexity into specifications, contracts, examples, indexes, tests, acceptance criteria, deterministic tooling, and explicit Project State. Strong planning captures architectural reasoning ahead of time; weaker execution remains bounded. This is a full-build design target, not merely the ability to continue one task and not a claim that any model or parameter count can complete every application.

Every phase MUST support zero-conversation resumption: locate Project State; establish completion and active phase; read the specification; locate implementation; understand the required outcome; make authorized safe changes; run validation; record results; determine completion; and proceed only where permitted by the phase gate. Local execution is the baseline design target; a suitable cloud model may follow the same artifacts, but provider/location alone does not establish capability and continued cloud access is not required.

**A weaker model is allowed to do less, but not to invent more.** If required information is missing, contradictory, or cannot be safely established, the executor MUST stop affected work and record the precise blocker and needed resolution. It MUST NOT invent architecture, silently reinterpret the Master Plan, claim unperformed validation, expand authority, or bypass [AI-1](#ai-1), [AI-3](#ai-3), or [AUTH-1](#auth-1). Full-build continuity does not grant unrestricted autonomous execution; it supplies the information needed to execute authorized work safely.

This **product-development** goal concerns building/continuing software from APP Plan, phases, Project State, tests, and Codebase. The separate **product-use** goal under [HERMES-2](#hermes-2) concerns navigating and using supported application tools through structured, bounded retrieval. Both apply where relevant; satisfying either one does not prove the other.

The owner’s measurable development-execution target includes approximately 4B-class models under [EXEC-6](#exec-6). This is distinct from the approximately 1B product-use retrieval target in HERMES-2, and neither parameter count guarantees success.

