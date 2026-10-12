#!/usr/bin/env python3
"""Install this skill project-wide or to ~/.claude/skills (safe: no overwrite)."""
from pathlib import Path
import argparse
import shutil
import sys


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--scope", choices=["project", "personal"], required=True)
    p.add_argument("--project", type=Path, default=Path.cwd(), help="project root for project scope")
    args = p.parse_args()
    source = Path(__file__).resolve().parents[1]
    if not (source / "SKILL.md").is_file():
        p.error("script must remain inside art-director/scripts/")
    target = ((args.project.expanduser().resolve() / ".claude" / "skills" / "art-director")
              if args.scope == "project"
              else (Path.home() / ".claude" / "skills" / "art-director"))
    if target.exists():
        print(f"Refusing to overwrite existing skill: {target}", file=sys.stderr)
        return 2
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(source, target, ignore=shutil.ignore_patterns(".git", "__pycache__", ".DS_Store", "*.pyc"))
    print(f"Installed: {target}")
    print("Important: merge templates/CLAUDE.md into the PROJECT ROOT CLAUDE.md manually; do not replace your existing instructions.")
    print("Optional: merge templates/AGENTS.md into project root AGENTS.md for Codex executors.")
    print("Start Claude Code in the repo, run /art-director and test with a planning-only brief.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
