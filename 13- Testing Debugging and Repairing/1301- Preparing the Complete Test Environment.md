<a id="s27"></a>
## 27. Verification and evidence

*Section 27 rules across lifecycle files: [TEST-1](#test-1), [TEST-2](1303-%20Running%20Integration%20Tests.md#test-2).*

<a id="test-1"></a>
### 27.1. TEST-1 — Evidence appropriate to the claim

**Type:** UNIVERSAL INVARIANT | **Origin:** DERIVED ENGINEERING RULE | **Applies:** claimed application guarantees

Applications MUST verify claims with evidence appropriate to scope, risk, and failure model. Important claims require relevant failure, recovery, concurrency, migration, portability, security-boundary, AI-capability, and NAS-mode checks where those capabilities exist. Record tested configurations and distinguish passed, failed, skipped, unrun, and unsupported outcomes. A syntactic checklist does not prove semantics.

Non-AI apps need no AI tests; stateless formatters need no backup tests; NAS backup does not imply raw network-database support. Reuse engine/platform evidence only within its assumptions and verify integration. Tests reduce uncertainty rather than establish absence of all defects.

