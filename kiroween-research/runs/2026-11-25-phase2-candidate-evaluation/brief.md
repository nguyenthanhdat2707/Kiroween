# Shared Brief — Phase 2A: Independent Candidate Evaluation

- Run ID: `2026-11-25-phase2-candidate-evaluation`
- Run root: `/home/tdat/Documents/Learn/Infrastructure/Hackathon/Kiroqeen/kiroween-research/runs/2026-11-25-phase2-candidate-evaluation/`
- Previous run (inputs): `/home/tdat/Documents/Learn/Infrastructure/Hackathon/Kiroqeen/kiroween-research/runs/2026-11-25-phase1-discovery/` (below: `P1/`)
- Identical for Agents A, B and C. Instructions: `prompts/phase-2-instructions.md`. Rubric: `rubric-and-anchors.md` (binding).

## 1. Objective

**Independently** research and score the 8 candidates below with the Candidate Selection Rubric. Then stop.

- A debate round (Phase 2B) follows later and will be sent to you separately.
- Do **not** rank to pick a winner, and do **not** try to agree with other agents.
- The Coordinator aggregates scores afterwards.

| ID | Candidate (source: Phase 1 report of that agent) |
|---|---|
| A-P1 | Yahoo! Pipes → user-assembled filtering and aggregation of web sources |
| A-P2 | Apple Guide → in-app guidance anchored to live UI state |
| A-P4 | Del.icio.us and Pocket → link-rot-proof bookmarks and read-later, not SaaS-dependent |
| A-P7 | Stack Overflow → preserved, human-verified fixes for edge-case errors |
| B-P1 | Devices bricked when the vendor shuts down cloud or app |
| B-P4 | Scientific instruments locked to end-of-life PCs and operating systems |
| C-P1 | Google Reader → following chosen sources without re-reading the same event |
| C-P4 | Telecare continuity during the UK PSTN switch-off |

This shortlist is the **user's preliminary judgment**, not a validated conclusion. You may conclude that a candidate is weak. You may not drop it: score all 8.

## 2. Required inputs (read before scoring)

1. `/home/tdat/Documents/Learn/Infrastructure/Hackathon/Kiroqeen/kiroween-research/AGENTS.md` (project rules)
2. `rubric-and-anchors.md` (binding anchors and weights)
3. The candidate sections in `P1/agent-a/discovery.md`, `P1/agent-b/discovery.md`, `P1/agent-c/discovery.md`. These Phase 1 reports are **shared input** for everyone.
4. `P1/quality-gate/corrections-overlay.md`: **binding label corrections**. Where it corrects a Phase 1 label, use the corrected label.
5. `P1/quality-gate/claim-verification.md` and `P1/quality-gate/overlaps.md`.

The Phase 1 reports came from different models. Treat their claims as **claims to check**, not as facts. Their reference scores are not comparable across agents (see `P1/quality-gate/calibration.md`).

## 3. Research you must add (Phase 1 did not cover these)

For **every** candidate:

1. **International relevance.**
   - Look for evidence of the problem in North America, Europe and Asia. No region is more important than another.
   - Name **concrete target users** per region, not "everyone".
   - Record cross-cultural, legal and language barriers.
   - If you found no evidence for a region, write "no evidence found", plus the queries you tried. Do not assume.
2. **Demand.**
   - Find current (2025–2026) behavioural evidence: workarounds, spending, migrations, forum volume, regulator actions.
   - Separate evidence of the **problem** from evidence that users want a **new solution**.
3. **Commercial viability.**
   - Who would pay or fund this, and is there evidence of comparable spending?
   - Write the unscored note described in rubric §4.
4. **Strongest current competitor.**
   - Confirm it with at least official documentation.
   - Re-check the "gap" claimed in Phase 1.
5. **Feasibility.**
   - Can a working core slice be built in ≤ 7 days with Kiro (deadline 4 Dec 2026 14:00 PT)?
   - What legally usable data, devices or APIs exist **now**?
6. **Explainability.** Can the problem be explained to an international judging panel in one sentence? Write that sentence.

Task B (digital heritage, endangered online communities, platform continuity) is a **separate track and is not part of this run**. You may note heritage or continuity angles of a candidate, but do not add candidates.

