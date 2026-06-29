# Documentation Consistency Report Template

Default output path:

```text
.agent/outputs/reports/DOC_CONSISTENCY_REPORT.md
```

## Template

```markdown
# Documentation Consistency Report

## Summary

- Repository:
- Audit date:
- Overall status:
- Critical issues:
- Major issues:
- Minor issues:
- Info notes:

## Overall Status

Choose one:

| Status | Meaning |
|---|---|
| Ready | Docs are consistent enough for the requested next step |
| Needs Cleanup | Docs have issues but are still understandable |
| Not Ready | Docs may cause wrong implementation, issue generation, or workflow |

## Files Reviewed

| File | Role | Status | Notes |
|---|---|---|---|
| `README.md` | Project overview | Reviewed / Missing / Skipped | |
| `docs/requirements/SRS.md` | Functional requirements | Reviewed / Missing / Skipped | |
| `docs/requirements/PRD.md` | Product requirements | Reviewed / Missing / Skipped | |
| `CHANGELOG.md` | Version history | Reviewed / Missing / Skipped | |
| `CONTRIBUTING.md` | Contribution workflow | Reviewed / Missing / Skipped | |
| `database/schema.sql` | Database schema | Reviewed / Missing / Skipped | |
| `database/README.md` | Database docs | Reviewed / Missing / Skipped | |
| `.github/labels.yml` | GitHub labels | Reviewed / Missing / Skipped | |
| `.github/ISSUE_TEMPLATE/` | Issue templates | Reviewed / Missing / Skipped | |
| `AGENTS.md` | Agent instructions | Reviewed / Missing / Skipped | |
| `.agent/repo-contract.yml` | Repo contract | Reviewed / Missing / Skipped | |

## Findings

| ID | Severity | Area | Problem | Evidence | Recommended Fix | Owner Decision Needed |
|---|---|---|---|---|---|---|
| DOC-001 | Major | Structure | README says `agent/`, repo uses `.agent/` | `README.md` folder tree vs actual folder | Update README path | No |
| DOC-002 | Critical | Database | SRS and schema define different core entity names | SRS: `Customer`; schema: no customer table | Decide canonical entity model | Yes |

## Cross-Document Checks

| Check | Result | Notes |
|---|---|---|
| README vs repo structure | Pass / Fail / Skipped | |
| SRS vs PRD | Pass / Fail / Skipped | |
| SRS vs database schema | Pass / Fail / Skipped | |
| README vs CHANGELOG | Pass / Fail / Skipped | |
| GitHub templates vs labels.yml | Pass / Fail / Skipped | |
| AGENTS.md vs repo-contract.yml | Pass / Fail / Skipped | |
| Metadata/version scope | Pass / Fail / Skipped | |

## Draft / Under Review Notes

| File | Version | Status | Stable Source? | Notes |
|---|---|---|---|---|
| `docs/requirements/SRS.md` | v0.3.0 | Under Review | No | User confirmation needed before issue generation |

## Suggested Fix Order

1. Critical issues that can cause wrong implementation or issue generation.
2. Major requirement/database drift.
3. Agent contract and path drift.
4. Broken links and structure drift.
5. Version scope and baseline mapping issues.
6. Minor cleanup.

## Files Suggested for Update

| File | Reason |
|---|---|
| `README.md` | Folder structure drift |
| `docs/requirements/SRS.md` | Requirement/database mismatch |
| `.agent/repo-contract.yml` | Missing or outdated canonical paths |

## Final Recommendation

State one:

- Ready for coding.
- Ready for GitHub Issue decomposition.
- Ready for merge.
- Needs documentation cleanup first.
- Not ready until owner decisions are made.
```

## Final Response Summary

After writing the report, summarize:

```text
Audit completed.
Status: Ready / Needs cleanup / Not ready
Critical: X
Major: X
Minor: X
Info: X
Report: .agent/outputs/reports/DOC_CONSISTENCY_REPORT.md

Top issues:
1. ...
2. ...
3. ...
```
