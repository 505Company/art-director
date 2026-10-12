"""Unit and local fake-executor tests (never call a real remote Codex agent)."""
from __future__ import annotations
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest import mock

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("dispatch_codex", ROOT / "scripts" / "dispatch_codex.py")
mod = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(mod)


def run(*args, cwd=None):
    return subprocess.run(args, cwd=cwd, text=True, capture_output=True, check=True)


class ManifestTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.project = self.root / "site"
        self.project.mkdir()
        run("git", "init", "-q", str(self.project))
        run("git", "config", "user.email", "test@example.local", cwd=self.project)
        run("git", "config", "user.name", "Test Runner", cwd=self.project)
        task_dir = self.project / "docs" / "art-direction" / "tasks"
        task_dir.mkdir(parents=True)
        (task_dir / "TASK-101.md").write_text(
            "# TASK-101\nBASE_SHA: resolved by runtime\nAllowed: src/components/hero/**\nAC-101-01: dummy test\n",
            encoding="utf-8",
        )
        (self.project / "README.md").write_text("project test fixture\n")
        run("git", "add", ".", cwd=self.project)
        run("git", "commit", "-qm", "baseline", cwd=self.project)
        self.manifest = self.root / "batch.json"
        self.batch = {"base_sha": "HEAD", "tasks": [{"id": "TASK-101", "spec": "docs/art-direction/tasks/TASK-101.md", "allow": ["src/components/hero/**"], "depends_on": []}]}
        self.write()

    def tearDown(self):
        self.temp.cleanup()

    def write(self):
        self.manifest.write_text(json.dumps(self.batch), encoding="utf-8")

    def test_clean_path_and_scope(self):
        self.assertTrue(mod.allows("src/components/hero/**", "src/components/hero/Hero.tsx"))
        self.assertFalse(mod.allows("src/components/hero/**", "src/components/features/Steps.tsx"))
        self.assertTrue(mod.scopes_overlap("src/components/**", "src/components/hero/**"))
        self.assertFalse(mod.scopes_overlap("src/components/features/**", "src/components/hero/**"))
        for bad in ("../outside", "/etc/passwd", "src/**", "src/thing/*.tsx"):
            with self.assertRaises(ValueError):
                mod.clean_relative(bad, wildcard=True)

    def test_protected_scopes_rejected(self):
        for scope in ("src/styles/tokens.css", "src/App.tsx", "docs/.env", ".claude/skills/**"):
            with self.subTest(scope=scope):
                self.batch["tasks"][0]["allow"] = [scope]
                self.write()
                with self.assertRaises(ValueError):
                    mod.get_manifest(self.manifest, self.project)

    def test_manifest_parsing(self):
        tasks, sha = mod.get_manifest(self.manifest, self.project)
        self.assertEqual(len(tasks), 1)
        self.assertEqual(sha, run("git", "rev-parse", "HEAD", cwd=self.project).stdout.strip())

    def test_parallel_overlap_rejected(self):
        self.batch["tasks"].append({"id": "TASK-102", "spec": "docs/art-direction/tasks/TASK-101.md", "allow": ["src/components/**"], "depends_on": []})
        self.write()
        with self.assertRaises(ValueError):
            mod.get_manifest(self.manifest, self.project)

    def test_dependent_task_rejected(self):
        self.batch["tasks"][0]["depends_on"] = ["TASK-100"]
        self.write()
        with self.assertRaisesRegex(ValueError, "independent wave"):
            mod.get_manifest(self.manifest, self.project)

    def test_plan_zero_side_effects(self):
        rc = mod.main(["--project", str(self.project), "--manifest", str(self.manifest)])
        self.assertEqual(rc, 0)
        self.assertFalse((self.root / "site-codex-worktrees").exists())

    def test_execute_requires_opt_in(self):
        rc = mod.main(["--project", str(self.project), "--manifest", str(self.manifest), "--execute"])
        self.assertEqual(rc, 2)
        self.assertFalse((self.root / "site-codex-worktrees").exists())

    def test_execute_fake_codex_and_scope_evidence(self):
        fakebin = self.root / "bin"
        fakebin.mkdir()
        fake = fakebin / "codex"
        fake.write_text('''#!/usr/bin/env python3
import pathlib, sys, os
args=sys.argv[1:]
if args == ['exec','--help']:
    print('Options: --sandbox --output-last-message -C')
    sys.exit(0)
if args[0] != 'exec': sys.exit(4)
wt=pathlib.Path(args[args.index('-C')+1])
report=pathlib.Path(args[args.index('--output-last-message')+1])
prompt=sys.stdin.read()
assert 'FULL WORK ORDER:' in prompt
assert 'APPROVED_BASE_SHA:' in prompt
if os.environ.get('MOCK_CODEX_OUTSIDE'):
    path=wt / 'README.md'
else:
    path=wt / 'src/components/hero/Hero.tsx'
path.parent.mkdir(parents=True,exist_ok=True)
path.write_text('export const Hero = () => null;\\n')
report.write_text('IMPLEMENTED (FAKE): no tests run')
print('fake codex complete')
''', encoding="utf-8")
        fake.chmod(0o755)
        with mock.patch.dict(os.environ, {"PATH": str(fakebin) + os.pathsep + os.environ["PATH"]}):
            rc = mod.main(["--project", str(self.project), "--manifest", str(self.manifest), "--execute", "--approve-sharing-code", "--workers", "1"])
        self.assertEqual(rc, 0)
        files = list((self.root / "site-codex-runs").rglob("results.json"))
        self.assertEqual(len(files), 1)
        result = json.loads(files[0].read_text())
        self.assertEqual(result["results"][0]["status"], "CODEX_REPORTED_NOT_REVIEWED")
        self.assertEqual(result["results"][0]["changed_paths"], ["src/components/hero/Hero.tsx"])
        self.assertTrue((self.root / "site-codex-worktrees" / "TASK-101" / "src/components/hero/Hero.tsx").exists())


    def test_three_agent_wave_rejects_out_of_scope_change(self):
        # Spawn three local fake Codex processes, each in a different worktree.
        spec_dir = self.project / "docs" / "art-direction" / "tasks"
        for task_id in ("TASK-102", "TASK-104"):
            (spec_dir / f"{task_id}.md").write_text(
                f"# {task_id}\nBASE_SHA: runtime\nAC-{task_id.split('-')[1]}-01: pass\n", encoding="utf-8"
            )
        run("git", "add", ".", cwd=self.project)
        run("git", "commit", "-qm", "add two independent work orders", cwd=self.project)
        self.batch["tasks"] = [
            {"id": "TASK-101", "spec": "docs/art-direction/tasks/TASK-101.md", "allow": ["src/components/hero/**"], "depends_on": []},
            {"id": "TASK-102", "spec": "docs/art-direction/tasks/TASK-102.md", "allow": ["src/lib/motion/**"], "depends_on": []},
            {"id": "TASK-104", "spec": "docs/art-direction/tasks/TASK-104.md", "allow": ["src/components/features/**"], "depends_on": []},
        ]
        self.write()
        fakebin = self.root / "bin"
        fakebin.mkdir()
        fake = fakebin / "codex"
        fake.write_text('''#!/usr/bin/env python3
import pathlib, sys, re
args = sys.argv[1:]
if args == ['exec', '--help']:
    print('Options: --sandbox --output-last-message -C')
    sys.exit(0)
wt = pathlib.Path(args[args.index('-C') + 1])
report = pathlib.Path(args[args.index('--output-last-message') + 1])
match = re.search(r'TASK: (TASK-[0-9]+)', sys.stdin.read())
assert match, 'missing task ID'
target = {'TASK-101': 'src/components/hero/Hero.tsx',
          'TASK-102': 'src/lib/motion/easing.ts',
          'TASK-104': 'README.md'}[match.group(1)]
p = wt / target
p.parent.mkdir(parents=True, exist_ok=True)
p.write_text('// fake executor\\n')
report.write_text('stub completed (not visually validated)')
''', encoding="utf-8")
        fake.chmod(0o755)
        with mock.patch.dict(os.environ, {"PATH": str(fakebin) + os.pathsep + os.environ["PATH"]}):
            rc = mod.main(["--project", str(self.project), "--manifest", str(self.manifest),
                           "--execute", "--approve-sharing-code", "--workers", "3"])
        self.assertEqual(rc, 2)  # Batch fails if ANY agent exceeded permitted files.
        reports = list((self.root / "site-codex-runs").rglob("results.json"))
        self.assertEqual(len(reports), 1)
        results = json.loads(reports[0].read_text(encoding="utf-8"))
        by_id = {entry["id"]: entry for entry in results["results"]}
        self.assertEqual(set(by_id), {"TASK-101", "TASK-102", "TASK-104"})
        self.assertEqual(by_id["TASK-101"]["status"], "CODEX_REPORTED_NOT_REVIEWED")
        self.assertEqual(by_id["TASK-102"]["status"], "CODEX_REPORTED_NOT_REVIEWED")
        self.assertEqual(by_id["TASK-104"]["status"], "FAILED_SCOPE")
        self.assertEqual(by_id["TASK-104"]["outside_scope"], ["README.md"])
        for task_id in by_id:
            self.assertTrue((self.root / "site-codex-worktrees" / task_id).exists())
        self.assertEqual(run("git", "status", "--porcelain", cwd=self.project).stdout, "")


class PackageTests(unittest.TestCase):
    def test_skill_frontmatter_and_links(self):
        body = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertTrue(body.startswith("---\n"))
        fm = body.split("---", 2)[1]
        self.assertIn("name: art-director", fm)
        self.assertIn("description:", fm)
        self.assertIn("Codex CLI", fm)
        for path in ["README.md", "ATTRIBUTION.md", "templates/CLAUDE.md", "templates/AGENTS.md", "references/codex-cli.md", "references/visual-qa.md", "references/image-production.md", "templates/image-task.md", "scripts/dispatch_codex.py", "scripts/install.py"]:
            self.assertTrue((ROOT / path).exists(), path)

if __name__ == "__main__":
    unittest.main()
