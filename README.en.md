# Art Director

[Русский](README.md) · English

Art Director is a Claude Code skill that helps take a visual project from an idea to a finished result. It reviews the project, suggests a visual direction, and turns it into clear tasks for Codex. Once the work is done, it checks how everything looks and behaves and suggests specific fixes.

It works with websites, app interfaces, and images.

## What it can do

- Review a project, its constraints, and visual references.
- Plan composition, typography, colors, imagery, and motion.
- Prepare a small concept sketch to agree on the direction.
- Write detailed tasks for Codex with clear acceptance criteria.
- Coordinate independent tasks across agents.
- Review appearance, responsive layouts, interactions, and accessibility.
- Plan image generation and compositing, compare variants, and check details.

Running tasks through agents requires an installed and configured Codex CLI. Image generators, Photoshop, and other tools are connected separately when needed for a task.

The repository contains instructions, blank templates, helper scripts, and tests. It includes no completed project examples or client images.

## Installation

Download the repository and run this from the `art-director` folder:

```bash
python3 scripts/install.py --scope personal
```

The skill will be installed in `~/.claude/skills/art-director`. To install it for a single project:

```bash
python3 scripts/install.py --scope project --project /path/to/project
```

The installer preserves existing files and refuses to overwrite an installed skill. You can manually merge the `CLAUDE.md` and `AGENTS.md` templates into your project instructions.

## Usage

In Claude Code, run `/art-director` and describe your task. Available modes:

- `brief` — understand the task and propose a direction.
- `plan` — prepare implementation tasks.
- `execute` — run the tasks.
- `image` — work on images.
- `review` — check the result.

The dispatcher shows a plan first. Execution requires the explicit flags `--execute --approve-sharing-code`; it does not automatically publish or merge changes. See the [dispatch guide](references/orchestration.md) for details.

## Package checks

```bash
python3 -m unittest discover -s tests -v
```

The tests use a local fake Codex executor and do not call any models.

See [ATTRIBUTION.md](ATTRIBUTION.md) for sources and acknowledgments.
