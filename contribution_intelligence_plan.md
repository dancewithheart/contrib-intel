# Contribution Intelligence Toolkit

## Why this matters

My bottleneck is no longer "can I write a PR?". With strong AI support, the harder and more valuable problem is:

- where to spend attention
- which issues have the highest leverage
- which fixes teach me the most
- which changes unlock multiple related improvements
- which contributions fit my interests: compilers, distributed systems, FP, property testing, formal methods

This suggests a shift:

**from PR production**  
**to contribution selection and portfolio design**

That is higher leverage and more aligned with long-term growth.

---

## Core idea

Build a small personal toolkit that helps answer:

1. **What should I work on next in this codebase?**
2. **Which issues are probably symptoms of one deeper cause?**
3. **Where are there dormant diagnostics, commented-out tests, TODOs, or partial fixes?**
4. **Which subsystems are under-tested or bug-prone?**
5. **Which candidate changes maximize:**
   - impact
   - learning
   - acceptance probability
   - usefulness to the ecosystem
   - personal joy

This is not mainly "AI writes code".

It is:

**AI-assisted contribution intelligence**

---

## Working hypothesis

A strong contributor advantage comes from **problem selection**, not only coding speed.

The best opportunities often look like:

- one dormant warning / TODO fixing multiple issues
- one unstable module behind several regressions
- one under-tested subsystem where a property test prevents future bugs
- one commented-out test that points to unfinished design work
- one hotspot file with repeated bugfix churn

My Scala 3 `MatchTypeNoCases` PR is an example of this pattern.

---

## Long-term use cases

This toolkit could help me:

- contribute more strategically to open source
- build a focused portfolio across ecosystems I care about
- act as a short-term consultant improving codebases quickly
- learn data science / ML on a real problem
- use AI in a way that is evidence-based and useful
- train by contributing to real systems instead of toy projects

This also resembles a ranking / classification problem:

- classify issues by subsystem / likely root cause
- rank opportunities by leverage and fit
- detect clusters and dormant design debt

---

## Design principles

### 1. Start from real repositories I already touch
Not a generic platform first. Start from concrete work:

- Scala 3 compiler
- Cardano / Hydra / io-sim / Plutus / other Haskell codebases
- Agda compiler / stdlib / Cubical
- ZIO / zio-prelude

### 2. Tight loop
Avoid a giant dashboard-first project.

Loop:

1. collect data
2. generate candidate opportunities
3. manually inspect top few
4. choose one
5. ship a PR
6. record whether the recommendation was good
7. improve scripts

### 3. Evidence first
Every suggestion should be backed by something concrete:

- issue links
- commit history
- files touched by bug fixes
- TODO / FIXME / commented tests
- stack traces / symbols / labels / maintainers
- coverage gaps or missing tests

### 4. Personal goals matter
The toolkit should not optimize for "any merged PR".
It should optimize for:

- high leverage
- learning value
- relevance to my interests
- likely acceptance
- opportunity to add good tests / property tests

---

## What the toolkit should eventually analyze

### A. Issue map
Pull issues and PRs and extract:

- labels
- authors / maintainers
- milestone / state
- issue text
- referenced files / symbols
- linked PRs / commits
- stack traces / error messages
- subsystem keywords

Goal:

- cluster issues
- find repeated patterns
- identify dormant but real problems

### B. Code signals
Search repository for:

- `TODO`, `FIXME`, `XXX`, `HACK`
- commented-out warnings
- commented-out tests
- ignored / pending tests
- temporary code paths
- suspicious phrases like:
  - `should not happen`
  - `TODO warn ?`
  - `temporarily`
  - `work around`
  - `unsound`
  - `re-enable test`

Goal:

- detect unfinished work and likely leverage points

### C. Git / history signals
Mine git history for:

- files with high churn
- files often touched by bugfix commits
- revert-heavy files
- files mentioned often in issue-linked PRs
- files repeatedly patched by maintainers

Goal:

- locate unstable or important subsystems

### D. Test signals
Inspect:

- missing property tests
- low coverage
- comment-disabled tests
- flaky tests
- many snapshot tests but few semantic tests
- regression tests without deeper invariants

Goal:

- identify places where testing investment has high value

### E. Personal fit signals
Score opportunities by:

- compiler / type system relevance
- property-testing potential
- distributed systems relevance
- FP abstraction relevance
- whether the subsystem seems educational and joyful

---

## Candidate scoring dimensions

For each opportunity, estimate:

- **Leverage**: likely one root cause affects multiple issues
- **Learning value**: teaches an important subsystem
- **Test value**: chance to add strong regression / property tests
- **Acceptance probability**: small enough, aligned enough, reviewable
- **Dormancy signal**: real problem, not currently actively owned
- **Maintainer signal**: prior discussion hints at desired direction
- **Blast radius**: impactful but not too broad
- **Personal joy**: do I actually want to understand this area?

Simple scoring is enough at first. No fancy ML needed.

---

## Output format

Use simple, inspectable outputs first.

### 1. Raw data
Store as JSON / CSV / Markdown tables.

Examples:

- `issues.json`
- `prs.json`
- `todo_hits.csv`
- `bugfix_file_churn.csv`
- `candidate_opportunities.json`

### 2. Human-readable summary
Generate a Markdown report such as:

`reports/scala3-weekly-opportunities.md`

For each candidate:

```md
## Candidate: Match type diagnostics around TypeComparer / Namer

Score:
- leverage: high
- learning: high
- acceptance: medium-high
- testing: high

Evidence:
- issues: #24753, #23822, #12974
- files: `TypeComparer.scala`, `messages.scala`
- signals:
  - dormant warning path
  - commented code
  - related ignored history

Suggested next step:
- inspect higher-level reporting around `Namer.inferredResultType`
- try to separate primary typing from diagnostic-only normalization
```

