# Car Wash Sample Workflow

This example shows how the skill kit can be applied to an Automated Car Wash Management System.

---

## Input Example

```text
FR-001: The system shall allow customers to create a car wash booking.
Tech Stack: Java Servlet, JSP, SQL Server, HTML/CSS/JS
Team: 4 members
```

---

## Refined FR

```text
FR-001: The system shall allow authenticated customers to create a car wash booking by selecting a vehicle, service package, date, and available time slot.
```

---

## Epic

```text
EPIC-001 - Booking Management
```

---

## User Story

```text
US-001: As a Customer, I want to create a car wash booking, so that I can reserve a washing time slot before arriving at the station.
```

---

## Layer-Based Tasks

### Database

```text
TASK-DB-001: Create Booking table and relationships
```

### Backend

```text
TASK-BE-001: Implement booking creation validation and service logic
TASK-BE-002: Create booking controller endpoint
```

### Frontend

```text
TASK-FE-001: Build booking form UI
TASK-FE-002: Display available time slots
```

### Testing

```text
TASK-QA-001: Test booking creation happy path and invalid slot cases
```

---

## Labels

```text
feature
backend
frontend
database
testing
priority:high
domain:booking
```

---

## Milestone

```text
Sprint 2 - Booking & Service Management
```

---

## Project Fields

```yaml
Status: Ready
Priority: High
Layer: Backend
Story Point: 5
Sprint: Sprint 2
Module: Booking
```

---

## Generated GitHub Issue Example

```markdown
# [BE][Booking] Implement booking creation validation and service logic

## Traceability

- FR: FR-001
- Epic: EPIC-001 Booking Management
- User Story: US-001
- Task ID: TASK-BE-001

## Context

Customers need to create car wash bookings by selecting service, vehicle, date and available time slot.

## Objective

Implement backend service logic that validates booking data and creates a booking record.

## Scope

- [ ] Validate authenticated customer.
- [ ] Validate selected vehicle belongs to customer.
- [ ] Validate selected service package exists.
- [ ] Validate selected date and time slot are available.
- [ ] Create booking record with initial status.

## Out of Scope

- Payment processing.
- Staff assignment.
- Notification sending.

## Acceptance Criteria

- [ ] Given a logged-in customer and valid booking data, When the customer submits the booking, Then the system shall create a booking successfully.
- [ ] Given a selected time slot is full, When the customer submits the booking, Then the system shall reject the booking and show an error message.

## Dependencies

- TASK-DB-001

## Definition of Done

- [ ] Service logic implemented.
- [ ] Validation cases handled.
- [ ] Error response structure prepared.
- [ ] Manual test completed.
```

---

## GitHub CLI Example

```bash
REPO="owner/auto-wash"

gh issue create \
  --repo "$REPO" \
  --title "[BE][Booking] Implement booking creation validation and service logic" \
  --body-file "issues/TASK-BE-001.md" \
  --label "backend,feature,priority:high,domain:booking" \
  --milestone "Sprint 2 - Booking & Service Management"
```
