# Shared Brief — Stage 2: Cross-Domain Review

- Run root (below: `RM/`): `/home/tdat/Documents/Learn/Infrastructure/Hackathon/Kiroqeen/kiroween-research/runs/2026-11-26-mission-heritage-resurrection/`
- Mission: `RM/prompts/mission-instructions.md` §9 Stage 2 (binding). The evidence rules of `RM/brief-stage1.md` §3 still apply.
- This is a follow-up on **your same session**. Your Stage 1 report is frozen by hash: **do not edit it**. Record changes in this review.

## 1. What you are doing

Read the other two Stage 1 reports in full:

- `RM/agent-a/heritage-and-experience.md` + `summary.json`
- `RM/agent-b/business-and-sustainability.md` + `summary.json`
- `RM/agent-c/technical-architecture.md` + `summary.json`

Then review them from **your own domain**, looking for conflicts between:

1. user experience and technical limitations;
2. preservation value and operating economics;
3. accessibility and cultural or legal restrictions;
4. historical authenticity and AI reconstruction;
5. product ambition and hackathon feasibility (the submission deadline is 2026-12-04 14:00 PT, so about 8 days of build time remain).

**For every conflict you raise, propose a resolution.** Criticism without a proposed resolution does not count. Do not force consensus. When you disagree, say what evidence would settle it.

Do **not** design the final product and do **not** score candidates. Section 7 asks for coherent **combinations** of existing deliverables as input for the Coordinator; that is the limit.

## 2. Deliverables (write **only** these two files)

### `RM/cross-review/<x>-review.md` (Vietnamese)

```
# Stage 2 — Agent <X> cross-domain review
## Metadata                              (start/end UTC; sources opened directly vs snippet-only; failures)
## 1. Answers to questions addressed to me  (every question the other two reports addressed to you, by their ID; answer with evidence and labels, or "cannot answer" + why)
## 2. Conflicts and proposed resolutions    (table: axis 1–5 | conflict | evidence on each side (claim IDs) | proposed resolution | residual risk)
## 3. Claims I challenge                    (claim ID | original label | my assessment | reason | evidence that would settle it)
## 4. Overlooked alternatives and counterevidence
## 5. Changes to my own Stage 1 judgment    (what changed, which claim or deliverable, and who triggered it; "none" is allowed but must be justified)
## 6. Positions I keep despite challenge
## 7. Coherent combinations for convergence (at most 3; each = one A-E + one or more B-M + one C-X, with why they fit, the conflicts that remain blocking, and the Resurrection anchor if any; no scoring)
## 8. New references                        (same table format as Stage 1; new ones only)
```

### `RM/cross-review/<x>-review.json`

```json
{
  "agent": "A",
  "stage": 2,
  "questions_answered": 0,
  "questions_unanswerable": 0,
  "conflicts_raised": 0,
  "claims_challenged": ["B-C12"],
  "own_claims_relabelled": [{"claim": "A-C3", "from": "VERIFIED", "to": "INFERENCE", "reason": "one sentence"}],
  "own_deliverables_changed": [{"id": "A-E1", "change": "kept|revised|withdrawn", "reason": "one sentence", "triggered_by": "B|C|self"}],
  "combinations": [
    {"experience": "A-E2", "operating_models": ["B-M5"], "architecture": "C-X2", "fit": "one sentence", "blocking_conflicts": ["one sentence"], "resurrection_anchor": "string or null"}
  ]
}
```

## 3. Conduct

- Read the other agents' Stage 1 files. Do **not** read the other agents' `cross-review/` files. Do not message other agents.
- Write only the two files above. Your process is unsandboxed; these limits are enforced only by you.
- Same rules as Stage 1: no installs. Agent C: no captures, crawlers, emulators or historical software.
- Targeted new searches are allowed to settle a specific conflict. Do not restart broad discovery.
- Time box: about 30 minutes. Never wait for user input.
- **When finished:** report the paths, the number of questions answered, the conflicts raised, own labels changed, deliverables kept/revised/withdrawn, and failures.
