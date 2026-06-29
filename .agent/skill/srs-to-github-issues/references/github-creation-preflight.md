# GitHub Creation and Project Sync Preflight

Use this checklist before any real GitHub action.

## Before Creating Real GitHub Issues

- [ ] User explicitly requested real issue creation.
- [ ] `ISSUE_INDEX.md` exists.
- [ ] Selected draft files are listed in `ISSUE_INDEX.md`.
- [ ] Every selected draft file exists.
- [ ] No unreferenced draft files remain in the final draft directory.
- [ ] No local `file:///` paths exist in drafts or index.
- [ ] Selected drafts are `Approved`, or the user explicitly selected `Draft` / `Needs Review` items.
- [ ] Labels are valid.
- [ ] Missing labels are defined in `.github/labels.yml` before creation.
- [ ] Issue bodies include Source Trace.
- [ ] Issue titles are professional English.
- [ ] Full issue bodies will not be printed in chat unless requested.

If any check fails, stop and report the failure.

## Before Syncing GitHub Project Metadata

- [ ] User explicitly requested Project sync.
- [ ] Project owner is known.
- [ ] Project number or Project ID is known.
- [ ] Field IDs are known.
- [ ] Option IDs are known for single-select fields.
- [ ] Issue item IDs are known.
- [ ] No field is guessed.
- [ ] Relationship sync is best-effort only.
- [ ] Relationship target issue IDs can be resolved if relationship sync is attempted.

Do not sync if IDs cannot be determined confidently.

## Allowed Actions

Allowed only after explicit approval:

- `gh issue create`
- Create missing labels that are defined in `.github/labels.yml`
- Update `ISSUE_INDEX.md` after successful creation
- Sync verified GitHub Project fields

## Forbidden Actions

Never do these as part of this skill unless separately and explicitly requested:

- Close issues
- Delete issues
- Delete labels
- Delete branches
- Force-push
- Modify source code
- Create branches
- Merge pull requests
