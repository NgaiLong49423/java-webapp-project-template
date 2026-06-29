# Minimal AGENTS.md Example

Use this reference when the repository is missing `AGENTS.md`.

Keep the real `AGENTS.md` short. It should guide agents to the right sources, not duplicate full docs.

```markdown
# Agent Instructions

## Canonical Docs

- Requirements: `docs/requirements/SRS.md`
- Product requirements: `docs/requirements/PRD.md`
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
- Do not treat `v0.x.x` documents as stable unless the user confirms.
- Update `CHANGELOG.md` after major docs, database, feature, or structure changes.
- Use relative links only.

## Commit Rules

- Follow `CONTRIBUTING.md`.
- AI commits must include a `Co-Authored-By` line when applicable.
```
