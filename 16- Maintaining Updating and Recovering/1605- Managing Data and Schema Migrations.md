<a id="s24"></a>
## 24. Schema evolution and migrations

<a id="migrate-1"></a>
### 24.1. MIGRATE-1 — Versioned, recoverable evolution

**Type:** CONDITIONAL | **Origin:** DERIVED ENGINEERING RULE | **Applies:** persistent format/schema evolution

Migrations MUST be explicit, versioned, and testable with defined dependencies/order, preconditions, interruption, and recovery. Define exclusive versus online execution, compatibility windows, concurrent writers, rollback/roll-forward, snapshot role, restoration boundary, and failure classification. Resource preflights cannot prove future allocation succeeds.

Consistent snapshots/backups are useful safeguards; a local full copy is not required for every migration. Failure MUST NOT cause unconditional snapshot restoration. Determine whether rollback succeeded, work remains partial, newer writes exist, or forward recovery is needed. Restoration requires authority over the real loss boundary. Restricted/read-only operation may be appropriate during recovery.

Retry safety may come from idempotent steps or a correctly recorded execution protocol. Safe downgrade may be unavailable; do not invent a non-destructive `down()` when information has been lost.

<a id="migrate-2"></a>
### 24.2. MIGRATE-2 — Semantic compatibility

**Type:** CONDITIONAL | **Origin:** DERIVED ENGINEERING RULE | **Applies:** evolving persistent formats and protocols

Compatibility MUST be explicit. Unknown fields/new semantics MUST NOT be silently accepted then destroyed or misinterpreted. Define readable, preservable, transformable, and writable versions; reject unsafe writes or require supported migration. Liberal acceptance is not a blanket persistence rule. Tolerant reading may work when content is preserved safely and constraints remain understood.

An older application MUST NOT silently write or downgrade a newer data/workspace format it does not understand. If safe compatibility cannot be established, use a supported read-only, export-only, migration-required, or refusal mode as appropriate; do not offer even read/export behavior as faithful unless its contract can be met. Unknown newer fields MUST NOT be silently discarded.

