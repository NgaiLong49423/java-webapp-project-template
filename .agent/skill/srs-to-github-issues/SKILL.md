---
name: srs-to-github-issues
description: Convert PRD, SRS, product specs, requirement documents, or planning documents into professional GitHub Issue drafts, optionally create real GitHub Issues, and optionally sync GitHub Project metadata. Use this when the user asks to break down requirements into issues, create GitHub issue drafts, estimate issue size/story points, assign labels, or prepare project-ready work items.
risk: critical
source: self
source_type: custom
---

# SRS to GitHub Issues

## Overview

This skill converts requirement documents into professional GitHub Issues. It is reusable across projects and must adapt to the current repository's documents, issue templates, labels, and GitHub Project configuration.

Primary outputs:

- GitHub Issue draft files.
- A module-based issue index.
- Optional real GitHub Issues when explicitly requested.
- Optional GitHub Project field sync when explicitly requested.

Default behavior is safe: create draft files only. Do not create real GitHub Issues, update GitHub Projects, create branches, close issues, or modify source code unless the user explicitly asks for that action.

## When to Use

Use this skill when the user asks to:

- Convert SRS, PRD, spec, requirements, user stories, or planning documents into GitHub Issues.
- Split a large requirement into smaller implementation-ready issues.
- Create professional issue drafts with traceability, acceptance criteria, labels, priority, size, story points, and relationships.
- Create GitHub Issues from approved drafts.
- Sync issue metadata into a GitHub Project.
- Estimate issue size or story points from requirement scope.
- Generate an issue index for project planning.

Do not use this skill for ordinary code implementation, bug fixing, or pull request work unless the user specifically asks to create or manage GitHub Issues from requirements.

## Core Principles

1. Source truth first.
   - Read the available source documents before drafting issues.
   - Prefer detailed requirement documents over summaries when documents conflict.
   - If both PRD and SRS exist, use PRD for product overview and SRS for detailed behavior.
   - If PRD and SRS conflict, prefer SRS unless the user says otherwise.

2. No invention.
   - Do not add product behavior, technical choices, workflows, actors, labels, fields, or dates that are not grounded in the source documents or repository configuration.
   - If information is missing, mark it as `TBD`, `Unknown`, or ask the user.

3. Traceability is mandatory.
   - Every issue must trace back to at least one source reference such as FR, NFR, UC, business rule, product goal, requirement section, or spec heading.
   - If an issue cannot be traced to a source document, do not create it as a requirement issue.

4. Draft first.
   - Default mode is draft-only.
   - Real GitHub issue creation requires explicit user approval.
   - GitHub Project sync requires explicit user approval.
   - For large documents, use a phased workflow instead of doing planning, draft generation, GitHub creation, and Project sync in one pass.

5. Index-driven creation.
   - `ISSUE_INDEX.md` is the single source of truth for which draft files may become real GitHub Issues.
   - In GitHub Creation Mode, never create issues by scanning every `.md` file in the draft directory.
   - Create real GitHub Issues only from draft files explicitly listed in `ISSUE_INDEX.md`.

6. Respect the current repository.
   - Read `.github/ISSUE_TEMPLATE/*.yml` before drafting issues when present.
   - Read `.github/labels.yml` before assigning labels when present.
   - Do not invent labels outside `.github/labels.yml` unless the user explicitly allows it.
   - Use the current repository's conventions for templates, labels, and Project fields.

7. Professional titles, localized bodies.
   - Issue titles must be professional English.
   - Issue bodies should be Vietnamese by default unless the user requests another language.
   - Suggested branch names must be English kebab-case.

## Operating Modes

### 1. Draft Mode — Default

Create Markdown issue drafts only.

Default output directory:

```text
.agent/report/github-issue-drafts/
```

Required output files:

```text
.agent/report/github-issue-drafts/ISSUE_INDEX.md
.agent/report/github-issue-drafts/001-module-short-title.md
.agent/report/github-issue-drafts/002-module-short-title.md
...
```

Draft mode must not:

- Create real GitHub Issues.
- Update GitHub Project fields.
- Create labels on GitHub.
- Create branches.
- Commit changes unless the user explicitly asks.

When regenerating drafts, clean stale drafts first:

- Delete or archive old issue draft files in `.agent/report/github-issue-drafts/`.
- Regenerate only the final intended draft set.
- Ensure every draft file listed in `ISSUE_INDEX.md` exists.
- Ensure every `.md` draft file in the draft directory is referenced by `ISSUE_INDEX.md`.
- Do not leave stale, duplicate, or unreferenced draft files in the final draft directory.

