---
name: changelog-automation
description: "Standardize changelog updates, git tag versioning, release notes, and commit conventions. Prefer a lightweight CHANGELOG.md + git tag workflow for small documentation or student projects; only introduce automation when explicitly needed."
risk: medium
source: customized
version: v1.0.0
created_date: 2026-06-29
last_updated_date: 2026-06-29
---

# Changelog Automation

Use this skill to help maintain a clear project history through `CHANGELOG.md`, git tags, version rules, and commit conventions.

This skill supports both:
- **Minimal workflow**: manual `CHANGELOG.md` updates + git tags.
- **Automated workflow**: tools such as `standard-version`, `semantic-release`, GitHub Actions, `git-cliff`, or `commitizen`.

For small projects, documentation repositories, school projects, or repositories without a formal release process, prefer the **minimal workflow** by default.

---

## Use this skill when

- Updating or standardizing `CHANGELOG.md`.
- Deciding whether a change should be recorded in the changelog.
- Suggesting the next version tag.
- Preparing release notes from recent commits, pull requests, or issue summaries.
- Defining or applying commit message conventions.
- Managing semantic versioning.
- Creating a lightweight release workflow using `CHANGELOG.md` and `git tag`.
- Reviewing whether changelog content is safe, clear, and complete.

---

## Do not use this skill when

- The project has no versioning, no changelog, and no need to track notable changes.
- The user only needs a quick one-time summary that should not be stored in `CHANGELOG.md`.
- Commit history is unavailable, unreliable, or too vague to infer meaningful changes.
- The user asks for unrelated project documentation such as SRS, README, wiring guides, test plans, or implementation plans without mentioning changelog, release notes, versioning, tags, or commit conventions.
- The user is asking for deployment automation, CI/CD setup, or package publishing without needing changelog or version management.

---

## Core principles

### 1. Prefer minimal workflow for small projects

For projects that only use `CHANGELOG.md` and git tags, do not introduce external release tools by default.

Recommended minimal flow:

```text
Make changes
→ Commit changes with a clear message
→ Update CHANGELOG.md manually
→ Review changelog for accuracy and safety
→ Create a git tag only when the user explicitly asks
```

Use this workflow unless the user explicitly asks for automation or the repository already has a formal release process.

---

### 2. Use Keep a Changelog structure

Use a clear changelog structure inspired by Keep a Changelog.

Recommended sections:

```markdown
# Changelog

All notable changes to this project will be documented in this file.

## [Unreleased]

### Added
- New features, documents, modules, or major sections.

### Changed
- Meaningful changes to existing behavior, structure, or documentation.

### Fixed
- Corrections, resolved contradictions, bugs, or wrong descriptions.

### Removed
- Removed features, documents, modules, or obsolete content.

### Security
- Security-related changes that are safe to disclose.
```

Use only the sections that are needed. Do not create empty sections unless the project convention requires them.

---

### 3. Treat `CHANGELOG.md` as the source of release history

For lightweight projects, `CHANGELOG.md` is the main human-readable history.

A git tag marks a stable point in repository history, but the changelog explains what changed.

Before suggesting a tag, check that:
- The changelog has an entry for the intended version.
- The entry is understandable to humans.
- The entry does not expose secrets or internal-only details.
- The version bump matches the actual change scope.

---

### 4. Do not create or push tags without explicit permission

Never create, push, delete, overwrite, or move git tags unless the user explicitly asks.

Allowed by default:
- Suggest the next version tag.
- Explain why a version should be patch, minor, or major.
- Provide commands the user can run manually.
- Prepare changelog text.

Not allowed unless explicitly requested:
- `git tag ...`
- `git push origin ...`
- `git tag -d ...`
- `git push origin --delete ...`
- Any action that changes remote release history.

---

## Version policy

Use Semantic Versioning when the project does not define a different rule.

Format:

```text
MAJOR.MINOR.PATCH
```

Meaning:

- **MAJOR**: breaking change or large structural change.
- **MINOR**: new feature, new document, new major section, or meaningful capability added.
- **PATCH**: bug fix, correction, clarification, small documentation update, metadata update, or minor cleanup.

Examples:

```text
v1.0.2 → v1.0.3  patch update
v1.0.2 → v1.1.0  minor update
v1.0.2 → v2.0.0  major update
```

---

## Draft version policy

If the project uses `v0.x.x` as draft versions:

- `v0.x.x` means the document or project state is still draft, unstable, or under review.
- Do not treat `v0.x.x` as a stable release.
- Avoid aggressive edits to `v0.x.x` documents unless the user explicitly asks.
- Prefer reporting issues, suggesting improvements, or preparing proposed changes.
- Use `v1.0.0` or higher only when the user confirms the document or project is stable enough.

---

## Commit convention

Use clear commit messages. Conventional Commits are recommended but not mandatory for minimal projects.

Recommended format:

```text
<type>(<scope>): <short description>
```

Common types:

