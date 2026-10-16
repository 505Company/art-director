"""Scaffold and wrapper tests in temp folders; no remote agent invocations."""
from pathlib import Path
import os
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


class NewProjectTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.project = self.root / "project with spaces"

    def tearDown(self):
        self.temp.cleanup()

    def scaffold(self, *args):
        return subprocess.run([sys.executable, str(ROOT / "scripts/new_project.py"),
                               "--project", str(self.project), *args], text=True, capture_output=True)

    def test_dry_run_and_create_preserve_existing_files(self):
        plan = self.scaffold("--dry-run")
        self.assertEqual(plan.returncode, 0, plan.stderr)
        self.assertIn("CREATE file", plan.stdout)
        self.assertFalse(self.project.exists())
        created = self.scaffold()
        self.assertEqual(created.returncode, 0, created.stderr)
        for directory in ("tasks", "findings", "runs"):
            self.assertTrue((self.project / directory).is_dir())
        setup = self.project / "docs/art-direction/PROJECT-SETUP.md"
        template = (ROOT / "templates/project-setup.md").read_text(encoding="utf-8")
        self.assertEqual(setup.read_text(encoding="utf-8"), template.replace("[Project]", self.project.name, 1))
        wrapper = self.project / "dispatch.sh"
        self.assertTrue(os.access(wrapper, os.X_OK))
        setup.write_text("user's existing setup", encoding="utf-8")
        wrapper.write_text("user's existing wrapper", encoding="utf-8")
        rerun = self.scaffold("--effort", "low")
        self.assertEqual(rerun.returncode, 0, rerun.stderr)
        self.assertEqual(setup.read_text(encoding="utf-8"), "user's existing setup")
        self.assertEqual(wrapper.read_text(encoding="utf-8"), "user's existing wrapper")

    def test_symlink_escape_rejected_before_writes(self):
        self.project.mkdir()
        outside = self.root / "outside"
        outside.mkdir()
        (self.project / "docs").symlink_to(outside, target_is_directory=True)
        result = self.scaffold()
        self.assertEqual(result.returncode, 2)
        self.assertIn("escapes project", result.stderr)
        self.assertEqual(list(outside.iterdir()), [])
        self.assertFalse((self.project / "tasks").exists())

    def test_wrapper_plan_opt_in_and_task_boundary(self):
        self.assertEqual(self.scaffold().returncode, 0)
        (self.project / "tasks/TASK-001.md").write_text("authorized test prompt", encoding="utf-8")
        wrapper = str(self.project / "dispatch.sh")
        for args, expected in ((["--dry-run", "TASK-001"], 0),
                               (["--execute", "TASK-001"], 2),
                               (["--dry-run", "../outside"], 2)):
            result = subprocess.run([wrapper, *args], text=True, capture_output=True)
            self.assertEqual(result.returncode, expected, result.stderr)
        self.assertEqual(list((self.project / "runs").iterdir()), [])

    def test_wrapper_captures_exit_logs_tokens_and_refuses_reuse(self):
        self.assertEqual(self.scaffold("--effort", "medium").returncode, 0)
        fakebin = self.root / "bin"
        fakebin.mkdir()
        fake = fakebin / "codex"
        fake.write_text('''#!/usr/bin/env python3
import pathlib, sys
args = sys.argv[1:]
assert args[:1] == ['exec']
project = pathlib.Path(args[args.index('-C') + 1])
assert pathlib.Path.cwd() == project
assert args[args.index('--sandbox') + 1] == 'workspace-write'
assert '--skip-git-repo-check' in args and args[-1] == '-'
configs = [args[i+1] for i, arg in enumerate(args) if arg == '-c']
assert configs == ['sandbox_workspace_write.network_access=true', 'web_search=live', 'model_reasoning_effort=medium']
assert sys.stdin.read() == 'fake local prompt'
report = pathlib.Path(args[args.index('-o') + 1])
report.write_text('fake executor report')
print('fake stdout')
print('tokens used\\n1234', file=sys.stderr)
sys.exit(7 if report.parent.name == 'TASK-FAIL' else 0)
''', encoding="utf-8")
        fake.chmod(0o755)
        env = dict(os.environ, PATH=str(fakebin) + os.pathsep + os.environ["PATH"])
        wrapper = str(self.project / "dispatch.sh")
        for task_id, expected in (("TASK-OK", 0), ("TASK-FAIL", 7)):
            (self.project / f"tasks/{task_id}.md").write_text("fake local prompt", encoding="utf-8")
            result = subprocess.run([wrapper, "--execute", "--approve-sharing-code", task_id],
                                    env=env, text=True, capture_output=True)
            self.assertEqual(result.returncode, expected, result.stderr)
            self.assertIn("tokens used\n1234", result.stdout)
            run = self.project / "runs" / task_id
            self.assertEqual((run / "report.txt").read_text(), "fake executor report")
            self.assertIn("fake stdout", (run / "stdout.log").read_text())
            self.assertIn("tokens used", (run / "stderr.log").read_text())
            repeat = subprocess.run([wrapper, "--execute", "--approve-sharing-code", task_id],
                                    env=env, text=True, capture_output=True)
            self.assertEqual(repeat.returncode, 2)
            self.assertIn("run already exists", repeat.stderr)
        self.assertEqual((self.project / "runs/status.log").read_text(), "TASK-OK exit=0\nTASK-FAIL exit=7\n")


if __name__ == "__main__":
    unittest.main()
