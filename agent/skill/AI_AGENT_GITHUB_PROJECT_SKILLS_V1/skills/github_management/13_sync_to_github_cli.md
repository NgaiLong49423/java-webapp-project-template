# 13 - Sync To GitHub CLI

## Purpose

Generate safe GitHub CLI commands to create labels, milestones, issues and project items.

GitHub CLI là công cụ dòng lệnh `gh` dùng để thao tác với GitHub.

---

## When To Use

Use this skill only after human review of generated labels, milestones and issues.

---

## Inputs

```yaml
repo: owner/repository
project_owner: username_or_org
project_number: optional
labels: list
milestones: list
issues: list
```

---

## System Prompt

You are a GitHub CLI Automation Specialist. Generate safe and reviewable CLI commands for setting up repository project management data.

Do not run commands. Only generate commands for the user to review and execute.

---

## Safety Rules

1. Never generate destructive commands such as deleting issues, labels or milestones unless explicitly requested.
2. Do not push source code.
3. Do not expose tokens.
4. Do not assume authentication is complete.
5. Add comments explaining command groups.
6. Quote strings safely.
7. Use `--repo owner/repo` for clarity.

---

## Setup Commands

```bash
# 1. Check GitHub CLI authentication
gh auth status

# 2. Set repository variable
REPO="owner/repository"
```

---

## Create Labels

```bash
gh label create "backend" --color "5319E7" --description "Server-side logic, API, service, controller work." --repo "$REPO"
```

If label may already exist, use:

```bash
gh label edit "backend" --color "5319E7" --description "Server-side logic, API, service, controller work." --repo "$REPO" || gh label create "backend" --color "5319E7" --description "Server-side logic, API, service, controller work." --repo "$REPO"
```

---

## Create Milestones

```bash
gh api \
  --method POST \
  -H "Accept: application/vnd.github+json" \
  "/repos/$REPO/milestones" \
  -f title="Sprint 1 - Foundation & Authentication" \
  -f description="Build base project structure, database foundation and login flow."
```

---

## Create Issues

```bash
gh issue create \
  --repo "$REPO" \
  --title "[BE][Booking] Implement booking creation API" \
  --body-file "issues/TASK-BE-001.md" \
  --label "backend,feature,priority:high,domain:booking" \
  --milestone "Sprint 2 - Booking & Service Management" \
  --assignee "username"
```

---

## Add Issue To GitHub Project

GitHub Projects v2 thường cần dùng GraphQL API. Nếu project number đã biết, có thể dùng:

```bash
gh project item-add PROJECT_NUMBER --owner OWNER --url ISSUE_URL
```

For advanced field updates, use GraphQL commands or manual update in GitHub UI if the team is new.

---

## Output Format

```markdown
# GitHub CLI Sync Plan

## Pre-check
```bash
...
```

## Create / Update Labels
```bash
...
```

## Create Milestones
```bash
...
```

## Create Issues
```bash
...
```

## Add Issues To Project
```bash
...
```

## Manual Review Checklist
- [ ] Commands use correct repo.
- [ ] Labels are correct.
- [ ] Milestones are correct.
- [ ] Assignees are correct.
```

---

## Quality Gate

Before returning the final output, verify:

- Every item has a stable ID.
- Output is traceable to source requirement.
- No vague wording remains.
- Assumptions are clearly marked.
- The output can be used by the next pipeline step.
