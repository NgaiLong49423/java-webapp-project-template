# Documentation Finding Types

Use this reference when `SKILL.md` needs detailed examples for documentation consistency findings.

## 1. Structure Drift

The repository structure described in docs does not match the actual folder layout.

Examples:

```text
README.md says `agent/`, but the repo uses `.agent/`.
README.md says source code is under `src/`, but the repo uses `App/`.
AGENTS.md says reports go to `.agent/reports/`, but the repo uses `.agent/outputs/reports/`.
```

Typical severity:

- Major if it can make an agent create files in the wrong location.
- Minor if it is a non-blocking outdated diagram/list.
- Critical if it points to the wrong canonical source.

## 2. Broken or Local Links

Docs contain links that are broken or only work on one machine.

Examples:

```text
file:///d:/Github-Projects/project/README.md
D:\Github-Projects\project\docs\SRS.md
C:\Users\Name\Desktop\repo\...
```

Recommended fix:

```text
Use repository-relative links.
```

Typical severity:

- Major for canonical docs.
- Minor for supporting docs.
- Info if the file is clearly an example.

## 3. Version Scope Drift

Do not flag different document versions by default.

Valid:

```text
PRD.md Document Version: v1.0.0
SRS.md Document Version: v1.0.2
```

Report only when the same version scope conflicts.

Examples to report:

```text
README.md Project Version: v0.2.0
CHANGELOG.md has no v0.2.0 entry.
```

```text
PRD.md says it is based on SRS v1.0.1.
Current SRS.md is v1.0.3.
No baseline mapping explains whether this is intentional.
```

Severity:

- Info for missing baseline mapping.
- Major for conflicting project version.
- Critical if issue generation or implementation would use the wrong baseline.

## 4. Date Drift

Created or last updated dates conflict with documented changes.

Examples:

```text
SRS.md says Last Updated: 2026-06-28.
CHANGELOG.md has no nearby entry for a significant SRS change.
```

```text
Created: 2026-06-30
Last Updated: 2026-06-29
```

Severity:

- Minor for format/date mismatch.
- Major if it obscures the current canonical document.

## 5. Requirement Drift

Requirement documents disagree.

Examples:

```text
SRS.md says users can cancel bookings.
PRD.md does not mention cancellation.
GitHub issue templates include a cancellation label.
```

```text
README.md lists RFID as in scope.
SRS.md does not define RFID behavior.
```

Severity:

- Critical if implementation or issue decomposition would be wrong.
- Major if it only confuses scope.
- Info if likely intentional but undocumented.

## 6. Feature Status Drift

One document says a feature is complete while another says planned/draft/future.

Examples:

```text
README.md says booking module is completed.
SRS.md marks booking as future scope.
```

```text
CHANGELOG.md says loyalty feature was added.
SRS.md still marks loyalty as pending.
```

Severity:

- Major by default.
- Critical if it affects release readiness.

## 7. Database Drift

Database schema and requirements disagree.

Examples:

```text
SRS.md mentions a `LoyaltyPoint` entity.
database/schema.sql has no related table.
```

```text
database/schema.sql defines `BookingStatus`.
SRS.md does not define booking statuses.
```

```text
SRS.md says SQL Server.
database/README.md says MySQL.
```

Severity:

- Critical if core entities or DB technology conflict.
- Major if supporting tables/statuses are missing in docs.
- Minor for naming inconsistencies with clear mapping.

## 8. GitHub Config Drift

GitHub labels, templates, or workflow docs conflict.

Examples:

```text
Issue template uses label `feature`.
.github/labels.yml only defines `enhancement`.
```

```text
CONTRIBUTING.md says branch prefix `feat/`.
Issue template examples use `feature/`.
```

```text
PR template requires screenshots.
CONTRIBUTING.md says screenshots are optional.
```

Severity:

- Major if it breaks issue/PR workflow.
- Minor for wording mismatch.

## 9. Agent Contract Drift

Agent-facing docs conflict.

Examples:

```text
AGENTS.md says reports go to `.agent/reports/`.
repo-contract.yml says `.agent/outputs/reports/`.
```

```text
SKILL.md says active skills are under `.agent/skill/`.
repo uses `.agent/skills/active/`.
```

Severity:

- Critical if the agent may read the wrong canonical file.
- Major if outputs may be created in the wrong folder.

## 10. Placeholder Leakage

Template placeholders remain in real project documents.

Examples:

```text
[Tên Dự Án]
[Project Name]
TODO
TBD
Mô tả ngắn về dự án
```

Report only if the file appears to be a real project document, not a template/example.

Severity:

- Major in canonical docs.
- Minor in supporting docs.
- Info in examples/templates.

## 11. Language and Encoding Drift

Docs disagree on language or encoding expectations.

Examples:

```text
CONTRIBUTING.md says documentation must be Vietnamese.
README.md has unfinished mixed English/Vietnamese sections.
```

```text
Java terminal notes require English output to avoid encoding issues.
SRS.md requires Vietnamese CLI output.
```

Severity:

- Major if it affects implementation or testing.
- Minor if only wording consistency is affected.

## 12. Template Example Confusion

Examples are mixed with real project content.

Examples:

```text
CHANGELOG.md contains both a real v0.1.0 entry and an unmarked sample v0.1.0 entry.
```

```text
README.md has real setup instructions mixed with `[example command]`.
```

Recommended fix:

```text
Move examples to `docs/examples/` or clearly mark them as examples.
```

Severity:

- Major if agent can confuse sample with real state.
- Minor otherwise.
