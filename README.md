# Resume Checker Skill

A portable collection of ten Codex skills for evidence-based technical resumes. Invoke **$resume-builder** to coordinate career intake, role positioning, writing, review and verified document delivery.

Supports senior/staff software engineering, applied AI and forward deployed engineering. Choose separate or combined versions based on the user's target. The collection contains no candidate resumes, career records or customer data.

## Skills

| Skill | Purpose |
|---|---|
| resume-builder | Coordinates the workflow and supporting skills |
| resume-career-intake | Reconstructs contributions, decisions and trustworthy outcomes |
| resume-role-positioning | Selects evidence and calibrates scope/seniority |
| resume-evidence-writing | Writes drafts tied to source evidence |
| resume-screening-review | Reviews facts, parsing, role fit and technical credibility |
| resume-document-delivery | Produces and visually verifies PDF, Word and text files |
| tech-resume-optimizer | Examines technical ownership, depth and production scope |
| resume-bullet-writer | Improves action, mechanism and outcome statements |
| resume-section-builder | Organizes chronology, summaries, skills and projects |
| resume-ats-optimizer | Checks extraction, job alignment and real checker findings |

## Install

Copy the ten directories inside **skills/** into your Codex skills directory, normally **~/.codex/skills/**, or install the individual GitHub paths with the skill installer. Keep the sibling names unchanged so the main skill can resolve its links. If a same-named skill already exists, compare/back it up before replacement.

The core skill package is Markdown plus UI metadata. No paid plugin, network request, browser extension or Python dependency is required to read and apply it. PDF/Word generation uses whatever compatible tools are available in the user's environment.

## Use

“Use $resume-builder to improve my software-engineering and forward-deployed resumes. Keep the skills identical and ask only for missing evidence.”

“Use $resume-screening-review to review this draft against the supplied job description without rewriting it.”

“Use $resume-bullet-writer to improve these accomplishments without inventing metrics.”

Save private career-evidence.json, open questions and document exports in a separate user workspace, outside this repository.

## Optional plugins

Connected resume checkers can provide their actual score when the user authorizes sharing a resume. A second plugin that supplies only an editor link is not a second independent evaluation. Repository connectors, live job research and PDF/Word tools are optional capabilities with local fallbacks described in the bundle.

A tool score is a heuristic, not a hiring probability or guaranteed ATS pass. Preserve truthful titles, ownership, metric units, customer boundaries and production status.

## Validate

Run **python3 scripts/validate_bundle.py** for package structure, relative links, metadata and publication checks.

Run **python3 -m unittest discover -s tests -v** for evidence-validator behavior.

Run **python3 scripts/check_evidence.py /path/to/career-evidence.json /path/to/bullet-map.json** to check evidence references and unresolved sources before document delivery. The script reads only explicit paths, prints no candidate facts and makes no network requests.

These checks do not replace behavioral review or visual inspection of generated resumes.
