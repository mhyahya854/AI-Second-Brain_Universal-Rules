<a id="ops-1"></a>
### 14.2. OPS-1 — Operation identity and recovery receipts

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** consequential operations whose retry, boundary crossing, crash survival, or uncertainty requires effect correlation

Such operations SHOULD use a stable operation identity or equivalent correlation mechanism to distinguish retrying the same intended operation from a genuinely new operation. Pure local reads with no meaningful side effects do not require idempotency keys. Where identity is used for idempotency, the complete protocol in [RETRY-1](#retry-1) applies; an ID alone does not prevent all duplicates.

When recovery requires knowing what happened, the application MUST maintain durable evidence appropriate to the operation. A receipt may contain operation ID, normalized request identity/hash, result, affected object IDs, commit/reconciliation state, verification evidence, timestamps, and relevant actor/principal. No one format or permanent payload-retention rule is required. Receipts MAY reuse existing audit or execution records rather than duplicate them; required mutation/evidence coupling follows [AUDIT-2](1005-%20Implementing%20Transactions%20and%20Migrations.md#audit-2) and privacy follows [PRIV-1](../6-%20Writing%20the%20Complete%20Master%20Plan/606-%20Documenting%20Data%20Security%20and%20Recovery.md#priv-1).

Receipts MUST distinguish observed results from unestablished external completion under [OUT-1](../0-%20Start%20Here%20and%20Universal%20Rules/009-%20Evidence%20and%20Truthful%20Completion.md#out-1). Recording intent or a local commit cannot prove that a remote or physical effect occurred. Unknown outcomes require reconciliation or a demonstrably safe retry policy, not blind replay after a lost acknowledgement.

<a id="s15"></a>
## 15. Retries and deduplication

<a id="retry-1"></a>
### 15.1. RETRY-1 — Replay safety is a protocol

**Type:** CONDITIONAL | **Origin:** DERIVED ENGINEERING RULE | **Applies:** retried, replayed, or redelivered operations

Contracts MUST distinguish idempotent transitions, request deduplication, replay-safe execution, ambiguous outcomes, and irreversible effects. A new retry identifier does not deduplicate an earlier request.

Key-based protocols MUST define principal/operation scope, persistence, concurrent requests, payload matching, retention, expiry, and result recovery. Reuse of the same operation identity for a materially different normalized request MUST be rejected or explicitly reconciled under the operation contract; it MUST NOT silently reinterpret the ID or apply a different action. Deduplication state and local effects need sufficient commit consistency for the replay claim. Expiration limits MUST be accounted for. Correlation and durable recovery receipts follow [OPS-1](#ops-1).

External duplicate prevention depends on the remote contract; a client key alone cannot provide it. An uncertain external action MUST NOT be retried merely because of a timeout. Status queries, reconciliation, durable intent/outboxes, remote idempotency, cancellation, or human intervention may be appropriate. Attempts may be observable without falsely recording repeated business effects.

