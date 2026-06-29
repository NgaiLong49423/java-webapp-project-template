---
name: document-metadata-standardizer
description: Use this skill when the user asks to add, update, audit, or standardize metadata at the top of Markdown documentation files, including document version, created date, last updated date, status, and version bump decisions after document edits.
risk: low
source: self
version: v1.1.0
created_date: 2026-06-29
last_updated_date: 2026-06-29
---

# Document Metadata Standardizer

Standardize metadata for repository documentation files.

This skill focuses only on document metadata and document versioning. It does not judge whether requirements are correct, except when metadata or version state creates confusion.

## When to Use

Use this skill for:

- Adding or standardizing metadata in Markdown docs.
- Auditing docs for missing or invalid metadata.
- Updating metadata after document edits.
- Deciding document version bumps.
- Creating new Markdown documentation files.
- Preparing docs before audit, issue decomposition, merge, or release.

Target files:

```text
CONTRIBUTING.md
AGENTS.md
docs/**/*.md
database/**/*.md
.github/**/*.md
.agent/**/*.md
```

Do not apply to code, generated outputs, binaries, archives, SQL/YAML/XML configs, or dependency/build folders unless explicitly requested.

Ignore by default:

```text
.git/ node_modules/ target/ build/ dist/ out/
*.class *.jar *.zip *.rar *.png *.jpg *.pdf
*.sql *.java *.xml *.yml *.yaml
```

## Required Metadata

Every important Markdown document should start with this block before the first heading:

```markdown
> **Document:** Document Name  
> **File:** `relative/path/to/file.md`  
> **Version:** v1.0.0  
> **Created:** YYYY-MM-DD  
> **Last Updated:** YYYY-MM-DD  
> **Status:** Active  
```

Required fields:

| Field | Rule |
|---|---|
| Document | Human-readable name; no `[Project Name]`, `TODO`, or `TBD` |
| File | Repo-relative path only; never `D:\...` or `file:///...` |
| Version | Document version in `vMAJOR.MINOR.PATCH` format |
| Created | First creation date in `YYYY-MM-DD`; preserve unless missing/wrong |
| Last Updated | Latest intentional edit date in `YYYY-MM-DD` |
| Status | `Draft`, `Under Review`, `Active`, `Deprecated`, `Archived`, or `Template` |

Optional fields may be added only when useful:

```markdown
> **Owner:** Team/Person  
> **Related Docs:** `README.md`, `CHANGELOG.md`  
> **Project Version:** v0.2.0  
> **Baseline:** Project Baseline v0.2.0  
```

Do not invent `Project Version` or `Baseline`.

## Version Scope Rules

Always distinguish:

- **Document Version**: version of one file.
- **Project Version**: version of the software/project.
- **Baseline Version**: version of a group of approved docs.

Different documents may have different document versions.

Valid:

```text
PRD.md: v1.0.0
SRS.md: v1.0.2
```

Do not report different document versions as an issue unless the files conflict on the same version scope.

## Draft Version Rule

Versions starting with `v0.` mean the document is still draft/under review.

For `v0.x.x` documents:

- Do not treat them as stable source of truth unless the user explicitly confirms.
- Do not rewrite large sections unless explicitly requested.
- Do not use them as the only basis for GitHub Issue creation unless confirmed.
- Prefer reporting recommendations instead of direct edits.
- Safe metadata-only fixes are allowed when requested.

Recommended status for `v0.x.x`:

```text
Draft
Under Review
```

If `Version` starts with `v0.` but `Status` is `Active`, report a warning.

Do not promote `v0.x.x` to `v1.0.0` automatically. User approval is required.

Promotion rule:

```text
v0.x.x + user approval -> v1.0.0 + Status: Active
```

## Version Bump Rules

### No Bump

Do not increase version when:

- The file was only read/reviewed.
- No file content changed.
- Only Git metadata changed.
- The file is generated.
- The file is archived and the user did not ask to edit archived docs.

### PATCH

Increase PATCH for small edits that do not change meaning.

Examples:

```text
v1.0.2 -> v1.0.3
v0.2.0 -> v0.2.1
```

Use PATCH for typo/grammar fixes, formatting cleanup, metadata correction, broken link fixes, local path fixes, small wording clarification, or folder name correction such as `agent/` to `.agent/`.

### MINOR

Increase MINOR for meaningful additions that keep the previous intent compatible.

Examples:

```text
v1.0.2 -> v1.1.0
v0.2.1 -> v0.3.0
```

Use MINOR for adding/expanding sections, requirements, scenarios, workflows, roles, diagrams, references, documentation areas, or standard metadata for a file newly added to the template standard.

### MAJOR

Increase MAJOR for changes that alter scope, contract, source-of-truth behavior, or implementation direction.

Example:

```text
v1.2.3 -> v2.0.0
```

Use MAJOR for core scope changes, replacing/removing major requirements, architecture/database changes, approved hardware/main technology changes, canonical document changes, template-to-active conversion, or active document deprecation/replacement.

## Date Rules

- Preserve `Created` if it exists.
- If `Created` is missing, infer from file history, changelog, repo creation, or current date.
- If inferred, state that it was inferred.
- Use the current edit date for `Last Updated`, unless the user provides a specific date.
- Convert dates to `YYYY-MM-DD`.
- Ensure `Created` is not after `Last Updated`.

## Audit Workflow

1. Find target Markdown docs.
2. Check required metadata fields.
3. Validate path, version format, date format, status, placeholders, and local paths.
4. Check `Created <= Last Updated`.
5. Classify each edit as `No bump`, `PATCH`, `MINOR`, or `MAJOR`.
6. Report findings, or apply minimal metadata fixes if the user asked to fix.

## Audit Output

When auditing, produce:

```markdown
# Document Metadata Report

## Summary
- Files reviewed:
- Missing metadata:
- Invalid metadata:
- Version updates needed:
- Date issues:
- Overall status:

## Findings
| File | Issue | Severity | Recommended Fix |
|---|---|---|---|

## Version Decisions
| File | Current Version | Recommended Version | Reason |
|---|---|---|---|
```

Severity:

| Severity | Use When |
|---|---|
| Critical | Metadata can make agent/contributor use the wrong source of truth |
| Major | Metadata can confuse version tracking or documentation sync |
| Minor | Small metadata/date/format problem |
| Info | Optional improvement |

## Fix Rules

When fixing metadata:

- Make minimal edits.
- Do not rewrite document content unless needed for metadata.
- Do not change `Created` unless missing or clearly wrong.
- Always update `Last Updated` when editing.
- Increase version according to the bump rules.
- Do not force document versions to match across files.
- Do not invent `Project Version` or `Baseline`.
- Do not mark a template, example, or archive as `Active`.
- Use repository-relative paths only.
- Preserve existing language and heading style.
- Treat `v0.x.x` documents as draft/under review.

## Completion Criteria

The task is complete when required metadata exists, metadata format is valid, version bump decisions are explained, `Created` is preserved where possible, `Last Updated` reflects the latest intentional edit, `v0.x.x` documents are not treated as stable unless approved, and no document version is forced to match another document version.

## Final Response Format

Audit mode:

```text
Metadata audit completed.
Files reviewed: X
Missing metadata: X
Invalid metadata: X
Version updates needed: X
Top issues:
1. ...
2. ...
3. ...
```

Fix mode:

```text
Metadata standardization completed.
Updated files:
- ...
Version changes:
- ...
Date changes:
- ...
Remaining issues:
- ...
```
