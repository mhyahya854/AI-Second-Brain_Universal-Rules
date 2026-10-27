<a id="s40"></a>
## 40. Beginner-readable implementation documentation and simplicity

<a id="doc-1"></a>
### 40.1. DOC-1 — File and function explanations for non-programmers

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** meaningful application source files and important functions

Every meaningful source file MUST begin with appropriate language-native file/module documentation, using clear separators and plain language understandable to a reader without programming experience. Explain, as applicable: **(1)** identity/location, **(2)** purpose, **(3)** what it does, **(4)** what it deliberately does not do, **(5)** owning feature/component, **(6)** actual users/callers, **(7)** dependencies/interfaces, **(8)** data read/modified, **(9)** permissions/boundaries, **(10)** invariants, **(11)** errors/failure, **(12)** relevant tests, **(13)** related Master Plan sections, **(14)** maintenance warnings, and **(15)** relevant architectural decisions. Omit inapplicable detail with care; do not replace an explanation with an unexplained acronym or boilerplate slogan.

Important functions MUST document purpose, inputs, outputs, meaningful callers/interfaces, side effects, data mutations, error conditions, assumptions, security/integrity effects, and dependencies. Explain non-obvious internal operations in simple numbered steps. Do not narrate trivial syntax, invent connections, or let comments substitute for types, tests, contracts, or verification. For generated or externally vendored code whose regeneration, upstream preservation, or language syntax prevents safe inline headers, provide a clearly linked adjacent explanation and provenance mapping; the exception is to placement, not to understandability or traceability.

