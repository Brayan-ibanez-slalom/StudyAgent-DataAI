# Lakeflow Jobs — tasks, control flow and triggers

**Domain:** dbde-04 — Task 4.1, 4.2, 4.3, 4.4
**Verified:** 2026-11-03
**Concepts:** lakeflow jobs, task graph, retries, conditional task, for each task, task values, scheduled trigger, file arrival trigger, table update trigger, continuous trigger

> Seed note. Scope is from the official exam guide; deepen the task-type detail from
> the linked docs before sealing hard items.

## Why this is on the exam

16% of the exam, and the questions are almost always operational: a pipeline needs to
run when something happens, or needs to not run when nothing happened. Trigger choice
is the single highest-yield idea here.

## Scope — official objectives

| Task | Objective (verbatim from the exam guide) |
|---|---|
| 4.1 | Implement control flows (retries and conditional tasks such as branching and looping) using Lakeflow Jobs for pipeline orchestration |
| 4.2 | Configure common tasks (notebook, SQL query, dashboard, and pipeline tasks) and their dependencies using Lakeflow Jobs and its DAG-based task graph |
| 4.3 | Implement job schedules using Lakeflow Jobs with an understanding of trigger types (scheduled, file arrival, and table update) |
| 4.4 | Choose between time-based and data-driven triggers based on data availability and pipeline dependencies |

## Choosing a trigger

| Situation | Trigger |
|---|---|
| Data lands on a predictable clock | **Scheduled** (cron) |
| Files arrive at unpredictable intervals and you want to process each drop soon after it lands, without paying for idle polling | **File arrival** |
| A downstream job should run when an upstream table is updated | **Table update** |
| The pipeline must run essentially without gaps | **Continuous** |
| A human decides | **Manual** |

The exam's own sample question contrasts a 5-minute poll against a file arrival
trigger for a vendor that uploads "sometimes several files within an hour, sometimes
nothing for most of a day" — file arrival wins because polling burns compute on empty
runs.

## Control flow

- **Retries** are configured per task, with a retry count and interval.
- **Conditional (`If/else`) tasks** branch the graph on a condition.
- **For each** tasks loop a task over a list of inputs.
- A task's **dependency condition** (run if all succeeded / at least one failed /
  all done, etc.) decides whether a downstream task runs at all.
- **Task values** pass small values from one task to a later one in the same run.

## Traps

- **Trap:** a task that fails with status **Timed Out** is hitting the *task run
  duration threshold*, not the cluster auto-termination setting and not max concurrent
  runs. Raise the duration threshold.
- **Trap:** "max concurrent runs" controls overlapping *job* runs, not how long a task
  may take.
- **Trap:** continuous is not the cheap answer for bursty arrivals — it keeps compute
  alive through the quiet periods.
- **Trap:** retries do not fix a deterministic failure. If the scenario says the same
  error recurs, retries are a distractor.

## Verify before sealing

- [Lakeflow Jobs](https://docs.databricks.com/aws/en/jobs/)
- [Data Engineer Associate exam guide](https://www.databricks.com/learn/certification/data-engineer-associate)
