# dbde-02 — Data Ingestion and Loading

**Exam:** Databricks Certified Data Engineer Associate
**Weight:** not published by dbt Labs. Every question scores one point.
**Provenance of this domain:** Databricks Data Engineer Associate exam guide, Section 2 (21%)

## Tasks

| Task | Title |
|---|---|
| 2.1 | Enable and detail data ingestion patterns, including batch, streaming, and incremental loading, and import data from sources such as local files, Lakeflow Connect standard connectors, and Lakeflow Connect managed connectors |
| 2.2 | Use the COPY INTO command to incrementally load files from cloud object storage (ADLS/S3/GCS) into Unity Catalog-governed tables |
| 2.3 | Use Auto Loader with schema enforcement and schema evolution in batch modes (for example, directory listing or file notification) to land data into Unity Catalog-governed tables |
| 2.4 | Configure Lakeflow Connect to reliably ingest data from diverse enterprise sources into Unity Catalog-governed tables |
| 2.5 | Use JDBC/ODBC or REST clients in notebooks to land data into cloud storage or directly into Unity Catalog-governed tables, usually orchestrated and scheduled with Lakeflow Jobs |
| 2.6 | Prioritize between Auto Loader, Lakeflow Connect (standard and managed connectors), partner connectors, and other ingestion methods based on technical requirements such as data volume, ingestion frequency, data types, and governance needs with Unity Catalog |
| 2.7 | Ingest semi-structured and unstructured data (for example, JSON and nested data) via Lakeflow Connect and other managed connectors into Unity Catalog-governed Delta tables |

## Notes in this folder

One `.md` per concept, kebab-case. Every note must carry:

```
# <Title>

**Domain:** dbde-02 — Task 2.1
**Verified:** YYYY-MM-DD
**Concepts:** comma, separated, lookup, keys
```

Then rebuild the index: `python3 scripts/build_topic_index.py`

See [knowledge/README.md](../../README.md) for the full note contract.
