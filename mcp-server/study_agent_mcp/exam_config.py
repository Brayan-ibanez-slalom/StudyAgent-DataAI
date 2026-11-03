"""Single source of truth for exam metadata. Nothing else may hardcode a domain.

TRACKS
------
  `ae`      — dbt Analytics Engineering Certification Exam           (dbt Labs)
  `arch`    — dbt Architect Certification Exam                       (dbt Labs)
  `dbde`    — Databricks Certified Data Engineer Associate           (Databricks)
  `dbgenai` — Databricks Certified Generative AI Engineer Associate  (Databricks)
  `gcgenai` — Google Cloud Certified Generative AI Leader            (Google Cloud)

PROVENANCE — these are OFFICIAL outlines, not derived ones
-----------------------------------------------------------
Domains and tasks below are transcribed from each vendor's official guide:

  AE:      "dbt Analytics Engineering Certification Exam Study Guide", updated for
           dbt Core 1.11 — 7 numbered topics with their sub-topics.
           https://www.getdbt.com/dbt-assets/certifications/dbt-certificate-study-guide-version-1-11
  ARCH:    "dbt Architect Certification Exam Study Guide V.6.4" — 8 numbered topics.
           https://www.getdbt.com/dbt-assets/dbt-certificate-study-guide-for-cloud-architect
  DBDE:    "Databricks Certified Data Engineer Associate" exam guide, updated
           2026-08-06 — 7 weighted sections.
  DBGENAI: "Databricks Certified Generative AI Engineer Associate" exam guide,
           updated 2026-03-18 — 6 weighted sections.
  GCGENAI: "Generative AI Leader Certification exam guide" (Google Cloud) —
           4 weighted sections with numbered sub-objectives.

Each domain is one official Topic/Section. Each task is one official sub-topic or
objective bullet, with its title quoted from the guide. Keywords are ours (for
classification); titles are the vendor's.

Databricks and Google print their objectives as unnumbered bullets, so the `N.M` task
ids here are ours — assigned in published order. The titles are not.

WEIGHTS: PUBLISHED BY SOME VENDORS, NOT OTHERS
----------------------------------------------
dbt Labs publishes NO per-topic weighting. Both dbt guides state only: "The exam is
scored on a point basis, with 1 point for each correct answer... All questions are
weighted equally." So for `ae` and `arch`, `weight` stays None and the honest proxy is
**sub-topic count** — AE Topic 1 has 14 sub-topics while Topic 4 has 2.
`subtopic_share()` surfaces that proxy, explicitly labelled as derived.

Databricks and Google DO print a percentage per section. For those tracks `weight`
holds the real published number and `weights_published` is True. Never mix the two:
`official_weights()` returns real weights or nothing, and `study_share()` says which
of the two it handed back.

PASSING SCORE: PUBLISHED BY dbt LABS ONLY
-----------------------------------------
dbt publishes 65%. Databricks and Google publish no cut score for these exams, so
`passing_score_pct` is None there and `passing_score_published` is False. Do not
quote a pass mark for a track that does not publish one.
"""
from __future__ import annotations

from typing import Optional

# --------------------------------------------------------------------------- #
# Exam-level facts. Every one is stated in the official study guide.
# --------------------------------------------------------------------------- #

EXAM_FACTS = {
    "ae": {
        "id": "ae",
        "code": "DBTAE",
        "vendor": "dbt Labs",
        "name": "dbt Analytics Engineering Certification Exam",
        "duration_minutes": 120,
        "question_count": 65,
        "question_count_range": None,
        "passing_score_pct": 65,
        "passing_score_published": True,
        "cost_usd": 200,
        "delivery": "online proctored",
        "validity_years": 2,
        "languages": ["English", "Japanese"],
        "target_version": "dbt Core 1.11",
        "guide_version": "updated for dbt Core 1.11",
        "recommended_experience": "SQL proficiency and 6+ months of dbt experience",
        "weights_published": False,
        "authoritative_hosts": ("docs.getdbt.com", "getdbt.com", "learn.getdbt.com"),
        "doc_root": "https://docs.getdbt.com",
        "exam_guide_url": "https://www.getdbt.com/certifications/analytics-engineer-certification-exam",
        "study_guide_url": "https://www.getdbt.com/dbt-assets/certifications/dbt-certificate-study-guide-version-1-11",
        "official_url": "https://www.getdbt.com/dbt-certification",
        "unscored_note": (
            "An undisclosed number of unscored research questions are mixed in and "
            "are indistinguishable from scored ones, so not all 65 questions count "
            "toward the score."
        ),
        "scope_statement": (
            "Evaluates your ability to build, test, and maintain models to make data "
            "accessible to others, and to use dbt to apply engineering principles to "
            "analytics infrastructure."
        ),
    },
    "arch": {
        "id": "arch",
        "code": "DBTARCH",
        "vendor": "dbt Labs",
        "name": "dbt Architect Certification Exam",
        "duration_minutes": 120,
        "question_count": 65,
        "question_count_range": None,
        "passing_score_pct": 65,
        "passing_score_published": True,
        "cost_usd": 200,
        "delivery": "online proctored",
        "validity_years": 2,
        "languages": ["English", "Japanese", "French"],
        "target_version": None,
        "guide_version": "V.6.4",
        "recommended_experience": (
            "SQL proficiency and at least six months administrating an Enterprise "
            "dbt account"),
        "weights_published": False,
        "authoritative_hosts": ("docs.getdbt.com", "getdbt.com", "learn.getdbt.com"),
        "doc_root": "https://docs.getdbt.com",
        "exam_guide_url": "https://www.getdbt.com/certifications/dbt-architect-certification-exam",
        "study_guide_url": "https://www.getdbt.com/dbt-assets/dbt-certificate-study-guide-for-cloud-architect",
        "official_url": "https://www.getdbt.com/dbt-certification",
        "unscored_note": (
            "An undisclosed number of unscored research questions are mixed in and "
            "are indistinguishable from scored ones, so not all 65 questions count "
            "toward the score."
        ),
        "scope_statement": (
            "Assesses your ability to design secure, scalable dbt implementations, with "
            "a focus on environment orchestration, role-based access control, "
            "integrations with other tools, and collaborative development workflows "
            "aligned with best practices."
        ),
    },
    "dbde": {
        "id": "dbde",
        "code": "DBXDE",
        "vendor": "Databricks",
        "name": "Databricks Certified Data Engineer Associate",
        "duration_minutes": 90,
        "question_count": 45,
        "question_count_range": None,
        "passing_score_pct": None,
        "passing_score_published": False,
        "cost_usd": 200,
        "delivery": "online proctored or test center",
        "validity_years": 2,
        "languages": ["English", "Japanese", "Brazilian Portuguese (pt-BR)", "Korean"],
        "target_version": None,
        "guide_version": "exam guide updated 2026-08-06",
        "recommended_experience": (
            "Six months of hands-on experience in the Databricks Platform, against "
            "the listed exam outline"),
        "weights_published": True,
        "authoritative_hosts": (
            "docs.databricks.com", "databricks.com", "learn.databricks.com"),
        "doc_root": "https://docs.databricks.com",
        "exam_guide_url": "https://www.databricks.com/learn/certification/data-engineer-associate",
        "study_guide_url": "https://www.databricks.com/sites/default/files/2026-10/Databricks-Certified-Data-Engineer-Associate-Exam-Guide-August-2026.pdf",
        "official_url": "https://www.databricks.com/learn/certification",
        "unscored_note": (
            "45 items are scored; up to 10 additional unscored items may be included. "
            "They are not identified on the form, do not affect the score, and the "
            "90-minute limit already accounts for them."
        ),
        "scope_statement": (
            "Assesses the ability to use the Databricks Data + AI Platform for "
            "foundational data engineering: the platform, workspace and architecture, "
            "ingestion, loading, transformation and modelling with PySpark and SQL, "
            "Lakeflow Jobs, CI/CD, troubleshooting, monitoring, optimization, and "
            "governance and security."
        ),
    },
    "dbgenai": {
        "id": "dbgenai",
        "code": "DBXGAI",
        "vendor": "Databricks",
        "name": "Databricks Certified Generative AI Engineer Associate",
        "duration_minutes": 90,
        "question_count": 45,
        "question_count_range": None,
        "passing_score_pct": None,
        "passing_score_published": False,
        "cost_usd": 200,
        "delivery": "online proctored or test center",
        "validity_years": 2,
        "languages": ["English", "Japanese", "Brazilian Portuguese (pt-BR)", "Korean"],
        "target_version": None,
        "guide_version": "exam guide updated 2026-03-18",
        "recommended_experience": (
            "6+ months of hands-on experience performing the generative AI solution "
            "tasks outlined in the exam guide"),
        "weights_published": True,
        "authoritative_hosts": (
            "docs.databricks.com", "databricks.com", "learn.databricks.com",
            "mlflow.org"),
        "doc_root": "https://docs.databricks.com",
        "exam_guide_url": "https://www.databricks.com/learn/certification/genai-engineer-associate",
        "study_guide_url": "https://www.databricks.com/sites/default/files/2026-10/databricks-certified-gen-ai-associate-exam-guide-august-2026.pdf",
        "official_url": "https://www.databricks.com/learn/certification",
        "unscored_note": (
            "45 items are scored; up to 10 additional unscored items may be included. "
            "They are not identified on the form, do not affect the score, and the "
            "90-minute limit already accounts for them."
        ),
        "scope_statement": (
            "Assesses the ability to design and implement LLM-enabled solutions on "
            "Databricks: decomposing requirements, choosing models and tools, and "
            "using Vector Search, Model Serving, MLflow and Unity Catalog to build "
            "and deploy RAG applications and agentic systems."
        ),
    },
    "gcgenai": {
        "id": "gcgenai",
        "code": "GCGAIL",
        "vendor": "Google Cloud",
        "name": "Google Cloud Certified — Generative AI Leader",
        "duration_minutes": 90,
        "question_count": None,
        "question_count_range": (50, 60),
        "passing_score_pct": None,
        "passing_score_published": False,
        "cost_usd": 99,
        "delivery": "online-proctored or onsite-proctored",
        "validity_years": 3,
        "languages": ["English", "Japanese", "Spanish"],
        "target_version": None,
        "guide_version": None,
        "recommended_experience": (
            "No prerequisites; aimed at any job role, with or without hands-on "
            "technical experience"),
        "weights_published": True,
        "authoritative_hosts": (
            "cloud.google.com", "services.google.com", "ai.google.dev",
            "developers.google.com", "support.google.com"),
        "doc_root": "https://cloud.google.com/docs",
        "exam_guide_url": "https://cloud.google.com/learn/certification/generative-ai-leader",
        "study_guide_url": "https://services.google.com/fh/files/misc/generative_ai_leader_exam_guide_english.pdf",
        "official_url": "https://cloud.google.com/learn/certification",
        "unscored_note": (
            "Google publishes the exam as 50-60 multiple choice questions and does "
            "not state how many, if any, are unscored."
        ),
        "scope_statement": (
            "Assesses business-level knowledge of generative AI and Google Cloud's "
            "gen AI offerings: gen AI fundamentals, Google Cloud's products and "
            "services, techniques to improve model output, and business strategies "
            "for a successful gen AI solution. Strategic leadership and influence, "
            "not technical implementation."
        ),
    },
}

