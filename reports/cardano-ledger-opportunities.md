# cardano-ledger opportunity report

## Short summary

Use the sections below differently:

1. **Issue clusters** — high-leverage fixes
2. **Issue candidates** — concrete next contribution targets
3. **Churn / test investment** — audits, refactors, property-test opportunities
4. **Topic map** — learning and exploration

Most promising current issue-cluster directions:

1. **Era Translation** — issues #5664, #5661, #5652; files `eras/byron/ledger/impl/test/mainnet-genesis.json`, `eras/alonzo/test-suite/golden/mainnet-alonzo-genesis.json`
2. **Governance** — issues #5664, #5661, #5646; files `eras/conway/impl/test/data/conway-genesis.json`, `eras/conway/impl/golden/pparams.json`
3. **Tests** — issues #5661, #5660, #5646; files no file sample

Top concrete issue candidates:

- **#4185** Ensure every predicate check is imp tested in Conway (subsystem: `era_translation`, score: 180.0) — candidate for revival: dormant but still open
- **#5199** GOVCERT constrained generator failure on CI (subsystem: `tests`, score: 38.0) — candidate for revival: dormant but still open
- **#4949** CDDLs for NTC LocalStateQuery (subsystem: `governance`, score: 36.0) — candidate for revival: dormant but still open
- **#2839** Alonzo test failure: Missing script witnesses (subsystem: `era_translation`, score: 31.0) — candidate for revival: dormant but still open
- **#2877** Cosmetic/minor issues in comments and formal specifications (subsystem: `era_translation`, score: 28.0) — candidate for revival: dormant but still open

## Issue clusters

### Era Translation

