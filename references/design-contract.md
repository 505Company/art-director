# Shared design & architecture contracts (freeze before parallelism)

## Design contract requirements
- Version and approved baseline SHA; owner and change control.
- Token names/values for palette, type, spacing, radius, border, elevation, motion, grid and breakpoints. `TBD` is valid only for unapproved slots; no Codex agent fills a TBD differently in parallel.
- Asset inventory with actual repo paths, licenses if known, allowed substitutions and fallback behavior.
- Accessibility targets, responsive layouts, copy locale and font glyph coverage.
- Component list with states, names, roles/props, and shared dependency ownership.
- Per-surface screenshot requirements and measurable tolerances; no false pixel-perfection with unknown source/zoom.

## Architecture contract requirements
- Framework/runtime/build/package manager and package versions as observed; avoid unnecessary dependency additions.
- Route structure and one integrator who wires page composition, CSS variables, shared layouts, API types and configuration.
- Public component signatures and exported module paths; import conventions; feature flags.
- Required tests, selector conventions and visual check route(s).
- File ownership table with exclusive write scope for each TASK.
- Environment config rules, secrets and prohibited effects.

## Contract handoff procedure
1. Draft contracts and resolve conflicting requirements before tasks.
2. Save to `docs/art-direction/` or pre-existing design-doc directory.
3. Stage/commit approved contract and shared scaffolding as a single baseline (respect user's VCS permissions and uncommitted edits). Record `BASE_SHA`.
4. Fork only from `BASE_SHA` for an independent wave. Agents must read the same design contract version.
5. Changes to shared tokens/contracts require a serial `CHANGE-REQUEST` with impact analysis. Pause dependent tasks until integrated into a new baseline.
6. Integration owner alone adjusts shared files. No separate agents editing root `package.json`, global CSS, shared tokens, routing/lockfile at the same time.

## Write ownership
| Area | Owner | Editable paths | Protected paths |
|---|---|---|---|

Fill this table with the actual project areas, designated owners and verified paths. Assign shared tokens, routing and configuration to one integration owner.

Do not infer an owner merely because tasks have different titles. Files, generated outputs, lockfiles, tests and assets are the actual unit of conflict.
