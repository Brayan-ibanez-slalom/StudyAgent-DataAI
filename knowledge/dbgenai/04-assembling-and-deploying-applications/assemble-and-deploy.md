# Assembling, registering and serving the application

**Domain:** dbgenai-04 — Task 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.8, 4.9, 4.10, 4.11, 4.12, 4.13, 4.14, 4.15
**Verified:** 2026-11-03
**Concepts:** pyfunc, model signature, input example, unity catalog model registry, vector search index, delta sync index, model serving, foundation model api, provisioned throughput, ai_query, mcp, databricks apps

> Seed note. Fifteen objectives sit under this section; split it as you deepen it.

## Why this is on the exam

22% of the exam. This is where the design becomes an artifact: logged, registered,
indexed, served and callable.

## Scope — official objectives

| Task | Objective (verbatim from the exam guide) |
|---|---|
| 4.1 | Code a chain using a pyfunc model with pre- and post-processing |
| 4.2 | Control access to resources from model serving endpoints |
| 4.3 | Code a simple chain according to requirements |
| 4.4 | Choose the basic elements needed to create a RAG application: model flavor, embedding model, retriever, dependencies, input examples, model signature |
| 4.5 | Register the model to Unity Catalog using MLflow |
| 4.6 | Create and query a Vector Search index |
| 4.7 | Identify how to serve an LLM application that leverages Foundation Model APIs |
| 4.8 | Explain the key concepts and components of Mosaic AI Vector Search |
| 4.9 | Identify batch inference workloads and apply ai_query() appropriately |
| 4.10 | Configure vector search for a particular solution based on number of embeddings, update frequency, latency, and cost requirements |
| 4.11 | Configure a persistent datastore to store and retrieve intermediate memory or structured information |
| 4.12 | Apply CI/CD best practices such as updating a Vector Search index, promoting prompts across environments, and testing individual components of an agent |
| 4.13 | Integrate managed, external, and custom MCP servers based on a given application requirements |
| 4.14 | Apply prompt version control and manage prompt lifecycle |
| 4.15 | Develop an appropriate interactive user facing interface for an agent usage scenario (Apps, Slack, Teams, etc.) |

## Real-time vs batch

| Requirement | Use |
|---|---|
| A user waits for the answer | A **serving endpoint** |
| Score a whole table, no user waiting | **`ai_query()`** in SQL — batch inference |

## Logging a chain

A `pyfunc` model is the wrapper to reach for when the thing you are logging is custom
code with pre- and post-processing around the model call. What you log with it matters:

- **model flavor** — how MLflow should load it back
- **model signature** and **input example** — the declared input/output schema
- **dependencies** — pinned so the serving environment reproduces yours
- the **retriever** and **embedding model** references for a RAG chain

Then register it to Unity Catalog under `catalog.schema.model`, and move versions with
**aliases** rather than hard-coding version numbers downstream.

## Vector Search sizing

Objective 4.10 names the four levers explicitly: **number of embeddings**, **update
frequency**, **latency**, and **cost**. A Delta sync index keeps itself in step with a
source table; how often it syncs is the freshness/cost trade-off.

## Traps

- **Trap:** using a real-time endpoint to score a whole table. That is what `ai_query()`
  is for, and the cost difference is the point of the question.
- **Trap:** omitting the model signature or dependencies and expecting serving to work.
  "It ran in my notebook" is the failure mode being tested.
- **Trap:** pinning a downstream app to a model *version* instead of an alias, then
  being unable to promote a new one without a code change.
- **Trap:** treating a vector index as a database. Intermediate memory and structured
  state belong in a persistent datastore (4.11), not in the index.

## Verify before sealing

- [Mosaic AI Vector Search](https://docs.databricks.com/aws/en/generative-ai/vector-search)
- [Model serving](https://docs.databricks.com/aws/en/machine-learning/model-serving/)
- [Foundation Model APIs](https://docs.databricks.com/aws/en/machine-learning/foundation-model-apis/)
- [Manage model lifecycle in Unity Catalog](https://docs.databricks.com/aws/en/machine-learning/manage-model-lifecycle/)
- [ai_query](https://docs.databricks.com/aws/en/large-language-models/ai-query) · [MCP](https://docs.databricks.com/aws/en/generative-ai/mcp/) · [Databricks Apps](https://docs.databricks.com/aws/en/dev-tools/databricks-apps/)
