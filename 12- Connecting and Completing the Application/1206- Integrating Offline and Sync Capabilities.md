<a id="s20"></a>
## 20. Synchronization

<a id="sync-1"></a>
### 20.1. SYNC-1 — Explicit distributed authority

**Type:** CONDITIONAL | **Origin:** DERIVED ENGINEERING RULE | **Applies:** synchronization or replicas of a logical dataset

Protocols MUST define authority, identity, causal/conflict semantics, disconnected changes, duplicate handling, deletion propagation, and recovery. Peer data MUST pass applicable authority/integrity controls; sync is not a bypass. Preserve origin and propagation identity where needed for accountability.

Offline availability is constrained by invariants: scarce resources may need online coordination or preallocated rights. Convergence is not proof of correctness. Tombstone retention, long-offline replicas, and reintroduction of erased information need explicit lifecycle semantics. Conflicts follow [CON-2](../10-%20Building%20the%20Core%20and%20Backend/1005-%20Implementing%20Transactions%20and%20Migrations.md#con-2); delay follows [OFFLINE-2](../4-%20Planning%20the%20Architecture%20and%20Data/407-%20Planning%20Offline%20and%20Sync%20Behavior.md#offline-2).

Applications synchronizing large retained datasets MUST define a risk-based policy for destructive or anomalous bulk-change propagation; a locally observed change is not automatically legitimate user intent. Consider mass rewrites, renames/deletions, unexpected encrypted/high-entropy replacements, unexplained bursts, and broad schema-invalidating changes where relevant. These signals are not proof of malware. Proportionate responses may pause propagation, stage/quarantine, reconcile, preserve permitted prior versions, or alert; no universal numeric threshold or fresh prompt for every bulk operation is required.

Where suspected compromise could propagate damage, the system MUST provide an appropriate containment route, such as sync pause, device revocation, replica isolation, read-only operation, connector disablement, or staged-import quarantine. Resume automatic propagation only after applicable validation/reconciliation under [RECOVER-1](1207-%20Integrating%20Error%20and%20Recovery%20Behavior.md#recover-1). Authorized bulk work and legitimate deletion/erasure remain supported under [AUTH-2](../4-%20Planning%20the%20Architecture%20and%20Data/406-%20Planning%20Security%20and%20Permissions.md#auth-2) and [PRIV-1](../6-%20Writing%20the%20Complete%20Master%20Plan/606-%20Documenting%20Data%20Security%20and%20Recovery.md#priv-1); containment is not indefinite retention authority.

<a id="sync-2"></a>
### 20.2. SYNC-2 — Device continuity without a NAS

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** personal products requiring cross-device continuity

Without a NAS, supported laptops, desktops, phones, and tablets MUST retain applicable local operation under [OFFLINE-3](../4-%20Planning%20the%20Architecture%20and%20Data/407-%20Planning%20Offline%20and%20Sync%20Behavior.md#offline-3). Such products MUST support direct device synchronization or another explicitly selected local-first synchronization mechanism, for example Phone ↔ Laptop or Phone ↔ Laptop ↔ Tablet. A permanent central cloud server MUST NOT be required merely to synchronize the user's own devices. Optional selected intermediaries remain subject to declared dependencies, privacy, and authorization. Conflicts, offline changes, unknown outcomes, integrity, retries, and recovery follow [SYNC-1](#sync-1), [OUT-1](../0-%20Start%20Here%20and%20Universal%20Rules/009-%20Evidence%20and%20Truthful%20Completion.md#out-1), and [RETRY-1](../10-%20Building%20the%20Core%20and%20Backend/1006-%20Implementing%20APIs%20and%20Services.md#retry-1).

<a id="sync-3"></a>
### 20.3. SYNC-3 — Opt-in NAS synchronization hub

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** applicable personal products with a suitable NAS enabled by the user for shared synchronization

When a suitable NAS is available and the user enables this role, it MUST become the primary shared synchronization hub for application data. All applicable retained/shared data SHOULD synchronize to it according to the declared data scope, permissions, retention, and synchronization contract. Desktop, mobile, and tablet instances act as clients of that shared system while retaining appropriate local working copies. This policy does not silently upload data excluded by user scope, authority, or privacy rules.

The NAS MUST NOT become a hard requirement for ordinary offline work. Temporary disconnection MUST preserve applicable local operation; reconnection MUST synchronize and reconcile according to the declared consistency model and current authority. Primary hub placement does not by itself transfer ownership or make every local write a globally final commit. This enabled-NAS hub policy remains active; it does not finalize a universal authoritative-copy topology or require every device to hold the complete workspace. The App Plan must settle actual write authority and placement under [JSON-4](../4-%20Planning%20the%20Architecture%20and%20Data/408-%20Planning%20Backup%20Migration%20and%20Recovery.md#json-4), without inferring a decision from the hub role. Distinguish local persistence, hub acknowledgement, and reconciliation under [OUT-1](../0-%20Start%20Here%20and%20Universal%20Rules/009-%20Evidence%20and%20Truthful%20Completion.md#out-1). NAS storage/service, backup, and hosting roles remain distinct under [NAS-1](../4-%20Planning%20the%20Architecture%20and%20Data/407-%20Planning%20Offline%20and%20Sync%20Behavior.md#nas-1).

<a id="sync-4"></a>
### 20.4. SYNC-4 — Safe topology transitions

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** applicable products transitioning between device-local/peer operation and a NAS synchronization hub

Products SHOULD support safe transitions between no-NAS local or peer operation and an enabled NAS hub. Adding a NAS MUST NOT require destructive migration or recreation of all user data. Removing or temporarily losing the NAS MUST NOT make the user's locally held data inaccessible. Appropriate working copies and documented availability still apply; a client cannot promise offline access to content it has never retained.

Authority transitions MUST define identity continuity, reconciliation of concurrent/offline changes, deletion handling, pending or unknown operations, and which participants may accept changes during and after the transition. Removing a hub deliberately MUST provide a preservation/transfer path for retained data needed by the chosen replacement topology; failures MUST report remaining unavailable data truthfully. Existing synchronization, migration, recovery, and authorization contracts apply. These are outcome requirements, not a mandated peer protocol, conflict algorithm, or central-cloud dependency.

