---
name: srs-to-github-issues
description: Convert PRD, SRS, product specs, requirement documents, or planning documents into professional GitHub Issue drafts, optionally create real GitHub Issues, and optionally sync GitHub Project metadata. Use this when the user asks to break down requirements into issues, create GitHub issue drafts, estimate size/story points, assign labels, or prepare project-ready work items.
risk: critical
source: self
source_type: custom
version: v1.1.0
created_date: 2026-06-27
last_updated_date: 2026-06-29
---

# SRS to GitHub Issues

Converts requirement documents into professional GitHub Issue drafts.

Default behavior is safe: create draft files only. Do not create real GitHub Issues, update GitHub Projects, create branches, close issues, or modify source code unless the user explicitly asks.

## When to Use

Use this skill when the user asks to:

- Convert SRS, PRD, specs, requirements, user stories, or planning docs into GitHub Issues.
- Split requirements into implementation-ready work items.
- Create issue drafts with traceability, acceptance criteria, labels, priority, size, story points, and relationships.
- Create real GitHub Issues from approved drafts.
- Sync issue metadata into a GitHub Project.
- Estimate issue size/story points or generate an issue index.

Do not use for ordinary coding, bug fixing, PR review, or CI debugging unless the user specifically asks to create/manage GitHub Issues from requirements.

## Source Truth Rules

Before drafting:

1. Read available source documents.
2. Prefer detailed requirement documents over summaries when documents conflict.
3. If both PRD and SRS exist, use PRD for product overview and SRS for detailed behavior.
4. If PRD and SRS conflict, prefer SRS unless the user says otherwise.
5. If a source document version starts with `v0.`, treat it as draft/under review.
6. Do not treat `v0.x.x` requirement docs as final unless the user confirms.

If source hierarchy is unclear, summarize available docs and ask which are authoritative.

## No Invention Rule

Do not invent product behavior, technical choices, workflows, actors, labels, Project fields, dates, dependencies, or relationships.

If information is missing, mark it as `TBD`, `Unknown`, or ask the user.

## Traceability Rule

Every issue must trace back to at least one source reference: FR, NFR, UC, business rule, product goal, requirement section, or spec heading.

If an issue cannot be traced to a source document, do not create it as a requirement issue.

## Repository Inspection

Before drafting, inspect relevant files:

- `AGENTS.md`
- `.agent/repo-contract.yml`
- `README.md`
- `PRD.md`
- `SRS.md`
- `requirements.md`
- `SPEC.md`
- `docs/`
- `.github/ISSUE_TEMPLATE/*.yml`
- `.github/labels.yml`

If the repo uses the standard template, prefer:

- `docs/requirements/SRS.md`
- `docs/requirements/PRD.md`
- `.agent/outputs/drafts/github-issues/`
- `.agent/outputs/reports/`

If the repo contract defines different paths, follow the repo contract.

## Operating Modes

### Draft Mode

Default mode. Create Markdown issue drafts only.

Default output:

- `.agent/outputs/drafts/github-issues/ISSUE_INDEX.md`
- numbered issue draft files such as `001-module-short-title.md`

Draft mode must not create real issues, update Projects, create labels, create branches, commit changes, or modify code unless explicitly asked.

When regenerating drafts:

- Clean or archive stale draft files first.
- Ensure every draft file listed in `ISSUE_INDEX.md` exists.
- Ensure every `.md` draft file in the final draft directory is referenced by `ISSUE_INDEX.md`.
- Do not leave stale, duplicate, or unreferenced drafts.

### GitHub Creation Mode

Explicit approval required.

Rules:

- Create issues only from drafts listed in `ISSUE_INDEX.md`.
- Do not scan every `.md` file in the draft directory.
- Default: create only items with `Status = Approved`.
- If the user specifies IDs/ranges, create only those drafts.
- If the user says create all drafts, create all listed drafts.
- After creation, update `ISSUE_INDEX.md` with issue number, URL, status `Created`, and date if available.

Run `references/github-creation-preflight.md` before creating.

If a preflight check fails, stop and report it. Do not create partial issues unless the user explicitly approves continuing.

### GitHub Project Sync Mode

Explicit approval required.

Before syncing, verify repository owner/name, Project owner/number/ID, field IDs, option IDs, and issue item IDs.

Do not sync if required IDs cannot be determined confidently.

Normal fields to sync when available:

- Type
- Size
- Story Points
- Priority
- Start date
- Target date

Relationship sync is optional and best-effort only. Do not treat relationship sync failure as full workflow failure.

