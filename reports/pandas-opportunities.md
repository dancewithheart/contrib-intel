# pandas opportunity report

## Short summary

Use the sections below differently:

1. **Issue clusters** — high-leverage fixes
2. **Issue candidates** — concrete next contribution targets
3. **Churn / test investment** — audits, refactors, property-test opportunities
4. **Topic map** — learning and exploration

Most promising current issue-cluster directions:

1. **Sql Io** — issues #68505, #68433, #68372; files `pandas/tests/io/test_sql.py`, `pandas/io/sql.py`
2. **Categorical** — issues #68703, #68437, #67065; files `pandas/core/arrays/categorical.py`, `pandas/tests/arrays/categorical/test_constructors.py`
3. **Groupby** — issues #67995, #66850, #66626; files `pandas/tests/groupby/test_groupby.py`, `pandas/core/groupby/groupby.py`

Top concrete issue candidates:

- **#66688** API: astype to CategoricalDtype matches by lookup instead of casting, so legitimate casts silently become NaN (subsystem: `categorical`, score: 41.0) — inspect manually
- **#66626** NumPy/object fallbacks in Arrow-backed arrays (subsystem: `groupby`, score: 20.0) — inspect manually
- **#67014** API: Restrictions on EA scalar types (subsystem: `missing_data`, score: 16.0) — inspect manually
- **#66382** BUG: read_csv(dtype="category") ignores dtype_backend for the c and python engines (subsystem: `categorical`, score: 14.0) — inspect manually
- **#65419** BUG: Index.get_indexer matches pd.NA against NaN for list input but not ndarray input (subsystem: `missing_data`, score: 14.0) — inspect manually

## Issue clusters

### Sql Io

