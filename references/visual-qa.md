# Integrated visual QA and exact correction protocol

## Only review what actually rendered
Preferred browser: Playwright (existing project setup or optional Playwright MCP), alternatives as available. If browser inaccessible, mark `NOT VISUALLY VERIFIED`; read code and tests as weaker evidence, never pretend to see final pixels. Review the **integrated running app**, not only isolated component snapshots.

## Minimum target matrix (adapt contract)
| Profile | Sample viewport | Expected inspection |
|---|---|---|
| Desktop | 1440×900 | composition, grid, typographic hierarchy, focus, scroll transitions |
| Tablet | 768×1024 | column reflow, safe image crop, navigation, density |
| Mobile | 390×844 | reading order, CTA, wrapping, image focal points, sticky UI |
| Narrow mobile | 320×700 | clipping, overflow, localized long text |

Each viewport: capture normal state PLUS relevant hover/focus/loading/error/mobile menu where implemented. Screenshots include routes, theme, and exact viewport metadata. Compare with supplied screenshots only if reference is accessible and scale/theme aligned. Snapshot differences alone do not equal UX failure; manual design review is required.

## Visual checklist — measure, don't opine vaguely
1. **Brand preservation and creative intent:** primary concept visible? consistent style, no generic filler, no unintended redesign?
2. **Hierarchy and reading flow:** first focal point, message order, heading/copy ratio, CTA prominence; scan path on mobile.
3. **Grid and rhythm:** container, columns, alignment, gutters, vertical cadence, equal baselines; section variation intentional.
4. **Typography:** actual font loaded (including Cyrillic glyph support where relevant), text wrap/contrast, no clipping at 200% zoom, readable line lengths.
5. **Color/assets:** contrast measured, correct real images, license/fallback, cropping, alt text, media load/performance.
6. **Interaction:** links/buttons work, keyboard navigation/focus visible, errors and loading readable, screen-reader semantics, menu/dialog escape behavior.
7. **Motion:** duration/easing/trigger matches contract, no layout-shifting or attention hijack, reduced-motion preference respected.
8. **Responsive:** no horizontal scrolling/overlap, tappable controls, sensible content flow, safe-area/layout in critical widths.
9. **Reliability:** browser console, JS exceptions, slow loading, network errors, hydration, required build/e2e/unit/a11y checks.

## Accessibility caution
For WCAG 2.2 AA, body text usually needs contrast >= 4.5:1; large text >= 3:1 (contextual exceptions apply). Touch target rule is nuanced: WCAG 2.2 AA minimum target size criterion is 24×24 CSS px with spacing exceptions, while a 44×44 CSS px comfortable target is a practical design preference / enhanced standard, not the blanket AA minimum. Do not invent measured ratios.

## Severity and evidence
- **BLOCKER (P0)**: broken primary flow, severe accessibility/functional fault, invalid contract, leaked secret, unsafe scope.
- **HIGH (P1)**: major layout defect, wrong asset, unresponsive critical state, significant readability issue.
- **MEDIUM (P2)**: visible hierarchy/spacing/motion deviations without primary-flow breakage.
- **LOW (P3)**: micro-polish with limited impact.

Each finding: `ISSUE-ID`, severity, observed evidence path/viewport/route/state, expected contract/AC, measured delta or qualified observation, exact file owner, fix instructions, regression test, and non-goals. No “looks weird, improve it.”

## Bounded corrections
Pass 1: capture all viewport/state issues together; assign isolated correction work with detailed delta packets. Pass 2: compare rerendered product and run regressions. If major unresolved problems remain, disclose them and escalate or explicitly plan another supervised cycle. Don't burn unlimited tokens polishing an already-acceptable site.

## Acceptance evidence
Record commands AND exits, browser screenshot filenames, which files were viewed by reviewer, actual route and viewport, contract IDs verified, untested states and risks. Agent's claim is not independent verification. End with `ACCEPTED | PARTIAL | BLOCKED` and why.

## Inserted-element QA (applies to UI assets and image composites)
For every element that was inserted, replaced or edited: compare it with its native neighbours and its own surroundings on
light, colour, tone, texture and geometry/grounding; inspect at 100 % and at full-frame scale; record "looks pasted in?" per
element. Downscaled contact sheets and the agent's self-report are not evidence. Image-specific checklist:
`references/image-production.md` §5–6.