### 2. GitHub Creation Mode — Explicit Approval Required

Only enter this mode if the user explicitly says something like:

- "create GitHub issues"
- "tạo issue thật"
- "create the approved issues"
- "create issues 001 to 005"
- "tạo toàn bộ draft"

Default behavior in this mode:

- Create only issues with `Status = Approved` in `ISSUE_INDEX.md`.
- If the user specifies a range or exact IDs, create only those drafts.
- If the user explicitly says "create all drafts", create all draft issues.
- Create real GitHub Issues only from draft files explicitly listed in `ISSUE_INDEX.md`.
- Do not create issues by scanning every `.md` file in the draft directory.
- After creation, update `ISSUE_INDEX.md` with issue number, issue URL, status `Created`, and created date if available.

Before creating real issues, run the preflight checks:

- `ISSUE_INDEX.md` exists.
- All selected draft files listed in `ISSUE_INDEX.md` exist.
- No unreferenced issue draft files remain in the final draft directory.
- No local `file:///` paths exist in drafts or in `ISSUE_INDEX.md`.
- The issue title and body are derived from the selected draft.
- Labels exist on GitHub.
- If labels are missing but exist in `.github/labels.yml`, create those missing labels from `labels.yml`.
- Do not create labels that are not listed in `.github/labels.yml` unless the user explicitly approves.
- Project field names and option IDs have been inspected if Project sync will run in the same request.

If any preflight check fails, stop and report the failure. Do not create partial issues unless the user explicitly approves continuing.

### 3. GitHub Project Sync Mode — Explicit Approval Required

Only enter this mode if the user explicitly says something like:

- "sync project metadata"
- "cập nhật vào GitHub Project"
- "set project fields"
- "sync project fields"

When requested, sync directly without creating a separate plan, but only after inspecting the Project configuration.

Before syncing, inspect and verify:

- Repository owner.
- Repository name.
- GitHub Project owner.
- Project number or Project ID.
- Field names.
- Field IDs.
- Option IDs for single-select fields.
- Current issue item IDs in the Project.

Do not sync if any required field ID, option ID, project number, or issue item ID cannot be determined confidently. Stop and ask the user.

Normal fields to sync when available:

- Type
- Size
- Story Points
- Priority
- Start date
- Target date

Relationship sync is optional and best-effort only. Do not treat relationship sync failure as a full workflow failure.

After syncing, update `ISSUE_INDEX.md` with status `Synced` for successfully synced normal Project fields and record any failed fields with reasons.

## Required Repository Inspection

Before drafting issues, inspect the repository for:

```text
PRD.md
SRS.md
requirements.md
SPEC.md
spec.md
docs/
.github/ISSUE_TEMPLATE/*.yml
.github/labels.yml
README.md
```

If multiple source documents exist, identify the source hierarchy. A recommended hierarchy is:

1. SRS or detailed requirement specification.
2. PRD or product requirement document.
3. Use case documents.
4. Architecture/design notes.
5. README or high-level docs.

If the hierarchy is unclear, summarize the available documents and ask the user which documents are authoritative.

## Issue Decomposition Strategy

Use a hybrid decomposition strategy, but prefer FR-level traceability.

Default rule:

- Prefer one GitHub Issue per Functional Requirement (FR).

Allowed exceptions:

- Split one FR into multiple implementation issues if it is too large, risky, or unclear.
- Group multiple FRs only when they are small, strongly coupled, and implemented in the same workflow.
- Do not group many FRs into one issue only for convenience.
- Every grouping or splitting decision must be justified in `ISSUE_INDEX.md`.

General rules:

- Group issues by module, domain, feature area, or workflow only when that grouping improves implementation clarity.
- Preserve traceability to FR, NFR, UC, business rules, or source sections.
- Split large requirements into implementation-ready issues.
- Do not split by code layer alone unless the source document or project workflow requires it.
- Prefer vertical slices when possible: each issue should represent a meaningful, testable piece of behavior.

## Epic and Relationship Rules

Use parent/epic issues only when useful.

Issue relationships must always be written in the issue body. GitHub Project relationship synchronization is optional and best-effort.

Required relationship fields in every draft issue:

- Parent
- Blocked by
- Blocking
- Security alert

