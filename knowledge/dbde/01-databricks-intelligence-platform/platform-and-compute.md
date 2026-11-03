# Databricks platform architecture and compute choice

**Domain:** dbde-01 — Task 1.1, 1.2
**Verified:** 2026-11-03
**Concepts:** delta lake, unity catalog, time travel, lakehouse, all-purpose cluster, job cluster, sql warehouse, serverless, photon, dbu

> Seed note. The scope and the decision tables below are grounded in the official exam
> guide and the vendor docs linked at the bottom. Deepen it before sealing hard items.

## Why this is on the exam

Section 1 is only 6% of the exam, but it is the section every other section leans on.
A compute question is rarely "what is a cluster" — it is a scenario that names a
workload shape (many concurrent analysts, a nightly ETL job, a lone developer) and asks
which compute fits, with cost as the tie-breaker.

## Scope — official objectives

| Task | Objective (verbatim from the exam guide) |
|---|---|
| 1.1 | Understand the core components of the Databricks Platform, such as its architecture, Delta Lake, and Unity Catalog |
| 1.2 | Understand Databricks Platform's compute services, including their characteristics, limitations, and cost models, and select the most suitable option for each workload use case |

## Core components

- **Delta Lake** is the table format: ACID transactions over files in cloud object
  storage, plus versioning. That versioning is what gives you **time travel** (read an
  earlier version) and `RESTORE TABLE ... TO VERSION AS OF` (roll a bad load back).
- **Unity Catalog** is the governance layer. Objects are addressed through a
  three-level namespace, `catalog.schema.table`, and privileges are granted on those
  objects rather than on storage paths.
- Together they are the lakehouse answer to "reliable rollback + audit trail + one
  governed source of truth for BI and AI" — a phrasing the official sample questions
  use almost word for word.

## Choosing compute

| Workload | Use | Why not the others |
|---|---|---|
| Many analysts running ad hoc SQL all day | **Serverless SQL warehouse**, autoscaling | Fast start and query isolation for concurrent users; a job cluster is for scheduled ETL, and a fixed or single-node cluster cannot balance concurrency against cost |
| Scheduled production ETL | **Job cluster** | Created for the run and torn down after, so you do not pay for idle time |
| Interactive notebook development | **All-purpose cluster** | Persists between commands; set auto-termination so it does not idle |
| Tiny dev or test work | **Single-node cluster** | No worker cost, but no parallelism either |

**Cost model:** compute is billed in DBUs, and the DBU rate varies by compute type.
Idle all-purpose clusters are the classic avoidable cost; auto-termination and
autoscaling are the classic answers.

## Traps

- **Trap:** "Add more executors" is almost never the right answer to a slow job in this
  exam. Look for the real cause (skew, idle compute, wrong compute type) first.
- **Trap:** a job cluster is not interchangeable with a SQL warehouse. If the scenario
  says *concurrent interactive SQL users*, the answer is a SQL warehouse.
- **Trap:** DBFS-era answers (manual file versioning, nightly copies) are distractors.
  Delta Lake plus Unity Catalog is the governed answer.
- **Trap:** Delta Lake and Unity Catalog solve different problems. Delta gives you ACID
  and history; Unity Catalog gives you permissions and lineage. A question asking about
  *access* is a Unity Catalog question even if the table is Delta.

## Verify before sealing

- [Delta Lake on Databricks](https://docs.databricks.com/aws/en/delta/)
- [Unity Catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/)
- [Compute](https://docs.databricks.com/aws/en/compute/)
- [Data Engineer Associate exam guide](https://www.databricks.com/learn/certification/data-engineer-associate)
