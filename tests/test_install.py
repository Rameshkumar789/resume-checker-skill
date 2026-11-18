import importlib.util
from pathlib import Path
import re
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("installer", ROOT / "scripts/install.py")
installer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(installer)


class InstallChecks(unittest.TestCase):
    def test_entire_package_installs_and_all_module_links_resolve(self):
        with tempfile.TemporaryDirectory() as temp:
            destination = Path(temp) / "resume-checker"
            installed = installer.install(ROOT, destination).resolve()
            self.assertTrue((installed / "SKILL.md").exists())
            self.assertEqual(len(list((installed / "skills").glob("*/SKILL.md"))), 10)
            for manifest in installed.rglob("SKILL.md"):
                for link in re.findall(r"\]\(([^)]+)\)", manifest.read_text()):
                    if link.startswith(("https://", "http://", "#")):
                        continue
                    target = (manifest.parent / link).resolve()
                    self.assertTrue(target.is_relative_to(installed))
                    self.assertTrue(target.exists(), (manifest, link))
            self.assertFalse((installed / ".git").exists())

    def test_existing_install_is_preserved(self):
        with tempfile.TemporaryDirectory() as temp:
            destination = Path(temp) / "resume-checker"
            destination.mkdir()
            marker = destination / "existing.txt"
            marker.write_text("keep")
            with self.assertRaises(FileExistsError):
                installer.install(ROOT, destination)
            self.assertEqual(marker.read_text(), "keep")

    def test_private_work_is_not_copied(self):
        with tempfile.TemporaryDirectory() as temp:
            source = Path(temp) / "source"
            source.mkdir()
            (source / "SKILL.md").write_text("Example")
            for folder in ["private", "outputs", ".git", "__pycache__"]:
                (source / folder).mkdir()
                (source / folder / "data.txt").write_text("private example")
            (source / ".env").write_text("example")
            destination = Path(temp) / "resume-checker"
            installer.install(source, destination)
            self.assertEqual({p.name for p in destination.iterdir()}, {"SKILL.md"})

    def test_install_inside_source_is_rejected(self):
        with self.assertRaises(ValueError):
            installer.install(ROOT, ROOT / "nested-install")

    def test_project_wrappers_load_the_same_portable_entry(self):
        for prefix in [".agents", ".claude"]:
            manifest = ROOT / prefix / "skills/resume-checker/SKILL.md"
            target = re.search(r"\]\(([^)]+)\)", manifest.read_text()).group(1)
            self.assertEqual((manifest.parent / target).resolve(), ROOT / "SKILL.md")
        self.assertEqual((ROOT / "CLAUDE.md").read_text().strip(), "@AGENTS.md")


if __name__ == "__main__":
    unittest.main()
