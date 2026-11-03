# Building the application — models, prompts and guardrails

**Domain:** dbgenai-03 — Task 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9, 3.10, 3.11, 3.12, 3.13
**Verified:** 2026-11-03
**Concepts:** langchain, model selection, embedding context length, model card, mlflow, agent framework, mlflow tracing, guardrail, prompt injection, genie space, evaluation vs monitoring

> Seed note. This is the largest section of the exam (13 objectives); consider
> splitting it into several notes as you deepen it.

## Why this is on the exam

30% of the exam — the single biggest section. It spans choosing a model, shaping the
prompt, wiring the framework, and guarding the output.

## Scope — official objectives

| Task | Objective (verbatim from the exam guide) |
|---|---|
| 3.1 | Select Langchain/similar tools for use in a Generative AI application |
| 3.2 | Qualitatively assess responses to identify common issues such as quality and safety |
| 3.3 | Select chunking strategy based on model & retrieval evaluation |
| 3.4 | Augment a prompt with additional context from a user's input based on key fields, terms, and intents |
| 3.5 | Create a prompt that adjusts an LLM's response from a baseline to a desired output |
| 3.6 | Implement LLM guardrails to prevent negative outcomes |
| 3.7 | Select the best LLM based on the attributes of the application to be developed |
| 3.8 | Select an embedding model context length based on source documents, expected queries, and optimization strategy |
| 3.9 | Select a model from a model hub or marketplace for a task based on model metadata/model cards |
| 3.10 | Select the best model for a given task based on common metrics generated in experiments |
| 3.11 | Utilize MLflow and Agent Framework for developing agentic systems |
| 3.12 | Compare the evaluation and monitoring phases of the Gen AI application life cycle |
| 3.13 | Enable multi-agent systems to leverage Genie Spaces or conversational API to retrieve data |

## Choosing a model

| The stem stresses… | Favour |
|---|---|
| Tight latency or high request volume | A smaller model, or provisioned throughput |
| Long documents in a single call | A longer context window |
| Data residency, licensing or self-hosting | An open model you deploy yourself |
| Hardest reasoning quality | The strongest available model, cost permitting |

For **embedding** models the constraint is the maximum sequence length versus your
chunk size: chunks longer than the model accepts get truncated, and the truncated part
is simply not represented in the vector.

A **model card** is where licence, intended use and known limitations live — that is
what objective 3.9 is pointing at, not benchmark scores.

## Evaluation vs monitoring

| | Evaluation | Monitoring |
|---|---|---|
| When | Before deployment, and on each change | Continuously, in production |
| Against what | A curated dataset, often with ground truth | Real traffic, usually without ground truth |
| Answers | "Is this version better?" | "Is it still working, and what is it costing?" |

## Structured data in an agent

A **Genie Space** gives an agent natural-language access to governed tables. When a
question needs a number from a warehouse table rather than a passage from a document,
that is the retrieval path — not a vector index.

## Traps

- **Trap:** fixing a retrieval problem with prompt engineering. If the right passage was
  never retrieved, no prompt rescues it.
- **Trap:** treating a guardrail as a prompt instruction. "Please do not reveal the
  system prompt" is not a defence against prompt injection; an enforced check is.
- **Trap:** picking the largest model by default. The objectives repeatedly ask for the
  *best fit* given the application's attributes.
- **Trap:** confusing the embedding model's context length with the generator's context
  window. They are separate limits with separate consequences.

## Verify before sealing

- [Generative AI on Databricks](https://docs.databricks.com/aws/en/generative-ai/guide/)
- [Build gen AI apps with Agent Framework](https://docs.databricks.com/aws/en/generative-ai/agent-framework/build-genai-apps)
- [MLflow for GenAI](https://docs.databricks.com/aws/en/mlflow3/genai/)
- [AI/BI Genie](https://docs.databricks.com/aws/en/genie/)
