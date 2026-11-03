# Exam dry-run review — 2026-10-27/28

61 unseen questions drawn proportionally across ae-01–ae-07 (65-target, 4 short due to
pacing). Score: **42/61 (~69%)**. This file explains every one of the 19 misses in
detail. For spaced repetition, these are also queued in `missed-questions.md` via
`drill_pick(mode="missed")`.

---

## ae-01 — Developing and optimizing dbt models (22/29, 7 misses)

### Q-AU-DBTAE-005 — Snapshot hard-deletes config key
**You answered:** C (`hard_deletes: new_record`) **Correct:** A (`hard_deletes: invalidate`)
A snapshot using the `timestamp` strategy needs to close out a row's validity window when
the source row is hard-deleted. `hard_deletes: invalidate` is the current key that
replaced the older `invalidate_hard_deletes=true` boolean. `new_record` is a real option
but it *inserts* a new "deleted" record rather than invalidating the existing one.
Review: `knowledge/ae/01-developing-and-optimizing-models/snapshots.md`

### Q-AU-DBTAE-009 — Grants: additive privilege key
**You answered:** "add" **Correct:** `'+select'`
To make a model's `grants` config *add* to the project-level grantees instead of
clobbering them, prefix the privilege name with `+` — e.g. `+select`. There is no literal
key called "add"; the `+` prefix is the actual addition mechanism on the privilege name.
Review: `knowledge/ae/01-developing-and-optimizing-models/grants.md`

### Q-AU-DBTAE-013 — Flag precedence (CLI vs env var vs project)
**You answered:** C (`dbt_project.yml` value) **Correct:** B (the CLI option)
With `dbt build --fail-fast` on the command line, an env var set to `0`, and
`dbt_project.yml` also setting `fail_fast: true`, the **CLI flag always wins** — it's the
most specific setting in the precedence ladder (CLI > env var > `dbt_project.yml` flags >
`user_settings.yml`). A flag physically present at the command line overrides everything
else, no matter what else is also configured.
Review: `knowledge/ae/01-developing-and-optimizing-models/project-config-and-flags.md`

### Q-AU-DBTAE-057 — `dbt show` vs the built table
**You answered:** B (reads run-results artifact) **Correct:** D (recompiles and reruns from source)
`dbt show` **always compiles and runs the query from source** — it never reads the
already-materialized relation. That's exactly why its output can differ from what a
warehouse client sees against the built table: `dbt show` re-executes the model's logic
live, it doesn't peek at run-results metadata or the table itself.
Review: `knowledge/ae/01-developing-and-optimizing-models/dbt-commands.md`

### Q-AU-DBTAE-069 — `packages.yml` vs `dependencies.yml`
**You answered:** D ("just the new name for packages.yml") **Correct:** A,B
These are two different files with different jobs, not a rename: cross-project
references for dbt Mesh go in `dependencies.yml`. A private Git package whose spec needs
a **Jinja-rendered token** must stay in `packages.yml`, because `dependencies.yml` does
**not** render Jinja. Mixing the two files by capability, not treating one as the
successor of the other, is the correct mental model.
Review: `knowledge/ae/01-developing-and-optimizing-models/packages.md`

### Q-AU-DBTAE-071 — Materialization config precedence (in-file vs YAML vs project)
**You answered:** C (project-wide default) **Correct:** B (in-file `config()` block)
When a `.sql` file's `config()` block, a model's `schema.yml` property, and
`dbt_project.yml` all disagree, **the in-file `config()` block wins** — it's the most
specific/deepest-nested layer dbt reads, same "most specific wins" logic as flag
precedence, just applied to resource configs instead of global flags.
Review: `knowledge/ae/01-developing-and-optimizing-models/materializations.md`

### Q-AU-DBTAE-079 — Preserving seed column types (leading zeros)
**You answered:** B (post-hook casting the column) **Correct:** C (`column_types` config)
To stop dbt from inferring a numeric type on a `zipcode` seed column and stripping
leading zeros, use the seed's `column_types` config to **explicitly declare the type as
varchar** — this is a first-class, documented seed config, not "just documentation." A
post-hook would work too in principle but is not the documented, direct fix; `column_types`
is purpose-built for exactly this.
Review: `knowledge/ae/01-developing-and-optimizing-models/dbt-commands.md`

