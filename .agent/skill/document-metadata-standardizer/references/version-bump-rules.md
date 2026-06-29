# Version Bump Rules

This reference file explains how to decide document version changes.

Use this file when the main `SKILL.md` needs a more detailed version decision.

## Core Rule

Always distinguish between:

| Version Type | Meaning | Must Match Across Docs? |
|---|---|---|
| Document Version | Version of one document file | No |
| Project Version | Version of the software/project | Usually yes |
| Baseline Version | Version of a group of approved documents | Should have clear mapping |

Do not report an issue only because two documents have different document versions.

Valid example:

```text
PRD.md Document Version: v1.0.0
SRS.md Document Version: v1.0.2
```

This is valid because PRD and SRS can evolve independently.

## Version Format

Use:

```text
vMAJOR.MINOR.PATCH
```

Example:

```text
v1.0.2
```

## v0.x.x Draft Rule

Versions starting with `v0.` mean the document is still draft or under review.

Examples:

```text
v0.1.0
v0.2.3
v0.9.9
```

Meaning:

- The document is not fully approved.
- The document may still change significantly.
- The document should not be treated as stable unless the user confirms.
- The agent should avoid direct heavy edits unless explicitly asked.
- The agent should prefer recommendations or draft patches.

Recommended status:

```text
Draft
Under Review
```

Warning condition:

```text
Version: v0.3.0
Status: Active
```

Recommended response:

```text
Version is v0.3.0, which indicates draft/under review, but Status is Active.
Recommended fix: change Status to Draft/Under Review or ask the user whether it should be promoted to v1.0.0.
```

## Promotion to v1.0.0

Promote to `v1.0.0` only when the user confirms the document is stable.

Conditions:

- Main content has been reviewed.
- The document is approved as a stable reference.
- The document can guide coding, issue decomposition, testing, or planning.
- The user confirms it is no longer draft.

Do not automatically promote `v0.x.x` to `v1.0.0`.

## No Version Bump

Do not increase version when:

| Case | Reason |
|---|---|
| File was only read | No content change |
| File was only reviewed | No content change |
| Change happened only in Git metadata | Document content unchanged |
| Archived file was not intentionally edited | Historical copy should remain stable |
| Generated file was regenerated automatically | Manual document version may not apply |

## PATCH

Increase PATCH for small changes that do not change document meaning.

Pattern:

```text
v1.0.2 -> v1.0.3
```

For draft documents:

```text
v0.2.0 -> v0.2.1
```

Use PATCH for:

| Change | Example |
|---|---|
| Typo fix | Fix misspelled heading |
| Grammar cleanup | Improve sentence wording |
| Formatting cleanup | Fix table alignment |
| Metadata correction | Correct file path in metadata |
| Date format fix | `28/6` -> `2026-06-28` |
| Broken relative link fix | Fix `docs/SRS.md` link |
| Local link fix | Remove `file:///d:/...` |
| Folder name correction | `agent/` -> `.agent/` |
| Small clarification | Clarify wording without changing requirement |
| Status metadata fix | `Active` -> `Under Review` for `v0.x.x` |

PATCH does not add new meaning.

## MINOR

Increase MINOR for meaningful additions that remain compatible with the previous document intent.

Pattern:

```text
v1.0.2 -> v1.1.0
```

For draft documents:

```text
v0.2.1 -> v0.3.0
```

Use MINOR for:

| Change | Example |
|---|---|
| Add new section | Add `Demo Scenarios` |
| Add new functional requirement | Add FR for booking cancellation |
| Add new non-functional requirement | Add response-time requirement |
| Add new actor/role | Add Admin role |
| Add new scenario | Add fire alert demo scenario |
| Add hardware/module description | Add RC522 module description |
| Add database documentation | Add table explanation |
| Add GitHub workflow | Add branch naming workflow |
| Expand accepted content | Add examples or cases that affect understanding |
| Add metadata to a newly standardized document | Make document part of template standard |

MINOR adds useful content but does not break the old intent.

## MAJOR

Increase MAJOR for changes that alter scope, contract, architecture, or source-of-truth behavior.

Pattern:

```text
v1.2.3 -> v2.0.0
```

Use MAJOR for:

| Change | Example |
|---|---|
| Change core scope | Web app becomes mobile app |
| Replace major requirements | Remove booking module and add queue-only module |
| Change main architecture | MVC Servlet/JSP -> Spring Boot REST |
| Change database model | SQL Server schema replaced by PostgreSQL model |
| Change approved hardware list | Replace ESP32-CAM with another board |
| Change canonical source | PRD replaces SRS as requirements source |
| Breaking workflow change | Branch rules or release workflow are replaced |
| Rewrite document structure | Old section references no longer apply |
| Active -> Deprecated replacement | A new canonical file replaces an old one |
| Template -> Active conversion | Template becomes real project document |

MAJOR changes can affect implementation, planning, testing, or issue decomposition.

## Decision Table

| Situation | Version Change |
|---|---|
| Read/review only | No bump |
| Fix typo | PATCH |
| Fix broken link | PATCH |
| Fix metadata path | PATCH |
| Add missing metadata to existing standard doc | PATCH |
| Add metadata and make document part of template standard | MINOR |
| Add new section | MINOR |
| Add new requirement | MINOR |
| Add new actor/role | MINOR |
| Add new demo scenario | MINOR |
| Remove a requirement | MAJOR |
| Change database technology | MAJOR |
| Change approved hardware list | MAJOR |
| Change source of truth | MAJOR |
| Promote draft to stable | v1.0.0, only after user confirmation |
| Edit archived file | Avoid unless user explicitly asks |

## Status and Version Consistency

| Version | Recommended Status | Notes |
|---|---|---|
| `v0.x.x` | Draft / Under Review | Not stable |
| `v1.0.0` | Active | First stable version |
| `v1.x.x` | Active | Stable document updates |
| `v2.0.0+` | Active | Stable document with major changes |
| Any version | Archived | Historical copy |
| Any version | Deprecated | Not canonical |
| Any version | Template | Reusable pattern, not project truth |

## Ambiguous Cases

If the change is unclear:

1. Prefer the smaller bump.
2. Explain the uncertainty.
3. Ask for user confirmation only when the decision affects stability, scope, or source of truth.

Examples:

```text
This looks like a MINOR change because it adds a new section, but it may be MAJOR if the section changes project scope.
```

```text
This v0.x.x document should not be promoted to v1.0.0 without user approval.
```
