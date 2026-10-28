<a id="safe-3"></a>
### 2.3. SAFE-3 — Explicit, testable core behavior

**Type:** DEFAULT | **Origin:** DERIVED ENGINEERING RULE | **Applies:** domain logic and authoritative decisions

Domain logic SHOULD make inputs, constraints, and transitions explicit and testable. Isolate or record time, randomness, observations, and model outputs where needed for claimed reproducibility. Randomized algorithms and probabilistic domain functions are permitted. Deterministic code is not proof of correctness; total system determinism is not required. Effective enforcement follows [AUTH-1](1007-%20Implementing%20Security%20and%20Authorization.md#auth-1).

