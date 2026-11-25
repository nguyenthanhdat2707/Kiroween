# Task B — user instructions (verbatim) and decisions

Received 2026-11-25 (UTC+7). Saved by the Coordinator for reproducibility.

## Decisions recorded before launch

| Question | Answer |
|---|---|
| Execution mode | **Accept risk again, scoped.** Unsandboxed workers, prompt-only isolation, post-run audit. A bubblewrap boundary was tested in scratch and shown to be feasible: writes outside the agent folder were blocked, peer folders were hidden, web access and the Orca socket worked. The user declined to build it for this run. |

---

# Task B — Digital Preservation & Platform Continuity

## 1. Project Context

Workspace:

`/home/tdat/Documents/Learn/Infrastructure/Hackathon/Kiroqeen`

Phase 1, Phase 1.5, and Phase 2 Candidate Evaluation are complete.

Preserve the existing research results:

- B-P1: Cloud-dependent device resurrection.
- A-P4: Web content preservation and link rot.
- The unresolved third position.

Treat Task B as a separate exploratory research track. Do not let previous rankings constrain new discoveries.

## 2. Research Mission

Investigate opportunities to preserve the valuable content, knowledge, functionality, workflows, and communities of digital platforms that disappear due to:

- Declining user adoption.
- Commercial failure.
- Unsustainable operating costs.
- Discontinued maintenance.
- Vendor shutdown.
- Technological obsolescence.

The central question is:

Can we preserve the value created by digital platforms even when the original platforms can no longer survive?

Treat this mission as a human-proposed hypothesis, not a validated problem or predetermined product.

Challenge its assumptions.

## 3. Agent Configuration

Launch three independent research agents:

| Agent | Model | Reasoning Effort |
|---|---|---|
| A | gemini-4-neon-medium | Medium |
| B | claude-sonnet-5-5 | Medium |
| C | gpt-6.1-sol | Medium |

Use the invocation mechanisms verified during Preflight.

- Use fresh worker sessions.
- Verify actual runtime parameters.
- Do not use Astra or extra-high reasoning effort.
- Escalate to High only for specific unresolved problems where additional reasoning is justified.
- Record escalation reasons, token usage, execution time, and observable outcomes.

Verify runtime security and filesystem boundaries before launching workers. Report unresolved risks and obtain approval if the required isolation cannot be established.

## 4. Research Approach — Business Analysis First

Do not immediately design an application.

Investigate the following dimensions.

### 4.1. Problem and root causes

- Why do valuable digital platforms disappear?
- Is declining adoption the cause or a symptom?
- What distinguishes commercially unsuccessful platforms from genuinely obsolete platforms?
- Which losses create meaningful harm?
- When is preservation unnecessary or economically unjustified?

### 4.2. Stakeholders and demand

Identify concrete stakeholders:

- Individual users.
- Online communities.
- Researchers and educators.
- Cultural institutions.
- Software developers.
- Platform operators.
- Organizations responsible for digital heritage.

Investigate their actual problems, existing behavior, willingness to contribute, and willingness to pay.

Distinguish demonstrated demand from hypothetical demand.

### 4.3. Preservation dimensions

Explore these dimensions independently:

- Content preservation.
- Knowledge preservation.
- Software functionality.
- User data and workflows.
- Community continuity.
- Cultural and historical heritage.
- Operational continuity.

Determine which dimensions create the greatest value and which are technically and economically realistic.

### 4.4. Existing solutions

Investigate existing approaches, including:

- Internet Archive and web archiving.
- Software preservation and emulation.
- Data portability and migration.
- Open-source alternatives.
- Self-hosting.
- Decentralized storage.
- Community-led platform revival.
- Digital heritage preservation systems.

Identify their strengths, limitations, adoption barriers, and unresolved problems.

Do not claim a market gap without examining credible existing alternatives.

### 4.5. Sustainability

Investigate:

- Who benefits?
- Who pays?
- Who maintains the preserved assets?
- What are the ongoing infrastructure costs?
- Can preservation remain viable without continuous commercial growth?
- Could community, nonprofit, institutional, or commercial models work?

Do not assume that every discontinued platform deserves to survive.

### 4.6. AI contribution

Investigate where AI could provide genuine, measurable value.

Compare AI-enabled approaches against conventional engineering alternatives.

Reject unnecessary AI integration.

### 4.7. Legal and ethical constraints

Investigate copyright, licensing, privacy, ownership, consent, data protection, and preservation rights.

Distinguish publicly accessible content from content that can legally be copied or redistributed.

## 5. International Orientation

Prioritize problems with international relevance.

Investigate evidence from North America, Europe, Asia, and other relevant regions.

