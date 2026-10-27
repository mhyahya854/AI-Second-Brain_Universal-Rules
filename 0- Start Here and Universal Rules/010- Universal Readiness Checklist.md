<a id="s29"></a>
## 29. Anti-pattern index — non-normative

This navigation index adds no requirements. Applicability, strength, and exceptions remain those of the governing clauses.

| Warning sign | Governing clause |
|---|---|
| Accepted/uncertain operation reported as known final completion | [OUT-1](#out-1) |
| UI controls or prompts treated as effective permission enforcement | [AUTH-1](#auth-1), [AI-2](#ai-2) |
| Untrusted content grants AI new authority | [AI-1](#ai-1) |
| Read-only label or record count used as complete risk model | [AI-3](#ai-3) |
| Expendable cache holds the only copy promised preservation | [DATA-1](#data-1) |
| Generated artifact assumed disposable or exactly reproducible | [DATA-2](#data-2) |
| Application replacement accidentally deletes retained data | [LIFE-1](#life-1) |
| One write algorithm prescribed without backend failure semantics | [STORE-1](#store-1) |
| WAL, hashes, or unfenced leases treated as sufficient NAS safety | [NAS-2](#nas-2), [CON-1](#con-1) |
| Docker or backup-only support presented as all NAS modes | [NAS-1](#nas-1) |
| Required evidence written independently after mutation commit | [AUDIT-2](#audit-2) |
| Attacker-rewritable manifest presented as protected anchor | [AUDIT-3](#audit-3) |
| Permanent sensitive retention justified only by auditability | [PRIV-1](#priv-1) |
| Migration failure blindly restores over newer work | [MIGRATE-1](#migrate-1) |
| Unknown persistent semantics accepted then destroyed | [MIGRATE-2](#migrate-2) |
| Recovery claimed without restoration evidence | [BACKUP-2](#backup-2) |
| Loopback or VPN treated as complete authorization | [SEC-1](#sec-1) |
| Invariants bypassed or distribution introduced without rationale | [ARCH-1](#arch-1), [ARCH-2](#arch-2) |
| Unjustified non-Rust implementation | [LANG-1](#lang-1) |
| Unsupported or untested targets presented as verified | [TEST-1](#test-1), [PORT-1](#port-1) |

