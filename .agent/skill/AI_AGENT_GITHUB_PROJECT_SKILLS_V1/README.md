# AI Agent GitHub Project Skills Kit v1

Bộ tài liệu này dùng để cấu hình một AI Agent có khả năng biến tài liệu dự án như SRS, ERD, SQL Script, Use Case Diagram thành hệ thống quản lý việc chuyên nghiệp trên GitHub.

Mục tiêu chính:

- Đọc và hiểu tài liệu yêu cầu phần mềm.
- Tách Functional Requirement thành Epic, User Story và Task.
- Phân layer công việc: Database, Backend, Frontend, Integration, Testing, Documentation.
- Tạo nhãn, milestone, sprint, story point, priority và custom fields cho GitHub Project.
- Sinh nội dung GitHub Issue theo chuẩn kỹ thuật, dễ chia việc cho nhóm.
- Sinh lệnh GitHub CLI để tạo Issue, Label, Milestone và đưa vào Project Board.

---

## Cấu trúc bộ skill

```text
AI_AGENT_GITHUB_PROJECT_SKILLS_V1/
├── README.md
├── HOW_TO_USE.md
├── 00_AI_AGENT_ORCHESTRATOR.md
├── OUTPUT_CONTRACTS.md
├── GLOSSARY.md
│
├── skills/
│   ├── project_management/
│   │   ├── 01_extract_requirements_from_srs.md
│   │   ├── 02_refine_functional_requirements.md
│   │   ├── 03_generate_epics_and_user_stories.md
│   │   ├── 04_decompose_tasks_by_layer.md
│   │   ├── 05_calculate_priority_and_story_points.md
│   │   └── 06_assign_team_workload.md
│   │
│   ├── architecture/
│   │   ├── 07_fr_to_technical_spec.md
│   │   └── 08_generate_project_structure.md
│   │
│   ├── github_management/
│   │   ├── 09_generate_labels.md
│   │   ├── 10_generate_milestones.md
│   │   ├── 11_generate_github_project_fields.md
│   │   ├── 12_generate_github_issues.md
│   │   └── 13_sync_to_github_cli.md
│   │
│   └── quality_assurance/
│       └── 14_generate_acceptance_criteria_and_test_cases.md
│
├── templates/
│   ├── EPIC_TEMPLATE.md
│   ├── GITHUB_ISSUE_TEMPLATE.md
│   ├── LABELS_TEMPLATE.md
│   ├── MILESTONE_TEMPLATE.md
│   └── PROJECT_FIELDS_TEMPLATE.md
│
└── examples/
    └── CAR_WASH_SAMPLE_WORKFLOW.md
```

---

## Triết lý thiết kế

Không nên để một file Agent làm mọi thứ. Agent càng ôm nhiều nhiệm vụ thì càng dễ sinh output lung tung. Vì vậy bộ này tách từng skill thành từng file nhỏ, mỗi skill có:

- Purpose: mục đích.
- When to use: khi nào dùng.
- Inputs: đầu vào.
- Outputs: đầu ra.
- System prompt: chỉ thị chính cho Agent.
- Rules: luật bắt buộc.
- Quality gate: tiêu chí kiểm tra chất lượng.
- Example: ví dụ mẫu.

---

## Pipeline đề xuất

```text
SRS / ERD / SQL / Use Case
        ↓
01_extract_requirements_from_srs
        ↓
02_refine_functional_requirements
        ↓
03_generate_epics_and_user_stories
        ↓
07_fr_to_technical_spec
        ↓
04_decompose_tasks_by_layer
        ↓
05_calculate_priority_and_story_points
        ↓
09_generate_labels
        ↓
10_generate_milestones
        ↓
11_generate_github_project_fields
        ↓
06_assign_team_workload
        ↓
12_generate_github_issues
        ↓
13_sync_to_github_cli
```

---

## Phạm vi hiện tại

Bộ này tập trung vào quản lý dự án GitHub, chưa bắt Agent tự code toàn bộ dự án.

Lý do: giai đoạn đầu nên để Agent làm tốt vai trò Technical Project Manager trước. Khi task, spec, database, API và UI rõ ràng rồi mới thêm skill code generation ở phiên bản sau.

---

## Cách dùng nhanh

1. Đưa cho Agent file `00_AI_AGENT_ORCHESTRATOR.md`.
2. Đưa thêm các skill liên quan trong thư mục `skills/`.
3. Đưa tài liệu dự án: SRS, ERD, SQL Script, Use Case Diagram.
4. Yêu cầu Agent chạy pipeline theo `HOW_TO_USE.md`.
5. Kiểm tra output bằng `OUTPUT_CONTRACTS.md`.
6. Dùng file `13_sync_to_github_cli.md` để sinh lệnh GitHub CLI.

---

## Kết quả mong đợi

Sau khi chạy đúng pipeline, Agent có thể sinh ra:

- Danh sách FR chuẩn.
- Epic và User Story.
- Task theo từng layer.
- Acceptance Criteria.
- Test cases.
- Labels.
- Milestones.
- GitHub Project custom fields.
- Story points.
- Workload assignment.
- GitHub Issues chuyên nghiệp.
- CLI commands để tạo dữ liệu trên GitHub.
