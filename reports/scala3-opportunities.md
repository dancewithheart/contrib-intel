# scala3 opportunity report

## Short summary

Use the sections below differently:

1. **Issue clusters** — high-leverage fixes
2. **Issue candidates** — concrete next contribution targets
3. **Churn / test investment** — audits, refactors, property-test opportunities
4. **Topic map** — learning and exploration

Most promising current issue-cluster directions:

1. **Explicit Nulls** — issues #25565, #25551, #25271; files `tests/run/bridges.scala`, `compiler/src/dotty/tools/dotc/typer/Nullables.scala`
2. **Typer** — issues #25565, #25557, #25555; files `compiler/src/dotty/tools/dotc/typer/Typer.scala`, `compiler/src/dotty/tools/dotc/core/Definitions.scala`
3. **Match Types** — issues #25341, #25246, #25129; files `compiler/src/dotty/tools/dotc/core/Types.scala`, `compiler/src/dotty/tools/dotc/semanticdb/generated/Type.scala`

Top concrete issue candidates:

- **#24776** Crash in experimental macro annotation adding a definition to ClassDef (subsystem: `typer`, score: 324.0) — inspect manually
- **#25204** no owner from  <none>/ <none> in emb.apply (subsystem: `typer`, score: 265.0) — inspect manually
- **#24719** Assertion failure in `LazyAnnotation.tree` (subsystem: `typer`, score: 245.0) — inspect manually
- **#24824** Crash during type inference after failed implicit search: assertion failed: `wildApprox` failed to remove uninstantiated T (subsystem: `typer`, score: 207.0) — inspect manually
- **#25447** Presentation compiler issues with Scala JS (subsystem: `typer`, score: 194.0) — inspect manually

## Issue clusters

### Explicit Nulls

