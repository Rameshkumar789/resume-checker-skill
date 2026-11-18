# Resume Checker

One folder for Codex and Claude Code. One entry point coordinates career intake, writing, technical review, ATS review and verified document delivery.

## Quick start — open the folder

```bash
git clone https://github.com/Rameshkumar789/resume-checker-skill.git
cd resume-checker-skill
```

Open this folder as your project in Codex or start Claude Code here. Start a new session after cloning.

- **Codex:** send `$resume-checker Improve my resume using my career experience.`
- **Claude Code:** send `/resume-checker Improve my resume using my career experience.`
- **Plain-language fallback:** “Read SKILL.md and use this workflow to improve my resume.”

Project entry points are already included. No installation script, global configuration, paid plugin or API key is needed for this folder-based workflow. The agent uses the capabilities available in its environment; document export and external scoring remain optional.

Place candidate files in **private/** and save generated resumes in **outputs/**, or tell the agent another private destination. Both folders are ignored by Git.

## Optional — use it from any project

Run this once from the cloned folder to install the complete package as one skill folder for each tool:

```bash
python3 scripts/install.py --agent both
```

Or choose just one:

```bash
python3 scripts/install.py --agent codex
python3 scripts/install.py --agent claude
```

The installer copies this entire package to **~/.agents/skills/resume-checker/** for Codex and **~/.claude/skills/resume-checker/** for Claude Code. It excludes Git history, caches, environment files and private work. It does not modify existing configuration or overwrite an existing destination. Move an older resume-checker folder aside before reinstalling.

Start a new session after installation. Preview destinations without changing anything with `python3 scripts/install.py --agent both --dry-run`.

For manual installation, copy the entire package into the relevant **resume-checker/** skill folder. Keep the internal structure intact. You do not need to install the ten supporting modules individually.

## What is inside

```text
resume-checker-skill/
  SKILL.md                         Main portable entry point
  AGENTS.md                        Codex project guidance
  CLAUDE.md                        Imports shared project guidance
  .agents/skills/resume-checker/    Codex project entry
  .claude/skills/resume-checker/    Claude Code project entry
  skills/                          Ten included supporting modules
  scripts/                         Installer and local validators
  tests/                           Package and evidence checks
```

The supporting modules cover career intake, role positioning, evidence writing, screening review, document delivery, technical depth, accomplishment bullets, section structure and ATS analysis. The coordinator loads only the relevant instructions for a narrow edit and combines the stages for a complete rebuild.

Examples:
- “Build software-engineering and forward-deployed versions. Keep skills identical.”
- “Evaluate this resume against the job description without rewriting it.”
- “Improve the impact statements without inventing metrics.”

Private career data is not part of the reusable package. External checker uploads require user authorization. Scores are reported only when a checker actually returns them; no ATS pass is guaranteed.

## Validate

```bash
python3 scripts/validate_bundle.py
python3 -m unittest discover -s tests -v
```

To check an explicit career bank and bullet map:

```bash
python3 scripts/check_evidence.py /path/to/career-evidence.json /path/to/bullet-map.json
```

These local checks do not upload data and do not replace human review or rendered document inspection.

## Platform references

Packaging follows the documented project/user skill locations for [Codex](https://learn.chatgpt.com/docs/build-skills) and [Claude Code](https://code.claude.com/docs/en/skills). Shared project guidance uses a [CLAUDE.md import](https://code.claude.com/docs/en/memory). Actual discovery can depend on tool version and managed settings; the explicit “read SKILL.md” prompt remains the folder-based fallback.
