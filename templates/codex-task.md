# TASK-[NNN] — [exact human-readable title]

**State:** PLANNED\
**Owner:** Codex [agent identifier]\
**Priority:** P[0-3]\
**Wave:** [number]\
**BASE_SHA:** [actual Git SHA]\
**Design contract:** [actual path + version]\
**Architecture contract:** [actual path + version]

## 1. User outcome / intent
- Why this change exists:
- Precisely what the user should see/do after completion:
- Success signal:

## 2. Deliverables and non-goals
- Must create/change:
- Must NOT implement or change:

## 3. Observed inputs and references
| Input file/URL | Is it available in this worktree? | Observed details | Assumptions to validate |
|---|---|---|---|

## 4. Verified technical context
- Framework and versions:
- Actual patterns/components to reuse:
- Public imports/exports and API contracts:
- Tokens and fonts (values or exact source):
- Current route and integration owner:

## 5. STRICT file ownership
- ALLOWED to create/modify (paths/globs with reason):
- READ ONLY / PROTECTED (explicit paths):
- Changes outside whitelist: stop, report, do not continue to commit.

## 6. Content and assets
- Exact text/labels/locale (no invented marketing metrics):
- Existing media path / aspect ratio / crop/focal point / alt:
- Fallback when asset missing:

## 7. Visual specification
- Hero/section layout and visual hierarchy:
- Grid/container/gutters/column spans:
- Typography (role, family, size, weight, line-height, tracking, max width):
- Color/border/surface/radius/shadow:
- Spacing scale and section rhythm:
- Icons/media style:
- Source of each value: APPROVED/PROPOSED/MEASURED ESTIMATE.

## 8. Desktop / tablet / mobile
| Viewport | Layout and ordering | Typography and spacing | Media behavior | Navigation/CTA | Edge cases |
|---|---|---|---|---|---|
| 1440×900 | | | | | |
| 768×1024 | | | | | |
| 390×844 | | | | | |
| 320×700 | | | | | |

## 9. Interactions and states
- Default/hover/focus-visible/pressed/disabled:
- Loading/empty/error/success:
- Keyboard, touch and screen-reader semantics:
- Scroll/resize/back-forward behavior:

## 10. Motion and reduced-motion
- Trigger, coordinates/property, durations and easing:
- Choreography/performance guardrails:
- `prefers-reduced-motion` behavior:

## 11. Accessibility and performance
- Semantics/contrast/focus/alt/labels:
- Images/fonts/loading/layout stability/perf budgets:

## 12. Dependencies, assumptions and STOP conditions
- Dependencies that must already be INTEGRATED:
- Reversible assumptions:
- Stop and report if:

## 13. Implementation checkpoints (numbered)
1. Inspect exact named files and contract.
2. Implement isolated component using approved values.
3. Verify responsive state(s) and required interactions.
4. Run actual available checks and capture results.
5. Record changed paths and unresolved issues.

## 14. Acceptance criteria (objective)
- [ ] AC-01: [observable and binary]
- [ ] AC-02: [observable and binary]
- [ ] AC-03: [observable and binary]

## 15. Checks and screenshot evidence
| AC | Command / browser route | Viewport/state | Required resulting evidence | Owner |
|---|---|---|---|---|

## 16. Security and prohibited side effects
- No secrets, private data, production access, migrations, deployment or unsafe external calls.
- New packages/system configuration only with integrator approval.

## 17. Required completion report
Return TASK-ID and `IMPLEMENTED | PARTIAL | BLOCKED`, paths changed, tested commands with exit codes (or NOT RUN), screenshot paths (or NOT CAPTURED), assumed choices, deviations, risks, and exact integration steps. Do NOT self-report `ACCEPTED` or `INTEGRATED`.
