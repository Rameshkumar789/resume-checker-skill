import importlib.util
from pathlib import Path
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / "scripts/validate_bundle.py"
spec = importlib.util.spec_from_file_location("bundle_checker", SCRIPT)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class BundleChecks(unittest.TestCase):
    def fixture(self, root):
        folder = root / "skills/example-skill"
        (folder / "agents").mkdir(parents=True)
        (folder / "SKILL.md").write_text(
            '---\nname: example-skill\ndescription: "Review example work."\n---\n\n# Example\n'
        )
        (folder / "agents/openai.yaml").write_text(
            'interface:\n  display_name: "Example"\n'
            '  short_description: "Review verified example material"\n'
            '  default_prompt: "Use $example-skill to review work."\n'
        )
        return folder

    def test_clean_fixture_passes(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.fixture(root)
            self.assertEqual(module.validate(root), [])

    def test_missing_reference_is_reported(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            folder = self.fixture(root)
            with (folder / "SKILL.md").open("a") as out:
                out.write("\n[Guide](references/missing.md)\n")
            self.assertTrue(any("broken/outside reference" in x for x in module.validate(root)))

    def test_candidate_email_is_detected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.fixture(root)
            (root / "notes.md").write_text("candidate" + "@" + "example.com")
            self.assertTrue(any("candidate data" in x for x in module.validate(root)))

    def test_private_export_is_detected(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.fixture(root)
            (root / ("sample" + ".pdf")).write_bytes(b"example")
            self.assertTrue(any("private/artifact" in x for x in module.validate(root)))


if __name__ == "__main__":
    unittest.main()
