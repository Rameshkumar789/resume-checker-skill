# Resume Checker workspace

This repository is a self-contained resume workflow for Codex and Claude Code.

When the user asks to build, improve, tailor or evaluate a resume, read the root [SKILL.md](SKILL.md) and follow its routing. The ten modules inside skills/ are included supporting instructions, not separate installation requirements. Read only the modules needed for the task.

Keep candidate inputs and career evidence in private/ and deliverables in outputs/ unless the user supplies another workspace. These ignored directories keep personal data out of the published skill package. Never publish candidate data as part of a resume-writing task.

For maintenance of this package, honor the user's requested change, run python3 scripts/validate_bundle.py and python3 -m unittest discover -s tests -v, and keep both project entry points pointing to the same root SKILL.md.
