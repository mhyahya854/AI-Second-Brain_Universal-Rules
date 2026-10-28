<a id="s14"></a>
## 14. Operation outcomes and acknowledgements

<a id="out-1"></a>
### 14.1. OUT-1 — Report what is actually known

**Type:** UNIVERSAL INVARIANT | **Origin:** DERIVED ENGINEERING RULE | **Applies:** important local and external operation results

Results MUST distinguish relevant states: rejection, acceptance, queued intent, local application, local durable commit, remote acknowledgement, external completion, failure before execution, partial execution, or unknown outcome. Exact labels are optional. Acceptance MUST NOT imply completion; remote acknowledgement MUST NOT imply stronger durability/finality than its contract provides.

A timeout, crash, or NAS disconnect can leave success indeterminate. Applications MUST report uncertainty, retain suitable recovery correlation, and reconcile or use a demonstrably safe retry policy. Missing acknowledgement alone MUST NOT be reported as proof of failure. Relevant callers, including AI, need the actual durability/completion boundary.

Example result fields: operation ID, known phase, affected resources, durability scope, external correlation, uncertainty, and allowed next actions. A small utility may convey these semantics through exit status and a concise message.

<a id="evid-1"></a>
### 17.4. EVID-1 — Provenance, evidence status, and uncertainty

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** imported/observed information and research whose provenance or evidence strength materially affects decisions or meaning

Relevant provenance MUST be retained proportionately: source/identifier/version, acquisition or import method, observation time, importer/tool, human modification, and verification scope where meaningful. Successful import, a credible source, or canonical designation MUST NOT silently upgrade an observation into verified factual truth; [DATA-1](../10-%20Building%20the%20Core%20and%20Backend/1001-%20Implementing%20Shared%20Data%20Types.md#data-1) keeps those dimensions distinct.

Applications and planning records MUST represent evidence strength equivalent to **VERIFIED**, **INFERRED / CONDITIONAL**, and **UNKNOWN** where it affects decisions. Verification identifies its actual scope and supporting evidence. Research, compatibility, external integrations, migrations, planning assumptions, and source observations MUST NOT become architectural facts through repetition alone. Meaningful uncertainty MUST remain representable, including known, unknown, unavailable, ambiguous, unverified, stale, conflicting, and pending-review states as applicable; one universal enumeration is not required. This complements operation uncertainty under [OUT-1](#out-1).

When credible sources conflict, preserve sufficient competing evidence, provenance, uncertainty, and review state rather than silently choosing a winner. Automatic resolution requires an explicit deterministic, justified rule; otherwise retain an unresolved interpretation or obtain authorized review. Evidence retention is purpose-limited under [PRIV-1](../6-%20Writing%20the%20Complete%20Master%20Plan/606-%20Documenting%20Data%20Security%20and%20Recovery.md#priv-1), not a mandate to keep all original sensitive payloads forever.

An upstream source changing or deleting its copy MUST NOT automatically destroy locally retained evidence or user data. Represent removed-upstream, unavailable, superseded/new-version, stale, or tombstone status as appropriate. Actual deletion follows the applicable retention, privacy, authority, and synchronization contract; legitimate erasure and agreed deletion propagation remain enforceable.

