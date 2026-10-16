# Codex CLI dispatch contract

Use the installed CLI version and help output to verify commands and arguments before dispatch. Adapt flags to the actual environment.

## Preflight

```bash
command -v codex
codex --version
codex exec --help
command -v git
git status --porcelain
```

Read current `PROJECT-SETUP.md`; honor its agent policy and global/per-tool caps. Run the capability probe in `references/context-audit.md` and consult `references/tooling-limits.md`. Check configured authentication and security constraints on the actual machine. A CLI binary being present is NOT proof of active Codex authorization. Do not echo secrets into terminal/logs.

## One worktree / one Codex invocation (Unix shell)

```bash
# From a clean project repo, after contract files are integrated:
BASE_SHA="$(git rev-parse HEAD)"
mkdir -p ../project-codex-worktrees
git worktree add -b codex/TASK-101 ../project-codex-worktrees/TASK-101 "$BASE_SHA"
REPORT_ROOT="$(pwd)/../project-codex-runs/TASK-101"
mkdir -p "$REPORT_ROOT"

# Codex reads complete TASK.md from stdin; --sandbox limits writes to its workspace.
# Record real exit code and report; do not claim acceptance from exit 0.
codex exec \
  -C "$(realpath ../project-codex-worktrees/TASK-101)" \
  --sandbox workspace-write \
  --output-last-message "$REPORT_ROOT/report.txt" \
  - < docs/art-direction/tasks/TASK-101.md \
  > "$REPORT_ROOT/stdout.log" \
  2> "$REPORT_ROOT/stderr.log"
STATUS=$?
printf 'codex exit=%s\n' "$STATUS"
```

`-C/--cd`, `--sandbox workspace-write`, `-o/--output-last-message`, `PROMPT=-` (read stdin), and optional `--json` are documented. As of this reference `--full-auto` is a **deprecated compatibility flag**, so it is intentionally not used. The **current installed version must be checked** before changing flags. `--dangerously-bypass-approvals-and-sandbox` is explicitly forbidden here; only use sandboxed defaults.

For CI optional `--json` streams JSONL events, but do not parse assumed undocumented event shapes as completion proof. Use subprocess exit code, resulting Git diff and independent tests.

## Fallback when Codex CLI unavailable
1. Mark tasks `PLANNED/BLOCKED`; list missing binary/auth/permissions precisely.
2. Output complete individual TASK.md files, DAG, accepted design contract, and the exact safe manual invocation.
3. **Do not say Codex was run or automatically substitute another executor.** Only switch executor when user explicitly requests it.

## Shell portability
Samples are POSIX shell; use the included Python dispatcher for cross-platform task launching. Windows Git/worktrees, executable name, subprocess environment and file paths must be verified on that machine. PowerShell callers may need to adjust redirection and path syntax; do not claim samples are universal.

## Integration is Git, not an invented Codex operation
After reviewer approval, integrator may use `git merge --no-ff codex/TASK-101` (ONLY if branch work is committed), or selective cherry-pick/patch using inspected diffs. `codex exec` often leaves uncommitted changes in its worktree; **commit intentionally and with consent**, after checking scope, tests and authorship. Merge sequencing and final QA are integrator responsibilities. No automatic merge is provided by this skill.

## Version-dependent capabilities
- Verify image attachment, non-Git execution and network configuration against the installed CLI before using them. Record required permissions in PROJECT-SETUP.
- For generated images, verify actual output paths, dimensions and file types; copy approved outputs into the project. Derive resizing from the required final size.
- Noninteractive runs cannot obtain new approvals. Probe required operations separately; use an authorized interactive session or a permitted create-only flow where appropriate. Do not bypass approval policy or silently change global settings.
- Inventory tools in the actual executor session; a tool available in the host UI may be absent from the CLI. Probe approved integrations read-only before dependent work.
- Configure or register integrations only within the authorized scope. Use each tool's supported interface for desktop/browser work and serialize shared sessions.
- Record usage from actual logs when available. Verify dependency access, local-server access and test execution in each worktree; treat blocked checks as unverified.

## Runner and connector budgets
The included runner accepts 1–10 workers and has no per-tool scheduler. Use `--workers` within its limit and the recorded user maximum; split shared-tool waves manually. Design-tool and task-tracker quotas, browser profile/sign-in/capture limits and web-generator downloads are detailed in `references/tooling-limits.md`. Report exact unverified work and verified resume time (UNKNOWN if not known) when a quota or approval blocks execution.
