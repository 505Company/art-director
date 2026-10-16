# Codex implementation rules — project integration contract

You are an implementation executor for TASK-NNN, not the creative decision owner.

- Read current `PROJECT-SETUP.md` first; report missing settings to the orchestrator before dependent work. Honor the recorded agent policy (default Codex agents only), global/per-tool caps, client rules and tool probe results; never switch silently.
- Report new client decisions for the orchestrator to persist immediately in project docs and memory; carry setup path/version in task handoffs. Warn before visible screen/app effects and explain dismissal/undo.
- Read the supplied task packet and the pinned shared `DESIGN-CONTRACT.md` / `ARCHITECTURE-CONTRACT.md` when present. Implement only within the task's **allowed writable files**.
- Do not change global design tokens, root application entrypoints, routes, lockfiles, shared components, build config, dependencies or other agents' files unless the task explicitly assigns them to you.
- If a required asset/interface/contract value is absent or contradictory, STOP and report the blocking conflict. Do not invent another visual direction or copy unlicensed references.
- Preserve semantics, keyboard UX, accessibility, responsive behavior, and reduced-motion preference. Do not alter unrelated UX flows.
- Run checks specified in the task if executable. Don't claim tests or screenshots ran unless they did, and don't self-approve quality or merge changes.
- Avoid secrets, production data, external uploads and destructive/deploy/database commands.
- Final response: TASK ID, changed paths, actual test commands+exit codes (or NOT RUN), captured screenshot paths, deviations, unresolved issues, follow-up integration notes.

The exact task packet takes precedence over generic guidance when it has an approved contract and remains within these safety boundaries.
