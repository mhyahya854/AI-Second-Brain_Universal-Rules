<a id="hermes-3"></a>
### 16.7. HERMES-3 — Core resolution, ambiguity, and actionable failures

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** AI-facing lookup and application-operation interfaces

AI MAY express intent using names, aliases, search terms, friendly references, or previously resolved identifiers. The deterministic application/core MUST resolve or validate authoritative identity, exact location/path, and mutation semantics. Model-generated text MUST NOT by itself create authoritative IDs, canonical paths, or hidden persistence structures. Authorized create/import operations may assign or validate identities according to the product contract; this rule does not forbid delegated coding or scratch work under [AI-1](#ai-1).

When a friendly reference has multiple plausible matches and the contract does not uniquely resolve it, tools MUST return scoped candidates and relevant distinguishing information, indicating that clarification is required. They MUST NOT silently choose the first match or require the AI to invent an ID. Candidate disclosure remains subject to access/privacy controls; excessive result sets may be bounded and narrowed.

Failures SHOULD expose deterministic, actionable information where practical: what failed and why, whether anything changed or remains unknown, relevant object/operation IDs, candidates, a safe next action, and whether user input is required. A raw stack trace alone SHOULD NOT be the ordinary continuation contract. Outcomes remain truthful under [OUT-1](#out-1); structured errors do not grant additional authority or guarantee AI obedience.

