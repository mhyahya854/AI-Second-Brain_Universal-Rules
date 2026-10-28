<a id="s13"></a>
## 13. Concurrency and conflict semantics

<a id="con-1"></a>
### 13.1. CON-1 — Prevent invalid interleavings

**Type:** CONDITIONAL | **Origin:** DERIVED ENGINEERING RULE | **Applies:** state reachable by concurrent actors/processes

Applications MUST prevent invalid interleavings according to declared consistency semantics. Enforced single-writer access is permitted. Exclusive-access assumptions MUST be enforced or explicitly bounded; a convention alone is not exclusion.

MVCC, serialized services, transactions, optimistic concurrency, CRDTs, append protocols, and storage-enforced fencing are possible mechanisms. Version/hash checks MUST be coupled to transitions when used to prevent races; check-then-write is insufficient. Lease designs MUST prevent stale holders violating promised semantics through storage-enforced fencing or an equivalent protocol, not just heartbeats.

Lock scope/deadlines depend on engine and workload; relational writes do not universally need exclusive database locks. Define cancellation, timeout, and starvation behavior where material to correctness or availability.

<a id="con-2"></a>
### 13.2. CON-2 — Domain-appropriate conflict resolution

**Type:** CONDITIONAL | **Origin:** DERIVED ENGINEERING RULE | **Applies:** conflicting state changes

Resolution MUST preserve declared semantics and MUST NOT silently discard independently meaningful work contrary to them. Reject/retry, semantic merge, preserved alternatives, domain-approved last-writer-wins, or user decisions are options. A deterministic merge can still violate an invariant.

Lamport clocks order events consistently with causality but do not alone identify concurrency. Vector clocks track causal relationships under protocol assumptions. Hashes indicate content equality/difference, not independent causality. CRDTs provide specific convergence semantics, not arbitrary business-invariant preservation. These mechanisms are not interchangeable.

<a id="s17"></a>
## 17. Audit and provenance

<a id="audit-1"></a>
### 17.1. AUDIT-1 — Proportionate accountable evidence

**Type:** CONDITIONAL | **Origin:** DERIVED ENGINEERING RULE | **Applies:** operations requiring accountability under domain, policy, or applicable obligations

Applications MUST define required events and an audit contract covering granularity, principal/actor/mechanism, outcome, resources, necessary before/after information, retention, access, redaction, archival, deletion, integrity, and recovery. Evidence MUST support the claim without indiscriminate payload capture. Relevant failures/unknown outcomes MUST be distinguishable from successful effects.

Bulk events may reference an affected set; micro-events may be aggregated if accountability is retained. Model identities may be unknown/provider-reported. Human review records its actual scope. Prompts and free-text reasons need privacy treatment and are not mandatory permanent payloads. Rollback identifiers SHOULD be references rather than enduring bearer authority.

Diagnostics and audit evidence have distinct purposes/lifecycles, without mandatory separate directories. Ordinary correction/reversal should retain its relation to earlier events. Authorized expiry/redaction follows [PRIV-1](../6-%20Writing%20the%20Complete%20Master%20Plan/606-%20Documenting%20Data%20Security%20and%20Recovery.md#priv-1); append-only semantics do not forbid it.

<a id="audit-2"></a>
### 17.2. AUDIT-2 — Mutation and evidence commit consistency

**Type:** CONDITIONAL | **Origin:** DERIVED ENGINEERING RULE | **Applies:** evidence required for a committed mutation

Required evidence MUST be atomic, transactionally coupled, or recoverably linked with its committed effect. A crash window between unrelated writes MUST NOT be accepted as fulfilling that contract. Define recovery and how evidence-storage failure affects execution, including safety obligations under [SAFE-2](../0-%20Start%20Here%20and%20Universal%20Rules/002-%20The%20Universal%20Constitution.md#safe-2).

Non-normative local example:

```text
validate authority and preconditions
begin transaction
    apply canonical transition
    persist required audit event or recoverable outbox evidence
commit that consistency unit
report the outcome supported by the commit contract
deliver outbox evidence with retry-safe processing where applicable
```

An outbox does not atomically execute a physical or remote API effect. Durable intent, correlation, observed outcome, and reconciliation remain necessary, and outcomes can remain unknown. Recoverable evidence needs sufficient information for the actual obligation; a lossy queue marker is not sufficient by definition.

