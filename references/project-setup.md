# Project setup — Gate −1 before work

Run first in every new project, or when required settings are missing. Propose a configuration; ask only questions that affect this run. Use the host's question UI, batch related questions, and skip answers already supplied by the user or project docs. Separate proposed defaults from confirmed choices; silence is not consent to optional agents, spending or data sharing.

## Profiles and inheritance
When a previous `PROJECT-SETUP.md` is available, offer **“Same settings as <previous project>?”** in the user's language, naming the setup path/version. On acceptance, copy applicable settings into the new setup and ask only the deltas: engagement, scope, destinations, tools, budgets or permissions that differ. Record the inherited profile, confirmation source and overrides; retain unresolved items as UNKNOWN. Do not infer acceptance from silence or carry another project's contacts, confidential files or disclosure permission beyond its recorded scope. Re-probe account access and quotas at Gate 0 even when settings are inherited.

**Engagement type changes defaults**, independently of production mode (UI, images, research or other work):

| Engagement | Default output / conversation |
|---|---|
| Cold outreach | Validated research + message brief; T1–T5 draft chain where outreach is requested |
| Warm lead | Validated dossier + relevant response/next-step brief; agree cadence, no automatic cold chain |
| Existing client (hot) | Validated dossier; expansion options or call prep only on request; no cold T1–T5 chain |
| Inbound request (e.g. recruiter/partner approached us) | Validated dossier answering the request; expansion options or call prep only on request; no cold T1–T5 chain |
| Internal product | Discovery/decision dossier + requested production artifacts; outreach N/A unless requested |

Preserve the user's explicitly requested deliverables. For existing clients and inbound requests, **never criticise the client's team or current work**: frame help as extra capacity, a bounded collaboration or the next step. Named contractors/partners may be collaborators, not presumed competitors. Record engagement and the resulting deliverable/chain defaults before research or copy dispatch.

## Configure the run
Use `templates/project-setup.md` and offer these defaults where applicable:
- **Engagement:** choose the profile above from known context; ask only if unclear. Record relationship, requested outcome and any default override.
- **Concurrency:** global max 10; shared browser profile/computer use/raster editor 1 each; design tool 1–2; task tracker/other service connectors ≈5; web research up to global max. Lower caps for quotas, shared files and local limitations; see `references/tooling-limits.md`.
- **Agent policy:** Codex agents only by default (orchestrator-dispatched workers). Ask separately whether Claude Code subagents and/or nested Codex sub-agents are allowed. Record the exact choice; never switch silently or treat unavailable Codex as permission to substitute the orchestrator.
- **Destination:** XLSX/CSV, a task tracker, a docs/sheets tool, a design tool or a local folder. Name one source of truth and identify generated views/exports. Default to the project's existing destination, otherwise local docs/artifacts.
- **Outputs:** review pages/artifacts, decks, docs and required export formats; ask only for outputs the task needs.
- **Connectors/sign-ins:** a design tool, task tracker, docs/sheets tool, messaging app, web image generator and browsers as relevant. Identify which account/session is required and who signs in; default to the user handling sign-in. For web generators, configure a separate automation browser profile, dedicated downloads folder and user-preconfigured MCP approvals; the user signs in once and agents never type credentials. Read `references/tooling-limits.md` before using that profile. Probe actual availability in Gate 0.
- **Image generators:** the agent's built-in image generator, a web image generator (any; record the exact model/mode), or both when requested; resolution, variants and export sizes. Record tested capabilities per edit type, especially camera/viewpoint re-rendering; see `references/image-production.md` §2.1. Default to Unlimited only/no credit spend; stop if that mode is unavailable. Sign-in, purchases and account changes remain outside generator-agent scope.
- **Language/tone:** deliverables use the user's language even when sources use another language; keep source titles and quotes in their original language. Default to simple, polite, conversational, human copy. For outreach record sender identity, allowed channels, cleared cases and any chain changes; apply the engagement tone rule above.
- **Reviews:** samples before mass production, review cadence and number of rounds. Default to sample review and two correction rounds; preserve the skill's required mini-sketch and selection gates.
- **Budgets/deadlines:** agree per-run and total usage, generation limits, daily connector quotas, cost ceiling and deadline. Record actual usage and split work when it exceeds the agreed budget.
- **Confidentiality:** what may reach each external provider/agent; public/cleared cases versus NDA, regulated and tender work. Record authorization scope; setup does not override security boundaries.

## Save and maintain
1. Save answers, proposed defaults, unresolved blockers, date and version to `docs/art-direction/PROJECT-SETUP.md`, or the project's existing docs directory. Avoid duplicate sources of truth.
2. Immediately write client rules and decisions into project docs and the orchestrator's project memory. If persistent memory is unavailable, record that limitation and keep a durable project handoff pointer; do not claim memory was saved.
3. Reference the current setup path/version in **every** task spec, including research, copywriting, images and corrections. Include the applicable choices in the packet so a fresh agent needs no conversation history.
4. Let the user change settings any time. Update docs and memory immediately, version the change and revise queued/dependent tasks before dispatch. Preserve completed evidence and decision history.
5. Proceed with independent reversible preparation while required answers are pending; hold work dependent on missing permissions/settings. Finish setup when applicable choices are recorded and blocking unknowns have an owner.
