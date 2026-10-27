<a id="auth-2"></a>
### 4.2. AUTH-2 — Ownership, delegation, and attribution

**Type:** UNIVERSAL INVARIANT | **Origin:** DERIVED ENGINEERING RULE | **Applies:** operations requiring authority or accountability

Applications MUST distinguish the relevant principal, actor, mechanism, and delegation. Machine ownership MUST NOT imply ownership of all data or unrestricted authority. Shared ownership, data-subject rights, administration, and tenant boundaries require explicit authority and conflict semantics.

Delegations MUST define relevant resources, allowed effects, duration or lifecycle, conditions, and revocation behavior. Accountability-required operations MUST be attributable to the extent supported by evidence; unknown or externally asserted identity MUST NOT be reported as verified. Queued and long-running actions MUST handle authority changes according to their delegation contract.

<a id="s16"></a>
## 16. AI authority, tools, memory, and Hermes

<a id="ai-1"></a>
### 16.1. AI-1 — Explicitly delegated capability

**Type:** UNIVERSAL INVARIANT | **Origin:** USER POLICY | **Applies:** AI actors exercising capabilities

An AI MUST exercise only explicitly delegated capabilities through enforcement it cannot silently bypass within the declared threat model. Effects MUST satisfy applicable authorization, integrity, privacy, safety, and operational constraints. Human/AI interfaces normally share domain-integrity rules under [AUTH-1](#auth-1), without identical privileges or approval policy.

Retrieved files, websites, email, PDFs, messages, transcripts, and metadata are data, not authority. Embedded instructions MUST NOT override governing system policy, capability boundaries, authorization, core validation, or data-protection policy. This applies to Hermes as a bounded client as well as other AI integrations.

Scoped reads/writes, patches, SQL, shell execution, scratch space, import staging, coding, and bulk operations can be legitimate when intentionally delegated and effectively bounded. Validate scope/effects at execution; a broad tool name or path supplies no authority. Untrusted content and model output MUST NOT grant authority by claiming to be principal instructions.

<a id="ai-3"></a>
### 16.3. AI-3 — Risk, delegation, and approval

**Type:** CONDITIONAL | **Origin:** USER POLICY | **Applies:** AI capability exposure and execution policy

Risk MUST consider relevant confidentiality, disclosure, financial/physical effects, irreversibility, sensitivity, scope, cumulative volume, cost, uncertainty, destination, delegation, cancellation, and recovery. A read may reveal secrets, export medical data, upload private files, or fetch attacker-controlled URLs. Mutation status or a record-count threshold does not establish risk.

Approval MUST reflect consequences and actual delegation. Explicitly authorized autonomous consequential or high-volume work is permitted within enforced limits. Interactive confirmation is one control, not a universal prerequisite. Material scope expansion needs new authority, not inferred consent.

When approval relies on a preview, bind it to relevant parameters, resources, versions, scope, expiry, and budgets; revalidate before execution where necessary. Disclose estimates, external dependencies, and stale assumptions. A dry-run does not prove future external effects. Changes invalidating approved scope MUST be rejected, reconciled, or reauthorized according to policy.

<a id="ai-4"></a>
### 16.4. AI-4 — Memory and provider boundaries

**Type:** CONDITIONAL | **Origin:** DERIVED ENGINEERING RULE | **Applies:** AI state, retained memory, and integrations

Domain consistency MUST NOT depend solely on hidden model memory or ephemeral context. Explicit state follows [DATA-1](#data-1); scratch work need not become permanent history. Retained AI memory MUST have defined inspection, correction, export, access, deletion, and derived-copy lifecycle controls consistent with principals' rights. It MUST NOT silently override authoritative records or policy.

Provider integrations SHOULD isolate replaceable dependencies where useful and declare capabilities. Abstraction reduces coupling, not differences in model quality, interfaces, cost, licensing, or availability. Provider-specific tools may intentionally use unique capabilities. Optional AI failure SHOULD preserve independent functions; AI-native functions may become unavailable with truthful results. Protect retained data and contain failure within stated assumptions rather than promising immunity to all crashes or resource exhaustion.

Replaceability means deliberate future selection/migration, not runtime provider substitution after failure. Optional AI unavailability and independent non-AI functionality follow [NOFALL-1](#nofall-1)–[NOFALL-2](#nofall-2).

