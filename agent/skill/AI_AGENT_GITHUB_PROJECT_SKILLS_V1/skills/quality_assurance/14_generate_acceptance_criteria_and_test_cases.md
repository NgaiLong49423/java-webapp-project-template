# 14 - Generate Acceptance Criteria And Test Cases

## Purpose

Generate Acceptance Criteria and Test Cases for each User Story or Functional Requirement.

Acceptance Criteria là tiêu chí nghiệm thu. Test Case là kịch bản kiểm thử cụ thể.

---

## When To Use

Use this skill after User Stories or Technical Specifications are available.

---

## Inputs

```yaml
fr_id: FR-001
user_story: string
business_rules: list
technical_notes: optional
```

---

## System Prompt

You are a QA Analyst. Generate clear Acceptance Criteria using Given-When-Then and practical Test Cases that cover happy paths, validation errors and edge cases.

---

## Rules

1. Use Given-When-Then for Acceptance Criteria.
2. Include at least 2 happy paths.
3. Include at least 2 edge/error cases.
4. Test permissions if the feature has roles.
5. Test invalid input.
6. Test empty state if relevant.
7. Do not test implementation details that users cannot observe unless it is an API/database task.

---

## Acceptance Criteria Format

```gherkin
AC-001
Given the customer is logged in
When the customer submits a valid booking form
Then the system shall create a new booking and display a success message
```

---

## Test Case Format

```markdown
| Test Case ID | Scenario | Precondition | Steps | Expected Result | Type |
|---|---|---|---|---|---|
| TC-001 | Create valid booking | Customer logged in | Select service, date, slot, submit | Booking is created | Happy Path |
```

---

## Output Format

```markdown
# Acceptance Criteria and Test Cases for FR-001

## Acceptance Criteria

## Test Cases

## Edge Cases

## Permission Tests

## Notes
```

---

## Quality Gate

Before returning the final output, verify:

- Every item has a stable ID.
- Output is traceable to source requirement.
- No vague wording remains.
- Assumptions are clearly marked.
- The output can be used by the next pipeline step.
