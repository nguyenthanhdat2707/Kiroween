# Mission-Driven Research — user instructions (verbatim) and decisions

Received 2026-11-26 (UTC+7). Saved by the Coordinator for reproducibility. The text below the line is the user's message, unchanged.

## Decisions recorded before launch

| Question | Answer |
|---|---|
| Relationship to the Phase 3–7 run | This mission arrived at the Phase 3 exit gate and is treated as **superseding** that run's draft Phases 4–7. Phase 3 outputs are reused as prior research. The Phase 3 gate decisions P3-1 to P3-4 were not answered. |
| Stage 1 execution mode | **Accept risk, scoped** (2026-11-26, Stage 1 only). Fresh unsandboxed workers, prompt-only isolation, integrity snapshot plus post-run audit. |

---

# Mission-Driven Research — Digital Heritage & Resurrection Platform

## 1. Human Vision

Workspace:

`/home/tdat/Documents/Learn/Infrastructure/Hackathon/Kiroqeen`

After reviewing previous research, I have refined my mission.

In an era of rapidly advancing AI and technology, valuable websites, software, research projects, and digital communities should not disappear simply because they lose users, funding, maintenance, or commercial viability.

The primary mission is to enable people to discover, understand, compare, and experience valuable digital creations from the past.

The secondary mission is to help researchers, developers, website owners, and communities preserve their work when they can no longer maintain it.

The exploration experience is the primary product value. Preservation infrastructure enables that experience.

Treat this vision as a human-defined direction, not a validated product.

## 2. Core Research Questions

How can we:

- Preserve valuable digital creations without continuously operating their original infrastructure?
- Package digital artifacts into portable, compact, independently recoverable formats?
- Allow future generations to explore and experience historical websites and applications?
- Show how the same application, technology, or digital experience evolved from the past to the present?
- Preserve meaningful functionality rather than merely screenshots?
- Keep long-term operating costs sustainable?

Do not assume that every website must be preserved or that the platform must host every artifact.

## 3. Multi-Agent Configuration

Use a specialized multi-agent architecture rather than repeating identical research three times.

| Agent | Model | Effort | Responsibility |
|---|---|---|---|
| A | gemini-4-neon-medium | Medium | Digital Heritage & Human Experience |
| B | claude-sonnet-5-5 | Medium | Business Analysis & Sustainability |
| C | gpt-6.1-sol | High | Technical Research & Architecture |

Use fresh worker sessions and verified invocation mechanisms.

Agent C may use Medium for straightforward source collection and High for complex architecture analysis if the runtime supports effort changes. Otherwise, record the actual configuration used.

Do not use Astra or Extra High.

Verify actual model availability, runtime configuration, permissions, and filesystem boundaries. Obtain approval for unresolved security risks before launching workers.

## 4. Agent A — Digital Heritage & Human Experience

Investigate how humans preserve valuable objects, knowledge, and cultural achievements in the physical world.

Research:

- Museums and exhibitions.
- Libraries and archives.
- Artifact restoration.
- Archaeology and historical reconstruction.
- Time capsules.
- Seed banks.
- Cultural heritage preservation.
- Institutional collections.

For each relevant mechanism, analyze:

1. What is preserved?
2. Why is it considered valuable?
3. Who decides what deserves preservation?
4. How is authenticity maintained?
5. How is it made accessible?
6. Which principles can transfer to digital preservation?
7. Where does the physical-world analogy break down?

Investigate digital museums, historical software collections, web history, and interactive archival experiences.

Design possible explorer experiences:

- Discovering historical websites and applications.
- Comparing past and present versions.
- Interactive historical timelines.
- Experiencing archived functionality.
- Understanding technological evolution.
- Discovering discontinued research tools.
- Exploring cultural and historical digital artifacts.

Distinguish authentic historical captures from AI-generated reconstructions.

Identify concrete explorer personas, motivations, and user journeys. Investigate whether these experiences create genuine educational, research, or cultural value.

Deliver three distinct explorer experience concepts with supporting evidence and counterarguments.

## 5. Agent B — Business Analysis & Sustainability

Investigate the demand, stakeholders, operating economics, governance, and sustainability of the proposed mission.

Distinguish two stakeholder groups:

- Primary audience: people exploring historical digital creations.
- Contributors and beneficiaries: researchers, developers, communities, and website owners preserving their work.

Investigate actual cases involving:

- Websites abandoned because of declining usage.
- Research applications abandoned after grants end.
- Small online communities shutting down.
- Discontinued software.
- Digital heritage collections with limited resources.

Study existing preservation institutions and their funding models.

Analyze:

- Who benefits?
- Who contributes artifacts?
- Who pays?
- Who is responsible for maintenance?
- Why would someone use this platform instead of existing archives?
- How can the platform remain sustainable without hosting everything?
- What content deserves preservation?
- How should copyright, privacy, consent, and cultural restrictions be handled?

Compare nonprofit, community-supported, institutional, freemium, and bring-your-own-storage models.

Investigate international relevance using evidence from multiple geographic regions.

Do not assume willingness to pay, contribution behavior, or educational demand.

Deliver a stakeholder map, operating model alternatives, cost drivers, adoption barriers, and concrete validation experiments.

## 6. Agent C — Technical Research & Architecture

Investigate technically feasible mechanisms for low-cost, portable, recoverable digital preservation.

Research existing formats and technologies:

