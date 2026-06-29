---

name: repo-template-doc-sync-auditor
description: Use this skill when the user asks to audit, review, synchronize, or fix documentation consistency in a repository that follows the standard Java webapp project template. This skill checks contradictions across README, SRS, project requirements, database docs, GitHub templates, changelog, AGENTS.md, and agent contract files before making any edits.
risk: medium
source: self
version: v1.0.1
created_date: 2026-06-29
last_updated_date: 2026-06-29
------------

# Repo Template Documentation Sync Auditor

This skill audits documentation consistency for repositories that follow the standard project template.

The main goal is to detect contradictions, outdated information, missing links, wrong paths, version drift, and documentation that no longer matches the repository structure.

## When to Use

Use this skill when the user asks to:

* Check whether repo documentation is consistent.
* Audit docs before coding, merging, or releasing.
* Review whether `README.md`, `SRS.md`, `CHANGELOG.md`, and database files match.
* Detect contradictions in a template-based repository.
* Synchronize documentation after changing requirements, database schema, issue templates, labels, or project structure.
* Create a report before editing documentation.
* Fix documentation only after an audit report is produced or the user explicitly requests fixes.

Example user requests:

```text
Check whether the repo docs have contradictions.
```

```text
Audit my template repo documentation before I start coding.
```

```text
Sync README, SRS, CHANGELOG, and database docs.
```

```text
Find outdated docs in this repo.
```

```text
Fix the documentation inconsistencies you found.
```

## Do Not Use

Do not use this skill when:

* The user only asks to write a new feature.
* The user only asks to debug code or CI.
* The user only asks to create GitHub Issues from SRS.
* The user only asks to write a README from scratch.
* The repository does not contain enough documentation to compare.
* The user asks for broad software advice unrelated to repository files.

If another skill is more specific, use the more specific skill first.

## Expected Repository Template

Assume the repository may contain these standard files and folders:

```text
.
├── AGENTS.md
├── README.md
├── CHANGELOG.md
├── CONTRIBUTING.md
├── LICENSE
├── App/
├── database/
│   ├── README.md
│   ├── schema.sql
│   ├── sample-data.sql
│   └── queries.sql
├── docs/
│   ├── README.md
│   ├── requirements/
│   │   ├── SRS.md
│   │   └── project-requirements.md
│   ├── diagrams/
│   └── reports/
├── .github/
│   ├── ISSUE_TEMPLATE/
│   ├── labels.yml
│   └── pull_request_template.md
└── .agent/
    ├── repo-contract.yml
    ├── skills/
    │   ├── active/
    │   ├── reference/
    │   └── archive/
    └── outputs/
        ├── reports/
        ├── drafts/
        └── logs/
```

The repo may not contain every file. Missing expected files should be reported only when they affect the requested audit.

## Canonical Sources

Prefer these files as the source of truth:

| Information Type                | Canonical Source                            |
| ------------------------------- | ------------------------------------------- |
| Project overview                | `README.md`                                 |
| Functional requirements         | `docs/requirements/SRS.md`                  |
| High-level project requirements | `docs/requirements/PRD.md` |
| Version history                 | `CHANGELOG.md`                              |
| Contribution workflow           | `CONTRIBUTING.md`                           |
| Database schema                 | `database/schema.sql`                       |
| Database usage notes            | `database/README.md`                        |
| GitHub labels                   | `.github/labels.yml`                        |
| GitHub issue format             | `.github/ISSUE_TEMPLATE/`                   |
| Agent behavior                  | `AGENTS.md`                                 |
| Repository contract             | `.agent/repo-contract.yml`                  |
| Agent outputs                   | `.agent/outputs/`                           |

If `.agent/repo-contract.yml` exists, follow it first. If it conflicts with this skill, report the conflict instead of silently choosing one.

## Operating Modes

### Audit Mode

Default mode.

In audit mode:

1. Read the repository structure.
2. Identify canonical documents.
3. Detect contradictions and outdated content.
4. Produce a report.
5. Do not modify files unless the user explicitly asks.

### Fix Mode

