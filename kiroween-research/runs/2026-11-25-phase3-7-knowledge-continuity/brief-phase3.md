# Shared Brief — Phase 3: Focused Deep Research

- Run ID: `2026-11-25-phase3-7-knowledge-continuity`
- Run root (below: `RC/`): `/home/tdat/Documents/Learn/Infrastructure/Hackathon/Kiroqeen/kiroween-research/runs/2026-11-25-phase3-7-knowledge-continuity/`
- Mission (binding): `RC/prompts/cycle-instructions.md`, sections **1, 3, 8, 9** and the evidence rules below. Sections 4–7 describe later phases; read them for context but **do not do them now**.
- Identical for Agents A, B and C.

## 1. What you are doing

Business-analysis research on **four opportunity spaces** that a human selected because they interest them. They are **not** validated conclusions.

| Space | Short name | One-line scope |
|---|---|---|
| **S2** | Research apps after funding | Keeping academic and research web applications, tools and databases usable after their grant or funding ends |
| **T2** | Small-platform shutdown window | Helping small SaaS platforms and online communities transfer valuable assets to a successor **before** shutdown |
| **T3** | Disappearing journals | Preserving academic journals that disappear (especially small, independent or scholar-led ones) |
| **T4** | Heritage archive transfer | Preserving and transferring digital heritage archives (community, Indigenous, language, cultural collections) when the custodian can no longer maintain them |

The human's umbrella question:

> *Do these spaces share a broader problem: valuable digital knowledge, functionality and cultural assets disappearing because the organizations responsible for maintaining them no longer have sufficient resources?*

Rules:

- **Investigate each space independently first** (report §2–§5). Only after that, in report §6, test whether they share an underlying problem. "They do not share one" is a valid result.
- **Do not assume they should become one product.** Do not design a product or pick one. Solution design is Phase 5, not now.
- **Business analysis before solutions.** You may name existing solutions and mechanisms; do not propose your own architecture.
- **Preservation vs restoration.** For every space, test whether preserving content/data is enough, or whether **restoring lost functionality** (a working tool, a searchable journal, an interactive archive with its access rules) creates additional, evidenced value.
- **Theme gate, T3 and T4.** In Task B both scored `theme` = 1 under the shared anchors. Investigate whether a **legitimate** Resurrection opportunity exists inside them: a specific, verifiably discontinued or officially retired technology that is central to the problem. **Do not stretch the official theme text or the anchors to make them pass.** "No legitimate Resurrection angle found" is a valid and useful result. Apply the same test to S2 and T2 (both scored 3 in Task B).

## 2. Context you receive, and what you deliberately do not receive

**Read (binding):**

1. `/home/tdat/Documents/Learn/Infrastructure/Hackathon/Kiroqeen/kiroween-research/AGENTS.md`
2. `RC/prompts/cycle-instructions.md`
3. `/home/tdat/Documents/Learn/Infrastructure/Hackathon/Kiroqeen/kiroween-research/runs/2026-11-25-phase2-candidate-evaluation/rubric-and-anchors.md`: candidate-rubric anchors. Use them **only** to collect evidence per criterion (`rubric_evidence` in the JSON). Read the `theme` anchor carefully.
4. `RC/coordinator/kiroween-official-rules-snapshot.txt`: official rules fetched 2026-11-25 from <https://kiroween.devpost.com/rules>.

**Prior findings to test, not to accept.** These come from an earlier research round (Task B). Treat every claim as something to check. Where you confirm, contradict or extend one, cite its claim ID.

5. `/home/tdat/Documents/Learn/Infrastructure/Hackathon/Kiroqeen/kiroween-research/runs/2026-11-25-taskb-digital-preservation/synthesis/opportunity-map.md`
6. `/home/tdat/Documents/Learn/Infrastructure/Hackathon/Kiroqeen/kiroween-research/runs/2026-11-25-taskb-digital-preservation/synthesis/hypotheses-validation-plan.md`
7. `/home/tdat/Documents/Learn/Infrastructure/Hackathon/Kiroqeen/kiroween-research/runs/2026-11-25-taskb-digital-preservation/synthesis/problem-analysis.md`
8. **Lookup only:** you may open the Task B agent files `runs/2026-11-25-taskb-digital-preservation/agent-*/{report.md,cross-review.md,opportunities-revised.json}` to look up a specific claim ID or reference. Do not adopt their conclusions without checking the source.

**Not given to you, on purpose:** Phase 1 and Phase 2 scores, shortlists and rankings, and the details of earlier leading candidates. Comparison with them happens in Phase 6. Do not search for them in the project.

## 3. Evidence rules (unchanged from Task B)

- Every substantive claim gets a claim ID: `<X>-<space>-C<m>` (for example `B-T3-C4`) or `<X>-G-C<m>` for cross-space claims. Label each: VERIFIED, INFERENCE, HYPOTHESIS or UNKNOWN.
- VERIFIED needs a primary source **opened directly** plus independent confirmation, or a reproducible check. Apply: claim → primary evidence → independent confirmation → reproduction or mechanism check. Record how far each key claim got.
- A single official document opened directly supports VERIFIED **only** for a claim scoped as "X officially stated Y".
- **Search snippets are never VERIFIED evidence.** If you only saw a snippet, label the claim at most INFERENCE and mark the reference "snippet only".
- Score each reference on the 7-criterion reference rubric (Authority 20, Technical Evidence 20, Mechanism 20, Context 15, Freshness 10, Reproducibility 10, Bias 5; scores 0–5; weighted = Σ weight × score / 5). Give **Source Reliability** and **Reference Relevance** separately.
- **Do not confuse reference-quality scores with candidate-rubric scores.**
- Separate **demonstrated** demand (observed behaviour: migrations, donations, volunteer hours, spending, contracts, archive usage, rescue projects) from **hypothetical** demand.
- Keep counterevidence. Never fabricate sources, statistics, users, interviews, cases or competitors. "No evidence found" with the queries you ran is a valid entry.
- **International:** concrete cases for North America, Europe, Asia and other regions where they exist. Do not assume global applicability. Do not transfer demand from one region or user group to another.

