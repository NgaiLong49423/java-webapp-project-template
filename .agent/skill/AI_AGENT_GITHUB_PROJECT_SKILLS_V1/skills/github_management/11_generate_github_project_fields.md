# 11 - Generate GitHub Project Fields

## Purpose

Define custom fields for GitHub Projects so the team can track work professionally.

Custom Field là trường tùy chỉnh trong GitHub Project, ví dụ Priority, Sprint, Layer, Story Point.

---

## When To Use

Use this skill when setting up GitHub Projects v2.

---

## Inputs

```yaml
project_name: string
workflow_statuses: optional
labels: list
milestones: list
team_members: optional
```

---

## System Prompt

You are a GitHub Projects Specialist. Design a practical set of custom fields for project tracking.

The field set must be useful for a small student software team and not too complex.

---

## Recommended Fields

```yaml
fields:
  - name: Status
    type: single_select
    options:
      - Backlog
      - Ready
      - In Progress
      - Code Review
      - Testing
      - Blocked
      - Done

  - name: Priority
    type: single_select
    options:
      - High
      - Medium
      - Low

  - name: Layer
    type: single_select
    options:
      - Database
      - Backend
      - Frontend
      - Integration
      - Testing
      - Documentation
      - DevOps

  - name: Story Point
    type: number

  - name: Sprint
    type: single_select
    options:
      - Sprint 1
      - Sprint 2
      - Sprint 3
      - Sprint 4
      - Sprint 5

  - name: Module
    type: single_select
    options:
      - Authentication
      - Booking
      - Service
      - Membership
      - Payment
      - Reporting
```

---

## Rules

1. Do not create too many fields.
2. Prefer single-select fields for consistent filtering.
3. Avoid overlapping fields with identical meaning.
4. Keep names short and easy to understand.
5. Use Story Point as number field.
6. Use Milestone for delivery phase; use Sprint field only if the team uses sprints.

---

## Output Format

```markdown
# GitHub Project Fields

| Field Name | Type | Options | Purpose |
|---|---|---|---|
| Layer | Single Select | Database, Backend, Frontend, Testing | Shows technical layer of the issue. |
```

---

## Recommended Views

Create these project views:

```text
Board by Status
Table by Sprint
Table by Layer
Table by Assignee
Roadmap by Milestone
```

View nghĩa là cách nhìn dữ liệu trong Project Board.

---

## Quality Gate

Before returning the final output, verify:

- Every item has a stable ID.
- Output is traceable to source requirement.
- No vague wording remains.
- Assumptions are clearly marked.
- The output can be used by the next pipeline step.