- WARC and WACZ.
- Webrecorder and ReplayWeb.page.
- Static website conversion.
- Content-addressable storage.
- Compression and deduplication.
- Browser-based replay.
- WebAssembly.
- Software emulation.
- Dependency and runtime packaging.
- Software Heritage.
- Object storage and cold storage.
- Distributed and user-controlled storage.
- On-demand execution.

Study the following architectural alternatives:

1. Archive-only preservation.
2. Static snapshot preservation.
3. Client-side replay.
4. Portable executable artifacts.
5. On-demand isolated runtime.
6. Federated artifact discovery without centralized hosting.
7. Hybrid approaches combining these mechanisms.

Distinguish between capturing:

- Appearance.
- Content.
- Data.
- Interactions.
- Executable functionality.
- Original runtime environments.

Investigate what cannot be recovered when only a public website is available.

Do not assume a ZIP archive can preserve backend functionality.

Analyze security risks associated with executing or replaying untrusted historical software and web content.

Develop three architecture alternatives with:

- Component diagrams.
- Data flows.
- Preservation and recovery workflows.
- Storage requirements.
- Operational cost estimates with explicit assumptions.
- Failure scenarios.
- Technical limitations.
- Existing open-source components that can be reused.
- Potential AI contributions.
- MVP feasibility.

Compare storage and compute costs against continuously hosting the original applications. Include capture, retrieval, indexing, metadata, replication, maintenance, and AI inference costs.

Do not reinvent existing formats without demonstrating an actual gap.

## 7. Required Seed References

Investigate and evaluate these sources rather than blindly accepting them:

- Webrecorder WACZ specification.
  https://specs.webrecorder.net/wacz/latest/

- Digital Preservation Coalition Handbook.
  https://www.dpconline.org/handbook/organisational-activities/preservation-action

- Managing 100 Digital Humanities Projects, James Smithies et al., 2019.
  https://kclpure.kcl.ac.uk/portal/en/publications/managing-100-digital-humanities-projects-digital-scholarship-amp-/

- Software Heritage.
  https://www.softwareheritage.org/

- Official Kiroween rules.
  https://kiroween.devpost.com/rules

Find independent confirmation, competing approaches, expert criticism, and documented failures.

## 8. Evidence Requirements

Reuse the existing claim-level reference rubric:

- Source Authority: 20%.
- Technical Evidence: 20%.
- Mechanism Correctness: 20%.
- Context Fit: 15%.
- Freshness: 10%.
- Reproducibility: 10%.
- Commercial / Opinion Bias: 5%.

Score each criterion from 0–5.

Distinguish Source Reliability from Reference Relevance.

Use:

Claim → Primary evidence → Independent confirmation → Reproduction or mechanism check, where applicable.

Preserve counterevidence and uncertainty.

Do not treat search snippets as verified evidence.

## 9. Execution Workflow

### Stage 1 — Specialized Research

Each agent researches its assigned domain independently.

Reuse relevant existing research instead of repeating previous discovery.

Provide only the context necessary for each responsibility.

### Stage 2 — Cross-Domain Review

Each agent reviews the other two reports.

Focus on conflicts between:

- User experience and technical limitations.
- Preservation value and operational economics.
- Accessibility and cultural or legal restrictions.
- Historical authenticity and AI reconstruction.
- Product ambition and hackathon feasibility.

Each agent must propose ways to resolve identified conflicts, not merely criticize.

### Stage 3 — Product Convergence

The Coordinator synthesizes the three domains into a maximum of three concrete product concepts.

Each concept must include:

- Primary target user.
- Contributor workflow.
- Explorer workflow.
- Core preservation mechanism.
- Past-versus-present experience.
- Existing alternatives.
- Differentiation.
- Meaningful AI contribution.
- Sustainability model.
- International applicability.
- Resurrection theme fit.
- Technical architecture.
- MVP scope.
- Explicitly excluded features.
- Critical assumptions and validation experiments.

Apply the established candidate-selection rubric.

Recommend a preferred concept if supported by evidence, but preserve alternatives and explain trade-offs.

Do not restart another broad discovery cycle.

## 10. AI Engineering Learning Objectives

Document:

- Why specialization was chosen over identical parallel research.
- Context selection and handoffs.
- Cross-domain dependencies.
- Agent disagreements.
- Model and effort decisions.
- Cached and uncached token usage where available.
- Execution time.
- Runtime security limitations.
- Whether specialized research reduces duplication.
- Whether cross-review produces meaningful improvements.

Do not attribute improvements to specialization or model changes without sufficient evidence.

## 11. Deliverables

Persist workflow instructions and outputs locally.

Reuse existing skills and output contracts.

Suggested artifacts:

- `agent-a/heritage-and-experience.md`
- `agent-b/business-and-sustainability.md`
- `agent-c/technical-architecture.md`
- `cross-review/`
- `coordinator/product-concepts.md`
- `coordinator/architecture-tradeoffs.md`
- `coordinator/execution-log.md`
- `human/product-decision-brief.md`

Use the existing better-writing skill for the Vietnamese human-readable decision brief.

Preserve original evidence and link to detailed artifacts instead of duplicating them.

Update progress according to AGENTS.md.

## 12. Exit Criteria

This research cycle must converge toward actionable product concepts.

The final brief must allow me to understand:

- What we could build.
- Who would use it.
- Why it matters.
- How it works.
- How it differs from existing solutions.
- How it avoids excessive operating costs.
- What can realistically be demonstrated during the hackathon.

Stop at the human decision gate.

Do not implement, commit, or push.
