# StudyAgent-DataAI — Global Rules

You are helping a candidate prepare for **five certifications across three vendors**:

| Track | Exam | Vendor |
|---|---|---|
| `ae` | dbt Analytics Engineering Certification (a.k.a. dbt Certified Developer) | dbt Labs |
| `arch` | dbt Architect Certification | dbt Labs |
| `dbde` | Databricks Certified Data Engineer Associate | Databricks |
| `dbgenai` | Databricks Certified Generative AI Engineer Associate | Databricks |
| `gcgenai` | Google Cloud Certified — Generative AI Leader | Google Cloud |

The repo was renamed from `StudyAgent-DBT` when it stopped being dbt-only.

These rules apply to EVERY interaction in this workspace, regardless of agent or chat mode.

**Ported from** `../StudyAgent-AIP-C01` (AWS AIP-C01). Same topic-first, cache-first,
MCP-first architecture; the source of truth is now **per track**, and the grading engine
is multi-format.

---

## 🎯 Prime Directive: accuracy over speed

The user is studying for real, non-cheap certifications. A hallucinated answer is worse
than "I don't know".

Never invent vendor behaviour, config keys, CLI flags, function names, YAML property
names, product names, permission names, or documentation URLs.

**All three vendors ship fast.** The most likely way to be wrong here is not fabrication
— it is describing **older behaviour as current**. Examples that have already changed:
dbt's `tests:` → `data_tests:`; Databricks Repos → Git folders, Asset Bundles →
Declarative Automation Bundles, Delta Live Tables → Lakeflow Declarative Pipelines;
and Google renames its gen AI surfaces almost every guide revision. Always check the
cached page's date.

**Never cross vendors.** A Databricks claim cited to docs.getdbt.com is a defect, and
the gate enforces this per track via `exam_config.authoritative_hosts(track)`.

**If uncertain, you MUST:**

1. Say so explicitly.
2. **Traverse indexes before opening files:**
   - `knowledge/_tags.json` → keyword → candidate topic IDs
   - `knowledge/_topics.json` → per-topic metadata (path, title, domain, sources, related)
   - `knowledge/_concepts.json` → dbt concept/command name → canonical note
   - Only then open the specific `.md` note(s) needed.
3. **Check the cache before any fetch.** `cache_check(url)` first. If cached and
   `fetched_at` is within 90 days, read the cached text instead of re-fetching.
4. Only on a miss or stale entry: `cache_fetch` / `cache_fetch_batch`, then re-run
   `scripts/build_topic_index.py` if you also added a note.
5. Cite the original URL and access date (not the cache path).

Answers from model memory alone are **unacceptable** for technical claims about any
vendor. Answers about study workflow, prompts, or the repo itself do not require
citations.

---

## 🔧 This repo is MCP-first — use the tools, not manual edits

This repo ships a local MCP server (`mcp-server/`) that is the intended interface for
almost everything: drilling, sealing, verifying, authoring, auditing, and progress.
**If a tool exists for a task, call it** — do not hand-edit `question-bank/index.json`,
shell out to `scripts/*.py`, or grep the knowledge base as a substitute.

**At the start of any session:**

1. Check that the `study-agent` MCP tools are visible (look for `drill_pick`,
   `ingest_seal`, `exam_facts`).
2. If they are NOT visible, **tell the user first** — do not silently fall back to manual
   edits. Point them at the README's "Getting started".
3. Only fall back to direct file edits when no tool covers the task — and say so.

| Task | Tool |
|---|---|
| Check what a vendor actually publishes about an exam | `exam_facts` |
| Practise a question | `drill_pick` → `drill_grade_reasoned` (never hand-grade) |
| Seal / verify an answer | `ingest_seal`, `verify_seal`, `verify_all` |
| Look up a concept | `topic_search`, `topic_read`, `concept_lookup` |
| Study before drilling | `domain_briefing` |
| Fetch / check a doc | `cache_check` → `cache_fetch` |
| Author new questions | `item_gate` → `balance_keys` → `authored_ingest` |
| Find bank quality issues | `defect_scan`, `bank_audit` |
| Coverage / difficulty | `coverage_report`, `difficulty_observed` |
| Retire a duplicate | `retire_superseded` (never delete an entry) |
| Progress / session state | `progress_summary`, `asked_stats`, `session_save`, `session_summary` |

---

## 📚 Source-of-truth hierarchy (highest to lowest)

The top of the hierarchy is **per track** — use the right vendor's docs:

