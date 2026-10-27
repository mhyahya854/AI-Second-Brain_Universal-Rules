<a id="ui-3"></a>
### 6.7. UI-3 — Accessible interaction as product correctness

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** user-facing capabilities, including administration and tooling interfaces where exposed

Important supported workflows MUST provide reasonable accessible interaction appropriate to the target platform and interaction model. The App Plan MUST identify applicable accessibility acceptance criteria and relevant platform/industry standards, considering keyboard or other non-pointer operation, semantic controls, assistive technology, text scaling, visible/readable focus, contrast, reduced motion, and alternative interaction where relevant. Accessibility is part of product correctness, not merely optional visual polish; validate applicable workflows under [TEST-1](#test-1).

Native, shared cross-platform, and web UIs retain this outcome while adapting mechanisms and presentation under [UI-1](#ui-1) and [UI-2](#ui-2). No single accessibility standard or identical UI is universally required. Headless libraries, background daemons, and machine-facing APIs need no graphical accessibility controls; any user-facing administration or tooling is assessed on its own applicable interactions.

Accessibility MUST be considered from relevant wireframe, component, interaction/state, and design-system decisions, not deferred entirely to final polish. Applicable criteria SHOULD address accessible names, focus order/visibility, screen-reader structure, target size, dragging alternatives, and non-color-only meaning. Use current platform/industry guidance and WCAG/APG where applicable without imposing web mechanisms on native/headless software.

