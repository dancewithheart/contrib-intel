# ouroboros-consensus opportunity report

## Short summary

Use the sections below differently:

1. **Issue clusters** — high-leverage fixes
2. **Issue candidates** — concrete next contribution targets
3. **Churn / test investment** — audits, refactors, property-test opportunities
4. **Topic map** — learning and exploration

Most promising current issue-cluster directions:

1. **Ledger Db** — issues #1907, #1885, #1875; files no file sample
2. **Hard Forks** — issues #1849, #1631, #1464; files no file sample
3. **Network** — issues #1852, #1711, #1590; files no file sample

Top concrete issue candidates:

- **#618** Reconsider ImmutableDB caching and iterator prefetch (subsystem: `tests`, score: 51.0) — candidate for revival: dormant but still open
- **#1753** LMDB database is put in the wrong place under some circumstances (subsystem: `ledger_db`, score: 19.0) — candidate for revival: dormant but still open
- **#1242** Assertion failure in long-range HFC ticking (subsystem: `hard_forks`, score: 19.0) — candidate for revival: dormant but still open
- **#1130** [BUG] - `NodeToClientV_16` protocol changed unexpectedly (subsystem: `network`, score: 15.0) — candidate for revival: dormant but still open
- **#299** ChainDB q-s-m model vs SUT discrepancy for GC'd `Iterator`s (subsystem: `tests`, score: 14.0) — candidate for revival: dormant but still open

## Issue clusters

### Ledger Db

