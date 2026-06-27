---
name: srs-to-github-issues-vn
description: Bản tiếng Việt để người dùng đọc lại và hiểu skill srs-to-github-issues. Không dùng bản này làm skill chính cho agent nếu muốn tiết kiệm token.
risk: documentation
source: self
source_type: custom
---

# SRS to GitHub Issues — Bản tiếng Việt

## Mục đích

Skill này dùng để chuyển tài liệu yêu cầu như PRD, SRS, spec, requirement document hoặc planning document thành GitHub Issues chuyên nghiệp.

Skill này là reusable skill, nghĩa là dùng lại được cho nhiều project, không bị khóa vào một app cụ thể.

Mặc định skill chỉ tạo bản nháp issue, không tạo issue thật trên GitHub, không cập nhật GitHub Project, không tạo branch, không sửa code.

## Khi nào dùng skill này

Dùng khi muốn agent:

- Đọc PRD/SRS/spec rồi phân rã thành GitHub Issue.
- Tạo issue draft chuyên nghiệp.
- Gắn Source Trace, Acceptance Criteria, Size, Story Points, Priority, Labels, Relationships.
- Tạo GitHub Issue thật từ draft đã duyệt.
- Đồng bộ metadata vào GitHub Project.
- Ước lượng size và story points cho issue.

## Nguyên tắc chính

### 1. Tài liệu nguồn là sự thật

Agent phải đọc tài liệu nguồn trước khi tạo issue.

Nếu có cả PRD và SRS:

- PRD dùng để hiểu tổng quan sản phẩm.
- SRS dùng để kiểm tra chi tiết nghiệp vụ.
- Nếu PRD và SRS mâu thuẫn thì ưu tiên SRS, trừ khi người dùng nói khác.

### 2. Không bịa

Agent không được tự thêm:

- Chức năng mới.
- Actor mới.
- Luồng nghiệp vụ mới.
- Công nghệ mới.
- Label mới.
- Ngày bắt đầu/kết thúc.
- GitHub Project field chưa kiểm chứng.

Nếu thiếu thông tin thì ghi `TBD`, `Unknown`, hoặc hỏi lại người dùng.

### 3. Bắt buộc có Source Trace

Source Trace nghĩa là dấu vết nguồn, cho biết issue này được lấy từ phần nào trong tài liệu.

Mỗi issue phải trace được về ít nhất một nguồn như:

- FR
- NFR
- UC
- Business Rule
- Product Goal
- Requirement section
- Spec heading

Nếu không trace được thì không tạo thành requirement issue.

### 4. Draft trước

Mặc định agent chỉ tạo draft issue.

Chỉ tạo issue thật khi người dùng nói rõ như:

- “tạo issue thật”
- “create GitHub issues”
- “tạo issue 001 đến 005”
- “tạo toàn bộ draft”

Chỉ sync GitHub Project khi người dùng nói rõ như:

- “cập nhật vào GitHub Project”
- “sync project metadata”
- “set project fields”

## Các mode hoạt động

### 1. Draft mode — mặc định

Agent tạo file Markdown issue draft trong:

```text
.agent/report/github-issue-drafts/
```

Cấu trúc:

```text
.agent/report/github-issue-drafts/ISSUE_INDEX.md
.agent/report/github-issue-drafts/001-module-short-title.md
.agent/report/github-issue-drafts/002-module-short-title.md
```

Trong mode này agent không được:

- Tạo GitHub Issue thật.
- Cập nhật GitHub Project.
- Tạo label trên GitHub.
- Tạo branch.
- Commit code.

### 2. GitHub creation mode

Chỉ dùng khi người dùng yêu cầu rõ.

Mặc định agent chỉ tạo issue có `Status = Approved` trong `ISSUE_INDEX.md`.

Nếu người dùng chỉ định phạm vi, ví dụ “tạo issue 001 đến 005”, agent chỉ tạo đúng phạm vi đó.

Sau khi tạo xong, agent cập nhật `ISSUE_INDEX.md` với:

- GitHub issue number.
- Issue URL.
- Status = Created.
- Created date nếu có.

### 3. GitHub Project sync mode

Chỉ dùng khi người dùng yêu cầu rõ.