- subsystem: `era_translation`
- overall score: **776.5**
- issue count: 154
- issues:
  - [#5664 — Check if any of the pre-Conway transactions contain padded IP addresses](https://github.com/IntersectMBO/cardano-ledger/issues/5664)
  - [#5661 — Define Huddle spec for all ledger state queries](https://github.com/IntersectMBO/cardano-ledger/issues/5661)
  - [#5652 — Update Dijkstra UTXO rule to account for nested transactions](https://github.com/IntersectMBO/cardano-ledger/issues/5652)
  - [#5649 — Zapper test failure](https://github.com/IntersectMBO/cardano-ledger/issues/5649)
  - [#5646 — cardano-ledger-conway failure on CI](https://github.com/IntersectMBO/cardano-ledger/issues/5646)
  - [#5644 — `ContextError`s for  should be lazy](https://github.com/IntersectMBO/cardano-ledger/issues/5644)
  - [#5643 — Remove `NoThunks` instance for Predicate failures](https://github.com/IntersectMBO/cardano-ledger/issues/5643)
  - [#5642 — Remove state update from `UTXOS` rule completely](https://github.com/IntersectMBO/cardano-ledger/issues/5642)
  - [#5634 — Fail Plutus translation with DirectDeposit and BalanceInterval](https://github.com/IntersectMBO/cardano-ledger/issues/5634)
  - [#5633 — Fail Plutus translation with SubTransactions](https://github.com/IntersectMBO/cardano-ledger/issues/5633)

- top files:
  - `eras/byron/ledger/impl/test/mainnet-genesis.json`
  - `eras/alonzo/test-suite/golden/mainnet-alonzo-genesis.json`
  - `eras/alonzo/impl/golden/pparams-update.json`
  - `eras/babbage/impl/golden/pparams-update.json`
  - `eras/conway/impl/golden/pparams.json`

- linkage/context signals:
  - same-repo PR links: 4
  - external repo references: 0
  - maintainer hint comments: 0
  - dormant issues: 113

### Governance

- subsystem: `governance`
- overall score: **497.5**
- issue count: 76
- issues:
  - [#5664 — Check if any of the pre-Conway transactions contain padded IP addresses](https://github.com/IntersectMBO/cardano-ledger/issues/5664)
  - [#5661 — Define Huddle spec for all ledger state queries](https://github.com/IntersectMBO/cardano-ledger/issues/5661)
  - [#5646 — cardano-ledger-conway failure on CI](https://github.com/IntersectMBO/cardano-ledger/issues/5646)
  - [#5642 — Remove state update from `UTXOS` rule completely](https://github.com/IntersectMBO/cardano-ledger/issues/5642)
  - [#5631 — Failure in Conway CDDL tests](https://github.com/IntersectMBO/cardano-ledger/issues/5631)
  - [#5605 — Remove `isValid` from transaction deserialization](https://github.com/IntersectMBO/cardano-ledger/issues/5605)
  - [#5601 — Fix CantFollow conformance](https://github.com/IntersectMBO/cardano-ledger/issues/5601)
  - [#5578 — Switch `spssStake` to use `NonZero`](https://github.com/IntersectMBO/cardano-ledger/issues/5578)
  - [#5549 — Streaming Transition interface](https://github.com/IntersectMBO/cardano-ledger/issues/5549)
  - [#5511 — Add imp test to cover the case of phase 2 validation failure and invalid governance actions](https://github.com/IntersectMBO/cardano-ledger/issues/5511)

- top files:
  - `eras/conway/impl/test/data/conway-genesis.json`
  - `eras/conway/impl/golden/pparams.json`
  - `eras/dijkstra/impl/golden/pparams.json`
  - `eras/dijkstra/impl/golden/pparams-update.json`
  - `eras/conway/impl/golden/pparams-update.json`

- linkage/context signals:
  - same-repo PR links: 2
  - external repo references: 0
  - maintainer hint comments: 0
  - dormant issues: 61

### Tests

- subsystem: `tests`
- overall score: **418.5**
- issue count: 95
- issues:
  - [#5661 — Define Huddle spec for all ledger state queries](https://github.com/IntersectMBO/cardano-ledger/issues/5661)
  - [#5660 — Define result types for all ledger state queries](https://github.com/IntersectMBO/cardano-ledger/issues/5660)
  - [#5646 — cardano-ledger-conway failure on CI](https://github.com/IntersectMBO/cardano-ledger/issues/5646)
  - [#5639 — Move validation of Metadata sizes into the decoder](https://github.com/IntersectMBO/cardano-ledger/issues/5639)
  - [#5638 — Fix Int Metadata CDDL](https://github.com/IntersectMBO/cardano-ledger/issues/5638)
  - [#5637 — Optimize String length check in metadata](https://github.com/IntersectMBO/cardano-ledger/issues/5637)
  - [#5634 — Fail Plutus translation with DirectDeposit and BalanceInterval](https://github.com/IntersectMBO/cardano-ledger/issues/5634)
  - [#5633 — Fail Plutus translation with SubTransactions](https://github.com/IntersectMBO/cardano-ledger/issues/5633)
  - [#5631 — Failure in Conway CDDL tests](https://github.com/IntersectMBO/cardano-ledger/issues/5631)
  - [#5625 — Fail on new features in TxInfo translation](https://github.com/IntersectMBO/cardano-ledger/issues/5625)

- linkage/context signals:
  - same-repo PR links: 4
  - external repo references: 0
  - maintainer hint comments: 0
  - dormant issues: 74

### Utxo

- subsystem: `utxo`
- overall score: **216.5**
- issue count: 36
- issues:
  - [#5660 — Define result types for all ledger state queries](https://github.com/IntersectMBO/cardano-ledger/issues/5660)
  - [#5652 — Update Dijkstra UTXO rule to account for nested transactions](https://github.com/IntersectMBO/cardano-ledger/issues/5652)
  - [#5642 — Remove state update from `UTXOS` rule completely](https://github.com/IntersectMBO/cardano-ledger/issues/5642)
  - [#5634 — Fail Plutus translation with DirectDeposit and BalanceInterval](https://github.com/IntersectMBO/cardano-ledger/issues/5634)
  - [#5625 — Fail on new features in TxInfo translation](https://github.com/IntersectMBO/cardano-ledger/issues/5625)
  - [#5549 — Streaming Transition interface](https://github.com/IntersectMBO/cardano-ledger/issues/5549)
  - [#5533 — Change `accountBalanceIntervalTxBodyL` to accommodate multi-assets](https://github.com/IntersectMBO/cardano-ledger/issues/5533)
  - [#5500 — Add bodies to the sub-transaction rules](https://github.com/IntersectMBO/cardano-ledger/issues/5500)
  - [#5474 — Idea discussion: Allow PlutusV1-V3 with Nested Transactions](https://github.com/IntersectMBO/cardano-ledger/issues/5474)
  - [#5336 — Flip serialization of `TxIx` in MemPack](https://github.com/IntersectMBO/cardano-ledger/issues/5336)

- top files:
  - `eras/alonzo/impl/golden/pparams.json`
  - `eras/alonzo/test-suite/golden/mainnet-alonzo-genesis.json`
  - `eras/babbage/impl/golden/pparams.json`
  - `eras/byron/ledger/impl/test/mainnet-genesis.json`
  - `eras/conway/impl/golden/pparams-update.json`

- linkage/context signals:
  - same-repo PR links: 0
  - external repo references: 0
  - maintainer hint comments: 0
  - dormant issues: 27

### Serialization

- subsystem: `serialization`
- overall score: **91.5**
- issue count: 22
- issues:
  - [#5649 — Zapper test failure](https://github.com/IntersectMBO/cardano-ledger/issues/5649)
  - [#5646 — cardano-ledger-conway failure on CI](https://github.com/IntersectMBO/cardano-ledger/issues/5646)
  - [#5631 — Failure in Conway CDDL tests](https://github.com/IntersectMBO/cardano-ledger/issues/5631)
  - [#5598 — Fix the DecShareCBOR instance for StakeWithDelegations](https://github.com/IntersectMBO/cardano-ledger/issues/5598)
  - [#5588 — When possible, remove un-need allow-newer stanzas for ghc-9.14](https://github.com/IntersectMBO/cardano-ledger/issues/5588)
  - [#5549 — Streaming Transition interface](https://github.com/IntersectMBO/cardano-ledger/issues/5549)
  - [#5537 — Remove unused `FromCBOR` instances](https://github.com/IntersectMBO/cardano-ledger/issues/5537)
  - [#5513 — Indefinite length decoding support for Bytes](https://github.com/IntersectMBO/cardano-ledger/issues/5513)
  - [#5124 — Byron CDDLs are missing transaction encodings](https://github.com/IntersectMBO/cardano-ledger/issues/5124)
  - [#5026 — Upgrade hard-coded transactions in `ledger-state:bench:performance`](https://github.com/IntersectMBO/cardano-ledger/issues/5026)

- linkage/context signals:
  - same-repo PR links: 1
  - external repo references: 0
  - maintainer hint comments: 0
  - dormant issues: 14

## Issue candidates

Concrete issues enriched with contribution signals.

### #4185 — Ensure every predicate check is imp tested in Conway

- subsystem guess: `era_translation`
- local score: **180.0**
- recommendation: candidate for revival: dormant but still open
- issue url: https://github.com/IntersectMBO/cardano-ledger/issues/4185

- likely files:
  - `eras/byron/ledger/impl/test/mainnet-genesis.json`
  - `eras/alonzo/test-suite/golden/mainnet-alonzo-genesis.json`
  - `eras/alonzo/impl/golden/pparams-update.json`
  - `eras/babbage/impl/golden/pparams-update.json`
  - `eras/conway/impl/golden/pparams.json`

- contribution signals:
  - already actively worked on in same repo? no
  - same-repo PR links: 0
  - referenced by external repos? no
  - external references: 0
  - maintainer hinted direction? no
  - maintainer-hint count: 0
  - dormant days: 185

### #5199 — GOVCERT constrained generator failure on CI

- subsystem guess: `tests`
- local score: **38.0**
- recommendation: candidate for revival: dormant but still open
- issue url: https://github.com/IntersectMBO/cardano-ledger/issues/5199

- contribution signals:
  - already actively worked on in same repo? no
  - same-repo PR links: 0
  - referenced by external repos? no
  - external references: 0
  - maintainer hinted direction? no
  - maintainer-hint count: 0
  - dormant days: 203

### #4949 — CDDLs for NTC LocalStateQuery

- subsystem guess: `governance`
- local score: **36.0**
- recommendation: candidate for revival: dormant but still open
- issue url: https://github.com/IntersectMBO/cardano-ledger/issues/4949

- likely files:
  - `eras/conway/impl/test/data/conway-genesis.json`
  - `eras/conway/impl/golden/pparams.json`
  - `eras/dijkstra/impl/golden/pparams.json`
  - `eras/dijkstra/impl/golden/pparams-update.json`
  - `eras/conway/impl/golden/pparams-update.json`

- contribution signals:
  - already actively worked on in same repo? no
  - same-repo PR links: 0
  - referenced by external repos? no
  - external references: 0
  - maintainer hinted direction? no
  - maintainer-hint count: 0
  - dormant days: 364

### #2839 — Alonzo test failure: Missing script witnesses

- subsystem guess: `era_translation`
- local score: **31.0**
- recommendation: candidate for revival: dormant but still open
- issue url: https://github.com/IntersectMBO/cardano-ledger/issues/2839

- likely files:
  - `eras/byron/ledger/impl/test/mainnet-genesis.json`
  - `eras/alonzo/test-suite/golden/mainnet-alonzo-genesis.json`
  - `eras/alonzo/impl/golden/pparams-update.json`
  - `eras/babbage/impl/golden/pparams-update.json`
  - `eras/conway/impl/golden/pparams.json`

- contribution signals:
  - already actively worked on in same repo? no
  - same-repo PR links: 0
  - referenced by external repos? no
  - external references: 0
  - maintainer hinted direction? no
  - maintainer-hint count: 0
  - dormant days: 1354

### #2877 — Cosmetic/minor issues in comments and formal specifications

- subsystem guess: `era_translation`
- local score: **28.0**
- recommendation: candidate for revival: dormant but still open
- issue url: https://github.com/IntersectMBO/cardano-ledger/issues/2877

- likely files:
  - `eras/byron/ledger/impl/test/mainnet-genesis.json`
  - `eras/alonzo/test-suite/golden/mainnet-alonzo-genesis.json`
  - `eras/alonzo/impl/golden/pparams-update.json`
  - `eras/babbage/impl/golden/pparams-update.json`
  - `eras/conway/impl/golden/pparams.json`

- contribution signals:
  - already actively worked on in same repo? no
  - same-repo PR links: 0
  - referenced by external repos? no
  - external references: 0
  - maintainer hinted direction? no
  - maintainer-hint count: 0
  - dormant days: 412

### #5075 — Add CDDLs for ConwayLedgerPredFailure

- subsystem guess: `governance`
- local score: **27.0**
- recommendation: candidate for revival: dormant but still open
- issue url: https://github.com/IntersectMBO/cardano-ledger/issues/5075

- likely files:
  - `eras/conway/impl/test/data/conway-genesis.json`
  - `eras/conway/impl/golden/pparams.json`
  - `eras/dijkstra/impl/golden/pparams.json`
  - `eras/dijkstra/impl/golden/pparams-update.json`
  - `eras/conway/impl/golden/pparams-update.json`

- contribution signals:
  - already actively worked on in same repo? no
  - same-repo PR links: 0
  - referenced by external repos? no
  - external references: 0
  - maintainer hinted direction? no
  - maintainer-hint count: 0
  - dormant days: 264

### #5420 — SPO ratification takes less epochs than expected

- subsystem guess: `governance`
- local score: **26.0**
- recommendation: candidate for revival: dormant but still open
- issue url: https://github.com/IntersectMBO/cardano-ledger/issues/5420

- likely files:
  - `eras/conway/impl/test/data/conway-genesis.json`
  - `eras/conway/impl/golden/pparams.json`
  - `eras/dijkstra/impl/golden/pparams.json`
  - `eras/dijkstra/impl/golden/pparams-update.json`
  - `eras/conway/impl/golden/pparams-update.json`

- contribution signals:
  - already actively worked on in same repo? no
  - same-repo PR links: 0
  - referenced by external repos? no
  - external references: 0
  - maintainer hinted direction? no
  - maintainer-hint count: 0
  - dormant days: 126

### #5617 — Implement Forecast API

- subsystem guess: `era_translation`
- local score: **25.0**
- recommendation: likely already active; inspect before contributing
- issue url: https://github.com/IntersectMBO/cardano-ledger/issues/5617

- likely files:
  - `eras/byron/ledger/impl/test/mainnet-genesis.json`
  - `eras/alonzo/test-suite/golden/mainnet-alonzo-genesis.json`
  - `eras/alonzo/impl/golden/pparams-update.json`
  - `eras/babbage/impl/golden/pparams-update.json`
  - `eras/conway/impl/golden/pparams.json`

- contribution signals:
  - already actively worked on in same repo? yes
  - same-repo PR links: 1
  - referenced by external repos? no
  - external references: 0
  - maintainer hinted direction? no
  - maintainer-hint count: 0
  - dormant days: 12

### #2811 — Alonzo test failure

- subsystem guess: `era_translation`
- local score: **24.0**
- recommendation: candidate for revival: dormant but still open
- issue url: https://github.com/IntersectMBO/cardano-ledger/issues/2811

- likely files:
  - `eras/byron/ledger/impl/test/mainnet-genesis.json`
  - `eras/alonzo/test-suite/golden/mainnet-alonzo-genesis.json`
  - `eras/alonzo/impl/golden/pparams-update.json`
  - `eras/babbage/impl/golden/pparams-update.json`
  - `eras/conway/impl/golden/pparams.json`

- contribution signals:
  - already actively worked on in same repo? no
  - same-repo PR links: 0
  - referenced by external repos? no
  - external references: 0
  - maintainer hinted direction? no
  - maintainer-hint count: 0
  - dormant days: 1354

### #5197 — haskell-language-server reports several errors and warnings

- subsystem guess: `era_translation`
- local score: **21.0**
- recommendation: candidate for revival: dormant but still open
- issue url: https://github.com/IntersectMBO/cardano-ledger/issues/5197

- likely files:
  - `eras/byron/ledger/impl/test/mainnet-genesis.json`
  - `eras/alonzo/test-suite/golden/mainnet-alonzo-genesis.json`
  - `eras/alonzo/impl/golden/pparams-update.json`
  - `eras/babbage/impl/golden/pparams-update.json`
  - `eras/conway/impl/golden/pparams.json`

- contribution signals:
  - already actively worked on in same repo? no
  - same-repo PR links: 0
  - referenced by external repos? no
  - external references: 0
  - maintainer hinted direction? no
  - maintainer-hint count: 0
  - dormant days: 200

### #4085 — Collection of things to be cleaned up after release of Conway 

- subsystem guess: `era_translation`
- local score: **21.0**
- recommendation: candidate for revival: dormant but still open
- issue url: https://github.com/IntersectMBO/cardano-ledger/issues/4085

- likely files:
  - `eras/byron/ledger/impl/test/mainnet-genesis.json`
  - `eras/alonzo/test-suite/golden/mainnet-alonzo-genesis.json`
  - `eras/alonzo/impl/golden/pparams-update.json`
  - `eras/babbage/impl/golden/pparams-update.json`
  - `eras/conway/impl/golden/pparams.json`

- contribution signals:
  - already actively worked on in same repo? no
  - same-repo PR links: 0
  - referenced by external repos? no
  - external references: 0
  - maintainer hinted direction? no
  - maintainer-hint count: 0
  - dormant days: 206

### #3647 — Uncouple DReps from Committee Members

- subsystem guess: `governance`
- local score: **20.0**
- recommendation: candidate for revival: dormant but still open
- issue url: https://github.com/IntersectMBO/cardano-ledger/issues/3647

- likely files:
  - `eras/conway/impl/test/data/conway-genesis.json`
  - `eras/conway/impl/golden/pparams.json`
  - `eras/dijkstra/impl/golden/pparams.json`
  - `eras/dijkstra/impl/golden/pparams-update.json`
  - `eras/conway/impl/golden/pparams-update.json`

- contribution signals:
  - already actively worked on in same repo? no
  - same-repo PR links: 0
  - referenced by external repos? no
  - external references: 0
  - maintainer hinted direction? no
  - maintainer-hint count: 0
  - dormant days: 577

### #3235 — Byron era property test failure on CI

- subsystem guess: `utxo`
- local score: **20.0**
- recommendation: candidate for revival: dormant but still open
- issue url: https://github.com/IntersectMBO/cardano-ledger/issues/3235

- likely files:
  - `eras/alonzo/impl/golden/pparams.json`
  - `eras/alonzo/test-suite/golden/mainnet-alonzo-genesis.json`
  - `eras/babbage/impl/golden/pparams.json`
  - `eras/byron/ledger/impl/test/mainnet-genesis.json`
  - `eras/conway/impl/golden/pparams-update.json`

- contribution signals:
  - already actively worked on in same repo? no
  - same-repo PR links: 0
  - referenced by external repos? no
  - external references: 0
  - maintainer hinted direction? no
  - maintainer-hint count: 0
  - dormant days: 448

### #3040 — Look further at:  MissingScriptWitnessesUTXOW (fromList [])

- subsystem guess: `utxo`
- local score: **19.0**
- recommendation: candidate for revival: dormant but still open
- issue url: https://github.com/IntersectMBO/cardano-ledger/issues/3040

- likely files:
  - `eras/alonzo/impl/golden/pparams.json`
  - `eras/alonzo/test-suite/golden/mainnet-alonzo-genesis.json`
  - `eras/babbage/impl/golden/pparams.json`
  - `eras/byron/ledger/impl/test/mainnet-genesis.json`
  - `eras/conway/impl/golden/pparams-update.json`

- contribution signals:
  - already actively worked on in same repo? no
  - same-repo PR links: 0
  - referenced by external repos? no
  - external references: 0
  - maintainer hinted direction? no
  - maintainer-hint count: 0
  - dormant days: 412

### #5642 — Remove state update from `UTXOS` rule completely

- subsystem guess: `utxo`
- local score: **18.0**
- recommendation: inspect manually
- issue url: https://github.com/IntersectMBO/cardano-ledger/issues/5642

- likely files:
  - `eras/alonzo/impl/golden/pparams.json`
  - `eras/alonzo/test-suite/golden/mainnet-alonzo-genesis.json`
  - `eras/babbage/impl/golden/pparams.json`
  - `eras/byron/ledger/impl/test/mainnet-genesis.json`
  - `eras/conway/impl/golden/pparams-update.json`

- contribution signals:
  - already actively worked on in same repo? no
  - same-repo PR links: 0
  - referenced by external repos? no
  - external references: 0
  - maintainer hinted direction? no
  - maintainer-hint count: 0
  - dormant days: 8

### #5014 — Inconsistent voting stake calculation when compared to leader election

- subsystem guess: `governance`
- local score: **18.0**
- recommendation: candidate for revival: dormant but still open
- issue url: https://github.com/IntersectMBO/cardano-ledger/issues/5014

- likely files:
  - `eras/conway/impl/test/data/conway-genesis.json`
  - `eras/conway/impl/golden/pparams.json`
  - `eras/dijkstra/impl/golden/pparams.json`
  - `eras/dijkstra/impl/golden/pparams-update.json`
  - `eras/conway/impl/golden/pparams-update.json`

- contribution signals:
  - already actively worked on in same repo? no
  - same-repo PR links: 0
  - referenced by external repos? no
  - external references: 0
  - maintainer hinted direction? no
  - maintainer-hint count: 0
  - dormant days: 133

### #5541 — Introduce `BlockHeader` type class

- subsystem guess: `era_translation`
- local score: **17.0**
- recommendation: inspect manually
- issue url: https://github.com/IntersectMBO/cardano-ledger/issues/5541

- likely files:
  - `eras/byron/ledger/impl/test/mainnet-genesis.json`
  - `eras/alonzo/test-suite/golden/mainnet-alonzo-genesis.json`
  - `eras/alonzo/impl/golden/pparams-update.json`
  - `eras/babbage/impl/golden/pparams-update.json`
  - `eras/conway/impl/golden/pparams.json`

- contribution signals:
  - already actively worked on in same repo? no
  - same-repo PR links: 0
  - referenced by external repos? no
  - external references: 0
  - maintainer hinted direction? no
  - maintainer-hint count: 0
  - dormant days: 18

### #5537 — Remove unused `FromCBOR` instances

- subsystem guess: `serialization`
- local score: **17.0**
- recommendation: inspect manually
- issue url: https://github.com/IntersectMBO/cardano-ledger/issues/5537

- contribution signals:
  - already actively worked on in same repo? no
  - same-repo PR links: 0
  - referenced by external repos? no
  - external references: 0
  - maintainer hinted direction? no
  - maintainer-hint count: 0
  - dormant days: 60

### #4856 — Too many discards is now also a problem in conformance

- subsystem guess: `governance`
- local score: **17.0**
- recommendation: candidate for revival: dormant but still open
- issue url: https://github.com/IntersectMBO/cardano-ledger/issues/4856

- likely files:
  - `eras/conway/impl/test/data/conway-genesis.json`
  - `eras/conway/impl/golden/pparams.json`
  - `eras/dijkstra/impl/golden/pparams.json`
  - `eras/dijkstra/impl/golden/pparams-update.json`
  - `eras/conway/impl/golden/pparams-update.json`

- contribution signals:
  - already actively worked on in same repo? no
  - same-repo PR links: 0
  - referenced by external repos? no
  - external references: 0
  - maintainer hinted direction? no
  - maintainer-hint count: 0
  - dormant days: 203

### #5646 — cardano-ledger-conway failure on CI

- subsystem guess: `era_translation`
- local score: **16.0**
- recommendation: likely already active; inspect before contributing
- issue url: https://github.com/IntersectMBO/cardano-ledger/issues/5646

- likely files:
  - `eras/byron/ledger/impl/test/mainnet-genesis.json`
  - `eras/alonzo/test-suite/golden/mainnet-alonzo-genesis.json`
  - `eras/alonzo/impl/golden/pparams-update.json`
  - `eras/babbage/impl/golden/pparams-update.json`
  - `eras/conway/impl/golden/pparams.json`

- contribution signals:
  - already actively worked on in same repo? yes
  - same-repo PR links: 1
  - referenced by external repos? no
  - external references: 0
  - maintainer hinted direction? no
  - maintainer-hint count: 0
  - dormant days: 7

## Churn / test investment report

Top files where tests, refactors, or smaller components may pay off:

- `libs/constrained-generators/src/Constrained/Base.hs` — churn=88, bugfix_churn=29, todo_hits=0
- `eras/conway/impl/cardano-ledger-conway.cabal` — churn=302, bugfix_churn=25, todo_hits=0
- `eras/shelley/impl/testlib/Test/Cardano/Ledger/Shelley/ImpTest.hs` — churn=191, bugfix_churn=21, todo_hits=0
- `libs/cardano-ledger-test/src/Test/Cardano/Ledger/Generic/PrettyCore.hs` — churn=218, bugfix_churn=19, todo_hits=0
- `eras/alonzo/impl/src/Cardano/Ledger/Alonzo/TxInfo.hs` — churn=111, bugfix_churn=18, todo_hits=0
- `libs/cardano-ledger-core/cardano-ledger-core.cabal` — churn=222, bugfix_churn=17, todo_hits=0
- `libs/cardano-ledger-test/src/Test/Cardano/Ledger/Generic/Trace.hs` — churn=94, bugfix_churn=15, todo_hits=0
- `eras/conway/test-suite/cardano-ledger-conway-test.cabal` — churn=105, bugfix_churn=14, todo_hits=0
- `libs/cardano-ledger-core/testlib/Test/Cardano/Ledger/Core/Arbitrary.hs` — churn=100, bugfix_churn=14, todo_hits=0
- `eras/babbage/impl/src/Cardano/Ledger/Babbage/Rules/Utxow.hs` — churn=94, bugfix_churn=14, todo_hits=0
- `eras/shelley/impl/cardano-ledger-shelley.cabal` — churn=195, bugfix_churn=13, todo_hits=0
- `eras/conway/impl/src/Cardano/Ledger/Conway/Governance.hs` — churn=155, bugfix_churn=13, todo_hits=0
- `libs/cardano-ledger-test/src/Test/Cardano/Ledger/Examples/BabbageFeatures.hs` — churn=117, bugfix_churn=13, todo_hits=0
- `eras/conway/impl/testlib/Test/Cardano/Ledger/Conway/ImpTest.hs` — churn=186, bugfix_churn=12, todo_hits=0
- `eras/alonzo/impl/testlib/Test/Cardano/Ledger/Alonzo/ImpTest.hs` — churn=76, bugfix_churn=12, todo_hits=0

## Topic map

### Era Translation

- issue count: 154
- issues:
  - [#5664 — Check if any of the pre-Conway transactions contain padded IP addresses](https://github.com/IntersectMBO/cardano-ledger/issues/5664)
  - [#5661 — Define Huddle spec for all ledger state queries](https://github.com/IntersectMBO/cardano-ledger/issues/5661)
  - [#5652 — Update Dijkstra UTXO rule to account for nested transactions](https://github.com/IntersectMBO/cardano-ledger/issues/5652)
  - [#5649 — Zapper test failure](https://github.com/IntersectMBO/cardano-ledger/issues/5649)
  - [#5646 — cardano-ledger-conway failure on CI](https://github.com/IntersectMBO/cardano-ledger/issues/5646)
  - [#5644 — `ContextError`s for  should be lazy](https://github.com/IntersectMBO/cardano-ledger/issues/5644)
  - [#5643 — Remove `NoThunks` instance for Predicate failures](https://github.com/IntersectMBO/cardano-ledger/issues/5643)
  - [#5642 — Remove state update from `UTXOS` rule completely](https://github.com/IntersectMBO/cardano-ledger/issues/5642)
  - [#5634 — Fail Plutus translation with DirectDeposit and BalanceInterval](https://github.com/IntersectMBO/cardano-ledger/issues/5634)
  - [#5633 — Fail Plutus translation with SubTransactions](https://github.com/IntersectMBO/cardano-ledger/issues/5633)


- representative files:
  - `eras/byron/ledger/impl/test/mainnet-genesis.json`
  - `eras/alonzo/test-suite/golden/mainnet-alonzo-genesis.json`
  - `eras/alonzo/impl/golden/pparams-update.json`
  - `eras/babbage/impl/golden/pparams-update.json`
  - `eras/conway/impl/golden/pparams.json`

### Tests

- issue count: 95
- issues:
  - [#5661 — Define Huddle spec for all ledger state queries](https://github.com/IntersectMBO/cardano-ledger/issues/5661)
  - [#5660 — Define result types for all ledger state queries](https://github.com/IntersectMBO/cardano-ledger/issues/5660)
  - [#5646 — cardano-ledger-conway failure on CI](https://github.com/IntersectMBO/cardano-ledger/issues/5646)
  - [#5639 — Move validation of Metadata sizes into the decoder](https://github.com/IntersectMBO/cardano-ledger/issues/5639)
  - [#5638 — Fix Int Metadata CDDL](https://github.com/IntersectMBO/cardano-ledger/issues/5638)
  - [#5637 — Optimize String length check in metadata](https://github.com/IntersectMBO/cardano-ledger/issues/5637)
  - [#5634 — Fail Plutus translation with DirectDeposit and BalanceInterval](https://github.com/IntersectMBO/cardano-ledger/issues/5634)
  - [#5633 — Fail Plutus translation with SubTransactions](https://github.com/IntersectMBO/cardano-ledger/issues/5633)
  - [#5631 — Failure in Conway CDDL tests](https://github.com/IntersectMBO/cardano-ledger/issues/5631)
  - [#5625 — Fail on new features in TxInfo translation](https://github.com/IntersectMBO/cardano-ledger/issues/5625)


### Governance

- issue count: 76
- issues:
  - [#5664 — Check if any of the pre-Conway transactions contain padded IP addresses](https://github.com/IntersectMBO/cardano-ledger/issues/5664)
  - [#5661 — Define Huddle spec for all ledger state queries](https://github.com/IntersectMBO/cardano-ledger/issues/5661)
  - [#5646 — cardano-ledger-conway failure on CI](https://github.com/IntersectMBO/cardano-ledger/issues/5646)
  - [#5642 — Remove state update from `UTXOS` rule completely](https://github.com/IntersectMBO/cardano-ledger/issues/5642)
  - [#5631 — Failure in Conway CDDL tests](https://github.com/IntersectMBO/cardano-ledger/issues/5631)
  - [#5605 — Remove `isValid` from transaction deserialization](https://github.com/IntersectMBO/cardano-ledger/issues/5605)
  - [#5601 — Fix CantFollow conformance](https://github.com/IntersectMBO/cardano-ledger/issues/5601)
  - [#5578 — Switch `spssStake` to use `NonZero`](https://github.com/IntersectMBO/cardano-ledger/issues/5578)
  - [#5549 — Streaming Transition interface](https://github.com/IntersectMBO/cardano-ledger/issues/5549)
  - [#5511 — Add imp test to cover the case of phase 2 validation failure and invalid governance actions](https://github.com/IntersectMBO/cardano-ledger/issues/5511)


- representative files:
  - `eras/conway/impl/test/data/conway-genesis.json`
  - `eras/conway/impl/golden/pparams.json`
  - `eras/dijkstra/impl/golden/pparams.json`
  - `eras/dijkstra/impl/golden/pparams-update.json`
  - `eras/conway/impl/golden/pparams-update.json`

### Utxo

- issue count: 36
- issues:
  - [#5660 — Define result types for all ledger state queries](https://github.com/IntersectMBO/cardano-ledger/issues/5660)
  - [#5652 — Update Dijkstra UTXO rule to account for nested transactions](https://github.com/IntersectMBO/cardano-ledger/issues/5652)
  - [#5642 — Remove state update from `UTXOS` rule completely](https://github.com/IntersectMBO/cardano-ledger/issues/5642)
  - [#5634 — Fail Plutus translation with DirectDeposit and BalanceInterval](https://github.com/IntersectMBO/cardano-ledger/issues/5634)
  - [#5625 — Fail on new features in TxInfo translation](https://github.com/IntersectMBO/cardano-ledger/issues/5625)
  - [#5549 — Streaming Transition interface](https://github.com/IntersectMBO/cardano-ledger/issues/5549)
  - [#5533 — Change `accountBalanceIntervalTxBodyL` to accommodate multi-assets](https://github.com/IntersectMBO/cardano-ledger/issues/5533)
  - [#5500 — Add bodies to the sub-transaction rules](https://github.com/IntersectMBO/cardano-ledger/issues/5500)
  - [#5474 — Idea discussion: Allow PlutusV1-V3 with Nested Transactions](https://github.com/IntersectMBO/cardano-ledger/issues/5474)
  - [#5336 — Flip serialization of `TxIx` in MemPack](https://github.com/IntersectMBO/cardano-ledger/issues/5336)


- representative files:
  - `eras/alonzo/impl/golden/pparams.json`
  - `eras/alonzo/test-suite/golden/mainnet-alonzo-genesis.json`
  - `eras/babbage/impl/golden/pparams.json`
  - `eras/byron/ledger/impl/test/mainnet-genesis.json`
  - `eras/conway/impl/golden/pparams-update.json`

### Serialization

- issue count: 22
- issues:
  - [#5649 — Zapper test failure](https://github.com/IntersectMBO/cardano-ledger/issues/5649)
  - [#5646 — cardano-ledger-conway failure on CI](https://github.com/IntersectMBO/cardano-ledger/issues/5646)
  - [#5631 — Failure in Conway CDDL tests](https://github.com/IntersectMBO/cardano-ledger/issues/5631)
  - [#5598 — Fix the DecShareCBOR instance for StakeWithDelegations](https://github.com/IntersectMBO/cardano-ledger/issues/5598)
  - [#5588 — When possible, remove un-need allow-newer stanzas for ghc-9.14](https://github.com/IntersectMBO/cardano-ledger/issues/5588)
  - [#5549 — Streaming Transition interface](https://github.com/IntersectMBO/cardano-ledger/issues/5549)
  - [#5537 — Remove unused `FromCBOR` instances](https://github.com/IntersectMBO/cardano-ledger/issues/5537)
  - [#5513 — Indefinite length decoding support for Bytes](https://github.com/IntersectMBO/cardano-ledger/issues/5513)
  - [#5124 — Byron CDDLs are missing transaction encodings](https://github.com/IntersectMBO/cardano-ledger/issues/5124)
  - [#5026 — Upgrade hard-coded transactions in `ledger-state:bench:performance`](https://github.com/IntersectMBO/cardano-ledger/issues/5026)

