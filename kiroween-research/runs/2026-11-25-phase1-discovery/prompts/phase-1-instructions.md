# Phase 1 — Independent Discovery (verbatim user instructions)

Received: 2026-11-25 (UTC+7). Saved by the coordinator for reproducibility. Unmodified below.

---

Workspace: `/home/tdat/Documents/Learn/Infrastructure/Hackathon/Kiroqeen`

Phase 0 Preflight has passed its smoke tests. Proceed with Phase 1.

## 1. Objective

Discover promising problem spaces and revival opportunities for Kiroween, particularly the Resurrection category.

Do not prematurely converge on existing ideas, technologies, or proposed solutions. Prioritize genuine problems over technological novelty.

## 2. Preparation

- Read applicable AGENTS.md, project context, personal context, relevant skills, and existing research.
- Create `runs/<run-id>/brief.md`.
- Save the Phase 1 instructions locally for reproducibility.
- Verify competition requirements directly against official Kiroween sources.

## 3. Agent Configuration

Launch three independent research agents through Orca:

| Agent | Model | Effort |
|---|---|---|
| A | gemini-4-neon-high | High |
| B | claude-sonnet-5-5 | High |
| C | gpt-6.1-sol | High |

Use the invocation mechanisms verified during Preflight, adjusting reasoning effort as required. Record actual execution parameters and failures.

## 4. Independent Research

Give all three agents the same research objective and constraints.

Each agent must independently:

- Explore abandoned technologies, discontinued software, obsolete workflows, and underserved communities.
- Investigate why they declined and whether the underlying problems still exist.
- Identify current alternatives and their limitations.
- Examine whether revival could provide meaningful contemporary value.
- Challenge existing project assumptions rather than simply extending previous ideas.
- Identify opportunities where AI provides genuine value, not superficial integration.

Agents must not read each other's findings during Discovery.

## 5. Evidence Requirements

Evaluate references at the claim level using the established rubric:

- Source Authority: 20%
- Technical Evidence: 20%
- Mechanism Correctness: 20%
- Context Fit: 15%
- Freshness: 10%
- Reproducibility: 10%
- Commercial / Opinion Bias: 5%

Score each criterion from 0–5.

Distinguish Source Reliability from Reference Relevance.

Validation flow:

Claim → Primary evidence → Independent confirmation → Reproduction or mechanism check, where applicable.

Label substantive findings as VERIFIED, INFERENCE, HYPOTHESIS, or UNKNOWN.

Include source URLs, publication dates where available, and supporting evidence. Do not fabricate references.

## 6. Deliverables

Each agent writes exclusively to its assigned directory:

- `runs/<run-id>/agent-a/discovery.md`
- `runs/<run-id>/agent-b/discovery.md`
- `runs/<run-id>/agent-c/discovery.md`

Each report must contain:

- Research methodology
- Discovered problem spaces
- Historical context
- Evidence of contemporary relevance
- Existing alternatives
- Potential revival opportunities
- Counterevidence and limitations
- Unresolved questions
- Evaluated references

## 7. Coordinator Responsibilities

- Monitor execution and record failures.
- Verify that all three reports exist and satisfy the required structure.
- Check for instruction violations and unsupported claims.
- Record model parameters and execution metadata.
- Produce a Phase 1 completion report without merging, ranking, or selecting ideas.

Do not treat prompt-based workspace isolation as enforced security.

## 8. Exit Gate

Stop after Phase 1.

Do not initiate Deep Research, Cross Review, Synthesis, or Implementation without human approval.

Do not commit or push.

Execute Phase 1 now.
