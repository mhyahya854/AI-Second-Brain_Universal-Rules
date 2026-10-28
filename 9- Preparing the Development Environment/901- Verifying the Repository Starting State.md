<a id="dev-14"></a>
### 31.14. DEV-14 — Brownfield assessment and conformance before features

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** existing or partially built applications when these rules are applied with appropriate authority

Normal feature development MUST pause before extending inherited implementation. First inspect the authorized application, create/update its Master Plan, compare implementation with the applicable Universal Rules, Master Plan, and intended architecture, classify existing work, create Conformance Phases, repair, verify conformance, and only then resume ordinary planned development. Applying this workflow requires actual authority for that repository; this constitutional rule alone grants none.

An Existing App Assessment or equivalent MUST classify inherited implementation as applicable: already compliant, correct and reusable, usable with modification, obsolete, unsafe, architecturally inconsistent, or missing. **Preserve compliant work, repair non-compliant work, replace only where necessary.** Age or predating the current plan does not justify rewriting working compliant code. Record evidence, gaps, retained work, required repairs, and any approved exceptions.

Conformance Phases MUST precede new feature phases and use [DEV-10](../8-%20Dividing%20the%20Project%20Into%20Executable%20Steps/801-%20Creating%20Development%20Phases.md#dev-10) and [DEV-13](../14-%20Reviewing%20the%20Entire%20Application/1408-%20Checking%20Rule%20and%20Requirement%20Compliance.md#dev-13). They bring the inherited implemented scope into alignment with the constitution and current Master Plan; they do not require all future roadmap features to exist before development can resume. A failed gate permits scoped repair, not ordinary feature expansion. Following aggregate conformance verification, every subsequent phase remains subject to the same three-layer gate. Applicable safety/containment actions under [SAFE-2](../0-%20Start%20Here%20and%20Universal%20Rules/002-%20The%20Universal%20Constitution.md#safe-2) remain possible; they are not a feature-development bypass.

