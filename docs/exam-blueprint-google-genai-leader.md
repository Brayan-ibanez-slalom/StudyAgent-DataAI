# Google Cloud Certified — Generative AI Leader — Official Blueprint

Transcribed from the **official Google Cloud exam guide**. Track id `gcgenai`. Section
titles and the `N.M` objective numbering are Google's — this guide numbers its own
objectives, unlike the Databricks guides.

- Certification page: <https://cloud.google.com/learn/certification/generative-ai-leader>
- Exam guide PDF: <https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf>
- Authoritative docs: <https://cloud.google.com>

## Logistics (published)

| | |
|---|---|
| Length | 90 minutes |
| Format | 50–60 multiple choice questions |
| Registration fee | USD 99 (plus tax where applicable) |
| Delivery | Online-proctored or onsite-proctored |
| Languages | English, Japanese, Spanish |
| Prerequisites | None |
| Validity | 3 years |

**Passing score is NOT published**, and neither is an exact question count — only the
50–60 range. `planning_question_count("gcgenai")` returns the mid-point (55) purely so
study estimates have something to divide by; it is not a published figure.

## Section weighting (published — these ARE facts)

Google prints these with a tilde ("~30% of the exam"), so treat them as approximate by
the vendor's own wording.

| Domain | Section | Weight | Knowledge folder |
|---|---|---|---|
| `gcgenai-01` | Fundamentals of gen AI | ~30% | `knowledge/gcgenai/01-fundamentals-of-gen-ai` |
| `gcgenai-02` | Google Cloud's gen AI offerings | ~35% | `knowledge/gcgenai/02-google-cloud-gen-ai-offerings` |
| `gcgenai-03` | Techniques to improve gen AI model output | ~20% | `knowledge/gcgenai/03-techniques-to-improve-model-output` |
| `gcgenai-04` | Business strategies for a successful gen AI solution | ~15% | `knowledge/gcgenai/04-business-strategies` |

**Why the published weights matter here more than anywhere else:** this track has only
15 sub-objectives, spread 4 / 5 / 3 / 3. A sub-topic-count proxy would rate Section 1
and Section 2 almost equally and badly understate Section 2. The vendor weights say
Section 2 is the largest. Use the weights.

## Audience

The guide is explicit that this is a **business and leadership** certification:
"expertise is in strategic leadership and influence, not technical implementation,
though they have a conceptual understanding of gen AI concepts and technology." It is
open to any job role, with or without hands-on experience.

Author questions accordingly. A question that hinges on an API parameter spelling is
off-blueprint; a question that hinges on choosing grounding over fine-tuning for a
stale-facts problem is on it.

## Objectives

Held verbatim in
[mcp-server/study_agent_mcp/exam_config.py](../mcp-server/study_agent_mcp/exam_config.py)
and surfaced by `exam_facts(track="gcgenai")`.

## Confusion pairs specific to this track

| Do not confuse | Because |
|---|---|
| secure AI vs responsible AI | Attack and misuse vs harm from the system working as built |
| grounding vs fine-tuning | Keeps facts current vs teaches style and task |
| RAG vs grounding | RAG is one way to ground, not a synonym |
| Agent Studio vs Google AI Studio | Objective 2.5 asks when to use which |
| Gemini app vs Gemini Enterprise vs Gemini for Workspace | Individual, enterprise content, productivity suite |
| anonymization vs pseudonymization | Pseudonymized data can be re-identified with the key |
| temperature vs top-p | Randomness scaling vs restricting the candidate set |
| the five landscape layers | Infrastructure / Models / Platforms / Agents / Applications |

## Volatility warning

Google renames gen AI surfaces frequently and the exam guide tracks the current names.
Re-fetch the guide before a heavy authoring session and re-check product names against
it rather than against memory.
