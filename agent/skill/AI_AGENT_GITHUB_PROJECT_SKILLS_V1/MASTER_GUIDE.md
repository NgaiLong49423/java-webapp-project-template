# Master Guide - AI Agent GitHub Project Workflow

## Recommended Use For Your Current Stage

Because you are new to Agent design, use this kit in two phases.

---

## Phase 1 - Project Management Agent

Goal:

```text
SRS → FR → Epic → User Story → Task → GitHub Issue
```

Use:

```text
00_AI_AGENT_ORCHESTRATOR.md
01_extract_requirements_from_srs.md
02_refine_functional_requirements.md
03_generate_epics_and_user_stories.md
04_decompose_tasks_by_layer.md
05_calculate_priority_and_story_points.md
09_generate_labels.md
10_generate_milestones.md
11_generate_github_project_fields.md
12_generate_github_issues.md
```

Result:

- Professional GitHub Issues.
- Labels.
- Milestones.
- Project fields.
- Clear task distribution.

---

## Phase 2 - Technical Specification Agent

Goal:

```text
FR → Database Spec → API Spec → Frontend Spec → Test Cases
```

Use:

```text
07_fr_to_technical_spec.md
08_generate_project_structure.md
14_generate_acceptance_criteria_and_test_cases.md
```

Result:

- Better task quality.
- Clear work for Backend and Frontend.
- Better acceptance criteria.

---

## Phase 3 - Code Generation Agent

Do not start this phase until Phase 1 and Phase 2 are stable.

Future skills may include:

```text
generate_database_script.md
generate_backend_servlet_code.md
generate_jsp_pages.md
generate_css_layout.md
generate_unit_tests.md
generate_pull_request.md
```

---

## Best Practice

Keep the old file as historical reference, but use this new structure for real Agent work.

Reason:

- Easier to maintain.
- Easier to improve.
- Easier to debug.
- Easier to reuse in future projects.
- Less chance that Agent mixes many tasks together.
