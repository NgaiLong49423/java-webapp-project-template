# 12 - Generate GitHub Issues

## Purpose

Generate professional GitHub Issue bodies from tasks, stories, technical specs, labels, milestones and assignment data.

Issue Body là phần nội dung mô tả bên trong GitHub Issue.

---

## When To Use

Use this skill after tasks, labels, milestones, priority and story points are ready.

---

## Inputs

```yaml
tasks:
  - task_id: TASK-BE-001
    title: string
    layer: Backend
    parent_story: US-001
    related_fr: FR-001
    priority: high
    story_points: 5
    assignee: optional
    milestone: Sprint 1
    dependencies: list
    acceptance_criteria: list
```

---

## System Prompt

You are a professional GitHub Issue Writer. Create clear, actionable and well-structured GitHub Issues.

Each issue must be easy for a team member to understand and execute.

---

## Issue Title Convention

Use:

```text
[LAYER][MODULE] Action-oriented title
```

Examples:

```text
[BE][Booking] Implement booking creation API
[FE][Booking] Build booking form UI
[DB][Booking] Create booking table and relationships
[QA][Booking] Test booking creation scenarios
```

---

## Issue Body Template

```markdown
## Context
Explain why this issue exists and which FR/User Story it supports.

## Objective
State the clear goal of this issue.

## Scope
- [ ] Work item 1
- [ ] Work item 2

## Out of Scope
- Item not included in this issue.

## Technical Notes
Add relevant database/API/UI notes.

## Acceptance Criteria
- [ ] Given ..., When ..., Then ...

## Dependencies
- TASK-DB-001

## Definition of Done
- [ ] Implementation completed.
- [ ] Basic validation handled.
- [ ] Error cases handled.
- [ ] Tested manually or with test case.
- [ ] No unrelated changes included.
```

---

## Rules

1. One Issue equals one clear task.
2. Do not mix unrelated layers in one issue.
3. Include traceability: FR, Epic, User Story.
4. Include Definition of Done.
5. Include dependencies.
6. Use checklists for scope and acceptance criteria.
7. Keep title action-oriented.
8. Avoid vague phrases.

---

## Output Format

```markdown
# Generated GitHub Issues

## Issue 1

**Title:** [BE][Booking] Implement booking creation API

**Labels:** backend, feature, priority:high, domain:booking

**Milestone:** Sprint 2 - Booking & Service Management

**Assignee:** Long

**Story Points:** 5

**Body:**
...
```

---

## Quality Gate

Before returning the final output, verify:

- Every item has a stable ID.
- Output is traceable to source requirement.
- No vague wording remains.
- Assumptions are clearly marked.
- The output can be used by the next pipeline step.
