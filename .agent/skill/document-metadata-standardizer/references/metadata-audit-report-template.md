# Metadata Audit Report Template

Use this template when auditing document metadata.

Default output path:

```text
.agent/outputs/reports/DOCUMENT_METADATA_REPORT.md
```

If the output folder does not exist, recommend creating it.

## Report Template

```markdown
# Document Metadata Report

## Summary

- Repository:
- Audit date:
- Files reviewed:
- Files with complete metadata:
- Files missing metadata:
- Files with invalid metadata:
- Version updates needed:
- Date issues:
- Overall status:

## Overall Status

Choose one:

| Status | Meaning |
|---|---|
| Ready | Metadata is complete enough for normal repo work |
| Needs Cleanup | Some metadata issues should be fixed |
| Not Ready | Metadata issues may cause wrong agent/contributor behavior |

## Files Reviewed

| File | Role | Metadata Status | Notes |
|---|---|---|---|
| `README.md` | Project overview | Complete / Missing / Invalid | |
| `docs/requirements/SRS.md` | Requirements | Complete / Missing / Invalid | |
| `docs/requirements/PRD.md` | Product requirements | Complete / Missing / Invalid | |
| `CHANGELOG.md` | Version history | Complete / Missing / Invalid | |
| `CONTRIBUTING.md` | Contribution rules | Complete / Missing / Invalid | |
| `AGENTS.md` | Agent instructions | Complete / Missing / Invalid | |

## Findings

| ID | Severity | File | Problem | Evidence | Recommended Fix |
|---|---|---|---|---|---|
| META-001 | Major | `docs/requirements/SRS.md` | Missing Version | Metadata block has no Version field | Add `> **Version:** v...` |
| META-002 | Minor | `README.md` | Invalid date format | Created is `29/6` | Use `2026-06-29` |
| META-003 | Major | `docs/requirements/SRS.md` | Draft version marked active | Version is `v0.3.0`, Status is `Active` | Change Status to `Under Review` or ask user to promote |
| META-004 | Critical | `docs/archive/SRS_v1.0.0.md` | Archived file marked active | Status is `Active` in archive folder | Change Status to `Archived` |

## Version Decisions

| File | Current Version | Recommended Version | Decision | Reason |
|---|---|---|---|---|
| `README.md` | v1.0.0 | v1.0.1 | PATCH | Fixed metadata path |
| `docs/requirements/SRS.md` | v0.2.0 | v0.2.1 | PATCH | Standardized date format while still draft |
| `docs/requirements/PRD.md` | v1.0.0 | No bump | No bump | Reviewed only, no content change |

## Date Checks

| File | Created | Last Updated | Result | Notes |
|---|---|---|---|---|
| `README.md` | 2026-06-29 | 2026-06-29 | OK | |
| `docs/requirements/SRS.md` | 2026-06-30 | 2026-06-29 | Invalid | Created date is after Last Updated |

## Draft / Under Review Documents

| File | Version | Status | Safe to Treat as Stable? | Notes |
|---|---|---|---|---|
| `docs/requirements/SRS.md` | v0.3.0 | Under Review | No | Needs user confirmation before issue decomposition |
| `docs/requirements/PRD.md` | v1.0.0 | Active | Yes | Stable |

## Missing Metadata Fields

| File | Missing Fields |
|---|---|
| `docs/requirements/SRS.md` | Version, Status |
| `database/README.md` | Created, Last Updated |

## Invalid Metadata Fields

| File | Field | Current Value | Expected Format |
|---|---|---|---|
| `README.md` | File | `D:\repo\README.md` | Repository-relative path |
| `CHANGELOG.md` | Created | `29/6` | `YYYY-MM-DD` |
| `AGENTS.md` | Version | `1.0.0` | `v1.0.0` |

## Recommended Fix Order

1. Fix Critical metadata issues.
2. Fix wrong Status on archived, deprecated, or draft documents.
3. Add missing required fields to canonical documents.
4. Standardize version and date formats.
5. Fix optional metadata only if it improves clarity.

## Files Suggested for Update

| File | Reason |
|---|---|
| `docs/requirements/SRS.md` | Missing required metadata fields |
| `README.md` | Local absolute path in metadata |
| `CHANGELOG.md` | Date format issue |

## Final Recommendation

State one of the following:

- Metadata is ready for normal repo work.
- Metadata should be cleaned before documentation audit.
- Metadata should be cleaned before GitHub Issue decomposition.
- Metadata should be cleaned before coding.
- Metadata should be cleaned before merge/release.
```

## Severity Guide

Use these severity levels.

### Critical

Metadata issue can make the agent or contributor use the wrong source of truth.

Examples:

- Two active SRS files both claim to be canonical.
- Archived document is marked `Active`.
- File metadata points to a different canonical file.
- Draft document is used as stable without confirmation.

### Major

Metadata issue can confuse version tracking or documentation sync.

Examples:

- Missing `Version` in SRS or PRD.
- Missing `Status` in canonical document.
- `Last Updated` is older than a known major change.
- `Version: v0.x.x` with `Status: Active`.

### Minor

Small metadata issue.

Examples:

- Date format is `29/6` instead of `2026-06-29`.
- File path uses backslashes but is still understandable.
- Optional field format is inconsistent.

### Info

Optional improvement.

Examples:

- Consider adding `Related Docs`.
- Consider adding `Baseline`.
- Consider moving examples to `docs/examples/`.

## Final Response Format

After metadata audit:

```text
Metadata audit completed.
Status: Ready / Needs Cleanup / Not Ready
Files reviewed: X
Missing metadata: X
Invalid metadata: X
Version decisions needed: X
Report: .agent/outputs/reports/DOCUMENT_METADATA_REPORT.md

Top issues:
1. ...
2. ...
3. ...
```

After metadata fixes:

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

Next recommended step:
- ...
```
