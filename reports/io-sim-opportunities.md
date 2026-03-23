# io-sim opportunity report

## Short summary

Use the sections below differently:

1. **Issue clusters** — high-leverage fixes
2. **Issue candidates** — concrete next contribution targets
3. **Churn / test investment** — audits, refactors, property-test opportunities
4. **Topic map** — learning and exploration

Most promising current issue-cluster directions:

1. **Por** — issues #244, #229, #227; files no file sample
2. **Traces** — issues #247, #229, #219; files no file sample
3. **Stm** — issues #219, #183, #180; files no file sample

Top concrete issue candidates:

- **#160** Minimize redundancy in IOSimPOR logs (subsystem: `exceptions`, score: 144.0) — candidate for revival: dormant but still open
- **#148** IOSimPOR propExploration failure (subsystem: `por`, score: 66.0) — candidate for revival: dormant but still open
- **#183** IOSimPOR fails to find a race under specific circumstances (subsystem: `traces`, score: 15.0) — candidate for revival: dormant but still open
- **#229** Missing `PropertyM` callbacks for `IOSimPOR` (subsystem: `por`, score: 13.0) — candidate for revival: dormant but still open
- **#180** Implement combinator that forbids descheduling (subsystem: `por`, score: 9.0) — good candidate: externally relevant

## Issue clusters

### Por