Agent được sync trực tiếp nhưng phải inspect GitHub Project trước.

Agent phải xác định chắc chắn:

- Repository owner.
- Repository name.
- Project owner.
- Project number hoặc Project ID.
- Field name.
- Field ID.
- Option ID.
- Project item ID.

Nếu thiếu thông tin thì dừng lại và hỏi người dùng.

Các field có thể sync:

- Type
- Size
- Story Points
- Priority
- Start date
- Target date
- Relationships

Relationships gồm:

- Parent
- Blocked by
- Blocking
- Security alert

Security alert chỉ dùng cho issue bảo mật thật.

## Cách phân rã issue

Skill dùng kiểu hybrid decomposition, nghĩa là phân rã kết hợp.

Cách làm:

- Nhóm issue theo module, domain, feature area hoặc workflow.
- Mỗi issue vẫn phải trace về FR/NFR/UC/Business Rule hoặc section trong tài liệu.
- Requirement quá lớn thì tách nhỏ.
- Requirement quá nhỏ có thể gom nếu cùng một luồng.
- Không chia theo layer code như model/service/controller nếu tài liệu không yêu cầu.

Nên ưu tiên vertical slice, nghĩa là mỗi issue tạo ra một lát cắt chức năng có thể kiểm thử được.

## Epic và Relationships

Epic nghĩa là issue cha dùng để gom nhiều issue con.

Chỉ đề xuất Epic khi:

- Một module có từ 3 issue con trở lên.
- Requirement có Size = XL.
- Story Points >= 13.
- Công việc quá lớn để code trực tiếp.

Nếu issue có Size = XL hoặc Story Points >= 13:

- Nếu là Epic thì được giữ.
- Nếu là implementation issue thì phải tách nhỏ.

## Size và Story Points

Size và Story Points được đánh giá riêng.

### Size

Size đo phạm vi công việc.

```text
XS = rất nhỏ
S  = nhỏ
M  = vừa
L  = lớn
XL = quá lớn, thường nên tách hoặc làm Epic
```

### Story Points

Story Points đo nỗ lực, độ khó và rủi ro, không phải số giờ.

```text
1  = rất dễ
2  = dễ
3  = trung bình
5  = khó
8  = rất khó
13 = quá lớn hoặc rủi ro cao, nên tách
```

Mỗi issue phải có lý do ước lượng.

## Priority

Agent được tự đề xuất Priority nhưng phải ghi lý do.

Priority nên dựa trên:

- Issue có chặn issue khác không.
- Có thuộc core workflow không.
- Rủi ro nếu làm muộn.
- Có cần trước khi test hoặc integration không.

Nếu `.github/labels.yml` có label priority thì phải dùng đúng label trong file đó.

## Start date và Target date

Mặc định:

```text
Start Date: TBD
Target Date: TBD
```

Agent không được tự đoán ngày.

Chỉ điền ngày khi người dùng đưa lịch rõ ràng.

## Labels

Agent phải đọc:

```text
.github/labels.yml
```

Quy tắc:

- Không tự bịa label.
- Chỉ dùng label có trong `labels.yml`.
- Mỗi issue phải có ít nhất một label type chính.
- Nếu tạo issue thật và label chưa tồn tại trên GitHub nhưng có trong `labels.yml`, agent được tạo label đó.
- Không tạo label ngoài `labels.yml` nếu chưa được phép.

## Issue templates

Agent phải đọc:

```text
.github/ISSUE_TEMPLATE/*.yml
```

Rồi chọn template phù hợp:

- Bug -> bug template.
- Feature/FR -> feature hoặc functional requirement template.
- NFR -> non-functional requirement template.
- Task/docs/setup -> task template.

Nếu template thiếu field cần thiết thì agent bổ sung vào issue body.

## Quy tắc đặt title

Issue title phải viết bằng tiếng Anh chuyên nghiệp.

Format gợi ý:

```text
[Module][Source Trace] Verb-Based Professional Title
```

Ví dụ:

```text
[Booking][FR-05/FR-06] Implement Booking Creation With Window Validation
[Queue][FR-10/FR-11] Activate Service Period And Prevent Duplicate Activation
[Loyalty][FR-19] Recalculate Customer Loyalty From Completed Records
```

