> **Document:** Database Starter Guide\
> **File:** `database/README.md`\
> **Version:** v1.0.0\
> **Created:** 2026-06-14\
> **Last Updated:** 2026-10-09\
> **Status:** Template\

# Hướng Dẫn Thư Mục Database

Thư mục này có thể chứa các script cơ sở dữ liệu được dự án lựa chọn. Các file SQL hiện tại chỉ là khung trống, không mặc định sản phẩm cơ sở dữ liệu hoặc cách quản lý migration.

## Các File Gợi Ý

- `schema.sql`: khung schema tùy chọn, cần điều chỉnh theo cú pháp của cơ sở dữ liệu đã chọn.
- `sample-data.sql`: dữ liệu mẫu tổng hợp nếu cần; không dùng dữ liệu cá nhân hoặc dữ liệu production.
- `queries.sql`: các truy vấn tùy chọn phục vụ phát triển hoặc xác minh.

Xóa hoặc thay thế file không phù hợp với quy trình cơ sở dữ liệu đã chọn. Nếu dự án sử dụng công cụ migration, hãy ghi rõ nguồn sự thật và vòng đời của nó tại đây; không duy trì nhiều lịch sử schema cạnh tranh nếu chưa có kế hoạch đồng bộ cụ thể.

Không đưa thông tin xác thực hoặc dữ liệu riêng tư có thật vào script. Cập nhật tài liệu dự án liên quan khi schema hoặc quy trình cơ sở dữ liệu thay đổi.
