<a id="asset-1"></a>
### 10.4. ASSET-1 — Genuine vector source artwork

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** application-owned visual assets, including web UI assets

Naturally vector-representable assets SHOULD use genuine SVG as their source format, including icons, logos, interface symbols, badges, simple illustrations, diagrams, and decorative vector artwork. When recreating a raster reference as a UI icon or another vector-representable asset, authors MUST reconstruct genuine vector geometry rather than embed PNG/JPEG content in an SVG wrapper and claim compliance. Appropriate structures include paths, shapes, gradients, masks, and vector text converted appropriately when needed.

Photographs, screenshots, scans, textures, camera images, complex photographic artwork, and other intrinsically raster content MAY remain raster in formats appropriate to the use case. They MUST NOT be converted into meaningless SVG merely to satisfy this policy. Required generated raster icon sizes and platform/store-specific containers are permitted; naturally vector artwork SHOULD retain vector source-of-truth artwork. Generated platform derivatives do not violate this policy.

<a id="asset-2"></a>
### 10.5. ASSET-2 — Third-party brand fidelity

**Type:** ECOSYSTEM POLICY | **Origin:** USER POLICY | **Applies:** third-party trademarks and brand assets

Products MUST NOT inaccurately redraw third-party trademarks from screenshots. Where permitted, use official brand assets and follow applicable brand requirements. The application-owned SVG preference does not authorize inaccurate conversion or disregard of asset licensing or brand constraints.

<a id="asset-3"></a>
### 10.6. ASSET-3 — SVG trust boundaries

**Type:** CONDITIONAL | **Origin:** USER POLICY | **Applies:** SVG acceptance, rendering, and application-owned SVG assets

Untrusted SVG MUST NOT automatically be treated as harmless image data. Applications accepting external SVG MUST handle script execution, remote resource access, and unsafe embedded content according to the actual renderer and trust boundary, using appropriate restrictions, sanitization, isolation, or rejection. Application-owned SVG SHOULD avoid unnecessary executable or external content. File extensions and SVG wrappers do not establish safety.

