<a id="ui-6"></a>
### 6.10. UI-6 — Complete workflow states and actionable copy

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** user-facing workflows and their materially relevant states

Design MUST cover relevant states beyond the ideal happy path: initial/empty, loading/progressive loading, success/error/partial failure, unavailable service, offline/reconnecting, sync conflict, stale information, permission denied/authentication required, migration/recovery/unsupported version, security scan running/detection/quarantine/scanner unavailable, backup/recovery state, destructive confirmation, and irreversible-action warnings. A state with no applicable capability need not be invented. State presentation MUST accurately reflect outcomes and uncertainty under [OUT-1](#out-1), [RUN-2](#run-2), and [IO-3](#io-3), without changing established authorization or confirmation policy.

User-facing copy MUST be specific, understandable, context-aware, and concise where possible, explaining actual value, state, or action rather than generic AI marketing. Empty states SHOULD explain what belongs there, why it is empty, a useful next action, and whether content is expected automatically where relevant; generic “Nothing here yet!” filler and meaningless illustrations are insufficient when guidance is needed. Errors SHOULD explain what happened/was affected, whether anything changed, whether retry is safe, and the next action to the extent known. Raw implementation failures or “Something went wrong” MUST NOT be the sole explanation when they conceal known material information or uncertainty. Apply [PRIV-1](#priv-1) and [SEC-2](#sec-2) to disclosures.