Project relationship fields may be synced only when:

- The GitHub Project explicitly supports the relationship field.
- The exact target issue number or issue ID can be resolved.
- The required GitHub CLI or GraphQL operation is known and safe.
- The operation can be performed without guessing.

If relationship sync fails or is not safely supported:

- Do not fail the whole workflow.
- Keep the relationship information in the issue body.
- Report the relationship sync failure in the final report.
- Continue syncing normal Project fields such as Type, Priority, Story Points, Start date, and Target date.

Never guess relationship field IDs or relationship target IDs.

Create or propose an Epic when:

- A module has 3 or more child issues.
- A requirement is estimated as `XL`.
- Story Points are `13` or higher.
- The work is too broad for a direct implementation issue.

Rules:

- If `Size = XL` or `Story Points >= 13`, keep it only as an Epic or split it into smaller implementation issues.
- Do not create real parent/epic issues unless the user approves.
- In draft mode, record relationships in the issue body and index.

Supported relationship types:

- Parent
- Blocked by
- Blocking
- Security alert

Use `Security alert` only for real security or vulnerability-related issues.

## Size and Story Point Estimation

Estimate `Size` and `Story Points` independently.

### Size

Use size to estimate scope.

```text
XS = very small change, narrow scope, minimal rules
S  = small feature or task, few edge cases
M  = medium feature, validation, persistence, or several business rules
L  = large feature, multiple flows, multiple modules, important dependencies
XL = too large for direct implementation; should usually become an Epic or be split
```

### Story Points

Use story points to estimate implementation effort, uncertainty, and risk. Story points are not hours.

```text
1  = very easy
2  = easy
3  = medium
5  = hard
8  = very hard
13 = too large or high risk; split or turn into Epic unless explicitly approved
```

Each issue must include a short estimation reason.

Example:

```text
Size: M
Story Points: 5
Estimation Reason: Medium scope, but higher effort because it affects validation, persistence, and business rule consistency.
```

## Priority Rules

The agent may propose priority, but must explain why.

Allowed priority values should come from the repository's GitHub Project configuration or labels. If `.github/labels.yml` exists, map priority to labels from that file.

Common mapping example:

```text
Critical -> Critical or priority-critical label if defined
High     -> priority-high label if defined
Medium   -> priority-medium label if defined
Low      -> priority-low label if defined
```

Do not invent priority labels outside `.github/labels.yml`.

Priority must consider:

- Dependency order.
- Core user workflow importance.
- Risk if delayed.
- Whether other issues are blocked by it.
- Whether it is required before testing or integration.

## Date Rules

Default dates:

```text
Start Date: TBD
Target Date: TBD
```

Do not invent dates.

Only fill dates when the user provides a schedule, such as:

- "start from 2026-06-27"
- "split this into 7 days"
- "foundation issues on day 1"
- "target all booking issues by Friday"

## Labels Rules

Before assigning labels:

1. Read `.github/labels.yml` if present.
2. Use only labels defined there unless the user explicitly allows new labels.
3. Each issue must include at least one primary type/work-item label.
4. Add technical area, priority, status, or other labels only when relevant and available.
5. If creating real issues and a required label is missing on GitHub but exists in `.github/labels.yml`, create the missing label from `labels.yml`.

If `.github/labels.yml` is missing:

- Use labels from existing GitHub repository labels if available.
- Otherwise, place proposed labels in the draft and mark them as `Proposed`, not guaranteed.

## Issue Template Rules

Before drafting issues, inspect `.github/ISSUE_TEMPLATE/*.yml` when present.

Choose the most appropriate template:

- Bug issue -> bug report template.
- Functional requirement / feature -> feature or functional requirement template.
- Non-functional requirement -> NFR template.
- Technical task / documentation / setup -> task template.

If the repository's templates do not include required sections, add the missing sections in the Markdown issue body.

Required sections for requirement-derived issues:

- Source Trace
- Summary
- Goal
- Scope
- Non-Goals
- Business Rules or Requirement Details
- Implementation Notes, only when the source documents explicitly mention them
- Acceptance Criteria
- Project Metadata
- Labels
- Relationships
- Suggested Branch
- Notes for Assignee

## Title Rules

Issue titles must be in professional English.

Recommended format:

```text
[Module][Source Trace] Verb-Based Professional Title
```

Examples:

