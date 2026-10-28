<a id="workspace-test-2"></a>
### 49.2. WORKSPACE-TEST-2 — Literal JSON capacity and feasible workload

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** workload planning and performance claims for literal dual-JSON storage

<a id="workspace-workload"></a>
#### 49.2.1. Workload and lifetime costs

Evaluate capacity, storage amplification, temporary write space, write frequency, serialization time, crash consistency, memory, backup growth, cloud upload/transfer cost, NAS bandwidth, mobile constraints, concurrent access and lifetime growth under [DEV-16](../13-%20Testing%20Debugging%20and%20Repairing/1306-%20Testing%20Performance%20and%20Reliability.md#dev-16). State assumptions and measured or estimated evidence, including workload and target-platform limits. A small edit may require producing a new complete global JSON representation; hashing alone cannot remove the payload requirement.

<a id="workspace-storage-math"></a>
#### 49.2.2. Logical storage amplification

For illustration, 100 GB of binary originals plus approximately 133 GB of Base64 payloads in individual JSON and 133 GB in global JSON totals about **366 GB** before other overhead, temporary generations and history. This is approximate logical storage accounting, not a measured universal physical requirement. For binary lengths nᵢ, N = Σnᵢ and B = Σ(4 × ceil(nᵢ/3)), originals plus two single-encoded layers require approximately N + 2B; for large inputs this approaches 11N/3, so 100 decimal GB is approximately 366.7 GB. The rounded 366 GB illustration assumes each layer encodes each original payload once. Encoding an already encoded individual JSON envelope again inside the global layer adds expansion; separately encoded chunks add padding/framing. The actual schema must account for these costs rather than assume this estimate universally. Git uses separately stored content objects and references, unlike one literal complete JSON payload.

<a id="workspace-streaming"></a>
#### 49.2.3. Peak resources and streaming limits

Memory estimates MUST include the largest parser/encoder token and buffers: streaming records does not bound memory if an enormous Base64 string is allocated at once. Measure or bound peak disk while prior valid state and staging coexist, total bytes written/transferred, CPU, latency and growth; bounded memory does not remove total serialization, validation or I/O costs.

<a id="workspace-optimization"></a>
#### 49.2.4. Measured optimizations and material conflicts

Streaming serialization, compression, copy-on-write, snapshots, sparse files, reflinks and other optimizations MAY be evaluated within the eventual approved design, but their portability, actual savings, crash behavior and recovery dependencies require evidence. None is universally selected here or excuses complete payloads. If literal duplication cannot meet the agreed workload, present the material conflict honestly to the owner and resolve affected planning under [GOV-3](../0-%20Start%20Here%20and%20Universal%20Rules/003-%20Rule%20Priority%20and%20Authority.md#gov-3) and [DEV-5](710-%20Freezing%20the%20Approved%20Master%20Plan.md#dev-5); do not silently replace payloads with pointers, invent capacity, hide loss or implement a fallback.

