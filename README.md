# StudyAgent-DataAI

An agentic study workbench for **five data and AI certifications across three vendors**,
built as a local MCP server plus a verified knowledge base.

| Track | Exam | Vendor |
|---|---|---|
| `ae` | **dbt Analytics Engineering Certification** — the learning path and study guide call it the *dbt Certified Developer* exam | dbt Labs |
| `arch` | **dbt Architect Certification** | dbt Labs |
| `dbde` | **Databricks Certified Data Engineer Associate** | Databricks |
| `dbgenai` | **Databricks Certified Generative AI Engineer Associate** | Databricks |
| `gcgenai` | **Google Cloud Certified — Generative AI Leader** | Google Cloud |

The repo name is historical — it started dbt-only.

Ported from [`StudyAgent-AIP-C01`](../StudyAgent-AIP-C01) (AWS). Same topic-first,
cache-first, MCP-first architecture; the source of truth is now per track, and the
grading engine is multi-format.

---

## What makes this different from a flashcard app

- **Nothing is asserted without a citation.** Every question's answer is sealed against a
  cached page from **the vendor that owns the track**, and the authoring gate rejects any
  item whose deciding fact cannot be found in that cached text — or whose citation points
  at a different vendor.
- **All seven question formats are drilled in their real form** — including Discrete
  Option Multiple Choice, where options are shown one at a time and you cannot revise.
  Practising only multiple choice trains recognition instead of recall.
- **Reasoning is graded, not just the answer.** `drill_grade_reasoned` compares your
  stated reason against the sealed rationale, so "right for the wrong reason" is caught.
- **No invented exam facts.** Domains are the official topic outlines from each vendor's
  guide. dbt publishes no per-topic weighting, so the dbt tracks have none; Databricks and
  Google do publish section weights, so those are stored as facts. A unit test fails the
  build if a weight appears where the vendor publishes none — or if a passing score is
  stated for a vendor that publishes no cut score.

---

## Getting started

```bash
git clone <this repo> && cd StudyAgent-DataAI
./scripts/setup.sh
```

That creates the venv, installs deps, generates the directory skeleton and progress
artifacts from `exam_config.py`, builds the knowledge indexes, and runs the smoke test.

Then reload your editor window so the MCP client picks up `.vscode/mcp.json`, and confirm
the `study-agent` server is listed and started.

### Slash commands

| Command | Model | Purpose |
|---|---|---|
| `/study` | Sonnet | Brief a domain from the notes, then drill it |
| `/drill` | Sonnet | Interactive quiz, one question per turn, reasoning validated |
| `/author` | Opus | Write new items from the track's vendor docs through the quality gate |
| `/seal` | Opus | Independently derive and verify an unsealed answer |
| `/verify` | Sonnet | Sweep for broken seals, stale sources, and version drift |

### Other MCP clients

The server is plain stdio, so any MCP client works. Point it at:

```
command: <repo>/mcp-server/.venv/bin/python
args:    [<repo>/mcp-server/run.py]
```

For Copilot CLI, choose "Yes, and remember this folder" on first run — without folder
trust the MCP config is silently ignored.

---

## Agent customization — nothing to install

Everything that shapes the agent lives in `.github/` and is **workspace-local**. Clone
the repo, trust the folder, and it is active. There is no extension to install, no
marketplace entry, and nothing to copy into your user profile.

| Asset | Path | How it activates |
|---|---|---|
| **Global rules** | `.github/copilot-instructions.md` | Loaded automatically on every request in this workspace |
| **Scoped instructions** | `.github/instructions/*.instructions.md` | Applied when the file you are touching matches the `applyTo` glob in the frontmatter |
| **Prompts** | `.github/prompts/*.prompt.md` | Invoked explicitly as a `/` slash command, named after the file |
| **Skills** | `.github/skills/<name>/SKILL.md` | Loaded on demand when your request matches the skill's `description` |

### What each one is for

- **`copilot-instructions.md`** is the constitution: the prime directive, the
  source-of-truth hierarchy, the per-vendor confusion pairs, and the drill protocol. It
  applies no matter which agent or chat mode you are in.
