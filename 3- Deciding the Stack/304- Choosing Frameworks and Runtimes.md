<a id="tech-3"></a>
### 35.3. TECH-3 — Explicit platform commitments and frontend evidence

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** supported-platform definition and frontend selection

Each product MUST choose its actual desktop/mobile/tablet scope under [PORT-3](#port-3), rather than imply universal support. Where desktop Linux is supported, explicitly assess **Linux Mint, Ubuntu LTS, Arch Linux, and CachyOS** and record supported versions/configurations, test commitments, unsupported cases, and reasons. This requires a disposition for these distributions, not an unsupported guarantee that every distribution works identically.

Explain a selected Tauri architecture accurately: it uses a web-rendered interface with native integration; Rust application logic does not make every frontend component Rust. The owner's preference for web-inspired visual design does not require web languages for every app. Select frontend technology through demonstrated design fidelity, performance, accessibility, integration, and platform suitability, using prototypes when necessary. Compare native-appearing, platform-specific UI and deliberately shared/custom appearance on their merits under [UI-1](#ui-1)–[UI-3](#ui-3). Hybrid strategies require explicit reasons rather than becoming an automatic default. Preserve essential platform behavior and accessibility. Relevant future phone/tablet constraints SHOULD inform desktop-first architecture without claiming unimplemented mobile support.