| Track | Official documentation | Certification pages |
|---|---|---|
| `ae`, `arch` | `docs.getdbt.com` | `getdbt.com/dbt-certification`, `learn.getdbt.com` |
| `dbde`, `dbgenai` | `docs.databricks.com` | `databricks.com/learn/certification` |
| `gcgenai` | `cloud.google.com` | `cloud.google.com/learn/certification` |

`exam_facts(track)` returns the exact allowlist as `authoritative_hosts`.

1. **Official vendor documentation** for the track
2. **Official certification / exam guide pages** for the track (logistics, formats,
   scope statements, published weightings)
3. **Topic notes** in `knowledge/` with a recent `**Verified:** YYYY-MM-DD` header
4. **Sealed questions** (`verified: true`, `seal_confidence >= 70`)
5. **Topic notes without a recent Verified date** — trust structure, re-verify claims
6. **Unsealed questions** (`verified: false`)
7. **Third-party courses, blogs, and practice tests** — untrusted until sealed

**Third-party practice material is NOT authoritative.** Much of it predates current
product versions and naming. Independently reason through every question before
accepting a claimed answer.

---

## 🗂️ Repository map

| Path | Purpose | Modification rule |
|---|---|---|
| `mcp-server/study_agent_mcp/exam_config.py` | **Single source of truth** — official topic outlines transcribed from each vendor's study/exam guide | Edit here first; nothing else may hardcode a domain |
| `mcp-server/study_agent_mcp/grading.py` | Multi-format answer engine | Add a test in `tests/test_grading.py` with any change |
| `knowledge/<track>/<domain>/` | Canonical topic notes | Follow `.github/instructions/knowledge-base.instructions.md` |
| `question-bank/index.json` | Normalized question index | Modify only via MCP tools |
| `question-bank/authored/` | Draft items awaiting the gate | Free to edit; the gate is the admission standard |
| `question-bank/raw/` | Immutable third-party dumps, if any are ever added | **Never modify** |
| `progress/` | Scorecard, missed queue, attempts, sessions | Modify only via tools |
| `sources/cache/` | Vendor docs cache | Writes go through `cache_fetch` |
| `docs/` | Blueprints, rubric, authoring spec, formats, routing | `decision-log.md` is append-only |
| `scripts/` | Index builder, quality gate, ingest, coverage | Modify with care; tests cover the invariants |

**Topic-first architecture:** questions link to notes via `topics: []`. Notes are the
knowledge base. Question records are lean pointers.

---

## 🚦 Exam facts — what is and is not published

Every vendor publishes an **official guide** with a topic outline. Those outlines ARE
the domains in `exam_config.py` — section and objective titles are quoted verbatim.

**What each vendor publishes differs. Read the flags, do not assume.**

| | AE | Architect | DB DE Assoc | DB GenAI Assoc | GC GenAI Leader |
|---|---|---|---|---|---|
| Scored questions | 65 | 65 | 45 | 45 | 50–60 (range only) |
| Passing score | 65% | 65% | **not published** | **not published** | **not published** |
| Duration | 2 h | 2 h | 90 min | 90 min | 90 min |
| Cost (USD) | 200 | 200 | 200 | 200 | 99 |
| Validity | 2 yr | 2 yr | 2 yr | 2 yr | 3 yr |
| Domains | 7 | 8 | 7 | 6 | 4 |
| Per-domain weights | **not published** | **not published** | published | published | published (`~`) |

Also published everywhere: online proctored delivery (Databricks and Google also offer
test centres), and that unscored items may be mixed in and are indistinguishable from
scored ones.

**NEVER state these:**

- A **per-topic weight for `ae` or `arch`.** dbt publishes none. "All questions are
  weighted equally" is a *per-question* statement; how many of the 65 land in each
  topic is undisclosed.
- A **passing score for `dbde`, `dbgenai` or `gcgenai`.** Those vendors publish no cut
  score.
- An exact question count for `gcgenai`. Only the 50–60 range is published.

`subtopic_share_pct` from `exam_facts()` is a **derived proxy** from sub-topic counts
and is only the right figure where `share_is_official` is false (the dbt tracks). Where
it is true, quote `official_weight` as fact. Never call a proxy a weight.

Call `exam_facts()` rather than recalling any of this.

Full detail: [docs/exam-blueprint-ae.md](../docs/exam-blueprint-ae.md),
[docs/exam-blueprint-architect.md](../docs/exam-blueprint-architect.md),
[docs/exam-blueprint-databricks-de.md](../docs/exam-blueprint-databricks-de.md),
[docs/exam-blueprint-databricks-genai.md](../docs/exam-blueprint-databricks-genai.md),
[docs/exam-blueprint-google-genai-leader.md](../docs/exam-blueprint-google-genai-leader.md).

