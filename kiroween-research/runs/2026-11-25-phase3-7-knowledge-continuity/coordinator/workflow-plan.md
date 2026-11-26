# Workflow plan — Phases 3–7 (Digital Knowledge Continuity)

Prepared 2026-11-25 by the Coordinator, before any launch. Phase 3 is final. Phases 4–7 are **drafts**: each is re-checked against the previous phase's results and saved as `prompts/phase-<n>-instructions.md` before it runs. There is a human stop at the end of every phase.

Mission: [`../prompts/cycle-instructions.md`](../prompts/cycle-instructions.md) (verbatim).

## Time budget [measured + inferred]

- Submission deadline: 04/12/2026 14:00 PT, which is 05/12/2026 05:00 in Vietnam. About **9 days** remain as of 25/11.
- Measured worker cost in Task B: 8–14 minutes per research round, 13–20 minutes per agent for two rounds.
- [inferred] Each phase needs about 30–90 minutes of machine time plus your review. With five gates, the research cycle realistically takes **2–4 days**, which leaves about 5–7 days to build. This tension is reported, not resolved: it is your call.

## Reused mechanisms (no new skills, frameworks or components)

| Need | Reused | Source |
|---|---|---|
| Worker launch | `orchestration run-create` → `worker-start --spec-file --worktree current --agent --model [--effort] --keep-open --json` | Task B execution log §1 |
| Agent A effort | model suffix `gemini-4-neon-medium` (agy rejects `--effort`) | memory: Orca launch facts |
| Follow-up round on the same session | `orchestration send --to dispatch:<id> --type dispatch --body-file` | Task B §5 |
| Output contract | Task B `brief.md` §4 schema, extended with space, verdict, payer, maintainer, cases, preservation-vs-restoration, resurrection anchor | `brief-phase3.md` §4 |
| Evidence rules | 7-criterion reference rubric; snippet ≠ VERIFIED; single official document ⇒ VERIFIED only for "X officially stated Y" | Phase 1–Task B |
| Candidate rubric | Phase 2 `rubric-and-anchors.md`, unchanged | Phase 2 |
| Aggregation and sensitivity | Phase 2 `coordinator/analysis/aggregate.py` (Dirichlet α = 40, N = 20000, seeded) + one-at-a-time weight swings | Phase 2 |
| Token measurement | Claude `~/.claude/projects` usage (dedupe by id); Codex `rollout-*.jsonl` token_count; agy not measurable | Task B §0 |
| Integrity | pre-launch sha256 snapshot written in scratch, then copied; post-run audit | Task B |
| Human brief | `better-writing` skill | Phase 1–Task B |

## Phase 3 — Focused Deep Research (final)

- Three **fresh** worker sessions: A `gemini-4-neon-medium`, B `claude-sonnet-5-5 --effort medium`, C `gpt-6.1-sol` at reasoning effort medium.
- All three agents investigate **all four** spaces. No roles. Reason: the mission asks for all four, and triangulation across three models is what makes cross-review useful. Cost is about three times that of splitting the spaces.
- Context selection: see the execution log §0.
- Outputs: `agent-<x>/report.md`, `agent-<x>/opportunities.json`.
- Coordinator after the run:
  - integrity audit and metrics;
  - a short coverage check against the contract;
  - human brief `human/phase-3-decision-brief.md`.
  - **No** synthesis ranking.
- Exit gate: verdict per space per agent, convergence and divergence, theme-gate result for T3/T4, open questions, and approval to start Phase 4.

## Phase 4 — Cross-review (draft)

- Follow-up dispatch on the **same** Phase 3 sessions, effort medium. Phase 3 outputs are frozen by hash first.
- Each agent reads the other two reports and writes `cross-review.md` and `opportunities-revised.json`, with the Task B Round 2 format extended by the user's §4 items:
  1. shared underlying problem: yes / no / partial, with evidence;
  2. proposals to combine: challenge each one;
  3. where preservation is unnecessary or unsustainable;
  4. technical feasibility vs actual user demand, kept as separate columns.
- No forced consensus. The Coordinator records changes of judgment and disagreements in a table.
- Escalation candidate: a disagreement over the interpretation of **one** legal or theme text that all agents have opened. More reasoning can resolve that kind of dispute; it does not need new evidence.

## Phase 5 — Solution exploration (draft)

- Only for spaces or sub-opportunities that survive Phase 4 (a `continue` or `narrow` verdict from at least one agent, not refuted in cross-review), subject to your approval at the Phase 4 gate.
- Proposed: a follow-up on the same sessions. Each agent writes 2–4 approaches per surviving opportunity, each with:
  - a conventional baseline and an AI-enabled variant;
  - one narrowly scoped initial target user;
  - a measurable value proposition;
  - the smallest useful MVP and its limits.
- A separate section asks whether a **shared capability** (not a platform) serves more than one use case, with the mission's guard against a universal preservation platform.
- Open choice for that gate: the same sessions (context continuity) or fresh sessions (less attachment to their own Phase 3 findings).

## Phase 6 — Comparative evaluation (draft)

- **Fresh** evaluator sessions, distinct from the Phase 3–5 sessions. Reason: researchers scoring their own opportunities have a self-preference bias.
- Candidates: up to 3–5 surviving new opportunities, plus B-P1 and A-P4 from Phase 2 as they stood after that phase's revision.
- Blinded labels: candidates are renamed (for example K1–K7). Evaluators receive evidence dossiers, not the source agent's scores.
- Flow:
  - **6a.** Independent scoring with the shared anchors.
  - **6b.** Adversarial review: each evaluator challenges the other two.
  - **6c.** Coordinator aggregation with `aggregate.py` (Dirichlet weight resampling) plus one-at-a-time weight swings and an evaluator-leave-one-out.
- The theme gate (≥ 3) applies.
- Output: a shortlist of up to three, or an explicit statement that the evidence cannot separate them.
- Known calibration limit: model labelling bias (A generous, C strict). Mitigated by shared anchors, blinding and leave-one-out. Not removed.

## Phase 7 — Feasibility and validation planning (draft)

- Coordinator-led. For each finalist: assumptions, falsifying experiments, datasets and permissions, technical risks, scope within the remaining days, and success and failure criteria.
- Optionally one fresh worker red-teams the plan with the `idea-red-team` skill.
- No experiments or implementation without approval.

## Per-phase deliverables (mission §11)

Each phase ends with:

- the research artifacts;
- claim references;
- an execution-log section with tokens, time, escalation and the audit;
- `human/phase-<n>-decision-brief.md` written with `better-writing`;
- open questions;
- the exit criteria and the approvals needed.

`progress/` is updated only when you approve (decision G6 is still open).