| Type | Use for | Changelog mapping |
|---|---|---|
| `feat` | New feature or capability | Added |
| `fix` | Bug fix or contradiction fix | Fixed |
| `docs` | Documentation changes | Added / Changed / Fixed depending on meaning |
| `chore` | Maintenance, metadata, version updates | Changed or usually excluded |
| `refactor` | Restructure without changing meaning | Changed |
| `ci` | CI/CD workflow changes | Changed or usually excluded |
| `test` | Test changes | Usually excluded unless notable |
| `build` | Build system changes | Usually excluded unless notable |

Examples:

```bash
git commit -m "docs(srs): update intrusion detection scenario"
git commit -m "fix(wiring): correct RC522 pin description"
git commit -m "chore(changelog): record v1.0.2 changes"
git commit -m "docs(readme): update project setup guide"
```

Do not rely only on vague commits such as:

```bash
git commit -m "update"
git commit -m "fix"
git commit -m "done"
```

If the commit history is vague, ask for or infer from file diffs, PR descriptions, issue summaries, or user-provided context.

---

## Changelog entry rules

Record changes that are notable to the project, team, instructor, reviewer, or future maintainer.

Good changelog entries:

```markdown
### Changed
- Updated the hardware wiring guide to describe connections by device instead of by ESP32-CAM pin.

### Fixed
- Corrected the RC522 module pin description to avoid wiring ambiguity.
```

Weak changelog entries:

```markdown
### Changed
- Updated file.
- Fixed stuff.
- Changed something.
```

Prefer human-readable descriptions over raw commit messages.

---

## Safety rules

Never expose secrets, credentials, internal-only values, or private contact details in release notes or changelog entries.

Do not include:

- API keys.
- Tokens.
- Passwords.
- Private URLs.
- Private email addresses unless explicitly intended for public documentation.
- Internal-only deployment details.
- Sensitive security exploit details that increase risk.

Bad:

```markdown
### Fixed
- Fixed Telegram bot token 123456:ABCDEF...
```

Good:

```markdown
### Fixed
- Improved Telegram alert configuration handling.
```

For security changes, describe the impact safely.

---

## Minimal workflow commands

Use these as suggestions only. Do not execute tag-changing commands unless explicitly requested.

Check changes:

```bash
git status
git diff
git log --oneline
```

Commit changelog update:

```bash
git add CHANGELOG.md
git commit -m "chore(changelog): update release notes"
```

Create a local tag:

```bash
git tag v1.0.2
```

Push a tag:

```bash
git push origin v1.0.2
```

List tags:

```bash
git tag --list
```

Show current version history:

```bash
git log --oneline --decorate
```

---

## Automation guidance

Do not introduce automation tools by default.

Only recommend tools such as `standard-version`, `semantic-release`, GitHub Actions, `git-cliff`, or `commitizen` when:

- The user explicitly asks for changelog automation.
- The repository already has CI/CD.
- The project has a real release process.
- The team needs repeated release-note generation.
- Manual changelog maintenance is becoming error-prone.

When automation is appropriate, choose the simplest tool that matches the project:

| Situation | Suggested approach |
|---|---|
| Small documentation repo | Manual `CHANGELOG.md` + git tags |
| Java or mixed repo with no package release | Manual changelog or `git-cliff` |
| Node.js package | `standard-version` or `semantic-release` |
| Python package | `commitizen` |
| Mature GitHub project | GitHub Actions + release notes |
| Team with strict commit rules | `commitlint` + PR review |

---

## Agent behavior

When asked to update or review changelog/versioning:

1. Identify the project workflow: minimal or automated.
2. Inspect the available context: changed files, commits, PRs, issues, or user notes.
3. Decide whether the change is notable.
4. Classify the change under `Added`, `Changed`, `Fixed`, `Removed`, or `Security`.
5. Suggest the version bump if needed.
6. Do not create or push tags unless explicitly asked.
7. Check for secrets or internal-only details.
8. Keep entries concise and understandable.
9. Explain uncertain assumptions instead of inventing release history.

---

## Recommended prompt for small projects

Use this prompt when asking an agent to update a lightweight changelog:

```text
Dựa trên các thay đổi gần đây trong repo, hãy cập nhật CHANGELOG.md theo format Keep a Changelog. 
Chỉ ghi các thay đổi đáng chú ý. 
Không ghi secret, token, private URL, mật khẩu, email riêng tư hoặc chi tiết nội bộ nhạy cảm. 
Dự án này chỉ dùng CHANGELOG.md và git tag, nên không tự thêm semantic-release, standard-version, GitHub Actions hoặc automation tool khác. 
Nếu phù hợp, hãy đề xuất version tag tiếp theo theo Semantic Versioning, nhưng không tự tạo hoặc push tag nếu chưa được yêu cầu.
```

---

## Resources

- `resources/implementation-playbook.md` for detailed patterns, templates, and examples.
- Use the resource file only when the user needs detailed automation setup, tool configuration, release workflow examples, or implementation templates.

---

## Limitations

- This skill does not replace manual review.
- Generated changelog entries may be incomplete if commit history is vague.
- Version suggestions are recommendations, not final decisions.
- Environment-specific validation is still required before release.
- If required inputs, permissions, safety boundaries, or success criteria are missing, ask for clarification or make the safest minimal recommendation.
