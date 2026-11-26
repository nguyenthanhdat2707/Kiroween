# Shared Brief — Stage 1: Specialized Research

- Run ID: `2026-11-26-mission-heritage-resurrection`
- Run root (below: `RM/`): `/home/tdat/Documents/Learn/Infrastructure/Hackathon/Kiroqeen/kiroween-research/runs/2026-11-26-mission-heritage-resurrection/`
- Mission (binding): `RM/prompts/mission-instructions.md`. Read §1, §2, **your own agent section** (§4 for A, §5 for B, §6 for C), §7, §8 and §9 Stage 1. The other agents' sections are context only.
- This brief is identical for all agents. Your role-specific output contract is in §4 below.

## 1. What you are doing

This is **specialized** research, not three copies of the same work. Each agent owns one domain:

| Agent | Domain | Owns these questions |
|---|---|---|
| A | Digital Heritage & Human Experience | What deserves preservation and why; authenticity; how people explore and experience the past; explorer personas and journeys |
| B | Business Analysis & Sustainability | Who benefits, contributes, pays and maintains; demand evidence; operating models; rights and governance |
| C | Technical Research & Architecture | Formats, capture layers, replay and execution, storage, cost, security, architecture alternatives |

Rules:

- The human's vision (mission §1) is a **direction to test**, not a premise. Saying that part of it is wrong, too costly or already solved is a valid result.
- Stay inside your domain. When your work depends on another domain, write the dependency as a question in your "Questions for the other domains" section. Do not research it yourself.
- **Do not restart broad discovery.** Earlier research in this project already covers many cases (§2). Reuse it and cite its claim IDs. Only add new cases when your domain needs them.
- **Do not design the final product.** Product convergence is the Coordinator's job in Stage 3. A delivers explorer **experience concepts**, B delivers **operating models**, and C delivers **architecture alternatives**.

## 2. Context you receive

**Everyone reads (binding):**

1. `/home/tdat/Documents/Learn/Infrastructure/Hackathon/Kiroqeen/kiroween-research/AGENTS.md`
2. `RM/prompts/mission-instructions.md`
3. `RM/coordinator/kiroween-official-rules-snapshot.txt`: official rules fetched 2026-11-25. You may re-check the live page.
4. `/home/tdat/Documents/Learn/Infrastructure/Hackathon/Kiroqeen/kiroween-research/runs/2026-11-25-phase3-7-knowledge-continuity/human/phase-3-decision-brief.md`: the latest research summary (Vietnamese). It contains the key prior findings: nobody has been found paying for a third-party preservation tool; the spaces conflict on access defaults; only narrow anchors tied to retired technology pass the theme gate.
5. `/home/tdat/Documents/Learn/Infrastructure/Hackathon/Kiroqeen/kiroween-research/runs/2026-11-25-phase2-candidate-evaluation/rubric-and-anchors.md`: read the `theme` anchor. It defines what counts as "Resurrection" in this project.

**Role-specific prior research.** Read what is listed for you. You may open the others only to look up a specific claim ID.

| Agent | Prior research to reuse | Path (under `kiroween-research/runs/`) |
|---|---|---|
| A | Heritage archive transfer (T4) and interactive scholarship (C-T3a) findings | `2026-11-25-phase3-7-knowledge-continuity/agent-{a,b,c}/report.md` §5 and §4 (lookup) |
| A | Problem framing: value is not data; selection | `2026-11-25-taskb-digital-preservation/synthesis/problem-analysis.md` |
| B | Stakeholders, payers, demand | `2026-11-25-taskb-digital-preservation/synthesis/stakeholder-analysis.md` |
| B | Falsifiers and hypotheses H0–H8 | `2026-11-25-taskb-digital-preservation/synthesis/hypotheses-validation-plan.md` |
| B | Per-space payers and cases | `2026-11-25-phase3-7-knowledge-continuity/agent-{a,b,c}/opportunities.json` (fields `payer`, `maintainer`, `cases`) |
| C | Existing solutions and baselines | `2026-11-25-taskb-digital-preservation/synthesis/alternatives-gap-analysis.md` |
| C | Staticization, retired runtimes, Ruffle/CheerpJ | `2026-11-25-phase3-7-knowledge-continuity/agent-{a,b,c}/report.md` §2e, §2i, §4e (lookup) |