DEFAULT_TRACK = "ae"

# Per-track wording lives in EXAM_FACTS[track]["unscored_note"]. This stays as the
# dbt-shaped default so existing callers keep working.
UNSCORED_QUESTIONS_NOTE = EXAM_FACTS[DEFAULT_TRACK]["unscored_note"]


# --------------------------------------------------------------------------- #
# Domains == official Topics. Task titles are quoted from the study guides.
# --------------------------------------------------------------------------- #

DOMAINS: dict[str, dict] = {
    # ============================ Analytics Engineering ===================== #
    "ae-01": {
        "track": "ae",
        "dir": "01-developing-and-optimizing-models",
        "title": "Developing and optimizing dbt models",
        "weight": None,
        "provenance": "AE study guide, Topic 01 (14 sub-topics)",
        "tasks": {
            "1.1": ("Identifying and verifying any raw object dependencies", [
                "source(", "{{ source", "sources.yml", "raw table", "raw object",
                "dependency", "dependencies", "upstream", "hard coded",
                "hardcoded table", "database + schema",
            ]),
            "1.2": ("Understanding core dbt materializations", [
                "materialization", "materialized", "view", "table", "ephemeral",
                "materialized_view", "cte", "create table as", "create view as",
                "rebuilt", "persisting",
            ]),
            "1.3": ("Conceptualizing modularity and how to incorporate DRY principles", [
                "modularity", "dry", "refactor", "reusable", "staging", "intermediate",
                "mart", "jinja", "macro", "{% macro", "duplication", "common logic",
                "project structure",
            ]),
            "1.4": ("Using commands such as build, run, test, docs, show, snapshot, and seed", [
                "dbt build", "dbt run", "dbt test", "dbt docs", "dbt show",
                "dbt snapshot", "dbt seed", "dbt compile", "--select", "--exclude",
                "node selection", "graph operator", "dbt docs generate",
            ]),
            "1.5": ("Creating a logical flow of models and building clean DAGs", [
                "dag", "ref(", "{{ ref", "lineage", "build order", "downstream",
                "model flow", "runs after", "execution order", "build in the correct order",
            ]),
            "1.6": ("Defining configurations in dbt_project.yml", [
                "dbt_project.yml", "+materialized", "config-version", "model-paths",
                "seed-paths", "macro-paths", "vars", "project config", "folder config",
                "+tags", "+schema",
            ]),
            "1.7": ("Using dbt Packages", [
                "package", "packages.yml", "dbt deps", "dbt_utils", "dbt-utils",
                "dbt_expectations", "codegen", "audit_helper", "hub.getdbt.com",
                "revision", "install package",
            ]),
            "1.8": ("Creating Python Models", [
                "python model", "dbt.ref", "def model(dbt, session)", "pandas",
                "pyspark", "snowpark", "dataframe", ".py model",
            ]),
            "1.9": ('Providing access to users to models with the "grants" config', [
                "grants", "grant select", "privileges", "copy_grants",
                "database_role", "revoke", "access to users",
            ]),
            "1.10": ("Creating snapshots in YAML", [
                "snapshot", "snapshots.yml", "slowly changing", "scd", "check strategy",
                "timestamp strategy", "unique_key", "updated_at", "check_cols",
                "invalidate_hard_deletes", "dbt_valid_from", "dbt_valid_to",
            ]),
            "1.11": ("Selecting the optimal incremental strategy based on a dataset's characteristics", [
                "incremental", "is_incremental", "incremental_strategy", "merge",
                "append", "delete+insert", "insert_overwrite", "on_schema_change",
                "--full-refresh", "new records", "only new data",
            ]),
            "1.12": ("Validating model logic and schema definitions in dry-runs using the --empty flag", [
                "--empty", "empty flag", "dry run", "dry-run", "zero rows",
                "validate schema", "build --empty",
            ]),
            "1.13": ("Running models in sample mode using the --sample flag", [
                "--sample", "sample mode", "sample flag", "subset of data",
            ]),
            "1.14": ("Understanding advanced dbt materializations such as microbatch", [
                "microbatch", "batch_size", "event_time", "lookback", "begin",
                "backfill", "partitioned batch",
            ]),
        },
    },
    "ae-02": {
        "track": "ae",
        "dir": "02-model-governance",
        "title": "Managing dbt models governance",
        "weight": None,
        "provenance": "AE study guide, Topic 02 (3 sub-topics)",
        "tasks": {
            "2.1": ("Adding contracts to models to ensure the shape of models", [
                "contract", "enforced: true", "model contract", "shape of models",
                "data_type", "column type", "contract enforcement",
            ]),
            "2.2": ("Creating different versions of our models and deprecating the old ones", [
                "model version", "versions:", "latest_version", "deprecation_date",
                "deprecate", "defined_in", "include/exclude",
            ]),
            "2.3": ("Defining constraints in YAML to enforce data integrity at the platform level", [
                "constraint", "constraints:", "check constraint", "primary key",
                "foreign key", "data integrity", "platform level", "warn_unenforced",
            ]),
        },
    },
    "ae-03": {
        "track": "ae",
        "dir": "03-debugging-modeling-errors",
        "title": "Debugging data modeling errors",
        "weight": None,
        "provenance": "AE study guide, Topic 03 (5 sub-topics)",
        "tasks": {
            "3.1": ("Understanding logged error messages", [
                "error message", "logs/dbt.log", "stack trace", "compilation error",
                "database error", "runtime error", "parsing error", "log output",
            ]),
            "3.2": ("Troubleshooting using compiled code", [
                "compiled code", "target/compiled", "target/run", "dbt compile",
                "compiled sql", "rendered sql",
            ]),
            "3.3": ("Troubleshooting .yml compilation errors", [
                "yml", "yaml error", "indentation", "invalid configuration",
                "properties file", "schema.yml", "yaml compilation",
            ]),
            "3.4": ("Developing and implementing a fix and testing it prior to merging", [
                "feature branch", "pull request", "git pull", "git fetch",
                "before merging", "code review", "head branch", "merge conflict",
            ]),
            "3.5": ("Managing dbt behavior with flags", [
                "flags", "global config", "behavior change", "--fail-fast",
                "--warn-error", "--no-partial-parse", "flags:", "behavior flag",
            ]),
        },
    },
    "ae-04": {
        "track": "ae",
        "dir": "04-troubleshooting-pipelines",
        "title": "Troubleshooting and optimizing dbt pipelines",
        "weight": None,
        "provenance": "AE study guide, Topic 04 (2 sub-topics)",
        "tasks": {
            "4.1": ("Troubleshooting and managing failure points in the DAG", [
                "failure point", "skipped", "downstream model", "blocked",
                "dag failure", "partial failure", "fail-fast", "test-before-model",
                "skip relation",
            ]),
            "4.2": ("Using dbt clone", [
                "dbt clone", "zero-copy", "cloned relation",
            ]),
        },
    },
    "ae-05": {
        "track": "ae",
        "dir": "05-implementing-tests",
        "title": "Implementing dbt tests",
        "weight": None,
        "provenance": "AE study guide, Topic 05 (3 sub-topics)",
        "tasks": {
            "5.1": ("Using generic, singular, custom, custom generic, and unit tests on a wide variety of models and sources", [
                "generic test", "singular test", "custom generic test", "unit test",
                "unit_tests:", "unique", "not_null", "accepted_values", "relationships",
                "data_tests:", "tests:", "given", "expect", "fixture", "mock input",
            ]),
            "5.2": ("Testing assumptions for dbt models and sources", [
                "assumption", "test a source", "source test", "data quality",
                "severity", "warn_if", "error_if", "store_failures", "where config",
                "threshold",
            ]),
            "5.3": ("Implementing various testing steps in the workflow", [
                "testing workflow", "test before", "ci test", "when to test",
                "test ordering", "test in the pipeline",
            ]),
        },
    },
    "ae-06": {
        "track": "ae",
        "dir": "06-external-dependencies",
        "title": "Implementing and maintaining external dependencies",
        "weight": None,
        "provenance": "AE study guide, Topic 06 (2 sub-topics)",
        "tasks": {
            "6.1": ("Implementing dbt exposures", [
                "exposure", "exposures:", "dashboard", "downstream consumer",
                "maturity", "exposure type", "depends_on",
            ]),
            "6.2": ("Implementing source freshness", [
                "source freshness", "dbt source freshness", "loaded_at_field",
                "freshness:", "warn_after", "error_after", "stale source",
            ]),
        },
    },
    "ae-07": {
        "track": "ae",
        "dir": "07-dbt-state",
        "title": "Leveraging the dbt state",
        "weight": None,
        "provenance": "AE study guide, Topic 07 (2 sub-topics)",
        "tasks": {
            "7.1": ("Understanding state and state selection", [
                "state:modified", "state:new", "--state", "defer", "--defer",
                "--favor-state", "manifest.json", "run_results.json", "artifact",
                "state selection", "slim ci",
            ]),
            "7.2": ("Using dbt retry", [
                "dbt retry", "rerun failed", "previous invocation", "resume",
            ]),
        },
    },

    # ================================= Architect ============================= #
    "arch-01": {
        "track": "arch",
        "dir": "01-warehouse-connections",
        "title": "Configuring dbt data warehouse connections",
        "weight": None,
        "provenance": "Architect study guide, Topic 1 (5 sub-topics)",
        "tasks": {
            "1.1": ("Understanding how to connect the warehouse", [
                "warehouse connection", "account-level connection", "snowflake",
                "databricks", "bigquery", "redshift", "connection settings",
                "extended attributes",
            ]),
            "1.2": ("Configuring IP whitelist", [
                "ip whitelist", "ip allowlist", "ip restriction", "allowlist",
                "static ip", "firewall", "network policy", "egress ip",
            ]),
            "1.3": ("Creating and testing a connection for the project", [
                "test connection", "project connection", "connection test",
                "connection credentials", "connection failure",
            ]),
            "1.4": ("Authenticating through OAuth to access the data in dbt", [
                "oauth", "development credentials", "access token", "token expire",
                "re-authorize", "sso-based connection", "identity provider",
            ]),
            "1.5": ("Adding Client ID and Secret for OAuth", [
                "client id", "client secret", "oauth app", "security integration",
                "redirect uri",
            ]),
        },
    },
    "arch-02": {
        "track": "arch",
        "dir": "02-git-connections",
        "title": "Configuring dbt git connections",
        "weight": None,
        "provenance": "Architect study guide, Topic 2 (2 sub-topics)",
        "tasks": {
            "2.1": ("Connecting the git repo to dbt", [
                "git repo", "repository", "deploy key", "git clone",
                "connect repository", "managed repository", "ssh key",
            ]),
            "2.2": ("Setting up integrations with git providers", [
                "github", "gitlab", "azure devops", "native integration",
                "git provider", "pull request", "merge request",
            ]),
        },
    },
    "arch-03": {
        "track": "arch",
        "dir": "03-environments",
        "title": "Creating and maintaining dbt environments",
        "weight": None,
        "provenance": "Architect study guide, Topic 3 (8 sub-topics)",
        "tasks": {
            "3.1": ("Understanding access control to different environments", [
                "environment access", "access control", "environment permission",
                "restrict environment",
            ]),
            "3.2": ("Determining when to use a service account", [
                "service account", "deployment credentials", "non-human",
                "production credentials", "automated deployment",
            ]),
            "3.3": ("Rotating key pair authentication via the API", [
                "key pair", "keypair", "rotate", "rotation", "private key",
                "admin api credentials",
            ]),
            "3.4": ("Understanding environment variables", [
                "environment variable", "env var", "env_var(", "dbt_env_secret",
                "variable override", "secret env var",
            ]),
            "3.5": ("Creating a new dbt deployment environment", [
                "deployment environment", "create environment", "environment type",
                "staging environment", "production environment",
                "development environment",
            ]),
            "3.6": ("Setting a default schema/dataset for environments", [
                "default schema", "custom schema", "dataset", "target schema",
                "generate_schema_name",
            ]),
            "3.7": ("Understanding custom branches and how to configure them to environments", [
                "custom branch", "main branch", "release branch",
                "branch per environment", "git branch setting",
            ]),
            "3.8": ("Configuring dbt to allow deferral to other environments", [
                "deferral", "defer to production", "defer to staging",
                "production environment ref",
            ]),
        },
    },
    "arch-04": {
        "track": "arch",
        "dir": "04-job-definitions",
        "title": "Creating and maintaining job definitions",
        "weight": None,
        "provenance": "Architect study guide, Topic 4 (11 sub-topics)",
        "tasks": {
            "4.1": ("Set up a CI job with deferral", [
                "ci job", "continuous integration", "pr job", "slim ci",
                "ci with deferral", "run on pull request",
            ]),
            "4.2": ("Understanding steps within a dbt job", [
                "job step", "run command", "job command", "steps within",
                "execution step",
            ]),
            "4.3": ("Scheduling a job to run on schedule", [
                "schedule", "cron", "scheduled job", "custom cron", "frequency",
            ]),
            "4.4": ("Implementing run commands in the correct order", [
                "command order", "correct order", "sequence of commands",
                "order of operations",
            ]),
            "4.5": ("Creating a new dbt job", [
                "create job", "new job", "deploy job", "job definition",
            ]),
            "4.6": ("Configuring optional settings such as environment variable overrides, threads, deferral, target name, and dbt version override", [
                "threads", "target name", "dbt version override", "override",
                "optional setting", "job setting", "concurrency",
            ]),
            "4.7": ("Generating documentation on a job that populates the dbt Catalog page", [
                "generate docs", "dbt docs generate", "documentation job",
                "populate catalog", "docs on a job",
            ]),
            "4.8": ("Configuring jobs to be triggered after other dbt jobs (job chaining)", [
                "job chaining", "triggered after", "upstream job", "chained job",
                "on job completion",
            ]),
            "4.9": ("Configuring Advanced CI", [
                "advanced ci", "compare changes", "data diff", "ci cache",
                "code change comparison",
            ]),
            "4.10": ("Configuring self-deferral", [
                "self deferral", "self-defer", "defer to itself",
                "previous run of this job",
            ]),
            "4.11": ("Understanding when to use which type of job deferral", [
                "type of deferral", "which deferral", "defer to environment",
                "defer to job", "deferral choice",
            ]),
        },
    },
    "arch-05": {
        "track": "arch",
        "dir": "05-security-and-licenses",
        "title": "Configuring dbt security and licenses",
        "weight": None,
        "provenance": "Architect study guide, Topic 5 (6 sub-topics)",
        "tasks": {
            "5.1": ("Creating service tokens for API access", [
                "service token", "api token", "token permission", "token scope",
                "administrative api", "discovery api", "semantic layer api",
            ]),
            "5.2": ("Assigning permission sets", [
                "permission set", "enterprise permission", "account admin",
                "job admin", "analyst", "developer permission",
                "project-level permission", "read-only",
            ]),
            "5.3": ("Creating license mappings", [
                "license", "license mapping", "developer license", "read-only license",
                "it license", "seat", "assign license",
            ]),
            "5.4": ("Adding and removing users", [
                "add user", "remove user", "invite", "deactivate", "user management",
                "seat management",
            ]),
            "5.5": ("Adding SSO application for dbt Enterprise", [
                "sso", "single sign-on", "saml", "okta", "azure ad", "entra",
                "google workspace", "scim", "enterprise sso",
            ]),
            "5.6": ("Creating and assigning RBAC", [
                "rbac", "role-based access", "user group", "group mapping",
                "assign role", "sso group",
            ]),
        },
    },
    "arch-06": {
        "track": "arch",
        "dir": "06-monitoring-and-alerting",
        "title": "Setting up monitoring and alerting for jobs",
        "weight": None,
        "provenance": "Architect study guide, Topic 6 (2 sub-topics)",
        "tasks": {
            "6.1": ("Setting up email notifications", [
                "email notification", "notification", "alert", "job outcome",
                "run status notification", "slack", "microsoft teams",
            ]),
            "6.2": ("Using Webhooks for event-driven integrations with other systems", [
                "webhook", "event-driven", "outbound", "http callback",
                "webhook subscription",
            ]),
        },
    },
    "arch-07": {
        "track": "arch",
        "dir": "07-mesh-and-cross-project",
        "title": "Setting up a dbt mesh and leveraging cross-project references",
        "weight": None,
        "provenance": "Architect study guide, Topic 7 (3 sub-topics)",
        "tasks": {
            "7.1": ("Setting up additional dbt projects", [
                "additional project", "multi-project", "dependencies.yml",
                "project dependency", "producer project", "consumer project",
            ]),
            "7.2": ("Understanding how environment types relate to cross-project references", [
                "cross-project", "cross project ref", "environment type",
                "public model ref", "staging environment ref",
            ]),
            "7.3": ("Utilizing model governance", [
                "model governance", "access:", "public", "protected", "private",
                "group:", "governed model",
            ]),
        },
    },
    "arch-08": {
        "track": "arch",
        "dir": "08-dbt-catalog",
        "title": "Configuring and using dbt Catalog",
        "weight": None,
        "provenance": "Architect study guide, Topic 8 (2 sub-topics)",
        "tasks": {
            "8.1": ("Using dbt Catalog to understand the current lineage, troubleshoot issues and optimize cost and performance", [
                "dbt catalog", "lineage", "column-level lineage", "explorer",
                "optimize cost", "model timing", "data health",
            ]),
            "8.2": ("Using dbt Catalog to find public models and cross-project references", [
                "find public model", "catalog search", "discover model",
                "cross-project reference",
            ]),
        },
    },

    # ================ Databricks Certified Data Engineer Associate ========== #
    # Section weights ARE published by Databricks and sum to 100.
    "dbde-01": {
        "track": "dbde",
        "dir": "01-databricks-intelligence-platform",
        "title": "Databricks Intelligence Platform",
        "weight": 6,
        "provenance": "Databricks Data Engineer Associate exam guide, Section 1 (6%)",
        "tasks": {
            "1.1": ("Understand the core components of the Databricks Platform, such as its architecture, Delta Lake, and Unity Catalog", [
                "delta lake", "unity catalog", "lakehouse", "control plane",
                "compute plane", "architecture", "time travel", "acid",
                "metastore", "catalog.schema.table", "three-level namespace",
            ]),
            "1.2": ("Understand Databricks Platform's compute services, including their characteristics, limitations, and cost models, and select the most suitable option for each workload use case", [
                "all-purpose cluster", "job cluster", "sql warehouse", "serverless",
                "classic compute", "dbu", "autoscaling", "auto-termination",
                "single-node", "photon", "instance pool", "cost model",
            ]),
        },
    },
    "dbde-02": {
        "track": "dbde",
        "dir": "02-data-ingestion-and-loading",
        "title": "Data Ingestion and Loading",
        "weight": 21,
        "provenance": "Databricks Data Engineer Associate exam guide, Section 2 (21%)",
        "tasks": {
            "2.1": ("Enable and detail data ingestion patterns, including batch, streaming, and incremental loading, and import data from sources such as local files, Lakeflow Connect standard connectors, and Lakeflow Connect managed connectors", [
                "ingestion pattern", "batch ingestion", "streaming ingestion",
                "incremental load", "lakeflow connect", "standard connector",
                "managed connector", "add data ui", "upload file",
            ]),
            "2.2": ("Use the COPY INTO command to incrementally load files from cloud object storage (ADLS/S3/GCS) into Unity Catalog-governed tables", [
                "copy into", "idempotent", "cloud object storage", "adls", "s3",
                "gcs", "file_format", "copy_options", "format_options",
                "external location", "volume",
            ]),
            "2.3": ("Use Auto Loader with schema enforcement and schema evolution in batch modes (for example, directory listing or file notification) to land data into Unity Catalog-governed tables", [
                "auto loader", "cloudfiles", "cloudFiles.schemaLocation",
                "schema evolution", "schema enforcement", "directory listing",
                "file notification", "rescued data", "_rescued_data",
                "schemaHints", "availableNow",
            ]),
            "2.4": ("Configure Lakeflow Connect to reliably ingest data from diverse enterprise sources into Unity Catalog-governed tables", [
                "lakeflow connect", "ingestion pipeline", "salesforce connector",
                "sql server connector", "workday", "enterprise source",
                "ingestion gateway", "cdc",
            ]),
            "2.5": ("Use JDBC/ODBC or REST clients in notebooks to land data into cloud storage or directly into Unity Catalog-governed tables, usually orchestrated and scheduled with Lakeflow Jobs", [
                "jdbc", "odbc", "rest client", "spark.read.format(\"jdbc\")",
                "partitionColumn", "fetchsize", "driver", "secret scope",
                "lakeflow jobs",
            ]),
            "2.6": ("Prioritize between Auto Loader, Lakeflow Connect (standard and managed connectors), partner connectors, and other ingestion methods based on technical requirements such as data volume, ingestion frequency, data types, and governance needs with Unity Catalog", [
                "choose ingestion", "auto loader vs copy into", "partner connect",
                "ingestion frequency", "data volume", "governance needs",
                "which ingestion method", "trade-off",
            ]),
            "2.7": ("Ingest semi-structured and unstructured data (for example, JSON and nested data) via Lakeflow Connect and other managed connectors into Unity Catalog-governed Delta tables", [
                "semi-structured", "unstructured", "json", "nested data",
                "struct", "variant", "from_json", "explode", "binary file",
            ]),
        },
    },
    "dbde-03": {
        "track": "dbde",
        "dir": "03-data-transformation-and-modeling",
        "title": "Data Transformation and Modeling",
        "weight": 22,
        "provenance": "Databricks Data Engineer Associate exam guide, Section 3 (22%)",
        "tasks": {
            "3.1": ("Implement data cleaning by reading bronze tables with PySpark/SQL, cleaning nulls, standardizing data types, and writing to new silver tables", [
                "bronze", "silver", "medallion", "data cleaning", "null handling",
                "na.drop", "fillna", "cast", "standardize data type", "coalesce(",
            ]),
            "3.2": ("Combine DataFrames with operations such as Inner join, left join, broadcast join, multiple keys, cross join, union, and union all", [
                "inner join", "left join", "broadcast join", "cross join",
                "union", "unionAll", "unionByName", "join keys", "semi join",
                "anti join",
            ]),
            "3.3": ("Manipulate columns, rows, and table structures by adding, dropping, splitting, renaming column names, applying filters, and exploding arrays", [
                "withColumn", "withColumnRenamed", "drop(", "select(", "filter(",
                "where(", "split(", "explode", "array", "alias",
            ]),
            "3.4": ("Perform data deduplication operations and aggregate operations on DataFrames, such as count, approximate count distinct, and mean, summary", [
                "dropDuplicates", "distinct", "deduplication", "groupBy", "agg(",
                "approx_count_distinct", "count(", "mean", "summary", "window function",
                "row_number",
            ]),
            "3.5": ("Understand the basic tuning parameters (spark.sql.shuffle.partitions, spark.default.parallelism, spark.executor/driver.memory, spark.sql.autoBroadcastJoinThreshold) and re-measure the performance", [
                "spark.sql.shuffle.partitions", "spark.default.parallelism",
                "spark.executor.memory", "spark.driver.memory",
                "spark.sql.autoBroadcastJoinThreshold", "adaptive query execution",
                "aqe", "tuning", "re-measure",
            ]),
            "3.6": ("Understand the difference between, and how to build, Gold layer objects such as materialized views, views, streaming tables, and tables for BI and analytics teams in Unity Catalog", [
                "gold layer", "materialized view", "streaming table", "view",
                "create or refresh", "declarative pipeline", "bi", "serving layer",
            ]),
            "3.7": ("Apply data quality checks and validation rules to ensure reliable Silver and Gold datasets", [
                "data quality", "expectations", "expect_or_drop", "expect_or_fail",
                "constraint", "validation rule", "quarantine", "check constraint",
            ]),
        },
    },
    "dbde-04": {
        "track": "dbde",
        "dir": "04-working-with-lakeflow-jobs",
        "title": "Working with Lakeflow Jobs",
        "weight": 16,
        "provenance": "Databricks Data Engineer Associate exam guide, Section 4 (16%)",
        "tasks": {
            "4.1": ("Implement control flows (retries and conditional tasks such as branching and looping) using Lakeflow Jobs for pipeline orchestration", [
                "retry policy", "conditional task", "if/else task", "for each task",
                "branching", "looping", "run if", "control flow", "task dependency condition",
            ]),
            "4.2": ("Configure common tasks (notebook, SQL query, dashboard, and pipeline tasks) and their dependencies using Lakeflow Jobs and its DAG-based task graph", [
                "notebook task", "sql task", "dashboard task", "pipeline task",
                "task graph", "dag", "depends on", "job parameter", "task values",
            ]),
            "4.3": ("Implement job schedules using Lakeflow Jobs with an understanding of trigger types (scheduled, file arrival, and table update)", [
                "scheduled trigger", "file arrival trigger", "table update trigger",
                "cron", "continuous trigger", "manual trigger", "schedule",
            ]),
            "4.4": ("Choose between time-based and data-driven triggers based on data availability and pipeline dependencies", [
                "time-based trigger", "data-driven trigger", "data availability",
                "unpredictable arrival", "idle compute cost", "polling",
            ]),
        },
    },
    "dbde-05": {
        "track": "dbde",
        "dir": "05-implementing-ci-cd",
        "title": "Implementing CI/CD",
        "weight": 10,
        "provenance": "Databricks Data Engineer Associate exam guide, Section 5 (10%)",
        "tasks": {
            "5.1": ("Manage your code development workflow within the Databricks workspace UI, including creating and switching between branches in Databricks Git folders (formerly Databricks Repos), committing and pushing changes, and creating pull requests using Databricks Git integration", [
                "git folder", "databricks repos", "branch", "commit", "push",
                "pull request", "git integration", "sparse checkout",
            ]),
            "5.2": ("Understand environment-specific configuration using Declarative Automation Bundle (formerly Databricks Asset Bundles) variables and overrides while promoting the same codebase across dev, test, and prod targets", [
                "databricks.yml", "variables block", "targets", "override",
                "BUNDLE_VAR_", "dev target", "prod target", "asset bundle",
                "declarative automation bundle", "dab",
            ]),
            "5.3": ("Deploy Declarative Automation Bundles (formerly Databricks Asset Bundles) to package, configure, and promote Lakeflow Jobs, Lakeflow Declarative Pipelines, and other workspace assets across dev, test, and prod environments", [
                "bundle deploy", "promote", "package", "resources", "workspace asset",
                "declarative pipeline", "dab", "asset bundle",
            ]),
            "5.4": ("Understand the Databricks CLI to validate, deploy, and manage Declarative Automation Bundles (formerly Databricks Asset Bundles) and other workspace assets in automated CI/CD workflows", [
                "databricks cli", "bundle validate", "bundle deploy", "bundle run",
                "bundle destroy", "service principal", "oauth", "ci/cd workflow",
            ]),
        },
    },
    "dbde-06": {
        "track": "dbde",
        "dir": "06-troubleshooting-monitoring-and-optimization",
        "title": "Troubleshooting, Monitoring, and Optimization",
        "weight": 10,
        "provenance": "Databricks Data Engineer Associate exam guide, Section 6 (10%)",
        "tasks": {
            "6.1": ("Identify trends in job performance using the Lakeflow Jobs run history view to compare current execution times against historical baselines", [
                "run history", "job duration", "historical baseline", "trend",
                "performance regression", "job run list",
            ]),
            "6.2": ("Use the Lakeflow Jobs UI to monitor pipeline health by interpreting job statuses, viewing DAG-based task graphs to spot upstream blockers, and tracking pipeline run times and failure rates", [
                "job status", "timed out", "failure rate", "task graph",
                "upstream blocker", "pipeline health", "run duration threshold",
                "task run duration",
            ]),
            "6.3": ("Identify common performance bottlenecks such as data skew, shuffling, and disk spilling by interpreting stage-level metrics in the Spark UI", [
                "spark ui", "data skew", "shuffle read", "spill", "stage metrics",
                "task summary", "salting", "skew join", "straggler",
            ]),
            "6.4": ("Understand the features of Liquid Clustering and predictive optimization", [
                "liquid clustering", "cluster by", "predictive optimization",
                "optimize", "zorder", "auto compaction", "file size",
            ]),
            "6.5": ("Diagnose cluster startup failures, library conflicts, and out-of-memory issues", [
                "cluster startup failure", "library conflict", "out of memory",
                "oom", "driver crash", "init script", "event log", "dependency conflict",
            ]),
        },
    },
    "dbde-07": {
        "track": "dbde",
        "dir": "07-governance-and-security",
        "title": "Governance and Security",
        "weight": 15,
        "provenance": "Databricks Data Engineer Associate exam guide, Section 7 (15%)",
        "tasks": {
            "7.1": ("Differentiate between managed and external tables in Unity Catalog and perform basic operations (create, modify, delete, and convert between managed and external tables) on them", [
                "managed table", "external table", "location", "drop table",
                "set managed", "set external", "convert table", "managed storage",
            ]),
            "7.2": ("Configure access controls using the UI and SQL by applying GRANT, REVOKE, and DENY privileges to principals (users, groups, and service principals) at appropriate levels of the security hierarchy", [
                "grant", "revoke", "deny", "privilege", "principal",
                "service principal", "group", "securable", "use catalog",
                "use schema", "select on", "ownership",
            ]),
            "7.3": ("Understand column-level masking and row-level security to restrict data visibility based on user groups", [
                "column mask", "row filter", "row-level security",
                "is_account_group_member", "masking function", "set masking policy",
                "current_user",
            ]),
            "7.4": ("Understand Unity Catalog ABAC policies to centrally control row-level filtering and column masking for sensitive data", [
                "abac", "attribute-based access control", "policy", "governed tag",
                "tag policy", "central policy", "sensitive data",
            ]),
        },
    },

    # ========= Databricks Certified Generative AI Engineer Associate ======== #
    "dbgenai-01": {
        "track": "dbgenai",
        "dir": "01-design-applications",
        "title": "Design Applications",
        "weight": 14,
        "provenance": "Databricks Generative AI Engineer Associate exam guide, Section 1 (14%)",
        "tasks": {
            "1.1": ("Design a prompt that elicits a specifically formatted response", [
                "prompt design", "output format", "json output", "structured output",
                "response schema", "formatting instruction", "few-shot",
            ]),
            "1.2": ("Select model tasks to accomplish a given business requirement", [
                "model task", "summarization", "classification", "extraction",
                "translation", "business requirement", "task decomposition",
            ]),
            "1.3": ("Select chain components for a desired model input and output", [
                "chain component", "retriever", "prompt template", "output parser",
                "llm", "pipeline component", "langchain",
            ]),
            "1.4": ("Translate business use case goals into a description of the desired inputs and outputs for the AI pipeline", [
                "use case goal", "desired input", "desired output", "ai pipeline",
                "requirements", "problem decomposition",
            ]),
            "1.5": ("Define and order tools that gather knowledge or take actions for multi-stage reasoning", [
                "tool calling", "function calling", "multi-stage reasoning",
                "tool order", "agent tool", "react", "action",
            ]),
            "1.6": ("Determine how and when to use Agent Bricks (Knowledge Assistant, Multiagent Supervisor, Information Extraction) to solve problems", [
                "agent bricks", "knowledge assistant", "multiagent supervisor",
                "information extraction", "no-code agent",
            ]),
        },
    },
    "dbgenai-02": {
        "track": "dbgenai",
        "dir": "02-data-preparation",
        "title": "Data Preparation",
        "weight": 14,
        "provenance": "Databricks Generative AI Engineer Associate exam guide, Section 2 (14%)",
        "tasks": {
            "2.1": ("Apply a chunking strategy for a given document structure and model constraints", [
                "chunking", "chunk size", "chunk overlap", "recursive splitter",
                "token limit", "context window", "document structure",
            ]),
            "2.2": ("Filter extraneous content in source documents that degrades quality of a RAG application", [
                "extraneous content", "boilerplate", "header footer", "noise",
                "cleaning", "rag quality", "deduplicate documents",
            ]),
            "2.3": ("Choose the appropriate Python package to extract document content from provided source data and format", [
                "pypdf", "unstructured", "beautifulsoup", "python package",
                "document extraction", "ocr", "parser", "html parsing",
            ]),
            "2.4": ("Define operations and sequence to write given chunked text into Delta Lake tables in Unity Catalog", [
                "delta lake", "unity catalog", "write chunks", "change data feed",
                "delta table", "sequence of operations", "primary key",
            ]),
            "2.5": ("Identify needed source documents that provide necessary knowledge and quality for a given RAG application", [
                "source document", "knowledge coverage", "corpus", "document selection",
                "data quality", "rag application",
            ]),
            "2.6": ("Use tools and metrics to evaluate retrieval performance", [
                "retrieval metric", "recall@k", "precision@k", "ndcg", "mrr",
                "retrieval evaluation", "hit rate",
            ]),
            "2.7": ("Design retrieval systems using advanced chunking strategies", [
                "advanced chunking", "semantic chunking", "parent document retriever",
                "hierarchical chunk", "windowed chunk", "metadata filter",
            ]),
            "2.8": ("Explain the role of re-ranking in the information retrieval process", [
                "re-ranking", "reranker", "cross-encoder", "candidate set",
                "two-stage retrieval", "relevance ordering",
            ]),
        },
    },
    "dbgenai-03": {
        "track": "dbgenai",
        "dir": "03-application-development",
        "title": "Application Development",
        "weight": 30,
        "provenance": "Databricks Generative AI Engineer Associate exam guide, Section 3 (30%)",
        "tasks": {
            "3.1": ("Select Langchain/similar tools for use in a Generative AI application", [
                "langchain", "llamaindex", "framework selection", "orchestration library",
                "runnable", "lcel",
            ]),
            "3.2": ("Qualitatively assess responses to identify common issues such as quality and safety", [
                "qualitative assessment", "hallucination", "toxicity", "safety issue",
                "response quality", "manual review",
            ]),
            "3.3": ("Select chunking strategy based on model & retrieval evaluation", [
                "chunking strategy", "evaluation driven", "chunk tuning",
                "retrieval evaluation", "model evaluation",
            ]),
            "3.4": ("Augment a prompt with additional context from a user's input based on key fields, terms, and intents", [
                "prompt augmentation", "context injection", "user intent",
                "key field", "query rewriting", "entity extraction",
            ]),
            "3.5": ("Create a prompt that adjusts an LLM's response from a baseline to a desired output", [
                "prompt iteration", "baseline response", "desired output",
                "system prompt", "instruction tuning prompt",
            ]),
            "3.6": ("Implement LLM guardrails to prevent negative outcomes", [
                "guardrail", "safety filter", "content moderation", "refusal",
                "prompt injection defense", "ai gateway guardrails",
            ]),
            "3.7": ("Select the best LLM based on the attributes of the application to be developed", [
                "model selection", "latency", "cost per token", "context length",
                "open model", "proprietary model", "foundation model api",
            ]),
            "3.8": ("Select an embedding model context length based on source documents, expected queries, and optimization strategy", [
                "embedding model", "embedding context length", "bge", "gte",
                "max sequence length", "truncation",
            ]),
            "3.9": ("Select a model from a model hub or marketplace for a task based on model metadata/model cards", [
                "model card", "model hub", "marketplace", "model metadata",
                "license", "intended use",
            ]),
            "3.10": ("Select the best model for a given task based on common metrics generated in experiments", [
                "mlflow experiment", "metric comparison", "benchmark",
                "evaluation run", "best model", "rouge", "bleu",
            ]),
            "3.11": ("Utilize MLflow and Agent Framework for developing agentic systems", [
                "mlflow", "agent framework", "chatagent", "responsesagent",
                "mlflow tracing", "log_model", "agentic system",
            ]),
            "3.12": ("Compare the evaluation and monitoring phases of the Gen AI application life cycle", [
                "evaluation phase", "monitoring phase", "lifecycle", "offline eval",
                "online monitoring", "pre-deployment", "post-deployment",
            ]),
            "3.13": ("Enable multi-agent systems to leverage Genie Spaces or conversational API to retrieve data", [
                "genie space", "conversational api", "multi-agent", "text-to-sql",
                "structured data retrieval", "genie",
            ]),
        },
    },
    "dbgenai-04": {
        "track": "dbgenai",
        "dir": "04-assembling-and-deploying-applications",
        "title": "Assembling and Deploying Applications",
        "weight": 22,
        "provenance": "Databricks Generative AI Engineer Associate exam guide, Section 4 (22%)",
        "tasks": {
            "4.1": ("Code a chain using a pyfunc model with pre- and post-processing", [
                "pyfunc", "python_function", "pre-processing", "post-processing",
                "predict(", "custom model", "mlflow pyfunc",
            ]),
            "4.2": ("Control access to resources from model serving endpoints", [
                "model serving", "endpoint permission", "on-behalf-of-user",
                "service principal", "resource access", "automatic authentication",
            ]),
            "4.3": ("Code a simple chain according to requirements", [
                "simple chain", "prompt | llm", "lcel", "chain code", "invoke(",
            ]),
            "4.4": ("Choose the basic elements needed to create a RAG application: model flavor, embedding model, retriever, dependencies, input examples, model signature", [
                "model flavor", "model signature", "input example", "retriever",
                "dependencies", "pip_requirements", "rag application",
            ]),
            "4.5": ("Register the model to Unity Catalog using MLflow", [
                "register model", "unity catalog", "mlflow.register_model",
                "catalog.schema.model", "model alias", "model version",
            ]),
            "4.6": ("Create and query a Vector Search index", [
                "vector search index", "create index", "similarity_search",
                "delta sync index", "direct vector access index", "query index",
            ]),
            "4.7": ("Identify how to serve an LLM application that leverages Foundation Model APIs", [
                "foundation model api", "pay-per-token", "provisioned throughput",
                "serving endpoint", "external model",
            ]),
            "4.8": ("Explain the key concepts and components of Mosaic AI Vector Search", [
                "mosaic ai vector search", "vector search endpoint", "embedding column",
                "source table", "sync", "hybrid search",
            ]),
            "4.9": ("Identify batch inference workloads and apply ai_query() appropriately", [
                "ai_query", "batch inference", "sql inference", "throughput",
                "batch scoring",
            ]),
            "4.10": ("Configure vector search for a particular solution based on number of embeddings, update frequency, latency, and cost requirements", [
                "number of embeddings", "update frequency", "latency requirement",
                "cost requirement", "sync mode", "triggered sync", "continuous sync",
            ]),
            "4.11": ("Configure a persistent datastore to store and retrieve intermediate memory or structured information", [
                "persistent datastore", "memory", "conversation state",
                "checkpoint", "delta table state", "lakebase",
            ]),
            "4.12": ("Apply CI/CD best practices such as updating a Vector Search index, promoting prompts across environments, and testing individual components of an agent", [
                "ci/cd", "promote prompt", "update index", "component test",
                "asset bundle", "environment promotion",
            ]),
            "4.13": ("Integrate managed, external, and custom MCP servers based on a given application requirements", [
                "mcp", "model context protocol", "managed mcp", "external mcp",
                "custom mcp server", "tool server",
            ]),
            "4.14": ("Apply prompt version control and manage prompt lifecycle", [
                "prompt registry", "prompt version", "prompt lifecycle",
                "prompt alias", "version control",
            ]),
            "4.15": ("Develop an appropriate interactive user facing interface for an agent usage scenario (Apps, Slack, Teams, etc.)", [
                "databricks apps", "slack", "teams", "user interface",
                "chat ui", "front end",
            ]),
        },
    },
    "dbgenai-05": {
        "track": "dbgenai",
        "dir": "05-governance",
        "title": "Governance",
        "weight": 8,
        "provenance": "Databricks Generative AI Engineer Associate exam guide, Section 5 (8%)",
        "tasks": {
            "5.1": ("Use masking techniques as guard rails to meet a performance objective", [
                "masking", "pii redaction", "anonymization", "guard rail",
                "column mask", "sensitive field",
            ]),
            "5.2": ("Select guardrail techniques to protect against malicious user inputs to a Gen AI application", [
                "prompt injection", "jailbreak", "malicious input", "input validation",
                "guardrail technique", "ai gateway",
            ]),
            "5.3": ("Use legal/licensing requirements for data sources to avoid legal risk", [
                "license", "copyright", "legal risk", "terms of use",
                "data source licensing", "commercial use",
            ]),
            "5.4": ("Recommend an alternative for problematic text mitigation in a data source feeding a GenAI application", [
                "problematic text", "mitigation", "toxic content", "bias in corpus",
                "replace source", "filtering alternative",
            ]),
        },
    },
    "dbgenai-06": {
        "track": "dbgenai",
        "dir": "06-evaluation-and-monitoring",
        "title": "Evaluation and Monitoring",
        "weight": 12,
        "provenance": "Databricks Generative AI Engineer Associate exam guide, Section 6 (12%)",
        "tasks": {
            "6.1": ("Select an LLM choice (size and architecture) based on a set of quantitative evaluation metrics", [
                "model size", "architecture", "quantitative metric",
                "evaluation metric", "model comparison", "parameter count",
            ]),
            "6.2": ("Select key metrics to monitor for a specific LLM deployment scenario", [
                "key metric", "latency", "throughput", "token usage",
                "error rate", "monitoring metric",
            ]),
            "6.3": ("Evaluate agent performance using MLflow scoring and tracing", [
                "mlflow evaluate", "mlflow tracing", "trace", "span",
                "agent evaluation", "scoring",
            ]),
            "6.4": ("Use inference logging to assess deployed RAG application performance", [
                "inference logging", "payload logging", "deployed performance",
                "request log", "response log",
            ]),
            "6.5": ("Use Databricks features to control LLM costs", [
                "cost control", "rate limit", "token budget", "provisioned throughput",
                "caching", "usage tracking",
            ]),
            "6.6": ("Use inference tables and Agent Monitoring to track a live LLM endpoint", [
                "inference table", "agent monitoring", "live endpoint",
                "production monitoring", "payload table",
            ]),
            "6.7": ("Identify evaluation judges that require ground truth", [
                "llm judge", "ground truth", "reference answer", "correctness judge",
                "groundedness", "answer relevance",
            ]),
            "6.8": ("Use AI Gateway (Inference Tables, Usage Tables, and rate limiting) to track an LLM or agent deployed via Agent Framework", [
                "ai gateway", "usage table", "rate limiting", "inference table",
                "agent framework", "gateway policy",
            ]),
            "6.9": ("Use Databricks custom Scorers for evaluating agents and LLMs", [
                "custom scorer", "scorer", "@scorer", "custom metric",
                "evaluation harness",
            ]),
        },
    },

    # ============ Google Cloud Certified — Generative AI Leader ============= #
    "gcgenai-01": {
        "track": "gcgenai",
        "dir": "01-fundamentals-of-gen-ai",
        "title": "Fundamentals of gen AI",
        "weight": 30,
        "provenance": "Google Cloud Generative AI Leader exam guide, Section 1 (~30%)",
        "tasks": {
            "1.1": ("Describe core generative AI (gen AI) concepts and use cases", [
                "artificial intelligence", "machine learning", "natural language processing",
                "foundation model", "multimodal", "diffusion model", "large language model",
                "supervised", "unsupervised", "reinforcement", "ml lifecycle",
                "prompt tuning",
            ]),
            "1.2": ("Describe how various data types are used in gen AI and the business implications", [
                "structured data", "unstructured data", "labeled data", "unlabeled data",
                "data quality", "data accessibility", "completeness", "consistency",
                "relevance",
            ]),
            "1.3": ("Identify the core layers of the gen AI landscape and the business implications", [
                "infrastructure layer", "models layer", "platforms layer",
                "agents layer", "applications layer", "gen ai landscape",
            ]),
            "1.4": ("Identify the use cases and strengths of Google's foundation models", [
                "gemini", "gemma", "imagen", "veo", "foundation model strengths",
                "model choice", "modality",
            ]),
        },
    },
    "gcgenai-02": {
        "track": "gcgenai",
        "dir": "02-google-cloud-gen-ai-offerings",
        "title": "Google Cloud's gen AI offerings",
        "weight": 35,
        "provenance": "Google Cloud Generative AI Leader exam guide, Section 2 (~35%)",
        "tasks": {
            "2.1": ("Describe Google Cloud's strengths in the field of gen AI", [
                "ai-first", "enterprise-ready", "hypercomputer", "tpu", "gpu",
                "open approach", "data control", "democratize ai", "low-code",
                "responsible secure private",
            ]),
            "2.2": ("Describe how Google Cloud's prebuilt gen AI offerings enable AI powered work", [
                "gemini app", "gemini advanced", "gems", "gemini enterprise",
                "gemini for google workspace", "multimodal search", "notebook api",
            ]),
            "2.3": ("Describe how Google Cloud's gen AI offerings improve the customer experience", [
                "agent search", "google search", "customer engagement suite",
                "conversational agents", "agent assist", "conversational insights",
                "contact center as a service", "ccaas",
            ]),
            "2.4": ("Describe how Google Cloud empowers developers to build with AI", [
                "agent platform", "model garden", "automl", "rag api",
                "prebuilt rag", "custom agent", "build with ai",
            ]),
            "2.5": ("Define the purpose and types of tooling for gen AI agents", [
                "extensions", "functions", "data stores", "plugins",
                "agent studio", "google ai studio", "speech-to-text",
                "text-to-speech", "translation api", "document ai", "cloud vision",
                "natural language api", "cloud run", "cloud functions",
            ]),
        },
    },
    "gcgenai-03": {
        "track": "gcgenai",
        "dir": "03-techniques-to-improve-model-output",
        "title": "Techniques to improve gen AI model output",
        "weight": 20,
        "provenance": "Google Cloud Generative AI Leader exam guide, Section 3 (~20%)",
        "tasks": {
            "3.1": ("Describe how to proactively overcome foundation model limitations", [
                "knowledge cutoff", "hallucination", "bias", "fairness", "edge case",
                "data dependency", "grounding", "fine-tuning", "human in the loop",
                "hitl", "drift monitoring", "model versioning",
            ]),
            "3.2": ("Describe prompt engineering techniques and how they drive better results", [
                "prompt engineering", "zero-shot", "one-shot", "few-shot",
                "role prompting", "prompt chaining", "chain-of-thought", "react",
            ]),
            "3.3": ("Identify grounding techniques and their use cases", [
                "grounding", "retrieval-augmented generation", "rag",
                "first-party data", "third-party data", "world data",
                "grounding with google search", "temperature", "top-p",
                "token count", "safety settings", "output length",
            ]),
        },
    },
    "gcgenai-04": {
        "track": "gcgenai",
        "dir": "04-business-strategies",
        "title": "Business strategies for a successful gen AI solution",
        "weight": 15,
        "provenance": "Google Cloud Generative AI Leader exam guide, Section 4 (~15%)",
        "tasks": {
            "4.1": ("Describe the Google Cloud-recommended steps to successfully implement a transformational gen AI solution", [
                "text generation", "image generation", "code generation",
                "business requirement", "technical constraint", "choose the right solution",
                "integrate gen ai", "measure impact", "roi",
            ]),
            "4.2": ("Define secure AI and its importance in protecting AI systems from malicious attacks and misuse", [
                "secure ai framework", "saif", "ml lifecycle security",
                "identity and access management", "iam", "security command center",
                "secure-by-design", "workload monitoring",
            ]),
            "4.3": ("Describe the importance of responsible AI in business", [
                "responsible ai", "transparency", "privacy risk", "anonymization",
                "pseudonymization", "accountability", "explainability",
                "data quality bias fairness",
            ]),
        },
    },
}