Use fix mode only when the user explicitly asks to fix, update, rewrite, or synchronize files.

In fix mode:

1. Start from the audit findings.
2. Apply minimal edits.
3. Preserve the intended meaning of requirements.
4. Do not invent new requirements.
5. Update `CHANGELOG.md` when the change is significant.
6. Summarize every changed file.
7. Verify that the edited files no longer contradict each other.

## Audit Workflow

### Step 1: Identify Repository Root

Locate the repo root by checking for:

```text
README.md
CHANGELOG.md
CONTRIBUTING.md
AGENTS.md
.github/
docs/
database/
.agent/
```

If multiple roots are possible, choose the directory containing the most template markers.

### Step 2: Read Agent Instructions

Read these files first if they exist:

```text
AGENTS.md
.agent/repo-contract.yml
CONTRIBUTING.md
```

Use them to determine:

* Which files are canonical.
* Which files are archived.
* Which files the agent may edit.
* Which commands or workflows must be followed.
* Where reports and drafts should be written.

### Step 3: Build Documentation Inventory

Create an internal inventory of relevant files:

```text
README.md
CHANGELOG.md
CONTRIBUTING.md
docs/**/*.md
database/**/*.sql
database/**/*.md
.github/**/*.md
.github/**/*.yml
.github/**/*.yaml
.agent/**/*.md
.agent/**/*.yml
.agent/**/*.yaml
```

Ignore these by default:

```text
.git/
node_modules/
target/
build/
dist/
out/
.class files
archive folders unless needed
```

If archived files contain information that conflicts with canonical files, only report it when the archive is not clearly marked as archived.

### Step 4: Extract Key Facts

Extract facts from each canonical file.

Important fact groups:

* Project name
* Project type
* Technology stack
* Java version
* Build tool
* Database type
* Main features
* Functional requirements
* Non-functional requirements
* Actors and roles
* Entity names
* Database table names
* Version number
* Created date
* Last updated date
* GitHub labels
* Issue types
* Branch workflow
* Output folders
* Agent skill folders

### Step 5: Cross-Check Consistency

Compare facts across documents.

Check for these inconsistency types:

#### 1. Structure Drift

Repository structure described in docs does not match actual folders.

Examples:

```text
README.md says `agent/`, but the repo uses `.agent/`.
```

```text
README.md says `src/`, but source code is under `App/`.
```

#### 2. Broken or Local Links

Detect links that are invalid, local-only, or not portable.

Examples:

```text
file:///d:/...
C:\Users\...
D:\Github-Projects\...
```

Prefer relative links.

#### 3. Version Drift

Do not treat different document versions as an issue by default.

Each document may have its own independent `Document Version`.

Only report version drift when files conflict on the same version scope.

Version scopes:

| Scope | Meaning | Consistency Rule |
|---|---|---|
| Document Version | Version of one document only | May differ across files |
| Project Version | Version of the whole project/product | Should be consistent across canonical docs |
| Baseline Version | A documented release/baseline tying multiple docs together | Should have clear mapping |

Examples that are not issues:

```text
PRD.md Document Version: v1.0.0
SRS.md Document Version: v1.0.2
```


#### 4. Date Drift

Created date or last updated date is inconsistent.

Examples:

```text
SRS.md says last updated 2026-06-28.
CHANGELOG.md has no entry near 2026-06-28.
```

#### 5. Requirement Drift

Requirements differ between SRS, project requirements, README, issue drafts, and implementation notes.

Examples:

```text
SRS.md says users can cancel bookings.
README.md does not mention cancellation.
GitHub issue templates contain cancellation labels, but SRS has no cancellation FR.
```

#### 6. Feature Status Drift

A feature is described as complete in one file and planned in another.

Examples:

```text
README.md says the booking module is completed.
SRS.md marks booking as future scope.
```

#### 7. Database Drift

Database schema does not match requirements.

Examples:

```text
SRS.md mentions a `LoyaltyPoint` entity.
database/schema.sql has no related table.
```

```text
database/schema.sql has `BookingStatus`.
SRS.md does not define booking statuses.
```

#### 8. GitHub Config Drift

