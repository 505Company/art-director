# Tooling limits — probe, budget, queue

Use these planning constraints with actual account/version probes. Record account tier, date, evidence and unknowns in the context audit; re-probe failures instead of multiplying blocked calls across agents.

## Capability checklist and mitigations
- [ ] **Codex `exec` approval policy:** noninteractive runs use `never`; MCP/app operations requiring new approval fail. Probe read/create/edit separately: creation may work while updates require approval. Plan create-only flows with values set at creation, or an authorized interactive session for edits. The user must pre-configure approved MCP operations before noninteractive runs; agents must not bypass policy or change global config.
- [ ] **Design-tool quota:** check actual allowance/reset and account capabilities. Budget one inventory pass, targeted reads/screenshots and final verification; lower parallelism for shared files or daily limits.
- [ ] **Task-tracker quota:** estimate calls per task, subtask, comment, search and read-back, not task count alone. Split import from verification into resumable stages when needed; save imported IDs and exact unverified sections.
- [ ] **Computer use/capture:** probe a read-only capture on the actual browser surface; mark unavailable captures NOT CAPTURED. Use the separate automation profile below for web generators, keeping the user's main browser free.
- [ ] **Session sign-in:** a login in the user's main browser does not authorize a separate automation profile or in-app browser. Identify the actual profile/session and have the user sign in; agents never type credentials.
- [ ] **Web image generator:** record exact model/mode, subscription/unlimited availability, resolution and edit capabilities in PROJECT-SETUP. Do not infer re-angling support from a generic edit mode; see `references/image-production.md` §2.1.
- [ ] **Connector visibility:** a connector configured in a host's web UI may be absent from its CLI or a Codex CLI session. Inventory the actual executor's tools.
- [ ] **Service account capability:** a messaging app's bot account may lack public-channel search or other operations. Verify account type and access, not just login; report missing capability.

## Separate automation browser for web generators
Use an agent-owned browser profile through a browser-automation MCP, **separate from the user's main browser**. Browser automation operates that profile without taking over the user's screen, mouse or keyboard.

1. Record the dedicated profile, downloads folder, tool owner and approval setup in `PROJECT-SETUP.md`. The user signs in once in that profile; agents never enter credentials.
2. Some sites block headless browsers with **HTTP 403**. When this is a browser-mode restriction and access is authorized, run **headed in its own window**, controlled through the automation MCP. Keep the user's main browser free; do not work around account/access restrictions.
3. A profile can be held by **only one process**. Close the sign-in window before agent runs; assign **one agent per profile**. On "profile in use", release the existing owner/sign-in window before retrying; do not start another process against the locked profile.
4. Configure downloads into a dedicated folder. MCP tool approvals must be **pre-configured by the user** for the required operations: noninteractive runs cannot approve new requests. Probe from the actual executor before a batch; missing approval means hold dependent work.
5. Native Save dialogs may still occur. Warn before triggering them and explain Cancel/Escape; let the user change download settings themselves, or fetch a known authorized file URL within current permissions. Do not silently alter browser settings.

## Browser prompt and file hygiene
- **Before every submit**, read back the committed prompt from the page. A field can display new text while an editor retains stale internal state; commit/refill through the supported UI and verify again if needed. A screenshot of newly displayed text alone does not prove the submitted prompt. Hold submit if read-back cannot establish the intended prompt.
- Locate each download by its **exact filename in all subfolders of the dedicated downloads folder**; browsers can remember a last-used nested folder. Verify the selected file's content/type rather than relying on a recent-file guess.
- **Copy**, never move or delete, the user's source/download files. Write project copies and new versions only inside the assigned scope.
- Verify deliverable targets and use the host's supported link format; reveal non-previewable layered files in the file manager with the visible-effect warning in `references/security.md`.

## Per-tool concurrency
Apply the recorded global limit and every required tool limit to each wave. Quota budget may lower concurrency further.

| Resource | Default cap | Scheduling rule |
|---|---|---|
| All agents | User's chosen max; default 10 | Count active workers and nested sub-agents together |
| Each shared browser profile / computer-use session / raster editor | 1 each | Exclusive owner; queue access; keep the user's main browser free for generator work |
| Design tool | 1–2 | Prefer 1 for a shared file; serialize shared-node writes |
| Task tracker / other service connectors | ≈5 | Lower for account rate/quota limits and shared entities |
| Web research | Up to global max | Disjoint entity batches/dimensions; merge serially |

The included dispatcher supports only 1–10 workers and does not enforce tool caps. Set `--workers` within its maximum and the user's chosen global limit; split tool-specific waves manually. For a higher global maximum, use an otherwise verified executor.

## Quota-aware scheduling
Prefer **one inventory pass, then targeted reads** by saved IDs. Budget inventory/search + import/creation + read-back/final verification + bounded retry allowance. Separate import and verification packets if their call estimate exceeds the remaining window; schedule verification for the next window.

On quota exhaustion, stop that connector's calls across agents. Record error evidence, **verified reset time with timezone and UTC**, remaining work/IDs, call estimate and setup version. If reset is known and retry already authorized, schedule a background sleep-then-dispatch after reset with a small margin, following `references/orchestration.md`. Continue independent work; report actual scheduler PID/log. A sleeping scheduler is SCHEDULED, not DISPATCHED.

If reset is UNKNOWN, access/approval is missing, or background survival is unavailable, save a ready retry packet and report PLANNED/BLOCKED with the missing condition. Never invent a reset or a scheduled job. Retry only remaining work, re-probe before dependent operations and stop/report a failed bounded retry. Scheduling never expands sharing, mutation or spending permission.

## Blocked-step report
Record tool/operation, error/approval/quota evidence, completed artifacts/IDs, **exact unverified work**, earliest verified resume time and scheduler state/PID/log (or why unavailable). If reset is unknown, say UNKNOWN and name the probe/interactive action needed. Preserve checkpoints; an imported but unread task is not VERIFIED.
