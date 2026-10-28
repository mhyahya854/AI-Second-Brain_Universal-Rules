<a id="hermes-2"></a>
### 16.6. HERMES-2 — Structured, bounded small-model retrieval

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** information architecture and retrieval interfaces for Hermes or other AI clients

Information architecture and AI retrieval interfaces MUST provide structured, scoped discovery and bounded context rather than uncontrolled workspace wandering or reliance on loading entire huge workspaces into a model. The logical flow is **user intent → capability discovery → structured query → catalog/index/core → stable ID → exact object → precise anchor where meaningful → bounded context**. Equivalent mechanisms are allowed. The application/core SHOULD perform as much deterministic narrowing as practical through IDs, aliases, catalogs, typed filters, relationships, bounded search, anchors, candidate lists, and structured errors.

Normal retrieval MUST NOT require the language model to recursively scan the entire user-data tree to answer ordinary queries. Authorized deterministic maintenance or index construction may traverse the corpus; that is distinct from the bounded result consumed by the model. Enforce relevant scope, authorization, and privacy during retrieval and context assembly. Rebuild claims follow [DATA-2](../10-%20Building%20the%20Core%20and%20Backend/1001-%20Implementing%20Shared%20Data%20Types.md#data-2).

Where Hermes/local AI is part of the product, interfaces MUST be designed and tested assuming a suitably capable constrained local model before relying on a powerful cloud model. Approximately 1B-class models are an engineering target where realistic, not a guarantee of flawless behavior or a universal parameter-count threshold. Record tested capabilities and limits under [TEST-1](../13-%20Testing%20Debugging%20and%20Repairing/1301-%20Preparing%20the%20Complete%20Test%20Environment.md#test-1). Cloud clients may provide better reasoning but MUST use the same authority model without hidden architectural privileges.

The **Hermes / User-Adaptable File Structure Blueprint is integrated as CANDIDATE policy**, together with [section 32](../5-%20Designing%20the%20UI%20and%20UX/503-%20Designing%20Information%20Architecture%20and%20Flows.md#s32). It standardizes discoverability and integrity while leaving user-facing organization domain-appropriate and adaptable. This product-use goal is distinct from the full-app development continuity goal in [DEV-11](../8-%20Dividing%20the%20Project%20Into%20Executable%20Steps/808-%20Creating%20Small%20Model%20Execution%20Packets.md#dev-11).

<a id="workspace-ai-2"></a>
### 48.2. WORKSPACE-AI-2 — Measurable one-billion-parameter navigation target

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** AI workspace navigation design and material small-model capability claims

<a id="ai-navigation-route"></a>
#### 48.2.1. Bounded retrieval route

Design for appropriately scoped data navigation by a suitably capable model around **1 billion parameters**. The preferred route is **AI → trusted application Skill → 00-START-HERE.md → folder guide and catalog → bounded retrieval operation → relevant record and precise content**. Supply clear entry points, stable IDs, readable names, bounded indexes/catalogs, precise sub-object addresses, deterministic lookup, limited outputs, ambiguity reporting, enforced authorization, task-specific examples and documented errors. A model MUST NOT need to read the complete global JSON, massive database or thousands of files merely to retrieve one ordinary record.

<a id="ai-navigation-evidence"></a>
#### 48.2.2. Actual evaluation and separate development target

Material capability claims MUST identify model/version and available parameter/quantization evidence, environment/tools/context limits, representative tasks and actual evaluation. Measure retrieval accuracy, errors, hallucinated paths, unauthorized mutations, context budget and correct escalation. Record passed/failed/unrun results and limits; parameter count alone proves no capability. Preserve [HERMES-2](#hermes-2)'s local constrained-model testing and [EXEC-6](../8-%20Dividing%20the%20Project%20Into%20Executable%20Steps/809-%20Allocating%20Context%20and%20Memory%20Budgets.md#exec-6)'s separate approximately 4B code-execution target. Navigating data and implementing an application are distinct evaluations.