**Not given to you, on purpose:** earlier candidate scores and rankings. Stage 3 applies the candidate rubric; your job is evidence, not scoring.

## 3. Evidence rules (unchanged)

- Every substantive claim gets a claim ID `<X>-C<m>` (for example `C-C14`) and a label: VERIFIED, INFERENCE, HYPOTHESIS or UNKNOWN. In Vietnamese text you may use ĐÃ XÁC MINH / SUY LUẬN / GIẢ THUYẾT / CHƯA RÕ.
- VERIFIED needs a primary source **opened directly** plus independent confirmation, or a reproducible check. Apply: claim → primary evidence → independent confirmation → reproduction or mechanism check, and record how far each key claim got.
- A single official document opened directly supports VERIFIED **only** for a claim scoped as "X officially stated Y".
- **Search snippets are never VERIFIED evidence.** Label a snippet-only claim at most INFERENCE and mark the reference "snippet only".
- Score each reference on the 7-criterion rubric (Authority 20, Technical Evidence 20, Mechanism 20, Context 15, Freshness 10, Reproducibility 10, Bias 5; scores 0–5; weighted = Σ weight × score / 5). Give **Source Reliability** and **Reference Relevance** separately.
- Separate **demonstrated** behaviour (visits, usage, donations, deposits, contracts, volunteer hours) from **hypothetical** demand. Do not assume willingness to pay, contribution behaviour or educational demand.
- Cost estimates must state every assumption (unit prices with source and date, volumes, replication factor). Mark an estimate as an estimate.
- Keep counterevidence. Never fabricate sources, statistics, users, interviews, cases or competitors. "No evidence found", together with the queries you ran, is a valid entry.
- **Seed references (mission §7).** Evaluate them; do not accept them blindly. Each one has an owner who must open it and score it:
  - A: DPC Handbook, Smithies et al. 2019;
  - B: Smithies et al. 2019, DPC Handbook, Kiroween rules;
  - C: WACZ spec, Software Heritage, DPC Handbook.

  For each, find independent confirmation, a competing approach, expert criticism or a documented failure where one exists.

## 4. Deliverables (write **only** to your own folder `RM/agent-<x>/`)

Every report is written in **Vietnamese**. Technical terms and source titles may stay in English. Every report starts with a `## Metadata` section (model and effort if observable, else "not observable"; start/end UTC; approx. searches; sources opened directly vs snippet-only; failures) and ends with these sections:

```
## Questions for the other domains    (numbered; addressed to A, B or C)
## Challenges to the human's vision   (where §1/§2 of the mission is wrong, too broad or already solved)
## Unresolved questions
## References                         (Ref ID | URL | title | publisher | pub date | accessed | opened directly or snippet | claims | 7 scores | weighted | Source Reliability | Reference Relevance)
```

### Agent A → `agent-a/heritage-and-experience.md`

```
# Stage 1 — Agent A: Digital Heritage & Human Experience
## Metadata
## 1. Method
## 2. Physical-world preservation mechanisms   (museums, libraries/archives, restoration, archaeology/reconstruction, time capsules, seed banks, cultural heritage, institutional collections; for each, the 7 questions of mission §4 as a table)
## 3. Transferable principles and where the analogy breaks
## 4. Existing digital museums, software collections, web history and interactive archives   (what they do, usage evidence, limits, failures)
## 5. Authentic capture vs AI-generated reconstruction   (how to label, provenance, known cases of confusion)
## 6. Explorer personas, motivations and journeys   (concrete; demonstrated vs hypothetical; evidence)
## 7. Evidence of educational, research or cultural value
## 8. Three explorer experience concepts   (each: persona, journey, artifacts involved, past-vs-present element, authenticity handling, supporting evidence, strongest counterargument, closest existing alternative, theme anchor if any, dependencies on B and C)
```

### Agent B → `agent-b/business-and-sustainability.md`

