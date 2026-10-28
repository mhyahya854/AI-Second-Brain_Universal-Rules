<a id="s26"></a>
## 26. Configuration, observability, and runtime lifecycle

*Section 26 rules across lifecycle files: [RUN-1](#run-1), [RUN-2](../16-%20Maintaining%20Updating%20and%20Recovering/1601-%20Monitoring%20Application%20Health.md#run-2), [RUN-3](#run-3).*

<a id="run-1"></a>
### 26.1. RUN-1 — Explicit configuration and defaults

**Type:** DEFAULT | **Origin:** ARCHITECTURAL DECISION | **Applies:** configurable applications

Applications SHOULD separate environment-specific settings from portable logic and define deterministic resolution/validation. Built-in defaults are legitimate. CLI, environment, deployment file, user preferences, defaults is an illustrative order; managed policy may be non-overridable. Surface relevant effective non-secret settings and use supported host discovery or explicit configuration. Changing configuration does not imply environments have equivalent capabilities.

<a id="run-3"></a>
### 26.3. RUN-3 — Declared deployment and bounded lifecycle

**Type:** CONDITIONAL | **Origin:** DERIVED ENGINEERING RULE | **Applies:** supported deployment modes and persistent services

Applications MUST document supported runtime modes. Native binaries, desktops, mobile/browser runtimes, services, and OCI images are options, not universal simultaneous requirements. Container identities, mounts, permissions, and isolation must fit their role; packaging does not establish NAS semantics.

Startup MUST verify prerequisites for safe operation, including relevant schema compatibility/exclusivity. Read-only software need not demand writable canonical storage. Preflight success does not replace runtime handling. Shutdown SHOULD stop new work, complete or safely interrupt work, and flush/close according to contract within appropriate bounds. Crash safety cannot depend solely on graceful shutdown. Exit status and diagnostics MUST reflect material failures; process exit alone does not prove effects completed.