## 4. Evidence rules (unchanged from Phase 1)

- Label each claim VERIFIED / INFERENCE / HYPOTHESIS / UNKNOWN. VERIFIED needs a primary source plus independent confirmation, or a reproducible check.
- Give a URL, publication date and access date (2026-11-25 or later) for every new source.
- **Never fabricate** URLs, statistics, users, interviews or competitors. If a source would not open, say so.
- Search for the strongest counter-evidence for every candidate, and keep it in the report.

## 5. Deliverables (write **only** to your own folder)

### 5.1 `agent-<x>/evaluation.md`

Write in **Vietnamese** (AGENTS.md rule). Technical terms and source titles may stay in English. Use these headings, in this order:

```
# Phase 2A Evaluation — Agent <X>
## Metadata                 (model id and effort FROM YOUR LAUNCH ARGS if you can read them, else write "not observable"; start/end UTC; searches; failures)
## 1. Method
## 2. Score table          (8 rows × 8 criteria + weighted total + theme gate PASS/FAIL; for reference only, NOT a ranking)
## 3. Per-candidate evaluation   (one subsection per ID, in the order of the table in §1 of the brief)
##    For each: one-sentence pitch for an international panel · concrete target users by region (NA / EU / Asia) · demand evidence · commercial viability note · strongest competitor and gap · per-criterion score with confidence, evidence and label · strongest counter-evidence · what would change your score
## 4. Rubric challenges     (any anchor or weight you disagree with, and why; you still scored with the given weights)
## 5. Unresolved questions
## 6. References            (Ref ID | URL | title | publisher | pub date | accessed | claims | 7 reference-quality scores | weighted | Source Reliability | Reference Relevance)
```

### 5.2 `agent-<x>/scores.json`

Machine-readable. **Exactly** this schema, with all 8 candidates and all 8 criteria:

```json
{
  "agent": "A",
  "phase": "2A",
  "model_observed": "string or null",
  "effort_observed": "string or null",
  "candidates": {
    "A-P1": {
      "scores": {
        "demand":         {"score": 0, "confidence": "L", "evidence": ["url or claim id"]},
        "international":  {"score": 0, "confidence": "L", "evidence": []},
        "innovation":     {"score": 0, "confidence": "L", "evidence": []},
        "theme":          {"score": 0, "confidence": "L", "evidence": []},
        "ai":             {"score": 0, "confidence": "L", "evidence": []},
        "feasibility":    {"score": 0, "confidence": "L", "evidence": []},
        "demo":           {"score": 0, "confidence": "L", "evidence": []},
        "sustainability": {"score": 0, "confidence": "L", "evidence": []}
      },
      "theme_gate_pass": false,
      "weighted_total": 0.0
    }
  }
}
```

Scores are integers 0–5. Confidence is `H`, `M` or `L`. `weighted_total` = Σ weight × score / 5, rounded to one decimal.

## 6. Isolation and conduct

- **Do not read** other agents' Phase 2 folders (`agent-*` in this run, other than your own). Do not message other agents. This isolation is enforced only by instruction. Your process runs **unsandboxed**, so follow it strictly.
- **Do not modify** any file outside your own `agent-<x>/` folder. That includes `P1/`, `progress/`, `ideas/`, `brief.md` and the rubric. Scratch files go in `agent-<x>/scratch/`.
- Do not install packages, do not run code from community repositories, do not commit or push.
- **Skills:**
  - Recommended project skills: `../../.agents/skills/idea-red-team/SKILL.md` and `../../.agents/skills/user-problem-validation/SKILL.md`.
  - BMAD skills only if they run without waiting for user input.
  - Do not use `bmad-party-mode` or `bmad-advanced-elicitation`.
- **Never wait for user input.** If truly blocked, use `orca orchestration ask`. Otherwise record the assumption and continue.
- **Time box:** aim to finish within about 60 minutes. Prioritise `demand`, `international` and `innovation` evidence over polishing prose.
- **When finished:** report the paths, the 8 weighted totals, the gate results, the number of new references, and any failures. Partial work must be reported as partial.