- subsystem: `por`
- overall score: **47.5**
- issue count: 10
- issues:
  - [#244 — SimEvent redesign](https://github.com/input-output-hk/io-sim/issues/244)
  - [#229 — Missing `PropertyM` callbacks for `IOSimPOR`](https://github.com/input-output-hk/io-sim/issues/229)
  - [#227 — Figure out if a thread is alive in `io-classes`](https://github.com/input-output-hk/io-sim/issues/227)
  - [#183 — IOSimPOR fails to find a race under specific circumstances](https://github.com/input-output-hk/io-sim/issues/183)
  - [#180 — Implement combinator that forbids descheduling](https://github.com/input-output-hk/io-sim/issues/180)
  - [#160 — Minimize redundancy in IOSimPOR logs](https://github.com/input-output-hk/io-sim/issues/160)
  - [#148 — IOSimPOR propExploration failure](https://github.com/input-output-hk/io-sim/issues/148)
  - [#125 — Make it possible to generate schedules](https://github.com/input-output-hk/io-sim/issues/125)
  - [#112 — Implement IORefs for both io-sim and io-sim-por](https://github.com/input-output-hk/io-sim/issues/112)
  - [#36 — Add support for nested exception testing in Test/STM](https://github.com/input-output-hk/io-sim/issues/36)

- linkage/context signals:
  - same-repo PR links: 2
  - external repo references: 2
  - maintainer hint comments: 0
  - dormant issues: 9

### Traces

- subsystem: `traces`
- overall score: **32.5**
- issue count: 6
- issues:
  - [#247 — `io-sim-1.10` compiler error when used with `io-classes-1.9`](https://github.com/input-output-hk/io-sim/issues/247)
  - [#229 — Missing `PropertyM` callbacks for `IOSimPOR`](https://github.com/input-output-hk/io-sim/issues/229)
  - [#219 — Trace information about deadlock](https://github.com/input-output-hk/io-sim/issues/219)
  - [#183 — IOSimPOR fails to find a race under specific circumstances](https://github.com/input-output-hk/io-sim/issues/183)
  - [#160 — Minimize redundancy in IOSimPOR logs](https://github.com/input-output-hk/io-sim/issues/160)
  - [#125 — Make it possible to generate schedules](https://github.com/input-output-hk/io-sim/issues/125)

- linkage/context signals:
  - same-repo PR links: 0
  - external repo references: 1
  - maintainer hint comments: 0
  - dormant issues: 5

### Stm

- subsystem: `stm`
- overall score: **27.5**
- issue count: 7
- issues:
  - [#219 — Trace information about deadlock](https://github.com/input-output-hk/io-sim/issues/219)
  - [#183 — IOSimPOR fails to find a race under specific circumstances](https://github.com/input-output-hk/io-sim/issues/183)
  - [#180 — Implement combinator that forbids descheduling](https://github.com/input-output-hk/io-sim/issues/180)
  - [#160 — Minimize redundancy in IOSimPOR logs](https://github.com/input-output-hk/io-sim/issues/160)
  - [#148 — IOSimPOR propExploration failure](https://github.com/input-output-hk/io-sim/issues/148)
  - [#137 — Write compatibility tests for `io` and `io-sim`'s stm APIs](https://github.com/input-output-hk/io-sim/issues/137)
  - [#36 — Add support for nested exception testing in Test/STM](https://github.com/input-output-hk/io-sim/issues/36)

- linkage/context signals:
  - same-repo PR links: 3
  - external repo references: 1
  - maintainer hint comments: 0
  - dormant issues: 7

### Generators

- subsystem: `generators`
- overall score: **20.5**
- issue count: 5
- issues:
  - [#248 — Test suite is missing lower bound on QuickCheck](https://github.com/input-output-hk/io-sim/issues/248)
  - [#229 — Missing `PropertyM` callbacks for `IOSimPOR`](https://github.com/input-output-hk/io-sim/issues/229)
  - [#148 — IOSimPOR propExploration failure](https://github.com/input-output-hk/io-sim/issues/148)
  - [#125 — Make it possible to generate schedules](https://github.com/input-output-hk/io-sim/issues/125)
  - [#36 — Add support for nested exception testing in Test/STM](https://github.com/input-output-hk/io-sim/issues/36)

- linkage/context signals:
  - same-repo PR links: 1
  - external repo references: 0
  - maintainer hint comments: 0
  - dormant issues: 4

### Exceptions

- subsystem: `exceptions`
- overall score: **17.5**
- issue count: 4
- issues:
  - [#183 — IOSimPOR fails to find a race under specific circumstances](https://github.com/input-output-hk/io-sim/issues/183)
  - [#160 — Minimize redundancy in IOSimPOR logs](https://github.com/input-output-hk/io-sim/issues/160)
  - [#148 — IOSimPOR propExploration failure](https://github.com/input-output-hk/io-sim/issues/148)
  - [#36 — Add support for nested exception testing in Test/STM](https://github.com/input-output-hk/io-sim/issues/36)

- linkage/context signals:
  - same-repo PR links: 1
  - external repo references: 0
  - maintainer hint comments: 0
  - dormant issues: 4

## Issue candidates

Concrete issues enriched with contribution signals.

### #160 — Minimize redundancy in IOSimPOR logs

- subsystem guess: `exceptions`
- local score: **144.0**
- recommendation: candidate for revival: dormant but still open
- issue url: https://github.com/input-output-hk/io-sim/issues/160

- contribution signals:
  - already actively worked on in same repo? no
  - same-repo PR links: 0
  - referenced by external repos? no
  - external references: 0
  - maintainer hinted direction? no
  - maintainer-hint count: 0
  - dormant days: 533

### #148 — IOSimPOR propExploration failure

- subsystem guess: `por`
- local score: **66.0**
- recommendation: candidate for revival: dormant but still open
- issue url: https://github.com/input-output-hk/io-sim/issues/148

- contribution signals:
  - already actively worked on in same repo? no
  - same-repo PR links: 0
  - referenced by external repos? no
  - external references: 0
  - maintainer hinted direction? no
  - maintainer-hint count: 0
  - dormant days: 756

### #183 — IOSimPOR fails to find a race under specific circumstances

- subsystem guess: `traces`
- local score: **15.0**
- recommendation: candidate for revival: dormant but still open
- issue url: https://github.com/input-output-hk/io-sim/issues/183

- contribution signals:
  - already actively worked on in same repo? no
  - same-repo PR links: 0
  - referenced by external repos? no
  - external references: 0
  - maintainer hinted direction? no
  - maintainer-hint count: 0
  - dormant days: 523

### #229 — Missing `PropertyM` callbacks for `IOSimPOR`

- subsystem guess: `por`
- local score: **13.0**
- recommendation: candidate for revival: dormant but still open
- issue url: https://github.com/input-output-hk/io-sim/issues/229

- contribution signals:
  - already actively worked on in same repo? no
  - same-repo PR links: 0
  - referenced by external repos? no
  - external references: 0
  - maintainer hinted direction? no
  - maintainer-hint count: 0
  - dormant days: 146

### #180 — Implement combinator that forbids descheduling

- subsystem guess: `por`
- local score: **9.0**
- recommendation: good candidate: externally relevant
- issue url: https://github.com/input-output-hk/io-sim/issues/180

- contribution signals:
  - already actively worked on in same repo? no
  - same-repo PR links: 0
  - referenced by external repos? yes
  - external references: 1
  - maintainer hinted direction? no
  - maintainer-hint count: 0
  - dormant days: 521

### #247 — `io-sim-1.10` compiler error when used with `io-classes-1.9`

- subsystem guess: `traces`
- local score: **6.0**
- recommendation: good candidate: externally relevant
- issue url: https://github.com/input-output-hk/io-sim/issues/247

- contribution signals:
  - already actively worked on in same repo? no
  - same-repo PR links: 0
  - referenced by external repos? yes
  - external references: 1
  - maintainer hinted direction? no
  - maintainer-hint count: 0
  - dormant days: 14

### #219 — Trace information about deadlock

- subsystem guess: `traces`
- local score: **6.0**
- recommendation: candidate for revival: dormant but still open
- issue url: https://github.com/input-output-hk/io-sim/issues/219

- contribution signals:
  - already actively worked on in same repo? no
  - same-repo PR links: 0
  - referenced by external repos? no
  - external references: 0
  - maintainer hinted direction? no
  - maintainer-hint count: 0
  - dormant days: 272

### #125 — Make it possible to generate schedules

- subsystem guess: `por`
- local score: **6.0**
- recommendation: candidate for revival: dormant but still open
- issue url: https://github.com/input-output-hk/io-sim/issues/125

- contribution signals:
  - already actively worked on in same repo? no
  - same-repo PR links: 0
  - referenced by external repos? no
  - external references: 0
  - maintainer hinted direction? no
  - maintainer-hint count: 0
  - dormant days: 830

### #244 — SimEvent redesign

- subsystem guess: `por`
- local score: **4.0**
- recommendation: good candidate: externally relevant
- issue url: https://github.com/input-output-hk/io-sim/issues/244

- contribution signals:
  - already actively worked on in same repo? no
  - same-repo PR links: 0
  - referenced by external repos? yes
  - external references: 1
  - maintainer hinted direction? no
  - maintainer-hint count: 0
  - dormant days: 38

### #227 — Figure out if a thread is alive in `io-classes`

- subsystem guess: `por`
- local score: **3.0**
- recommendation: candidate for revival: dormant but still open
- issue url: https://github.com/input-output-hk/io-sim/issues/227

- contribution signals:
  - already actively worked on in same repo? no
  - same-repo PR links: 0
  - referenced by external repos? no
  - external references: 0
  - maintainer hinted direction? no
  - maintainer-hint count: 0
  - dormant days: 146

### #36 — Add support for nested exception testing in Test/STM

- subsystem guess: `por`
- local score: **3.0**
- recommendation: likely already active; inspect before contributing
- issue url: https://github.com/input-output-hk/io-sim/issues/36

- contribution signals:
  - already actively worked on in same repo? yes
  - same-repo PR links: 1
  - referenced by external repos? no
  - external references: 0
  - maintainer hinted direction? no
  - maintainer-hint count: 0
  - dormant days: 533

### #248 — Test suite is missing lower bound on QuickCheck

- subsystem guess: `generators`
- local score: **2.0**
- recommendation: inspect manually
- issue url: https://github.com/input-output-hk/io-sim/issues/248

- contribution signals:
  - already actively worked on in same repo? no
  - same-repo PR links: 0
  - referenced by external repos? no
  - external references: 0
  - maintainer hinted direction? no
  - maintainer-hint count: 0
  - dormant days: 12

### #221 — Add a `PrimBase (IOSim s)` instance

- subsystem guess: `unknown`
- local score: **2.0**
- recommendation: candidate for revival: dormant but still open
- issue url: https://github.com/input-output-hk/io-sim/issues/221

- contribution signals:
  - already actively worked on in same repo? no
  - same-repo PR links: 0
  - referenced by external repos? no
  - external references: 0
  - maintainer hinted direction? no
  - maintainer-hint count: 0
  - dormant days: 257

### #122 — Add a link to the `io-sim` hackage pages in the README and/or repo description

- subsystem guess: `unknown`
- local score: **2.0**
- recommendation: candidate for revival: dormant but still open
- issue url: https://github.com/input-output-hk/io-sim/issues/122

- contribution signals:
  - already actively worked on in same repo? no
  - same-repo PR links: 0
  - referenced by external repos? no
  - external references: 0
  - maintainer hinted direction? no
  - maintainer-hint count: 0
  - dormant days: 865

### #53 — Is it possible to integrate with dejafu?

- subsystem guess: `unknown`
- local score: **2.0**
- recommendation: candidate for revival: dormant but still open
- issue url: https://github.com/input-output-hk/io-sim/issues/53

- contribution signals:
  - already actively worked on in same repo? no
  - same-repo PR links: 0
  - referenced by external repos? no
  - external references: 0
  - maintainer hinted direction? no
  - maintainer-hint count: 0
  - dormant days: 1214

### #33 — Add MonadSay instances for monad transformers

- subsystem guess: `unknown`
- local score: **2.0**
- recommendation: candidate for revival: dormant but still open
- issue url: https://github.com/input-output-hk/io-sim/issues/33

- contribution signals:
  - already actively worked on in same repo? no
  - same-repo PR links: 0
  - referenced by external repos? no
  - external references: 0
  - maintainer hinted direction? no
  - maintainer-hint count: 0
  - dormant days: 1265

### #22 — `concurrent` library as an alternative for `io-classes`

- subsystem guess: `unknown`
- local score: **2.0**
- recommendation: candidate for revival: dormant but still open
- issue url: https://github.com/input-output-hk/io-sim/issues/22

- contribution signals:
  - already actively worked on in same repo? no
  - same-repo PR links: 0
  - referenced by external repos? no
  - external references: 0
  - maintainer hinted direction? no
  - maintainer-hint count: 0
  - dormant days: 1285

### #112 — Implement IORefs for both io-sim and io-sim-por

- subsystem guess: `por`
- local score: **0.0**
- recommendation: likely already active; inspect before contributing
- issue url: https://github.com/input-output-hk/io-sim/issues/112

- contribution signals:
  - already actively worked on in same repo? yes
  - same-repo PR links: 1
  - referenced by external repos? no
  - external references: 0
  - maintainer hinted direction? no
  - maintainer-hint count: 0
  - dormant days: 941

### #137 — Write compatibility tests for `io` and `io-sim`'s stm APIs

- subsystem guess: `stm`
- local score: **-2.0**
- recommendation: likely already active; inspect before contributing
- issue url: https://github.com/input-output-hk/io-sim/issues/137

- contribution signals:
  - already actively worked on in same repo? yes
  - same-repo PR links: 2
  - referenced by external repos? no
  - external references: 0
  - maintainer hinted direction? no
  - maintainer-hint count: 0
  - dormant days: 782

### #128 — Add Chan, QSem and QSenN

- subsystem guess: `unknown`
- local score: **-2.0**
- recommendation: likely already active; inspect before contributing
- issue url: https://github.com/input-output-hk/io-sim/issues/128

- contribution signals:
  - already actively worked on in same repo? yes
  - same-repo PR links: 1
  - referenced by external repos? no
  - external references: 0
  - maintainer hinted direction? no
  - maintainer-hint count: 0
  - dormant days: 830

## Churn / test investment report

Top files where tests, refactors, or smaller components may pay off:

- `io-sim/src/Control/Monad/IOSimPOR/Internal.hs` — churn=127, bugfix_churn=15, todo_hits=0
- `io-sim/src/Control/Monad/IOSim.hs` — churn=139, bugfix_churn=14, todo_hits=0
- `io-sim/src/Control/Monad/IOSim/Internal.hs` — churn=104, bugfix_churn=8, todo_hits=0
- `io-sim/src/Control/Monad/IOSim/Types.hs` — churn=103, bugfix_churn=8, todo_hits=0
- `io-sim/test/Test/IOSim.hs` — churn=52, bugfix_churn=6, todo_hits=0
- `io-sim/src/Control/Monad/IOSim/STM.hs` — churn=25, bugfix_churn=6, todo_hits=0
- `io-sim/test/Test/Control/Monad/IOSim.hs` — churn=34, bugfix_churn=4, todo_hits=0
- `io-sim/test/Test/Control/Monad/IOSimPOR.hs` — churn=34, bugfix_churn=2, todo_hits=0
- `io-sim/test/Test/STM.hs` — churn=11, bugfix_churn=1, todo_hits=0
- `io-classes/strict-stm/Control/Concurrent/Class/MonadSTM/Strict/TMVar.hs` — churn=4, bugfix_churn=1, todo_hits=0
- `io-classes/strict-stm/Control/Concurrent/Class/MonadSTM/Strict/TVar.hs` — churn=4, bugfix_churn=1, todo_hits=0
- `io-sim/test/Test/Control/Concurrent/Class/MonadMVar.hs` — churn=4, bugfix_churn=1, todo_hits=0
- `io-sim/src/Control/Monad/IOSim/CommonTypes.hs` — churn=20, bugfix_churn=0, todo_hits=0
- `io-sim/src/Control/Monad/IOSimPOR/Types.hs` — churn=19, bugfix_churn=0, todo_hits=0
- `io-sim/src/Control/Monad/IOSim/InternalTypes.hs` — churn=13, bugfix_churn=0, todo_hits=0

## Topic map

### Por

- issue count: 10
- issues:
  - [#244 — SimEvent redesign](https://github.com/input-output-hk/io-sim/issues/244)
  - [#229 — Missing `PropertyM` callbacks for `IOSimPOR`](https://github.com/input-output-hk/io-sim/issues/229)
  - [#227 — Figure out if a thread is alive in `io-classes`](https://github.com/input-output-hk/io-sim/issues/227)
  - [#183 — IOSimPOR fails to find a race under specific circumstances](https://github.com/input-output-hk/io-sim/issues/183)
  - [#180 — Implement combinator that forbids descheduling](https://github.com/input-output-hk/io-sim/issues/180)
  - [#160 — Minimize redundancy in IOSimPOR logs](https://github.com/input-output-hk/io-sim/issues/160)
  - [#148 — IOSimPOR propExploration failure](https://github.com/input-output-hk/io-sim/issues/148)
  - [#125 — Make it possible to generate schedules](https://github.com/input-output-hk/io-sim/issues/125)
  - [#112 — Implement IORefs for both io-sim and io-sim-por](https://github.com/input-output-hk/io-sim/issues/112)
  - [#36 — Add support for nested exception testing in Test/STM](https://github.com/input-output-hk/io-sim/issues/36)


### Stm

- issue count: 7
- issues:
  - [#219 — Trace information about deadlock](https://github.com/input-output-hk/io-sim/issues/219)
  - [#183 — IOSimPOR fails to find a race under specific circumstances](https://github.com/input-output-hk/io-sim/issues/183)
  - [#180 — Implement combinator that forbids descheduling](https://github.com/input-output-hk/io-sim/issues/180)
  - [#160 — Minimize redundancy in IOSimPOR logs](https://github.com/input-output-hk/io-sim/issues/160)
  - [#148 — IOSimPOR propExploration failure](https://github.com/input-output-hk/io-sim/issues/148)
  - [#137 — Write compatibility tests for `io` and `io-sim`'s stm APIs](https://github.com/input-output-hk/io-sim/issues/137)
  - [#36 — Add support for nested exception testing in Test/STM](https://github.com/input-output-hk/io-sim/issues/36)


### Traces

- issue count: 6
- issues:
  - [#247 — `io-sim-1.10` compiler error when used with `io-classes-1.9`](https://github.com/input-output-hk/io-sim/issues/247)
  - [#229 — Missing `PropertyM` callbacks for `IOSimPOR`](https://github.com/input-output-hk/io-sim/issues/229)
  - [#219 — Trace information about deadlock](https://github.com/input-output-hk/io-sim/issues/219)
  - [#183 — IOSimPOR fails to find a race under specific circumstances](https://github.com/input-output-hk/io-sim/issues/183)
  - [#160 — Minimize redundancy in IOSimPOR logs](https://github.com/input-output-hk/io-sim/issues/160)
  - [#125 — Make it possible to generate schedules](https://github.com/input-output-hk/io-sim/issues/125)


### Generators

- issue count: 5
- issues:
  - [#248 — Test suite is missing lower bound on QuickCheck](https://github.com/input-output-hk/io-sim/issues/248)
  - [#229 — Missing `PropertyM` callbacks for `IOSimPOR`](https://github.com/input-output-hk/io-sim/issues/229)
  - [#148 — IOSimPOR propExploration failure](https://github.com/input-output-hk/io-sim/issues/148)
  - [#125 — Make it possible to generate schedules](https://github.com/input-output-hk/io-sim/issues/125)
  - [#36 — Add support for nested exception testing in Test/STM](https://github.com/input-output-hk/io-sim/issues/36)


### Exceptions

- issue count: 4
- issues:
  - [#183 — IOSimPOR fails to find a race under specific circumstances](https://github.com/input-output-hk/io-sim/issues/183)
  - [#160 — Minimize redundancy in IOSimPOR logs](https://github.com/input-output-hk/io-sim/issues/160)
  - [#148 — IOSimPOR propExploration failure](https://github.com/input-output-hk/io-sim/issues/148)
  - [#36 — Add support for nested exception testing in Test/STM](https://github.com/input-output-hk/io-sim/issues/36)

