<a id="s09"></a>
## 9. Local and offline operation

<a id="offline-1"></a>
### 9.1. OFFLINE-1 — Useful local operation by policy

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** capability design and network dependencies

Applications SHOULD maximize useful local operation where the domain permits it. They MUST define offline behavior per capability and avoid unrelated cloud dependencies disabling otherwise independent local access. Intentional departures need technical justification under [GOV-3](../0-%20Start%20Here%20and%20Universal%20Rules/003-%20Rule%20Priority%20and%20Authority.md#gov-3).

Search services, email delivery, streaming, live collaboration, market access, and other remote-native capabilities may need connectivity. Intrinsic documented dependence is not a policy exception. Preserve useful drafts, cached content, or inspection where appropriate; do not imply uncached or remotely authoritative information is current or available.

Independent local capabilities and honest cached/pending states are distinguished from prohibited failure substitutions in [NOFALL-2](../0-%20Start%20Here%20and%20Universal%20Rules/002-%20The%20Universal%20Constitution.md#nofall-2).

<a id="offline-2"></a>
### 9.2. OFFLINE-2 — Safe delayed execution

**Type:** CONDITIONAL | **Origin:** DERIVED ENGINEERING RULE | **Applies:** queued or offline operations

Queueing MUST have domain-safe freshness, expiry, cancellation, authorization, replay, and conflict semantics. Time-sensitive orders, physical commands, or door-unlock actions MUST NOT replay automatically merely because connectivity returns. A domain may reject offline writes, allocate rights in advance, or restrict operations to preserve shared invariants. Distinguish queued intent from completed remote action under [OUT-1](../0-%20Start%20Here%20and%20Universal%20Rules/009-%20Evidence%20and%20Truthful%20Completion.md#out-1).

<a id="offline-3"></a>
### 9.3. OFFLINE-3 — Device-local personal operation

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** personal applications with ordinary local capabilities

Each applicable personal application MUST remain usable locally on its supported devices. A permanent NAS, cloud service, or Internet connection MUST NOT be required for ordinary local capabilities unless the capability itself is inherently remote. Devices MAY maintain appropriate local working copies; loss of connectivity MUST NOT unnecessarily remove ordinary local functionality or access to locally held user data. Products MUST describe what is retained locally, what is available offline, and which operations require remote coordination. An appropriate working copy need not contain an entire huge media collection. Offline changes and reconnection remain subject to [OFFLINE-2](#offline-2) and [SYNC-1](../12-%20Connecting%20and%20Completing%20the%20Application/1206-%20Integrating%20Offline%20and%20Sync%20Capabilities.md#sync-1).

<a id="s11"></a>
## 11. NAS support

<a id="nas-1"></a>
### 11.1. NAS-1 — Mandatory ecosystem support policy

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** relevant hosting, storage, file-access, service-client, and backup roles

NAS support is intentional. Applicable applications MUST identify and support NAS modes needed for their intended workflow, documenting configurations, concurrency assumptions, disconnection semantics, recovery, and tested guarantees. They MUST NOT silently assume only fast local disks. Supporting one mode does not imply the others.

| Mode | Meaning | Scope of support claim |
|---|---|---|
| 1 — NAS/server hosted | Application runs on a NAS/private server using server-local storage. | Runtime, storage, permissions, resources, and lifecycle. |
| 2 — NAS-hosted service client | Client communicates with an application/database/service on NAS. | Protocol, identity, versions, timeouts, cancellation, retries, and outcomes. |
| 3 — User files on a share | Ordinary documents/media/files accessed through network storage. | File operations, identity, caching, concurrency, disconnection, recovery. |
| 4 — Transactional database over a share | Database files opened directly across SMB/NFS or equivalent. | Engine-supported configuration and verified assumptions under [NAS-2](#nas-2). |
| 5 — Backup destination | NAS holds recovery artifacts. | Consistent capture, transfer, restore, keys, access, and failure-domain limits. |

All five modes are not required. Backup-only support MUST NOT be presented as active shared-data support. A service-mediated design can satisfy active NAS use without shared raw database files. Software with no relevant role may document non-applicability; applicable software omitting NAS support needs an approved exception. Docker is neither necessary nor sufficient for NAS compatibility.

A NAS synchronization hub is a topology role under [SYNC-3](../12-%20Connecting%20and%20Completing%20the%20Application/1206-%20Integrating%20Offline%20and%20Sync%20Capabilities.md#sync-3), not an assertion of raw database access or a sixth interchangeable storage mode. Products MUST distinguish NAS as sync hub, storage service, backup destination, and application/service host. A deployment may combine these roles, but each role retains its own contract; synchronization alone is not a backup.

For important retained data, NAS-hub compromise MUST be included in the recovery risk assessment under [BACKUP-1](../16-%20Maintaining%20Updating%20and%20Recovering/1606-%20Testing%20Backup%20and%20Restoration.md#backup-1). Consider protected snapshots/version history, separately protected backup, or another independent recovery mechanism so the hub does not unnecessarily become a single point whose compromise destroys every historical copy. Ordinary sync clients SHOULD NOT require unrestricted NAS administrator authority; [SEC-1](../7-%20Attacking%20and%20Freezing%20the%20Master%20Plan/703-%20Finding%20Security%20and%20Privacy%20Risks.md#sec-1) governs least privilege.

<a id="nas-2"></a>
### 11.2. NAS-2 — Configuration-specific evidence

**Type:** CONDITIONAL | **Origin:** DERIVED ENGINEERING RULE | **Applies:** claimed NAS modes and network storage

Claims MUST identify engine, protocol, client/server, filesystem, and configuration assumptions with proportionate empirical evidence. Mode 4 MUST be supported only where the engine explicitly supports that configuration and the application's assumptions have been verified. Unsupported configurations MUST be rejected or clearly reported as unsupported, rather than silently accepted as safe.

SMB/NFS locking is configuration- and failure-dependent. Ordinary multi-process SQLite WAL coordination commonly relies on shared coordination mechanisms; shared-memory coordination does not describe every possible WAL configuration. This does not establish safe multi-host SQLite database access over SMB/NFS. Specialized configurations, including custom VFS behavior, require their own supported contract and evidence under Mode 4. A NAS-local database service is a different mode.

`fsync` and `FlushFileBuffers` offer the guarantees implemented by the complete storage stack; server acknowledgements, caches, hardware, and error propagation matter. Oplocks do not alone define stable-storage durability. Permissions depend on identities/ACLs; `0755` and `0644` are not universal privacy settings. Latency assumptions MUST be measured or bounded for the claimed workload, not copied from fixed illustrative numbers.

Access, quota, and free-space preflights improve diagnostics but cannot prove a future operation succeeds. Disconnects may leave outcomes unknown under [OUT-1](../0-%20Start%20Here%20and%20Universal%20Rules/009-%20Evidence%20and%20Truthful%20Completion.md#out-1). Timestamp leases and heartbeats without stale-writer exclusion cannot establish safe overlapping access; coordination follows [CON-1](../10-%20Building%20the%20Core%20and%20Backend/1005-%20Implementing%20Transactions%20and%20Migrations.md#con-1).

Possible patterns include NAS-local database services, supported transactional engines, ordinary files with bounded semantics, or immutable chunks with a publication protocol. Chunking is not mandatory and does not itself create a transaction.

