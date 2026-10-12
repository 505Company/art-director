# Context audit — do not design blind

## Source priority
1. Explicit user instructions and approved references.
2. Brand/product/design docs in repository; approved current visuals.
3. Running product/screenshots and actual code/tokens/assets.
4. Reasoned inference labelled ASSUMPTION.
Never pretend a repository reveals target audience or brand positioning when those facts are missing.

## Minimum inspection
- Path/repository root, branch, HEAD, `git status --short`, uncommitted user work (do not overwrite).
- Package manifest/lockfile, language/framework versions, routing, styles/Tailwind and UI libraries, runtime configuration.
- Existing UI components, design tokens, icons, fonts/licenses, image/brand assets, content and localization.
- API endpoints/types, state management, auth, external integrations. Identify sensitive/regulated boundaries.
- Tests, eslint/typecheck/build/start commands, CI expectations and supported browsers.
- Screenshots, mockups, prototypes and design files: what inputs are truly accessible. Do not claim analysis of inaccessible materials.
- Existing `CLAUDE.md`, `AGENTS.md`, project rules. Respect non-overwrite instruction.
- Deployment, performance and accessibility requirements; browser availability for QA.

## Evidence ledger
| Decision/observation | Source/line/path/screenshot | Confidence | Status | Needs verification |
|---|---|---|---|---|

Keep separate `OBSERVED`, `USER-SUPPLIED`, `INFERRED`, `PROPOSED`, and `UNKNOWN`. Carry critical unknowns into work orders as explicit assumptions; do not invent precise values from vague screenshots.

## Scope classification
- **Preserve**: redesign not requested, inherited UI system must survive.
- **Extend**: introduce new surfaces under existing system.
- **Redesign**: visual identity replacement explicitly permitted; identify preservation constraints first.
- **Prototype**: permitted shortcuts and placeholders, clearly labelled; never substitute for production without approval.

## Discovery exit checks
State repo hash; source of truth for colors/type/assets; read/write boundaries; test commands (not yet executed vs observed); missing reference details; sensitive material; and whether Codex binary/auth exists. If not a Git repo, use a single nonparallel planning mode by default and explicitly request a repo/worktree setup before multi-agent execution.
