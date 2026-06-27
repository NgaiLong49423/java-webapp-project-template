# 09 - Generate GitHub Labels

## Purpose

Generate a professional GitHub label system for issues, tasks and project tracking.

Label là nhãn dùng để phân loại Issue trong GitHub.

---

## When To Use

Use this skill before generating GitHub Issues or when setting up a new repository.

---

## Inputs

```yaml
project_type: web application
tech_stack: optional
task_layers:
  - Backend
  - Frontend
  - Database
  - Testing
issue_types:
  - feature
  - bug
  - documentation
```

---

## System Prompt

You are a GitHub Project Manager. Create a clean and professional label taxonomy for this repository.

Group labels by category and provide name, color and description.

---

## Required Label Categories

### Type Labels

```text
feature
bug
enhancement
documentation
refactor
test
```

### Layer Labels

```text
frontend
backend
database
integration
testing
devops
documentation
```

### Priority Labels

```text
priority:high
priority:medium
priority:low
```

### Status Labels

```text
status:blocked
status:needs-review
status:ready
```

### Difficulty Labels

```text
difficulty:easy
difficulty:medium
difficulty:hard
```

### Domain Labels

Generate based on project modules, for example:

```text
domain:auth
domain:booking
domain:payment
domain:membership
domain:reporting
```

---

## Rules

1. Label names must be lowercase.
2. Use colon namespace for grouped labels.
3. Avoid duplicate meaning.
4. Keep descriptions short and useful.
5. Use consistent colors per category.
6. Do not create too many labels.

---

## Output Format

```markdown
# GitHub Labels

| Name | Color | Description | Category |
|---|---|---|---|
| backend | 5319E7 | Server-side logic, API, service, controller work. | layer |
```

---

## Recommended Base Labels

```yaml
- name: feature
  color: 0E8A16
  description: New user-facing or system functionality.

- name: bug
  color: D73A4A
  description: Something is not working as expected.

- name: backend
  color: 5319E7
  description: Server-side logic, API, service, controller work.

- name: frontend
  color: 1D76DB
  description: UI, page layout, client-side interaction work.

- name: database
  color: BFDADC
  description: Schema, SQL script, query, seed data or database design.

- name: priority:high
  color: B60205
  description: Must be completed early or blocks important project flow.
```

---

## Quality Gate

Before returning the final output, verify:

- Every item has a stable ID.
- Output is traceable to source requirement.
- No vague wording remains.
- Assumptions are clearly marked.
- The output can be used by the next pipeline step.
