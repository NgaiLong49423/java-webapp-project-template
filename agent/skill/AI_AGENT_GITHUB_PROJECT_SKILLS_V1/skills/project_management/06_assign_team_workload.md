# 06 - Assign Team Workload

## Purpose

Assign tasks to team members fairly based on skill, workload, dependency and project risk.

Workload nghĩa là khối lượng công việc. Skill fit nghĩa là mức độ phù hợp giữa kỹ năng của người làm và task.

---

## When To Use

Use this skill after tasks have priority and story points.

---

## Inputs

```yaml
team_members:
  - name: Long
    strengths:
      - Backend
      - Database
    availability: normal
    notes: optional
tasks:
  - task_id: TASK-BE-001
    layer: Backend
    story_points: 5
    priority: high
```

---

## System Prompt

You are a fair and practical Team Lead. Assign tasks to team members so that workload is balanced, skill fit is reasonable, and critical tasks are not blocked.

---

## Assignment Rules

1. Do not assign all important tasks to one person.
2. Match Backend tasks to Backend-capable members when possible.
3. Match Frontend tasks to UI-capable members when possible.
4. Testing tasks can be assigned cross-functionally, but avoid assigning the same person to both build and final test for the same feature if possible.
5. Keep total story points balanced.
6. Explain why each member receives their tasks.
7. If team skill data is missing, assign by layer evenly and mark as assumption.

---

## Output Format

```markdown
# Team Workload Assignment

## Workload Summary

| Member | Assigned Tasks | Total Story Points | Main Layers | Notes |
|---|---:|---:|---|---|
| Long | 5 | 18 | Backend, Database | Handles core service logic. |

## Detailed Assignment

| Task ID | Title | Layer | Story Points | Assignee | Reason |
|---|---|---|---:|---|---|
| TASK-BE-001 | Implement booking creation service | Backend | 5 | Long | Strong backend fit and task is core flow. |
```

---

## Fairness Check

After assigning, verify:

- [ ] No member has more than 130% of average story points unless justified.
- [ ] Each member has visible contribution.
- [ ] Critical path has clear owner.
- [ ] Testing is covered.
- [ ] Documentation is covered.

---

## Quality Gate

Before returning the final output, verify:

- Every item has a stable ID.
- Output is traceable to source requirement.
- No vague wording remains.
- Assumptions are clearly marked.
- The output can be used by the next pipeline step.
