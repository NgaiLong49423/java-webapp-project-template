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
- Use relative links only. Do not use local `file:///` links.

## Commit Rules
- Follow Conventional Commits from `CONTRIBUTING.md`.
- AI commits must include a `Co-Authored-By` line when applicable.