- subsystem: `sql_io`
- overall score: **458.5**
- issue count: 34
- issues:
  - [#68505 — BUG: parallel read_csv with sqlite converters](https://github.com/pandas-dev/pandas/issues/68505)
  - [#68433 — ENH: move the postgresql extra from psycopg2 to psycopg 3](https://github.com/pandas-dev/pandas/issues/68433)
  - [#68372 — BUG: mixed int64/float64 Index operations falsely match distinct labels above 2**53](https://github.com/pandas-dev/pandas/issues/68372)
  - [#68310 — BUG: .to_latex() throws an exception in some cases](https://github.com/pandas-dev/pandas/issues/68310)
  - [#68264 — BUG: `RangeIndex.symmetric_difference` skips required sort when one side is empty](https://github.com/pandas-dev/pandas/issues/68264)
  - [#68041 — BUG: read_csv fails to finalize index when engine='pyarrow' and dtype is scalar (or dict without an index specified)](https://github.com/pandas-dev/pandas/issues/68041)
  - [#68026 — BUG: to_xml() export not valid for bool dtype](https://github.com/pandas-dev/pandas/issues/68026)
  - [#67949 — BUG: pd.to_numeric with errors="coerce" fails to produce actual NA values when applied to dtype string[pyarrow] values](https://github.com/pandas-dev/pandas/issues/67949)
  - [#67726 — BUG: IndexError with certain subplot order in stacked barchart](https://github.com/pandas-dev/pandas/issues/67726)
  - [#67065 — BUG: HDFStore.select with where="cat == None" returns empty DataFrame for Categorical columns instead of matching missing/NaN rows](https://github.com/pandas-dev/pandas/issues/67065)

- top files:
  - `pandas/tests/io/test_sql.py`
  - `pandas/io/sql.py`
  - `pandas/core/generic.py`
  - `pandas/core/frame.py`
  - `pandas/tests/api/test_api.py`

- linkage/context signals:
  - same-repo PR links: 0
  - external repo references: 0
  - maintainer hint comments: 0
  - dormant issues: 1

- notes:
  - pandas/tests/io/test_sql.py:1932 mentions TODO
  - pandas/tests/io/test_sql.py:1993 mentions TODO
  - pandas/io/sql.py:204 mentions TODO
  - pandas/io/sql.py:974 mentions TODO
  - pandas/io/sql.py:1477 mentions TODO

### Categorical

- subsystem: `categorical`
- overall score: **283.16**
- issue count: 5
- issues:
  - [#68703 — API: select_dtypes](https://github.com/pandas-dev/pandas/issues/68703)
  - [#68437 — DOC/RLS: improve the 3.1.0 whatsnew notes](https://github.com/pandas-dev/pandas/issues/68437)
  - [#67065 — BUG: HDFStore.select with where="cat == None" returns empty DataFrame for Categorical columns instead of matching missing/NaN rows](https://github.com/pandas-dev/pandas/issues/67065)
  - [#66688 — API: astype to CategoricalDtype matches by lookup instead of casting, so legitimate casts silently become NaN](https://github.com/pandas-dev/pandas/issues/66688)
  - [#66382 — BUG: read_csv(dtype="category") ignores dtype_backend for the c and python engines](https://github.com/pandas-dev/pandas/issues/66382)

- top files:
  - `pandas/core/arrays/categorical.py`
  - `pandas/tests/arrays/categorical/test_constructors.py`
  - `pandas/tests/groupby/test_categorical.py`
  - `pandas/tests/reshape/test_union_categoricals.py`
  - `pandas/tests/reshape/concat/test_categorical.py`

- linkage/context signals:
  - same-repo PR links: 0
  - external repo references: 0
  - maintainer hint comments: 0
  - dormant issues: 0

- notes:
  - pandas/core/arrays/categorical.py:2398 mentions TODO
  - pandas/tests/groupby/test_categorical.py:1426 mentions TODO
  - pandas/tests/groupby/test_categorical.py:1456 mentions TODO

### Groupby

- subsystem: `groupby`
- overall score: **248.66**
- issue count: 6
- issues:
  - [#67995 — BUILD: window/meson.build never passes --shared=pandas._libs._cyutility to its extensions](https://github.com/pandas-dev/pandas/issues/67995)
  - [#66850 — ENH: add `DatetimeIndexResampler`, `PeriodIndexResampler` and `TimedeltaIndexResampler` to `pandas.api.typing`](https://github.com/pandas-dev/pandas/issues/66850)
  - [#66626 — NumPy/object fallbacks in Arrow-backed arrays](https://github.com/pandas-dev/pandas/issues/66626)
  - [#66605 — BUG: cumsum/cumprod raises ArrowInvalid: overflow on integer ArrowDtypes instead of upcasting](https://github.com/pandas-dev/pandas/issues/66605)
  - [#66410 — BUG: Cannot build `pandas` with MSVC](https://github.com/pandas-dev/pandas/issues/66410)
  - [#66281 — ENH: Optimize Series.apply User-Defined Functions (UDFs) via JIT Compilation Engine Option](https://github.com/pandas-dev/pandas/issues/66281)

- top files:
  - `pandas/tests/groupby/test_groupby.py`
  - `pandas/core/groupby/groupby.py`
  - `pandas/core/groupby/generic.py`
  - `pandas/tests/groupby/aggregate/test_aggregate.py`
  - `pandas/tests/groupby/test_categorical.py`

- linkage/context signals:
  - same-repo PR links: 0
  - external repo references: 0
  - maintainer hint comments: 0
  - dormant issues: 0

- notes:
  - pandas/tests/groupby/test_groupby.py:345 mentions TODO
  - pandas/tests/groupby/test_groupby.py:1841 mentions TODO
  - pandas/tests/groupby/test_groupby.py:2839 mentions TODO
  - pandas/core/groupby/groupby.py:223 mentions TODO
  - pandas/core/groupby/groupby.py:948 mentions TODO

### Missing Data

- subsystem: `missing_data`
- overall score: **132.49**
- issue count: 7
- issues:
  - [#67949 — BUG: pd.to_numeric with errors="coerce" fails to produce actual NA values when applied to dtype string[pyarrow] values](https://github.com/pandas-dev/pandas/issues/67949)
  - [#67065 — BUG: HDFStore.select with where="cat == None" returns empty DataFrame for Categorical columns instead of matching missing/NaN rows](https://github.com/pandas-dev/pandas/issues/67065)
  - [#67014 — API: Restrictions on EA scalar types](https://github.com/pandas-dev/pandas/issues/67014)
  - [#66966 — ENH: Allow assign() lambdas to optionally receive the target column as a second argument](https://github.com/pandas-dev/pandas/issues/66966)
  - [#66255 — BUG: Float64 vs float64 incorrect result when using empty slice](https://github.com/pandas-dev/pandas/issues/66255)
  - [#65419 — BUG: Index.get_indexer matches pd.NA against NaN for list input but not ndarray input](https://github.com/pandas-dev/pandas/issues/65419)
  - [#65237 — BUG: read_csv() into FloatingArrays converts np.nan into pd.NA, even with distinguish_nan_and_na=True](https://github.com/pandas-dev/pandas/issues/65237)

- top files:
  - `pandas/tests/series/methods/test_fillna.py`
  - `pandas/tests/reductions/test_reductions.py`
  - `pandas/tests/frame/methods/test_fillna.py`
  - `pandas/tests/extension/test_arrow.py`
  - `pandas/tests/frame/test_reductions.py`

- linkage/context signals:
  - same-repo PR links: 0
  - external repo references: 0
  - maintainer hint comments: 0
  - dormant issues: 1

- notes:
  - pandas/tests/extension/test_arrow.py:88 mentions TODO
  - pandas/tests/extension/test_arrow.py:278 mentions TODO
  - pandas/tests/extension/test_arrow.py:540 mentions TODO
  - pandas/tests/extension/test_arrow.py:545 mentions TODO
  - pandas/tests/extension/test_arrow.py:782 mentions TODO

### Strings

- subsystem: `strings`
- overall score: **61.84**
- issue count: 2
- issues:
  - [#67024 — BUG: `Series.str.extract` with `ArrowDtype` raises on unnamed capture groups, and drops them when mixed with named ones](https://github.com/pandas-dev/pandas/issues/67024)
  - [#65892 — BUG: Inconsistent nan to None behaviour in replace() with scalar vs list value](https://github.com/pandas-dev/pandas/issues/65892)

- top files:
  - `pandas/tests/strings/test_extract.py`
  - `pandas/tests/strings/test_cat.py`
  - `pandas/core/strings/accessor.py`
  - `pandas/tests/strings/test_find_replace.py`
  - `pandas/core/arrays/string_.py`

- linkage/context signals:
  - same-repo PR links: 0
  - external repo references: 0
  - maintainer hint comments: 0
  - dormant issues: 0

- notes:
  - pandas/tests/strings/test_extract.py:14 mentions TODO
  - pandas/tests/strings/test_cat.py:381 mentions TODO
  - pandas/core/strings/accessor.py:186 mentions TODO
  - pandas/core/strings/accessor.py:647 mentions TODO
  - pandas/core/strings/accessor.py:2498 mentions TODO

## Issue candidates

Concrete issues enriched with contribution signals.

### #66688 — API: astype to CategoricalDtype matches by lookup instead of casting, so legitimate casts silently become NaN

- subsystem guess: `categorical`
- local score: **41.0**
- recommendation: inspect manually
- issue url: https://github.com/pandas-dev/pandas/issues/66688

- likely files:
  - `pandas/core/arrays/categorical.py`
  - `pandas/tests/arrays/categorical/test_constructors.py`
  - `pandas/tests/groupby/test_categorical.py`
  - `pandas/tests/reshape/test_union_categoricals.py`
  - `pandas/tests/reshape/concat/test_categorical.py`

- contribution signals:
  - already actively worked on in same repo? no
  - same-repo PR links: 0
  - referenced by external repos? no
  - external references: 0
  - maintainer hinted direction? no
  - maintainer-hint count: 0
  - dormant days: 33

### #66626 — NumPy/object fallbacks in Arrow-backed arrays

- subsystem guess: `groupby`
- local score: **20.0**
- recommendation: inspect manually
- issue url: https://github.com/pandas-dev/pandas/issues/66626

- likely files:
  - `pandas/tests/groupby/test_groupby.py`
  - `pandas/core/groupby/groupby.py`
  - `pandas/core/groupby/generic.py`
  - `pandas/tests/groupby/aggregate/test_aggregate.py`
  - `pandas/tests/groupby/test_categorical.py`

- contribution signals:
  - already actively worked on in same repo? no
  - same-repo PR links: 0
  - referenced by external repos? no
  - external references: 0
  - maintainer hinted direction? no
  - maintainer-hint count: 0
  - dormant days: 30

### #67014 — API: Restrictions on EA scalar types

- subsystem guess: `missing_data`
- local score: **16.0**
- recommendation: inspect manually
- issue url: https://github.com/pandas-dev/pandas/issues/67014

- likely files:
  - `pandas/tests/series/methods/test_fillna.py`
  - `pandas/tests/reductions/test_reductions.py`
  - `pandas/tests/frame/methods/test_fillna.py`
  - `pandas/tests/extension/test_arrow.py`
  - `pandas/tests/frame/test_reductions.py`

- contribution signals:
  - already actively worked on in same repo? no
  - same-repo PR links: 0
  - referenced by external repos? no
  - external references: 0
  - maintainer hinted direction? no
  - maintainer-hint count: 0
  - dormant days: 20

### #66382 — BUG: read_csv(dtype="category") ignores dtype_backend for the c and python engines

- subsystem guess: `categorical`
- local score: **14.0**
- recommendation: inspect manually
- issue url: https://github.com/pandas-dev/pandas/issues/66382

- likely files:
  - `pandas/core/arrays/categorical.py`
  - `pandas/tests/arrays/categorical/test_constructors.py`
  - `pandas/tests/groupby/test_categorical.py`
  - `pandas/tests/reshape/test_union_categoricals.py`
  - `pandas/tests/reshape/concat/test_categorical.py`

- contribution signals:
  - already actively worked on in same repo? no
  - same-repo PR links: 0
  - referenced by external repos? no
  - external references: 0
  - maintainer hinted direction? no
  - maintainer-hint count: 0
  - dormant days: 56

### #65419 — BUG: Index.get_indexer matches pd.NA against NaN for list input but not ndarray input

- subsystem guess: `missing_data`
- local score: **14.0**
- recommendation: inspect manually
- issue url: https://github.com/pandas-dev/pandas/issues/65419

- likely files:
  - `pandas/tests/series/methods/test_fillna.py`
  - `pandas/tests/reductions/test_reductions.py`
  - `pandas/tests/frame/methods/test_fillna.py`
  - `pandas/tests/extension/test_arrow.py`
  - `pandas/tests/frame/test_reductions.py`

- contribution signals:
  - already actively worked on in same repo? no
  - same-repo PR links: 0
  - referenced by external repos? no
  - external references: 0
  - maintainer hinted direction? no
  - maintainer-hint count: 0
  - dormant days: 11

### #67024 — BUG: `Series.str.extract` with `ArrowDtype` raises on unnamed capture groups, and drops them when mixed with named ones

- subsystem guess: `strings`
- local score: **13.0**
- recommendation: inspect manually
- issue url: https://github.com/pandas-dev/pandas/issues/67024

- likely files:
  - `pandas/tests/strings/test_extract.py`
  - `pandas/tests/strings/test_cat.py`
  - `pandas/core/strings/accessor.py`
  - `pandas/tests/strings/test_find_replace.py`
  - `pandas/core/arrays/string_.py`

- contribution signals:
  - already actively worked on in same repo? no
  - same-repo PR links: 0
  - referenced by external repos? no
  - external references: 0
  - maintainer hinted direction? no
  - maintainer-hint count: 0
  - dormant days: 18

### #67064 — DOC: user guide SQL section lacks PostgreSQL (psycopg 3) recipes

- subsystem guess: `sql_io`
- local score: **8.0**
- recommendation: inspect manually
- issue url: https://github.com/pandas-dev/pandas/issues/67064

- likely files:
  - `pandas/tests/io/test_sql.py`
  - `pandas/io/sql.py`
  - `pandas/core/generic.py`
  - `pandas/core/frame.py`
  - `pandas/tests/api/test_api.py`

- contribution signals:
  - already actively worked on in same repo? no
  - same-repo PR links: 0
  - referenced by external repos? no
  - external references: 0
  - maintainer hinted direction? no
  - maintainer-hint count: 0
  - dormant days: 3

### #68433 — ENH: move the postgresql extra from psycopg2 to psycopg 3

- subsystem guess: `sql_io`
- local score: **7.0**
- recommendation: inspect manually
- issue url: https://github.com/pandas-dev/pandas/issues/68433

- likely files:
  - `pandas/tests/io/test_sql.py`
  - `pandas/io/sql.py`
  - `pandas/core/generic.py`
  - `pandas/core/frame.py`
  - `pandas/tests/api/test_api.py`

- contribution signals:
  - already actively worked on in same repo? no
  - same-repo PR links: 0
  - referenced by external repos? no
  - external references: 0
  - maintainer hinted direction? no
  - maintainer-hint count: 0
  - dormant days: 4

### #68703 — API: select_dtypes

- subsystem guess: `categorical`
- local score: **5.0**
- recommendation: inspect manually
- issue url: https://github.com/pandas-dev/pandas/issues/68703

- likely files:
  - `pandas/core/arrays/categorical.py`
  - `pandas/tests/arrays/categorical/test_constructors.py`
  - `pandas/tests/groupby/test_categorical.py`
  - `pandas/tests/reshape/test_union_categoricals.py`
  - `pandas/tests/reshape/concat/test_categorical.py`

- contribution signals:
  - already actively worked on in same repo? no
  - same-repo PR links: 0
  - referenced by external repos? no
  - external references: 0
  - maintainer hinted direction? no
  - maintainer-hint count: 0
  - dormant days: 0

### #67065 — BUG: HDFStore.select with where="cat == None" returns empty DataFrame for Categorical columns instead of matching missing/NaN rows

- subsystem guess: `categorical`
- local score: **5.0**
- recommendation: inspect manually
- issue url: https://github.com/pandas-dev/pandas/issues/67065

- likely files:
  - `pandas/core/arrays/categorical.py`
  - `pandas/tests/arrays/categorical/test_constructors.py`
  - `pandas/tests/groupby/test_categorical.py`
  - `pandas/tests/reshape/test_union_categoricals.py`
  - `pandas/tests/reshape/concat/test_categorical.py`

- contribution signals:
  - already actively worked on in same repo? no
  - same-repo PR links: 0
  - referenced by external repos? no
  - external references: 0
  - maintainer hinted direction? no
  - maintainer-hint count: 0
  - dormant days: 12

### #68437 — DOC/RLS: improve the 3.1.0 whatsnew notes

- subsystem guess: `categorical`
- local score: **4.0**
- recommendation: inspect manually
- issue url: https://github.com/pandas-dev/pandas/issues/68437

- likely files:
  - `pandas/core/arrays/categorical.py`
  - `pandas/tests/arrays/categorical/test_constructors.py`
  - `pandas/tests/groupby/test_categorical.py`
  - `pandas/tests/reshape/test_union_categoricals.py`
  - `pandas/tests/reshape/concat/test_categorical.py`

- contribution signals:
  - already actively worked on in same repo? no
  - same-repo PR links: 0
  - referenced by external repos? no
  - external references: 0
  - maintainer hinted direction? no
  - maintainer-hint count: 0
  - dormant days: 1

### #68041 — BUG: read_csv fails to finalize index when engine='pyarrow' and dtype is scalar (or dict without an index specified)

- subsystem guess: `sql_io`
- local score: **4.0**
- recommendation: inspect manually
- issue url: https://github.com/pandas-dev/pandas/issues/68041

- likely files:
  - `pandas/tests/io/test_sql.py`
  - `pandas/io/sql.py`
  - `pandas/core/generic.py`
  - `pandas/core/frame.py`
  - `pandas/tests/api/test_api.py`

- contribution signals:
  - already actively worked on in same repo? no
  - same-repo PR links: 0
  - referenced by external repos? no
  - external references: 0
  - maintainer hinted direction? no
  - maintainer-hint count: 0
  - dormant days: 10

### #66410 — BUG: Cannot build `pandas` with MSVC

- subsystem guess: `groupby`
- local score: **4.0**
- recommendation: inspect manually
- issue url: https://github.com/pandas-dev/pandas/issues/66410

- likely files:
  - `pandas/tests/groupby/test_groupby.py`
  - `pandas/core/groupby/groupby.py`
  - `pandas/core/groupby/generic.py`
  - `pandas/tests/groupby/aggregate/test_aggregate.py`
  - `pandas/tests/groupby/test_categorical.py`

- contribution signals:
  - already actively worked on in same repo? no
  - same-repo PR links: 0
  - referenced by external repos? no
  - external references: 0
  - maintainer hinted direction? no
  - maintainer-hint count: 0
  - dormant days: 49

### #66255 — BUG: Float64 vs float64 incorrect result when using empty slice

- subsystem guess: `missing_data`
- local score: **4.0**
- recommendation: inspect manually
- issue url: https://github.com/pandas-dev/pandas/issues/66255

- likely files:
  - `pandas/tests/series/methods/test_fillna.py`
  - `pandas/tests/reductions/test_reductions.py`
  - `pandas/tests/frame/methods/test_fillna.py`
  - `pandas/tests/extension/test_arrow.py`
  - `pandas/tests/frame/test_reductions.py`

- contribution signals:
  - already actively worked on in same repo? no
  - same-repo PR links: 0
  - referenced by external repos? no
  - external references: 0
  - maintainer hinted direction? no
  - maintainer-hint count: 0
  - dormant days: 1

### #68505 — BUG: parallel read_csv with sqlite converters

- subsystem guess: `sql_io`
- local score: **3.0**
- recommendation: inspect manually
- issue url: https://github.com/pandas-dev/pandas/issues/68505

- likely files:
  - `pandas/tests/io/test_sql.py`
  - `pandas/io/sql.py`
  - `pandas/core/generic.py`
  - `pandas/core/frame.py`
  - `pandas/tests/api/test_api.py`

- contribution signals:
  - already actively worked on in same repo? no
  - same-repo PR links: 0
  - referenced by external repos? no
  - external references: 0
  - maintainer hinted direction? no
  - maintainer-hint count: 0
  - dormant days: 1

### #66605 — BUG: cumsum/cumprod raises ArrowInvalid: overflow on integer ArrowDtypes instead of upcasting

- subsystem guess: `groupby`
- local score: **3.0**
- recommendation: inspect manually
- issue url: https://github.com/pandas-dev/pandas/issues/66605

- likely files:
  - `pandas/tests/groupby/test_groupby.py`
  - `pandas/core/groupby/groupby.py`
  - `pandas/core/groupby/generic.py`
  - `pandas/tests/groupby/aggregate/test_aggregate.py`
  - `pandas/tests/groupby/test_categorical.py`

- contribution signals:
  - already actively worked on in same repo? no
  - same-repo PR links: 0
  - referenced by external repos? no
  - external references: 0
  - maintainer hinted direction? no
  - maintainer-hint count: 0
  - dormant days: 7

### #65892 — BUG: Inconsistent nan to None behaviour in replace() with scalar vs list value

- subsystem guess: `strings`
- local score: **3.0**
- recommendation: inspect manually
- issue url: https://github.com/pandas-dev/pandas/issues/65892

- likely files:
  - `pandas/tests/strings/test_extract.py`
  - `pandas/tests/strings/test_cat.py`
  - `pandas/core/strings/accessor.py`
  - `pandas/tests/strings/test_find_replace.py`
  - `pandas/core/arrays/string_.py`

- contribution signals:
  - already actively worked on in same repo? no
  - same-repo PR links: 0
  - referenced by external repos? no
  - external references: 0
  - maintainer hinted direction? no
  - maintainer-hint count: 0
  - dormant days: 80

### #65237 — BUG: read_csv() into FloatingArrays converts np.nan into pd.NA, even with distinguish_nan_and_na=True

- subsystem guess: `missing_data`
- local score: **3.0**
- recommendation: candidate for revival: dormant but still open
- issue url: https://github.com/pandas-dev/pandas/issues/65237

- likely files:
  - `pandas/tests/series/methods/test_fillna.py`
  - `pandas/tests/reductions/test_reductions.py`
  - `pandas/tests/frame/methods/test_fillna.py`
  - `pandas/tests/extension/test_arrow.py`
  - `pandas/tests/frame/test_reductions.py`

- contribution signals:
  - already actively worked on in same repo? no
  - same-repo PR links: 0
  - referenced by external repos? no
  - external references: 0
  - maintainer hinted direction? no
  - maintainer-hint count: 0
  - dormant days: 148

### #68372 — BUG: mixed int64/float64 Index operations falsely match distinct labels above 2**53

- subsystem guess: `sql_io`
- local score: **2.0**
- recommendation: inspect manually
- issue url: https://github.com/pandas-dev/pandas/issues/68372

- likely files:
  - `pandas/tests/io/test_sql.py`
  - `pandas/io/sql.py`
  - `pandas/core/generic.py`
  - `pandas/core/frame.py`
  - `pandas/tests/api/test_api.py`

- contribution signals:
  - already actively worked on in same repo? no
  - same-repo PR links: 0
  - referenced by external repos? no
  - external references: 0
  - maintainer hinted direction? no
  - maintainer-hint count: 0
  - dormant days: 5

### #68310 — BUG: .to_latex() throws an exception in some cases

- subsystem guess: `sql_io`
- local score: **2.0**
- recommendation: inspect manually
- issue url: https://github.com/pandas-dev/pandas/issues/68310

- likely files:
  - `pandas/tests/io/test_sql.py`
  - `pandas/io/sql.py`
  - `pandas/core/generic.py`
  - `pandas/core/frame.py`
  - `pandas/tests/api/test_api.py`

- contribution signals:
  - already actively worked on in same repo? no
  - same-repo PR links: 0
  - referenced by external repos? no
  - external references: 0
  - maintainer hinted direction? no
  - maintainer-hint count: 0
  - dormant days: 6

## Churn / test investment report

Top files where tests, refactors, or smaller components may pay off:

- `pandas/core/frame.py` — churn=3368, bugfix_churn=1132, todo_hits=23
- `pandas/core/generic.py` — churn=2234, bugfix_churn=661, todo_hits=13
- `pandas/core/series.py` — churn=2138, bugfix_churn=661, todo_hits=7
- `pandas/tests/test_frame.py` — churn=1123, bugfix_churn=569, todo_hits=0
- `pandas/core/indexes/base.py` — churn=1378, bugfix_churn=392, todo_hits=34
- `pandas/core/indexing.py` — churn=759, bugfix_churn=356, todo_hits=4
- `pandas/core/index.py` — churn=752, bugfix_churn=352, todo_hits=0
- `pandas/tests/test_series.py` — churn=649, bugfix_churn=328, todo_hits=0
- `pandas/core/groupby.py` — churn=668, bugfix_churn=312, todo_hits=0
- `pandas/core/internals.py` — churn=626, bugfix_churn=307, todo_hits=0
- `pandas/core/common.py` — churn=697, bugfix_churn=283, todo_hits=1
- `pandas/tests/test_groupby.py` — churn=450, bugfix_churn=241, todo_hits=0
- `pandas/core/groupby/groupby.py` — churn=729, bugfix_churn=237, todo_hits=13
- `pandas/core/indexes/multi.py` — churn=663, bugfix_churn=210, todo_hits=11
- `pandas/core/internals/blocks.py` — churn=764, bugfix_churn=204, todo_hits=24

## Topic map

### Sql Io

- issue count: 34
- issues:
  - [#68505 — BUG: parallel read_csv with sqlite converters](https://github.com/pandas-dev/pandas/issues/68505)
  - [#68433 — ENH: move the postgresql extra from psycopg2 to psycopg 3](https://github.com/pandas-dev/pandas/issues/68433)
  - [#68372 — BUG: mixed int64/float64 Index operations falsely match distinct labels above 2**53](https://github.com/pandas-dev/pandas/issues/68372)
  - [#68310 — BUG: .to_latex() throws an exception in some cases](https://github.com/pandas-dev/pandas/issues/68310)
  - [#68264 — BUG: `RangeIndex.symmetric_difference` skips required sort when one side is empty](https://github.com/pandas-dev/pandas/issues/68264)
  - [#68041 — BUG: read_csv fails to finalize index when engine='pyarrow' and dtype is scalar (or dict without an index specified)](https://github.com/pandas-dev/pandas/issues/68041)
  - [#68026 — BUG: to_xml() export not valid for bool dtype](https://github.com/pandas-dev/pandas/issues/68026)
  - [#67949 — BUG: pd.to_numeric with errors="coerce" fails to produce actual NA values when applied to dtype string[pyarrow] values](https://github.com/pandas-dev/pandas/issues/67949)
  - [#67726 — BUG: IndexError with certain subplot order in stacked barchart](https://github.com/pandas-dev/pandas/issues/67726)
  - [#67065 — BUG: HDFStore.select with where="cat == None" returns empty DataFrame for Categorical columns instead of matching missing/NaN rows](https://github.com/pandas-dev/pandas/issues/67065)


- representative files:
  - `pandas/tests/io/test_sql.py`
  - `pandas/io/sql.py`
  - `pandas/core/generic.py`
  - `pandas/core/frame.py`
  - `pandas/tests/api/test_api.py`

### Missing Data

- issue count: 7
- issues:
  - [#67949 — BUG: pd.to_numeric with errors="coerce" fails to produce actual NA values when applied to dtype string[pyarrow] values](https://github.com/pandas-dev/pandas/issues/67949)
  - [#67065 — BUG: HDFStore.select with where="cat == None" returns empty DataFrame for Categorical columns instead of matching missing/NaN rows](https://github.com/pandas-dev/pandas/issues/67065)
  - [#67014 — API: Restrictions on EA scalar types](https://github.com/pandas-dev/pandas/issues/67014)
  - [#66966 — ENH: Allow assign() lambdas to optionally receive the target column as a second argument](https://github.com/pandas-dev/pandas/issues/66966)
  - [#66255 — BUG: Float64 vs float64 incorrect result when using empty slice](https://github.com/pandas-dev/pandas/issues/66255)
  - [#65419 — BUG: Index.get_indexer matches pd.NA against NaN for list input but not ndarray input](https://github.com/pandas-dev/pandas/issues/65419)
  - [#65237 — BUG: read_csv() into FloatingArrays converts np.nan into pd.NA, even with distinguish_nan_and_na=True](https://github.com/pandas-dev/pandas/issues/65237)


- representative files:
  - `pandas/tests/series/methods/test_fillna.py`
  - `pandas/tests/reductions/test_reductions.py`
  - `pandas/tests/frame/methods/test_fillna.py`
  - `pandas/tests/extension/test_arrow.py`
  - `pandas/tests/frame/test_reductions.py`

### Groupby

- issue count: 6
- issues:
  - [#67995 — BUILD: window/meson.build never passes --shared=pandas._libs._cyutility to its extensions](https://github.com/pandas-dev/pandas/issues/67995)
  - [#66850 — ENH: add `DatetimeIndexResampler`, `PeriodIndexResampler` and `TimedeltaIndexResampler` to `pandas.api.typing`](https://github.com/pandas-dev/pandas/issues/66850)
  - [#66626 — NumPy/object fallbacks in Arrow-backed arrays](https://github.com/pandas-dev/pandas/issues/66626)
  - [#66605 — BUG: cumsum/cumprod raises ArrowInvalid: overflow on integer ArrowDtypes instead of upcasting](https://github.com/pandas-dev/pandas/issues/66605)
  - [#66410 — BUG: Cannot build `pandas` with MSVC](https://github.com/pandas-dev/pandas/issues/66410)
  - [#66281 — ENH: Optimize Series.apply User-Defined Functions (UDFs) via JIT Compilation Engine Option](https://github.com/pandas-dev/pandas/issues/66281)


- representative files:
  - `pandas/tests/groupby/test_groupby.py`
  - `pandas/core/groupby/groupby.py`
  - `pandas/core/groupby/generic.py`
  - `pandas/tests/groupby/aggregate/test_aggregate.py`
  - `pandas/tests/groupby/test_categorical.py`

### Categorical

- issue count: 5
- issues:
  - [#68703 — API: select_dtypes](https://github.com/pandas-dev/pandas/issues/68703)
  - [#68437 — DOC/RLS: improve the 3.1.0 whatsnew notes](https://github.com/pandas-dev/pandas/issues/68437)
  - [#67065 — BUG: HDFStore.select with where="cat == None" returns empty DataFrame for Categorical columns instead of matching missing/NaN rows](https://github.com/pandas-dev/pandas/issues/67065)
  - [#66688 — API: astype to CategoricalDtype matches by lookup instead of casting, so legitimate casts silently become NaN](https://github.com/pandas-dev/pandas/issues/66688)
  - [#66382 — BUG: read_csv(dtype="category") ignores dtype_backend for the c and python engines](https://github.com/pandas-dev/pandas/issues/66382)


- representative files:
  - `pandas/core/arrays/categorical.py`
  - `pandas/tests/arrays/categorical/test_constructors.py`
  - `pandas/tests/groupby/test_categorical.py`
  - `pandas/tests/reshape/test_union_categoricals.py`
  - `pandas/tests/reshape/concat/test_categorical.py`

### Strings

- issue count: 2
- issues:
  - [#67024 — BUG: `Series.str.extract` with `ArrowDtype` raises on unnamed capture groups, and drops them when mixed with named ones](https://github.com/pandas-dev/pandas/issues/67024)
  - [#65892 — BUG: Inconsistent nan to None behaviour in replace() with scalar vs list value](https://github.com/pandas-dev/pandas/issues/65892)


- representative files:
  - `pandas/tests/strings/test_extract.py`
  - `pandas/tests/strings/test_cat.py`
  - `pandas/core/strings/accessor.py`
  - `pandas/tests/strings/test_find_replace.py`
  - `pandas/core/arrays/string_.py`