GitHub labels, issue templates, and project workflow conflict.

Examples:

```text
Issue template uses label `feature`.
.github/labels.yml only defines `enhancement`.
```

```text
CONTRIBUTING.md says use branch prefix `feat/`.
Issue template examples use `feature/`.
```

#### 9. Agent Contract Drift

Agent documentation conflicts with repo contract or skill folder structure.

Examples:

```text
AGENTS.md says reports go to `.agent/reports/`.
repo-contract.yml says reports go to `.agent/outputs/reports/`.
```

#### 10. Placeholder Leakage

Template placeholders remain in real project files.

Examples:

```text
[Tên Dự Án]
[Project Name]
TODO
TBD
Mô tả ngắn về dự án
```

Report placeholders only if they appear in files that look like real project documents, not example templates.

#### 11. Encoding and Language Drift

Detect inconsistent documentation language or encoding assumptions.

Examples:

```text
CONTRIBUTING.md says write docs in Vietnamese.
README.md has mixed unfinished English/Vietnamese sections.
```

```text
Java terminal notes require English output, but docs still require Vietnamese CLI output.
```

#### 12. Template Example Confusion

Examples are mixed with real project content.

Examples:

```text
CHANGELOG.md contains a real v0.1.0 entry and an unmarked sample v0.1.0 entry.
```

Move examples to `docs/examples/` or clearly mark them as examples.

## Severity Levels

Use these severity levels:

### Critical

A contradiction can cause wrong implementation, wrong database design, wrong issue creation, or broken workflow.

Examples:

```text
SRS.md and database/schema.sql define different core entities.
```

```text
AGENTS.md points agents to the wrong canonical SRS file.
```

### Major

A contradiction can confuse contributors or agents but does not immediately break implementation.

Examples:

```text
README.md describes an outdated folder structure.
```

```text
Issue templates use labels missing from labels.yml.
```

### Minor

A small inconsistency, typo, outdated date, formatting issue, or non-blocking docs mismatch.

Examples:

```text
One file says last updated 28/06 while another says 2026-06-28.
```

### Info

Useful note, improvement suggestion, or optional cleanup.

Examples:

```text
Consider moving examples out of CHANGELOG.md.
```

## Required Output

In audit mode, write or propose this report:

```text
.agent/outputs/reports/DOC_CONSISTENCY_REPORT.md
```

If the output folder does not exist, report that it should be created.

The report must use this structure:

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

## Files Reviewed
| File | Role | Status |
|---|---|---|

## Findings
| ID | Severity | Area | Problem | Evidence | Recommended Fix | Owner Decision Needed |
|---|---|---|---|---|---|---|

## Cross-Document Checks
| Check | Result | Notes |
|---|---|---|

## Suggested Fix Order
1. Critical issues
2. Major requirement/database drift
3. Broken links and structure drift
4. Version and changelog drift
5. Minor cleanup

## Files Suggested for Update
| File | Reason |
|---|---|

## Final Recommendation
State whether the repo is ready for coding, ready for issue decomposition, ready for merge, or needs documentation cleanup first.
```

## Evidence Rules

Every finding must include concrete evidence.

Good evidence:

```text
README.md says the agent folder is `agent/`, but the repo contains `.agent/`.
```

Bad evidence:

```text
Docs seem outdated.
```

If line numbers are available, include them. If not, include section names or exact quoted phrases.

Do not report guesses as facts. Mark uncertain findings as `Info` or state what must be checked manually.

## Fix Rules

When fixing documentation:

* Make the smallest change that resolves the contradiction.
* Preserve user-approved requirements.
* Do not invent new features.
* Do not remove requirements unless the user explicitly approves.
* Do not change database schema unless the user asks.
* Prefer updating docs to match canonical sources.
* Prefer relative links over absolute local paths.
* Update `CHANGELOG.md` for meaningful documentation changes.
* Keep examples separate from real project history.
* Do not edit archived files unless the user asks.

## Changelog Rules

Update `CHANGELOG.md` when:

* Canonical requirements change.
* Repo structure changes.
* Database contract changes.
* GitHub workflow changes.
* Agent contract or skill folder structure changes.
* Major documentation inconsistencies are fixed.

Do not update `CHANGELOG.md` for tiny typo-only edits unless the repo convention requires it.

Use a clear entry such as:

```markdown
## [Unreleased]

