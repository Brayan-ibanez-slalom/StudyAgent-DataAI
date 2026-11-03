# Diagnosing slow and failing pipelines

**Domain:** dbde-06 — Task 6.1, 6.2, 6.3, 6.4, 6.5
**Verified:** 2026-11-03
**Concepts:** spark ui, data skew, shuffle, spill, aqe, salting, liquid clustering, predictive optimization, run history, out of memory, cluster startup failure

> Seed note. Scope is from the official exam guide; deepen the Spark UI metric detail
> from the linked docs before sealing hard items.

## Why this is on the exam

10% of the exam, and the questions read like incident reports: here are the symptoms,
pick the cause. Reading stage-level metrics correctly is the whole game.

## Scope — official objectives

| Task | Objective (verbatim from the exam guide) |
|---|---|
| 6.1 | Identify trends in job performance using the Lakeflow Jobs run history view to compare current execution times against historical baselines |
| 6.2 | Use the Lakeflow Jobs UI to monitor pipeline health by interpreting job statuses, viewing DAG-based task graphs to spot upstream blockers, and tracking pipeline run times and failure rates |
| 6.3 | Identify common performance bottlenecks such as data skew, shuffling, and disk spilling by interpreting stage-level metrics in the Spark UI |
| 6.4 | Understand the features of Liquid Clustering and predictive optimization |
| 6.5 | Diagnose cluster startup failures, library conflicts, and out-of-memory issues |

## Reading the symptom

| Symptom in the Spark UI | Diagnosis | Fix |
|---|---|---|
| Most tasks finish fast, one runs far longer; Max shuffle read is many times the median | **Data skew** on a hot key | Salt the key so it spreads across tasks, then combine partial results |
| Large spill-to-disk metrics on a stage | Partitions too large for memory | More partitions, more memory, or less data per task |
| Heavy shuffle read/write on a join | Shuffle join where a broadcast would do | Broadcast the small side |
| Driver OOM | Collecting too much to the driver | Avoid `collect()`; aggregate on the cluster |

**Adaptive Query Execution** handles *skewed joins* automatically. It does **not**
relieve a skewed `groupBy` aggregation — so "AQE is already enabled" in a stem about a
wide `groupBy` is a deliberate dead end, and salting is the answer. This is stated in
the exam guide's own answer key.

## Layout and maintenance

- **Liquid clustering** replaces fixed partitioning and Z-ordering with a clustering
  key you can change later without rewriting the table layout by hand.
- **Predictive optimization** lets Databricks decide and run maintenance operations
  for you rather than scheduling `OPTIMIZE`/`VACUUM` yourself.

## Traps

- **Trap:** scaling the cluster up does not fix skew — the one oversized task still runs
  alone while the new executors idle.
- **Trap:** lowering `spark.sql.shuffle.partitions` to "do less work" concentrates more
  rows per partition and worsens skew.
- **Trap:** a cluster that will not start is an infrastructure or init-script problem;
  look at the cluster event log, not the Spark UI.
- **Trap:** comparing a single run against nothing. The objective explicitly asks for
  the run history *baseline*.

## Verify before sealing

- [Optimization recommendations](https://docs.databricks.com/aws/en/optimizations/)
- [Spark UI guide](https://docs.databricks.com/aws/en/optimizations/spark-ui-guide/)
- [Liquid clustering](https://docs.databricks.com/aws/en/delta/clustering)