## Decomposition Strategy

Prefer FR-level traceability.

Default rule:

- Prefer one GitHub Issue per Functional Requirement.

Allowed exceptions:

- Split one FR if it is too large, risky, or unclear.
- Group multiple FRs only when they are small, strongly coupled, and implemented in the same workflow.
- Do not group many FRs into one issue only for convenience.
- Justify grouping/splitting decisions in `ISSUE_INDEX.md`.

Prefer vertical slices: each issue should represent meaningful, testable behavior.

Detailed guidance: `references/decomposition-rules.md`.

## Epic and Relationship Rules

Use parent/epic issues only when useful.

Create or propose an Epic when a module has 3+ child issues, a requirement is `XL`, Story Points are `13+`, or work is too broad for direct implementation.

Every draft issue must include relationship fields:

- Parent
- Blocked by
- Blocking
- Security alert

Relationship sync to GitHub Project is optional and best-effort only.

Never guess relationship field IDs or target issue IDs.

## Size, Priority, Dates

Estimate `Size` and `Story Points` independently.

Use rules from:

- `references/sizing-priority-rules.md`

Dates default to `TBD`. Do not invent dates. Fill dates only when the user provides a schedule.

## Labels and Templates

Before assigning labels:

1. Read `.github/labels.yml` if present.
2. Use only labels defined there unless the user explicitly allows new labels.
3. Each issue should include at least one primary type/work-item label.
4. If creating real issues and a needed label is missing on GitHub but exists in `.github/labels.yml`, create it from `labels.yml`.

Before drafting, inspect `.github/ISSUE_TEMPLATE/*.yml` when present.

Required issue body sections are defined in:

- `references/issue-body-template.md`

## Title and Branch Rules

Issue titles must be professional English.

Recommended title format:

- `[Module][Source Trace] Verb-Based Professional Title`

Use clear verbs such as Implement, Add, Support, Validate, Prevent, Recalculate, Restore, Sync, Generate, Refactor, or Fix.

Issue bodies should be Vietnamese by default unless the user requests another language.

Do not create branches. Only suggest branch names.

Branch format:

- `<prefix>/<short-kebab-case-title>`

Common prefixes: `feature/`, `fix/`, `refactor/`, `docs/`, `test/`, `data/`, `backend/`, `chore/`.

## Implementation Notes Rule

Implementation Notes are allowed only when source documents explicitly mention implementation constraints, technical choices, algorithms, storage mechanisms, architecture decisions, APIs, or data structures.

Do not add new technical solutions as facts.

If a useful technical suggestion is not in the source docs, place it under `Suggestion` and ask the user before finalizing.

## Token-Saving Workflow

For large documents, do not perform planning, draft generation, real issue creation, and Project sync in one pass unless explicitly asked.

Use phases:

1. Planning: create `ISSUE_INDEX.md`, traceability table, proposed issue list, estimates, and dependencies.
2. Draft Generation: create selected full issue draft files after approval.
3. GitHub Creation: create real issues only from drafts listed in `ISSUE_INDEX.md`.
4. Project Sync: sync normal Project fields after issues exist.
5. Final Report: concise result table only.

Do not print full issue bodies in chat unless the user asks.

## Required Outputs

Draft mode:

- `.agent/outputs/drafts/github-issues/ISSUE_INDEX.md`
- numbered draft files

Reference templates:

- `references/issue-index-template.md`
- `references/issue-body-template.md`

## Safety Boundaries

Do not create real issues, sync Project fields, create branches, commit changes, modify source code, close/delete issues, delete labels, delete branches, force-push, guess Project IDs, or treat `v0.x.x` docs as final without explicit permission.

## Completion Criteria

Draft mode is complete when source docs were inspected, issues trace to source references, the index exists, listed drafts exist, no stale/unreferenced draft files remain, and metadata fields are present or marked `TBD`.

GitHub creation is complete when approval was explicit, preflight passed, issues were created from indexed drafts, and issue numbers/URLs were recorded.

Project sync is complete when approval was explicit, IDs were verified, and sync results/failures were recorded.

## Final Response Format

Keep final responses concise.

After draft generation, report output directory, draft count, proposed Epic count, items needing review, path to `ISSUE_INDEX.md`, and whether real issues were created.

After real issue creation, report created issue count, issue numbers/URLs, labels applied, index update status, Project sync status, and skipped drafts.

After Project sync, report Project name/number, synced issues, updated fields, failures, and whether `ISSUE_INDEX.md` was updated to `Synced`.
