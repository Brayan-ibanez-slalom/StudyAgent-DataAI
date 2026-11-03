# Git folders, bundles and the Databricks CLI

**Domain:** dbde-05 — Task 5.1, 5.2, 5.3, 5.4
**Verified:** 2026-11-03
**Concepts:** git folder, databricks repos, asset bundle, declarative automation bundle, databricks.yml, targets, bundle variables, BUNDLE_VAR_, databricks cli, bundle validate, bundle deploy

> Seed note. Scope is from the official exam guide; deepen the bundle syntax from the
> linked docs before sealing hard items.

## Why this is on the exam

10% of the exam. The through-line is: the same codebase has to move across dev, test
and prod without being edited, and without secrets in the repo.

## Scope — official objectives

| Task | Objective (verbatim from the exam guide) |
|---|---|
| 5.1 | Manage your code development workflow within the Databricks workspace UI, including creating and switching between branches in Databricks Git folders (formerly Databricks Repos), committing and pushing changes, and creating pull requests using Databricks Git integration |
| 5.2 | Understand environment-specific configuration using Declarative Automation Bundle (formerly Databricks Asset Bundles) variables and overrides while promoting the same codebase across dev, test, and prod targets |
| 5.3 | Deploy Declarative Automation Bundles (formerly Databricks Asset Bundles) to package, configure, and promote Lakeflow Jobs, Lakeflow Declarative Pipelines, and other workspace assets across dev, test, and prod environments |
| 5.4 | Understand the Databricks CLI to validate, deploy, and manage Declarative Automation Bundles (formerly Databricks Asset Bundles) and other workspace assets in automated CI/CD workflows |

## Naming — a live rename

**Databricks Asset Bundles (DABs)** are now called **Declarative Automation Bundles**,
and **Databricks Repos** are now **Databricks Git folders**. The exam guide gives both
names. Treat the old and new names as the same thing; do not eliminate an option
because it uses the older label.

## Which tool for which job

| Need | Use |
|---|---|
| Version, package and promote jobs, pipelines and code across environments | A **bundle**, defined in `databricks.yml` and stored in Git |
| Per-environment differences (warehouse id, schema, schedule) | Bundle **variables** and **target** overrides — not edited source |
| Branch, commit, push and open a PR from inside the workspace | **Git folders** |
| Validate and deploy from CI | The **Databricks CLI** (`bundle validate`, `bundle deploy`, `bundle run`) |

## Secrets

A credential must not be hard-coded in `databricks.yml` or in notebook source. Declare
a variable in the `variables` block and supply its value at deploy time through an
environment variable prefixed **`BUNDLE_VAR_`** (this is the behaviour the exam guide's
own sample answer key endorses), or read it from a secret scope at runtime.

## Traps

- **Trap:** notebook revision history is not version control. Any option resting on it
  is wrong.
- **Trap:** there is no "encrypt the string and commit it" bundle command. Obfuscation
  is not secret management.
- **Trap:** `spark.conf.set("db_pass", ...)` inside a notebook puts the secret in source
  and in the Spark config. Wrong on both counts.
- **Trap:** registering ETL code as a model in Unity Catalog to get versioning is a
  scope error — models version models, bundles version workspace assets.

## Verify before sealing

- [Databricks Asset Bundles](https://docs.databricks.com/aws/en/dev-tools/bundles/)
- [Databricks CLI](https://docs.databricks.com/aws/en/dev-tools/cli/)