Explore disappearing online communities, digital heritage, endangered cultural knowledge, and abandoned software across different societies.

Cultural opportunities are encouraged when they address a transferable global problem.

A local cultural example may serve as the initial use case, but its broader applicability must be demonstrated.

Do not assume international judges will prefer or reject particular cultures.

Evaluate:

- Cross-cultural applicability.
- International demand.
- Accessibility.
- Adoption barriers.
- Ability to communicate the problem clearly to an international audience.

## 6. Research Methodology

Use appropriate Business Analysis methods:

- Stakeholder analysis.
- Root-cause analysis.
- Problem trees.
- Jobs to Be Done.
- Alternative analysis.
- Sustainability analysis.
- Hypothesis validation.

Select methods according to the problem. Do not mechanically apply every framework.

## 7. Evidence Requirements

Reuse the existing claim-level reference rubric:

| Criterion | Weight |
|---|---|
| Source Authority | 20% |
| Technical Evidence | 20% |
| Mechanism Correctness | 20% |
| Context Fit | 15% |
| Freshness | 10% |
| Reproducibility | 10% |
| Commercial / Opinion Bias | 5% |

Score each criterion from 0–5.

Distinguish Source Reliability from Reference Relevance.

Use the validation flow:

Claim → Primary evidence → Independent confirmation → Reproduction or mechanism check, where applicable.

Prioritize:

- Peer-reviewed research.
- Official documentation and datasets.
- Domain experts and engineering blogs.
- Documented case studies.
- Direct user evidence.
- Independent technical analysis.

Label claims as VERIFIED, INFERENCE, HYPOTHESIS, or UNKNOWN.

Do not treat search snippets as verified evidence.

Preserve counterevidence and conflicting findings.

## 8. Execution Workflow

### Round 1 — Independent Discovery

All three agents investigate independently.

Do not allow agents to read each other's findings during this round.

Explore different problem spaces without prematurely selecting a product.

### Round 2 — Cross-review

Allow agents to inspect each other's completed reports.

Challenge:

- Unsupported claims.
- Assumed user demand.
- Existing alternatives that were overlooked.
- Weak differentiation.
- Unsustainable preservation models.
- Unnecessary AI integration.
- Legal and operational assumptions.

Escalate reasoning effort only where justified.

### Round 3 — Synthesis

The Coordinator identifies promising opportunity spaces, overlaps, disagreements, and unresolved hypotheses.

Do not force consensus.

Do not rank Task B opportunities against the existing Phase 2 candidates yet.

## 9. Candidate Evaluation Framework

For promising opportunities, collect evidence relevant to the established candidate-selection rubric:

| Criterion | Weight |
|---|---|
| Real Problem & User Demand | 20% |
| International Relevance | 15% |
| Innovation & Differentiation | 15% |
| Resurrection Theme Fit | 15% |
| Technical & AI Contribution | 10% |
| Implementation Feasibility | 10% |
| Demo & Storytelling Potential | 10% |
| Long-term Sustainability | 5% |

Keep this rubric separate from the reference-quality rubric.

Verify official Kiroween requirements against primary sources.

Do not confuse candidate potential with predicted judging scores.

## 10. Deliverables

Save instructions and results locally.

Reuse existing workspace conventions, skills, and output contracts.

Produce:

- Independent research reports.
- Cross-review reports.
- Problem analysis.
- Stakeholder analysis.
- Existing alternatives and gap analysis.
- Opportunity map.
- Hypothesis and validation plan.
- Engineering execution log.
- Human-readable decision brief.

Use the existing better-writing skill where applicable.

The decision brief should take approximately 5–10 minutes to read and link directly to original evidence.

Avoid duplicating research content unnecessarily.

## 11. AI Engineering Learning Objectives

This project is also a hands-on AI Engineering experiment, not merely a hackathon submission.

Observe and document:

- Context selection and context handoffs.
- Agent orchestration.
- Research independence.
- Agent specialization.
- Runtime security and filesystem isolation.
- Evaluator disagreements.
- Evidence validation.
- Token consumption and execution time.
- Reasoning effort escalation.
- Whether cross-review changes research conclusions.

Distinguish measured results from assumptions.

Do not bypass meaningful engineering problems merely to finish faster.

Do not add new skills, frameworks, or architectural components unless an actual capability gap is identified.

## 12. Exit Gate

Stop after completing Task B.

Return artifact paths and a concise summary of:

- Promising opportunity spaces.
- Strongest supporting evidence.
- Strongest counterevidence.
- Unvalidated assumptions.
- Recommended validation experiments.
- AI Engineering lessons.
- Decisions requiring human approval.

Do not select the final hackathon idea.

Do not begin implementation, commit, or push.
