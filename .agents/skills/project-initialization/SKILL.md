---
name: project-initialization
description: Prepare a repository created from this GitHub template for an independent project. Use KEEP / INITIALIZE / CLEAN classification, preserve useful content, and avoid imposing a framework, database, architecture, or project-specific technology.
risk: medium
source: created
version: v1.0.0
created_date: 2026-10-09
last_updated_date: 2026-10-09
---

# Project Initialization

## Safety

- Confirm the target repository and inspect its Git state before proposing or applying changes.
- Do not overwrite or delete user content without explicit authorization. Compare colliding files and merge useful material deliberately.
- Never inspect or alter local `.agents/outputs/`.
- Never access, enumerate, search, parse, validate, create, edit, move, or delete anything under `docs/diagrams/`. Exclude it before input selection or traversal and never inspect a link target into it.
- Do not choose a framework, DBMS, architecture, or application layout for the project.

## Classification

- **KEEP:** reusable Agent policy, skills, workflows, scripts, contribution guidance, GitHub templates, labels, license, and the `app/`, `database/`, and `docs/` starter structure.
- **INITIALIZE:** project `README.md`, PRD/SRS, repository metadata in `.agents/repo-contract.yml`, setup instructions, and database examples. Confirm technology choices with project sources; do not convert placeholders into defaults.
- **CLEAN:** `docs/template-maintenance.md` and other material that exists only to maintain the source template. Remove the README link to the maintenance guide when cleaning it. Review each candidate, preserve unique useful content, and do not remove local outputs.

## Workflow

1. Build a scoped inventory from explicitly selected roots; prune protected paths before recursion.
2. Compare duplicate or case-colliding paths before any move. Preserve all unique content and verify the result.
3. Apply the classification and update relative links and artifact-appropriate metadata.
4. Verify skills' directory names match their frontmatter `name`; validate project docs without resolving protected link targets.
5. Confirm the new repository is independent. Do not create an automatic sync-back mechanism to the source template.
6. Review Git status and diff; report retained, initialized, cleaned, and unresolved items.