---

## ae-02 — Model governance (5/6, 1 miss)

### Q-AU-DBTAE-068 — Default version when `latest_version` is unset
**You answered:** B (v1, "always defaults to first version") **Correct:** C (v3)
This is a real exception worth remembering: **if `latest_version` is never set at all**,
dbt defaults to the **numerically highest version number** as latest — not v1, and not
"whichever was most recently built." This only differs from the "latest_version decides,
not the highest number" rule when `latest_version` is actually declared; absent that
declaration, highest-number wins by default.
Review: `knowledge/ae/02-model-governance/model-versions.md`

---

## ae-03 — Debugging data modeling errors (7/11, 4 misses)

### Q-AU-DBTAE-029 — Defer resolution when a stale local copy exists
**You answered:** B (resolves to prod) **Correct:** A (resolves to the developer's own copy)
Defer only falls back to the `--state` manifest (production) when the node is **both**
(1) unselected **and** (2) absent from the local database — or `--favor-state` is passed.
Here a stale copy already exists locally and `--favor-state` was *not* used, so `ref`
resolves to the **local** stale copy, not production. The existence check is the part
that's easy to skip past.
Review: `knowledge/ae/03-debugging-modeling-errors/fix-and-verify-before-merge.md`

### Q-AU-DBTAE-093 — Where to find the exact SQL dbt executed
**You answered:** B (`target/compiled/`) **Correct:** A (`target/run/`)
`target/compiled/` holds the **raw `select` statement** before dbt wraps it for
execution (e.g. before `merge`/`insert` wrapping for incremental models).
`target/run/` holds the **actual SQL dbt executed** against the warehouse — that's the
one to open when chasing a cryptic database error.
Review: `knowledge/ae/03-debugging-modeling-errors/compiled-code-and-logs.md`

### Q-AU-DBTAE-094 — Naming the dependency-cycle error type
**You answered:** D (Runtime Error) **Correct:** A (Dependency Error)
A cycle detected while building the dependency graph — after Jinja/YAML parsing
succeeds, before any SQL runs — is a **Dependency Error**, a distinct named error type
from Compilation Error (parsing stage) and Database Error (execution stage).
Review: `knowledge/ae/03-debugging-modeling-errors/compiled-code-and-logs.md`

### Q-AU-DBTAE-095 — First step to isolate a Database Error
**You answered:** B (rewrite model, different materialization) **Correct:** A (open the compiled SQL and re-run it)
90% of the time a Database Error is a plain mistake in the model's SQL. The fastest
documented triage step is opening the **compiled SQL at the path the error names** and
re-executing it directly in a query editor to isolate exactly where it breaks — not
assuming the materialization itself is unsupported.
Review: `knowledge/ae/03-debugging-modeling-errors/compiled-code-and-logs.md`

---

## ae-04 — Troubleshooting pipelines (2/3, 1 miss)

### Q-AU-DBTAE-036 — `dbt retry` after a connection/permission failure
**You answered:** D (add `--warn-error`) **Correct:** C (check `run_results.json`, re-run the full job)
When a job dies on a permission error **before any node executes**, there is nothing
recorded for `dbt retry` to resume from — it runs nothing, by design, not because the
error was treated as a warning. The documented fix is to check `run_results.json` and
manually re-run the entire job once the underlying permission problem is fixed.
Review: `knowledge/ae/04-troubleshooting-pipelines/dag-failure-points.md`

---

## ae-05 — Implementing dbt tests (1/5, 4 misses)

### Q-AU-DBTAE-044 — `dbt build` execution order for one model
**You answered:** Materialize → unit tests → data tests on parents → data tests on model → docs
**Correct order:** unit tests on model → materialize model → data tests on model
Two things to unlearn here: (1) unit tests run **before** materialization, not after —
they validate logic against static fixtures before the model is ever built; (2) "data
tests on parents" and "generate docs" aren't part of this ordering question at all — the
build sequence for a single model is just the three steps above.
Review: `knowledge/ae/05-implementing-tests/test-severity-and-workflow.md`

### Q-AU-DBTAE-045 — Generic test argument nesting key (v1.10.5+)
**You answered:** "values:" **Correct:** "arguments"
Current dbt (v1.10.5+) nests any arguments passed to a generic test — including the
`values` list for `accepted_values` — under an `arguments:` key. `values:` is the
*content* inside that key, not the key itself. Older dbt put `values:` directly at the
top level with no wrapper; that's the version-drift trap here.
Review: `knowledge/ae/05-implementing-tests/test-severity-and-workflow.md`

### Q-AU-DBTAE-105 — `accepted_values` config, current recommended form
**You answered:** B (top-level `values:`, no `arguments:` key) **Correct:** A (nested under `arguments:`)
Same underlying fact as Q-045 above, tested from the other direction: the docs now
recommend nesting `values` under `arguments:`. The top-level form still works as a
legacy alias but is not "the form the docs now recommend" — which is literally what the
question asked for.
Review: `knowledge/ae/05-implementing-tests/test-types.md`

### Q-AU-DBTAE-106 — Generic `{% test %}` block parameters
**You answered:** B (letter), reasoning described `model`/`column_name` (= option A's content)
**Correct:** A
This was a **transcription slip, not a knowledge gap** — your own stated reasoning
("model for what we run the test against, and column to test") is exactly option A's
content, but you wrote the letter B. Every generic test block takes exactly two
parameters: `model` and `column_name`. Double-check the letter matches your reasoning
before submitting — this cost a free point here.
Review: `knowledge/ae/05-implementing-tests/test-types.md`

---

## ae-07 — Leveraging dbt state (2/4, 2 misses — this was your zero-data domain going in)

### Q-AU-DBTAE-053 — Matching `state:modified` subselectors (3/4 pairs)
**Wrong pair:** "A model's schema or alias changed" → you said `state:modified.configs`,
**correct:** `state:modified.relation`
Schema/alias/database changes are tracked by `state:modified.relation` specifically —
`state:modified.configs` is a distinct subselector for other resource configs. The other
three pairs (`body` for SQL changes, `macros` for upstream macro changes, `contract` for
contracted column `data_type` changes) were correct.
Review: `knowledge/ae/07-dbt-state/state-selection.md`

### Q-AU-DBTAE-055 — Can `dbt retry` take a new/widened selector?
**You answered:** A ("retry honours a new selector") **Correct:** B (re-run the build command with the widened selector instead)
`dbt retry` **resumes the previous invocation exactly as it was** — it does not
re-select or accept a new selector argument. To widen scope to include models that were
never part of the failed invocation, you must re-run the original build/run command with
the new selector; `retry` is strictly for resuming, not for re-scoping.
Review: `knowledge/ae/07-dbt-state/dbt-retry.md`

---

## Cross-cutting patterns worth fixing before the real exam

1. **`arguments:` nesting (v1.10.5+)** cost two separate points in ae-05 alone — this is
   clearly not yet solid. Re-read `test-severity-and-workflow.md` and `test-types.md`
   fully before re-drilling.
2. **Letter/reasoning mismatches** (Q-106 here, plus a couple during the earlier drill
   session) are pure transcription errors, not knowledge gaps — but they score identically
   to being wrong. Build a habit of re-reading your own answer line before sending it.
3. **"Most specific wins" generalizes further than flags** — it governs resource-config
   precedence too (Q-071: in-file `config()` beats YAML properties beats
   `dbt_project.yml`), and CLI-vs-env-var-vs-project-file flag precedence (Q-013). Same
   underlying principle, two different application areas — don't silo them mentally.
4. **ae-07 is still fragile** (50% in this run, was completely untouched before the
   exam) — needs a full `/study` pass, not just spaced re-drills of these two misses.
