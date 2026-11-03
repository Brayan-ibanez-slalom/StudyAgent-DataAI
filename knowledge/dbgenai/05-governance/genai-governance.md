# Governance for gen AI applications

**Domain:** dbgenai-05 — Task 5.1, 5.2, 5.3, 5.4
**Verified:** 2026-11-03
**Concepts:** masking, pii redaction, guardrail, prompt injection, jailbreak, licensing, problematic text, ai gateway

> Seed note. Scope is from the official exam guide; deepen the AI Gateway guardrail
> detail from the linked docs before sealing hard items.

## Why this is on the exam

Only 8% — the smallest section — but it is cheap to secure, and the distractors are
very distinguishable once you know the four objectives.

## Scope — official objectives

| Task | Objective (verbatim from the exam guide) |
|---|---|
| 5.1 | Use masking techniques as guard rails to meet a performance objective |
| 5.2 | Select guardrail techniques to protect against malicious user inputs to a Gen AI application |
| 5.3 | Use legal/licensing requirements for data sources to avoid legal risk |
| 5.4 | Recommend an alternative for problematic text mitigation in a data source feeding a GenAI application |

## Which control

| Risk | Control |
|---|---|
| Sensitive values reaching the model or the response | **Masking / redaction** before the text is embedded or sent |
| Hostile input trying to override instructions | **Input guardrails** — validation and filtering, enforced outside the prompt |
| Unsafe or off-policy output | **Output guardrails** |
| A source you are not licensed to use | Remove or replace the source — not a technical control |
| A source containing toxic or biased text | Filter it, or substitute a cleaner source (objective 5.4) |

## Prompt injection

Hostile instructions can arrive in **user input or in retrieved documents**. A RAG
application therefore has two injection surfaces, not one. Defences that only inspect
the user's message leave the retrieved-content surface open — a reliable discriminator
between a good and a weak option.

## Traps

- **Trap:** a stronger system prompt treated as a guardrail. Instructions are advisory;
  guardrails are enforced.
- **Trap:** masking applied only on display, after the raw value has already been sent
  to the model or written to a log.
- **Trap:** answering a licensing question with a technical mitigation. If the data may
  not be used, no amount of filtering makes it usable.
- **Trap:** forgetting that retrieved documents are untrusted input too.

## Verify before sealing

- [Mosaic AI Gateway](https://docs.databricks.com/aws/en/ai-gateway/)
- [Generative AI on Databricks](https://docs.databricks.com/aws/en/generative-ai/guide/)