# --------------------------------------------------------------------------- #
# Question formats. Both guides list the same six.
# --------------------------------------------------------------------------- #

QUESTION_TYPES = {
    "multiple_choice": {
        "answer_shape": "single letter, e.g. 'B'",
        "partial_credit": False,
    },
    "multiple_response": {
        "answer_shape": "sorted letters, e.g. 'A,C' — exact-set match required",
        "partial_credit": False,
    },
    "fill_in_blank": {
        "answer_shape": "string; graded against `accepted_answers` after normalization",
        "partial_credit": False,
    },
    "matching": {
        "answer_shape": "dict {left_item: right_item}",
        "partial_credit": True,
    },
    "hotspot": {
        "answer_shape": "list of target ids selected from `hotspot_targets`",
        "partial_credit": True,
    },
    "build_list": {
        "answer_shape": "ordered list of item ids — order is graded",
        "partial_credit": True,
    },
    "domc": {
        "answer_shape": "dict {option_letter: 'Y'|'N'} — Discrete Option Multiple Choice",
        "partial_credit": False,
    },
}

NON_LETTER_TYPES = {"fill_in_blank", "matching", "hotspot", "build_list"}

# The official AE sample questions use four OR five options for single-answer items,
# so the gate must not insist on exactly four.
OFFICIAL_OPTION_COUNTS = (4, 5)

