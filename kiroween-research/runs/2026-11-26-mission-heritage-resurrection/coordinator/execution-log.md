# Engineering Execution Log — Mission: Digital Heritage & Resurrection Platform

Measured facts are labelled **[measured]**; interpretations are labelled **[inferred]**. Plan: [`workflow-plan.md`](workflow-plan.md).

## 0. Stage 1 pre-launch

### Runtime and security re-check (2026-11-26, before launch) [measured]

- Orca 1.4.272. Settings read in read-only mode:
  - `agentPermissionDefault = full-access`;
  - `agentPermissionOverrides = {antigravity: own}`;
  - `agentCmdOverrides`: antigravity → `agy-api.sh`, claude → `claude-pro.sh`.

  **Unchanged since Phase 3.**
- Workers would run as Claude `--dangerously-skip-permissions`, Codex `--dangerously-bypass-approvals-and-sandbox` and agy `always-proceed`. No per-launch sandbox flag exists.
- No Phase 3 worker processes are still alive, so fresh sessions are guaranteed.
- **Model availability:** all three model and effort combinations were launched successfully in earlier phases:
  - C at high: Phase 1;
  - B at medium: Phase 3;
  - A as `gemini-4-neon-medium`: Phase 3, with a startup "not recognized" warning followed by "Gemini 4 Neon (Medium)" being applied.

  Availability is re-confirmed from /proc and logs after launch.
- **Unresolved risk (same as Phase 3):** a worker can read and write anything the user account can, reach the network, and use your credentials. Isolation is enforced by instructions plus a post-run audit. The audit cannot detect reads, network actions, or changes outside `kiroween-research/`.
- **New risk in this mission:** Agent C researches the replay and execution of untrusted historical content. The brief forbids running captures, crawlers, emulators or historical software in Stage 1, but that ban is enforced only by instructions.

### Safety gate decision

- **User decision: "Accept risk, scoped"** for Stage 1 only. The alternatives offered were: build a bwrap boundary first, or don't launch.

### Context selection [measured]

- See `workflow-plan.md` and `brief-stage1.md` §2: a shared core plus per-role prior research; earlier scores withheld.

## 1. Stage 1 launch

- Orca run `run_952206765e94`, launched 2026-11-26T02:38:41Z. Fresh workers, `--worktree current`, `--keep-open`. Raw launch responses are in `launch-{a,b,c}.json`.

| Agent | PID | Runtime args (from /proc) [measured] | Dispatch | Task | Terminal |
|---|---|---|---|---|---|
| A | 21339 | `agy --settings ~/.config/orca/agy-api.json --model gemini-4-neon-medium` | ctx_cd06952b65d6 | task_e6b460f1407b | term_b3fb2503-cdb6-4424-bfc1-3ab13e533ae7 |
| B | 21336 | `claude --dangerously-skip-permissions --model claude-sonnet-5-5 --effort medium` | ctx_4c6480b8d180 | task_7aaba427bd22 | term_60b9b6fb-148d-4fa7-8bc6-cc6f799be4c6 |
| C | 21372 | `codex --dangerously-bypass-approvals-and-sandbox -m gpt-6.1-sol -c model_reasoning_effort=high` | ctx_91ced28ce1a8 | task_bcdde0974e11 | term_b9b1e957-f2fb-4080-8b54-9339dd1a50a8 |

- C runs at high for the whole stage, because effort cannot change within a process. No Astra model and no extra-high effort.

## 2. Stage 1 failures and anomalies

- **Agent A model resolution [measured].** The startup sequence matches Phase 3: first `failed to apply model override: … not recognized`, then `Propagating selected model override … "Gemini 4 Neon (Medium)"`. A's JSON self-reports "Gemini 4 Neon (Medium)".
- **Fetch failures (self-reported):**
  - softwareheritage.org would not open for C (TLS error and timeout), so the seed is scored 0 and not evaluated; B could not open it either;
  - other failures: perma.cc, opencollective, Trove, UKWA, UNESCO, rhizome ArtBase, bbc.com, EaaSI and LoC pages;
  - oldweb.today returned an empty single-page-app shell.
