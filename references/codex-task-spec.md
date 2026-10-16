# Codex TASK specification — exhaustive by design

**The Codex agent enters cold, without the orchestrator's conversation context. Every TASK is a complete work order.** Read the task template and fail preflight if any required slot is blank (N/A + reason is okay). Copy exact approved values from contracts; do not rely on unspecified implicit taste.

## Mandatory fields (19)
1. `TASK-ID`, priority, phase, owner, status and contract `BASE_SHA`; current `PROJECT-SETUP.md` path/version and applicable agent policy, tool caps, budget and client rules.
2. User-visible objective and rationale; precise user flow to improve.
3. Scope/non-goals; explicit list of what must not change.
4. Input/evidence: URLs, assets and paths that truly exist (reference observations vs approximations); links to contract version.
5. Stack/versions, architecture and file patterns; do not override stack for convenience.
6. Exclusive files allowed to create/modify and explicitly forbidden shared files. Wildcards only if narrow enough to audit.
7. Interfaces (imports, exports, props, events, API shapes, CSS tokens, DOM hooks) with examples.
8. Content: exact headlines, labels, locale, image/alt, real data vs placeholder policy.
9. Pixel/visual rules: hierarchy, type metrics, alignment, grid, spacing, color, border, radius, depth and media layout with measured values or explicitly labelled proposals.
10. Three viewports: desktop/tablet/mobile **behavior**, not just sizes; small viewport overflow cases; large text/long content.
11. Interactions: focus/hover/pressed/disabled/loading/empty/error/success and navigation outcomes.
12. Motion: trigger, duration, easing, layering, gesture, fallback, `prefers-reduced-motion` and performance constraints.
13. Accessibility: semantics, alt text, focus order, contrast, keyboard, aria only as needed.
14. Dependencies and exact available baseline; assumptions and when to STOP.
15. Implementation plan step-by-step with validation points. Don't micromanage trivial syntax but leave no product/design ambiguity.
16. Acceptance criteria (binary, verifiable, bounded tolerance; map AC-01 etc. to tests/screens).
17. Validation commands as they exist in repository; expected artifacts/capture paths, viewports and routes.
18. Required final delivery: changed files, commands & exits, screenshots, unresolved issues and commit/worktree state.
19. Risk/security: secret access, migration/deploy prohibitions, operator approval if needed.

## Acceptance quality
- Define layout, ordering, readability and overflow behavior at the agreed viewports. Map each requirement to an observable check.
- Separate visible reference observations from inferred implementation details. Use approved project fonts and tokens; label estimated measurements with their tolerance.
- Specify motion triggers, properties, timing and reduced-motion behavior from the current design contract. Require checks for repeated navigation and relevant interaction states.

## Task grading
- **Completeness**: no hidden prior context necessary to build intended behavior.
- **Design clarity**: exact approved measures, content, constraints, and observable decisions.
- **File isolation**: no shared writes or ambiguous owner.
- **Objective QA**: observable outcomes and reproducible commands/captures.
- **Risk control**: proper dependencies and data boundary.

If a critical dimension is genuinely unknown, designate a single owner for investigation/decision and make the implementation task dependent on the result; do not turn the unknown into 3 competing agent guesses.

## Final Codex response schema (plain text)
- `TASK-ID` + state `IMPLEMENTED | PARTIAL | BLOCKED` (never automatically ACCEPTED)
- `Changed:` relative paths
- `Checks:` command, exit code, actual summary; use NOT RUN where applicable
- `Screenshots:` exact paths if generated
- `Assumptions:` anything inferred in implementation
- `Deviations:` deviations from task or contract
- `Risks:` known remaining issues
- `Handoff:` recommended integration/test steps