- **`instructions/`** are narrow and glob-scoped. `knowledge-base.instructions.md`
  (`applyTo: knowledge/**`) holds the note contract; `question-bank.instructions.md`
  (`applyTo: question-bank/**`) holds the record contract. They load only when relevant,
  which keeps them out of the way during a drill.
- **`prompts/`** pin a model and a tool allowlist per workflow — `/drill` gets the fast
  tier and only drill tools, `/author` gets the heavy tier and only authoring tools. That
  allowlist is what stops `/drill` from quietly fetching docs mid-question.
- **`skills/`** are multi-step procedures the agent pulls in by itself. Today there is
  one: **`import-practice-questions`**, which turns a pasted third-party practice exam
  into original, gate-verified items.

### Using the import skill

You do not invoke it by name. Paste the practice questions into chat and say what you
want, e.g. *"add these to the bank for `dbde`"*. The agent matches your request against
the skill description and follows the procedure: copyright triage, domain remapping,
independent re-grounding against the right vendor's docs, authoring, then
`item_gate` → `balance_keys` → `authored_ingest`.

It will **not** copy stems verbatim and will **not** accept the source's claimed answer
key without re-deriving it. That is the point of the skill — third-party practice
material sits at the bottom of the source-of-truth hierarchy.

### Adding your own

```bash
mkdir -p .github/skills/my-skill && $EDITOR .github/skills/my-skill/SKILL.md
```

The frontmatter needs `name` and a `description` written for *matching* — state the
trigger conditions in the user's words, not a summary of the contents. Reference files
go alongside it (see `skills/import-practice-questions/references/`). Prompts are the
same idea with `mode`, `model`, `description` and a `tools` allowlist.

---

## Growing the bank

There is no trustworthy public question dump for any of these five exams, and the
third-party material that exists frequently describes superseded product versions and
names. Seeding from it uncritically would poison the bank — so every item enters through
one of two doors, both of which end at the same quality gate:

```
/author                      # write originals from the vendor docs
```

picks the emptiest task from `coverage_report`, fetches the relevant vendor pages into
the cache, and writes items through `item_gate`.

```
paste a practice exam + "add these for <track>"
```

triggers the `import-practice-questions` skill, which re-derives each answer
independently before anything is admitted.

`coverage_report(track="dbde")` shows both task gaps and **format gaps** — it will tell
you when the bank has drifted into being all multiple choice.

---

## Repo map

| Path | What it is |
|---|---|
| `mcp-server/study_agent_mcp/exam_config.py` | **Single source of truth**: official topic outlines, tasks, formats, per-track authoritative hosts, ID prefixes. Adding a track or domain is one edit here plus `bootstrap_repo.py`. |
| `mcp-server/study_agent_mcp/grading.py` | Multi-format answer engine (all seven formats) |
| `mcp-server/study_agent_mcp/server.py` | The MCP tool surface |
| `mcp-server/tests/` | 68 unit tests + a 43-check integration smoke test |
| `.github/` | Agent customization — global rules, scoped instructions, prompts, skills |
| `knowledge/<track>/<domain>/` | Verified topic notes — the knowledge base |
| `question-bank/` | `index.json` (sealed bank) and `authored/` (drafts awaiting the gate) |
| `progress/` | Scorecard, missed queue, per-attempt log, session snapshots |
| `sources/cache/` | Cached vendor docs; 90-day freshness window |
| `docs/` | Blueprints (one per track), question formats, authoring spec, domain rubric, model routing, decision log |
| `scripts/` | Index builder, quality gate, ingest, coverage, bootstrap |

---

## Exam facts — and what each vendor refuses to publish

| | AE | Architect | DB DE Assoc | DB GenAI Assoc | GC GenAI Leader |
|---|---|---|---|---|---|
| Scored questions | 65 | 65 | 45 | 45 | 50–60 (range only) |
| Passing score | 65% | 65% | **not published** | **not published** | **not published** |
| Duration | 2 h | 2 h | 90 min | 90 min | 90 min |
| Cost (USD) | 200 | 200 | 200 | 200 | 99 |
| Validity | 2 yr | 2 yr | 2 yr | 2 yr | 3 yr |
| Domains | 7 | 8 | 7 | 6 | 4 |
| Per-domain weights | **not published** | **not published** | published | published | published (`~`) |

