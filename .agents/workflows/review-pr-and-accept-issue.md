---
name: review-pr-and-accept-issue
description: Coordinate a scoped pull request review and, when requested, a separate acceptance check against its requirements.
---

# Review PR and Accept Issue

## Use

Use this workflow when a user asks for a pull request review, a re-review after changes, or acceptance against a linked work item. Load `.agents/skills/pr-issue-review/SKILL.md` for review mechanics.

## Steps

1. Confirm repository, PR, base branch, exact head SHA, latest base SHA, and linked Issue or requirement source when applicable.
2. Read repository entry instructions and contribution rules. Select only the files needed for the stated scope. Do not recursively scan the repository.
3. Exclude `docs/diagrams/` before selecting or traversing any input; never enumerate its contents, inspect a link target into it, or write there. Exclude local `.agents/outputs/` unless the user explicitly asks to inspect it.
4. Review the exact PR diff and relevant evidence. Report stable findings with severity and affected code location. Identify checks as passed, failed, blocked, or not tested.
5. Treat PR readiness and acceptance of the linked requirement as separate conclusions. Do not infer runtime behavior from static checks or a green CI status.
6. For re-review, compare the new head to the prior reviewed SHA and revisit findings affected by the change.
7. Present the review result in the conversation. Keep review artifacts local only when requested; never commit them by default.
8. Submit a GitHub review/comment or change an Issue only after explicit authorization for the exact remote action and content. Never merge or alter repository settings under this workflow.

## Completion

Report the repository, base/head SHA, scope and evidence examined, findings, and unresolved checks. State when GitHub state or a required check could not be verified.
