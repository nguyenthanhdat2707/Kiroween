# Engineering Execution Log — Task B

Measured facts are labelled **[measured]**; interpretations are labelled **[inferred]**.

## 0. Pre-launch

- **Security check [measured].**
  - Orca `agentPermissionDefault = full-access`, `agentPermissionOverrides = {antigravity: own}` (Antigravity `always-proceed`). No per-launch sandbox flag exists.
  - A bubblewrap 0.13.1 boundary was tested in scratch:
    - write to the own folder: allowed;
    - write to a project file and to `$HOME`: blocked (read-only filesystem);
    - peer folder: hidden behind tmpfs;
    - HTTPS: 200;
    - `orca status` through the socket: ok.
  - Not tested: agent CLIs running inside bwrap.
- **Decision (user):** "Accept risk again, scoped". Workers run unsandboxed with prompt-only isolation, followed by a post-run audit. The enforceable boundary was shown to be feasible and was not used **[measured]**.
- **Integrity snapshot:** `pre-launch-checksums.sha256`, 134 files, written to scratch first and then copied, which fixes the Phase 2 self-hash artefact.
- **Token measurability [measured]:**
  - Claude: per-message `usage` in `~/.claude/projects/*/*.jsonl`.
  - Codex: `token_count` events in `~/.codex/sessions/**/rollout-*.jsonl`.
  - Antigravity: conversation SQLite (`gen_metadata`, protobuf blobs). Token fields **not verified**.
- **Context selection.** Agents receive the mission, AGENTS.md, the candidate-rubric anchors, the official rules snapshot, and a **list** of already-explored topics. Phase 1/2 scores and rankings are withheld on purpose (mission §1: do not let earlier rankings constrain discovery). No dimension or role specialization is assigned, so any specialization that appears is emergent.

## 1. Round 1 launch

- Orca run `run_4e59f8b2768e`. Fresh workers (new dispatches, new processes). `--worktree current`, `--keep-open`.

| Agent | PID | Runtime args (from /proc) [measured] | Dispatch | Terminal |
|---|---|---|---|---|
| A | 89523 | `agy --settings ~/.config/orca/agy-api.json --model gemini-4-neon-medium` | ctx_6461ab7677eb | term_928bf257-35dc-429d-9e3d-c19e8c4e38a9 |
| B | 89499 | `claude --dangerously-skip-permissions --model claude-sonnet-5-5 --effort medium` | ctx_d9ea0006691e | term_d8065e3f-0266-4a4e-a167-28b796a4c0ce |
| C | 89524 | `codex --dangerously-bypass-approvals-and-sandbox -m gpt-6.1-sol -c model_reasoning_effort=medium` | ctx_6035c9d39daa | term_d79ad544-36a1-4d6b-a4a2-04b5a1b4e7a2 |

- All three processes started at 2026-11-25 19:28:04 (UTC+7) = 12:28:04Z.
- Effort: medium for all. No Astra model, no xhigh.
- Note: idle kept-open Phase 2 workers are still alive (agy pid 25701, codex pid 25736 at effort high). They are not part of Task B.

## 2. Failures / anomalies
- None at launch. Round 1 finished in the order B → C → A.
- Self-reported metadata gaps: B's effort field was null; C's model and effort were null. Actual values are taken from /proc (table above).

## 3. Round 1 results [measured]

| Agent | Wall time | Model calls | Input tokens (of which cached) | Output tokens | Opportunity spaces | Claims (V/I/H/U) | Refs: opened directly / snippet-only |
|---|---|---|---|---|---|---|---|
| A (agy) | 14 min 10 s (12:28:05Z–12:42:15Z, agy log) | 17 generations, 92 steps | **not measurable**: no token fields in agy logs or conversation DB | not measurable | 5 | 27/3/0/0 | 26 / 8 |
| B (claude) | 8 min 16 s (12:28:06Z–12:36:22Z) | 31 API messages (deduplicated by id) | 3,523,133 (3,376,303 cache read; 146,766 cache write) | 49,126 | 5 | 20/18/2/1 (self-reported: 15 VERIFIED are "source says" only) | 24 / 7 |
| C (codex) | 11 min 22 s (12:28:09Z–12:39:31Z) | — | 3,630,427 (3,456,000 cached) | 28,769 (4,052 reasoning) | 3 | 6/25/7/4 | 30 / 4 |

- **Integrity audit:**
  - no pre-launch file changed;
  - no new files outside the agent folders except this log;
  - no mention of forbidden paths in any transcript.
