---
name: pr-issue-review
description: Review a pull request against its stated scope, repository rules, and verifiable evidence. Use stable findings and exact commit snapshots; this skill does not authorize submitting reviews, changing Issues, or merging.
risk: medium
source: created
version: v1.0.0
created_date: 2026-10-09
last_updated_date: 2026-10-09
---

# Pull Request Review

## Review procedure

1. Confirm repository, PR, base branch, head SHA, and current base SHA. State if any cannot be verified.
2. Read the PR description, linked requirements or Issue, repository contribution rules, and only the relevant source/test files.
3. Review the exact diff at the pinned head. Check behavior, security, data handling, error handling, and relevant evidence for the declared scope.
4. Report actionable findings with stable IDs, severity, affected path/line, observed behavior, impact, and a concrete correction.
5. Distinguish PR readiness from product or Issue acceptance. A passing CI check does not prove untested behavior.
6. Re-review changes against the previously reviewed SHA and update findings only when new evidence supports it.

## Protected content and permissions

- Select inputs narrowly; do not recursively scan the whole repository.
- Exclude `docs/diagrams/` before traversal. Never read or list its contents, inspect links into it, or modify it.
- Do not inspect `.agents/outputs/` unless explicitly requested.
- Draft findings locally by default. Submitting a GitHub review/comment, changing an Issue, or merging requires separate explicit authorization for that action. This skill grants no remote permissions.

## Result

Report the reviewed SHA/base, evidence and checks examined, findings with stable IDs, and any unverified gates. If no findings are supported, say so without implying complete runtime or acceptance coverage.
