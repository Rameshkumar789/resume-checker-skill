import importlib.util
from pathlib import Path
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / "scripts/check_evidence.py"
spec = importlib.util.spec_from_file_location("evidence_checker", SCRIPT)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class EvidenceChecks(unittest.TestCase):
    def test_known_user_confirmed_evidence(self):
        errors, warnings = module.check_evidence(
            {"records": [{"id": "E001", "verification": "user_confirmed"}]},
            {"engineering": {"bullets": [{"bullet": "Built a validation service.", "evidence_ids": ["E001"]}]}},
        )
        self.assertEqual((errors, warnings), ([], []))

    def test_unknown_reference_blocks_delivery(self):
        errors, _ = module.check_evidence(
            {"records": [{"id": "E001"}]},
            [{"bullet": "Built a service.", "evidence_ids": ["E404"]}],
        )
        self.assertTrue(any("unknown evidence" in error for error in errors))

    def test_duplicate_evidence_is_not_silently_overwritten(self):
        errors, _ = module.check_evidence(
            {"records": [{"id": "E001"}, {"id": "E001"}]},
            [{"bullet": "Built a service.", "evidence_ids": ["E001"]}],
        )
        self.assertTrue(any("Duplicate" in error for error in errors))

    def test_conflicting_source_requires_review(self):
        errors, warnings = module.check_evidence(
            {"records": [{"id": "E001", "verification": "conflicting"}]},
            [{"bullet": "A provisional claim.", "evidence_ids": ["E001"]}],
        )
        self.assertFalse(errors)
        self.assertTrue(warnings)

    def test_empty_map_is_not_a_success(self):
        errors, _ = module.check_evidence({"records": []}, {"bullets": []})
        self.assertTrue(errors)

    def test_malformed_ids_are_errors(self):
        errors, _ = module.check_evidence(
            {"records": [{"id": "E001"}]},
            [{"bullet": "Built a service.", "evidence_ids": "E001"}],
        )
        self.assertTrue(errors)


if __name__ == "__main__":
    unittest.main()
