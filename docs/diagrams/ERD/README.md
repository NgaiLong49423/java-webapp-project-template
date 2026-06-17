# ERD - Entity Relationship Diagram

## Mục Đích

`ERD` (Entity Relationship Diagram - sơ đồ quan hệ thực thể) là mô hình trực quan dùng để biểu diễn các thực thể thông tin trong hệ thống dưới dạng bảng cơ sở dữ liệu và mối quan hệ ràng buộc giữa chúng. ERD giúp:
* Thiết kế cấu trúc cơ sở dữ liệu (Database) một cách rõ ràng và khoa học.
* Xác định chính xác cách thức các bảng liên kết với nhau (quan hệ 1-1, 1-N, N-N).
* Hạn chế tối đa việc dư thừa dữ liệu hoặc bất thường khi truy vấn.
* Làm tài liệu hướng dẫn trực tiếp để lập trình viên viết file kịch bản tạo bảng [database/schema.sql](file:///d:/Github-Projects/java-webapp-project-template/database/schema.sql).

## Thành Phần Cơ Bản

* **Entity (Thực thể):** Đại diện cho một đối tượng dữ liệu trong đời thực (thường tương ứng với 1 bảng trong database, ví dụ: bảng `User`, `Booking`).
* **Attribute (Thuộc tính):** Các thông tin chi tiết cấu thành nên thực thể (tương ứng với các cột trong bảng, ví dụ: `username`, `created_at`).
* **Primary Key (viết tắt là `PK` - Khóa chính):** Là một hoặc nhiều thuộc tính dùng để định danh duy nhất cho mỗi dòng dữ liệu trong bảng.
* **Foreign Key (viết tắt là `FK` - Khóa ngoại):** Là một cột trong bảng này dùng để trỏ đến khóa chính của bảng khác để thiết lập mối quan hệ liên kết dữ liệu giữa hai bảng.

## Quy Tắc Đặt Tên File

Các file sơ đồ quan hệ thực thể nên được lưu với định dạng tên và phiên bản rõ ràng:
```text
erd-v[version].drawio
erd-v[version].png
```

Ví dụ cụ thể:
* `erd-v0.1.0.drawio` (file sơ đồ gốc vẽ bằng Draw.io)
* `erd-v1.0.0.png` (ảnh xuất ra của cơ sở dữ liệu hoàn chỉnh để chèn vào báo cáo)

---

## Mẫu Mô Tả Bảng

Hãy mô tả chi tiết các bảng được thiết kế theo cấu trúc mẫu dưới đây:

### ## [Tên bảng, ví dụ: Bảng `booking`]

Mô tả vai trò của bảng: Lưu thông tin chi tiết lịch hẹn của khách hàng.

| Tên cột | Kiểu dữ liệu | Ràng buộc | Mô tả chi tiết |
|---|---|---|---|
| id | INT | PK, AUTO_INCREMENT | Mã số tự tăng dùng định danh booking. |
| customer_id | INT | FK | Mã liên kết với bảng `user` (đại diện cho khách hàng đặt lịch). |
| booking_date | DATE | NOT NULL | Ngày đặt lịch hẹn của khách hàng. |
| status | VARCHAR(50) | NOT NULL | Trạng thái của lịch hẹn (PENDING, APPROVED...). |

## Liên Kết Với Database

> [!IMPORTANT]
> * Mỗi khi thay đổi cấu trúc bảng hoặc thêm bảng mới trên sơ đồ ERD, bạn **bắt buộc** phải cập nhật lại file kịch bản SQL tương ứng tại [database/schema.sql](file:///d:/Github-Projects/java-webapp-project-template/database/schema.sql).
> * Hãy ghi chú rõ các thay đổi trong phần mô tả bảng của file này để nhóm phát triển dễ dàng theo dõi.