```text
[Booking][FR-05/FR-06] Implement Booking Creation With Window Validation
[Queue][FR-10/FR-11] Activate Service Period And Prevent Duplicate Activation
[Loyalty][FR-19] Recalculate Customer Loyalty From Completed Records
[Undo][FR-21] Restore Latest Completed Record With Related Rollback
[Persistence][FR-22/FR-23] Load And Save Data From Persistent Storage
```

Rules:

- Use English only for titles.
- Use a clear verb: Implement, Add, Support, Validate, Prevent, Recalculate, Restore, Sync, Generate, Refactor, Fix.
- Avoid vague titles such as "Update logic", "Fix feature", "Handle data".
- Keep titles concise but descriptive enough to generate a clean branch name.

## Suggested Branch Rules

Do not create branches.

Only write a suggested branch name in the issue body.

Format:

```text
<prefix>/<short-kebab-case-title>
```

Common prefixes:

```text
feature/    for feature work
fix/        for bugs
refactor/   for refactoring
docs/       for documentation
test/       for testing
data/       for persistence or data work
backend/    for backend/business logic work
chore/      for maintenance tasks
```

Example:

```text
feature/booking-window-validation
backend/loyalty-recalculation
fix/duplicate-period-activation
docs/update-prd-source-trace
```

## Implementation Notes Rules

Implementation Notes are allowed only when the source documents explicitly mention implementation constraints, technical choices, algorithms, storage mechanisms, architecture decisions, APIs, or data structures.

Do not propose new technical solutions as facts.

If a technical suggestion may be useful but is not in the source documents, place it under `Suggestion` and ask the user before including it in final issues.

Examples:

```text
Allowed: Source says the system uses text files. The issue may say: "Use text-file persistence as specified in the source document."
Not allowed: Source does not mention Redis. Do not add Redis.
Not allowed: Source does not mention Kafka. Do not add Kafka.
Not allowed: Source does not mention a database. Do not add a database.
```

## Draft Issue Body Template

Use Vietnamese issue bodies by default.

```md
# <Professional English Issue Title>

## Tóm tắt
Mô tả ngắn gọn issue này cần làm gì.

## Source Trace
- PRD: ...
- SRS/Spec: ...
- FR/NFR/UC/Business Rule: ...

## Mục tiêu
Mô tả kết quả mong muốn sau khi issue hoàn thành.

## Phạm vi
- ...

## Không nằm trong phạm vi
- ...

## Quy tắc nghiệp vụ / Yêu cầu liên quan
- ...

## Implementation Notes
Chỉ ghi nếu tài liệu nguồn có nêu rõ. Nếu không có, ghi: `Không có ghi chú triển khai cụ thể trong tài liệu nguồn.`

## Acceptance Criteria
- [ ] ...
- [ ] ...
- [ ] ...

## Project Metadata
- Type: ...
- Size: ...
- Story Points: ...
- Estimation Reason: ...
- Priority: ...
- Priority Reason: ...
- Start Date: TBD
- Target Date: TBD

## Labels
- ...

## Relationships
- Parent: None
- Blocked by: None
- Blocking: None
- Security alert: None

## Suggested Branch
`feature/example-branch-name`

## Ghi chú cho người thực hiện
- ...
```

## ISSUE_INDEX.md Template

Create an index grouped by module.

```md
# GitHub Issue Draft Index

## Summary
- Source documents:
  - ...
- Draft output directory: `.agent/report/github-issue-drafts/`
- Mode: Draft only
- Real GitHub issues created: No
- GitHub Project synced: No

## Module: <Module Name>

| No | Draft File | Title | Type | Size | Story Points | Priority | Source Trace | Dependencies | Relationships | Labels | Suggested Branch | Status | GitHub Issue |
|---|---|---|---|---|---:|---|---|---|---|---|---|---|---|
| 001 | 001-module-short-title.md | [Module][FR-xx] Title | ... | M | 5 | High | FR-xx, UC-xx | None | Parent: None | label-a, label-b | feature/example | Draft | N/A |
```

Allowed draft statuses:

```text
Draft
Needs Review
Approved
Created
Synced
```

Default status is `Draft`.

## Token-Saving Workflow

For large requirement documents or projects with many issues, do not perform the full workflow in one pass unless the user explicitly asks for it.

Prefer this phased workflow:

### Phase 1: Planning

Create only:

- `ISSUE_INDEX.md`.
- FR Traceability Table.
- Proposed issue list.
- Grouping/splitting reasons.
- Size and Story Points estimates.
- Dependencies.

