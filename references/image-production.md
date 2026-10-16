# Image production: generation and compositing

Read this for image deliverables. Use the generators, editor, formats and budgets recorded in PROJECT-SETUP; verify their capabilities for the requested operation.

## 1. Roles and selection
- The art director defines the composition, variants, inputs and acceptance criteria. Agents produce candidates, measurements, composites, exports and comparison sheets.
- After each generation stage, the art director views candidates at useful inspection sizes and records selected IDs, reasons and rejected defects in `SELECTION.md` before dependent work starts.
- User selections take precedence. Agents implement the recorded selection; their own quality verdict does not replace visual review.

## 2. Choose the build method
| Method | Use when | Main risk |
|---|---|---|
| Whole-scene generation | Shared lighting, interaction and natural composition matter most | Identity, text and geometry can drift |
| Hybrid production | Generated content must preserve approved products or source pixels | Boundaries and lighting between sources |
| Assembly from parts | Precise control and reusable elements are needed | Inconsistent scale, perspective and integration |

For hybrid work, identify which source regions must remain exact before generating edits. Approve the base composition first; create isolated edit stages only where needed. Preserve source pixels outside the agreed edit area, and check perspective, occlusion and scale before compositing. Choose foreground/background boundaries from the actual composition rather than a fixed scene recipe.

## 2.1. Choose the generator by edit capability
Test the requested edit on a small sample. A tool that generates new scenes may not preserve identity or change viewpoint reliably. Record tested capabilities and limits for scene creation, removal, insertion, viewpoint changes and identity edits in PROJECT-SETUP. Review geometry and lighting again after a viewpoint change.

## 2.5. Creative pilot gate
When a pilot or speculative visual is requested:
- Develop the idea from the approved brief and supported product benefits. Use references for their stated purpose and respect asset rights.
- Verify explicit and implied claims against approved evidence; retain source, date and limitations in project records.
- Compare distinctive geometry, proportions, orientation and text with the approved source.
- Label speculative concepts. Generated imagery does not establish real fit, usage or product performance; use appropriate approved evidence for those claims.
- Review an agreed sample before mass production. Compare generators only when requested, within the approved budget, using actual candidates and task-specific criteria.

## 3. Generation rules
- Record the exact tool/model/mode, dimensions, aspect ratio, variant count and generation budget. Stop if the approved mode or spending allowance is unavailable.
- The user handles sign-in and account changes. Use the approved browser/profile and tool access; see `references/tooling-limits.md` for profile ownership, prompt read-back and downloads.
- Express layout and scale in measurable terms derived from the brief. Verify generated results rather than treating prompt values as achieved measurements.
- Keep runs within the recorded budget. Inspect for unintended edits, altered text, extra elements, identity drift, geometry errors and lighting changes before continuing.

## 4. Identity and variants
- Use only approved identity references. Choose reference views for the required angle and detail; record their actual paths and rights.
- Preserve an approved subject's identity, proportions, wardrobe, expression and lighting unless the brief changes them.
- Replace a region only when the observed defect warrants it. Record the crop, mask and intended change; fit boundaries, feathering and resolution to the actual image.
- Define each variant's changes explicitly. Keep all other approved properties stable and inspect variants together before selection.

## 5. Integration rule for every edited element
Compare each element with its native neighbours and immediate surroundings:
1. **Light:** direction, falloff, highlights, shadow structure and reflected light.
2. **Colour:** white balance, saturation and lit/shadow values; derive targets from the approved scene.
3. **Tone:** brightness and local contrast without unintended pale, dark or tinted patches.
4. **Texture:** sharpness, grain and depth of field consistent with distance and source resolution.
5. **Geometry:** perspective, scale, occlusion, contact/cast shadows and reflections.

Inspect at 100% and full frame. Record measurements and tolerances where they help establish acceptance; use the brief and neighbouring pixels as their source.

## 6. Visual QA before delivery
- Inspect identities, boundaries, hair and fine detail, text, product proportions, alignment, shadows and reflections.
- Check inserted elements against their surroundings and compare protected regions with the approved base.
- Inspect extended or rebuilt surfaces for streaks, seams, halos and rectangular tonal changes.
- Use crops and comparison sheets to locate defects, then open the full-resolution deliverables before acceptance. An agent report or a downscaled sheet alone is insufficient.
- Reopen acceptance if a defect is found later. Delivery checks are in `references/visual-qa.md`.

## 7. Compositing and correction
- Work at the required canvas size with reusable source layers, masks and uniform scaling. Adapt edge treatment to the source resolution and local light.
- After rotating or moving an element, verify its independent alignment and rebuild affected shadows, reflections and exposed surfaces.
- If an exact product's geometry differs from the generated version, replace the whole object with an approved source at uniform scale. Apply label artwork only to matching geometry; do not stretch it to conceal a shape mismatch.
- Extend surfaces with matching perspective, gradient and texture. Preserve approved pixels outside the edit scope; avoid stretching source pixels into visible streaks.
- Use adjustment layers where available. Match local light and colour while preserving approved identity, skin tones and brand colours.
- When repeated visual corrections miss a measurable target, define a bounded correction from the approved baseline and mask. Record the rule, affected region and before/after measurements rather than applying a fixed correction percentage to every image.
- Save new layered versions and required exports. If the user edits a working file, pause competing writes, preserve that state as the new approved base and update dependent tasks.

## 8. Agent logistics and delivery
- Assign one owner to each shared editor or browser profile. Keep independent outputs separate; follow the global and per-tool limits in PROJECT-SETUP.
- Keep each run focused on one deliverable. Hand off approved sources, selections, coordinates, masks and task state through project files; record usage against the agreed budget.
- Prefer correction packets with observed defects and exact targets over broad polishing requests.
- Deliver the agreed layered files, previews and exports with verified dimensions and project naming. Use `references/visual-qa.md` for design-tool boards.
- Verify every file target and use the host's supported link format. Open a file-manager window only when needed and after explaining the visible action.
