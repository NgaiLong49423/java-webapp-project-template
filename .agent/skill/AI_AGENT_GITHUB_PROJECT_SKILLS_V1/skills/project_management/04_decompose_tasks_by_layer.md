# 04 - Decompose Tasks By Layer

## Purpose

Break each User Story into assignable technical tasks by layer: Database, Backend, Frontend, Integration, Testing and Documentation.

Layer nghĩa là lớp công việc kỹ thuật. Tách layer giúp chia việc rõ và tránh một Issue ôm quá nhiều thứ.

---

## When To Use

Use this skill after Epics and User Stories are generated.

---

## Inputs

```yaml
user_stories:
  - story_id: US-001
    epic_id: EPIC-001
    story: string
    related_frs: list
technical_spec: optional
tech_stack: optional
```

---

## System Prompt

You are a Technical Lead. Decompose each User Story into small, independent and assignable tasks grouped by technical layer.

Each task must be clear enough for a student developer to implement without guessing the main objective.

---

## Layer Types

Use these standard layers:

```text
Database
Backend
Frontend
Integration
Testing
Documentation
DevOps
```

---

## Task Splitting Rules

1. A task should belong to one primary layer.
2. A task should have one main objective.
3. Avoid tasks larger than 8 story points.
4. If a task is too large, split it.
5. Every task must reference its parent User Story.
6. Every task must include dependencies if any.
7. Do not assign people in this step unless explicitly requested.

---

## Output Format

```markdown
# Layer-Based Task Breakdown

## US-001 - Create Car Wash Booking

### Database Tasks
- TASK-DB-001: Design Booking table and relationships
  - Depends on: None
  - Output: SQL table design

### Backend Tasks
- TASK-BE-001: Implement booking creation service
  - Depends on: TASK-DB-001
  - Output: Booking service method and validation logic

### Frontend Tasks
- TASK-FE-001: Build booking creation form
  - Depends on: TASK-BE-001 API contract
  - Output: Booking form UI

### Testing Tasks
- TASK-QA-001: Test booking creation happy path and invalid slot cases
  - Depends on: TASK-BE-001, TASK-FE-001
  - Output: Test report
```

---

## Task Body Requirements

Each task should include:

```yaml
task_id: TASK-BE-001
title: Implement booking creation service
layer: Backend
parent_story: US-001
objective: string
scope:
  - item 1
  - item 2
out_of_scope:
  - item 1
dependencies:
  - TASK-DB-001
expected_output: string
```

---

## Quality Gate

Before returning the final output, verify:

- Every item has a stable ID.
- Output is traceable to source requirement.
- No vague wording remains.
- Assumptions are clearly marked.
- The output can be used by the next pipeline step.