Domains in this repo are the **official outlines** transcribed from each vendor's guide,
with section and objective titles quoted verbatim. Databricks prints its objectives as
unnumbered bullets, so the `N.M` task ids for those two tracks are ours — the titles are
not.

The two asymmetries are enforced by tests rather than by discipline:

- **dbt publishes no per-topic weighting.** `exam_facts()` returns a `subtopic_share_pct`
  proxy derived from sub-topic counts, flagged `share_is_official: false`. Databricks and
  Google do print section percentages, so those are stored as real weights and flagged
  `true`. `test_weights_are_not_fabricated` fails the build either way round.
- **Databricks and Google publish no cut score.** `passing_score_pct` is `null` for those
  three tracks and `test_passing_score_is_only_stated_where_published` keeps it that way.

Call `exam_facts(track=...)` rather than trusting this table — it is generated from the
same config the tests guard.

Per-track detail: [AE](docs/exam-blueprint-ae.md) ·
[Architect](docs/exam-blueprint-architect.md) ·
[Databricks DE](docs/exam-blueprint-databricks-de.md) ·
[Databricks GenAI](docs/exam-blueprint-databricks-genai.md) ·
[Google GenAI Leader](docs/exam-blueprint-google-genai-leader.md)

---

## Question formats

| Format | Answer |
|---|---|
| Multiple choice | one letter |
| Multiple response | exact set of letters |
| Fill in the blank | typed term, matched against accepted variants |
| Matching | `left -> right` pairs |
| Hotspot | region id(s) |
| Build list | ordered items — **order is graded** |
| DOMC | `Y`/`N` per option, presented **one at a time** |

See [docs/question-formats.md](docs/question-formats.md).

---

## Common tasks

```bash
# rebuild knowledge indexes after editing notes
./mcp-server/.venv/bin/python scripts/build_topic_index.py

# run a candidate batch through the quality gate
./mcp-server/.venv/bin/python scripts/item_qa.py question-bank/authored/batch.json --verbose

# what to author next
./mcp-server/.venv/bin/python scripts/blueprint_coverage.py --track ae

# tests
./mcp-server/.venv/bin/python -m unittest discover -s mcp-server/tests -p 'test_*.py'
./mcp-server/.venv/bin/python mcp-server/tests/smoke.py
```

Prefer the MCP tools over the scripts in normal use — the scripts are the implementation,
the tool surface is the product.

---

## Extending it

### Adding a track

1. Add an entry to `exam_config.EXAM_FACTS` — including `vendor`,
   `authoritative_hosts`, `weights_published` and `passing_score_published`. State only
   what the vendor actually prints; leave the rest `None`.
2. Add its domains to `exam_config.DOMAINS`, quoting section and objective titles
   verbatim and recording `provenance`.
3. `python3 scripts/bootstrap_repo.py` to create `knowledge/<track>/<NN>-<slug>/`.
4. Add a blueprint in `docs/`, scorecard rows in `progress/scorecard.md`, and a glossary
   in `server.py` if the vendor's vocabulary is new.
5. `python3 scripts/build_topic_index.py`, then run the tests.

Nothing else hardcodes a track — regexes build their alternation from
`exam_config.TRACK_RE_GROUP`, and citation checks resolve hosts per track.

### Adding a domain

Edit `exam_config.DOMAINS`, run `bootstrap_repo.py`, then `build_topic_index.py`.
`test_exam_config.py` catches an id that disagrees with its folder or a task with the
wrong major number, and `test_docs_consistency.py` fails if any doc names a folder that
does not exist.

### Adding a question format

See the checklist at the end of [docs/question-formats.md](docs/question-formats.md).
A test fails if you skip the rendering step.

### Renaming the repo

1. Rename it on GitHub (Settings → Repository name). GitHub redirects the old URL, so
   existing clones and links keep working.
2. `git remote set-url origin <new-url>`
3. Rename the local folder and reopen it — the MCP config uses `${workspaceFolder}`, so
   it follows automatically.
4. Update the name in `README.md`, `.github/copilot-instructions.md` and
   `scripts/setup.sh`, and append the reasoning to `docs/decision-log.md`.

---

## License

MIT — see [LICENSE](LICENSE).
