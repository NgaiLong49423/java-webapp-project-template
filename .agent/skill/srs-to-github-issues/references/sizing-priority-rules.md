# Sizing, Story Points, Priority, and Date Rules

## Size

Size estimates scope.

| Size | Meaning |
|---|---|
| XS | Very small change, narrow scope, minimal rules |
| S | Small feature/task, few edge cases |
| M | Medium feature, validation, persistence, or several business rules |
| L | Large feature, multiple flows/modules/dependencies |
| XL | Too large for direct implementation; should usually become Epic or be split |

## Story Points

Story Points estimate effort, uncertainty, and risk. They are not hours.

| Points | Meaning |
|---:|---|
| 1 | Very easy |
| 2 | Easy |
| 3 | Medium |
| 5 | Hard |
| 8 | Very hard |
| 13 | Too large/high risk; split or turn into Epic unless approved |

Each issue must include a short estimation reason.

Example:

```text
Size: M
Story Points: 5
Estimation Reason: Medium scope, but higher effort because it affects validation, persistence, and business rule consistency.
```

## Priority

Priority must consider:

- Dependency order
- Core user workflow importance
- Risk if delayed
- Whether other issues are blocked by it
- Whether it is required before testing/integration

Allowed priority values should come from repository Project config or labels.

If `.github/labels.yml` exists, map priority only to labels defined there.

Do not invent priority labels.

## Dates

Default:

```text
Start Date: TBD
Target Date: TBD
```

Do not invent dates.

Only fill dates when the user provides a schedule.

Examples:

```text
start from 2026-06-27
split this into 7 days
foundation issues on day 1
target all booking issues by Friday
```
