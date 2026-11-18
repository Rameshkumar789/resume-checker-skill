"""Check the portable package without third-party Python dependencies."""
import json
from pathlib import Path
import re


def validate(root):
    errors = []
    skills = root / "skills"
    entries = sorted(skills.glob("*/SKILL.md"))
    if not entries:
        return ["No skills found."]
    for path in entries:
        content = path.read_text()
        split = content.split("---", 2)
        if len(split) != 3 or split[0].strip():
            errors.append(f"{path.relative_to(root)}: invalid frontmatter")
            continue
        fields = {}
        for line in split[1].strip().splitlines():
            key, sep, value = line.partition(":")
            if sep:
                fields[key] = value.strip()
        if fields.get("name") != path.parent.name:
            errors.append(f"{path.relative_to(root)}: name mismatch")
        if not fields.get("description"):
            errors.append(f"{path.relative_to(root)}: missing description")
        if not re.fullmatch(r"[a-z0-9-]{1,63}", path.parent.name):
            errors.append(f"{path.relative_to(root)}: invalid skill name")
        metadata = path.parent / "agents/openai.yaml"
        if not metadata.exists():
            errors.append(f"{path.relative_to(root)}: missing UI metadata")
        else:
            values = {}
            for line in metadata.read_text().splitlines():
                key, sep, value = line.strip().partition(":")
                if sep and value.strip():
                    try:
                        values[key] = json.loads(value.strip())
                    except ValueError:
                        errors.append(f"{metadata.relative_to(root)}: expected quoted metadata")
            if "$" + path.parent.name not in values.get("default_prompt", ""):
                errors.append(f"{metadata.relative_to(root)}: invocation missing")
            if not 25 <= len(values.get("short_description", "")) <= 64:
                errors.append(f"{metadata.relative_to(root)}: UI description length")
    for path in root.rglob("*"):
        if not path.is_file() or ".git" in path.parts or "__pycache__" in path.parts:
            continue
        if path.suffix in {".pdf", ".docx", ".xlsx", ".pptx"} or path.name in {"career-evidence.json", "open-questions.txt"}:
            errors.append(f"{path.relative_to(root)}: private/artifact file in package")
            continue
        try:
            text = path.read_text()
        except UnicodeDecodeError:
            errors.append(f"{path.relative_to(root)}: unexpected binary file")
            continue
        private_pattern = "/" + "Users" + r"/|/home/[^ /]+/|[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}"
        if re.search(private_pattern, text, re.I):
            errors.append(f"{path.relative_to(root)}: candidate data or absolute user path")
        if ("byte" + "bytego") in text.lower():
            errors.append(f"{path.relative_to(root)}: removed external source still present")
        if path.suffix == ".md":
            for target in re.findall(r"\]\(([^)]+)\)", text):
                if target.startswith(("https://", "http://", "#", "mailto:")):
                    continue
                destination = (path.parent / target.split("#", 1)[0]).resolve()
                if not destination.is_relative_to(root.resolve()) or not destination.exists():
                    errors.append(f"{path.relative_to(root)}: broken/outside reference {target}")
    return errors


if __name__ == "__main__":
    root = Path(__file__).resolve().parents[1]
    errors = validate(root)
    for error in errors:
        print(error)
    if not errors:
        print(f"Validated {len(list((root / 'skills').glob('*/SKILL.md')))} skills, metadata, relative links and publication boundaries.")
    raise SystemExit(bool(errors))