## 4. Deliverables (write **only** to your own folder `RC/agent-<x>/`)

### 4.1 `report.md`

Write in **Vietnamese**. Technical terms and source titles may stay in English. Use exactly these headings, in this order:

```
# Phase 3 — Agent <X>
## Metadata                         (model/effort if observable, else "not observable"; start/end UTC; approx. searches; sources opened directly vs snippet-only; failures)
## 1. Method                        (BA methods chosen and why; what you did not do)
## 2. S2 — Research apps after funding
## 3. T2 — Small-platform shutdown window
## 4. T3 — Disappearing journals
## 5. T4 — Heritage archive transfer
## 6. Cross-space analysis          (only after §2–5: is there a shared underlying problem? evidence for and against; where combining them would be wrong)
## 7. Challenges to the human's framing (where the umbrella question is wrong, too broad or unjustified)
## 8. Unresolved questions
## 9. References                    (Ref ID | URL | title | publisher | pub date | accessed | opened directly or snippet | claims | 7 scores | weighted | Source Reliability | Reference Relevance)
```

Each of §2–§5 must contain these sub-headings, in this order:

```
### a. Problem and root causes          (problem tree; when preservation is NOT justified)
### b. Stakeholders and target users    (table: actor, job-to-be-done, current behaviour, willingness to contribute / pay, demonstrated vs hypothetical, evidence)
### c. Documented cases by region       (NA / EU / Asia / Other; "no evidence found" + queries when absent)
### d. Demand and consequences of inaction
### e. Existing solutions and limits    (name the strongest alternatives you checked; a claimed gap must name them)
### f. Barriers                         (legal, financial, technical, organizational)
### g. Who pays, who maintains
### h. AI: meaningful advantage or not  (vs conventional engineering; say where AI is unnecessary)
### i. Preservation vs restoring functionality
### j. Resurrection theme fit           (the specific discontinued technology, if any; anchor score you think applies and why; say plainly if none)
### k. Verdict for this space           (continue / narrow to … / drop, with the deciding evidence)
```

### 4.2 `opportunities.json`

One entry per space, plus optional narrowed sub-opportunities (id suffix `a`, `b`, e.g. `B-T3a`) when you find a specific, better-evidenced angle inside a space.

```json
{
  "agent": "A",
  "phase": 3,
  "model_observed": "string or null",
  "effort_observed": "string or null",
  "opportunities": [
    {
      "id": "A-S2",
      "space": "S2|T2|T3|T4",
      "title": "short title",
      "verdict": "continue|narrow|drop",
      "narrowed_scope": "string or null",
      "target_users": ["concrete actor"],
      "payer": "who pays, or 'none found'",
      "maintainer": "who maintains, or 'none found'",
      "regions_with_direct_evidence": ["NA|EU|Asia|Other"],
      "cases": [{"region": "EU", "case": "name", "refs": ["R3"]}],
      "demand_type": "demonstrated|mixed|hypothetical",
      "consequence_of_inaction": "one sentence",
      "strongest_alternative": "name",
      "strongest_counterevidence": "one sentence",
      "preservation_vs_restoration": "preservation-sufficient|restoration-adds-value|unclear",
      "resurrection_anchor": "specific discontinued technology, or null",
      "ai_role": "load-bearing|useful|unnecessary",
      "legal_risk": "low|medium|high",
      "key_claims": ["A-S2-C1"],
      "falsifier": "smallest experiment that would kill it",
      "rubric_evidence": {
        "demand": {"provisional_score": 0, "confidence": "L", "basis": "one sentence"},
        "international": {"provisional_score": 0, "confidence": "L", "basis": ""},
        "innovation": {"provisional_score": 0, "confidence": "L", "basis": ""},
        "theme": {"provisional_score": 0, "confidence": "L", "basis": ""},
        "ai": {"provisional_score": 0, "confidence": "L", "basis": ""},
        "feasibility": {"provisional_score": 0, "confidence": "L", "basis": ""},
        "demo": {"provisional_score": 0, "confidence": "L", "basis": ""},
        "sustainability": {"provisional_score": 0, "confidence": "L", "basis": ""}
      }
    }
  ]
}
```

Provisional scores are evidence summaries under the shared anchors, not final evaluation. Formal scoring happens in Phase 6.

## 5. Isolation and conduct

- **Do not read** the other `agent-*` folders of **this** run. Do not message other agents.
- Your process runs **unsandboxed**. These limits are enforced only by you.
- **Do not modify** anything outside `RC/agent-<x>/`. Scratch files go in `RC/agent-<x>/scratch/`.
- No package installs, no code from community repositories, no commits or pushes.
- **Skills:** recommended project skills `/home/tdat/Documents/Learn/Infrastructure/Hackathon/Kiroqeen/kiroween-research/.agents/skills/user-problem-validation/SKILL.md`, `.../idea-red-team/SKILL.md`, `.../historical-technology-discovery/SKILL.md`. No skill that waits for user input.
- **Never wait for user input.** If truly blocked, use `orca orchestration ask`.
- **Time box:** about 60 minutes. Four spaces at equal depth matters more than breadth inside one space. If you run short, finish all four §a–§k at reduced depth and say so.
- **When finished:** report the paths, verdict per space, claim counts by label, references opened directly versus snippet-only, and failures. Partial work must be reported as partial.
