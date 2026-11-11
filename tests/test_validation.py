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
        license_data = (Path(__file__).resolve().parents[1] / "LICENSE").read_bytes()
        (self.root / "LICENSE").write_bytes(license_data)
        for name in validation.SKILLS:
            directory = self.root / "skills" / name
            directory.mkdir(parents=True)
            (directory / "LICENSE").write_bytes(license_data)
            (directory / "SKILL.md").write_text(
                f"---\nname: {name}\ndescription: Use when reviewing scientific material.\nlicense: MIT\n---\n\n"
                "# Example\n\n## Integrity contract\n\nGround claims in evidence.\n\n## Task\n\nReturn the requested work.\n",
                encoding="utf-8"
            )

    def errors(self):
        return validation.validate_skills(self.root)

    def test_valid_bom_free_standalone_folders(self):
        self.assertEqual(self.errors(), [])

    def test_skill_entrypoint_rejects_utf8_bom(self):
        p = self.root / "skills" / "scientific-writing" / "SKILL.md"
        p.write_bytes(b"\xef\xbb\xbf" + p.read_bytes())
        self.assertTrue(any("UTF-8 BOM" in e for e in self.errors()))

    def test_agent_metadata_rejects_utf8_bom(self):
        folder = self.root / "skills" / "scientific-writing" / "agents"
        folder.mkdir()
        (folder / "openai.yaml").write_bytes(b"\xef\xbb\xbfinterface:\n  display_name: Example\n")
        self.assertTrue(any("UTF-8 BOM" in e for e in self.errors()))

    def test_standalone_license_is_required(self):
        p = self.root / "skills" / "scientific-writing-draft" / "LICENSE"
        p.unlink()
        self.assertTrue(any("Missing standalone license" in e for e in self.errors()))

    def test_standalone_license_matches_repository_grant(self):
        p = self.root / "skills" / "scientific-writing-draft" / "LICENSE"
        p.write_bytes(b"Different permission terms")
        self.assertTrue(any("Standalone license differs" in e for e in self.errors()))

    def test_missing_module_is_reported(self):
        (self.root / "skills" / "scientific-writing-draft" / "SKILL.md").unlink()
        self.assertTrue(any("Missing SKILL.md" in e for e in self.errors()))

    def test_directory_and_frontmatter_must_match(self):
        p = self.root / "skills" / "scientific-writing" / "SKILL.md"
        p.write_text(p.read_text(encoding="utf-8").replace("name: scientific-writing\n", "name: wrong-name\n"), encoding="utf-8")
        self.assertTrue(any("Name mismatch" in e for e in self.errors()))

    def test_contract_drift_is_reported(self):
        p = self.root / "skills" / "scientific-writing-draft" / "SKILL.md"
        p.write_text(p.read_text(encoding="utf-8").replace("Ground claims in evidence.", "Invent missing details."), encoding="utf-8")
        self.assertTrue(any("Contract differs" in e for e in self.errors()))

    def test_missing_local_reference_is_reported(self):
        p = self.root / "skills" / "scientific-writing-paraphrase" / "SKILL.md"
        p.write_text(p.read_text(encoding="utf-8") + "\n[Guide](references/missing.md)\n", encoding="utf-8")
        self.assertTrue(any("Broken local link" in e for e in self.errors()))

    def test_cross_folder_dependency_is_rejected(self):
        p = self.root / "skills" / "scientific-writing-paraphrase" / "SKILL.md"
        p.write_text(p.read_text(encoding="utf-8") + "\n[Contract](../scientific-writing/SKILL.md)\n", encoding="utf-8")
        self.assertTrue(any("Nonlocal skill dependency" in e for e in self.errors()))

    def test_executable_payload_is_rejected(self):
        p = self.root / "skills" / "scientific-writing-draft" / "run.py"
        p.write_text("print('unexpected payload')\n", encoding="utf-8")
        self.assertTrue(any("Unexpected installed file" in e for e in self.errors()))

if __name__ == "__main__":
    unittest.main()