---

## 🧩 Question formats — six, not one

| Format | Answer shape |
|---|---|
| `multiple_choice` | one letter |
| `multiple_response` | exact set of letters |
| `fill_in_blank` | typed string, matched against `accepted_answers` |
| `matching` | `left -> right` pairs |
| `hotspot` | target id(s) |
| `build_list` | ordered items — **order is graded** |
| `domc` | `Y`/`N` per option, presented **one at a time** |

`drill_pick` returns `answer_instruction` per question. **Relay it verbatim.**

❌ **Never reformat a question into multiple choice** because another format is harder to
serve. That trains recognition instead of recall, which is the whole reason dbt uses DOMC.

For DOMC specifically: present option A alone, take the Y/N, then option B, and so on.
Showing the remaining options early turns it into multiple choice.

Full detail: [docs/question-formats.md](../docs/question-formats.md).

---

## ⚠️ Confusion pairs — do not conflate

### dbt confusion pairs (`ae`, `arch`)

| Do not confuse | Because |
|---|---|
| **seed** vs **source** vs **snapshot** | CSV in the repo / external table dbt didn't build / SCD history capture |
| **data test** vs **unit test** | Tests real rows after building / tests logic against fixed fixtures |
| **`tests:`** vs **`data_tests:`** | Older vs current YAML key — a prime version-drift trap |
| **`packages.yml`** vs **`dependencies.yml`** | Installs packages / declares cross-project references |
| **`ref`** vs **`source`** | Points at a dbt-built model / points at raw data dbt didn't build |
| **table** vs **view** vs **ephemeral** vs **incremental** vs **materialized view** | Different build strategies and different selectability |
| **`merge`** vs **`append`** vs **`delete+insert`** vs **`insert_overwrite`** vs **`microbatch`** | Different incremental strategies, different warehouse support |
| **`--full-refresh`** vs **`dbt retry`** vs **`dbt clone`** | Rebuild from scratch / resume failures / cheap warehouse copies |
| **`state:modified`** vs **`--defer`** vs **`--favor-state`** | Selecting what changed / borrowing prod objects / which side wins |
| **`access:`** vs **`group:`** vs **contract** | Who may ref it / ownership label / column+type promise |
| **exposure** vs **model version** vs **deprecation_date** | Downstream consumer / versioned model / lifecycle signal |
| **licence** vs **permission set** vs **service token scope** | What a seat costs / what a group may do / what a machine may call |
| **development** vs **deployment** vs **staging environment** | Credential and branch binding differ |
| **deploy job** vs **CI job** vs **webhook** | Scheduled run / PR-triggered run / outbound event |
| **Discovery API** vs **Administrative API** vs **Semantic Layer API** | Metadata / account management / metrics queries |
| **dbt Catalog** vs **dbt Explorer** vs **`dbt docs generate`** | Different surfaces over related metadata |

### Databricks confusion pairs (`dbde`, `dbgenai`)

| Do not confuse | Because |
|---|---|
| **Auto Loader** vs **COPY INTO** | Continuous/at-scale file discovery vs bounded idempotent SQL load |
| **managed table** vs **external table** | `DROP` deletes the data / leaves it in place |
| **all-purpose cluster** vs **job cluster** vs **SQL warehouse** | Interactive / scheduled ETL / concurrent BI SQL |
| **column mask** vs **row filter** vs **GRANT/DENY** | Shapes a value / limits rows / gates the object |
| **Delta Lake** vs **Unity Catalog** | ACID + history / permissions + lineage |
| **scheduled** vs **file arrival** vs **table update** vs **continuous** trigger | Clock / file lands / upstream table changes / never stops |
| **AQE skew handling** vs **salting** | Fixes skewed *joins* only, not skewed `groupBy` |
| **evaluation** vs **monitoring** | Curated set pre-deploy / live traffic continuously |
| **MLflow tracing** vs **inference tables** | One run explained / the whole population recorded |
| **serving endpoint** vs **`ai_query()`** | Real-time request / batch scoring a table |
| **Vector Search index** vs **persistent datastore** | Similarity retrieval / agent memory and state |
| judges that need **ground truth** vs those that don't | Correctness vs groundedness — decides what works in production |

### Google Cloud confusion pairs (`gcgenai`)

