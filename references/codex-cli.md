# Codex CLI dispatch contract

Authoritative references:
- https://learn.chatgpt.com/docs/cli/reference (Codex CLI `exec` reference)
- https://github.com/openai/codex/blob/main/codex-rs/exec/src/cli.rs (CLI argument definitions)
- https://code.claude.com/docs/en/skills (Claude skills format and paths)

Verify commands against the installed CLI and official documentation before dispatch. Use the documented `codex exec` entry point.

## Preflight

```bash
command -v codex
codex --version
codex exec --help
command -v git
git status --porcelain
```

Check configured authentication and security constraints on the actual machine. A CLI binary being present is NOT proof of active Codex authorization. Do not echo secrets into terminal/logs.

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
3. **Do not say Codex was run or automatically replace Codex with Claude coding.** Only switch executor when user explicitly requests it.

## Shell portability
Samples are POSIX shell; use the included Python dispatcher for cross-platform task launching. Windows Git/worktrees, executable name, subprocess environment and file paths must be verified on that machine. PowerShell callers may need to adjust redirection and path syntax; do not claim samples are universal.

## Integration is Git, not an invented Codex operation
After reviewer approval, integrator may use `git merge --no-ff codex/TASK-101` (ONLY if branch work is committed), or selective cherry-pick/patch using inspected diffs. `codex exec` often leaves uncommitted changes in its worktree; **commit intentionally and with consent**, after checking scope, tests and authorship. Merge sequencing and final QA are integrator responsibilities. No automatic merge is provided by this skill.

## Version-dependent features (verify locally)
- **Attach images** to a task with `-i <file>` (repeatable); put `-- -` before stdin when using `-i`.
- **Non-git folders** need `--skip-git-repo-check`. **Network** for MCP/HTTP from the sandbox: `-c sandbox_workspace_write.network_access=true`.
- **Built-in image generation:** verify the output location and dimensions in the active environment. Copy approved outputs into the project and derive resizing or upscaling from the required final size.
- **MCP tools need approval** in `exec` mode, which defaults to "never" → mutating calls are rejected ("approval policy is
  never"). Per-server fix: in `~/.codex/config.toml` under `[mcp_servers.<name>]` add `default_tools_approval_mode = "approve"`
  (only with the user's explicit consent; back up the config first). Register a server with
  `codex mcp add <name> --env K=V -- <command> <args>`; verify with `codex mcp list` and a tiny probe run (ping + create/close).
- `--approve-for-me` routes approvals to automatic review but **cannot be combined with `--sandbox`**.
- Disable a server for one run: `-c 'mcp_servers.<name>.enabled=false'` — but NOT for plugin-provided servers (e.g.
  `cua_repl`): overriding them breaks config loading ("invalid transport").
- Computer use (desktop/browser control) is available to agents through the `cua_repl` MCP when the Codex app is installed;
  probe with a read-only screenshot request first.
- The sandbox blocks AppleEvents (`osascript` to apps) → drive desktop apps through their MCP servers, not scripts.
- Cost/size: the stderr log ends with `tokens used` + a number — record it per run.
