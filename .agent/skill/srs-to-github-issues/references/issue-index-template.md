# ISSUE_INDEX.md Template

Create this file at:

```text
.agent/outputs/drafts/github-issues/ISSUE_INDEX.md
```

If the repo contract defines another path, use the repo contract path.

```md
# GitHub Issue Draft Index

## Summary
- Source documents:
  - ...
- Draft output directory: `.agent/outputs/drafts/github-issues/`
- Mode: Draft only
- Real GitHub issues created: No
- GitHub Project synced: No

## Source Hierarchy
1. SRS / detailed requirements:
2. PRD / product overview:
3. Use case docs:
4. Architecture/design notes:
5. README/high-level docs:

## Traceability Table

| Source ID | Source Section | Proposed Issue(s) | Notes |
|---|---|---|---|
| FR-01 | ... | 001 | ... |

## Module: <Module Name>

| No | Draft File | Title | Type | Size | Story Points | Priority | Source Trace | Dependencies | Relationships | Labels | Suggested Branch | Status | GitHub Issue |
|---|---|---|---|---|---:|---|---|---|---|---|---|---|---|
| 001 | 001-module-short-title.md | [Module][FR-xx] Title | Feature | M | 5 | High | FR-xx | None | Parent: None | label-a | feature/example | Draft | N/A |

## Grouping / Splitting Decisions

| Source | Decision | Reason |
|---|---|---|
| FR-01 | Split into 001, 002 | Too large for one implementation issue |

## Review Notes

- Items requiring user confirmation:
  - ...
```

## Allowed Draft Statuses

```text
Draft
Needs Review
Approved
Created
Synced
```

Default status: `Draft`.

## Index Rules

- `ISSUE_INDEX.md` is the single source of truth for real issue creation.
- Every listed draft file must exist.
- Every `.md` draft file in the final draft directory must be listed.
- Do not create real GitHub Issues from files not listed in the index.
