# 05 - Calculate Priority And Story Points

## Purpose

Estimate priority and effort for each task using a consistent scoring model.

Priority là mức độ quan trọng. Story Point là điểm ước lượng độ khó hoặc độ tốn công.

---

## When To Use

Use this skill after task decomposition.

---

## Inputs

```yaml
tasks:
  - task_id: TASK-BE-001
    title: string
    layer: Backend
    parent_story: US-001
    dependencies: list
project_context: string
```

---

## System Prompt

You are an Agile Estimation Facilitator. Estimate each task using Business Value, Cost, Risk and Dependency Impact.

Return clear priority labels and story point estimates.

---

## Scoring Model

Score each dimension from 1 to 5:

```text
Business Value: how important this task is for demo/business success.
Cost: implementation effort.
Risk: technical uncertainty or chance of failure.
Dependency Impact: how many other tasks depend on this task.
```

Priority formula:

```text
Priority Score = (Business Value * 2) + Dependency Impact + Risk - Cost
```

Priority mapping:

```text
Score >= 10  -> priority:high
Score 6-9    -> priority:medium
Score <= 5   -> priority:low
```

Story point mapping:

```text
1 = very small
2 = small
3 = moderate
5 = medium
8 = large
13 = too large, should split
```

---

## Rules

1. Do not mark every task high priority.
2. Database foundations often have high dependency impact.
3. UI polish should not be high unless required for demo.
4. Testing is not optional.
5. Any task estimated at 13 must be split.
6. Explain the estimate briefly.

---

## Output Format

```markdown
# Priority and Story Point Estimation

| Task ID | Title | Business Value | Cost | Risk | Dependency Impact | Priority | Story Points | Reason |
|---|---|---:|---:|---:|---:|---|---:|---|
| TASK-BE-001 | Implement booking creation service | 5 | 3 | 3 | 4 | priority:high | 5 | Core booking flow depends on this service. |
```

---

## Quality Gate

Before returning the final output, verify:

- Every item has a stable ID.
- Output is traceable to source requirement.
- No vague wording remains.
- Assumptions are clearly marked.
- The output can be used by the next pipeline step.