- subsystem: `explicit_nulls`
- overall score: **10251.0**
- issue count: 15
- issues:
  - [#25565 — Regression for deriviation of enums/union types in `taig/mapping`](https://github.com/scala/scala3/issues/25565)
  - [#25551 — Repl returns null when using io.StdIn.readLine()](https://github.com/scala/scala3/issues/25551)
  - [#25271 — Runtime errors when implementing non-sealed java interface](https://github.com/scala/scala3/issues/25271)
  - [#25239 — False `Unreachable case except for null` warning in `inline def` with a match expression with type params](https://github.com/scala/scala3/issues/25239)
  - [#25183 — Compiler crash using `private var` constructor parameter and user-defined setter for field of the same name](https://github.com/scala/scala3/issues/25183)
  - [#25163 — Using value before definition results in null without warning](https://github.com/scala/scala3/issues/25163)
  - [#25162 — Null not removed when using .nn on a opaque type union with Null](https://github.com/scala/scala3/issues/25162)
  - [#24979 — "Unreachable case except for null" with `Free` and wildcard type](https://github.com/scala/scala3/issues/24979)
  - [#24899 — Unsound path-dependent types without initialization checking](https://github.com/scala/scala3/issues/24899)
  - [#24770 — Cannot assign nullable type parameter to generic types from Java under explicit nulls](https://github.com/scala/scala3/issues/24770)

- top files:
  - `tests/run/bridges.scala`
  - `compiler/src/dotty/tools/dotc/typer/Nullables.scala`
  - `compiler/src/dotty/tools/dotc/core/Types.scala`
  - `compiler/src/dotty/tools/dotc/typer/Typer.scala`
  - `compiler/src/dotty/tools/dotc/core/ImplicitNullInterop.scala`

- linkage/context signals:
  - same-repo PR links: 0
  - external repo references: 0
  - maintainer hint comments: 0
  - dormant issues: 0

### Typer

- subsystem: `typer`
- overall score: **9837.5**
- issue count: 36
- issues:
  - [#25565 — Regression for deriviation of enums/union types in `taig/mapping`](https://github.com/scala/scala3/issues/25565)
  - [#25557 — Path dependent type broken in secondary param list when args are reordered](https://github.com/scala/scala3/issues/25557)
  - [#25555 — Coverage instrumentation widens singleton types during argument lifting, causing Ycheck failure](https://github.com/scala/scala3/issues/25555)
  - [#25541 — `-Xcheck-macros` regression in `upickle` dependent projects](https://github.com/scala/scala3/issues/25541)
  - [#25534 — Typer regression in `atnos-org/eff`](https://github.com/scala/scala3/issues/25534)
  - [#25504 — Figure out the exact semantics of `apply` in edge cases](https://github.com/scala/scala3/issues/25504)
  - [#25493 — Member/extension defs as patterns](https://github.com/scala/scala3/issues/25493)
  - [#25491 — CC retyper infers Nothing from intersection with singleton type](https://github.com/scala/scala3/issues/25491)
  - [#25447 — Presentation compiler issues with Scala JS](https://github.com/scala/scala3/issues/25447)
  - [#25408 — Dotty allows compiling `scala.Int` but crashes during bytecode generation](https://github.com/scala/scala3/issues/25408)

- top files:
  - `compiler/src/dotty/tools/dotc/typer/Typer.scala`
  - `compiler/src/dotty/tools/dotc/core/Definitions.scala`
  - `compiler/test/dotty/tools/dotc/transform/LazyValsTest.scala`
  - `compiler/src/dotty/tools/dotc/core/Types.scala`
  - `compiler/src/dotty/tools/dotc/core/Contexts.scala`

- linkage/context signals:
  - same-repo PR links: 1
  - external repo references: 0
  - maintainer hint comments: 0
  - dormant issues: 0

- notes:
  - compiler/test/dotty/tools/dotc/transform/LazyValsTest.scala:7 mentions FIXME
  - compiler/test/dotty/tools/dotc/transform/LazyValsTest.scala:7 mentions re-enable

### Match Types

- subsystem: `match_types`
- overall score: **8973.0**
- issue count: 7
- issues:
  - [#25341 — Should `ConstFold` use `TypeComparer.constValue`?](https://github.com/scala/scala3/issues/25341)
  - [#25246 — Crash: `AssertionError` in `TypeOps.dominators` with complex context bounds and quoted expression](https://github.com/scala/scala3/issues/25246)
  - [#25129 — Matches and match types forget bound of extracted type variable](https://github.com/scala/scala3/issues/25129)
  - [#24836 — strictEquality doesn't work with GADTs](https://github.com/scala/scala3/issues/24836)
  - [#24760 — Overriding with an inline method and inline match is unsound](https://github.com/scala/scala3/issues/24760)
  - [#24548 — Inconsistent match type case legality](https://github.com/scala/scala3/issues/24548)
  - [#24512 — missing `scala.collection.generic.IsSeq` instance for `scala.IArray`](https://github.com/scala/scala3/issues/24512)

- top files:
  - `compiler/src/dotty/tools/dotc/core/Types.scala`
  - `compiler/src/dotty/tools/dotc/semanticdb/generated/Type.scala`
  - `compiler/src/dotty/tools/dotc/core/TypeComparer.scala`
  - `compiler/src/dotty/tools/dotc/typer/Typer.scala`
  - `compiler/src/dotty/tools/dotc/core/MatchTypeTrace.scala`

- linkage/context signals:
  - same-repo PR links: 0
  - external repo references: 0
  - maintainer hint comments: 0
  - dormant issues: 0

### Diagnostics

- subsystem: `diagnostics`
- overall score: **2911.0**
- issue count: 48
- issues:
  - [#25594 — Extension method overload resolution picks wrong candidate when lambda parameter type must be inferred](https://github.com/scala/scala3/issues/25594)
  - [#25590 — Inference of boundary/break style control abstractions broken unless via direct method reference](https://github.com/scala/scala3/issues/25590)
  - [#25585 — -Ysafe-init-global test warns pos/LazyList.scala](https://github.com/scala/scala3/issues/25585)
  - [#25571 — "-Werror" with "-Wunused:nowarn" does not work](https://github.com/scala/scala3/issues/25571)
  - [#25553 — Unable to suppress discarded non-unit warning](https://github.com/scala/scala3/issues/25553)
  - [#25544 — `@unchecked` tuple destructuring is now ignored](https://github.com/scala/scala3/issues/25544)
  - [#25534 — Typer regression in `atnos-org/eff`](https://github.com/scala/scala3/issues/25534)
  - [#25508 — REPL still prints LazyVal warnings (presumably because of fansi+pprint)](https://github.com/scala/scala3/issues/25508)
  - [#25493 — Member/extension defs as patterns](https://github.com/scala/scala3/issues/25493)
  - [#25465 — Capture checking breaks the REPL/scala-cli `:type` command](https://github.com/scala/scala3/issues/25465)

- top files:
  - `compiler/src/dotty/tools/dotc/transform/init/Objects.scala`
  - `compiler/test/dotty/tools/dotc/config/ScalaSettingsTests.scala`
  - `compiler/test/dotty/tools/vulpix/ParallelTesting.scala`
  - `compiler/src/dotty/tools/dotc/reporting/Reporter.scala`
  - `compiler/src/dotty/tools/dotc/config/ScalaSettings.scala`

- linkage/context signals:
  - same-repo PR links: 3
  - external repo references: 0
  - maintainer hint comments: 0
  - dormant issues: 0

### Namer

- subsystem: `namer`
- overall score: **2014.0**
- issue count: 3
- issues:
  - [#25447 — Presentation compiler issues with Scala JS](https://github.com/scala/scala3/issues/25447)
  - [#25244 — Crash in `tpd.singleton` on `PreviousErrorType` during error recovery (inline match + quoted pattern with unresolved import)](https://github.com/scala/scala3/issues/25244)
  - [#24719 — Assertion failure in `LazyAnnotation.tree`](https://github.com/scala/scala3/issues/24719)

- top files:
  - `tests/run/t8199.scala`
  - `compiler/src/dotty/tools/dotc/core/tasty/TastyPrinter.scala`
  - `compiler/src/dotty/tools/dotc/core/tasty/NameBuffer.scala`
  - `compiler/src/dotty/tools/dotc/core/unpickleScala2/Scala2Unpickler.scala`
  - `compiler/src/dotty/tools/dotc/typer/Namer.scala`

- linkage/context signals:
  - same-repo PR links: 0
  - external repo references: 0
  - maintainer hint comments: 0
  - dormant issues: 0

## Issue candidates

Concrete issues enriched with contribution signals.

### #24776 — Crash in experimental macro annotation adding a definition to ClassDef

- subsystem guess: `typer`
- local score: **324.0**
- recommendation: inspect manually
- issue url: https://github.com/scala/scala3/issues/24776

- likely files:
  - `compiler/src/dotty/tools/dotc/typer/Typer.scala`
  - `compiler/src/dotty/tools/dotc/core/Definitions.scala`
  - `compiler/test/dotty/tools/dotc/transform/LazyValsTest.scala`
  - `compiler/src/dotty/tools/dotc/core/Types.scala`
  - `compiler/src/dotty/tools/dotc/core/Contexts.scala`

- contribution signals:
  - already actively worked on in same repo? no
  - same-repo PR links: 0
  - referenced by external repos? no
  - external references: 0
  - maintainer hinted direction? no
  - maintainer-hint count: 0
  - dormant days: 94

### #25204 — no owner from  <none>/ <none> in emb.apply

- subsystem guess: `typer`
- local score: **265.0**
- recommendation: inspect manually
- issue url: https://github.com/scala/scala3/issues/25204

- likely files:
  - `compiler/src/dotty/tools/dotc/typer/Typer.scala`
  - `compiler/src/dotty/tools/dotc/core/Definitions.scala`
  - `compiler/test/dotty/tools/dotc/transform/LazyValsTest.scala`
  - `compiler/src/dotty/tools/dotc/core/Types.scala`
  - `compiler/src/dotty/tools/dotc/core/Contexts.scala`

- contribution signals:
  - already actively worked on in same repo? no
  - same-repo PR links: 0
  - referenced by external repos? no
  - external references: 0
  - maintainer hinted direction? no
  - maintainer-hint count: 0
  - dormant days: 35

### #24719 — Assertion failure in `LazyAnnotation.tree`

- subsystem guess: `typer`
- local score: **245.0**
- recommendation: inspect manually
- issue url: https://github.com/scala/scala3/issues/24719

- likely files:
  - `compiler/src/dotty/tools/dotc/typer/Typer.scala`
  - `compiler/src/dotty/tools/dotc/core/Definitions.scala`
  - `compiler/test/dotty/tools/dotc/transform/LazyValsTest.scala`
  - `compiler/src/dotty/tools/dotc/core/Types.scala`
  - `compiler/src/dotty/tools/dotc/core/Contexts.scala`

- contribution signals:
  - already actively worked on in same repo? no
  - same-repo PR links: 0
  - referenced by external repos? no
  - external references: 0
  - maintainer hinted direction? no
  - maintainer-hint count: 0
  - dormant days: 103

### #24824 — Crash during type inference after failed implicit search: assertion failed: `wildApprox` failed to remove uninstantiated T

- subsystem guess: `typer`
- local score: **207.0**
- recommendation: inspect manually
- issue url: https://github.com/scala/scala3/issues/24824

- likely files:
  - `compiler/src/dotty/tools/dotc/typer/Typer.scala`
  - `compiler/src/dotty/tools/dotc/core/Definitions.scala`
  - `compiler/test/dotty/tools/dotc/transform/LazyValsTest.scala`
  - `compiler/src/dotty/tools/dotc/core/Types.scala`
  - `compiler/src/dotty/tools/dotc/core/Contexts.scala`

- contribution signals:
  - already actively worked on in same repo? no
  - same-repo PR links: 0
  - referenced by external repos? no
  - external references: 0
  - maintainer hinted direction? no
  - maintainer-hint count: 0
  - dormant days: 69

### #25447 — Presentation compiler issues with Scala JS

- subsystem guess: `typer`
- local score: **194.0**
- recommendation: inspect manually
- issue url: https://github.com/scala/scala3/issues/25447

- likely files:
  - `compiler/src/dotty/tools/dotc/typer/Typer.scala`
  - `compiler/src/dotty/tools/dotc/core/Definitions.scala`
  - `compiler/test/dotty/tools/dotc/transform/LazyValsTest.scala`
  - `compiler/src/dotty/tools/dotc/core/Types.scala`
  - `compiler/src/dotty/tools/dotc/core/Contexts.scala`

- contribution signals:
  - already actively worked on in same repo? no
  - same-repo PR links: 0
  - referenced by external repos? no
  - external references: 0
  - maintainer hinted direction? no
  - maintainer-hint count: 0
  - dormant days: 17

### #25244 — Crash in `tpd.singleton` on `PreviousErrorType` during error recovery (inline match + quoted pattern with unresolved import)

- subsystem guess: `typer`
- local score: **138.0**
- recommendation: inspect manually
- issue url: https://github.com/scala/scala3/issues/25244

- likely files:
  - `compiler/src/dotty/tools/dotc/typer/Typer.scala`
  - `compiler/src/dotty/tools/dotc/core/Definitions.scala`
  - `compiler/test/dotty/tools/dotc/transform/LazyValsTest.scala`
  - `compiler/src/dotty/tools/dotc/core/Types.scala`
  - `compiler/src/dotty/tools/dotc/core/Contexts.scala`

- contribution signals:
  - already actively worked on in same repo? no
  - same-repo PR links: 0
  - referenced by external repos? no
  - external references: 0
  - maintainer hinted direction? no
  - maintainer-hint count: 0
  - dormant days: 33

### #25246 — Crash: `AssertionError` in `TypeOps.dominators` with complex context bounds and quoted expression

- subsystem guess: `typer`
- local score: **34.0**
- recommendation: inspect manually
- issue url: https://github.com/scala/scala3/issues/25246

- likely files:
  - `compiler/src/dotty/tools/dotc/typer/Typer.scala`
  - `compiler/src/dotty/tools/dotc/core/Definitions.scala`
  - `compiler/test/dotty/tools/dotc/transform/LazyValsTest.scala`
  - `compiler/src/dotty/tools/dotc/core/Types.scala`
  - `compiler/src/dotty/tools/dotc/core/Contexts.scala`

- contribution signals:
  - already actively worked on in same repo? no
  - same-repo PR links: 0
  - referenced by external repos? no
  - external references: 0
  - maintainer hinted direction? no
  - maintainer-hint count: 0
  - dormant days: 39

### #25170 — Internal error when using `-Ysafe-init-global` with basic ZIO

- subsystem guess: `typer`
- local score: **14.0**
- recommendation: inspect manually
- issue url: https://github.com/scala/scala3/issues/25170

- likely files:
  - `compiler/src/dotty/tools/dotc/typer/Typer.scala`
  - `compiler/src/dotty/tools/dotc/core/Definitions.scala`
  - `compiler/test/dotty/tools/dotc/transform/LazyValsTest.scala`
  - `compiler/src/dotty/tools/dotc/core/Types.scala`
  - `compiler/src/dotty/tools/dotc/core/Contexts.scala`

- contribution signals:
  - already actively worked on in same repo? no
  - same-repo PR links: 0
  - referenced by external repos? no
  - external references: 0
  - maintainer hinted direction? no
  - maintainer-hint count: 0
  - dormant days: 47

### #24770 — Cannot assign nullable type parameter to generic types from Java under explicit nulls

- subsystem guess: `explicit_nulls`
- local score: **13.0**
- recommendation: inspect manually
- issue url: https://github.com/scala/scala3/issues/24770

- likely files:
  - `tests/run/bridges.scala`
  - `compiler/src/dotty/tools/dotc/typer/Nullables.scala`
  - `compiler/src/dotty/tools/dotc/core/Types.scala`
  - `compiler/src/dotty/tools/dotc/typer/Typer.scala`
  - `compiler/src/dotty/tools/dotc/core/ImplicitNullInterop.scala`

- contribution signals:
  - already actively worked on in same repo? no
  - same-repo PR links: 0
  - referenced by external repos? no
  - external references: 0
  - maintainer hinted direction? no
  - maintainer-hint count: 0
  - dormant days: 94

### #24596 — Runtime regression in `getkyo/kyo` due to changes in Quotes API semantics

- subsystem guess: `typer`
- local score: **12.0**
- recommendation: inspect manually
- issue url: https://github.com/scala/scala3/issues/24596

- likely files:
  - `compiler/src/dotty/tools/dotc/typer/Typer.scala`
  - `compiler/src/dotty/tools/dotc/core/Definitions.scala`
  - `compiler/test/dotty/tools/dotc/transform/LazyValsTest.scala`
  - `compiler/src/dotty/tools/dotc/core/Types.scala`
  - `compiler/src/dotty/tools/dotc/core/Contexts.scala`

- contribution signals:
  - already actively worked on in same repo? no
  - same-repo PR links: 0
  - referenced by external repos? no
  - external references: 0
  - maintainer hinted direction? no
  - maintainer-hint count: 0
  - dormant days: 56

### #25162 — Null not removed when using .nn on a opaque type union with Null

- subsystem guess: `explicit_nulls`
- local score: **10.0**
- recommendation: inspect manually
- issue url: https://github.com/scala/scala3/issues/25162

- likely files:
  - `tests/run/bridges.scala`
  - `compiler/src/dotty/tools/dotc/typer/Nullables.scala`
  - `compiler/src/dotty/tools/dotc/core/Types.scala`
  - `compiler/src/dotty/tools/dotc/typer/Typer.scala`
  - `compiler/src/dotty/tools/dotc/core/ImplicitNullInterop.scala`

- contribution signals:
  - already actively worked on in same repo? no
  - same-repo PR links: 0
  - referenced by external repos? no
  - external references: 0
  - maintainer hinted direction? no
  - maintainer-hint count: 0
  - dormant days: 39

### #25555 — Coverage instrumentation widens singleton types during argument lifting, causing Ycheck failure

- subsystem guess: `typer`
- local score: **9.0**
- recommendation: likely already active; inspect before contributing
- issue url: https://github.com/scala/scala3/issues/25555

- likely files:
  - `compiler/src/dotty/tools/dotc/typer/Typer.scala`
  - `compiler/src/dotty/tools/dotc/core/Definitions.scala`
  - `compiler/test/dotty/tools/dotc/transform/LazyValsTest.scala`
  - `compiler/src/dotty/tools/dotc/core/Types.scala`
  - `compiler/src/dotty/tools/dotc/core/Contexts.scala`

- contribution signals:
  - already actively worked on in same repo? yes
  - same-repo PR links: 1
  - referenced by external repos? no
  - external references: 0
  - maintainer hinted direction? no
  - maintainer-hint count: 0
  - dormant days: 5

### #25055 — REPL has syntax warning crosstalk

- subsystem guess: `diagnostics`
- local score: **8.0**
- recommendation: inspect manually
- issue url: https://github.com/scala/scala3/issues/25055

- likely files:
  - `compiler/src/dotty/tools/dotc/transform/init/Objects.scala`
  - `compiler/test/dotty/tools/dotc/config/ScalaSettingsTests.scala`
  - `compiler/test/dotty/tools/vulpix/ParallelTesting.scala`
  - `compiler/src/dotty/tools/dotc/reporting/Reporter.scala`
  - `compiler/src/dotty/tools/dotc/config/ScalaSettings.scala`

- contribution signals:
  - already actively worked on in same repo? no
  - same-repo PR links: 0
  - referenced by external repos? no
  - external references: 0
  - maintainer hinted direction? no
  - maintainer-hint count: 0
  - dormant days: 60

### #24771 — -Wconf:src source path conversion to URI breaks Windows paths

- subsystem guess: `diagnostics`
- local score: **8.0**
- recommendation: inspect manually
- issue url: https://github.com/scala/scala3/issues/24771

- likely files:
  - `compiler/src/dotty/tools/dotc/transform/init/Objects.scala`
  - `compiler/test/dotty/tools/dotc/config/ScalaSettingsTests.scala`
  - `compiler/test/dotty/tools/vulpix/ParallelTesting.scala`
  - `compiler/src/dotty/tools/dotc/reporting/Reporter.scala`
  - `compiler/src/dotty/tools/dotc/config/ScalaSettings.scala`

- contribution signals:
  - already actively worked on in same repo? no
  - same-repo PR links: 0
  - referenced by external repos? no
  - external references: 0
  - maintainer hinted direction? no
  - maintainer-hint count: 0
  - dormant days: 95

### #24653 — Aliased Unit improperly boxed

- subsystem guess: `diagnostics`
- local score: **8.0**
- recommendation: inspect manually
- issue url: https://github.com/scala/scala3/issues/24653

- likely files:
  - `compiler/src/dotty/tools/dotc/transform/init/Objects.scala`
  - `compiler/test/dotty/tools/dotc/config/ScalaSettingsTests.scala`
  - `compiler/test/dotty/tools/vulpix/ParallelTesting.scala`
  - `compiler/src/dotty/tools/dotc/reporting/Reporter.scala`
  - `compiler/src/dotty/tools/dotc/config/ScalaSettings.scala`

- contribution signals:
  - already actively worked on in same repo? no
  - same-repo PR links: 0
  - referenced by external repos? no
  - external references: 0
  - maintainer hinted direction? no
  - maintainer-hint count: 0
  - dormant days: 109

### #25508 — REPL still prints LazyVal warnings (presumably because of fansi+pprint)

- subsystem guess: `diagnostics`
- local score: **7.0**
- recommendation: inspect manually
- issue url: https://github.com/scala/scala3/issues/25508

- likely files:
  - `compiler/src/dotty/tools/dotc/transform/init/Objects.scala`
  - `compiler/test/dotty/tools/dotc/config/ScalaSettingsTests.scala`
  - `compiler/test/dotty/tools/vulpix/ParallelTesting.scala`
  - `compiler/src/dotty/tools/dotc/reporting/Reporter.scala`
  - `compiler/src/dotty/tools/dotc/config/ScalaSettings.scala`

- contribution signals:
  - already actively worked on in same repo? no
  - same-repo PR links: 0
  - referenced by external repos? no
  - external references: 0
  - maintainer hinted direction? no
  - maintainer-hint count: 0
  - dormant days: 4

### #24760 — Overriding with an inline method and inline match is unsound

- subsystem guess: `match_types`
- local score: **6.0**
- recommendation: inspect manually
- issue url: https://github.com/scala/scala3/issues/24760

- likely files:
  - `compiler/src/dotty/tools/dotc/core/Types.scala`
  - `compiler/src/dotty/tools/dotc/semanticdb/generated/Type.scala`
  - `compiler/src/dotty/tools/dotc/core/TypeComparer.scala`
  - `compiler/src/dotty/tools/dotc/typer/Typer.scala`
  - `compiler/src/dotty/tools/dotc/core/MatchTypeTrace.scala`

- contribution signals:
  - already actively worked on in same repo? no
  - same-repo PR links: 0
  - referenced by external repos? no
  - external references: 0
  - maintainer hinted direction? no
  - maintainer-hint count: 0
  - dormant days: 67

### #24506 — Error message "No ClassTag available for T" not helpful on what to do to fix it and has no reflect.ClassTag to show where it is

- subsystem guess: `diagnostics`
- local score: **6.0**
- recommendation: inspect manually
- issue url: https://github.com/scala/scala3/issues/24506

- likely files:
  - `compiler/src/dotty/tools/dotc/transform/init/Objects.scala`
  - `compiler/test/dotty/tools/dotc/config/ScalaSettingsTests.scala`
  - `compiler/test/dotty/tools/vulpix/ParallelTesting.scala`
  - `compiler/src/dotty/tools/dotc/reporting/Reporter.scala`
  - `compiler/src/dotty/tools/dotc/config/ScalaSettings.scala`

- contribution signals:
  - already actively worked on in same repo? no
  - same-repo PR links: 0
  - referenced by external repos? no
  - external references: 0
  - maintainer hinted direction? no
  - maintainer-hint count: 0
  - dormant days: 119

### #25585 — -Ysafe-init-global test warns pos/LazyList.scala

- subsystem guess: `diagnostics`
- local score: **5.0**
- recommendation: inspect manually
- issue url: https://github.com/scala/scala3/issues/25585

- likely files:
  - `compiler/src/dotty/tools/dotc/transform/init/Objects.scala`
  - `compiler/test/dotty/tools/dotc/config/ScalaSettingsTests.scala`
  - `compiler/test/dotty/tools/vulpix/ParallelTesting.scala`
  - `compiler/src/dotty/tools/dotc/reporting/Reporter.scala`
  - `compiler/src/dotty/tools/dotc/config/ScalaSettings.scala`

- contribution signals:
  - already actively worked on in same repo? no
  - same-repo PR links: 0
  - referenced by external repos? no
  - external references: 0
  - maintainer hinted direction? no
  - maintainer-hint count: 0
  - dormant days: 3

### #25565 — Regression for deriviation of enums/union types in `taig/mapping`

- subsystem guess: `typer`
- local score: **5.0**
- recommendation: inspect manually
- issue url: https://github.com/scala/scala3/issues/25565

- likely files:
  - `compiler/src/dotty/tools/dotc/typer/Typer.scala`
  - `compiler/src/dotty/tools/dotc/core/Definitions.scala`
  - `compiler/test/dotty/tools/dotc/transform/LazyValsTest.scala`
  - `compiler/src/dotty/tools/dotc/core/Types.scala`
  - `compiler/src/dotty/tools/dotc/core/Contexts.scala`

- contribution signals:
  - already actively worked on in same repo? no
  - same-repo PR links: 0
  - referenced by external repos? no
  - external references: 0
  - maintainer hinted direction? no
  - maintainer-hint count: 0
  - dormant days: 4

## Churn / test investment report

Top files where tests, refactors, or smaller components may pay off:

- `compiler/src/dotty/tools/dotc/typer/Typer.scala` — churn=1637, bugfix_churn=471, todo_hits=12
- `compiler/src/dotty/tools/dotc/parsing/Parsers.scala` — churn=1000, bugfix_churn=295, todo_hits=2
- `compiler/src/dotty/tools/dotc/core/Types.scala` — churn=1242, bugfix_churn=282, todo_hits=9
- `compiler/src/dotty/tools/dotc/typer/Applications.scala` — churn=647, bugfix_churn=194, todo_hits=2
- `compiler/src/dotty/tools/dotc/core/TypeComparer.scala` — churn=719, bugfix_churn=178, todo_hits=2
- `compiler/src/dotty/tools/dotc/typer/Implicits.scala` — churn=593, bugfix_churn=177, todo_hits=1
- `compiler/src/dotty/tools/dotc/ast/Desugar.scala` — churn=635, bugfix_churn=175, todo_hits=4
- `compiler/src/dotty/tools/dotc/typer/Checking.scala` — churn=529, bugfix_churn=160, todo_hits=1
- `compiler/src/dotty/tools/dotc/reporting/diagnostic/messages.scala` — churn=264, bugfix_churn=153, todo_hits=0
- `compiler/test/dotty/tools/dotc/CompilationTests.scala` — churn=454, bugfix_churn=138, todo_hits=1
- `compiler/src/dotty/tools/dotc/core/SymDenotations.scala` — churn=586, bugfix_churn=136, todo_hits=2
- `compiler/src/dotty/tools/dotc/transform/patmat/Space.scala` — churn=369, bugfix_churn=133, todo_hits=0
- `compiler/src/dotty/tools/dotc/typer/Namer.scala` — churn=566, bugfix_churn=128, todo_hits=4
- `compiler/src/dotty/tools/dotc/reporting/messages.scala` — churn=306, bugfix_churn=126, todo_hits=1
- `compiler/src/dotty/tools/dotc/core/Definitions.scala` — churn=902, bugfix_churn=125, todo_hits=5

## Topic map

### Diagnostics

- issue count: 48
- issues:
  - [#25594 — Extension method overload resolution picks wrong candidate when lambda parameter type must be inferred](https://github.com/scala/scala3/issues/25594)
  - [#25590 — Inference of boundary/break style control abstractions broken unless via direct method reference](https://github.com/scala/scala3/issues/25590)
  - [#25585 — -Ysafe-init-global test warns pos/LazyList.scala](https://github.com/scala/scala3/issues/25585)
  - [#25571 — "-Werror" with "-Wunused:nowarn" does not work](https://github.com/scala/scala3/issues/25571)
  - [#25553 — Unable to suppress discarded non-unit warning](https://github.com/scala/scala3/issues/25553)
  - [#25544 — `@unchecked` tuple destructuring is now ignored](https://github.com/scala/scala3/issues/25544)
  - [#25534 — Typer regression in `atnos-org/eff`](https://github.com/scala/scala3/issues/25534)
  - [#25508 — REPL still prints LazyVal warnings (presumably because of fansi+pprint)](https://github.com/scala/scala3/issues/25508)
  - [#25493 — Member/extension defs as patterns](https://github.com/scala/scala3/issues/25493)
  - [#25465 — Capture checking breaks the REPL/scala-cli `:type` command](https://github.com/scala/scala3/issues/25465)


- representative files:
  - `compiler/src/dotty/tools/dotc/transform/init/Objects.scala`
  - `compiler/test/dotty/tools/dotc/config/ScalaSettingsTests.scala`
  - `compiler/test/dotty/tools/vulpix/ParallelTesting.scala`
  - `compiler/src/dotty/tools/dotc/reporting/Reporter.scala`
  - `compiler/src/dotty/tools/dotc/config/ScalaSettings.scala`

### Typer

- issue count: 36
- issues:
  - [#25565 — Regression for deriviation of enums/union types in `taig/mapping`](https://github.com/scala/scala3/issues/25565)
  - [#25557 — Path dependent type broken in secondary param list when args are reordered](https://github.com/scala/scala3/issues/25557)
  - [#25555 — Coverage instrumentation widens singleton types during argument lifting, causing Ycheck failure](https://github.com/scala/scala3/issues/25555)
  - [#25541 — `-Xcheck-macros` regression in `upickle` dependent projects](https://github.com/scala/scala3/issues/25541)
  - [#25534 — Typer regression in `atnos-org/eff`](https://github.com/scala/scala3/issues/25534)
  - [#25504 — Figure out the exact semantics of `apply` in edge cases](https://github.com/scala/scala3/issues/25504)
  - [#25493 — Member/extension defs as patterns](https://github.com/scala/scala3/issues/25493)
  - [#25491 — CC retyper infers Nothing from intersection with singleton type](https://github.com/scala/scala3/issues/25491)
  - [#25447 — Presentation compiler issues with Scala JS](https://github.com/scala/scala3/issues/25447)
  - [#25408 — Dotty allows compiling `scala.Int` but crashes during bytecode generation](https://github.com/scala/scala3/issues/25408)


- representative files:
  - `compiler/src/dotty/tools/dotc/typer/Typer.scala`
  - `compiler/src/dotty/tools/dotc/core/Definitions.scala`
  - `compiler/test/dotty/tools/dotc/transform/LazyValsTest.scala`
  - `compiler/src/dotty/tools/dotc/core/Types.scala`
  - `compiler/src/dotty/tools/dotc/core/Contexts.scala`

### Explicit Nulls

- issue count: 15
- issues:
  - [#25565 — Regression for deriviation of enums/union types in `taig/mapping`](https://github.com/scala/scala3/issues/25565)
  - [#25551 — Repl returns null when using io.StdIn.readLine()](https://github.com/scala/scala3/issues/25551)
  - [#25271 — Runtime errors when implementing non-sealed java interface](https://github.com/scala/scala3/issues/25271)
  - [#25239 — False `Unreachable case except for null` warning in `inline def` with a match expression with type params](https://github.com/scala/scala3/issues/25239)
  - [#25183 — Compiler crash using `private var` constructor parameter and user-defined setter for field of the same name](https://github.com/scala/scala3/issues/25183)
  - [#25163 — Using value before definition results in null without warning](https://github.com/scala/scala3/issues/25163)
  - [#25162 — Null not removed when using .nn on a opaque type union with Null](https://github.com/scala/scala3/issues/25162)
  - [#24979 — "Unreachable case except for null" with `Free` and wildcard type](https://github.com/scala/scala3/issues/24979)
  - [#24899 — Unsound path-dependent types without initialization checking](https://github.com/scala/scala3/issues/24899)
  - [#24770 — Cannot assign nullable type parameter to generic types from Java under explicit nulls](https://github.com/scala/scala3/issues/24770)


- representative files:
  - `tests/run/bridges.scala`
  - `compiler/src/dotty/tools/dotc/typer/Nullables.scala`
  - `compiler/src/dotty/tools/dotc/core/Types.scala`
  - `compiler/src/dotty/tools/dotc/typer/Typer.scala`
  - `compiler/src/dotty/tools/dotc/core/ImplicitNullInterop.scala`

### Match Types

- issue count: 7
- issues:
  - [#25341 — Should `ConstFold` use `TypeComparer.constValue`?](https://github.com/scala/scala3/issues/25341)
  - [#25246 — Crash: `AssertionError` in `TypeOps.dominators` with complex context bounds and quoted expression](https://github.com/scala/scala3/issues/25246)
  - [#25129 — Matches and match types forget bound of extracted type variable](https://github.com/scala/scala3/issues/25129)
  - [#24836 — strictEquality doesn't work with GADTs](https://github.com/scala/scala3/issues/24836)
  - [#24760 — Overriding with an inline method and inline match is unsound](https://github.com/scala/scala3/issues/24760)
  - [#24548 — Inconsistent match type case legality](https://github.com/scala/scala3/issues/24548)
  - [#24512 — missing `scala.collection.generic.IsSeq` instance for `scala.IArray`](https://github.com/scala/scala3/issues/24512)


- representative files:
  - `compiler/src/dotty/tools/dotc/core/Types.scala`
  - `compiler/src/dotty/tools/dotc/semanticdb/generated/Type.scala`
  - `compiler/src/dotty/tools/dotc/core/TypeComparer.scala`
  - `compiler/src/dotty/tools/dotc/typer/Typer.scala`
  - `compiler/src/dotty/tools/dotc/core/MatchTypeTrace.scala`

### Namer

- issue count: 3
- issues:
  - [#25447 — Presentation compiler issues with Scala JS](https://github.com/scala/scala3/issues/25447)
  - [#25244 — Crash in `tpd.singleton` on `PreviousErrorType` during error recovery (inline match + quoted pattern with unresolved import)](https://github.com/scala/scala3/issues/25244)
  - [#24719 — Assertion failure in `LazyAnnotation.tree`](https://github.com/scala/scala3/issues/24719)


- representative files:
  - `tests/run/t8199.scala`
  - `compiler/src/dotty/tools/dotc/core/tasty/TastyPrinter.scala`
  - `compiler/src/dotty/tools/dotc/core/tasty/NameBuffer.scala`
  - `compiler/src/dotty/tools/dotc/core/unpickleScala2/Scala2Unpickler.scala`
  - `compiler/src/dotty/tools/dotc/typer/Namer.scala`
