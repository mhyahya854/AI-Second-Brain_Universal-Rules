<a id="exec-4"></a>
### 41.4. EXEC-4 — Project State and a bare “Continue” request

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** every active application and new-session continuation

The concise Project State required by [DEV-9](../17-%20Preserving%20Memory%20and%20Learning/1701-%20Recording%20Current%20Project%20State.md#dev-9) MUST expose current phase/subphase; last verified completed phase/subphase; completed capabilities; work in progress and not started; actual implementation status; known blockers and important unresolved errors; applicable observed repository revision and relevant dirty state; next authorized action; phase/subphase paths; and continuation instructions. Its human-readable and machine-readable representations MUST agree; one structured Markdown record may serve both. Do not invent the future commit that will contain a state update.

On receiving only **“Continue,”** an executor MUST read repository entry instructions and Project State, reconcile them against actual files/revision/evidence, locate the first unfinished authorized phase and its first unfinished subphase, load its full contract, and inspect existing partial work before acting. A partial subphase MUST NOT automatically restart from scratch. After passing its gate, the executor MAY continue to the next ordered authorized subphase in the same session. Existing delegation persists; “Continue” does not grant new production, destructive, credential, or other ungranted authority. If observed state contradicts recorded state, reconcile evidence and authorization before proceeding; do not select an easier later task.