DIFFICULTY_LADDER = ["L1", "L2", "L3", "L4", "L5"]

VALID_STATUS = {"unsealed", "verified", "concept-only", "disputed"}

SEAL_CONFIDENCE_FLOOR = 70

# Union of every track's hosts. Use `authoritative_hosts(track)` for anything that
# judges a citation — a dbt claim cited to databricks.com must still fail.
AUTHORITATIVE_HOSTS = tuple(dict.fromkeys(
    h for f in EXAM_FACTS.values() for h in f["authoritative_hosts"]))

ID_PREFIXES = {
    "authored": "Q-AU-{code}",
    "official": "Q-OF-{code}",
    "community": "Q-CO-{code}",
    "practice": "Q-PA-{code}",
}


# --------------------------------------------------------------------------- #
# Derived lookups. Import these rather than recomputing.
# --------------------------------------------------------------------------- #

VALID_TRACKS = tuple(EXAM_FACTS)
VALID_DOMAINS = frozenset(DOMAINS)

# Regex fragment matching any known track id, longest first so that a track id which
# prefixes another cannot shadow it. Import this instead of writing '(ae|arch)'.
TRACK_RE_GROUP = "(" + "|".join(sorted(VALID_TRACKS, key=len, reverse=True)) + ")"


def authoritative_hosts(track: Optional[str] = None) -> tuple[str, ...]:
    """Hosts that count as official for one track, or every known host if track is None."""
    if track is None:
        return AUTHORITATIVE_HOSTS
    facts = EXAM_FACTS.get(track)
    return tuple(facts["authoritative_hosts"]) if facts else AUTHORITATIVE_HOSTS


