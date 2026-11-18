---
name: resume-career-intake
description: "Interview a candidate to reconstruct career accomplishments, technical decisions, and trustworthy resume evidence before writing or rewriting resumes."
---

# Career intake

Start with the user's most meaningful or omitted project. Ask a small related batch, then follow the answer. Do not make them fill every field before making progress. Review supplied resumes as starting claims, not an exhaustive career history. Capture all periods, including earlier work, contract-to-full-time transitions, promotions, independent work, and relevant projects.

For each project, discover:
- Business/user problem, why it mattered, dates, team context, constraints, and what existed before.
- The user's implementation, design decisions and alternatives, hard technical failure modes, operational responsibilities, and collaboration boundaries.
- What shipped versus prototype/pilot, who actually used it, before/after outcomes, and continuing ownership.
- Leadership scope: technical direction, mentoring, delivery coordination, or formal people management. Separate these.
- Metrics with units, denominator, time window, measured/estimated/target status, calculation or source, personal attribution, and whether safe to disclose. Ask for concrete qualitative outcomes when no defensible number exists.
- Stack attached to real work, recency, and depth of hands-on use; distinguish employer work from personal experiments.

For applied AI, ask about tool execution, data retrieval, evaluation design and results, failure handling, latency/cost, and production operation. Never assume training or fine-tuning from an LLM integration.
For forward deployment, ask who the customer was, discovery, success criteria, integration constraints, implementation, rollout, iteration, and support. Separate internal business partners from external paying customers.
For staff targeting, ask who adopted the technical direction, what changed across teams, how disagreement was resolved, and what remained effective beyond one delivery.

Persist career-evidence.json with stable evidence IDs. Suggested record shape:

```json
{"id":"E001","company":"","employment_type":"","official_title":"","functional_scope":"","dates":{"start":null,"end":null},"project":"","problem":"","personal_actions":[],"technical_decisions":[],"team_context":"","technologies":[],"outcomes":[],"metrics":[{"value":null,"unit":"","population":"","window":"","kind":"measured|estimated|target|unknown","basis":"","attribution":""}],"delivery_status":"unknown","source":"user interview or file/page reference","verification":"resume_only|user_confirmed|conflicting","disclosure":"unknown|approved|generalize","open_questions":[]}
```

This is a record schema, not an instruction to fill unknowns. Keep nulls and open questions. Store contact information and education separately from project records. Add new facts without overwriting conflicting prior evidence silently. Record the user's correction and which claim it supersedes. No secrets, proprietary code, customer datasets, or confidential screenshots are needed for a resume interview.

Persist unresolved factual questions in open-questions.txt alongside career-evidence.json. Return the organized evidence, omissions discovered, and the next highest-value questions. Before drafting final files, confirm dates, titles, material metrics and any sensitive naming. Do not require user confirmation for every stylistic edit.
