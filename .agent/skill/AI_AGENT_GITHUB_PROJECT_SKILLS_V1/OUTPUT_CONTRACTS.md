# Output Contracts

Output Contract nghĩa là hợp đồng đầu ra: Agent phải sinh dữ liệu theo cấu trúc cố định để các bước sau đọc lại được.

---

## Functional Requirement Contract

```yaml
fr_id: FR-001
title: Manage Booking
source_reference: SRS section 3.2
statement: The system shall allow customers to create and manage car wash bookings.
actor_roles:
  - Customer
  - Staff
business_value: Reduce waiting time and organize service schedule.
priority_hint: high
status: refined
assumptions:
  - Booking slot capacity is controlled by business rules.
```

---

## Epic Contract

```yaml
epic_id: EPIC-001
title: Booking Management
related_frs:
  - FR-001
business_goal: Allow customers and staff to manage car wash appointments.
user_roles:
  - Customer
  - Staff
success_metrics:
  - Customer can create booking successfully.
  - Staff can view booking queue.
```

---

## User Story Contract

```yaml
story_id: US-001
epic_id: EPIC-001
role: Customer
story: As a Customer, I want to book a car wash appointment, so that I can avoid waiting in line.
related_fr: FR-001
acceptance_criteria:
  - AC-001
  - AC-002
priority: high
story_points: 5
```

---

## Task Contract

```yaml
task_id: TASK-BE-001
story_id: US-001
layer: Backend
title: Create booking creation API
objective: Implement endpoint for customer booking creation.
dependencies:
  - TASK-DB-001
labels:
  - backend
  - feature
  - priority:high
milestone: Sprint 1 - Core Booking Flow
story_points: 5
assignee: Long
acceptance_criteria:
  - AC-001
```

---

## GitHub Issue Contract

```yaml
issue_title: "[BE][Booking] Create booking creation API"
issue_type: task
layer: Backend
priority: high
milestone: Sprint 1 - Core Booking Flow
labels:
  - backend
  - feature
  - priority:high
  - story:booking
body_sections:
  - Context
  - Objective
  - Scope
  - Technical Notes
  - Acceptance Criteria
  - Dependencies
  - Definition of Done
```

---

## Label Contract

```yaml
name: backend
color: "5319E7"
description: Work related to server-side logic, APIs, services, or controllers.
category: layer
```

---

## Milestone Contract

```yaml
name: Sprint 1 - Core System Setup
description: Build the foundation required for the main demo flow.
due_date: optional
success_criteria:
  - Authentication flow completed.
  - Database core tables completed.
  - Base layout completed.
```

---

## Project Field Contract

```yaml
field_name: Layer
field_type: single_select
options:
  - Database
  - Backend
  - Frontend
  - Testing
  - Documentation
  - Integration
  - DevOps
```
