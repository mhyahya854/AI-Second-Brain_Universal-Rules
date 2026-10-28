<a id="s10"></a>
## 10. Product platforms, portability, and visual assets

<a id="port-1"></a>
### 10.1. PORT-1 — Avoid unnecessary platform lock-in

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** platform and deployment choices

Applications SHOULD preserve portable architecture where practical and MUST document architectural portability, source portability, buildability, tested support, and official support separately. Product targets follow the declared scopes in [PORT-3](302-%20Choosing%20Supported%20Platforms.md#port-3); platform-specific departures use documented exceptions under [GOV-3](../0-%20Start%20Here%20and%20Universal%20Rules/003-%20Rule%20Priority%20and%20Authority.md#gov-3). A build is not runtime evidence. CPU architectures, OS versions, browser versions, BSD, and NAS platforms are not automatically one support matrix for every product. Declare concrete supported configurations and evidence. NAS obligations follow [NAS-1](../4-%20Planning%20the%20Architecture%20and%20Data/407-%20Planning%20Offline%20and%20Sync%20Behavior.md#nas-1).

<a id="port-2"></a>
### 10.2. PORT-2 — Portable references and faithful content

**Type:** CONDITIONAL | **Origin:** DERIVED ENGINEERING RULE | **Applies:** filesystem references and portable/interchange data

Hardcoded developer-specific paths in portable logic MUST NOT become runtime assumptions. Absolute paths may legitimately be host bindings, user configuration, filesystem-tool inputs, or audit evidence. Where relocation is promised, references MUST have documented identity/resolution semantics and explicit rebinding for host resources.

Use runtime path APIs where appropriate. Claimed targets require consideration of case behavior, Unicode normalization, reserved names, permissions, links, and collisions. Case-sensitive comparison or a universal sanitizer does not solve these differences. Preserve original names, bytes, and line endings when identity, signatures, fidelity, or user intent requires it; transformations need defined semantics and collision handling.

Example: `attachments/doc1.pdf` can be relative when its base and escaping are specified. `file://attachments/doc1.pdf` places `attachments` in the URI authority; it is not an ordinary relative reference. Reversible mappings can avoid lossy sanitation.

