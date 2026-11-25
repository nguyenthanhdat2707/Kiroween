# Coordinator Execution Log — Phase 2

## Pre-launch

- Quota (Orca account list): Claude weekly 5%; Codex weekly 66% (resets Saturday); Antigravity Gemini weekly 8%.
- Execution mode (user-approved): **unsandboxed workers, prompt-only isolation**. Orca `agentPermissionDefault = full-access`; Antigravity `own` (`always-proceed`).
- Integrity snapshot: `pre-launch-checksums.sha256` covers every file in the workspace except `.obsidian/` and this run's `agent-*` folders.
- Overlaps O1/O2 scored separately (E2 unanswered). Task B defined but not started.

## Phase 2A launch
- Orca run `run_39e4e5d570e9`. Launched 2026-11-25T11:07:15Z; all three worker-start exit 0, `--worktree current`, `--keep-open`.

| Agent | --model | --effort | Dispatch | Terminal |
|---|---|---|---|---|
| A (antigravity via agy-api.sh) | gemini-4-neon-high | (suffix) | ctx_84f96e13d5d8 | term_0df28859-a9b3-4772-9910-13eb548b98f7 |
| B (claude via claude-pro.sh) | claude-sonnet-5-5 | high | ctx_ddd748c3c4bd | term_d6843d6c-7011-4dba-9142-e6b6e10b526e |
| C (codex) | gpt-6.1-sol | high | ctx_fda9b7e9339b | term_99426492-4f5f-466a-8f4c-7693a2d7b48e |

## Failures / anomalies
- 2A completed: B ~11:33Z order B → A → C; all scores.json valid (schema, totals, gate flags); model/effort observed match launch args.
- Post-2A audit: no pre-launch file changed except the snapshot file itself (hashed while being written — snapshot method artefact); no new files outside agent dirs except this log; no cross-reads of other agents' Phase 2 folders in transcripts.
- B reports 38 of 50 new references as snippet-only. Raised in 2B rule: snippet-only evidence cannot justify a score above 3.
- 2A outputs frozen by hash: `2a-outputs.sha256`.

## Phase 2B launch (follow-up tasks on the same workers)

| Agent | Dispatch | Task |
|---|---|---|
| A | ctx_178b3565516d | task_031e5e5c5a03 |
| B | ctx_7294bf15d116 | task_8f13efc1be3f |
| C | ctx_b262d04447c6 | task_c4d249ac0d7f |
- 2B completed (B → A → C). All scores-revised.json valid; all debate.md headings present; 2A outputs unchanged (hash check).
- Post-2B audit: no pre-launch file changed; no files written outside agent dirs except this log; no cross-writes detected in transcripts.
- 13 score changes in total (A 5, B 6, C 2). After 2B, C-P4 fails the theme gate for all three agents.

## Phase 2C (Coordinator)
- Aggregation and sensitivity: `analysis/aggregate.py` (seeded) → `analysis/aggregate-results.json`, `analysis/criteria-table.md`.
- Result: A-P4 and B-P1 are robust Top 2 (89–100% across perturbations). Third place is a statistical tie (A-P1 66.0, A-P2 66.0, C-P1 65.7); the script's ordering of A-P1 is a tie-break artefact, not reported as a recommendation.
- Human report: `../human/phase-2-report.md`. Stopped at the approval gate 2026-11-25T11:44:23Z.
