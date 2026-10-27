<a id="dev-17"></a>
### 31.17. DEV-17 — Emergency maintenance and reconciliation

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** urgent maintenance where delay materially increases security, data-loss, privacy, safety, or unrecoverable operational risk

Emergency maintenance MAY precede complete normal planning when necessary under [SAFE-2](#safe-2). Bound work to the minimum necessary containment, mitigation, repair, urgency-appropriate validation, and preservation of change evidence. Defer only planning or routine approval steps that cannot practicably precede containment, using actual applicable emergency authority or prior delegation under [AUTH-2](#auth-2) and [GOV-3](#gov-3). Emergency status does not manufacture permission, waive integrity/privacy boundaries, or authorize ordinary feature development. Routine bugfixes do not automatically invoke this procedure.

Maintain a proportionate durable record of trigger, scope, authorization, affected components, actual change, validation, residual risks, and temporarily deferred requirements. Link it from Project State under [DEV-9](#dev-9) so an interrupted session can resume safely. A small urgent patch needs concise evidence, not a parallel paperwork system. [DEV-11](#dev-11) still prohibits guessing missing facts or inventing architecture; choose only safely established, authorized actions and record blockers for the rest.

Before ordinary feature development resumes after a material emergency change, reconcile the applicable Master Plan, Project State, Decisions, phase/execution history, tests, architecture, compatibility expectations, migration implications, and documentation. Establish or update the repair's phase contract and run the applicable [Three-Layer Conformance Gate](#dev-13); deferred required checks are not passes. Outstanding failures require repair or an actually approved scoped exception under [GOV-3](#gov-3), not silent permanent drift. Emergency repair may temporarily precede complete planning; it MUST NOT permanently bypass project truth or mark an unverified phase complete.

