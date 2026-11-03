# Designing a gen AI application on Databricks

**Domain:** dbgenai-01 — Task 1.1, 1.2, 1.3, 1.4, 1.5, 1.6
**Verified:** 2026-11-03
**Concepts:** prompt design, structured output, chain component, tool calling, multi-stage reasoning, agent bricks, knowledge assistant, multiagent supervisor, information extraction

> Seed note. Scope is from the official exam guide; deepen the Agent Bricks detail from
> the linked docs before sealing hard items.

## Why this is on the exam

14% of the exam, and it is the section that decides the *shape* of the solution. The
recurring question is: given this business requirement, what pieces does the pipeline
need, and in what order.

## Scope — official objectives

| Task | Objective (verbatim from the exam guide) |
|---|---|
| 1.1 | Design a prompt that elicits a specifically formatted response |
| 1.2 | Select model tasks to accomplish a given business requirement |
| 1.3 | Select chain components for a desired model input and output |
| 1.4 | Translate business use case goals into a description of the desired inputs and outputs for the AI pipeline |
| 1.5 | Define and order tools that gather knowledge or take actions for multi-stage reasoning |
| 1.6 | Determine how and when to use Agent Bricks (Knowledge Assistant, Multiagent Supervisor, Information Extraction) to solve problems |

## Which Agent Bricks offering

| Requirement | Use |
|---|---|
| Answer questions over a corpus of documents | **Knowledge Assistant** |
| Route a request across several specialised agents | **Multiagent Supervisor** |
| Pull structured fields out of unstructured documents | **Information Extraction** |

## Designing the chain

A minimal retrieval chain is: **input → retriever → prompt template → LLM → output
parser**. Each objective in this section maps to one of those boxes. If a stem names a
need the chain has no box for — say, taking an action in another system — that is a
**tool**, not a prompt change.

**Ordering tools** matters: gather knowledge before acting on it. A tool that writes
should not run before the tool that verifies.

## Traps

- **Trap:** asking the model nicely for JSON is weaker than constraining the output.
  When the stem stresses a *specific* format, prefer the option that enforces it rather
  than the one that requests it.
- **Trap:** reaching for a custom agent when a prebuilt Agent Bricks offering covers
  the requirement — and the reverse, forcing a prebuilt offering onto a requirement it
  does not cover.
- **Trap:** confusing a *model task* (summarize, classify, extract) with a *pipeline
  component*. 1.2 and 1.3 are different questions.

## Verify before sealing

- [Generative AI on Databricks](https://docs.databricks.com/aws/en/generative-ai/guide/)
- [Agent Bricks](https://docs.databricks.com/aws/en/generative-ai/agent-bricks/)
- [GenAI Engineer Associate exam guide](https://www.databricks.com/learn/certification/genai-engineer-associate)