def hosts_for_domain(domain: str) -> tuple[str, ...]:
    return authoritative_hosts(track_of(domain))


def domains_for(track: str) -> dict[str, dict]:
    return {d: v for d, v in DOMAINS.items() if v["track"] == track}


def track_of(domain: str) -> Optional[str]:
    d = DOMAINS.get(domain)
    return d["track"] if d else None


def domain_dir(domain: str) -> Optional[str]:
    """knowledge/ fragment for a domain, e.g. 'ae/01-developing-and-optimizing-models'."""
    d = DOMAINS.get(domain)
    return f"{d['track']}/{d['dir']}" if d else None


def domain_by_dir(track: str, dirname: str) -> Optional[str]:
    for did, d in DOMAINS.items():
        if d["track"] == track and d["dir"] == dirname:
            return did
    return None


def task_title(domain: str, task_id: str) -> Optional[str]:
    d = DOMAINS.get(domain)
    if not d:
        return None
    entry = d["tasks"].get(task_id)
    return entry[0] if entry else None


def subtopic_share(track: str) -> dict[str, float]:
    """Share of the track's sub-topics held by each domain, as a percentage.

    NOT an official weight. For `ae` and `arch` no per-topic weighting is published, and
    this is the most defensible available proxy: the study guide enumerates sub-topics,
    and a topic with 14 of them plainly covers more ground than one with 2. Use it to
    allocate study time, never to claim what the exam contains.

    For tracks that DO publish weights, prefer `official_weights()` / `study_share()`.
    """
    scope = domains_for(track)
    total = sum(len(d["tasks"]) for d in scope.values()) or 1
    return {did: round(100 * len(d["tasks"]) / total, 1) for did, d in scope.items()}


