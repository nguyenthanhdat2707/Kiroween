# Candidate Selection Rubric — shared scoring anchors

Binding for Agents A, B, C and the Coordinator. Agents may **challenge** an anchor or weight in the `Rubric challenges` section of their report, but must **score with the weights and anchors below**.

## 1. Three different rubrics — do not mix them

| Rubric | What it scores | Used in |
|---|---|---|
| Reference-quality rubric (Authority 20, Technical Evidence 20, Mechanism 20, Context 15, Freshness 10, Reproducibility 10, Bias 5) | How well **one source** supports **one claim** | Phase 1, 1.5, and still for every reference cited in Phase 2 |
| **Candidate Selection Rubric (this file)** | How promising a **candidate problem space** is, before anything is built | Phase 2 |
| Official Kiroween judging (Potential Impact, Technological Implementation, Design, Innovation/Idea, Presentation; 20% each) | A **finished, working submission**, judged after 4 Dec 2026 | Judges only |

The candidate rubric does **not** score Kiro usage (20% of official judging) and only partly covers Design (20%). A candidate-rubric Top 3 is therefore **not** a prediction of judges' scores. Do not present it as one.

## 2. Weights and gate

| Key | Criterion | Weight |
|---|---|---|
| `demand` | Real Problem & User Demand | 20% |
| `international` | International Relevance | 15% |
| `innovation` | Innovation & Differentiation | 15% |
| `theme` | Resurrection Theme Fit | 15% — **gate: must be ≥ 3 to be Top-3 eligible** |
| `ai` | Technical & AI Contribution | 10% |
| `feasibility` | Implementation Feasibility | 10% |
| `demo` | Demo & Storytelling Potential | 10% |
| `sustainability` | Long-term Sustainability | 5% |

**Weighted total (0–100)** = Σ (weight × score / 5).

## 3. Anchors (score 0–5)

Scores 2 and 4 lie between the anchors written for 1, 3 and 5. Every score must also carry:

- **confidence**: H, M or L;
- **evidence**: URLs or Phase 1 claim IDs;
- the evidence label (VERIFIED / INFERENCE / HYPOTHESIS / UNKNOWN) of its key support.

If evidence is missing, score from what exists, set confidence to **L**, and say so. Do not invent evidence to justify a higher score.

### `demand` — Real Problem & User Demand (20%)

| Score | Anchor |
|---|---|
| 5 | Direct, current (2025–2026) evidence from the **concrete target users** that they experience the problem **and** act on it: workarounds, money or time spent, migration effort, sustained requests. At least 2 independent sources, at least one quantitative. |
| 3 | Credible current secondary evidence that the problem exists (official documents, surveys, regulator actions, vendor EOL notices). No direct evidence that target users want a **new** solution. |
| 1 | Only anecdotes, historical adoption, nostalgia, or the author's inference. |
| 0 | No evidence, or evidence that the problem is already solved for the target users. |

None of the 8 candidates has interviews. A score of 5 needs primary behavioural evidence. Strong secondary behavioural evidence can reach 4.

### `international` — International Relevance (15%)

| Score | Anchor |
|---|---|
| 5 | Independent evidence that the problem exists in **at least 3** of {North America, Europe, Asia}, concrete target users named in each, and no major cross-cultural or legal barrier. |
| 3 | Evidence in 2 regions, **or** in 1 region plus a verified structural reason it generalises (for example a global vendor EOL, or the same technology deployed elsewhere). |
| 1 | Evidence from a single country; generalisation is assumed. |
| 0 | Inherently single-jurisdiction, with no analogue found. |

Do not penalise a local, cultural or heritage origin if a broader analogue is evidenced. No region is weighted above another.

### `innovation` — Innovation & Differentiation (15%)

| Score | Anchor |
|---|---|
| 5 | Strongest current competitors identified and checked (official documentation at minimum); a **specific, demonstrable** capability gap remains that the candidate fills. |
| 3 | A gap is plausible from the documentation, but competitors partly cover the core job. |
| 1 | Competitors already cover the core job; the difference is cosmetic or a feature add-on. |
| 0 | Direct clone of an existing product. |

Score differentiation against **today's** alternatives, not against the dead technology. Novelty of the revival framing alone belongs in `theme`, not here.

### `theme` — Resurrection Theme Fit (15%, gate ≥ 3)

Official text: "Bring your favorite dead technology back to life. Reimagine obsolete tech with today's innovations or solving tomorrow's problems."

| Score | Anchor |
|---|---|
| 5 | A specific, verifiably discontinued technology or product is **central to both the product and the demo**. |
| 4 | A discontinued product is the clear anchor; part of the value lies in the revived workflow. |
| 3 | A specific technology with an **officially announced or completed retirement** anchors a revived workflow or capability. |
| 2 | A living technology in decline; the "dead" framing is a stretch. |
| 1 | Generic practice or nostalgia, no specific dead technology. |
| 0 | No Resurrection element. |

These anchors operationalise open decision E3 (whether workflows and practices count). The user may override them.

### `ai` — Technical & AI Contribution (10%)

| Score | Anchor |
|---|---|
| 5 | AI is load-bearing: it does something impractical before, its output can be checked against a measurable oracle, and the mechanism is evidenced (paper, benchmark, documented method). |
| 3 | AI is useful but replaceable by rules or heuristics at moderate loss; or there is strong non-AI technical depth. |
| 1 | AI is decorative (chat sidebar, generic summary). |
| 0 | No meaningful technical contribution. |

### `feasibility` — Implementation Feasibility (10%)

| Score | Anchor |
|---|---|
| 5 | A working core slice is achievable by a small team in ≤ 7 days with Kiro, using legally usable data, devices and APIs that are available now. |
| 3 | Feasible only with a narrowed scope, or one material risk (data access, hardware, licensing, unproven method). |
| 1 | Depends on partners, data or hardware not in hand, or on a method not shown to work. |
| 0 | Not feasible before 4 Dec 2026. |

### `demo` — Demo & Storytelling Potential (10%)

| Score | Anchor |
|---|---|
| 5 | A demo under 3 minutes shows a clear before/after on a **real** artifact, understandable to an international panel without domain knowledge. |
| 3 | The demo works but needs domain explanation or synthetic data. |
| 1 | The value is abstract or invisible on screen. |
| 0 | No demonstrable output. |

### `sustainability` — Long-term Sustainability (5%)

| Score | Anchor |
|---|---|
| 5 | Evidence that someone pays for, funds, or maintains this kind of solution (comparable paid products, active OSS communities, institutional budgets), and the legal path is clear. |
| 3 | A plausible model (OSS, B2B, institutional), not verified. |
| 1 | Depends on unlikely funding, or sits in a legal grey zone. |
| 0 | Legally blocked. |

## 4. Commercial viability (required, not weighted separately)

For each candidate, write an unscored **commercial viability note**:

- who would pay or fund it;
- evidence of comparable spending, with its label;
- the main barrier.

This satisfies the instruction "Do not assume commercial viability or user demand. Validate both."
