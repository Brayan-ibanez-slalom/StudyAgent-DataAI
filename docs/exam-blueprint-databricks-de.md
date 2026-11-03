# Databricks Certified Data Engineer Associate — Official Blueprint

Transcribed from the **official Databricks exam guide** (updated 2026-08-06). Track id
`dbde`. Section titles and objective text are Databricks'; task numbering (`N.M`) is
ours, assigned in published order, because Databricks prints objectives as unnumbered
bullets.

- Certification page: <https://www.databricks.com/learn/certification/data-engineer-associate>
- Exam guide PDF: <https://www.databricks.com/sites/default/files/2026-10/Databricks-Certified-Data-Engineer-Associate-Exam-Guide-August-2026.pdf>
- Authoritative docs: <https://docs.databricks.com>

## Logistics (published)

| | |
|---|---|
| Scored questions | 45 |
| Unscored items | Up to 10, unmarked, time already allowed for |
| Time limit | 90 minutes |
| Question types | Multiple choice |
| Registration fee | USD 200 |
| Delivery | Online proctored or test center |
| Languages | English, Japanese, Brazilian Portuguese (pt-BR), Korean |
| Test aides | None allowed |
| Prerequisites | None; related training recommended |
| Recommended experience | Six months hands-on with the Databricks Platform |
| Validity | 2 years |

**Passing score is NOT published.** Databricks states no cut score for this exam. Do
not quote one.

Code in the exam is given in SQL where possible, otherwise Python.

## Section weighting (published — these ARE facts)

| Domain | Section | Weight | Knowledge folder |
|---|---|---|---|
| `dbde-01` | Databricks Intelligence Platform | 6% | `knowledge/dbde/01-databricks-intelligence-platform` |
| `dbde-02` | Data Ingestion and Loading | 21% | `knowledge/dbde/02-data-ingestion-and-loading` |
| `dbde-03` | Data Transformation and Modeling | 22% | `knowledge/dbde/03-data-transformation-and-modeling` |
| `dbde-04` | Working with Lakeflow Jobs | 16% | `knowledge/dbde/04-working-with-lakeflow-jobs` |
| `dbde-05` | Implementing CI/CD | 10% | `knowledge/dbde/05-implementing-ci-cd` |
| `dbde-06` | Troubleshooting, Monitoring, and Optimization | 10% | `knowledge/dbde/06-troubleshooting-monitoring-and-optimization` |
| `dbde-07` | Governance and Security | 15% | `knowledge/dbde/07-governance-and-security` |

Unlike the dbt tracks, these percentages come from the vendor and may be stated as
fact. At 45 scored questions they imply roughly: 3 / 9 / 10 / 7 / 5 / 5 / 7.

## Objectives

The full objective list per section is held verbatim in
[mcp-server/study_agent_mcp/exam_config.py](../mcp-server/study_agent_mcp/exam_config.py)
and surfaced by `exam_facts(track="dbde")`. Read it there rather than duplicating it
here — duplication is how outlines rot.

## Naming churn to watch

Databricks renamed several surfaces and the guide carries both names:

| Older name | Current name |
|---|---|
| Databricks Repos | Databricks Git folders |
| Databricks Asset Bundles (DABs) | Declarative Automation Bundles |
| Delta Live Tables | Lakeflow Declarative Pipelines |
| Jobs / Workflows | Lakeflow Jobs |

Do not eliminate an option purely because it uses the older label.

## Question formats

The vendor states multiple choice only. The repo still supports all seven formats;
authoring to `multiple_choice` and `multiple_response` keeps practice faithful to the
real exam.