- **[inferred] Label discipline differs sharply between models.** A labels 90% of its claims VERIFIED with 8 snippet-only references. B self-flags 15 of its 20 VERIFIED labels as single-source. C labels 14% VERIFIED. This matches the Phase 1.5 calibration direction (A generous).
- **[measured] Independent convergence** (no cross-reads):
  - live-service game end-of-life: A-O4, B-O1, C-O2;
  - small or scholarly journals: B-O3, C-O1 (A-O1 adjacent);
  - platform shutdown window: A-O2, B-O2;
  - heritage consent and sovereignty: A-O5, C-O3 (B-O4 adjacent);
  - abandoned software reconstruction and environments: A-O3, B-O5.

## 4. Round 2 plan

- Follow-up tasks on the **same** worker sessions, at effort **medium**. Context continuity is intended for cross-review.
- **Escalation rule:** effort is fixed per process, so escalating to High means launching a **separate, targeted** worker on one named unresolved problem. The reason and cost are recorded before launch. No escalation is planned before Round 2 results are in.

## 5. Round 2 launch

- Sent 2026-11-25T12:43:21Z as follow-up dispatches on the same sessions, effort medium. Round 1 outputs are frozen by hash (`r1-outputs.sha256`).

| Agent | Dispatch | Task |
|---|---|---|
| A | ctx_3dd2a246eb1d | task_c6dbfb956b3c |
| B | ctx_9b870590bc37 | task_b64f52da3e5b |
| C | ctx_cddb9f292cd7 | task_289e270ecdac |

## 6. Round 2 results [measured]

| Agent | Wall time | Input tokens (cached) | Output tokens | Challenges made | Own VERIFIED labels changed | Opportunities kept / revised / withdrawn |
|---|---|---|---|---|---|---|
| A (agy) | ~5 min 08 s (12:43:21Z sent → last log 12:48:29Z) | not measurable | not measurable | 11 (B 6, C 5) | **24 of 27** downgraded (23 → INFERENCE, 1 → HYPOTHESIS) | 0 / 4 / 1 (A-O5) |
| B (claude) | 4 min 51 s | 4,533,703 (4,420,280 cache read) | 36,947 | 21 (A 13, C 8) | 12 VERIFIED → INFERENCE (+1 UNKNOWN → INFERENCE) | 0 / 4 / 1 (B-O3) |
| C (codex) | 8 min 23 s | 6,069,839 (5,952,000 cached) | 20,938 (4,279 reasoning) | 19 (A 10, B 9) | 1 (C-G-C12) | 0 / 3 / 0 |

- **Integrity audit:**
  - no pre-launch file changed;
  - Round 1 outputs intact (hash);
  - no new files outside the agent folders except this log;
  - all cross-review headings present; all revised JSON valid.
- **Effort escalation: none.**
  - Reason: every remaining disagreement requires **new empirical evidence**: benchmark re-runs, real export packages, studio and maintainer interviews, sampling of closed games, jurisdiction-specific legal instruments.
  - None requires more reasoning over evidence already gathered, so higher effort would add cost without resolving anything. These were converted into validation experiments (`synthesis/hypotheses-validation-plan.md`).
- **Coordinator ruling on the VERIFIED threshold (B asked):** a single official document opened directly supports **VERIFIED** only for a claim scoped to "organisation X officially stated/announced Y". The underlying truth or effect of Y still needs independent confirmation. This is the same rule as the Phase 1.5 overlay (B-P4-C2).
- **Official rules re-checked** against the live page 2026-11-25: unchanged ("Updated November 16, 2026"; same submission period and Resurrection definition).

## 7. Totals [measured where stated]

| | Round 1 | Round 2 | Total |
|---|---|---|---|
| B input / output | 3,523,133 / 49,126 | 4,533,703 / 36,947 | 8,056,836 / 86,073 |
| C input / output | 3,630,427 / 28,769 | 6,069,839 / 20,938 | 9,700,266 / 49,707 |
| A | 14 min 10 s; tokens not measurable | ~5 min; tokens not measurable | ~19 min |
| Coordinator (this Claude session, 12:24Z–12:54Z) | | | 20,917,878 input (20,832,959 cache read) / 62,259 output |

- Wall-clock for Round 1 + Round 2: ~24 min (12:28Z → 12:52Z).
- Synthesis is Coordinator only.

## 8. Round 3 (Coordinator synthesis) and exit

- Outputs:
  - `synthesis/problem-analysis.md`, `stakeholder-analysis.md`, `alternatives-gap-analysis.md`, `opportunity-map.md`, `hypotheses-validation-plan.md`, `ai-engineering-lessons.md`;
  - `synthesis/data/rubric-evidence-table.md` and its generator script;
  - `human/taskb-decision-brief.md` (1,570 words, about 7 minutes).
- **Final checks [measured]:**
  - every relative link and claim ID in the synthesis and brief resolves;
  - no pre-launch file changed; Round 1 outputs intact;
  - no files changed outside this run folder since Round 1 was frozen.
- Workers remain open (kept-open) and idle. Nothing was committed or pushed. Stopped at the Exit Gate 2026-11-25T12:56:09Z.
