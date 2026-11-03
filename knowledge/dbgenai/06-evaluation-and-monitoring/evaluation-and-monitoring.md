# Evaluating and monitoring a deployed gen AI system

**Domain:** dbgenai-06 — Task 6.1, 6.2, 6.3, 6.4, 6.5, 6.6, 6.7, 6.8, 6.9
**Verified:** 2026-11-03
**Concepts:** mlflow evaluate, mlflow tracing, llm judge, ground truth, groundedness, inference table, agent monitoring, ai gateway, usage table, rate limiting, custom scorer

> Seed note. Scope is from the official exam guide; deepen the judge and scorer detail
> from the linked docs before sealing hard items.

## Why this is on the exam

12% of the exam, and it pairs directly with objective 3.12. The recurring question is
which instrument answers which question.

## Scope — official objectives

| Task | Objective (verbatim from the exam guide) |
|---|---|
| 6.1 | Select an LLM choice (size and architecture) based on a set of quantitative evaluation metrics |
| 6.2 | Select key metrics to monitor for a specific LLM deployment scenario |
| 6.3 | Evaluate agent performance using MLflow scoring and tracing |
| 6.4 | Use inference logging to assess deployed RAG application performance |
| 6.5 | Use Databricks features to control LLM costs |
| 6.6 | Use inference tables and Agent Monitoring to track a live LLM endpoint |
| 6.7 | Identify evaluation judges that require ground truth |
| 6.8 | Use AI Gateway (Inference Tables, Usage Tables, and rate limiting) to track an LLM or agent deployed via Agent Framework |
| 6.9 | Use Databricks custom Scorers for evaluating agents and LLMs |

## Which instrument

| Question | Instrument |
|---|---|
| Which step of the agent produced this answer? | **MLflow tracing** — spans for each retrieval, tool call and model call |
| Is candidate B better than candidate A on my dataset? | **MLflow evaluation** with scorers/judges |
| What is actually hitting the endpoint in production? | **Inference tables** |
| Who is consuming how much, and can I cap it? | **AI Gateway** usage tables and rate limiting |
| Is my own definition of "correct" being met? | A **custom scorer** |

## Judges and ground truth

Objective 6.7 asks you to tell these apart:

- **Needs ground truth** — anything comparing the answer to a known correct answer
  (correctness, answer similarity).
- **Does not need ground truth** — judges that score the answer against the *retrieved
  context* or the question itself (groundedness, relevance, safety). These work on
  live traffic, where no reference answer exists.

That is also why production monitoring leans on the second group.

## Controlling cost

Rate limiting, usage tracking, smaller models for easy requests, caching, and
provisioned throughput where volume is predictable.

## Traps

- **Trap:** proposing a correctness judge for production monitoring. There is no ground
  truth on live traffic.
- **Trap:** treating tracing and inference tables as interchangeable. Tracing explains a
  single run; inference tables record the population.
- **Trap:** evaluating only the final answer when the failure is in retrieval. Trace the
  steps.
- **Trap:** picking a model on benchmark reputation when objective 6.1 asks for a choice
  driven by *your* quantitative metrics.

## Verify before sealing

- [Agent evaluation](https://docs.databricks.com/aws/en/generative-ai/agent-evaluation/)
- [MLflow for GenAI](https://docs.databricks.com/aws/en/mlflow3/genai/)
- [Mosaic AI Gateway](https://docs.databricks.com/aws/en/ai-gateway/)
- [Model serving](https://docs.databricks.com/aws/en/machine-learning/model-serving/)
