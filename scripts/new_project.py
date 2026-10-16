#!/usr/bin/env python3
"""Create an art-direction project scaffold; stdlib only, never launch agents.

Existing files are preserved. --dry-run prints actions without writing anything.
"""
from __future__ import annotations

import argparse
from pathlib import Path
import sys


WRAPPER = '''#!/bin/sh
# Run only after setup, CLI/capability preflight and sharing authorization.
# No worktree isolation or write-scope enforcement; code waves use dispatch_codex.py.
set -u
usage() {
    echo "Usage: $0 --dry-run TASK-ID [effort]" >&2
    echo "       $0 --execute --approve-sharing-code TASK-ID [effort]" >&2
    exit 2
}
[ "$#" -ge 1 ] || usage
case "$1" in
    --dry-run) mode=plan; shift ;;
    --execute)
        [ "$#" -ge 2 ] || usage
        [ "$2" = "--approve-sharing-code" ] || usage
        mode=execute; shift 2 ;;
    *) usage ;;
esac
[ "$#" -ge 1 ] && [ "$#" -le 2 ] || usage
task_id=$1
effort=${2:-__DEFAULT_EFFORT__}
case "$task_id" in
    ''|*[!A-Za-z0-9_-]*) usage ;;
esac
case "$task_id" in
    [A-Za-z0-9]*) ;;
    *) usage ;;
esac
case "$effort" in
    low|medium|high|xhigh|max|ultra) ;;
    *) usage ;;
esac
project_root=$(CDPATH= cd -P "$(dirname "$0")" && pwd) || exit 2
task_file="$project_root/tasks/$task_id.md"
run_dir="$project_root/runs/$task_id"
if [ ! -f "$task_file" ] || [ -L "$task_file" ]; then
    echo "BLOCKED: missing or symlinked task: $task_file" >&2
    exit 2
fi
if [ -e "$run_dir" ] || [ -L "$run_dir" ]; then
    echo "BLOCKED: run already exists: $run_dir; use a fresh task/run ID" >&2
    exit 2
fi
if [ "$mode" = plan ]; then
    printf 'PLAN: codex exec -C %s --sandbox workspace-write --skip-git-repo-check -c sandbox_workspace_write.network_access=true -c web_search=live -c model_reasoning_effort=%s -o %s/report.txt - < %s\\n' "$project_root" "$effort" "$run_dir" "$task_file"
    exit 0
fi
command -v codex >/dev/null 2>&1 || { echo "BLOCKED: Codex CLI not found" >&2; exit 2; }
mkdir -p "$project_root/runs" || exit 2
# mkdir without -p refuses a concurrent/repeated run of the same task.
mkdir "$run_dir" || exit 2
cd "$project_root" || exit 2
codex exec -C "$project_root" --sandbox workspace-write --skip-git-repo-check \\
    -c sandbox_workspace_write.network_access=true -c web_search=live \\
    -c "model_reasoning_effort=$effort" -o "$run_dir/report.txt" - \\
    < "$task_file" > "$run_dir/stdout.log" 2> "$run_dir/stderr.log"
run_exit=$?
printf '%s exit=%s\\n' "$task_id" "$run_exit" >> "$project_root/runs/status.log" || exit 2
awk '/tokens used/ { print; if ($0 ~ /tokens used[[:space:]]*$/ && getline > 0) print }' "$run_dir/stderr.log"
printf '%s exit=%s\\n' "$task_id" "$run_exit"
exit "$run_exit"
'''


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", required=True, type=Path, help="project folder to create or extend")
    parser.add_argument("--effort", default="high", choices=["low", "medium", "high", "xhigh", "max", "ultra"],
                        help="wrapper default; verify support for the configured model")
    parser.add_argument("--dry-run", action="store_true", help="print CREATE/SKIP actions; zero writes")
    args = parser.parse_args(argv)
    try:
        project = args.project.expanduser().resolve()
        template = Path(__file__).resolve().parents[1] / "templates" / "project-setup.md"
        setup = template.read_text(encoding="utf-8").replace(
            "# PROJECT-SETUP — [Project]", f"# PROJECT-SETUP — {project.name}", 1
        )
        directories = [project, project / "docs" / "art-direction",
                       project / "tasks", project / "findings", project / "runs"]
        files = {project / "docs" / "art-direction" / "PROJECT-SETUP.md": setup,
                 project / "dispatch.sh": WRAPPER.replace("__DEFAULT_EFFORT__", args.effort)}
        # Check every destination before creating anything, including symlinked parents.
        for path in [*directories, *files]:
            if not path.resolve().is_relative_to(project):
                raise ValueError(f"destination escapes project through symlink: {path}")
            exists = path.exists() or path.is_symlink()
            if exists and ((path in directories and not path.is_dir()) or
                           (path in files and not path.is_file())):
                raise ValueError(f"destination has wrong type: {path}")
        for directory in directories:
            exists = directory.exists()
            print(f"{'SKIP' if exists else 'CREATE'} directory {directory}")
            if not args.dry_run:
                directory.mkdir(parents=True, exist_ok=True)
        for path, content in files.items():
            exists = path.exists() or path.is_symlink()
            print(f"{'SKIP' if exists else 'CREATE'} file {path}")
            if args.dry_run or exists:
                continue
            with path.open("x", encoding="utf-8") as handle:
                handle.write(content)
            if path.name == "dispatch.sh":
                path.chmod(0o755)
        return 0
    except (OSError, ValueError) as error:
        print(f"BLOCKED: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
