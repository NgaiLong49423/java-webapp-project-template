# 08 - Generate Project Structure

## Purpose

Generate a clean, professional folder structure based on the project type, tech stack and functional modules.

Folder structure nghĩa là cây thư mục của dự án. Nó giúp code dễ tìm, dễ sửa, dễ mở rộng.

---

## When To Use

Use this skill after the Agent knows:

- Project type.
- Tech stack.
- Main modules.
- Database entities.
- Frontend style.

---

## Inputs

```yaml
project_name: string
tech_stack:
  backend: Java Servlet | Spring Boot | Node.js | other
  frontend: JSP | HTML/CSS/JS | React | other
  database: SQL Server | MySQL | PostgreSQL | other
modules:
  - Booking
  - Payment
  - Membership
```

---

## System Prompt

You are a Senior Software Architect. Generate a clean, maintainable and student-friendly project folder structure.

The structure must be realistic for the provided tech stack and must not be over-engineered.

Over-engineered nghĩa là làm quá phức tạp so với nhu cầu thật.

---

## Rules

1. Do not create too many folders without purpose.
2. Separate source code, database scripts, documentation and assets.
3. For Java Servlet projects, use MVC-style organization.
4. For school projects, keep structure understandable.
5. Include a short explanation for important folders.
6. Do not list every single image or generated file.
7. Keep the displayed tree clean.

---

## Java Servlet + JSP Recommended Structure

```text
AutoWash/
├── README.md
├── docs/
│   ├── SRS.md
│   ├── ERD.md
│   ├── USE_CASE.md
│   └── PROJECT_PLAN.md
│
├── database/
│   ├── schema.sql
│   ├── seed.sql
│   └── queries/
│
├── src/
│   └── main/
│       ├── java/
│       │   └── com/autowash/
│       │       ├── controller/
│       │       ├── service/
│       │       ├── dao/
│       │       ├── model/
│       │       ├── dto/
│       │       ├── filter/
│       │       └── util/
│       │
│       └── webapp/
│           ├── assets/
│           │   ├── css/
│           │   ├── js/
│           │   └── images/
│           ├── views/
│           │   ├── auth/
│           │   ├── customer/
│           │   ├── staff/
│           │   └── admin/
│           └── WEB-INF/
│               └── web.xml
│
├── tests/
└── .github/
    ├── ISSUE_TEMPLATE/
    └── workflows/
```

---

## Output Format

```markdown
# Recommended Project Structure

## Folder Tree

```text
...
```

## Folder Explanation

| Folder | Purpose |
|---|---|

## Naming Convention

## Notes For Team
```

---

## Quality Gate

Before returning the final output, verify:

- Every item has a stable ID.
- Output is traceable to source requirement.
- No vague wording remains.
- Assumptions are clearly marked.
- The output can be used by the next pipeline step.
