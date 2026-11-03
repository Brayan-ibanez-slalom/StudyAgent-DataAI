# Transformations, joins and the gold layer

**Domain:** dbde-03 — Task 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7
**Verified:** 2026-11-03
**Concepts:** medallion, bronze, silver, gold, broadcast join, dropDuplicates, approx_count_distinct, explode, materialized view, streaming table, expectations, shuffle partitions

> Seed note. Scope is from the official exam guide; deepen the PySpark/SQL API detail
> from the linked docs before sealing hard items.

## Why this is on the exam

At 22% this is the largest section. Expect concrete PySpark/SQL behaviour questions
(what does this join/dedup/explode produce) mixed with design questions (which gold
object should the BI team read).

## Scope — official objectives

| Task | Objective (verbatim from the exam guide) |
|---|---|
| 3.1 | Implement data cleaning by reading bronze tables with PySpark/SQL, cleaning nulls, standardizing data types, and writing to new silver tables |
| 3.2 | Combine DataFrames with operations such as Inner join, left join, broadcast join, multiple keys, cross join, union, and union all |
| 3.3 | Manipulate columns, rows, and table structures by adding, dropping, splitting, renaming column names, applying filters, and exploding arrays |
| 3.4 | Perform data deduplication operations and aggregate operations on DataFrames, such as count, approximate count distinct, and mean, summary |
| 3.5 | Understand the basic tuning parameters (spark.sql.shuffle.partitions, spark.default.parallelism, spark.executor/driver.memory, spark.sql.autoBroadcastJoinThreshold) and re-measure the performance |
| 3.6 | Understand the difference between, and how to build, Gold layer objects such as materialized views, views, streaming tables, and tables for BI and analytics teams in Unity Catalog |
| 3.7 | Apply data quality checks and validation rules to ensure reliable Silver and Gold datasets |

## Which gold-layer object

| Need | Build |
|---|---|
| Always-current logic, no storage, recompute on every read | **View** |
| Precomputed and refreshable results for BI | **Materialized view** |
| Append-only results that keep up with arriving source data | **Streaming table** |
| A plain governed dataset built by your own job | **Table** |

## Joins and dedup — what to watch

- A **broadcast join** ships the small side to every executor and removes the shuffle.
  `spark.sql.autoBroadcastJoinThreshold` is the size cut-off that decides this
  automatically.
- `union` and `unionAll` combine by **position**; `unionByName` combines by column name.
- `dropDuplicates()` with no columns de-duplicates on the whole row; with columns it
  keeps an arbitrary row per key — if you need a *specific* row, use a window function
  with `row_number()`.
- `approx_count_distinct` trades exactness for speed; do not offer it when the question
  demands an exact count.

## Tuning parameters

| Parameter | Controls |
|---|---|
| `spark.sql.shuffle.partitions` | How many partitions a shuffle produces |
| `spark.default.parallelism` | Default parallelism for RDD operations |
| `spark.executor.memory` / `spark.driver.memory` | Memory per executor / driver |
| `spark.sql.autoBroadcastJoinThreshold` | Max size for an automatic broadcast join |

The objective ends with "and re-measure the performance" — the exam wants the loop, not
a one-shot setting.

## Traps

- **Trap:** *lowering* `spark.sql.shuffle.partitions` makes each partition bigger, which
  makes skew worse, not better.
- **Trap:** a materialized view is not just a cached view — it is stored and refreshed,
  so staleness is a real consideration.
- **Trap:** `explode` on an empty or null array drops the row. Use `explode_outer` when
  you need to keep it.

## Verify before sealing

- [Transform data](https://docs.databricks.com/aws/en/transform/)
- [Delta Lake on Databricks](https://docs.databricks.com/aws/en/delta/)
- [Optimization recommendations](https://docs.databricks.com/aws/en/optimizations/)
