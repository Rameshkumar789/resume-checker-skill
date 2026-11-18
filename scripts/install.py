"""Install the entire package as one skill folder; never install modules separately."""
import argparse
from pathlib import Path
import shutil
import tempfile


def install(source, destination):
    source, destination = Path(source).resolve(), Path(destination).expanduser().absolute()
    if not (source / "SKILL.md").is_file():
        raise ValueError("Source must contain the package SKILL.md.")
    if destination.exists() or destination.is_symlink():
        raise FileExistsError("Destination already exists; move it aside before installing.")
    if destination == source or source in destination.parents:
        raise ValueError("Install outside the source package.")
    destination.parent.mkdir(parents=True, exist_ok=True)
    stage = Path(tempfile.mkdtemp(prefix=".resume-checker-", dir=destination.parent))
    try:
        shutil.copytree(
            source, stage / "package",
            ignore=shutil.ignore_patterns(".git", "__pycache__", "*.pyc", ".DS_Store", ".env", ".env.*", ".venv", "private", "outputs", "work"),
        )
        # Atomic rename on the destination filesystem. Never overwrite an existing folder.
        (stage / "package").rename(destination)
    finally:
        shutil.rmtree(stage)
    return destination


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--agent", choices=["codex", "claude", "both"], default="both")
    parser.add_argument("--destination", type=Path, help="Explicit skill folder instead of the normal user locations.")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    source = Path(__file__).resolve().parents[1]
    if args.destination:
        destinations = [args.destination]
    else:
        destinations = []
        if args.agent in {"codex", "both"}:
            destinations.append(Path.home() / ".agents/skills/resume-checker")
        if args.agent in {"claude", "both"}:
            destinations.append(Path.home() / ".claude/skills/resume-checker")
    # Check every target before changing any.
    if not args.dry_run:
        for path in destinations:
            if path.exists() or path.is_symlink():
                parser.error("A destination already exists. Move the existing resume-checker folder aside first.")
    for path in destinations:
        if args.dry_run:
            print(f"Would install one complete skill folder: {path}")
        else:
            print(f"Installed: {install(source, path)}")
    if not args.dry_run:
        print("Start a new Codex or Claude Code session to discover the installed skill.")


if __name__ == "__main__":
    main()
