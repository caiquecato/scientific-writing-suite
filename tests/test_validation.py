"""Structural checks protect packaging invariants, not scientific truth."""
import importlib.util
import tempfile
import unittest
from pathlib import Path

SPEC = importlib.util.spec_from_file_location("suite_validation", Path(__file__).resolve().parents[1] / "scripts" / "validate.py")
validation = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(validation)

class PackageValidationTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(dir=Path(__file__).resolve().parent)
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        for name in validation.SKILLS:
            directory = self.root / "skills" / name
            directory.mkdir(parents=True)
            (directory / "SKILL.md").write_text(
                f"---\nname: {name}\ndescription: Use when reviewing scientific material.\nlicense: MIT\n---\n\n"
                "# Example\n\n## Integrity contract\n\nGround claims in evidence.\n\n## Task\n\nReturn the requested work.\n",
                encoding="utf-8-sig"
            )

    def errors(self):
        return validation.validate_skills(self.root)

    def test_valid_bom_encoded_standalone_folders(self):
        self.assertEqual(self.errors(), [])

    def test_missing_module_is_reported(self):
        (self.root / "skills" / "scientific-writing-draft" / "SKILL.md").unlink()
        self.assertTrue(any("Missing SKILL.md" in e for e in self.errors()))

    def test_directory_and_frontmatter_must_match(self):
        p = self.root / "skills" / "scientific-writing" / "SKILL.md"
        p.write_text(p.read_text(encoding="utf-8-sig").replace("name: scientific-writing\n", "name: wrong-name\n"), encoding="utf-8-sig")
        self.assertTrue(any("Name mismatch" in e for e in self.errors()))

    def test_contract_drift_is_reported(self):
        p = self.root / "skills" / "scientific-writing-draft" / "SKILL.md"
        p.write_text(p.read_text(encoding="utf-8-sig").replace("Ground claims in evidence.", "Invent missing details."), encoding="utf-8-sig")
        self.assertTrue(any("Contract differs" in e for e in self.errors()))

    def test_missing_local_reference_is_reported(self):
        p = self.root / "skills" / "scientific-writing-paraphrase" / "SKILL.md"
        p.write_text(p.read_text(encoding="utf-8-sig") + "\n[Guide](references/missing.md)\n", encoding="utf-8-sig")
        self.assertTrue(any("Broken local link" in e for e in self.errors()))

    def test_cross_folder_dependency_is_rejected(self):
        p = self.root / "skills" / "scientific-writing-paraphrase" / "SKILL.md"
        p.write_text(p.read_text(encoding="utf-8-sig") + "\n[Contract](../scientific-writing/SKILL.md)\n", encoding="utf-8-sig")
        self.assertTrue(any("Nonlocal skill dependency" in e for e in self.errors()))

    def test_executable_payload_is_rejected(self):
        p = self.root / "skills" / "scientific-writing-draft" / "run.py"
        p.write_text("print('unexpected payload')\n", encoding="utf-8-sig")
        self.assertTrue(any("Unexpected installed file" in e for e in self.errors()))

if __name__ == "__main__":
    unittest.main()
