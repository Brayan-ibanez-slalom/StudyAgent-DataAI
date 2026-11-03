# Fundamentals of gen AI

**Domain:** gcgenai-01 — Task 1.1, 1.2, 1.3, 1.4
**Verified:** 2026-11-03
**Concepts:** foundation model, multimodal, diffusion model, large language model, supervised, unsupervised, reinforcement, ml lifecycle, structured data, unstructured data, labeled data, gemini, gemma, imagen, veo

> Seed note. Scope is from the official exam guide; deepen the model-family detail from
> the linked docs before sealing hard items.

## Why this is on the exam

~30% of the exam — the second-largest section. It is vocabulary and judgement, not
implementation: the exam is for a leader who must choose well and explain why.

## Scope — official objectives

| Task | Objective (verbatim from the exam guide) |
|---|---|
| 1.1 | Describe core generative AI (gen AI) concepts and use cases |
| 1.2 | Describe how various data types are used in gen AI and the business implications |
| 1.3 | Identify the core layers of the gen AI landscape and the business implications |
| 1.4 | Identify the use cases and strengths of Google's foundation models |

## The five layers of the gen AI landscape

The guide names them explicitly, and questions are built on telling them apart:

| Layer | What sits there |
|---|---|
| **Infrastructure** | Compute, accelerators, data centres |
| **Models** | The foundation models themselves |
| **Platforms** | Tooling to build, tune, deploy and govern |
| **Agents** | Systems that use models plus tools to pursue goals |
| **Applications** | What the end user actually touches |

## Google's foundation models

| Model | Use for |
|---|---|
| **Gemini** | General multimodal reasoning across text, images, audio, video |
| **Gemma** | Open models you can run and customize yourself |
| **Imagen** | Image generation |
| **Veo** | Video generation |

## Choosing a foundation model

The guide lists the criteria: **modality, context window, security, availability and
reliability, cost, performance, and the ability to fine-tune or customize.** A question
that stresses one of those words is pointing at the answer.

## Data types

| Distinction | Means |
|---|---|
| Structured vs unstructured | Fixed schema (tables) vs none (documents, images, audio, video) |
| Labeled vs unlabeled | Carries the answer already vs does not — supervised learning needs labels |

Data quality attributes the guide names: **completeness, consistency, relevance,
availability, cost, format.**

## Traps

- **Trap:** conflating *machine learning approaches* (supervised, unsupervised,
  reinforcement) with *gen AI techniques* (prompting, grounding, fine-tuning).
- **Trap:** treating "multimodal" as "handles images". It means more than one modality,
  input or output.
- **Trap:** answering a *business implication* question with a technical mechanism. This
  exam rewards the business consequence.
- **Trap:** assuming the largest model is the right choice. Modality, cost and context
  window usually decide it.

## Verify before sealing

- [What is generative AI?](https://cloud.google.com/learn/what-is-generative-ai)
- [Generative AI on Vertex AI overview](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/overview)
- [Google models](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/models)
- [Generative AI Leader exam guide](https://cloud.google.com/learn/certification/generative-ai-leader)