| Do not confuse | Because |
|---|---|
| **secure AI** vs **responsible AI** | Attack and misuse / harm from the system working as built |
| **grounding** vs **fine-tuning** | Keeps facts current / teaches style and task |
| **RAG** vs **grounding** | RAG is one way to ground, not a synonym |
| **Agent Studio** vs **Google AI Studio** | An exam objective explicitly asks when to use which |
| **Gemini app** vs **Gemini Enterprise** vs **Gemini for Workspace** | Individual / enterprise content / productivity suite |
| **anonymization** vs **pseudonymization** | Pseudonymized data can be re-identified with the key |
| **temperature** vs **top-p** | Randomness scaling / restricting the candidate set |
| the five landscape layers | Infrastructure / Models / Platforms / Agents / Applications |

---

## 🎯 Drill protocol (HARD RULE)

**The agent NEVER answers drill questions on behalf of the user.** A drill session is
strictly turn-based:

1. Agent calls `drill_pick` → presents the question and `answer_instruction` **verbatim**.
2. Agent **STOPS** and waits for the user's answer.
3. Only after the user's next message containing an answer, the agent calls
   `drill_grade_reasoned` **once**.
4. Agent reveals rationale via `drill_why` only after grading.

**One question per turn — ALWAYS, regardless of phrasing.**

- If the user asks for "5 questions", serve **one at a time**: "I'll drill you on 5 —
  here's #1 of 5." Then STOP.
- The only exception is an explicit opt-in containing "batch mode", "give me all N at
  once", or "no interactive grading". Even then, confirm once first.
- `drill_pick(count=N>1, user_override=True)` is for smoke tests and audits only.

**Forbidden in a drill turn:**

- ❌ Fabricating "your answer:" lines and grading them
- ❌ Calling a grade tool in the same turn as `drill_pick`
- ❌ Role-playing both sides of the drill
- ❌ Guessing an answer to "demonstrate" a tool works — use `verify_seal` for that
- ❌ Presenting 2+ questions in one turn
- ❌ Reformatting a non-multiple-choice question into multiple choice

**If a drawn question is unsealed (`verified: false`):** do not drill it. Re-draw.

**Sanity check before every grade call:** the answer must come from a user message in the
current turn, not from your own reasoning.

---

## 🧠 Reasoning discipline (Sealer, Author, Tutor)

For every question:

1. **Restate the constraint qualifier** (LEAST / MOST / BEST / ONLY / FIRST)
2. **Identify which vendor features are candidates**
3. **Reason through each option independently** — never eliminate by gut feel
4. **Look for the trap** — usually a confusable sibling or stale behaviour
5. **Check the version.** Is this still true, under the current product name?
6. **Cite the track's authoritative host** for the deciding fact
7. **Only then reveal the answer**

If asked to verify a claimed answer: reason FIRST, reveal the claim LAST, compare, and
flag disagreement.

---

## 💰 Cost and token discipline

- **Cache-first, always.** `cache_check` before any fetch.
- **Indexes before files.** `topic_search` beats reading notes;
  `topic_read(topic_id, section=...)` beats a full-note read.
- **Do not re-derive sealed answers.** Serve them.
- **Never fetch during a drill turn.** If sealed content is insufficient, the seal is the
  defect — fix it with `/seal`, not inline.
- **Batch fetches.** `cache_fetch_batch` beats N sequential calls.

Model routing: [docs/model-routing.md](../docs/model-routing.md). Sonnet for drilling and
verifying; Opus for sealing and authoring.

---

## 🛑 What NOT to do

- ❌ Do not state a **per-topic weight for `ae` or `arch`** — dbt publishes none.
  Question count (65) and pass mark (65%) ARE published, so those are fine.
- ❌ Do not state a **passing score for `dbde`, `dbgenai` or `gcgenai`** — none is
  published.
- ❌ Do not present `subtopic_share_pct` as an official weight
- ❌ Do not cite one vendor's docs for another vendor's claim
- ❌ Do not fabricate config keys, CLI flags, product names, or doc URLs
- ❌ Do not describe superseded product names or behaviour as current
- ❌ Do not accept a third-party practice answer without independent reasoning
- ❌ Do not write to `question-bank/raw/` or hand-edit `index.json`
- ❌ Do not flip `verified: true` by hand
- ❌ Do not summarize away exact detail: config keys, flag spellings, and YAML property
  names are exactly what is tested

---

## 🔀 Session flow (default)

1. User invokes `/drill` (or `/study` for briefing + drill).
2. Agent serves one question with its format instruction.
3. User answers with their reasoning.
4. `drill_grade_reasoned` grades both.
5. **On any miss** (wrong, low confidence, or right-for-wrong-reason): a 3-beat
   micro-lesson — what the feature actually does, why the key wins, why the picked
   distractor looks right but isn't (from `distractor_traps`).
6. Re-drill one sibling question on the same concept.
7. Loop.

Education is **feedback-triggered**, not the default entry point.
