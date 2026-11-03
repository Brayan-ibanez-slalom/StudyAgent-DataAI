# Improving gen AI model output

**Domain:** gcgenai-03 — Task 3.1, 3.2, 3.3
**Verified:** 2026-11-03
**Concepts:** knowledge cutoff, hallucination, bias, grounding, rag, prompt engineering, zero-shot, one-shot, few-shot, role prompting, prompt chaining, chain-of-thought, react, fine-tuning, human in the loop, temperature, top-p, safety settings

> Seed note. Scope is from the official exam guide; deepen the sampling-parameter
> detail from the linked docs before sealing hard items.

## Why this is on the exam

~20% of the exam, and the most *technique*-flavoured section in an otherwise strategic
exam. The recurring question: the output is wrong in a specific way — what fixes it?

## Scope — official objectives

| Task | Objective (verbatim from the exam guide) |
|---|---|
| 3.1 | Describe how to proactively overcome foundation model limitations |
| 3.2 | Describe prompt engineering techniques and how they drive better results |
| 3.3 | Identify grounding techniques and their use cases |

## Which technique for which failure

| The output is… | Because | Fix |
|---|---|---|
| Confidently wrong about a recent fact | Knowledge cutoff | **Grounding / RAG** |
| Inventing specifics not in any source | Hallucination | **Grounding**, plus citations |
| Right content, wrong shape or tone | Under-specified instruction | **Prompt engineering** — role prompting, examples |
| Failing a multi-step reasoning task | No intermediate reasoning | **Chain-of-thought**, or **prompt chaining** |
| Needing to look things up and act | Single-shot prompting | **ReAct** |
| Consistently off-domain in style or format | The base model has not seen your task | **Fine-tuning** |
| Too risky to ship unreviewed | Consequence, not accuracy | **Human in the loop** |

## Prompting ladder

**Zero-shot** (no examples) → **one-shot** (one example) → **few-shot** (several). Add
examples when the task is hard to describe but easy to demonstrate. **Role prompting**
sets a persona; **prompt chaining** splits a task across several prompts.

## Grounding

The guide distinguishes grounding against **first-party enterprise data**, **third-party
data**, and **world data**. Google Cloud's named grounding offerings are **prebuilt RAG
with Agent Search**, **RAG APIs**, and **grounding with Google Search**.

## Sampling parameters

| Parameter | Effect |
|---|---|
| **Temperature** | Higher is more varied, lower is more deterministic |
| **Top-p** (nucleus sampling) | Restrict choices to the most probable tokens summing to p |
| **Token count / output length** | Caps how much is generated |
| **Safety settings** | Thresholds for blocking harmful content |

## Continuous monitoring (3.1)

The guide names: automatic model upgrades, KPIs, security patches and updates,
versioning, performance tracking, and drift monitoring.

## Traps

- **Trap:** fine-tuning offered as the fix for stale facts. Fine-tuning teaches *style
  and task*; it does not keep knowledge current. Grounding does.
- **Trap:** lowering temperature to stop hallucinations. It makes output more
  predictable, not more truthful.
- **Trap:** treating RAG and grounding as unrelated. RAG is one way to ground.
- **Trap:** adding few-shot examples to fix a factual gap.

## Verify before sealing

- [Prompt design strategies](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/prompt-design-strategies)
- [Grounding overview](https://cloud.google.com/vertex-ai/generative-ai/docs/grounding/overview)
- [Content generation parameters](https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/content-generation-parameters)
