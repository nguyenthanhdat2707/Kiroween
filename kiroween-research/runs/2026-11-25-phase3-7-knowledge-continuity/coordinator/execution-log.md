# Engineering Execution Log — Phases 3–7

Measured facts are labelled **[measured]**; interpretations are labelled **[inferred]**. Plan: [`workflow-plan.md`](workflow-plan.md).

## 0. Phase 3 pre-launch

### Runtime security re-check (2026-11-25, before launch) [measured]

- Orca 1.4.272. Settings read in read-only mode from `profile-state.db`:
  - `agentPermissionDefault = full-access`;
  - `agentPermissionOverrides = {antigravity: own}`;
  - `agentCmdOverrides`: antigravity → `agy-api.sh`, claude → `claude-pro.sh`.
- **Unchanged since Task B.** Workers would run as Claude `--dangerously-skip-permissions`, Codex `--dangerously-bypass-approvals-and-sandbox`, and agy `always-proceed`.
- No per-launch sandbox flag exists in `worker-start`.
- bubblewrap 0.13.1 is installed. It was tested as a boundary in Task B scratch, but **never with the agent CLIs running inside it**, and Orca has no hook for wrapping a worker in it without changing your `agentCmdOverrides`.
- No Task B or Phase 2 worker processes are still alive. The only agent process is this coordinator.
- **Unresolved risk:** a worker can read and write anything your user account can, reach the network, and use your credentials. Isolation is enforced only by instructions plus a post-run audit. The audit detects changes to the files in the snapshot; it does not detect reads, network actions, or changes outside `kiroween-research/`.

### Safety gate decision

- **User decision: "Accept risk, scoped"** for Phase 3 only. The alternatives offered were: build a bwrap boundary first, coordinator-only, or don't launch. Approval does not carry over to Phase 4.

### Integrity snapshot [measured]

- `pre-launch-checksums.sha256`: 133 files under `kiroween-research/`, excluding this run's `agent-*` folders and every `scratch/` folder. Written to scratch first, then copied, so it does not hash itself.

### Context selection and handoff decisions

| Decision | Choice | Why | Trade-off |
|---|---|---|---|
| Sessions | Fresh, as you instructed | No carry-over from Task B memory | Agents re-read the prior findings from files |
| Prior findings | Task B `opportunity-map`, `hypotheses-validation-plan` and `problem-analysis` given as **claims to test**. Task B agent files are allowed for **claim-ID lookup only**. | The four spaces came from Task B; re-deriving them blind wastes the 60-minute box. The validation plan holds the falsifiers. | Anchoring risk: agents may inherit Task B framings. Partly offset by requiring confirm / contradict / extend with claim IDs. |
| Withheld | Phase 1/2 scores, shortlists, rankings; B-P1 / A-P4 details | Comparison is Phase 6's job. Exposure now would bias Phase 3 verdicts toward or away from the leaders. | Agents cannot flag overlap with B-P1 or A-P4. Those overlaps were already noted in the Task B map. |
| Coverage | All agents investigate all four spaces; no roles | The mission says all four; triangulation feeds Phase 4 | About 3× the cost of splitting; less depth per space |
| Theme | Anchors restated; explicit "do not stretch"; "none found" is a valid result | Your §3 instruction about T3 and T4 | Agents may still over-claim; Phase 4 checks this |
| Effort | Medium for all three. Escalation only through a separate, targeted worker, with the reason recorded before launch. | Effort is fixed per process (Task B finding) | — |

## 1. Phase 3 launch

- Orca run `run_8a9466b24292`. Fresh workers, `--worktree current`, `--keep-open`. Launched 2026-11-25T16:15:37Z. Raw launch responses are in `launch-{a,b,c}.json`.

| Agent | PID | Runtime args (from /proc) [measured] | Dispatch | Task | Terminal |
|---|---|---|---|---|---|
| A | 45543 | `agy --settings ~/.config/orca/agy-api.json --model gemini-4-neon-medium` | ctx_c8f7273ef3f5 | task_05a4f1f0502b | term_7fab2529-a09d-40fa-aa44-c9dc0bf04950 |
| B | 45544 | `claude --dangerously-skip-permissions --model claude-sonnet-5-5 --effort medium` | ctx_bab79d229dd2 | task_e252383cc298 | term_b0cfb5ed-5df4-443f-8b82-f35c84ea3338 |
| C | 45576 | `codex --dangerously-bypass-approvals-and-sandbox -m gpt-6.1-sol -c model_reasoning_effort=medium` | ctx_57bfad7d7cef | task_a4b88b46fd57 | term_f82ad1a5-9e36-4a31-b728-e9aa6d3ed51e |

- Effort is medium for all three. No Astra model and no extra-high effort. No escalation planned.

## 2. Failures and anomalies

- **Agent A model resolution [measured].** The agy log (`~/.gemini/antigravity-cli/log/cli-20261125_231542.log`) shows two warnings at startup:
  - `Model ID gemini-4-neon-medium not in local config, defaulting to CCPA`;
  - `failed to apply model override: … not recognized as a known model`.

  One second later the same log shows `Propagating selected model override to backend: label="Gemini 4 Neon (Medium)"`, and A's JSON self-reports "Gemini 4 Neon (Medium)". **[inferred]** The intended model was applied after the early failure. Not checked: whether Task B's agy logs show the same warnings. This is a harness observability gap, because the per-request model name is not logged.
