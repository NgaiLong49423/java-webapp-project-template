> **Document:** GitHub Template Maintenance Guide\
> **File:** `docs/template-maintenance.md`\
> **Version:** v1.0.0\
> **Created:** 2026-10-09\
> **Last Updated:** 2026-10-09\
> **Status:** Template\

# Bảo Trì GitHub Template Này

Tài liệu này dành cho người duy trì repository template. Dự án tạo từ template nên xóa hướng dẫn này và hoàn thiện README riêng.

## Khi Tạo Dự Án Mới

Sử dụng `.agents/skills/project-initialization/SKILL.md` và phân loại nội dung repository như sau:

- **KEEP:** `.agents/POLICY.md`, skills, workflow, hướng dẫn đóng góp, mẫu GitHub, labels, license và khung `app/`, `database/`, `docs/` có thể tái sử dụng.
- **INITIALIZE:** `README.md`, tài liệu yêu cầu, metadata repository trong `.agents/repo-contract.yml`, ví dụ cơ sở dữ liệu và hướng dẫn cài đặt, build, kiểm thử riêng của dự án.
- **CLEAN:** hướng dẫn bảo trì này và nội dung chỉ phục vụ việc duy trì template gốc. Xem xét từng mục và giữ lại nội dung hữu ích cho dự án mới.

Không kiểm tra, sửa hoặc dọn `.agents/outputs/` local. Không truy cập vùng tài liệu được bảo vệ hoặc kiểm tra liên kết trỏ vào đó.

## Bảo Trì Repository Template

- Giữ định dạng phù hợp riêng cho tài liệu, YAML frontmatter của skill, metadata workflow, contract repository và cấu hình Actions.
- Giữ kiểm tra trung lập với framework và DBMS. Không tự đặt Required Status Checks khi thêm workflow.
- Repository được tạo từ template trở thành dự án độc lập. Không tạo cơ chế tự đồng bộ ngược về repository template nguồn.
- Xem lại quy trình branch trong `CONTRIBUTING.md`; giữ `main` là nhánh ổn định và `develop` là nhánh tích hợp trừ khi chủ repository duyệt chính sách khác.