- subsystem: `ledger_db`
- overall score: **286.5**
- issue count: 61
- issues:
  - [#1907 — Audit ImmDB QSM in light of PR 1872 chunkBetween bugfix](https://github.com/IntersectMBO/ouroboros-consensus/issues/1907)
  - [#1885 — Investigate segfaults in ChainDB q-s-m tests](https://github.com/IntersectMBO/ouroboros-consensus/issues/1885)
  - [#1875 — [BUG] - db-analyser --store-ledger does not store the ledger at the requested slot](https://github.com/IntersectMBO/ouroboros-consensus/issues/1875)
  - [#1870 — [BUG] - Mismatch in ChainDB.q-s-m wrt MaxSlotNo](https://github.com/IntersectMBO/ouroboros-consensus/issues/1870)
  - [#1853 — Add support for multiple snapshot intervals to SnapshotPolicy](https://github.com/IntersectMBO/ouroboros-consensus/issues/1853)
  - [#1840 — Propagate the additional-handle-for-testing idiom](https://github.com/IntersectMBO/ouroboros-consensus/issues/1840)
  - [#1782 — Refine the exported "chainDensity" metrics to use different timeframes](https://github.com/IntersectMBO/ouroboros-consensus/issues/1782)
  - [#1771 — Reconsider checkpoints during node initialization](https://github.com/IntersectMBO/ouroboros-consensus/issues/1771)
  - [#1753 — LMDB database is put in the wrong place under some circumstances](https://github.com/IntersectMBO/ouroboros-consensus/issues/1753)
  - [#1682 — Use a randomly generated security parameter in ChainDB q-s-m tests](https://github.com/IntersectMBO/ouroboros-consensus/issues/1682)

- linkage/context signals:
  - same-repo PR links: 1
  - external repo references: 0
  - maintainer hint comments: 0
  - dormant issues: 53

### Hard Forks

- subsystem: `hard_forks`
- overall score: **229.5**
- issue count: 46
- issues:
  - [#1849 — Improve TraceNoLedgerView Haddock](https://github.com/IntersectMBO/ouroboros-consensus/issues/1849)
  - [#1631 — Reorganize the documentation site](https://github.com/IntersectMBO/ouroboros-consensus/issues/1631)
  - [#1464 — Define a custom Cardano-like era with long TLL for benchmarking it](https://github.com/IntersectMBO/ouroboros-consensus/issues/1464)
  - [#1450 — Genesis test failure: restarting the mocked node is too slow](https://github.com/IntersectMBO/ouroboros-consensus/issues/1450)
  - [#1446 — Remove stale `*NodeTo*` versions](https://github.com/IntersectMBO/ouroboros-consensus/issues/1446)
  - [#1400 — Invent a mechanism to defer parsing of the block body](https://github.com/IntersectMBO/ouroboros-consensus/issues/1400)
  - [#1383 — [FEAT] - Mempool could do operations at the "ledgerstate" level to prevent projection and injection](https://github.com/IntersectMBO/ouroboros-consensus/issues/1383)
  - [#1336 — HFC: share implementation of `reconstructSummary` and `summarize`](https://github.com/IntersectMBO/ouroboros-consensus/issues/1336)
  - [#1255 — Design support for incrementally ticking the current ledger state as the wall clock advances](https://github.com/IntersectMBO/ouroboros-consensus/issues/1255)
  - [#1242 — Assertion failure in long-range HFC ticking](https://github.com/IntersectMBO/ouroboros-consensus/issues/1242)

- linkage/context signals:
  - same-repo PR links: 0
  - external repo references: 0
  - maintainer hint comments: 0
  - dormant issues: 45

### Network

- subsystem: `network`
- overall score: **164.5**
- issue count: 33
- issues:
  - [#1852 — Renaming and type chagnes in `LedgerPeersConsensusInterface`](https://github.com/IntersectMBO/ouroboros-consensus/issues/1852)
  - [#1711 — Implement Initial Barebones Downstream Server Mock (MVP)](https://github.com/IntersectMBO/ouroboros-consensus/issues/1711)
  - [#1590 — Debug Genesis a particular CSJ test failure](https://github.com/IntersectMBO/ouroboros-consensus/issues/1590)
  - [#1589 — Remove dummy codec for the obsolete `SafeBeforeEpoch` data type](https://github.com/IntersectMBO/ouroboros-consensus/issues/1589)
  - [#1508 — Provide functionality for assessing stake shift for Genesis peer snapshots](https://github.com/IntersectMBO/ouroboros-consensus/issues/1508)
  - [#1452 — CSJ: Objectors should never become Jumpers](https://github.com/IntersectMBO/ouroboros-consensus/issues/1452)
  - [#1446 — Remove stale `*NodeTo*` versions](https://github.com/IntersectMBO/ouroboros-consensus/issues/1446)
  - [#1400 — Invent a mechanism to defer parsing of the block body](https://github.com/IntersectMBO/ouroboros-consensus/issues/1400)
  - [#1301 — Simplify time conversions in Consensus](https://github.com/IntersectMBO/ouroboros-consensus/issues/1301)
  - [#1255 — Design support for incrementally ticking the current ledger state as the wall clock advances](https://github.com/IntersectMBO/ouroboros-consensus/issues/1255)

- linkage/context signals:
  - same-repo PR links: 0
  - external repo references: 0
  - maintainer hint comments: 0
  - dormant issues: 32

### Chain Sync

- subsystem: `chain_sync`
- overall score: **162.5**
- issue count: 33
- issues:
  - [#1711 — Implement Initial Barebones Downstream Server Mock (MVP)](https://github.com/IntersectMBO/ouroboros-consensus/issues/1711)
  - [#1697 — Build executable Agda spec via haskell.nix instead of the Nixpkgs haskell infra](https://github.com/IntersectMBO/ouroboros-consensus/issues/1697)
  - [#1688 — Don't use header protocol version for encoding Shelley headers](https://github.com/IntersectMBO/ouroboros-consensus/issues/1688)
  - [#1590 — Debug Genesis a particular CSJ test failure](https://github.com/IntersectMBO/ouroboros-consensus/issues/1590)
  - [#1557 — LedgerDB.V2: opportunistically reduce lock contention when closing a `Forker`](https://github.com/IntersectMBO/ouroboros-consensus/issues/1557)
  - [#1546 — Disk IO pipelining in UTxO-HD](https://github.com/IntersectMBO/ouroboros-consensus/issues/1546)
  - [#1481 — [FEAT] - Add Functionality to Query Full Block Details by Hash](https://github.com/IntersectMBO/ouroboros-consensus/issues/1481)
  - [#1452 — CSJ: Objectors should never become Jumpers](https://github.com/IntersectMBO/ouroboros-consensus/issues/1452)
  - [#1423 — Consistent naming for the Genesis/Devoted BlockFetch decision logic](https://github.com/IntersectMBO/ouroboros-consensus/issues/1423)
  - [#1375 — Add metrics for interesting Genesis events](https://github.com/IntersectMBO/ouroboros-consensus/issues/1375)

- linkage/context signals:
  - same-repo PR links: 0
  - external repo references: 0
  - maintainer hint comments: 0
  - dormant issues: 31

### Tests

- subsystem: `tests`
- overall score: **110.5**
- issue count: 23
- issues:
  - [#1907 — Audit ImmDB QSM in light of PR 1872 chunkBetween bugfix](https://github.com/IntersectMBO/ouroboros-consensus/issues/1907)
  - [#1885 — Investigate segfaults in ChainDB q-s-m tests](https://github.com/IntersectMBO/ouroboros-consensus/issues/1885)
  - [#1870 — [BUG] - Mismatch in ChainDB.q-s-m wrt MaxSlotNo](https://github.com/IntersectMBO/ouroboros-consensus/issues/1870)
  - [#1758 — Integrate the new `quickcheck-dynamic` with parallel actions](https://github.com/IntersectMBO/ouroboros-consensus/issues/1758)
  - [#1754 — Roundtrip tests for Ledger tables](https://github.com/IntersectMBO/ouroboros-consensus/issues/1754)
  - [#1682 — Use a randomly generated security parameter in ChainDB q-s-m tests](https://github.com/IntersectMBO/ouroboros-consensus/issues/1682)
  - [#1601 — Implement range reads tests](https://github.com/IntersectMBO/ouroboros-consensus/issues/1601)
  - [#1494 — Add IOSim POR support for QSM](https://github.com/IntersectMBO/ouroboros-consensus/issues/1494)
  - [#1493 — Add Parallel Tests for the DB Code](https://github.com/IntersectMBO/ouroboros-consensus/issues/1493)
  - [#1383 — [FEAT] - Mempool could do operations at the "ledgerstate" level to prevent projection and injection](https://github.com/IntersectMBO/ouroboros-consensus/issues/1383)

- linkage/context signals:
  - same-repo PR links: 0
  - external repo references: 0
  - maintainer hint comments: 0
  - dormant issues: 20

## Issue candidates

Concrete issues enriched with contribution signals.

### #618 — Reconsider ImmutableDB caching and iterator prefetch

- subsystem guess: `tests`
- local score: **51.0**
- recommendation: candidate for revival: dormant but still open
- issue url: https://github.com/IntersectMBO/ouroboros-consensus/issues/618

- contribution signals:
  - already actively worked on in same repo? no
  - same-repo PR links: 0
  - referenced by external repos? no
  - external references: 0
  - maintainer hinted direction? no
  - maintainer-hint count: 0
  - dormant days: 845

### #1753 — LMDB database is put in the wrong place under some circumstances

- subsystem guess: `ledger_db`
- local score: **19.0**
- recommendation: candidate for revival: dormant but still open
- issue url: https://github.com/IntersectMBO/ouroboros-consensus/issues/1753

- contribution signals:
  - already actively worked on in same repo? no
  - same-repo PR links: 0
  - referenced by external repos? no
  - external references: 0
  - maintainer hinted direction? no
  - maintainer-hint count: 0
  - dormant days: 137

### #1242 — Assertion failure in long-range HFC ticking

- subsystem guess: `hard_forks`
- local score: **19.0**
- recommendation: candidate for revival: dormant but still open
- issue url: https://github.com/IntersectMBO/ouroboros-consensus/issues/1242

- contribution signals:
  - already actively worked on in same repo? no
  - same-repo PR links: 0
  - referenced by external repos? no
  - external references: 0
  - maintainer hinted direction? no
  - maintainer-hint count: 0
  - dormant days: 564

### #1130 — [BUG] - `NodeToClientV_16` protocol changed unexpectedly

- subsystem guess: `network`
- local score: **15.0**
- recommendation: candidate for revival: dormant but still open
- issue url: https://github.com/IntersectMBO/ouroboros-consensus/issues/1130

- contribution signals:
  - already actively worked on in same repo? no
  - same-repo PR links: 0
  - referenced by external repos? no
  - external references: 0
  - maintainer hinted direction? no
  - maintainer-hint count: 0
  - dormant days: 657

### #299 — ChainDB q-s-m model vs SUT discrepancy for GC'd `Iterator`s

- subsystem guess: `tests`
- local score: **14.0**
- recommendation: candidate for revival: dormant but still open
- issue url: https://github.com/IntersectMBO/ouroboros-consensus/issues/299

- contribution signals:
  - already actively worked on in same repo? no
  - same-repo PR links: 0
  - referenced by external repos? no
  - external references: 0
  - maintainer hinted direction? no
  - maintainer-hint count: 0
  - dormant days: 361

### #1336 — HFC: share implementation of `reconstructSummary` and `summarize`

- subsystem guess: `hard_forks`
- local score: **12.0**
- recommendation: candidate for revival: dormant but still open
- issue url: https://github.com/IntersectMBO/ouroboros-consensus/issues/1336

- contribution signals:
  - already actively worked on in same repo? no
  - same-repo PR links: 0
  - referenced by external repos? no
  - external references: 0
  - maintainer hinted direction? no
  - maintainer-hint count: 0
  - dormant days: 440

### #623 — Use same Iterator for ChainDB as for the ImmutableDB

- subsystem guess: `ledger_db`
- local score: **12.0**
- recommendation: candidate for revival: dormant but still open
- issue url: https://github.com/IntersectMBO/ouroboros-consensus/issues/623

- contribution signals:
  - already actively worked on in same repo? no
  - same-repo PR links: 0
  - referenced by external repos? no
  - external references: 0
  - maintainer hinted direction? no
  - maintainer-hint count: 0
  - dormant days: 845

### #1339 — Re-enable the `GetLedgerDB` action in the `ChainDB` QSM tests

- subsystem guess: `ledger_db`
- local score: **11.0**
- recommendation: candidate for revival: dormant but still open
- issue url: https://github.com/IntersectMBO/ouroboros-consensus/issues/1339

- contribution signals:
  - already actively worked on in same repo? no
  - same-repo PR links: 0
  - referenced by external repos? no
  - external references: 0
  - maintainer hinted direction? no
  - maintainer-hint count: 0
  - dormant days: 475

### #868 — Decide on mitigation of missed leadership checks due to ledger snapshots

- subsystem guess: `ledger_db`
- local score: **11.0**
- recommendation: candidate for revival: dormant but still open
- issue url: https://github.com/IntersectMBO/ouroboros-consensus/issues/868

- contribution signals:
  - already actively worked on in same repo? no
  - same-repo PR links: 0
  - referenced by external repos? no
  - external references: 0
  - maintainer hinted direction? no
  - maintainer-hint count: 0
  - dormant days: 286

### #345 — [FEAT] - Generalize how the HFC handles era transitions

- subsystem guess: `hard_forks`
- local score: **11.0**
- recommendation: candidate for revival: dormant but still open
- issue url: https://github.com/IntersectMBO/ouroboros-consensus/issues/345

- contribution signals:
  - already actively worked on in same repo? no
  - same-repo PR links: 0
  - referenced by external repos? no
  - external references: 0
  - maintainer hinted direction? no
  - maintainer-hint count: 0
  - dormant days: 358

### #420 — Proposals for second iteration of the HFC

- subsystem guess: `hard_forks`
- local score: **10.0**
- recommendation: candidate for revival: dormant but still open
- issue url: https://github.com/IntersectMBO/ouroboros-consensus/issues/420

- contribution signals:
  - already actively worked on in same repo? no
  - same-repo PR links: 0
  - referenced by external repos? no
  - external references: 0
  - maintainer hinted direction? no
  - maintainer-hint count: 0
  - dormant days: 433

### #626 — Clarify relation between trivial HasHardForkHistory instance and NoHardForks

- subsystem guess: `hard_forks`
- local score: **10.0**
- recommendation: candidate for revival: dormant but still open
- issue url: https://github.com/IntersectMBO/ouroboros-consensus/issues/626

- contribution signals:
  - already actively worked on in same repo? no
  - same-repo PR links: 0
  - referenced by external repos? no
  - external references: 0
  - maintainer hinted direction? no
  - maintainer-hint count: 0
  - dormant days: 845

### #1870 — [BUG] - Mismatch in ChainDB.q-s-m wrt MaxSlotNo

- subsystem guess: `ledger_db`
- local score: **9.0**
- recommendation: inspect manually
- issue url: https://github.com/IntersectMBO/ouroboros-consensus/issues/1870

- contribution signals:
  - already actively worked on in same repo? no
  - same-repo PR links: 0
  - referenced by external repos? no
  - external references: 0
  - maintainer hinted direction? no
  - maintainer-hint count: 0
  - dormant days: 42

### #418 — Specify cross-era ticking/forecasting for Cardano

- subsystem guess: `hard_forks`
- local score: **9.0**
- recommendation: candidate for revival: dormant but still open
- issue url: https://github.com/IntersectMBO/ouroboros-consensus/issues/418

- contribution signals:
  - already actively worked on in same repo? no
  - same-repo PR links: 0
  - referenced by external repos? no
  - external references: 0
  - maintainer hinted direction? no
  - maintainer-hint count: 0
  - dormant days: 804

### #657 — Avoid header validation during block validation

- subsystem guess: `chain_sync`
- local score: **9.0**
- recommendation: candidate for revival: dormant but still open
- issue url: https://github.com/IntersectMBO/ouroboros-consensus/issues/657

- contribution signals:
  - already actively worked on in same repo? no
  - same-repo PR links: 0
  - referenced by external repos? no
  - external references: 0
  - maintainer hinted direction? no
  - maintainer-hint count: 0
  - dormant days: 845

### #1875 — [BUG] - db-analyser --store-ledger does not store the ledger at the requested slot

- subsystem guess: `ledger_db`
- local score: **8.0**
- recommendation: inspect manually
- issue url: https://github.com/IntersectMBO/ouroboros-consensus/issues/1875

- contribution signals:
  - already actively worked on in same repo? no
  - same-repo PR links: 0
  - referenced by external repos? no
  - external references: 0
  - maintainer hinted direction? no
  - maintainer-hint count: 0
  - dormant days: 26

### #1711 — Implement Initial Barebones Downstream Server Mock (MVP)

- subsystem guess: `network`
- local score: **8.0**
- recommendation: candidate for revival: dormant but still open
- issue url: https://github.com/IntersectMBO/ouroboros-consensus/issues/1711

- contribution signals:
  - already actively worked on in same repo? no
  - same-repo PR links: 0
  - referenced by external repos? no
  - external references: 0
  - maintainer hinted direction? no
  - maintainer-hint count: 0
  - dormant days: 162

### #1631 — Reorganize the documentation site

- subsystem guess: `hard_forks`
- local score: **8.0**
- recommendation: candidate for revival: dormant but still open
- issue url: https://github.com/IntersectMBO/ouroboros-consensus/issues/1631

- contribution signals:
  - already actively worked on in same repo? no
  - same-repo PR links: 0
  - referenced by external repos? no
  - external references: 0
  - maintainer hinted direction? no
  - maintainer-hint count: 0
  - dormant days: 223

### #1590 — Debug Genesis a particular CSJ test failure

- subsystem guess: `chain_sync`
- local score: **8.0**
- recommendation: candidate for revival: dormant but still open
- issue url: https://github.com/IntersectMBO/ouroboros-consensus/issues/1590

- contribution signals:
  - already actively worked on in same repo? no
  - same-repo PR links: 0
  - referenced by external repos? no
  - external references: 0
  - maintainer hinted direction? no
  - maintainer-hint count: 0
  - dormant days: 225

### #385 — Cardano SingleEraBlock instances should stop counting blocks after the nonce snapshot

- subsystem guess: `hard_forks`
- local score: **8.0**
- recommendation: candidate for revival: dormant but still open
- issue url: https://github.com/IntersectMBO/ouroboros-consensus/issues/385

- contribution signals:
  - already actively worked on in same repo? no
  - same-repo PR links: 0
  - referenced by external repos? no
  - external references: 0
  - maintainer hinted direction? no
  - maintainer-hint count: 0
  - dormant days: 902

## Churn / test investment report

Top files where tests, refactors, or smaller components may pay off:

- `ouroboros-consensus/src/Ouroboros/Consensus/Node.hs` — churn=284, bugfix_churn=20, todo_hits=0
- `ouroboros-consensus/src/Ouroboros/Consensus/Storage/ImmutableDB/Impl.hs` — churn=51, bugfix_churn=10, todo_hits=0
- `ouroboros-consensus/src/Ouroboros/Consensus/Ledger/Byron.hs` — churn=101, bugfix_churn=9, todo_hits=0
- `ouroboros-consensus/src/Ouroboros/Consensus/Storage/VolatileDB/Impl.hs` — churn=50, bugfix_churn=9, todo_hits=0
- `ouroboros-consensus/src/Ouroboros/Consensus/Storage/ChainDB/API.hs` — churn=44, bugfix_churn=9, todo_hits=0
- `ouroboros-consensus/src/Ouroboros/Consensus/Protocol/PBFT.hs` — churn=110, bugfix_churn=8, todo_hits=0
- `ouroboros-consensus/src/Ouroboros/Consensus/Storage/ChainDB/Impl/LgrDB.hs` — churn=61, bugfix_churn=7, todo_hits=0
- `ouroboros-consensus/src/Ouroboros/Storage/ChainDB/API.hs` — churn=59, bugfix_churn=7, todo_hits=0
- `ouroboros-consensus/src/Ouroboros/Consensus/HardFork/Combinator/Ledger.hs` — churn=47, bugfix_churn=7, todo_hits=0
- `ouroboros-consensus/src/Ouroboros/Consensus/Storage/ImmutableDB/Impl/Iterator.hs` — churn=40, bugfix_churn=7, todo_hits=0
- `ouroboros-consensus/src/Ouroboros/Storage/ChainDB/Impl/Reader.hs` — churn=34, bugfix_churn=7, todo_hits=0
- `ouroboros-consensus/src/Ouroboros/Storage/ChainDB/Impl/Iterator.hs` — churn=34, bugfix_churn=7, todo_hits=0
- `ouroboros-consensus/src/Ouroboros/Storage/ChainDB/Impl/ImmDB.hs` — churn=59, bugfix_churn=6, todo_hits=0
- `ouroboros-consensus/src/ouroboros-consensus/Ouroboros/Consensus/MiniProtocol/ChainSync/Client.hs` — churn=56, bugfix_churn=6, todo_hits=0
- `ouroboros-consensus/src/Ouroboros/Consensus/Storage/ChainDB/Impl/Args.hs` — churn=38, bugfix_churn=6, todo_hits=0

## Topic map

### Ledger Db

- issue count: 61
- issues:
  - [#1907 — Audit ImmDB QSM in light of PR 1872 chunkBetween bugfix](https://github.com/IntersectMBO/ouroboros-consensus/issues/1907)
  - [#1885 — Investigate segfaults in ChainDB q-s-m tests](https://github.com/IntersectMBO/ouroboros-consensus/issues/1885)
  - [#1875 — [BUG] - db-analyser --store-ledger does not store the ledger at the requested slot](https://github.com/IntersectMBO/ouroboros-consensus/issues/1875)
  - [#1870 — [BUG] - Mismatch in ChainDB.q-s-m wrt MaxSlotNo](https://github.com/IntersectMBO/ouroboros-consensus/issues/1870)
  - [#1853 — Add support for multiple snapshot intervals to SnapshotPolicy](https://github.com/IntersectMBO/ouroboros-consensus/issues/1853)
  - [#1840 — Propagate the additional-handle-for-testing idiom](https://github.com/IntersectMBO/ouroboros-consensus/issues/1840)
  - [#1782 — Refine the exported "chainDensity" metrics to use different timeframes](https://github.com/IntersectMBO/ouroboros-consensus/issues/1782)
  - [#1771 — Reconsider checkpoints during node initialization](https://github.com/IntersectMBO/ouroboros-consensus/issues/1771)
  - [#1753 — LMDB database is put in the wrong place under some circumstances](https://github.com/IntersectMBO/ouroboros-consensus/issues/1753)
  - [#1682 — Use a randomly generated security parameter in ChainDB q-s-m tests](https://github.com/IntersectMBO/ouroboros-consensus/issues/1682)


### Hard Forks

- issue count: 46
- issues:
  - [#1849 — Improve TraceNoLedgerView Haddock](https://github.com/IntersectMBO/ouroboros-consensus/issues/1849)
  - [#1631 — Reorganize the documentation site](https://github.com/IntersectMBO/ouroboros-consensus/issues/1631)
  - [#1464 — Define a custom Cardano-like era with long TLL for benchmarking it](https://github.com/IntersectMBO/ouroboros-consensus/issues/1464)
  - [#1450 — Genesis test failure: restarting the mocked node is too slow](https://github.com/IntersectMBO/ouroboros-consensus/issues/1450)
  - [#1446 — Remove stale `*NodeTo*` versions](https://github.com/IntersectMBO/ouroboros-consensus/issues/1446)
  - [#1400 — Invent a mechanism to defer parsing of the block body](https://github.com/IntersectMBO/ouroboros-consensus/issues/1400)
  - [#1383 — [FEAT] - Mempool could do operations at the "ledgerstate" level to prevent projection and injection](https://github.com/IntersectMBO/ouroboros-consensus/issues/1383)
  - [#1336 — HFC: share implementation of `reconstructSummary` and `summarize`](https://github.com/IntersectMBO/ouroboros-consensus/issues/1336)
  - [#1255 — Design support for incrementally ticking the current ledger state as the wall clock advances](https://github.com/IntersectMBO/ouroboros-consensus/issues/1255)
  - [#1242 — Assertion failure in long-range HFC ticking](https://github.com/IntersectMBO/ouroboros-consensus/issues/1242)


### Chain Sync

- issue count: 33
- issues:
  - [#1711 — Implement Initial Barebones Downstream Server Mock (MVP)](https://github.com/IntersectMBO/ouroboros-consensus/issues/1711)
  - [#1697 — Build executable Agda spec via haskell.nix instead of the Nixpkgs haskell infra](https://github.com/IntersectMBO/ouroboros-consensus/issues/1697)
  - [#1688 — Don't use header protocol version for encoding Shelley headers](https://github.com/IntersectMBO/ouroboros-consensus/issues/1688)
  - [#1590 — Debug Genesis a particular CSJ test failure](https://github.com/IntersectMBO/ouroboros-consensus/issues/1590)
  - [#1557 — LedgerDB.V2: opportunistically reduce lock contention when closing a `Forker`](https://github.com/IntersectMBO/ouroboros-consensus/issues/1557)
  - [#1546 — Disk IO pipelining in UTxO-HD](https://github.com/IntersectMBO/ouroboros-consensus/issues/1546)
  - [#1481 — [FEAT] - Add Functionality to Query Full Block Details by Hash](https://github.com/IntersectMBO/ouroboros-consensus/issues/1481)
  - [#1452 — CSJ: Objectors should never become Jumpers](https://github.com/IntersectMBO/ouroboros-consensus/issues/1452)
  - [#1423 — Consistent naming for the Genesis/Devoted BlockFetch decision logic](https://github.com/IntersectMBO/ouroboros-consensus/issues/1423)
  - [#1375 — Add metrics for interesting Genesis events](https://github.com/IntersectMBO/ouroboros-consensus/issues/1375)


### Network

- issue count: 33
- issues:
  - [#1852 — Renaming and type chagnes in `LedgerPeersConsensusInterface`](https://github.com/IntersectMBO/ouroboros-consensus/issues/1852)
  - [#1711 — Implement Initial Barebones Downstream Server Mock (MVP)](https://github.com/IntersectMBO/ouroboros-consensus/issues/1711)
  - [#1590 — Debug Genesis a particular CSJ test failure](https://github.com/IntersectMBO/ouroboros-consensus/issues/1590)
  - [#1589 — Remove dummy codec for the obsolete `SafeBeforeEpoch` data type](https://github.com/IntersectMBO/ouroboros-consensus/issues/1589)
  - [#1508 — Provide functionality for assessing stake shift for Genesis peer snapshots](https://github.com/IntersectMBO/ouroboros-consensus/issues/1508)
  - [#1452 — CSJ: Objectors should never become Jumpers](https://github.com/IntersectMBO/ouroboros-consensus/issues/1452)
  - [#1446 — Remove stale `*NodeTo*` versions](https://github.com/IntersectMBO/ouroboros-consensus/issues/1446)
  - [#1400 — Invent a mechanism to defer parsing of the block body](https://github.com/IntersectMBO/ouroboros-consensus/issues/1400)
  - [#1301 — Simplify time conversions in Consensus](https://github.com/IntersectMBO/ouroboros-consensus/issues/1301)
  - [#1255 — Design support for incrementally ticking the current ledger state as the wall clock advances](https://github.com/IntersectMBO/ouroboros-consensus/issues/1255)


### Tests

- issue count: 23
- issues:
  - [#1907 — Audit ImmDB QSM in light of PR 1872 chunkBetween bugfix](https://github.com/IntersectMBO/ouroboros-consensus/issues/1907)
  - [#1885 — Investigate segfaults in ChainDB q-s-m tests](https://github.com/IntersectMBO/ouroboros-consensus/issues/1885)
  - [#1870 — [BUG] - Mismatch in ChainDB.q-s-m wrt MaxSlotNo](https://github.com/IntersectMBO/ouroboros-consensus/issues/1870)
  - [#1758 — Integrate the new `quickcheck-dynamic` with parallel actions](https://github.com/IntersectMBO/ouroboros-consensus/issues/1758)
  - [#1754 — Roundtrip tests for Ledger tables](https://github.com/IntersectMBO/ouroboros-consensus/issues/1754)
  - [#1682 — Use a randomly generated security parameter in ChainDB q-s-m tests](https://github.com/IntersectMBO/ouroboros-consensus/issues/1682)
  - [#1601 — Implement range reads tests](https://github.com/IntersectMBO/ouroboros-consensus/issues/1601)
  - [#1494 — Add IOSim POR support for QSM](https://github.com/IntersectMBO/ouroboros-consensus/issues/1494)
  - [#1493 — Add Parallel Tests for the DB Code](https://github.com/IntersectMBO/ouroboros-consensus/issues/1493)
  - [#1383 — [FEAT] - Mempool could do operations at the "ledgerstate" level to prevent projection and injection](https://github.com/IntersectMBO/ouroboros-consensus/issues/1383)

