<a id="s22"></a>
## 22. Backup and restoration

<a id="backup-1"></a>
### 22.1. BACKUP-1 — Complete recovery dependency set

**Type:** CONDITIONAL | **Origin:** DERIVED ENGINEERING RULE | **Applies:** retained state with provided/claimed backup or recovery

Strategies MUST identify a consistent recovery point and complete dependency set for the promised result: potentially data, configuration, keys/key-recovery paths, audit evidence, schemas, readers, migration metadata, expensive derived artifacts, and external dependencies. Secrets need protection and recoverability, not indiscriminate packaging with public exports.

No directory inclusion list or derived-data exclusion applies universally. NAS/filesystem snapshots, OS backup, database-native, or application-native backup may be used. Understand snapshot scope and cross-store consistency. A copy in the same failure domain does not establish independent recovery.

For important retained data, the strategy MUST distinguish active copies, synchronized replicas, NAS hubs, snapshot/version history, and optional independently placed complete backups, and consider recovery copies not simultaneously destroyable through the same ordinary client credentials or failure mechanism. An individual workspace user MAY explicitly disable Complete On-Site Backup under [section 53](../4-%20Planning%20the%20Architecture%20and%20Data/408-%20Planning%20Backup%20Migration%20and%20Recovery.md#s53); when OFF, document loss-of-drive exposure and never imply an independent backup is present. Document the chosen protection and residual risk proportionately. Immutable/write-protected history, offline/disconnected media, separately credentialed storage, append/versioned backup, or another justified isolation mechanism may fit; no topology is universally required. Ordinary client credentials SHOULD NOT automatically have unrestricted deletion authority over all independent backup generations unless genuinely required; separate retention/deletion authority where meaningful. Isolation does not override authorized erasure under [PRIV-1](../6-%20Writing%20the%20Complete%20Master%20Plan/606-%20Documenting%20Data%20Security%20and%20Recovery.md#priv-1).

<a id="backup-2"></a>
### 22.2. BACKUP-2 — Recovery evidence

**Type:** CONDITIONAL | **Origin:** DERIVED ENGINEERING RULE | **Applies:** backup-readiness and recoverability claims

Claims MUST have documented, testable restoration and supporting evidence. Verify intended results, keys/dependencies, compatibility, and meaningful failure cases. Untested backups are unverified, not necessarily empty or legally nonexistent. State recovery-point/time expectations and untested limits.

Manifests/checksums can detect accidental corruption; adversaries may require protected evidence under [AUDIT-3](../14-%20Reviewing%20the%20Entire%20Application/1405-%20Reviewing%20Security%20and%20Data%20Safety.md#audit-3). Verification SHOULD avoid active-data changes and restore tests SHOULD use safe destinations. Actual restore requires authority and accounting for later work/deletion policy.

For important retained data, restoration or equivalent recoverability MUST be validated at a proportionate cadence defined in the App Plan. A successful backup write alone is insufficient. Test/sample restores, isolated rehearsals, integrity/dependency verification, or another justified method must support the actual recovery claim; checksums alone do not establish that an application can use the restored state. Assess possible corruption, malicious content, and already-compromised backup state, using evidence to select the best available known-good recovery point and preserving uncertainty when cleanliness cannot be established. Older or immutable does not automatically mean clean; [RECOVER-1](../12-%20Connecting%20and%20Completing%20the%20Application/1207-%20Integrating%20Error%20and%20Recovery%20Behavior.md#recover-1) governs safe recovery.

<a id="survive-2"></a>
### 36.2. SURVIVE-2 — Mobile uninstall and disappearance rehearsal

**Type:** CONDITIONAL | **Origin:** USER POLICY | **Applies:** applications retaining user information, including platforms with disposable app containers

The App Plan MUST identify which storage and keys the supported operating system may remove on uninstall, reset, account loss, or device failure. App-private mobile storage MUST NOT be the sole claimed independent representation. Select a platform-supported, authorized preservation route outside that disposable state, such as user-controlled files or independently maintained storage/service copies, with documented access and restoration procedures. Do not assume an uninstall hook, shared-folder name, OS backup setting, export format, or removable app key proves survival. If the required route cannot be established, report the unmet preservation requirement and stop claiming the platform configuration satisfies it; resolve the product/storage contract through planning.

Validate an actual app-disappearance scenario using representative retained information: make the original app/runtime unavailable in an isolated test environment, obtain the independent representation and required keys/schema, recover with documented independent means, and verify meaning, relationships, identifiers, and the declared recovery point. Relevant mobile claims require evidence for actual supported uninstall/container behavior rather than desktop extrapolation. Do not delete the owner's live data to run this rehearsal.

[RECOVER-1](../12-%20Connecting%20and%20Completing%20the%20Application/1207-%20Integrating%20Error%20and%20Recovery%20Behavior.md#recover-1), [BACKUP-1](#backup-1), and [BACKUP-2](#backup-2) continue to require complete dependencies, independently appropriate failure domains, and restoration evidence. External location or synchronization alone is not backup safety. `Codebase/Database/` contains implementation artifacts such as schemas, migrations, queries, and storage code/configuration; it is not automatically the location of private user data. Keep private data out of source repositories unless specifically authorized and appropriate under privacy policy.

