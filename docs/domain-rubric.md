# Domain classification rubric

How to decide which `domain` and `blueprint_task` a question belongs to. Consistency
matters more than perfection: `coverage_report` and the `weakest` drill mode both depend
on stable labels.

Domains are the **official topic outlines** from each vendor's study or exam guide,
defined in [exam_config.py](../mcp-server/study_agent_mcp/exam_config.py). Ids are
globally unique across all five tracks: `ae-01` … `ae-07`, `arch-01` … `arch-08`,
`dbde-01` … `dbde-07`, `dbgenai-01` … `dbgenai-06`, `gcgenai-01` … `gcgenai-04`.
A question therefore never needs a separate track column.

---

## Decision order

1. **Which exam?** The vendor named in the stem decides the track first:
   - dbt model code, tests, state → `ae-*`; dbt account administration (connections,
     environments, jobs, permissions, catalog) → `arch-*`
   - Databricks data engineering (ingestion, Spark, Jobs, Unity Catalog) → `dbde-*`
   - Databricks LLM/RAG/agent work (Vector Search, MLflow, serving, evaluation)
     → `dbgenai-*`
   - Google Cloud gen AI strategy, offerings and responsible AI → `gcgenai-*`
2. **What does the question actually test?** Label by the knowledge required to answer,
   not by the nouns in the stem.
3. **Which sub-topic?** Use `exam_config.classify_task` as a first guess, then override.
   Store it in `blueprint_task`.

> Unity Catalog appears in both `dbde` and `dbgenai`. Governance *of tables and
> privileges* is `dbde-07`; governance *of a gen AI application* (masking as a
> guardrail, licensing, prompt injection) is `dbgenai-05`.

---

## The single most common mistake

**`ae-01` is enormous.** It holds 14 of the AE exam's 31 sub-topics — materializations,
incremental strategy, snapshots, packages, Python models, `grants`, `dbt_project.yml`,
the DAG, `--empty`, `--sample`, microbatch, and the core commands.

The instinct to spread those across "nicer" domains is exactly what produced the
repo's earlier, wrong, derived structure. **Resist it.** If a question is about how a
model is built, it is `ae-01` unless it is specifically about governance, tests,
debugging, external dependencies, or state.

---

## AE tie-breakers

| If a question could be… | Choose | Because |
|---|---|---|
| `ae-01` (materializations 1.2) or `ae-01` (incremental 1.11) | 1.11 when the answer turns on a *strategy* choice; 1.2 when it turns on which of the five materializations | |
| `ae-01` (build 1.4) or `ae-04` (DAG failures 4.1) | `ae-04` when the answer is about what happens *after something fails* — skips, blocking, fail-fast | `ae-01` is "how do I run it", `ae-04` is "why did it stop" |
| `ae-01` (models) or `ae-02` (governance) | `ae-02` whenever a contract, model version, or YAML constraint decides the answer | Governance is a separate official topic, narrow on purpose |
| `ae-02` (contracts) or `ae-05` (tests) | `ae-02` for contracts/constraints (enforced by the platform at build time); `ae-05` for tests (queries that run after building) | This is the highest-value distinction on the exam |
| `ae-03` (debugging) or `ae-04` (pipelines) | `ae-03` for reading an error, compiled code, or YAML; `ae-04` for DAG-level failure management and `dbt clone` | `ae-03` is one node, `ae-04` is the graph |
| `ae-03` (flags 3.5) or `ae-01` (commands 1.4) | `ae-03` for behaviour-change flags and global configs; `ae-01` for the command itself | |
| `ae-05` (tests) or `ae-06` (external deps) | `ae-06` only for exposures and source freshness — everything else testing-shaped is `ae-05` | `ae-06` is two sub-topics, nothing more |
| `ae-01` (build 1.4) or `ae-07` (state 7.1) | `ae-07` when `state:modified`, `--defer`, `--favor-state`, or an artifact decides it | Selection-time, not build-time |
| `ae-04` (`dbt clone` 4.2) or `ae-07` (`dbt retry` 7.2) | Read carefully — these are genuinely in different official topics despite feeling like siblings | A known trap in the outline itself |

---

## Architect tie-breakers

| If a question could be… | Choose | Because |
|---|---|---|
| `arch-01` (connections) or `arch-03` (environments) | `arch-01` for account-level connection setup and OAuth; `arch-03` for environment-level credentials and deferral | Credential *precedence* between them is itself a good question — label it `arch-03` |
| `arch-01` (OAuth 1.4) or `arch-05` (SSO 5.5) | `arch-01` when it is about *warehouse* access tokens; `arch-05` when it is about *dbt account* login | Data-platform auth vs. workforce auth |
| `arch-03` (deferral 3.8) or `arch-04` (CI 4.1 / self-deferral 4.10 / which type 4.11) | `arch-03` for configuring an environment to *allow* deferral; `arch-04` for a job that *uses* it | Deferral spans four sub-topics — read which side is being configured |
| `arch-04` (jobs) or `arch-06` (monitoring) | `arch-06` only for notifications and webhooks; everything else about a job is `arch-04` | |
| `arch-05` (permission sets 5.2) or `arch-05` (licenses 5.3) | Licenses are what a seat *costs*; permission sets are what a group may *do* | Both in the same domain, but the distinction is heavily tested |
| `arch-07` (Mesh) or `arch-08` (Catalog) | `arch-07` for wiring projects together; `arch-08` for *finding* things through the Catalog UI/API | |
| `arch-04` (docs job 4.7) or `arch-08` (Catalog) | `arch-04` when the answer is about configuring the job that generates docs | |

