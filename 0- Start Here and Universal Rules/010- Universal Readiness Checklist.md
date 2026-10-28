<a id="s29"></a>
## 29. Anti-pattern index — non-normative

This navigation index adds no requirements. Applicability, strength, and exceptions remain those of the governing clauses.

| Warning sign | Governing clause |
|---|---|
| Accepted/uncertain operation reported as known final completion | [OUT-1](009-%20Evidence%20and%20Truthful%20Completion.md#out-1) |
| UI controls or prompts treated as effective permission enforcement | [AUTH-1](../10-%20Building%20the%20Core%20and%20Backend/1007-%20Implementing%20Security%20and%20Authorization.md#auth-1), [AI-2](../4-%20Planning%20the%20Architecture%20and%20Data/404-%20Defining%20APIs%20and%20Interfaces.md#ai-2) |
| Untrusted content grants AI new authority | [AI-1](../4-%20Planning%20the%20Architecture%20and%20Data/406-%20Planning%20Security%20and%20Permissions.md#ai-1) |
| Read-only label or record count used as complete risk model | [AI-3](../4-%20Planning%20the%20Architecture%20and%20Data/406-%20Planning%20Security%20and%20Permissions.md#ai-3) |
| Expendable cache holds the only copy promised preservation | [DATA-1](../10-%20Building%20the%20Core%20and%20Backend/1001-%20Implementing%20Shared%20Data%20Types.md#data-1) |
| Generated artifact assumed disposable or exactly reproducible | [DATA-2](../10-%20Building%20the%20Core%20and%20Backend/1001-%20Implementing%20Shared%20Data%20Types.md#data-2) |
| Application replacement accidentally deletes retained data | [LIFE-1](../4-%20Planning%20the%20Architecture%20and%20Data/408-%20Planning%20Backup%20Migration%20and%20Recovery.md#life-1) |
| One write algorithm prescribed without backend failure semantics | [STORE-1](../10-%20Building%20the%20Core%20and%20Backend/1004-%20Implementing%20Storage%20and%20Persistence.md#store-1) |
| WAL, hashes, or unfenced leases treated as sufficient NAS safety | [NAS-2](../4-%20Planning%20the%20Architecture%20and%20Data/407-%20Planning%20Offline%20and%20Sync%20Behavior.md#nas-2), [CON-1](../10-%20Building%20the%20Core%20and%20Backend/1005-%20Implementing%20Transactions%20and%20Migrations.md#con-1) |
| Docker or backup-only support presented as all NAS modes | [NAS-1](../4-%20Planning%20the%20Architecture%20and%20Data/407-%20Planning%20Offline%20and%20Sync%20Behavior.md#nas-1) |
| Required evidence written independently after mutation commit | [AUDIT-2](../10-%20Building%20the%20Core%20and%20Backend/1005-%20Implementing%20Transactions%20and%20Migrations.md#audit-2) |
| Attacker-rewritable manifest presented as protected anchor | [AUDIT-3](../14-%20Reviewing%20the%20Entire%20Application/1405-%20Reviewing%20Security%20and%20Data%20Safety.md#audit-3) |
| Permanent sensitive retention justified only by auditability | [PRIV-1](../6-%20Writing%20the%20Complete%20Master%20Plan/606-%20Documenting%20Data%20Security%20and%20Recovery.md#priv-1) |
| Migration failure blindly restores over newer work | [MIGRATE-1](../16-%20Maintaining%20Updating%20and%20Recovering/1605-%20Managing%20Data%20and%20Schema%20Migrations.md#migrate-1) |
| Unknown persistent semantics accepted then destroyed | [MIGRATE-2](../16-%20Maintaining%20Updating%20and%20Recovering/1605-%20Managing%20Data%20and%20Schema%20Migrations.md#migrate-2) |
| Recovery claimed without restoration evidence | [BACKUP-2](../16-%20Maintaining%20Updating%20and%20Recovering/1606-%20Testing%20Backup%20and%20Restoration.md#backup-2) |
| Loopback or VPN treated as complete authorization | [SEC-1](../7-%20Attacking%20and%20Freezing%20the%20Master%20Plan/703-%20Finding%20Security%20and%20Privacy%20Risks.md#sec-1) |
| Invariants bypassed or distribution introduced without rationale | [ARCH-1](../4-%20Planning%20the%20Architecture%20and%20Data/402-%20Dividing%20the%20Application%20Into%20Features.md#arch-1), [ARCH-2](../4-%20Planning%20the%20Architecture%20and%20Data/401-%20Designing%20the%20Application%20Architecture.md#arch-2) |
| Unjustified non-Rust implementation | [LANG-1](../3-%20Deciding%20the%20Stack/303-%20Choosing%20Programming%20Languages.md#lang-1) |
| Unsupported or untested targets presented as verified | [TEST-1](../13-%20Testing%20Debugging%20and%20Repairing/1301-%20Preparing%20the%20Complete%20Test%20Environment.md#test-1), [PORT-1](../3-%20Deciding%20the%20Stack/308-%20Checking%20Compatibility%20and%20Portability.md#port-1) |

