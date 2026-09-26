import importlib.util
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch


SPEC = importlib.util.spec_from_file_location("installer", Path(__file__).resolve().parents[1] / "scripts/install.py")
installer = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(installer)


class InstallTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="dev-mind-test-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)

    def run_install(self, *args):
        return installer.main(["--project", str(self.root), *args])

    def snapshot(self):
        return {str(p.relative_to(self.root)): p.read_bytes() for p in self.root.rglob("*") if p.is_file()}

    def test_both_preserves_instructions_and_memory_and_is_idempotent(self):
        (self.root / "AGENTS.md").write_text("Keep my instructions.\n", encoding="utf-8")
        (self.root / "CLAUDE.md").write_text("My Claude rules.", encoding="utf-8")
        (self.root / "DEV_MIND.md").write_text("Existing memory.", encoding="utf-8")
        self.assertEqual(self.run_install(), 0)
        before = self.snapshot()
        self.assertEqual(self.run_install(), 0)
        self.assertEqual(before, self.snapshot())
        self.assertTrue((self.root / "AGENTS.md").read_text().startswith("Keep my instructions.\n"))
        self.assertTrue((self.root / "CLAUDE.md").read_text().startswith("My Claude rules."))
        self.assertEqual((self.root / "DEV_MIND.md").read_text(), "Existing memory.")
        for host in (".agents", ".claude"):
            self.assertEqual((self.root / host / "skills/dev-mind/SKILL.md").read_bytes(), (installer.SOURCE / "SKILL.md").read_bytes())

    def test_dry_run_writes_nothing(self):
        self.assertEqual(self.run_install("--dry-run"), 0)
        self.assertEqual(list(self.root.iterdir()), [])

    def test_single_host(self):
        self.assertEqual(self.run_install("--agent", "claude"), 0)
        self.assertFalse((self.root / ".agents").exists())
        self.assertFalse((self.root / "AGENTS.md").exists())
        self.assertTrue((self.root / "CLAUDE.md").exists())

    def test_modified_skill_blocks_all_writes(self):
        path = self.root / ".claude/skills/dev-mind/SKILL.md"
        path.parent.mkdir(parents=True)
        path.write_text("Local customizations.")
        before = self.snapshot()
        self.assertEqual(self.run_install(), 1)
        self.assertEqual(before, self.snapshot())

    def test_symlink_parent_is_rejected(self):
        with tempfile.TemporaryDirectory() as outside:
            (self.root / ".agents").symlink_to(outside, target_is_directory=True)
            self.assertEqual(self.run_install(), 1)
            self.assertEqual(list(Path(outside).iterdir()), [])
            self.assertFalse((self.root / "DEV_MIND.md").exists())

    def test_memory_symlink_is_rejected_before_install(self):
        (self.root / "DEV_MIND.md").symlink_to(self.root / "missing.md")
        self.assertEqual(self.run_install(), 1)
        self.assertFalse((self.root / ".agents").exists())

    def test_custom_or_malformed_bridge_preserved(self):
        for body in (installer.START, installer.START + "\nCustom instructions\n" + installer.END):
            with self.subTest(body=body):
                (self.root / "AGENTS.md").write_text(body)
                before = self.snapshot()
                self.assertEqual(self.run_install(), 1)
                self.assertEqual(before, self.snapshot())

    def test_parent_file_rejected_before_install(self):
        (self.root / ".claude").write_text("Not a directory")
        before = self.snapshot()
        self.assertEqual(self.run_install(), 1)
        self.assertEqual(before, self.snapshot())

    def test_codex_only_preserves_claude_configuration(self):
        (self.root / "CLAUDE.md").write_bytes(b"Private Claude configuration\r\n")
        self.assertEqual(self.run_install("--agent", "codex"), 0)
        self.assertEqual((self.root / "CLAUDE.md").read_bytes(), b"Private Claude configuration\r\n")
        self.assertFalse((self.root / ".claude").exists())

    def test_non_utf8_instructions_stop_before_writes(self):
        (self.root / "CLAUDE.md").write_bytes(b"\xff\xfe")
        before = self.snapshot()
        self.assertEqual(self.run_install(), 1)
        self.assertEqual(before, self.snapshot())

    def test_missing_skill_entrypoint_stops_before_writes(self):
        with tempfile.TemporaryDirectory() as source:
            source = Path(source)
            (source / "assets").mkdir()
            (source / "assets/DEV_MIND.md").write_text("Template")
            with patch.object(installer, "SOURCE", source):
                self.assertEqual(self.run_install(), 1)
        self.assertEqual(list(self.root.iterdir()), [])

    def test_permission_error_is_reported_without_success(self):
        with patch.object(installer, "plan_install", side_effect=PermissionError("read-only")):
            self.assertEqual(self.run_install(), 1)
        self.assertEqual(list(self.root.iterdir()), [])


if __name__ == "__main__":
    unittest.main()