---

## Databricks Data Engineer tie-breakers

| If a question could be… | Choose | Because |
|---|---|---|
| `dbde-01` (compute 1.2) or `dbde-04` (jobs 4.x) | `dbde-01` when the answer is *which compute*; `dbde-04` when it is *when and how the work is triggered* | |
| `dbde-02` (ingestion) or `dbde-03` (transformation) | `dbde-02` up to and including landing the data; `dbde-03` from the first read of a bronze table onward | De-duplicating on a business key is transformation, not ingestion |
| `dbde-03` (tuning 3.5) or `dbde-06` (bottlenecks 6.3) | `dbde-03` when a parameter is being set; `dbde-06` when a symptom is being diagnosed from the Spark UI | |
| `dbde-04` (job monitoring) or `dbde-06` (6.1 / 6.2) | `dbde-06` whenever the answer is read off run history or the Jobs UI to explain a failure or slowdown | |
| `dbde-05` (bundles) or `dbde-07` (service principals) | `dbde-07` when the answer turns on a privilege; `dbde-05` when it turns on promotion across targets | |
| `dbde-07` (managed vs external 7.1) or `dbde-01` (Delta 1.1) | `dbde-07` whenever `DROP` semantics, `LOCATION` or conversion decides it | |

---

## Databricks GenAI tie-breakers

| If a question could be… | Choose | Because |
|---|---|---|
| `dbgenai-01` (design) or `dbgenai-03` (development) | `dbgenai-01` when choosing *what the pipeline is*; `dbgenai-03` when building a piece of it | |
| `dbgenai-02` (chunking 2.1) or `dbgenai-03` (chunking 3.3) | `dbgenai-02` when the document structure decides it; `dbgenai-03` when an evaluation result decides it | The official outline really does list chunking twice |
| `dbgenai-03` (3.12 evaluation vs monitoring) or `dbgenai-06` | `dbgenai-03` only for the *conceptual comparison*; `dbgenai-06` for any concrete instrument | |
| `dbgenai-04` (serving) or `dbgenai-06` (monitoring) | `dbgenai-04` for standing it up; `dbgenai-06` for watching it afterwards | Inference tables are `dbgenai-06` |
| `dbgenai-05` (guardrails) or `dbgenai-03` (guardrails 3.6) | `dbgenai-03` for implementing one in the app; `dbgenai-05` when the hinge is governance, legal or malicious input | |

---

## Google GenAI Leader tie-breakers

| If a question could be… | Choose | Because |
|---|---|---|
| `gcgenai-01` (concepts) or `gcgenai-03` (techniques) | `gcgenai-01` for what something *is*; `gcgenai-03` for which technique *fixes a bad output* | |
| `gcgenai-02` (offerings) or `gcgenai-03` (grounding 3.3) | `gcgenai-02` when naming the product; `gcgenai-03` when the hinge is the technique itself | Prebuilt RAG with Agent Search appears in both — follow the hinge |
| `gcgenai-04` (secure AI 4.2) or `gcgenai-04` (responsible AI 4.3) | 4.2 for attack and misuse; 4.3 for harm from the system working as built | Same domain, most-tested distinction in it |
| `gcgenai-01` (choose a model 1.1/1.4) or `gcgenai-04` (choose a solution 4.1) | `gcgenai-01` when picking a *model*; `gcgenai-04` when picking and rolling out a *solution* | |

---

## Cross-track questions

`ae-02` (contracts, versions, constraints) overlaps with `arch-07` (model governance).
Split by perspective:

- **`ae-02`** — the model author declaring a contract or version on their own model.
- **`arch-07`** — the platform architect deciding what is `public` and wiring projects.

Knowledge notes for shared concepts live in the track whose depth they belong to and are
cross-linked. `build_topic_index.py` resolves `` `note.md` `` references across tracks,
so one note can back questions in both.

---

## Confidence

Stub ingesters record `domain_confidence` (the classifier's hit count). Anything under 2
should be reviewed by a human during sealing — `ingest_scan` sorts by ascending
confidence so the shakiest labels surface first.

If a question genuinely spans two domains, pick the one whose **decision hinge** it
tests and note the other in `notes`. Do not duplicate the question.

---

## Re-labelling

Correct both at seal time:

```
ingest_seal(..., domain="ae-05", blueprint_task="5.1")
```

Both are validated against `exam_config`, so a typo is rejected rather than silently
creating a phantom domain. `test_docs_consistency.py` additionally fails the build if any
doc or authored draft names a domain or task that does not exist.
