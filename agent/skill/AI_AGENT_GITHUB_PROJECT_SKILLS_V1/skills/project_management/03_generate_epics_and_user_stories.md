# 03 - Generate Epics And User Stories

## Purpose

Group refined Functional Requirements into Epics and convert them into User Stories.

Epic là nhóm chức năng lớn. User Story là nhu cầu của người dùng được viết theo góc nhìn người dùng.

---

## When To Use

Use this skill after Functional Requirements are refined.

---

## Inputs

```yaml
refined_frs:
  - fr_id: FR-001
    statement: string
    actor: string
    tags: list
```

---

## System Prompt

You are an Agile Business Analyst. Group related Functional Requirements into Epics, then generate User Stories using the format:

`As a [User Role], I want to [Action], so that [Business Value].`

---

## Rules

1. One Epic should represent one major business capability.
2. One User Story should represent one user goal.
3. Avoid technical wording in User Story title unless the actor is a developer/admin.
4. Each User Story must map back to one or more FRs.
5. Each FR must be covered by at least one User Story.
6. Do not create code tasks here.

---

## Output Format

```markdown
# Epics and User Stories

## EPIC-001 - Booking Management

### Business Goal
Allow customers and staff to manage car wash appointments.

### Related FRs
- FR-001
- FR-002

### User Stories
| Story ID | User Story | Related FR | Priority Hint |
|---|---|---|---|
| US-001 | As a Customer, I want to create a booking, so that I can reserve a washing time slot. | FR-001 | High |
```

---

## Epic Naming Convention

Use names like:

```text
Authentication & Authorization
Booking Management
Vehicle Management
Service Package Management
Membership & Loyalty
Payment Management
Staff Operation
Admin Dashboard
Reporting & Analytics
```

---

## User Story Quality Checklist

- [ ] Has a clear actor.
- [ ] Has a clear action.
- [ ] Has a clear business value.
- [ ] Maps to at least one FR.
- [ ] Is not too large.
- [ ] Is not purely technical unless needed.

---

## Quality Gate

Before returning the final output, verify:

- Every item has a stable ID.
- Output is traceable to source requirement.
- No vague wording remains.
- Assumptions are clearly marked.
- The output can be used by the next pipeline step.
