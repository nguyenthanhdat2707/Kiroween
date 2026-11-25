# Shared Brief — Task B, Round 1: Independent Discovery

- Run ID: `2026-11-25-taskb-digital-preservation`
- Run root (below: `RB/`): `/home/tdat/Documents/Learn/Infrastructure/Hackathon/Kiroqeen/kiroween-research/runs/2026-11-25-taskb-digital-preservation/`
- Full mission text (binding): `RB/prompts/taskb-instructions.md`. Read it completely. This brief only adds the output contract, the context and the rules.
- Identical for Agents A, B and C.

## 1. What you are doing

Independent business-analysis research on the human-proposed hypothesis:

> *Can we preserve the value created by digital platforms even when the original platforms can no longer survive?*

- Treat the hypothesis as something to **test**, not a premise. Concluding that a dimension or opportunity is **not** worth pursuing is a valid result.
- Do **not** design an application. Do **not** pick a product.
- Cover the sections of the mission in this order: §4.1 root causes, §4.2 stakeholders, §4.3 dimensions, §4.4 existing solutions, §4.5 sustainability, §4.6 AI, §4.7 legal, §5 international.
- Choose business-analysis methods that fit the problem (mission §6). Say why you chose them.

## 2. Context you receive, and what you deliberately do not receive

**Read:**

1. `/home/tdat/Documents/Learn/Infrastructure/Hackathon/Kiroqeen/kiroween-research/AGENTS.md` (project rules, binding)
2. `RB/prompts/taskb-instructions.md` (mission, binding)
3. `/home/tdat/Documents/Learn/Infrastructure/Hackathon/Kiroqeen/kiroween-research/runs/2026-11-25-phase2-candidate-evaluation/rubric-and-anchors.md`: candidate-rubric anchors. Use them **only** to collect evidence per criterion (mission §9).
4. `RB/coordinator/kiroween-official-rules-snapshot.txt`: official rules, fetched 2026-11-25 from <https://kiroween.devpost.com/rules>. You may re-check the live page.

**Already explored in this project.** Use this only to avoid duplication. It is not a ranking. Revisit an item only with a genuinely new angle, and say so.

- **Cloud-dependent devices bricked when the vendor shuts down** (Car Thing, Wemo, Nest, AirPort; protocol recovery from traces).
- **Web link rot and read-later shutdown** (Pocket, Del.icio.us; personal bookmark archives).
- Declining Q&A platforms: Stack Overflow answer maintenance, CodeProject, DaniWeb, Yahoo Groups/Answers.
- Discord/Slack knowledge being unindexed (Usenet analogy); InfoPath forms after end of life; Flash/SWF; Jamboard; Google Reader; Yahoo! Pipes; DMOZ and webrings; VHS, cassette and floppy family media; Hán Nôm genealogies.

You do **not** receive earlier scores, shortlists or rankings. This is deliberate: earlier results must not constrain new discovery.

## 3. Evidence rules (mission §7)

- Every substantive claim gets a claim ID (`<X>-O<n>-C<m>` inside an opportunity, `<X>-G-C<m>` for general claims) and a label: VERIFIED, INFERENCE, HYPOTHESIS or UNKNOWN.
- VERIFIED needs a primary source **opened directly** plus independent confirmation, or a reproducible check.
- **Search snippets are never VERIFIED evidence.** If you only saw a snippet, label the claim at most INFERENCE and mark the reference "snippet only".
- Score each reference on the 7-criterion reference rubric. Give **Source Reliability** and **Reference Relevance** separately.
- Keep counterevidence. Never fabricate sources, statistics, users, interviews or competitors.
- Separate **demonstrated** demand (observed behaviour: migrations, donations, volunteer hours, spending, archive usage) from **hypothetical** demand.

## 4. Deliverables (write **only** to your own folder `RB/agent-<x>/`)

### 4.1 `report.md`

Write in **Vietnamese**. Technical terms and source titles may stay in English. Use exactly these headings, in this order:

```
# Task B Round 1 — Agent <X>
## Metadata                     (model/effort from your launch args if observable, else "not observable"; start/end UTC; approx. searches; sources opened directly vs snippet-only; failures)
## 1. Method                    (which BA methods and why; what you did not do)
## 2. Root causes               (problem tree: why platforms disappear; adoption decline = cause or symptom; commercially failed vs genuinely obsolete; when preservation is NOT justified)
## 3. Stakeholders and demand   (table per stakeholder: concrete actors, job-to-be-done, current behaviour, willingness to contribute, willingness to pay, demonstrated vs hypothetical, evidence)
## 4. Preservation dimensions   (all 7 from mission §4.3: value created, technical realism, economic realism, evidence)
## 5. Existing solutions and gaps (per approach in mission §4.4: strengths, limits, adoption barriers, unresolved problems; claimed gaps must name the alternatives checked)
## 6. Sustainability            (who benefits, pays, maintains; ongoing costs; viable models; failures)
## 7. AI contribution           (where AI adds measurable value vs conventional engineering; where AI is unnecessary)
## 8. Legal and ethical constraints (copyright, licensing, privacy, consent, data protection, preservation exceptions; public vs legally redistributable; by jurisdiction)
## 9. International evidence    (North America / Europe / Asia / other: concrete cases; cross-cultural barriers; "no evidence found" + queries when absent)
## 10. Opportunity spaces       (3–6 spaces; for each: problem, target users, dimension(s), why now, strongest alternative, strongest counterevidence, evidence per candidate-rubric criterion, key hypotheses, smallest falsifying experiment)
## 11. Challenges to the mission hypothesis (where the central question is wrong, too broad or unjustified)
## 12. Unresolved questions
## 13. References               (Ref ID | URL | title | publisher | pub date | accessed | opened directly or snippet | claims | 7 scores | weighted | Source Reliability | Reference Relevance)
```

### 4.2 `opportunities.json`

Machine-readable, for synthesis:

```json
{
  "agent": "A",
  "round": 1,
  "model_observed": "string or null",
  "effort_observed": "string or null",
  "opportunities": [
    {
      "id": "A-O1",
      "title": "short title",
      "dimensions": ["content|knowledge|software|user-data-workflows|community|heritage|operational"],
      "target_users": ["concrete actor"],
      "regions_with_direct_evidence": ["NA|EU|Asia|Other"],
      "demand_type": "demonstrated|mixed|hypothetical",
      "strongest_alternative": "name",
      "strongest_counterevidence": "one sentence",
      "ai_role": "load-bearing|useful|unnecessary",
      "legal_risk": "low|medium|high",
      "key_claims": ["A-O1-C1"],
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

Provisional scores are evidence summaries using the Phase 2 anchors. They will **not** be compared against Phase 2 candidates in this task.

## 5. Isolation and conduct

- **Do not read** the other `agent-*` folders in this run, other Task B outputs, or Phase 1/2 agent reports. Do not message other agents.
- Your process runs **unsandboxed**. These limits are enforced only by you.
- **Do not modify** anything outside `RB/agent-<x>/`. Scratch files go in `RB/agent-<x>/scratch/`.
- No package installs, no code from community repositories, no commits or pushes.
- **Skills:**
  - Recommended project skills: `../../.agents/skills/user-problem-validation/SKILL.md`, `../../.agents/skills/idea-red-team/SKILL.md`, `../../.agents/skills/historical-technology-discovery/SKILL.md`.
  - BMAD skills only if they run without waiting for user input.
  - No `bmad-party-mode` or `bmad-advanced-elicitation`.
- **Never wait for user input.** If truly blocked, use `orca orchestration ask`.
- **Time box:** about 60 minutes. Depth over breadth.
- **When finished:** report the paths, the number of opportunity spaces, the number of claims by label, references opened directly versus snippet-only, and failures. Partial work must be reported as partial.