- **Fetch failures (self-reported):** sites blocked by Anubis or robot challenges, 403/404/405/500/502 errors, a TLS error (curl exit 60) and timeouts. Affected sources include drupal.org, Adobe, EUR-Lex, the Mukurtu docs and the JLSC full text. Each agent recorded its failures in its Metadata section.
- **Contract deviation:** A's report names the narrowed scopes A-S2a and A-T2a, but A's JSON stores them only in `narrowed_scope`, not as separate entries. This is permitted by the schema (sub-entries are optional) and is noted for Phase 4.

## 3. Phase 3 results [measured]

| Agent | Wall time | Input tokens (cached) | Output tokens | Report words | JSON entries | Claims V/I/H/U (self-reported) | Refs: opened directly / snippet |
|---|---|---|---|---|---|---|---|
| A (agy) | ~13 min (16:15:37Z – report written 16:28:31Z) | not measurable | not measurable | 12,266 | 4 | 20/13/1/0 | 27 / 7 |
| B (claude) | 9 min 32 s (16:15:51Z – 16:25:23Z) | 3,246,723 (3,077,753 cache read; 168,916 cache write) | 66,785 | 11,608 | 7 | 18/22/5/4 (15 of the VERIFIED are "source X states") | 23 / 14 |
| C (codex) | 14 min 57 s (16:15:55Z – 16:30:51Z) | 7,260,721 (6,994,560 cached) | 34,032 (6,923 reasoning) | 9,289 | 5 | 24/34/4/4 | 45 / 3 |

- **Integrity audit:**
  - the only pre-launch file that changed is this log (the coordinator's appends);
  - no new files outside the agent folders, apart from this log and `launch-*.json`;
  - nothing outside `kiroween-research/` (searched two levels up) was modified after launch;
  - no peer-folder path of this run appears in B's transcript, C's rollout or A's agy CLI data.
- Outputs frozen by hash in `p3-outputs.sha256`.
- Contract coverage: all three reports have every required heading and all of the sub-headings a–k in §2–§5.
- Escalation: none. No dispute arose that needs more reasoning on a shared text.

### Verdicts per space [measured from JSON]

| Space | A | B | C |
|---|---|---|---|
| S2 | narrow → static/WASM revival on retired runtimes (theme 3) | narrow → **B-S2a** Flash / Java applet / Fusion Tables tools (theme 3, continue) | narrow → functional handoff (theme **1**, no anchor) |
| T2 | narrow → pre-shutdown export bridge (theme 3; payer none; AI unnecessary) | **drop** (no payer at shutdown; prevention, not revival) | narrow → Glitch retirement (theme 3, conditional, low confidence) |
| T3 | **drop** (theme 1) | narrow → **B-T3a** OJS 2.x EOL (theme 2, conditional) | drop; **C-T3a** Flash-based interactive scholarship such as Vectors (theme 3, demand 1) |
| T4 | **drop** (theme 1; Drupal 7 → Mukurtu 4 counted as a routine migration, ≤ 2) | narrow → **B-T4a** customised Mukurtu 3 on Drupal 7 (theme 3, continue) | **drop** (theme 1) |

- **[inferred] Convergence:**
  - all three see the umbrella as a valid **description** but too broad to act on;
  - all three say combining the spaces would be wrong, because the preservation goals conflict (T3 is public by default, T4 restricted by default);
  - all three find no payer for a third-party **tool** (H0 still not confirmed);
  - all three find that a valid Resurrection anchor exists only when a space is narrowed to a specific retired technology;
  - the convergent candidate anchor is **Flash / retired runtimes behind research or scholarly interactive works** (A-S2a, B-S2a, C-T3a).
- **[inferred] Divergence for Phase 4:**
  - T2: A and C narrow it, B drops it;
  - T4: is the Drupal 7 / Mukurtu 3 angle theme 3 (B) or a routine migration at ≤ 2 (A)?
  - S2 theme: 3 (A, B) vs 1 (C);
  - whether Ruffle and CheerpJ already close the Flash/applet gap (B and C both raise this; nobody measured it).
- **[inferred] Label discipline:** A's VERIFIED share (20/34 = 59%) is lower than in Task B (90%), but still the highest of the three. B (18/49 = 37%) and C (24/66 = 36%) are close to each other. A again gives international 5H to an opportunity with no proven buyer.

## 4. Phase 3 exit gate

- Human brief: `human/phase-3-decision-brief.md`, written with the better-writing skill. All claim IDs and links were checked.
- **Stopped. Awaiting:**
  - P3-1: approval to run Phase 4, and a fresh security decision (the Phase 3 approval does not carry over);
  - P3-2: which entries Phase 4 cross-reviews;
  - P3-3: whether to accept the narrow "retired technology" anchor;
  - P3-4: the time budget;
  - G6: the `progress/` update.
- Workers A, B and C are kept open (idle) for Phase 4 follow-up dispatches.

## 5. Superseded (2026-11-26)

- At this gate the user sent a new mission (Digital Heritage & Resurrection Platform). Draft Phases 4–7 are superseded by run `2026-11-26-mission-heritage-resurrection`. P3-1 to P3-4 were not answered. Phase 3 outputs remain frozen and are reused as prior research.