### Changed
- Synchronized repository documentation paths with the standard template structure.

### Fixed
- Fixed inconsistent references to `.agent/` across README and agent documentation.
```

## AGENTS.md Rules

If `AGENTS.md` is missing, recommend creating it.

A valid `AGENTS.md` should be concise and include:

```markdown
# Agent Instructions

## Canonical Docs
- Requirements: `docs/requirements/SRS.md`
- Project overview: `README.md`
- Changelog: `CHANGELOG.md`
- Contribution rules: `CONTRIBUTING.md`
- Database schema: `database/schema.sql`
- Agent contract: `.agent/repo-contract.yml`

## Project Layout
- App source: `App/`
- Database scripts: `database/`
- Documentation: `docs/`
- GitHub config: `.github/`
- Agent skills and outputs: `.agent/`

## Documentation Rules
- Report contradictions before editing requirement documents.
- Update `CHANGELOG.md` after major docs, database, feature, or structure changes.
- Use relative links only.

## Commit Rules
- Follow `CONTRIBUTING.md`.
- AI commits must include a `Co-Authored-By` line when applicable.
```

Keep `AGENTS.md` short. Do not paste full SRS, README, or workflow explanations into it.

## repo-contract.yml Rules

If `.agent/repo-contract.yml` is missing, recommend creating it.

Suggested minimal contract:

```yaml
project_type: java-webapp-template

canonical_docs:
  overview: README.md
  requirements: docs/requirements/SRS.md
  project_requirements: docs/requirements/project-requirements.md
  changelog: CHANGELOG.md
  contribution: CONTRIBUTING.md
  database_schema: database/schema.sql
  database_readme: database/README.md
  agent_instructions: AGENTS.md

agent_paths:
  skills_active: .agent/skills/active
  skills_reference: .agent/skills/reference
  skills_archive: .agent/skills/archive
  reports: .agent/outputs/reports
  drafts: .agent/outputs/drafts
  logs: .agent/outputs/logs

sync_rules:
  - when: docs/requirements/SRS.md changes
    check:
      - README.md
      - docs/requirements/project-requirements.md
      - CHANGELOG.md
      - .github/ISSUE_TEMPLATE
  - when: database/schema.sql changes
    check:
      - database/README.md
      - docs/requirements/SRS.md
      - docs/diagrams
      - CHANGELOG.md
  - when: .github/labels.yml changes
    check:
      - .github/ISSUE_TEMPLATE
      - CONTRIBUTING.md
  - when: AGENTS.md changes
    check:
      - .agent/repo-contract.yml
      - .agent/skills/active
```

## Safety Boundaries

Do not:

* Run destructive commands.
* Delete files unless explicitly requested.
* Rewrite requirements without user approval.
* Treat archived files as canonical.
* Create new project scope.
* Add new technologies, frameworks, database tables, or features unless requested.
* Claim the repo is consistent without checking the required canonical documents.

## Completion Criteria

The task is complete only when one of these is true:

### Audit completed

* Relevant files were reviewed.
* Findings were grouped by severity.
* Evidence was provided.
* Recommended fixes were listed.
* Final readiness status was stated.

### Fix completed

* Audit findings were addressed.
* Changed files were summarized.
* `CHANGELOG.md` was updated if needed.
* Remaining issues were listed.
* The final status was stated.

## Final Response Format

When responding to the user after audit mode, summarize:

```text
Audit completed.
Status: Ready / Needs cleanup / Not ready.
Critical: X
Major: X
Minor: X
Report: .agent/outputs/reports/DOC_CONSISTENCY_REPORT.md
Top issues:
1. ...
2. ...
3. ...
```

When responding after fix mode, summarize:

```text
Documentation sync completed.
Changed files:
- ...
Fixed issues:
- ...
Remaining issues:
- ...
Next recommended step:
- ...
```
