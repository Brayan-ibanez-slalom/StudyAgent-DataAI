# Business strategy, secure AI and responsible AI

**Domain:** gcgenai-04 — Task 4.1, 4.2, 4.3
**Verified:** 2026-11-03
**Concepts:** gen ai solution types, business requirements, measure impact, secure ai framework, saif, iam, security command center, responsible ai, transparency, anonymization, pseudonymization, accountability, explainability

> Seed note. Scope is from the official exam guide; deepen SAIF and the security tools
> from the linked docs before sealing hard items.

## Why this is on the exam

~15% of the exam, and the section most aligned with the exam's stated audience: a
leader who influences adoption rather than implements it.

## Scope — official objectives

| Task | Objective (verbatim from the exam guide) |
|---|---|
| 4.1 | Describe the Google Cloud-recommended steps to successfully implement a transformational gen AI solution |
| 4.2 | Define secure AI and its importance in protecting AI systems from malicious attacks and misuse |
| 4.3 | Describe the importance of responsible AI in business |

## Implementing a solution (4.1)

The guide's sequence: recognise the **type** of gen AI solution needed (text, image,
code generation, personalized experience) → identify the **factors** that shape it
(business requirements, technical constraints) → **choose** the solution for the need →
**integrate** it into the organization → **measure the impact**.

The last step is the one candidates skip and the exam rewards.

## Secure AI (4.2)

- Security applies across the **whole ML lifecycle**, not just at deployment.
- **SAIF** — Google's Secure AI Framework — is the named framework for securing AI
  systems.
- Named Google Cloud security tools: **secure-by-design infrastructure**, **Identity
  and Access Management (IAM)**, **Security Command Center**, and workload monitoring.

## Responsible AI (4.3)

| Concern | What it means in practice |
|---|---|
| **Transparency** | People know AI was involved and how it was used |
| **Privacy** | Privacy risk assessment, **anonymization**, **pseudonymization** |
| **Data quality, bias, fairness** | Training data shapes outcomes; skewed data produces skewed decisions |
| **Accountability** | A named owner answers for outcomes |
| **Explainability** | A decision can be explained to the person it affects |

## Secure vs responsible — do not conflate

| | Secure AI | Responsible AI |
|---|---|---|
| Protects against | Attackers and misuse | Harm from the system working as built |
| Typical answer | SAIF, IAM, Security Command Center | Transparency, fairness, explainability, accountability |

## Traps

- **Trap:** answering a responsible-AI question with a security control, or the reverse.
  This is the most reliable trap pair in the section.
- **Trap:** skipping impact measurement. If an option is the only one that defines how
  success will be measured, it is usually the answer.
- **Trap:** treating anonymization and pseudonymization as the same thing —
  pseudonymized data can still be re-identified with the key.
- **Trap:** leading with technology when the stem describes an organizational or change
  problem.

## Verify before sealing

- [Security and AI](https://cloud.google.com/security/ai)
- [Responsible AI](https://cloud.google.com/responsible-ai)
- [Security Command Center](https://cloud.google.com/security-command-center)
- [Generative AI Leader exam guide](https://cloud.google.com/learn/certification/generative-ai-leader)