### 3. Personal contribution queue
A short ranked list:

```md
# Next targets for me

1. Scala 3 explicit-nulls diagnostic cluster
2. Scala 3 match type redundant warning follow-up
3. Hydra issue with high user impact + small code surface
4. Agda stdlib issue with property-testable fix
```

This should be short and revisitable.

---

## Tech stack

### Initial stack
- **Python** for analysis, ranking, data wrangling
- **bash** for repo cloning, grep, git commands, lightweight automation
- **jq** optionally for JSON shaping
- **sqlite** later if needed

### Why Python
Because it has:

- great data tooling (`pandas`)
- easy scripting
- good text / JSON handling
- notebook support if needed
- ML libraries later if useful
- embeddings / LLM tooling if I want semantic clustering later

---

## Suggested project structure

```text
contrib-intel/
  README.md
  repos/
    scala3/
    hydra/
  scripts/
    fetch_github_issues.py
    scan_todos.sh
    mine_git_history.sh
    rank_candidates.py
    build_report.py
  data/
    scala3/
      issues.json
      prs.json
      todo_hits.csv
      churn.csv
      candidates.json
  reports/
    scala3-opportunities.md
  notes/
    lessons-learned.md
```

---

## How to improve the toolkit over time

### Phase 1: heuristic and transparent
Use grep + git log + issue metadata + simple ranking.

This is the right start.

### Phase 2: semantic grouping
Add embeddings / clustering for:

- issue text
- stack traces
- error messages
- file / symbol mentions

This helps discover hidden clusters.

### Phase 3: feedback loop
Track which recommendations led to:

- accepted PRs
- deep learning
- abandoned exploration
- maintainer engagement

Then tune scoring based on real outcomes.

### Phase 4: cross-project patterns
Look across repos for recurring opportunity classes:

- dormant diagnostics
- ignored tests
- warning/error layering problems
- property-test opportunities
- bug-prone high-churn modules

This could become reusable beyond one repo.

---

## What not to do

- do not build a giant generic platform first
- do not optimize for "most issues closed" only
- do not let analysis replace actual shipping
- do not hide logic inside opaque AI output
- do not trust heuristics without checking top recommendations manually

The toolkit should support judgment, not replace it.

---

## Quick iterations for Scala 3

## Iteration 1 — very small, very practical
Goal: generate a ranked shortlist of promising Scala 3 compiler targets.

### Inputs
- GitHub issues and PRs for `scala/scala3`
- grep results for:
  - `TODO`
  - `FIXME`
  - `TODO warn`
  - commented-out tests
  - `should not happen`
- git history summary for compiler files

### Scripts
- `fetch_github_issues.py`
- `scan_todos.sh`
- `mine_git_history.sh`
- `rank_candidates.py`

### Output
A Markdown report with top 10 candidate opportunities.

### What to rank by
- issue cluster size
- dormant code signal
- bugfix churn in same file
- test signal
- personal-interest keywords: `match type`, `Typer`, `Namer`, `explicit nulls`, `diagnostic`, `TASTy`

### Success criterion
The report identifies at least 3 candidates that look better than random issue browsing.

---

## Iteration 2 — issue cluster + subsystem map
Goal: understand Scala 3 compiler by subsystems while also finding targets.

### Extend iteration 1 by adding
- keyword/subsystem tagging:
  - typer
  - namer
  - type comparer
  - match types
  - explicit nulls
  - positions
  - semanticdb
  - diagnostics
- map issues to likely files via text matching and linked PRs
- identify clusters where:
  - multiple issues mention same file or same error wording
  - related tests are ignored / commented / flaky

### Output
A report like:

```md
# Scala 3 subsystem opportunity map

## Match types / diagnostics
- issue count: X
- key files: `TypeComparer.scala`, `messages.scala`, `ErrorReporting.scala`
- opportunities:
  1. redundant warning layering after `MatchTypeNoCases`
  2. no-case match type reporting in inference paths

## Explicit nulls
- issue count: Y
- key files: ...
- opportunities: ...
```

### Success criterion
I can pick the next target from a subsystem map instead of from the raw issue list.

---

## Possible consultant angle

This toolkit could also support short consulting-style engagements.

Example offer:

- analyze issue tracker + code history + tests
- identify leverage points
- propose ranked maintenance plan
- implement 1-2 fixes + targeted tests
- leave behind scripts and a roadmap

This is appealing because it is:

- practical
- measurable
- useful even in a short engagement
- aligned with AI-assisted software maintenance

---

## Why this may also be a good learning path

This project would teach me, in a real and useful setting:

- data wrangling
- ranking / classification thinking
- text clustering
- mining software repositories
- practical ML use
- effective AI-human collaboration
- codebase archaeology
- strategic contribution planning

That is better than learning data science on toy datasets.

---

## First concrete next steps

1. Create a small repo for the toolkit.
2. Implement iteration 1 for Scala 3 only.
3. Keep outputs simple: JSON + CSV + Markdown report.
4. Use the report to pick the next Scala 3 target.
5. After one more successful PR, refine scoring based on what actually worked.

---

## Final conclusion

This is worth doing.

Not as a generic "AI writes PRs" system.

But as a **personal contribution intelligence toolkit** that helps me:

- choose better problems
- learn faster
- contribute more strategically
- build a useful and joyful long-term path across compilers, FP, testing, and distributed systems

That feels like the right direction.

