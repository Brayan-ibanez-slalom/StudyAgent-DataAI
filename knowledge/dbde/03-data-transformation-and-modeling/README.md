# dbde-03 — Data Transformation and Modeling

**Exam:** Databricks Certified Data Engineer Associate
**Weight:** not published by dbt Labs. Every question scores one point.
**Provenance of this domain:** Databricks Data Engineer Associate exam guide, Section 3 (22%)

## Tasks

| Task | Title |
|---|---|
| 3.1 | Implement data cleaning by reading bronze tables with PySpark/SQL, cleaning nulls, standardizing data types, and writing to new silver tables |
| 3.2 | Combine DataFrames with operations such as Inner join, left join, broadcast join, multiple keys, cross join, union, and union all |
| 3.3 | Manipulate columns, rows, and table structures by adding, dropping, splitting, renaming column names, applying filters, and exploding arrays |
| 3.4 | Perform data deduplication operations and aggregate operations on DataFrames, such as count, approximate count distinct, and mean, summary |
| 3.5 | Understand the basic tuning parameters (spark.sql.shuffle.partitions, spark.default.parallelism, spark.executor/driver.memory, spark.sql.autoBroadcastJoinThreshold) and re-measure the performance |
| 3.6 | Understand the difference between, and how to build, Gold layer objects such as materialized views, views, streaming tables, and tables for BI and analytics teams in Unity Catalog |
| 3.7 | Apply data quality checks and validation rules to ensure reliable Silver and Gold datasets |

## Notes in this folder

One `.md` per concept, kebab-case. Every note must carry:

```
# <Title>

**Domain:** dbde-03 — Task 3.1
**Verified:** YYYY-MM-DD
**Concepts:** comma, separated, lookup, keys
```

Then rebuild the index: `python3 scripts/build_topic_index.py`

See [knowledge/README.md](../../README.md) for the full note contract.
