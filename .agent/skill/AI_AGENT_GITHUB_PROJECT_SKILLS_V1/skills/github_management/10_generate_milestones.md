# 10 - Generate GitHub Milestones

## Purpose

Generate practical GitHub Milestones based on project scope, demo needs, task dependencies and sprint planning.

Milestone là mốc hoàn thành lớn, ví dụ Sprint 1 hoặc Demo Phase 1.

---

## When To Use

Use this skill after Epics and Tasks are available.

---

## Inputs

```yaml
project_name: string
epics: list
tasks: list
available_weeks: optional
teacher_deadlines: optional
```

---

## System Prompt

You are a Delivery Manager. Create realistic project milestones that help the team deliver the project in stages.

Milestones must reflect dependencies and demo priorities.

---

## Recommended Milestone Strategy For Student Projects

Use 4 to 5 milestones:

```text
Milestone 1 - Project Foundation
Milestone 2 - Core Business Flow
Milestone 3 - Advanced Features
Milestone 4 - Integration & Testing
Milestone 5 - Final Documentation & Demo
```

For Car Wash:

```text
Sprint 1 - Foundation & Authentication
Sprint 2 - Booking & Service Management
Sprint 3 - Membership, Loyalty & Payment
Sprint 4 - Staff Operation & Reporting
Sprint 5 - Testing, Polish & Final Demo
```

---

## Rules

1. Do not create a milestone for every tiny feature.
2. Each milestone must have a clear goal.
3. Earlier milestones should unblock later work.
4. Testing and documentation must appear before final milestone ends.
5. If dates are unknown, omit due dates or mark as TBD.

---

## Output Format

```markdown
# GitHub Milestones

## Sprint 1 - Foundation & Authentication

**Goal:** Build base project structure, database foundation and login flow.

**Included Epics:**
- EPIC-001 Authentication & Authorization
- EPIC-002 Core Database Setup

**Success Criteria:**
- Users can log in by role.
- Core database tables exist.
- Base layout works.

**Suggested Due Date:** TBD
```

---

## Milestone Assignment Table

```markdown
| Milestone | Epic | Task IDs | Reason |
|---|---|---|---|
```

---

## Quality Gate

Before returning the final output, verify:

- Every item has a stable ID.
- Output is traceable to source requirement.
- No vague wording remains.
- Assumptions are clearly marked.
- The output can be used by the next pipeline step.
