# Context audit — do not design blind

## Capability probe — before planning waves
Read current `PROJECT-SETUP.md` and `references/tooling-limits.md`. Run a bounded **1–2 minute probe** in the actual Codex executor session; enumerate available connectors/tools and check each service the plan depends on. Record results in the project's context audit using `templates/context-audit.md`.
- Verify tool visibility, sign-in state, required account type and read/create/edit capabilities separately. For example, a messaging app's bot account may lack public-channel search; a login in the user's main browser does not sign in a separate automation browser profile.
- Check quota/remaining allowance/reset, approval requirements (`exec` uses `never`), screenshot availability and per-tool caps. Use read-only calls where possible; only probe mutations already authorized, with visible effects disclosed.
- Record service/tool, account/session (no credentials), operation, date, evidence, VERIFIED / UNAVAILABLE / UNKNOWN, mitigation and owner. A binary or connector listing is not proof of service access.
- If a check needs more than the probe budget or human sign-in, record it as pending; do not pretend it passed. Re-probe when a tool fails and before dependent work resumes.

## Source priority
1. Explicit user instructions and approved references.
2. Brand/product/design docs in repository; approved current visuals.
3. Running product/screenshots and actual code/tokens/assets.
4. Reasoned inference labelled ASSUMPTION.
Never pretend a repository reveals target audience or brand positioning when those facts are missing.

## Minimum inspection
- Path/repository root, branch, HEAD, `git status --short`, uncommitted user work (do not overwrite).
- Package manifest/lockfile, language/framework versions, routing, styling system and UI libraries, runtime configuration.
- Existing UI components, design tokens, icons, fonts/licenses, image/brand assets, content and localization.
- API endpoints/types, state management, auth, external integrations. Identify sensitive/regulated boundaries.
- Tests, lint/typecheck/build/start commands, CI expectations and supported browsers.
- Screenshots/mockups/prototypes/design-tool files: what files/links are truly accessible. Do not claim analysis of inaccessible materials.
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
Record setup version, capability probe results, pending sign-ins/quotas/approvals and tool budgets before wave planning. State repo hash; source of truth for colors/type/assets; read/write boundaries; test commands (not yet executed vs observed); missing reference details; sensitive material; and whether Codex binary/auth exists. For code implementation outside a Git repo, use a single nonparallel planning mode by default and explicitly request a repo/worktree setup before multi-agent execution. Research/copy/image batches may use disjoint output directories with stable IDs and a serial merge owner when no code branching is involved.
