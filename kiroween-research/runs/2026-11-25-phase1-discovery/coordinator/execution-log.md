# Coordinator Execution Log — Phase 1

| Time (UTC+7) | Event |
|---|---|
| 2026-11-25 | Official rules fetched via curl (HTTP 200; web-fetch tool got 403). Matches `competition/rules.md`; snapshot saved in `sources/`. |
| 2026-11-25 | brief.md, prompts/phase-1-instructions.md, prompts/agent-{a,b,c}-spec.md written. |

## Launch parameters

Effort mapping verified in Preflight: agy rejects `--effort` on Gemini 4 models, so effort is encoded in the model id for Agent A.

| Agent | Orca agent | Command override | --model | --effort | Dispatch | Terminal |
|---|---|---|---|---|---|---|
| A | antigravity | `~/.config/orca/agy-api.sh` | gemini-4-neon-high | (none; suffix) | ctx_72ffe508bed3 | term_506f13ae-f28f-490e-9935-effa8d25ca77 |
| B | claude | `~/.config/orca/claude-pro.sh` | claude-sonnet-5-5 | high | ctx_ebd802ca515e | term_39043647-2cf9-40be-a7f9-981ad844cacf |
| C | codex | (none) | gpt-6.1-sol | high | ctx_c26d22fcc8a6 | term_927a2c74-a8bc-4dbd-85e1-92f913f768af |

- Orca run: `run_d6dac92308e5`; all workers `--worktree current` (folder workspace), `--keep-open`.
- Launched: 2026-11-25T08:02:28Z. All three worker-start calls exit 0, state ready.
- Known risks: B runs with --dangerously-skip-permissions; A runs with always-proceed. Isolation is prompt-only.

## Failures / anomalies
- None at launch. All three dispatches reported worker_done/succeeded: B ~08:12Z, C ~08:12Z, A ~08:22Z.
- Actual process args (from /proc) confirm requested models/effort. Codex worker also runs `--dangerously-bypass-approvals-and-sandbox` (previously unrecorded): all three workers ran unsandboxed.
- Self-reported metadata errors: B (effort, start time), C (model/effort UNKNOWN). Overridden by actual args in the completion report.
- Coordinator verification: Stack Exchange API rate-limited the coordinator IP; A-P7-C1 not independently re-run.
- Lingering processes not started by this phase: agy pid 107817 (preflight A, Neon medium), claude pid 83303 (started 14:04). Not terminated by coordinator.

## Completion
- Phase 1 completion report: `coordinator/phase-1-completion-report.md`. Stopped at Exit Gate.
