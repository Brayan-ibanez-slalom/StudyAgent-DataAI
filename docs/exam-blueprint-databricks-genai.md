# Databricks Certified Generative AI Engineer Associate — Official Blueprint

Transcribed from the **official Databricks exam guide** (updated 2026-03-18). Track id
`dbgenai`. Section titles and objective text are Databricks'; task numbering (`N.M`) is
ours, assigned in published order.

- Certification page: <https://www.databricks.com/learn/certification/genai-engineer-associate>
- Exam guide PDF: <https://www.databricks.com/sites/default/files/2026-10/databricks-certified-gen-ai-associate-exam-guide-august-2026.pdf>
- Authoritative docs: <https://docs.databricks.com>

## Logistics (published)

| | |
|---|---|
| Scored questions | 45 (multiple-choice and multiple-selection) |
| Unscored items | Up to 10, unmarked, time already allowed for |
| Time limit | 90 minutes |
| Registration fee | USD 200 |
| Delivery | Online proctored or test center |
| Languages | English, Japanese, Brazilian Portuguese (pt-BR), Korean |
| Test aides | None allowed |
| Prerequisites | None; related training recommended |
| Recommended experience | 6+ months building generative AI solutions |
| Validity | 2 years |

**Passing score is NOT published.** Do not quote one.

Machine learning code in the exam is Python; non-ML workflow code may be SQL.

## Section weighting (published — these ARE facts)

| Domain | Section | Weight | Knowledge folder |
|---|---|---|---|
| `dbgenai-01` | Design Applications | 14% | `knowledge/dbgenai/01-design-applications` |
| `dbgenai-02` | Data Preparation | 14% | `knowledge/dbgenai/02-data-preparation` |
| `dbgenai-03` | Application Development | 30% | `knowledge/dbgenai/03-application-development` |
| `dbgenai-04` | Assembling and Deploying Applications | 22% | `knowledge/dbgenai/04-assembling-and-deploying-applications` |
| `dbgenai-05` | Governance | 8% | `knowledge/dbgenai/05-governance` |
| `dbgenai-06` | Evaluation and Monitoring | 12% | `knowledge/dbgenai/06-evaluation-and-monitoring` |

At 45 scored questions these imply roughly: 6 / 6 / 14 / 10 / 4 / 5.

Note the shape: **Application Development and Assembling/Deploying are over half the
exam.** Governance is the cheapest section to secure at 8% across only four objectives.

## Objectives

Held verbatim in
[mcp-server/study_agent_mcp/exam_config.py](../mcp-server/study_agent_mcp/exam_config.py)
and surfaced by `exam_facts(track="dbgenai")`.

## Confusion pairs specific to this track

| Do not confuse | Because |
|---|---|
| evaluation vs monitoring | Pre-deployment on a curated set vs continuous on live traffic |
| judges needing ground truth vs not | Correctness needs a reference answer; groundedness does not |
| MLflow tracing vs inference tables | Explains one run vs records the population |
| serving endpoint vs `ai_query()` | Real-time request vs batch scoring a table |
| Vector Search index vs persistent datastore | Similarity retrieval vs agent memory and state |
| retrieval failure vs generation failure | A prompt fix cannot rescue a chunk never retrieved |
| embedding context length vs generator context window | Two separate limits, two separate failure modes |
