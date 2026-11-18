---
name: resume-screening-review
description: "Review resume drafts for parsing, truthful job alignment, recruiter readability, and technical credibility without promising an ATS or hiring outcome."
---

# Screening review

Run distinct passes and return findings with concrete repairs. Read [references/current-screening.md](references/current-screening.md) when explaining ATS or AI screening behavior. Recheck vendor-specific claims when needed; screening features and employer configurations vary.

1. **Facts and consistency:** Trace important claims to evidence IDs. Compare dates, titles, metrics, seniority, management scope, customers, and delivery status across variants. Remove unsupported additions. Estimated metrics must remain labeled with a defensible basis. Flag internal customer work presented as external deployments.
2. **Parsing:** Review actual exported text for name, contact, sections, employers, roles, dates, degrees, key technologies, bullets, and reading order. Prefer single-column body text and ordinary headings. Avoid critical information in text boxes, headers/footers, graphics or skill charts. A visual or plain-text check cannot prove every ATS will parse it.
3. **Job fit / AI-assisted review:** Compare the actual requirements to demonstrated experience in the matrix. Include truthful terminology and expand useful acronyms. Report supported matches and remaining gaps, not a fabricated ATS score, universal threshold, or simulated employer probability. Never add hidden text, instructions to a screening model, irrelevant keyword repetition, or unsupported skills.
4. **Recruiter scan:** After a short independent scan, identify the target role, employment trajectory, strongest relevant technologies, location when supplied, and two compelling achievements. If these are difficult to find, revise ordering and wording. An agent's simulation is a heuristic, not evidence of actual recruiter behavior.
5. **Engineering depth:** Ask what the candidate personally built, what decision was difficult, why it mattered, and whether scale, reliability, and outcomes are attributable. For staff, examine sustained cross-team technical influence. For AI, distinguish evaluated production systems from demos. For FDE, examine discovery through deployment and adoption.
6. **Language and artifacts:** Check natural English, tense, spelling, punctuation, density, page flow, hyperlinks, and final file extraction. Follow employer file requirements.

When authorized and available, an independent reviewer can do passes 4-5 with the source bank and draft. Require findings grounded in evidence; a reviewer cannot invent missing facts. Otherwise keep the passes distinct yourself. Fix supported issues, rerun only affected checks, and stop when remaining uncertainty requires the user's factual input.

Return checks actually performed, material changes, remaining gaps, and draft/final readiness. State limits once, plainly: parsing, ranking, screening questions and human review differ by employer, and passing cannot be guaranteed. Do not claim access to an employer's configured screening criteria beyond what they disclose.