```
# Stage 1 — Agent B: Business Analysis & Sustainability
## Metadata
## 1. Method
## 2. Documented cases   (websites abandoned after declining use; research apps after grants; small communities shutting down; discontinued software; heritage collections with limited resources; by region)
## 3. Stakeholder map   (explorers vs contributors/beneficiaries; benefits, contribution, payment, maintenance; demonstrated vs hypothetical)
## 4. Explorer-side demand evidence
## 5. Existing preservation institutions and funding models
## 6. Operating model alternatives   (nonprofit, community-supported, institutional, freemium, bring-your-own-storage: who pays, cost drivers, failure modes, real examples)
## 7. Why use this instead of existing archives
## 8. Selection: what deserves preservation, and who decides
## 9. Copyright, privacy, consent and cultural restrictions   (by jurisdiction)
## 10. Adoption barriers
## 11. International relevance   (NA / EU / Asia / other; "no evidence found" + queries when absent)
## 12. Validation experiments   (hypothesis, smallest falsifying test, effort, kill criterion)
```

### Agent C → `agent-c/technical-architecture.md`

```
# Stage 1 — Agent C: Technical Research & Architecture
## Metadata
## 1. Method
## 2. Technology survey   (each technology in mission §6: what it does, maturity, adoption, limits, evidence)
## 3. Capture-layer matrix   (appearance, content, data, interactions, executable functionality, original runtime × the capture methods that preserve each)
## 4. What cannot be recovered from a public website alone
## 5. The seven architectural alternatives of mission §6, assessed
## 6. Three architecture alternatives   (each: Mermaid component diagram, data flow, preservation and recovery workflows, storage requirements, operating-cost estimate with explicit assumptions, failure scenarios, limitations, reusable open-source components, potential AI contributions, MVP feasibility within ~1 week)
## 7. Cost comparison vs continuously hosting the original   (capture, retrieval, indexing, metadata, replication, maintenance, AI inference; assumptions table)
## 8. Security of replaying or executing untrusted historical content
## 9. Gap analysis   (where existing formats and tools already suffice; any real gap, with the alternatives checked)
```

### Everyone → `agent-<x>/summary.json`

```json
{
  "agent": "A",
  "stage": 1,
  "model_observed": "string or null",
  "effort_observed": "string or null",
  "claims": {"VERIFIED": 0, "INFERENCE": 0, "HYPOTHESIS": 0, "UNKNOWN": 0},
  "references": {"opened_directly": 0, "snippet_only": 0},
  "seed_references": [{"url": "", "opened": true, "weighted_score": 0, "verdict": "one sentence"}],
  "deliverables": [
    {
      "id": "A-E1",
      "kind": "experience|operating_model|architecture",
      "title": "short title",
      "key_claims": ["A-C3"],
      "strongest_counterevidence": "one sentence",
      "closest_existing_alternative": "name",
      "depends_on": ["B: question 2", "C: question 1"]
    }
  ],
  "failures": ["string"]
}
```

Deliverable IDs: A-E1…E3 (experiences), B-M1…M5 (operating models), C-X1…X3 (architectures).

## 5. Isolation and conduct

- **Do not read** the other `agent-*` folders of **this** run. Do not message other agents.
- Your process runs **unsandboxed**. These limits are enforced only by you.
- **Do not modify** anything outside `RM/agent-<x>/`. Scratch files go in `RM/agent-<x>/scratch/`.
- No package installs, no cloning or running community code, no commits or pushes.
- **Agent C:** do **not** run captures, crawlers, emulators or historical software in this stage. Fetching documentation pages and specs is fine. Any measurement experiment is a Stage 3 proposal that needs the human's approval.
- **Skills:** recommended project skills under `/home/tdat/Documents/Learn/Infrastructure/Hackathon/Kiroqeen/kiroween-research/.agents/skills/` (`user-problem-validation`, `idea-red-team`, `historical-technology-discovery`). Use no skill that waits for user input.
- **Never wait for user input.** If truly blocked, use `orca orchestration ask`.
- **Time box:** about 60 minutes for A and B, about 75 minutes for C. If you run short, complete every heading at reduced depth and say so.
- **When finished:** report the paths, deliverable IDs, claim counts by label, references opened directly versus snippet-only, and failures. Partial work must be reported as partial.
