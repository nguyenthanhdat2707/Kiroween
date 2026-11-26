# Workflow plan — Mission: Digital Heritage & Resurrection Platform

Prepared 2026-11-26 by the Coordinator, before any launch. Mission (verbatim): [`../prompts/mission-instructions.md`](../prompts/mission-instructions.md).

## Relationship to earlier runs

- This mission arrived at the Phase 3 exit gate of `2026-11-25-phase3-7-knowledge-continuity`. The Coordinator treats it as **superseding** that run's draft Phases 4–7 (cross-review, solution exploration, comparative evaluation, validation planning) for the four spaces. Phase 3 outputs stay frozen and are reused as prior research.
- [inferred] Stage 3 applies the candidate rubric, so it partly replaces the old Phase 6. Comparison with the Phase 2 leaders (B-P1, A-P4) is **not requested** by this mission. The Coordinator will note overlaps descriptively, mainly A-P4 (web content preservation), and will not rank against them unless you ask.

## Why specialization instead of identical parallel research

- **Requested by you** (mission §3).
- [measured] In Task B and Phase 3, three identical-brief agents spent most of their effort on the same cases (Cohost, Mukurtu, PKP PN and JASPER appear in all three Phase 3 reports). The value came from labelling differences and cross-review, not from additional coverage.
- [inferred] Specialization should reduce duplicated case collection. The cost is that no domain gets independent triangulation within Stage 1: each domain has a single author, so its errors are caught only in Stage 2 by agents from other domains. Whether duplication actually drops will be measured: case and URL overlap across reports, compared with Phase 3.

## Model and effort decisions

| Agent | Model | Effort | How it is set | Verified |
|---|---|---|---|---|
| A | gemini-4-neon-medium | medium | Model suffix (agy rejects `--effort`) | Launched 2026-11-25; agy logged a "not recognized" warning, then applied "Gemini 4 Neon (Medium)" |
| B | claude-sonnet-5-5 | medium | `--effort medium` | Launched 2026-11-25; confirmed in /proc |
| C | gpt-6.1-sol | **high** | `--effort high` → `model_reasoning_effort=high` | Used at high in Phase 1; medium in Phase 3 |

- **Changing C's effort mid-session.** Effort is fixed per Codex process: a follow-up dispatch does not change it (Task B finding). Splitting C into a medium source-collection worker and a high architecture worker would need two processes and a file handoff, which adds coordination and a second context load. **Decision: C runs at high for all of Stage 1 and Stage 2.** This is recorded as the configuration actually used.
- No Astra model and no extra-high effort.

## Stage 1 — Specialized research

- Three fresh workers, each with the role contract in [`../brief-stage1.md`](../brief-stage1.md) §4.
- **Context selection:**
  - shared core: mission, AGENTS.md, rules snapshot, theme anchor, and the Phase 3 decision brief;
  - per role, only the prior research for that domain (brief §2);
  - earlier scores and rankings withheld.
- C may not run captures, crawlers, emulators or historical software. Measurement experiments are Stage 3 proposals that need your approval.
- Time box: A and B about 60 minutes, C about 75 minutes.

## Stage 2 — Cross-domain review (draft; finalized after Stage 1)

- Follow-up dispatch on the **same** sessions, which keeps context continuity. Stage 1 outputs are frozen by hash first.
- Each agent reads the other two reports and writes `cross-review/<x>-review.md`. The headings will cover:
  1. answers to questions addressed to me;
  2. conflicts across the five axes of mission §9 (UX vs technical limits, value vs economics, access vs legal and cultural limits, authenticity vs AI reconstruction, ambition vs hackathon feasibility), each with a **proposed resolution**;
  3. claims I challenge;
  4. what changed in my own Stage 1 judgment.
- Agents write only to their own review file.
- Escalation: only a separate targeted worker on one named dispute that needs more reasoning on shared evidence, with the reason recorded before launch.
- **A new security approval is needed** at the Stage 2 gate, as in earlier phases.

## Stage 3 — Product convergence (Coordinator)

- At most three product concepts in `coordinator/product-concepts.md`, each covering the 15 fields of mission §9 Stage 3.
- `coordinator/architecture-tradeoffs.md`: built from C's alternatives and the Stage 2 conflicts.
- Candidate rubric (Phase 2 anchors, theme gate ≥ 3):
  - Coordinator scoring with explicit evidence per score;
  - one-at-a-time weight-swing sensitivity, reusing Phase 2 `aggregate.py` where it applies.
- [inferred] Calibration limit: a single scorer is not independent. Independent multi-agent scoring was not requested and would add a stage. Offered as an option at the gate.
- A preferred concept is recommended only if the evidence separates the concepts. Otherwise the brief says so.
- `human/product-decision-brief.md`, written with better-writing.
- `progress/` update per AGENTS.md. This mission asks for it explicitly, which resolves G6 for this cycle.
- Stop at the human decision gate.

## Time budget [measured + inferred]

- Deadline: 05/12/2026 05:00 Vietnam time, about 8 days away.
- Expected:
  - Stage 1: 60–75 minutes;
  - Stage 2: 15–30 minutes;
  - Stage 3: about 1–2 hours of Coordinator time;
  - plus your two gates.