Do not generate full issue body files yet.

### Phase 2: Draft Generation

Generate issue draft files only after the issue list is approved.

Rules:

- Only read the source sections needed for each issue.
- Avoid re-reading the entire SRS/PRD repeatedly.
- Reuse extracted source trace and decisions from `ISSUE_INDEX.md`.
- Do not print full draft bodies in chat unless the user explicitly asks.

### Phase 3: GitHub Creation

Create real GitHub Issues only from draft files explicitly listed in `ISSUE_INDEX.md`.

Rules:

- Do not regenerate issue bodies during creation unless required.
- Do not scan every `.md` file in the draft directory.
- Run preflight checks before creating issues.

### Phase 4: Project Sync

Sync normal Project fields after issues are created.

Normal Project fields include:

- Type.
- Priority.
- Story Points.
- Start date.
- Target date.
- Size, if the Project supports it.

Relationship sync is best-effort only.

### Phase 5: Final Report

Report only concise results:

- Created issue number.
- Title.
- URL.
- Synced fields.
- Failed fields and reasons.
- Relationship sync failures, if any.

Avoid printing full issue bodies in the final report.

## Reporting Rules

Do not print full issue bodies in chat unless the user asks.

When reporting planning, draft generation, issue creation, or Project sync results, use compact tables.

Preferred report format:

```md
| No | Issue | GitHub URL | Type | Priority | Story Points | Sync Status |
|---|---|---|---|---|---:|---|
```

Keep the final report concise. Put detailed information in files such as `ISSUE_INDEX.md`, not in chat.

## GitHub CLI Guidelines

When creating real GitHub Issues, prefer `gh issue create`.

When updating GitHub Projects, inspect Project fields first. Use `gh project` commands or GitHub GraphQL API as needed.

Never run destructive commands unless explicitly requested.

Never close issues, delete issues, delete labels, delete branches, force-push, or modify repository code as part of this skill.

## Safety Checklist Before Real GitHub Actions

Before creating issues:

- [ ] User explicitly requested real issue creation.
- [ ] `ISSUE_INDEX.md` exists.
- [ ] Draft files selected for creation are listed in `ISSUE_INDEX.md`.
- [ ] Every selected draft file exists.
- [ ] No unreferenced draft files remain in the final draft directory.
- [ ] No local `file:///` paths exist in drafts or in `ISSUE_INDEX.md`.
- [ ] Selected drafts are `Approved`, or the user explicitly selected `Draft`/`Needs Review` items.
- [ ] Labels are valid.
- [ ] Missing labels are defined in `.github/labels.yml` before creation.
- [ ] Issue bodies include Source Trace.
- [ ] Issue titles are in professional English.
- [ ] Full issue bodies will not be printed in chat unless requested.

Before syncing Project metadata:

- [ ] User explicitly requested Project sync.
- [ ] Project owner and number are known.
- [ ] Field IDs are known.
- [ ] Option IDs are known for single-select fields.
- [ ] Issue item IDs are known.
- [ ] No field is guessed.
- [ ] Relationship sync is treated as best-effort, not mandatory.
- [ ] Relationship target issue IDs can be resolved if relationship sync is attempted.

## Final Response After Draft Generation

After creating drafts, respond concisely with:

- Output directory.
- Number of draft issues.
- Number of proposed Epics.
- Any issues requiring user review.
- Link/path to `ISSUE_INDEX.md`.
- Reminder that no real GitHub Issues were created unless GitHub Creation Mode was explicitly requested.

Do not print full draft issue bodies unless the user explicitly asks.

## Final Response After Real Issue Creation

After creating real issues, respond concisely with:

- Number of issues created.
- Issue numbers and URLs.
- Labels applied.
- Any labels created from `.github/labels.yml`.
- Whether `ISSUE_INDEX.md` was updated.
- Whether GitHub Project sync was performed.
- Any skipped draft and reason.

Do not print full issue bodies unless the user explicitly asks.

## Final Response After Project Sync

After syncing Project metadata, respond concisely with:

- Project name/number.
- Issues synced.
- Normal fields updated.
- Relationship sync result, if attempted.
- Relationship sync failures and reasons.
- Issues skipped and why.
- Whether `ISSUE_INDEX.md` was updated to `Synced`.

Do not treat failed relationship sync as a full workflow failure when normal fields were synced successfully.
