"""Offline packaging checks. These do not assess factual correctness."""
import argparse
import re
from pathlib import Path
from urllib.parse import unquote

SKILLS = (
    "scientific-writing",
    "scientific-writing-plan",
    "scientific-writing-structure",
    "scientific-writing-draft",
    "scientific-writing-paraphrase",
    "scientific-writing-review",
    "scientific-writing-submit",
)
PUBLIC = (
    "README.md", "README.pt-BR.md", "LICENSE", "THIRD_PARTY_NOTICES.md",
    "SECURITY.md", "CONTRIBUTING.md", "CHANGELOG.md", ".gitignore",
    ".gitattributes", "CITATION.cff", "assets", "skills", "tests", "scripts/validate.py",
    "docs/sources.md", "docs/examples.md", "docs/evaluation.md", "docs/AUDITORIA-JURIDICA.md", ".github/workflows/validate.yml",
)
LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")

def contract(text):
    match = re.search(r"^## Integrity contract\n(.*?)(?=^## |\Z)", text, re.M | re.S)
    return match.group(1).strip() if match else None

def links(path, boundary):
    errors = []
    for target in LINK.findall(path.read_text(encoding="utf-8-sig")):
        target = target.strip().strip("<>")
        if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target) or target.startswith("#"):
            continue
        target = unquote(target.split("#", 1)[0])
        resolved = (path.parent / target).resolve()
        if not resolved.is_relative_to(boundary.resolve()):
            errors.append(f"Nonlocal skill dependency: {path.name} -> {target}")
        elif not resolved.exists():
            errors.append(f"Broken local link: {path.name} -> {target}")
    return errors

def validate_skills(root):
    root = Path(root)
    errors, contracts = [], {}
    repository_license = root / "LICENSE"
    license_data = repository_license.read_bytes() if repository_license.is_file() else None
    if license_data is None:
        errors.append("Missing repository license")
    directory = root / "skills"
    actual = {p.name for p in directory.iterdir() if p.is_dir()} if directory.exists() else set()
    if actual != set(SKILLS):
        errors.append(f"Skill directory mismatch: expected {len(SKILLS)}, found {len(actual)}")
    for name in SKILLS:
        folder = directory / name
        path = folder / "SKILL.md"
        standalone_license = folder / "LICENSE"
        if not standalone_license.is_file():
            errors.append(f"Missing standalone license: {name}")
        elif license_data is not None and standalone_license.read_bytes() != license_data:
            errors.append(f"Standalone license differs: {name}")
        if not path.exists():
            errors.append(f"Missing SKILL.md: {name}")
            continue
        for installed_file in folder.rglob("*"):
            if installed_file.is_file() and installed_file.suffix in {".md", ".yaml"}:
                if installed_file.read_bytes().startswith(b"\xef\xbb\xbf"):
                    errors.append(f"UTF-8 BOM is not allowed in installed metadata: {installed_file.relative_to(root)}")
        # Inspect the literal frontmatter boundary; stripping a BOM masks host incompatibility.
        text = path.read_text(encoding="utf-8")
        header = re.match(r"^---\n(.*?)\n---\n", text, re.S)
        if not header:
            errors.append(f"Invalid frontmatter boundary: {name}")
            continue
        # Validate the simple single-line metadata used by this repository;
        # full YAML validation is a separate maintainer check.
        fields = dict(re.findall(r"^([a-z][a-z-]*):[ \t]*(.*)$", header.group(1), re.M))
        if fields.get("name") != name:
            errors.append(f"Name mismatch: {name}")
        desc = fields.get("description", "")
        if not desc.startswith("Use when") or len(desc) > 1024:
            errors.append(f"Invalid discovery description: {name}")
        if "allowed-tools" in fields:
            errors.append(f"Unexpected tool grant: {name}")
        contracts[name] = contract(text)
        if not contracts[name]:
            errors.append(f"Missing integrity contract: {name}")
        if len(text.split()) > 650:
            errors.append(f"Entrypoint exceeds 650 words: {name}")
        for file in folder.rglob("*"):
            if file.is_symlink():
                errors.append(f"Unexpected installed symlink: {file.relative_to(root)}")
            elif file.is_file() and file.relative_to(folder).as_posix() not in {"SKILL.md", "agents/openai.yaml", "LICENSE"}:
                errors.append(f"Unexpected installed file: {file.relative_to(root)}")
            elif file.is_file() and file.suffix == ".md":
                errors.extend(links(file, folder))
    base = contracts.get("scientific-writing")
    for name, value in contracts.items():
        if base and value != base:
            errors.append(f"Contract differs: {name}")
    return errors

def public_files(root):
    files = []
    for item in PUBLIC:
        path = root / item
        if path.is_file():
            files.append(path)
        elif path.is_dir():
            files.extend(p for p in path.rglob("*") if p.is_file() and "__pycache__" not in p.parts)
    return sorted(set(files))

def validate_repository(root):
    root = Path(root)
    errors = validate_skills(root)
    for item in PUBLIC:
        if not (root / item).exists():
            errors.append(f"Missing public deliverable: {item}")
    for path in public_files(root):
        if path.suffix in {".md", ".yaml", ".cff", ".svg"}:
            text = path.read_text(encoding="utf-8-sig")
            if "\ufeff" in text:
                errors.append(f"Embedded BOM: {path.relative_to(root)}")
            if re.search(r"[A-Za-z]:[\\/]Users[\\/]", text):
                errors.append(f"Personal absolute path: {path.relative_to(root)}")
        if path.suffix == ".md":
            errors.extend(links(path, root))
    return errors

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    errors = validate_repository(args.root)
    for error in errors:
        print("FAIL:", error)
    if not errors:
        print(f"PASS: {len(SKILLS)} standalone skill folders; public package structure and links checked.")
    return bool(errors)

if __name__ == "__main__":
    raise SystemExit(main())
