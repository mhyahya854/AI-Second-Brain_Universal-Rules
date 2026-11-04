<a id="arch-2"></a>
### 6.2. ARCH-2 — Modular monolith by default

**Type:** DEFAULT | **Origin:** USER POLICY | **Applies:** ordinary feature-rich application deployment

A modular monolith SHOULD be preferred when it is the simplest design satisfying isolation, reliability, privilege boundaries, scaling, deployment, lifecycle, maintainability, and performance. Multiple processes/services may be justified by fault containment, plugin isolation, runtime incompatibility, independent lifecycle, hardware placement, operational economics, reliability, or scaling. Record the rationale; literal single-process impossibility is not required. Distribution adds network, transaction, deployment, and recovery responsibilities.

<a id="workspace-3"></a>
### 45.3. WORKSPACE-3 — Three architectures and meaningful folder contracts

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** substantial application planning, with workspace detail required for persistent-data applications

<a id="workspace-three-architectures"></a>
#### 45.3.1. Workspace, planning, and implementation responsibilities

Planning MUST separately assess and validate **A: User Data Workspace**, **B: Master Plan**, and **C: Codebase**, including cross-references and distinct ownership/responsibilities. If no user information is retained, document A as inapplicable. Master Plan retains [BLUEPRINT-1](../6-%20Writing%20the%20Complete%20Master%20Plan/608-%20Finalizing%20the%20Project%20Folder%20Structure.md#blueprint-1)'s Languages and Data, complete specification, Research and Decisions, Design, Reviews, Project State and sequential phases/subphases. Codebase retains feature-first frontend, backend, database and genuine shared responsibilities. `Codebase/Database/` schemas/migrations are development artifacts, not actual user data by default.

<a id="workspace-folder-contract"></a>
#### 45.3.2. Per-folder and per-file design contract

For substantial persistent-data applications, the data hierarchy MUST be explicitly designed, explained, challenged and validated before plan approval. An attractive tree alone is insufficient. Use extensive meaningful headings/subheadings without arbitrary heading limits. Each meaningful folder/file or documented homogeneous class MUST establish purpose, ownership, contents, format, naming, relationships, dependencies, authority/replica/projection/historical-evidence role, rebuildability, discovery, human reading, AI reading, permitted modification, change detection, corruption detection, recovery, relocation behavior, access controls, and retention. Class-level contracts must resolve every actual member's role; they cannot hide exceptional authoritative content.

Do not create customary or empty folders without a demonstrated responsibility. Validate the hierarchy through [WORKSPACE-TEST-1](../13-%20Testing%20Debugging%20and%20Repairing/1304-%20Running%20End-to-End%20Tests.md#workspace-test-1), and keep the complete intended specification and its technical records consistent under [BLUEPRINT-2](../6-%20Writing%20the%20Complete%20Master%20Plan/602-%20Documenting%20Every%20Feature.md#blueprint-2).

<a id="web-sys-1"></a>
### WEB-SYS-1 — Needs-based backend architecture, production-readiness, and system-design evaluation

**Type:** DEFAULT | **Origin:** USER POLICY | **Applies:** backends, persistent services, networked applications, and other systems where operational constraints materially affect design

For production readiness, backend architecture, and system design, **consider the following based on actual needs rather than treating them as default implementation mandates; do not require mutually alternative system-design patterns simultaneously**. Assess the product's use cases, supported deployment modes, expected users and concurrency, data sensitivity, workload and growth envelope, failure model, offline/local-first requirements, capacity/budget, operational skills, and actual service-level goals. Record decisions and meaningful non-applicability proportionately in the App Plan or ADR, rather than manufacturing infrastructure for an unrelated problem. [ARCH-2](#arch-2) already prefers a modular monolith when sufficient; [DEV-16](../13-%20Testing%20Debugging%20and%20Repairing/1306-%20Testing%20Performance%20and%20Reliability.md#dev-16) governs growth-envelope evidence.

| Decision area | Consider when relevant (not simultaneous requirements) | Evidence/question to resolve |
|---|---|---|
| Quality attributes and capacity | scalability, availability, reliability, fault tolerance, resilience, latency, throughput, consistency, durability, partition tolerance, capacity planning | What workload, failure scenario, recovery objective, correctness guarantee, and performance budget must actually be met? |
| Scaling and traffic | load balancing; horizontal, vertical, and automatic scaling; load shedding; redundancy, failover, high availability, disaster recovery | Which component bottlenecks, what happens under overload, and which availability/recovery objective justifies added replicas or infrastructure? |
| Data layout and storage | database indexing, sharding, partitioning, replication, normalization, denormalization, query optimization, connection pooling, object/blob storage, full-text search/indexing, Bloom filters, consistent hashing | Which measured query/storage bottleneck or data-access pattern needs this, and which authoritative data guarantees might it weaken? |
| Transactions and consistency | ACID/BASE, isolation levels, strong/eventual consistency, distributed transactions, quorum, consensus, leader election, distributed locking, idempotency, race conditions, deadlocks, clock synchronization | What invariant/ordering/failure boundary requires it? How are retries, clocks, duplicate effects, conflicts, and recovery handled? |
| Caches and delivery | cache invalidation, eviction, stampede mitigation, CDN, cache-aside, write-through, write-back | Which content may be stale or lost, what are the freshness/ownership rules, and is any cached value improperly promoted to sole authoritative state? |
| Interfaces and access | REST, GraphQL, gRPC, API gateway, rate limiting, throttling, authentication, authorization, service discovery, WebSockets, long polling | Which clients, access boundaries, transport, abuse cases, and interaction patterns exist? Authentication does not imply authorization. |
| Architecture and asynchronous work | monoliths, microservices, event-driven architecture, event streaming, messages, queues, pub/sub, Kafka, event sourcing, CQRS, saga | What ownership, team/lifecycle boundary, delivery contract, throughput, and replay requirement justifies the distribution/coordination cost? |
| Failure containment and async operations | exponential backoff, circuit breaker, bulkhead, backpressure, dead-letter queue | Which failures are transient, which retries are safe, and how are overload, poison messages, exhaustion, and unknown outcomes bounded? |
| Operations and delivery | distributed tracing, observability, logging, metrics, SLI/SLO; rolling, blue-green, and canary deployments; containers and orchestration | What is deployable in the supported environment, what is observable, and how are failures detected, contained, rolled back, and verified? |
| Tenancy and network behavior | multitenancy; partition behavior; client connectivity; concurrent users | Are isolation boundaries, data residency/authority, noisy neighbors, or intermittent network access genuinely present? |

**Important distinctions, not additional platform mandates:**

- **CAP:** In a genuinely distributed data system under a network partition, there can be a tradeoff between continuing to answer requests (availability) and preserving a specified strong-consistency guarantee. CAP does **not** mean that an application permanently chooses any two of three qualities, or that a single-process offline app needs consensus infrastructure. Specify which operations remain available, fail closed, or reconcile when communication is unavailable.
- **ACID versus BASE, strong versus eventual consistency:** These are not blanket mutually exclusive labels for a whole product. Define correctness and isolation **per operation and data boundary**; separately classify transactional canonical state, replicas, projections, and caches. Derived or eventually reconciled views must not silently outrank authoritative originals under the existing data rules.
- **CQRS, event sourcing, saga, queues, pub/sub, and Kafka** solve different problems and may be independent or complementary. Neither CQRS nor Kafka implies event sourcing; neither a message broker nor a saga guarantees exactly-once external effects. Use only justified parts and preserve existing [RETRY-1](../10-%20Building%20the%20Core%20and%20Backend/1006-%20Implementing%20APIs%20and%20Services.md#retry-1) protocols.
- **Consensus, quorum, leader election, and locks** are conditional distributed coordination mechanisms, not universal prerequisites. Prevent races and deadlocks with appropriate local transactions/concurrency contracts where sufficient; introduce distributed coordination only when its failure model demands it.
- **Blue-green, canary, and rolling deployments**, and **monolith versus microservices**, are choices rather than instructions to deploy both. Availability, latency, throughput, and recovery require measurable budgets and verification, not an architecture diagram alone.

**Decision gate:** For each material architectural option, record **need/trigger → alternatives → chosen or not applicable → failure and correctness tradeoffs → cost/complexity → verification method**. Local-first, private, personal-only projects must not acquire cloud dependencies, external services, or multi-tenant infrastructure merely because a term appears in this catalog. Existing [SAFE-1](../0-%20Start%20Here%20and%20Universal%20Rules/002-%20The%20Universal%20Constitution.md#safe-1), [ARCH-1](402-%20Dividing%20the%20Application%20Into%20Features.md#arch-1), [RUN-1](../15-%20Packaging%20Deploying%20and%20Releasing/1506-%20Preparing%20Deployment%20Configuration.md#run-1), [TEST-1](../13-%20Testing%20Debugging%20and%20Repairing/1301-%20Preparing%20the%20Complete%20Test%20Environment.md#test-1), and data-preservation obligations remain applicable.
