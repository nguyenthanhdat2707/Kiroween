# Shared Research Brief — Phase 1: Independent Discovery

- Run ID: `2026-11-25-phase1-discovery`
- Run root: `/home/tdat/Documents/Learn/Infrastructure/Hackathon/Kiroqeen/kiroween-research/runs/2026-11-25-phase1-discovery/`
- Issued: 2026-11-25 (UTC+7) by the Coordinator
- Identical for Agents A, B and C. Source instructions: `prompts/phase-1-instructions.md` (verbatim).

## 1. Objective

Discover **problem spaces** and **revival opportunities** for the Kiroween 2026 hackathon, particularly the **Resurrection** category.

- Prioritize **genuine, present-day problems** over technological novelty or nostalgia.
- **Do not converge prematurely.** You are not choosing an idea to build. You are mapping problem spaces with evidence.
- **Challenge existing project assumptions** (Section 4). Do not simply extend previous ideas.
- Look for places where **AI provides genuine value** (it does something that was impractical before). Flag superficial "add a chatbot" integration as such.

## 2. Scope of exploration

Each agent independently explores:

1. Abandoned technologies, discontinued software, obsolete workflows and underserved communities.
2. **Why** each declined (technical, economic, legal, social). Separate published causes from speculation.
3. Whether the **underlying problem still exists today**, and for whom.
4. **Current alternatives** and their concrete limitations.
5. Whether a revival could give **meaningful contemporary value**, and what that value is.
6. Where AI is genuinely load-bearing versus decorative.

Depth beats breadth. Target **4–8 problem spaces**. Each needs real evidence on decline, present-day need and alternatives. Do not produce long lists of one-line ideas.

## 3. Competition facts (verified by Coordinator against the official source, 2026-11-25)

Source: <https://kiroween.devpost.com/rules> (page notes "Updated November 16, 2026"). Snapshot: `sources/kiroween-official-rules-2026-11-25.txt`. You may re-check the official page. Do not rely on third-party listings.

- **Resurrection category (official text):** "Bring your favorite dead technology back to life. Reimagine obsolete tech with today's innovations or solving tomorrow's problems." Other categories: Frankenstein, Skeleton Crew, Costume Contest.
- **Submission period:** Oct 30, 2026 09:00 PT – **Dec 4, 2026 14:00 PT** (= Dec 5, 05:00 Vietnam time). **New projects only**, built during the period. Pre-existing code or work must be disclosed.
- **The project must work:** installable and running on its intended platform. Built with **Kiro**. Public GitHub repo with an open-source license and a `/.kiro` directory at root. Demo video **under 3 minutes** on YouTube. Third-party APIs or data must be used within their terms.
- **Judging:**
  - Stage One is pass/fail for theme fit and tool use.
  - Stage Two has five criteria, each 20% (10 points): **Potential Impact** ("credible case for solving a real problem for a real audience … Would someone actually use this?"), **Technological Implementation** (use of Kiro), **Design** (complete, coherent product, not just a proof of concept), **Innovation/Idea** (differs from existing concepts), and **Presentation**.
  - There is no score for how old the technology is.
- **Practical implication (INFERENCE):** about 9 days of build time remain. A problem space is more useful if a small, working, demonstrable slice exists. Note feasibility, but **do not filter out problems solely on feasibility in Discovery**.

## 4. Existing project research — context to CHALLENGE, not to extend

Before this run, 26 research cycles were completed (see `../../progress/current-state.md`). The ledger shows **41 hypotheses generated, 31 rejected, 10 NEEDS EVIDENCE, 0 PROMISING, 0 STRONG CANDIDATE**.

Directions already explored include:

- BBS / Minitel / fax / TTY / pager
- Media: VHS "Tape Map", cassettes, floppy disks, CD-R
- Recipe box / scrapbook / story reconstruction from family media
- Library card catalogs (C20)
- AI displacement of websites and devices (DIY / Pinterest)
- Stack Overflow answer maintenance and version-fit
- Declining Q&A platforms (CodeProject, DaniWeb, Yahoo Groups)
- "Living Legacy Lab" (Web Forms behavior checks)
- "Behavioral Resurrection" (legacy software behavior as agent capabilities)

Prior assumptions you should **test, not inherit**:

- A1: The target user is individuals or families in the US/EU, with a widespread problem.
- A2: The Resurrection element must be an *obsolete technology*. (Could it be an obsolete **workflow**, **social practice** or **community structure**?)
- A3: Competitors already covering a problem disqualify it. (The user later accepted "improving one niche is enough".)
- A4: Developer-facing problems (Stack Overflow, legacy code) are a weak fit.
- A5: The repeated finding "0 PROMISING" means the search space is exhausted, rather than the evaluation criteria being too strict or mis-specified.

Rules for using prior research:

- You **may** read `../../progress/current-state.md`, `../../ideas/all-candidates.md` and `../../ideas/rejected.md` to avoid duplicating work and to know prior rejection reasons.
- If you revisit a prior direction, you must bring **new evidence or a new angle**, and say so explicitly. Re-checking a prior rejection reason with fresh evidence is valuable.
- At least **half** of your problem spaces must be ones **not** already in `ideas/all-candidates.md`.

## 5. Evidence requirements (mandatory)

### 5.1 Claim-level validation

