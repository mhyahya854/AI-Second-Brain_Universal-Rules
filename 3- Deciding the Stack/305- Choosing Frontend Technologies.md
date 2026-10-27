<a id="ui-1"></a>
### 6.5. UI-1 — Platform-appropriate or shared UI

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** products with user interfaces across platform scopes

Products MUST evaluate platform-appropriate native-appearing interfaces and deliberately shared/custom cross-platform interfaces against actual workflow, accessibility, platform integration, design fidelity, performance, and maintenance requirements. Preserve product identity, appropriate visual consistency, and applicable capabilities. Android-native UI technologies, Swift/SwiftUI on Apple platforms, and suitable desktop technologies are valid choices. Non-Rust platform UI components may meet [LANG-1](#lang-1)'s technical exception criteria; record the component or standing exception without treating it as permission to duplicate core behavior.

A shared cross-platform UI is a first-class compliant architecture and needs no exception merely for sharing presentation. Select native, shared/custom, or a justified hybrid through the documented comparison under [TECH-3](#tech-3), rather than imposing one presentation strategy by default. The implementation language still follows [LANG-1](#lang-1), and both strategies preserve the shared Rust core under [CORE-1](#core-1). Platform-specific essential behavior and accessibility remain mandatory.