def official_weights(track: str) -> Optional[dict[str, float]]:
    """Published per-domain weights, or None when the vendor publishes none."""
    if not EXAM_FACTS.get(track, {}).get("weights_published"):
        return None
    return {did: d["weight"] for did, d in domains_for(track).items()}


def study_share(track: str) -> tuple[dict[str, float], bool]:
    """(share_by_domain, is_official). Callers must surface the flag, not bury it."""
    official = official_weights(track)
    return (official, True) if official else (subtopic_share(track), False)


def planning_question_count(track: str) -> int:
    """Question count to plan against. Mid-point when the vendor publishes a range."""
    facts = EXAM_FACTS[track]
    if facts["question_count"] is not None:
        return facts["question_count"]
    lo, hi = facts["question_count_range"]
    return (lo + hi) // 2


def estimated_questions(track: str) -> dict[str, float]:
    """Share applied to the exam length. Exact where weights are published, else a proxy."""
    count = planning_question_count(track)
    share, _ = study_share(track)
    return {did: round(count * pct / 100, 1) for did, pct in share.items()}


def id_prefix(provenance: str, track: str) -> str:
    return ID_PREFIXES[provenance].format(code=EXAM_FACTS[track]["code"])


def classify_domain(text: str, track: Optional[str] = None) -> tuple[Optional[str], int]:
    """Heuristic domain classifier: (domain_id, hit_count). Indicative, not certified."""
    low = (text or "").lower()
    scope = domains_for(track) if track else DOMAINS
    best, best_hits = None, 0
    for did, d in scope.items():
        hits = sum(1 for _, kws in d["tasks"].values() for k in kws if k.lower() in low)
        if hits > best_hits:
            best, best_hits = did, hits
    return best, best_hits


def classify_task(text: str, domain: str) -> tuple[Optional[str], int]:
    """Pick the best-matching task inside an already-known domain."""
    d = DOMAINS.get(domain)
    if not d:
        return None, 0
    low = (text or "").lower()
    best, best_hits = None, 0
    for task_id, (_, kws) in d["tasks"].items():
        hits = sum(1 for k in kws if k.lower() in low)
        if hits > best_hits:
            best, best_hits = task_id, hits
    return best, best_hits