For every substantive claim:

`Claim → Primary evidence → Independent confirmation → Reproduction or mechanism check (where applicable)`

Record which step each claim reached. Label each claim:

| Label | Meaning (Vietnamese equivalent used in project files) |
|---|---|
| **VERIFIED** | Primary source plus independent confirmation (or reproducible check) directly supports it (ĐÃ XÁC MINH) |
| **INFERENCE** | Reasoned from verified evidence, but not directly stated (SUY LUẬN) |
| **HYPOTHESIS** | Plausible and testable, not yet supported (GIẢ THUYẾT) |
| **UNKNOWN** | Evidence insufficient or conflicting (CHƯA RÕ) |

### 5.2 Reference rubric (score each criterion 0–5)

| Criterion | Weight | 5 = | 0 = |
|---|---|---|---|
| Source Authority | 20% | Primary or official source (vendor docs, standards body, archive, original author, peer-reviewed) | Anonymous or unknown |
| Technical Evidence | 20% | Concrete data, code, measurements, logs | Pure assertion |
| Mechanism Correctness | 20% | The causal or technical explanation is sound and checked | Wrong or absent mechanism |
| Context Fit | 15% | Same population, use case and conditions as the claim | Different context |
| Freshness | 10% | Current for the claim (2025–2026 for "still exists" claims; contemporaneous for history) | Stale for the claim |
| Reproducibility | 10% | Anyone can re-check it (public data, runnable, archived) | Cannot be re-checked |
| Commercial / Opinion Bias | 5% | **No** material bias (higher = less biased) | Marketing or advocacy with a stake |

**Weighted score (0–100)** = Σ (weight × score / 5).
Example: all 5s give 100; all 3s give 60.

Separate two ratings for every reference:

- **Source Reliability** (High/Medium/Low): how trustworthy the source is *in general*. This is driven mainly by Authority, Bias and Technical Evidence.
- **Reference Relevance** (High/Medium/Low): how directly this reference supports *this specific claim*. This is driven mainly by Context Fit and Mechanism.

A reliable source can be irrelevant to a claim, and a relevant anecdote can be unreliable. Record both.

### 5.3 Integrity

- **Never fabricate** URLs, titles, dates, statistics, quotes, competitors, users or interviews. If you could not open a source, say so and mark the claim UNKNOWN.
- Give the publication date where available, and always the **access date** (2026-11-25).
- Search for the **strongest competitor or alternative** and for **counterevidence** to each problem space.
- Do not turn historical adoption into present-day demand. Do not turn Reddit complaints into market size.

## 6. Deliverable

Write **only** to `agent-<x>/discovery.md` inside the run root. Write the body text **in Vietnamese** (project rule, `AGENTS.md`). Technical terms and source titles may stay in English. Use exactly these top-level headings, in this order, so the Coordinator can check the structure:

```
# Discovery Report — Agent <X>
## Metadata            (model id, effort, start/end time UTC, tools used, searches run approx., failures)
## 1. Research methodology
## 2. Discovered problem spaces          (summary table: ID | problem space | who is affected | technology/workflow | new vs revisited)
## 3. Historical context                 (per problem space)
## 4. Evidence of contemporary relevance (per problem space; claim IDs with labels)
## 5. Existing alternatives              (per problem space; strongest alternative + concrete limitation)
## 6. Potential revival opportunities    (per problem space; where AI is genuinely load-bearing vs decorative)
## 7. Counterevidence and limitations
## 8. Challenged assumptions             (your verdict on A1–A5 with evidence)
## 9. Unresolved questions
## 10. Evaluated references              (table: Ref ID | URL | title | publisher | pub date | accessed | claims supported | 7 scores | weighted | Source Reliability | Reference Relevance)
```

Name problem spaces `<X>-P1`, `<X>-P2`, … and claims `<X>-P1-C1`, … (for example `A-P2-C3`).

Do **not** rank, score for winning, or pick a final idea. Discovery only.

## 7. Isolation and conduct rules

- **Do not read** any other `agent-*` directory in this run, `../_preflight/`, or any other agent's output. Do not message other agents. This isolation is enforced only by instruction; follow it strictly.
- **Do not modify** any file outside `agent-<x>/`. That includes `progress/`, `ideas/`, `brief.md` and `prompts/`. Temporary scratch files go in `agent-<x>/scratch/`.
- Do not install packages or run code from community repositories. Do not commit or push.
- **Skills:**
  - Recommended project skills (read the `SKILL.md` files and apply their method): `../../.agents/skills/historical-technology-discovery/SKILL.md` and `../../.agents/skills/user-problem-validation/SKILL.md`.
  - BMAD skills (`bmad-deep-recon` in *run* mode, `bmad-brainstorming`) are optional, and only if they run **without waiting for user input**.
  - Do **not** use `bmad-advanced-elicitation` or `bmad-party-mode` in this phase.
  - BMAD core config (`_bmad/`) is intentionally absent. Use neutral defaults and Vietnamese output.
- **Never block on a question to the user.** If something is genuinely ambiguous and blocks progress, ask the Coordinator with `orca orchestration ask`. Otherwise make a reasonable, recorded assumption and continue.
- When finished, report completion with the path to `discovery.md`, the count of problem spaces, claims, references and failures.