Không đặt title mơ hồ như:

```text
Update logic
Fix feature
Handle data
```

## Suggested Branch

Agent không được tự tạo branch.

Chỉ được ghi branch gợi ý trong issue body.

Format:

```text
<prefix>/<short-kebab-case-title>
```

Ví dụ:

```text
feature/booking-window-validation
backend/loyalty-recalculation
fix/duplicate-period-activation
```

Kebab-case nghĩa là viết thường và nối từ bằng dấu gạch ngang.

## Implementation Notes

Implementation Notes nghĩa là ghi chú triển khai.

Chỉ được ghi nếu tài liệu nguồn có nói rõ.

Ví dụ:

- Tài liệu ghi dùng file text -> được ghi dùng file text.
- Tài liệu không ghi Redis -> không được thêm Redis.
- Tài liệu không ghi database -> không được thêm database.
- Tài liệu không ghi Kafka -> không được thêm Kafka.

Nếu muốn đề xuất kỹ thuật ngoài tài liệu, agent phải đưa vào mục `Suggestion` và hỏi người dùng trước.

## Template issue body

Issue body mặc định viết tiếng Việt.

```md
# <Professional English Issue Title>

## Tóm tắt
Mô tả ngắn gọn issue này cần làm gì.

## Source Trace
- PRD: ...
- SRS/Spec: ...
- FR/NFR/UC/Business Rule: ...

## Mục tiêu
Mô tả kết quả mong muốn sau khi issue hoàn thành.

## Phạm vi
- ...

## Không nằm trong phạm vi
- ...

## Quy tắc nghiệp vụ / Yêu cầu liên quan
- ...

## Implementation Notes
Chỉ ghi nếu tài liệu nguồn có nêu rõ. Nếu không có, ghi: `Không có ghi chú triển khai cụ thể trong tài liệu nguồn.`

## Acceptance Criteria
- [ ] ...
- [ ] ...
- [ ] ...

## Project Metadata
- Type: ...
- Size: ...
- Story Points: ...
- Estimation Reason: ...
- Priority: ...
- Priority Reason: ...
- Start Date: TBD
- Target Date: TBD

## Labels
- ...

## Relationships
- Parent: None
- Blocked by: None
- Blocking: None
- Security alert: None

## Suggested Branch
`feature/example-branch-name`

## Ghi chú cho người thực hiện
- ...
```

## ISSUE_INDEX.md

File index phải chia theo module và có bảng tổng hợp.

Status có thể là:

```text
Draft
Needs Review
Approved
Created
Synced
```

Mặc định là `Draft`.

## Checklist trước khi tạo issue thật

Trước khi tạo GitHub Issue thật:

- Người dùng đã yêu cầu rõ.
- Draft tồn tại.
- `ISSUE_INDEX.md` tồn tại.
- Issue được chọn là Approved, hoặc người dùng chỉ định rõ issue khác.
- Labels hợp lệ.
- Missing labels có trong `.github/labels.yml`.
- Issue body có Source Trace.
- Issue title viết tiếng Anh chuyên nghiệp.

## Checklist trước khi sync GitHub Project

Trước khi sync Project:

- Người dùng đã yêu cầu rõ.
- Biết Project owner và Project number.
- Biết field ID.
- Biết option ID.
- Biết issue item ID.
- Không đoán field.

## Sau khi tạo draft

Agent cần báo:

- Thư mục output.
- Số lượng issue draft.
- Số Epic đề xuất.
- Issue nào cần review.
- Đường dẫn `ISSUE_INDEX.md`.
- Nhắc lại rằng chưa tạo GitHub Issue thật nếu người dùng chưa yêu cầu.

## Sau khi tạo GitHub Issue thật

Agent cần báo:

- Số issue đã tạo.
- Issue number và URL.
- Labels đã gắn.
- Labels nào được tạo từ `.github/labels.yml`.
- `ISSUE_INDEX.md` đã cập nhật chưa.
- GitHub Project đã sync chưa.

## Sau khi sync Project

Agent cần báo:

- Tên/số Project.
- Issue đã sync.
- Field đã cập nhật.
- Issue bị bỏ qua và lý do.
- `ISSUE_INDEX.md` đã đổi sang `Synced` chưa.
