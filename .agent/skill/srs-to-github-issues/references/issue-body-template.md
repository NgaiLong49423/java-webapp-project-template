# Issue Body Template

Use this template for requirement-derived GitHub Issue drafts.

Issue bodies should be Vietnamese by default unless the user asks for another language.

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
Chỉ ghi nếu tài liệu nguồn có nêu rõ.

Nếu tài liệu nguồn không nêu rõ, ghi:
`Không có ghi chú triển khai cụ thể trong tài liệu nguồn.`

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

## Required Rules

- Title must be professional English.
- Body should be Vietnamese by default.
- Source Trace is mandatory.
- Acceptance Criteria must be testable.
- Implementation Notes must not invent technology.
- Labels must come from `.github/labels.yml` when present.
- Relationships must always be present even if values are `None`.
- Suggested branch must be English kebab-case.
