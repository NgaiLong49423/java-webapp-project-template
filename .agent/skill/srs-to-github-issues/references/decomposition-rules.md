# Decomposition Rules

## Default Strategy

Prefer one GitHub Issue per Functional Requirement.

Every issue must have source trace.

## Split One Requirement When

Split a requirement when:

- It is too large for one implementation issue.
- It has multiple independent workflows.
- It has important dependencies.
- It has high uncertainty/risk.
- It has separate testable behavior slices.
- It is estimated as `XL` or `13` story points.

## Group Requirements When

Group multiple requirements only when:

- They are small.
- They are strongly coupled.
- They are implemented in the same workflow.
- Splitting would create artificial work items.
- The source document already describes them as one behavior.

Do not group many FRs into one issue only for convenience.

## Vertical Slice Rule

Prefer vertical slices.

A good issue should represent meaningful, testable behavior.

Avoid splitting only by code layer unless the source document or workflow requires it.

Bad split:

```text
Create DAO
Create Service
Create Servlet
Create JSP
```

Better split:

```text
Implement Booking Creation With Window Validation
```

## Epic Rules

Create or propose an Epic when:

- A module has 3 or more child issues.
- A requirement is `XL`.
- Story Points are `13` or higher.
- The work is too broad for direct implementation.

Do not create real Epic issues unless the user approves.
