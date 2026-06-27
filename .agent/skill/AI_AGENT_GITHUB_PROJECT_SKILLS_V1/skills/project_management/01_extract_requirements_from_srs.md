# 01 - Extract Requirements From SRS

## Purpose

Extract Business Requirements, Functional Requirements, Non-Functional Requirements, roles, constraints, assumptions and major modules from project documents.

Business Requirement là mục tiêu nghiệp vụ lớn. Functional Requirement là chức năng hệ thống cần làm. Non-Functional Requirement là yêu cầu chất lượng như bảo mật, tốc độ, độ tin cậy.

---

## When To Use

Use this skill when the Agent receives:

- SRS document.
- Assignment description.
- Teacher requirements.
- Use case description.
- Project proposal.
- Mixed raw notes about a software project.

---

## Inputs

```yaml
project_name: string
source_documents:
  - document_name: string
    document_type: SRS | assignment | use_case | notes | other
    content: text
```

---

## System Prompt

You are a senior Business Analyst. Analyze the provided documents and extract a clean requirement inventory.

Your job is not to improve or invent the project. Your job is to identify what the source document actually requires.

Return requirements in structured Markdown and YAML-like blocks.

---

## Extraction Rules

1. Extract only requirements supported by the source.
2. If a requirement is implied but not explicit, mark it as `inferred`.
3. Separate Functional Requirements and Non-Functional Requirements.
4. Identify actors and user roles.
5. Identify business constraints and technical constraints.
6. Preserve traceability by noting the source section when possible.
7. Do not create GitHub Issues in this step.
8. Do not generate code in this step.

---

## Output Format

```markdown
# Requirement Inventory

## Project Overview
- Project Name:
- Domain:
- Main Goal:
- Source Documents:

## Actors / User Roles
| Role ID | Role Name | Description |
|---|---|---|

## Business Requirements
| BR ID | Requirement | Source | Confidence |
|---|---|---|---|

## Functional Requirements
| FR ID | Statement | Actor | Source | Status |
|---|---|---|---|---|

## Non-Functional Requirements
| NFR ID | Category | Requirement | Source |
|---|---|---|---|

## Constraints
| Constraint ID | Type | Description |
|---|---|---|

## Assumptions
| Assumption ID | Description | Reason |
|---|---|---|

## Open Questions
| Question ID | Question | Why It Matters |
|---|---|---|
```

---

## Example

```markdown
| FR-001 | The system shall allow customers to create a car wash booking. | Customer | SRS 3.2 | explicit |
| FR-002 | The system shall allow staff to update booking status. | Staff | SRS 3.3 | inferred |
```

---

## Quality Gate

Before returning the final output, verify:

- Every item has a stable ID.
- Output is traceable to source requirement.
- No vague wording remains.
- Assumptions are clearly marked.
- The output can be used by the next pipeline step.
