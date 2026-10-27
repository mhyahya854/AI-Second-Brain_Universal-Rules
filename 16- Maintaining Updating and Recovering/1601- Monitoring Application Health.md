<a id="run-2"></a>
### 26.2. RUN-2 — Proportionate diagnostics

**Type:** CONDITIONAL | **Origin:** DERIVED ENGINEERING RULE | **Applies:** failure reporting and operations

Applications MUST provide sufficient outcome/failure information without unnecessary sensitive exposure. Expected conditions differ from faults; a best-effort cleanup failure may need no stack trace, but material loss or a failed commit MUST NOT be hidden. Logs need bounded resources and appropriate retention.

Structured logging, correlation IDs, metrics, and health endpoints SHOULD be used where helpful; short-lived tools may need only exit status and diagnostics. Separate liveness, readiness, and deeper checks. Ordinary probes SHOULD be lightweight/non-destructive. Read-only probes cannot guarantee future writes; deliberate synthetic writes need explicit scope and cleanup.