- **Obsidian:** `../.obsidian/workspace.json` changed at 09:59:14 local time. The Obsidian app (pid 12104) is running on the vault, and no worker transcript or log mentions `.obsidian`. **[inferred]** The app wrote the file, not a worker.

## 3. Stage 1 results [measured]

| Agent | Wall time | Input tokens: total (cached / uncached) | Output tokens | Report words | Deliverables | Claims V/I/H/U | Refs: direct / snippet |
|---|---|---|---|---|---|---|---|
| A (agy, Neon medium) | ~11 min (02:38:41Z – done message 02:49:56Z) | not measurable | not measurable | 12,467 | A-E1..E3 | 14/4/0/0 | 29 / 6 |
| B (claude, medium) | 8 min 25 s (02:38:43Z – 02:47:08Z) | 4,857,983 (4,669,538 cache read + 188,369 cache write / 76 uncached) | 57,674 | 11,948 | B-M1..M5 | 19/24/2/1 | 26 / 19 |
| C (codex, **high**) | 20 min 30 s (02:38:47Z – 02:59:17Z) | 4,405,019 (4,226,432 cached / 178,587 uncached) | 52,103 (20,217 reasoning) | 12,040 | C-X1..X3, 3 Mermaid diagrams | 23/16/10/3 | 41 / 0 |

- **Integrity audit:**
  - the only pre-launch file that changed is this log;
  - no new files outside the agent folders except coordinator files;
  - no peer-folder path of this run appears in B's transcript, C's rollout or A's agy data;
  - C's scratch holds documentation fetch scripts and a finalize script, with no capture, crawler or emulator invocation (searched for `subprocess`, `os.system`, docker, qemu, warcio and browsertrix: none).
- Outputs frozen by hash in `s1-outputs.sha256`. All required headings and all four closing sections are present in every report.
- **Escalation:** none.

### Duplication check (mission §10) [measured, with limits]

- URL overlap in Stage 1, specialized:
  - pairwise 3 (A–B), 1 (A–C) and 1 (B–C) of about 42–45 URLs each;
  - one URL shared by all three: the DPC Handbook seed.
- Phase 3 baseline, identical briefs: pairwise 4, 3 and 2 of 37–48; two URLs shared by all three.
- **[inferred] URL overlap was already low in Phase 3**, so this metric **cannot** show that specialization reduced duplication. Phase 3 duplication was at the **case** level (Cohost, Mukurtu, PKP PN in all three), which URL counts do not capture. In Stage 1, the clear case-level overlap is Conifer's shutdown, cited independently by A and B. No claim is made that specialization caused lower duplication.

### Seed reference scores (calibration signal) [measured]

| Seed | A | B | C |
|---|---|---|---|
| DPC Handbook | 93 | 68 | 85 |
| Smithies et al. 2019 | 93 | 82 | — |
| WACZ spec | — | — | 95 |
| Software Heritage | — | not fetched | 0 (not opened) |
| Kiroween rules | — | 74 | — |

- **[inferred]** On the same source (DPC), the spread is 25 points. The direction (A highest) matches every earlier phase.

### Early convergence across domains [inferred, before cross-review]

- **All three:** the core storage and replay infrastructure exists (Wayback, WACZ/ReplayWeb, Ruffle, Flashpoint, EaaSI, IA software collection). Long-term cost is human labour, not bytes. A Resurrection anchor requires a specific retired technology at the centre of the demo.
- **B:** explorer demand is demonstrated only in general and already served by large free providers. The only reason not yet refuted for a new platform is **curated context and past-vs-present comparison built on existing archives** (B-C37, a hypothesis). Payers exist only on the capture side.
- **C cost model** (assumptions, not measurements; C-C31):
  - monthly totals for 100 artifacts are about USD 233 (X1), 287 (X2) and 410 (X3), against about USD 7,953 for continuously hosting 100 apps as dedicated tasks;
  - labour dominates (C-C32);
  - the continuous-hosting baseline assumes one dedicated task per app, and C notes that shared hosting would narrow the gap.
- **A:** users come to web archives mainly for targeted lookups and nostalgia play, not museum-style browsing. That is A's own counterevidence to A-E1.
