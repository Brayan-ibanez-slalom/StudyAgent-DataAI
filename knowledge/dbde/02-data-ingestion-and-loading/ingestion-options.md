# Choosing and configuring an ingestion path

**Domain:** dbde-02 — Task 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7
**Verified:** 2026-11-03
**Concepts:** auto loader, cloudFiles, copy into, lakeflow connect, schema evolution, _rescued_data, directory listing, file notification, semi-structured

> Seed note. Scope is from the official exam guide; deepen the per-option detail from
> the linked docs before sealing hard items.

## Why this is on the exam

At 21% this is the second-largest section, and nearly every question is a *choose
between* question. You are given a volume, a cadence, a source type and a governance
requirement, and asked which ingestion mechanism fits.

## Scope — official objectives

| Task | Objective (verbatim from the exam guide) |
|---|---|
| 2.1 | Enable and detail data ingestion patterns, including batch, streaming, and incremental loading, and import data from sources such as local files, Lakeflow Connect standard connectors, and Lakeflow Connect managed connectors |
| 2.2 | Use the COPY INTO command to incrementally load files from cloud object storage (ADLS/S3/GCS) into Unity Catalog-governed tables |
| 2.3 | Use Auto Loader with schema enforcement and schema evolution in batch modes (for example, directory listing or file notification) to land data into Unity Catalog-governed tables |
| 2.4 | Configure Lakeflow Connect to reliably ingest data from diverse enterprise sources into Unity Catalog-governed tables |
| 2.5 | Use JDBC/ODBC or REST clients in notebooks to land data into cloud storage or directly into Unity Catalog-governed tables, usually orchestrated and scheduled with Lakeflow Jobs |
| 2.6 | Prioritize between Auto Loader, Lakeflow Connect (standard and managed connectors), partner connectors, and other ingestion methods based on technical requirements such as data volume, ingestion frequency, data types, and governance needs with Unity Catalog |
| 2.7 | Ingest semi-structured and unstructured data (for example, JSON and nested data) via Lakeflow Connect and other managed connectors into Unity Catalog-governed Delta tables |

## Which ingestion mechanism

| Situation | Use |
|---|---|
| New files land continuously in cloud storage, at scale | **Auto Loader** (`cloudFiles`) — it tracks processed files, so it never reprocesses one |
| A bounded, idempotent SQL load of files you control | **COPY INTO** — re-running skips files already loaded |
| An enterprise SaaS or database source (Salesforce, SQL Server, Workday) | **Lakeflow Connect** managed connector |
| A source with no connector, reachable over JDBC/ODBC or REST | A notebook client, scheduled by a Lakeflow Job |

Rough rule: **COPY INTO** suits thousands of files; **Auto Loader** suits millions and
is the default once file counts grow or arrival is continuous.

## Auto Loader schema handling

- `cloudFiles.schemaLocation` is where the inferred schema and the processed-file
  record live. Without it there is no incremental state.
- **Schema evolution** adds newly seen columns to the target rather than failing.
- Values that do not fit the schema land in `_rescued_data` instead of being dropped —
  a favourite exam detail, because "the data is silently lost" is the wrong answer.
- File discovery is either **directory listing** (simple, fine at modest scale) or
  **file notification** (uses cloud notification services; scales to very large
  directories).

## Traps

- **Trap:** COPY INTO and Auto Loader are both incremental and both idempotent. The
  discriminator is scale and arrival pattern, not "which one avoids duplicates".
- **Trap:** `merge` semantics are not part of either loader. De-duplicating on a
  business key is a transformation step, not an ingestion setting.
- **Trap:** Databricks audit logs are delivered as **JSON**, typically within 15 minutes
  of the event once delivery begins, and a later delivery **can overwrite** an existing
  file — so a pipeline over them must tolerate overwrites rather than assume files are
  immutable. (Stated in the exam guide's own answer key.)
- **Trap:** choosing a connector because it is newest. The objective says prioritize on
  volume, frequency, data type and governance need.

## Verify before sealing

- [Ingest data into a Databricks lakehouse](https://docs.databricks.com/aws/en/ingestion/)
- [Auto Loader](https://docs.databricks.com/aws/en/ingestion/cloud-object-storage/auto-loader/)
- [COPY INTO](https://docs.databricks.com/aws/en/ingestion/cloud-object-storage/copy-into/)
- [Lakeflow Connect](https://docs.databricks.com/aws/en/ingestion/lakeflow-connect/)
