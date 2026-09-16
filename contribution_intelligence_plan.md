# Contribution Intelligence Toolkit

## Why

The problem:
- where to spend attention
- which issues have the highest leverage
- which fixes teach me the most
- which changes unlock multiple related improvements
- which contributions fit my interests: compilers, distributed systems, FP, property testing, formal methods

---

## Core idea

Get statistics to answer:

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

---

## Working hypothesis

The best opportunities often look like:

- one dormant warning / TODO fixing multiple issues
- one unstable module behind several regressions
- one under-tested subsystem where a property test prevents future bugs
- one commented-out test that points to unfinished design work
- one hotspot file with repeated bugfix churn

---

## Long-term use cases

Ranking / classification problem:
- classify issues by subsystem / likely root cause
- rank opportunities by leverage and fit
- detect clusters and dormant design debt

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

Markdown report such as: `reports/scala3-weekly-opportunities.md`
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
