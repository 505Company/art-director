# Creative direction

## 1. Define the design problem
- Product, buyer/user, job to be done, stage of user journey, primary action, content density.
- Emotional promise: choose at most 3 meaningful adjectives supported by industry/brand (e.g., precise, inventive, humane).
- Establish what must be recognized instantly and what should be discovered second.
- Distinguish persuasion pages (editorial hierarchy), productivity tools (clarity/data density), reading products (typographic cadence), experiential interfaces (motion as narrative). Do not apply the same treatment everywhere.

## 2. Reference analysis with integrity
For EACH supplied screenshot/URL, record:
- source/path and whether image was actually seen (not just described);
- what is objectively visible: alignment, column count, text size relative to frame, dominant/secondary colors, image crop, negative space, borders, depth, density, animation if demonstrably shown;
- what is an inference: likely CSS layout, font family, breakpoints, hover behavior;
- what to adapt, what not to copy, and why it suits this project;
- exact measurements only when evidence allows. For screenshots without DPR/browser access, say *estimate* and supply tolerance rather than fake px precision.
Ref != permission to reuse third-party fonts, logos, images or copyrighted compositions. Prefer original structure and correctly licensed assets.

## 3. Commit to a coherent concept
Deliver a short concept statement, one distinctive visual move (e.g. typography-as-navigation, carefully cropped editorial stills, engineering diagram rhythm), and a list of details that make it product-specific. Avoid adding gratuitous noise, 3D, gradients or excessive animations. If proposing 2 directions, choose a clear recommended primary one and document why.

## 4. Convert taste into measurable rules
Describe:
- **Composition:** reading path; focal point; asymmetric vs symmetric choice; container and 12/8/4-column grids where appropriate; alignment rules and section transitions.
- **Type:** licensed font family or approved fallback; 3–6 roles; weight, size, line-height, letter spacing, line length, hyphenation and Cyrillic/Latin support as applicable. Write fluid sizing formulas only after checking visual outcomes.
- **Color:** background/surfaces/text/border/action/status; dark/light modes; contrast; state colors; avoid unverified accent dependence.
- **Spacing and density:** 4/8-based or intentional alternative scale; section rhythm (e.g. small introduction then generous feature section); no arbitrary one-off gaps.
- **Imagery:** asset source/rights, focal point, crop, `object-position`, aspect ratios, alt text; when generation is required, specify subject, styling, framing, lighting, background, exclusions and asset review step. Never invent image files.
- **Components:** content-first semantics; button/input/table/card hierarchy; radius, stroke, elevation, iconic treatment and feedback states.
- **Motion:** only purposeful transitions; timing, easing, trigger, choreography and alternate reduced-motion mode. No motion mandatory on forms/critical controls.
- **Adaptation:** define desktop/tablet/mobile structure (what stacks, hides, wraps and reorders); keep primary action and semantic order.
- **Quality:** contrast, keyboard/focus, touch comfort, empty/loading/error states, i18n and long copy.

## 5. Anti-generic review
Reject unexplained template signals (uniform rounded cards, stock gradients, decorative blobs, oversized pointless badges, interchangeable hero text, meaningless icon grids). Reject arbitrary removal of such traits if a real brand explicitly asks for them. Each component must serve navigation, understanding, trust, action, hierarchy or storytelling.

## 6. Concrete outputs
Use `templates/creative-brief.md` and approved assets. Phrase decisions so Codex can implement them WITHOUT having to invent mood, layout, content or interaction. Highlight trade-offs: high creativity vs performance/legibility; how to preserve fallback behavior when animation/asset not available.
