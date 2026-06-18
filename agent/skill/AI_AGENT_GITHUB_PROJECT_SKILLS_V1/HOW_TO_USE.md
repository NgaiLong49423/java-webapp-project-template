# How To Use - Hướng dẫn dùng bộ AI Agent Skills

Tài liệu này hướng dẫn cách dùng bộ skill theo từng mức độ, từ đơn giản đến chuyên nghiệp.

---

## Mức 1: Chỉ muốn tạo Issue từ SRS

Dùng các file:

```text
00_AI_AGENT_ORCHESTRATOR.md
01_extract_requirements_from_srs.md
02_refine_functional_requirements.md
03_generate_epics_and_user_stories.md
04_decompose_tasks_by_layer.md
12_generate_github_issues.md
```

Prompt mẫu:

```text
Bạn là AI Technical Project Manager.
Hãy đọc SRS này và chạy pipeline mức 1:
1. Extract FR
2. Refine FR
3. Generate Epics and User Stories
4. Decompose tasks by layer
5. Generate GitHub Issues

Yêu cầu output bằng Markdown, có mã Issue ID, label, priority, layer và acceptance criteria.
```

---

## Mức 2: Muốn GitHub Project chuyên nghiệp

Dùng thêm:

```text
05_calculate_priority_and_story_points.md
09_generate_labels.md
10_generate_milestones.md
11_generate_github_project_fields.md
13_sync_to_github_cli.md
```

Prompt mẫu:

```text
Hãy chạy pipeline mức 2 cho dự án này.
Tạo đầy đủ:
- Epics
- User Stories
- Tasks
- Labels
- Milestones
- Project Fields
- Story Points
- GitHub Issues
- GitHub CLI commands
```

---

## Mức 3: Muốn chia việc cho nhóm

Dùng thêm:

```text
06_assign_team_workload.md
```

Thông tin cần đưa cho Agent:

```text
Team members:
- Long: Backend, Database
- Member A: Frontend
- Member B: Testing, Documentation
- Member C: UI, Integration

Workload rule:
- Chia việc công bằng.
- Không giao task quá khó cho người không đúng skill.
- Mỗi người phải có contribution rõ ràng.
```

---

## Mức 4: Muốn phân tích kỹ thuật từng FR

Dùng thêm:

```text
07_fr_to_technical_spec.md
08_generate_project_structure.md
14_generate_acceptance_criteria_and_test_cases.md
```

Agent sẽ sinh thêm:

- Database schema đề xuất.
- API contract.
- Frontend screen specification.
- Backend exception handling.
- Test cases.
- Project folder structure.

---

## Gợi ý cho đồ án Car Wash

Với đồ án Automated Car Wash Management System, nên chạy theo mức 2 hoặc mức 3.

Không nên bắt Agent code ngay. Nên để Agent tạo GitHub Project, Issues, Milestones, Labels trước để nhóm làm việc có trật tự.

---

## Checklist trước khi chạy Agent

- [ ] Đã có SRS mới nhất.
- [ ] Đã có danh sách thành viên nhóm.
- [ ] Đã biết tech stack: Java Servlet, JSP, SQL Server, HTML/CSS/JS, v.v.
- [ ] Đã có repo GitHub.
- [ ] Đã thống nhất milestone hoặc số sprint.
- [ ] Đã biết phạm vi đồ án cần demo.
- [ ] Đã phân biệt rõ task học thuật và task code thực tế.

---

## Checklist sau khi Agent sinh output

- [ ] Mỗi Issue chỉ nên có một mục tiêu rõ ràng.
- [ ] Issue có label đúng layer.
- [ ] Issue có acceptance criteria.
- [ ] Issue có priority.
- [ ] Issue có story point.
- [ ] Issue có milestone.
- [ ] Issue không quá lớn.
- [ ] Không có task bị trùng.
- [ ] Không có chức năng nằm ngoài SRS.
