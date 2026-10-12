# Image production: generation and compositing

Read this when the deliverable is an image rather than a UI. Define the subject, intended use, dimensions, approved inputs and acceptance criteria from the current request. Choose tools and methods for that task.

## 1. Roles and selection

- The art director owns the concept, composition, prompts and final selection. Agents produce candidates, perform edits and prepare comparison sheets.
- After each generation stage, inspect the candidates side by side at full size and record the chosen files in `SELECTION.md` before dependent work begins.
- Record the user's approved choices in the brief and selection file. Keep agent reports separate from independent visual review.

## 2. Choose a build method

| Method | Suitable when | Inspect carefully |
|---|---|---|
| Whole-scene generation | Subjects need shared lighting and natural interaction | Identity, text, dimensions and unwanted changes |
| Hybrid generation and compositing | Some elements need exact geometry or approved source assets | Joins, perspective, scale and lighting |
| Assembly from separate elements | Precise placement and reuse matter | Grounding, masks, shadows and consistency |

Choose the method from the required fidelity, available assets and tool capabilities. Describe which layers are generated and which use approved sources. Keep lighting, camera and composition consistent across separately produced elements.

## 3. Generation rules

- Use the user's authorized tool, model, settings and budget. Confirm the active settings before starting; pause if they differ from the approved plan.
- Specify composition, proportions, lighting, framing, aspect ratio and required output size. Measure the actual output before compositing.
- Keep each run bounded by one clear deliverable and a stated generation limit. Pass selections and work state through files.
- Inspect generated geometry, text, object count, identity, pose, colors and background continuity. Correct observed defects with a precise edit brief.
- Use only inputs approved for the task. Preserve unrelated details when editing an existing image.

## 4. Character identity

- When consistent characters are required, define the needed reference views from the task. Record approved identity references by role and actual file path.
- Preserve the face generated within a scene when it matches the approved identity and lighting. Explain any requested replacement with an observed difference.
- For a localized edit, record the crop coordinates and preserve position, scale, angle, expression, hair, lighting and surrounding detail unless the brief specifies a change.
- Use masks suited to the actual boundaries, then match light, color and texture. Check the result against the approved identity and the surrounding image.
- Check light direction and anatomy before mirroring or transforming a subject. Apply requested appearance changes consistently across approved variants.

## 5. Integration of inserted or edited elements

Compare every element with its native neighbours in the same light zone and with its own surroundings. Evaluate:

1. **Light:** direction, gradient, highlights, falloff and reflected light.
2. **Color:** white balance, saturation and black level on both lit and shadow sides.
3. **Tone:** brightness and local contrast.
4. **Texture:** sharpness, grain and depth of field at the element's distance.
5. **Geometry and grounding:** perspective, camera height, scale, occlusion, contact shadows, cast shadows and reflections.

Derive target values and tolerances from the approved image and nearby elements. Matching average color alone does not establish matching light structure. Inspect at 100% and at full-frame scale; revise visible seams or elements that appear pasted in.

## 6. Independent visual QA

- Review full-size crops of identity details, masks, object bases, shadows, text and joins, together with the full composition.
- Check consistency across variants: identity, scale, perspective, colors and required content.
- Verify text against approved source copy. Inspect for halos, doubled edges, unwanted casts and missing or extra elements.
- Use comparison sheets for navigation, then open the original files for detailed checks. Record observed defects and corrective actions before accepting a deliverable.

## 7. Compositing and export

- Set the canvas from the required final dimensions. Preserve source layers and use editable masks or smart objects when supported.
- Transform elements with their associated shadows and labels. Rebuild exposed areas after moving an object.
- Use approved source artwork for text or product graphics that must remain exact. Match its perspective, surface shape and illumination.
- For background changes, match horizon, camera, depth of field, color and edges to the subject.
- Derive grading and sharpness from the brief and composition. Preserve required brand colors and natural skin appearance.
- Save new versions of editable documents and preserve user-edited layer state. Export the agreed formats and verify their dimensions, appearance and filenames. Close only documents opened for the task.

## 8. Agent and tool logistics

- Assign one agent at a time to tools sharing a live application or browser session. Parallelize tasks with separate inputs, outputs and tool state.
- Split large jobs by deliverable. Hand off selection files, coordinates, layer information and remaining issues rather than full conversation history.
- Record actual run usage where available and adjust later task size to the agreed budget.
- Collect editable sources, exports and review evidence in the agreed delivery directory. Include their exact paths and any unresolved issues in the handoff.
