# Unity Catalog governance and security

**Domain:** dbde-07 — Task 7.1, 7.2, 7.3, 7.4
**Verified:** 2026-11-03
**Concepts:** managed table, external table, grant, revoke, deny, principal, service principal, column mask, row filter, is_account_group_member, abac, securable

> Seed note. Scope is from the official exam guide; deepen the privilege model from the
> linked docs before sealing hard items.

## Why this is on the exam

15% of the exam — the second-largest section after transformation. Expect "only this
group may see the real value" and "what happens when I drop this table" scenarios.

## Scope — official objectives

| Task | Objective (verbatim from the exam guide) |
|---|---|
| 7.1 | Differentiate between managed and external tables in Unity Catalog and perform basic operations (create, modify, delete, and convert between managed and external tables) on them |
| 7.2 | Configure access controls using the UI and SQL by applying GRANT, REVOKE, and DENY privileges to principals (users, groups, and service principals) at appropriate levels of the security hierarchy |
| 7.3 | Understand column-level masking and row-level security to restrict data visibility based on user groups |
| 7.4 | Understand Unity Catalog ABAC policies to centrally control row-level filtering and column masking for sensitive data |

## Managed vs external

| | Managed | External |
|---|---|---|
| Who owns the files | Unity Catalog | You, at an explicit `LOCATION` |
| `DROP TABLE` | Deletes the data | Leaves the data in place |
| Maintenance | Databricks can optimize it for you | Yours to manage |

Default to **managed** unless something outside Databricks must read or write the files.

## Restricting what a user sees

| Requirement | Mechanism |
|---|---|
| Some users see a redacted value in one column | **Column mask** — a function on the column, typically branching on `is_account_group_member('<group>')` |
| Some users see only a subset of rows | **Row filter** |
| The same rule applied centrally across many tables by tag/attribute | **ABAC policy** |

## Traps

- **Trap:** maintaining a separate redacted copy of the table per group is the classic
  wrong answer to a masking question — it duplicates data and drifts.
- **Trap:** `DENY` on a column is not how column-level redaction is done; masking is.
  Privileges gate access to objects, masks shape returned values.
- **Trap:** granting `SELECT` on a table is not enough on its own — the principal also
  needs `USE CATALOG` and `USE SCHEMA` on the containing securables.
- **Trap:** IAM roles are cloud-provider permissions on storage; they are not a Unity
  Catalog column-level control.
- **Trap:** converting a table type is not automatically reversible. If the scenario
  asks to "undo" a conversion, check what the current runtime actually supports before
  assuming an `ALTER TABLE` reverses it. Delta time travel restores *data versions*,
  not the managed/external designation.

## Verify before sealing

- [Unity Catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/)
- [Manage privileges](https://docs.databricks.com/aws/en/data-governance/unity-catalog/manage-privileges/)
- [Row filters and column masks](https://docs.databricks.com/aws/en/tables/row-and-column-filters)
- [ABAC in Unity Catalog](https://docs.databricks.com/aws/en/data-governance/unity-catalog/abac/)
- [Managed tables](https://docs.databricks.com/aws/en/tables/managed) · [External tables](https://docs.databricks.com/aws/en/tables/external)
