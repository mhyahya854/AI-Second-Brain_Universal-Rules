<a id="s04"></a>
## 4. Principals and delegation

*Section 4 rules across lifecycle files: [AUTH-1](#auth-1), [AUTH-2](../4-%20Planning%20the%20Architecture%20and%20Data/406-%20Planning%20Security%20and%20Permissions.md#auth-2).*

<a id="auth-1"></a>
### 4.1. AUTH-1 — Effective authorization and integrity enforcement

**Type:** UNIVERSAL INVARIANT | **Origin:** DERIVED ENGINEERING RULE | **Applies:** effects subject to authorization or integrity constraints

Permissions, domain constraints, and effect limits MUST be enforced at a boundary callers cannot silently bypass within the declared threat model. Hidden UI controls and prompts alone are insufficient. Interfaces may differ in authentication, privileges, quotas, rate limits, confirmation, and scope; they MUST NOT introduce an unacknowledged bypass of applicable integrity constraints. Administrative operations need explicitly authorized semantics.

Enforcement can reside in functions, databases, services, sandboxes, operating-system boundaries, or combinations. An in-process convention does not establish protection against a malicious same-account process or host administrator.

