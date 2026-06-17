# Database

## Mục Đích Thư Mục `database/`

Thư mục `database/` dùng để lưu các file liên quan đến cơ sở dữ liệu của dự án.

`Database` là cơ sở dữ liệu, nơi lưu trữ dữ liệu của hệ thống như người dùng, đơn hàng, sản phẩm, lịch đặt, vai trò hoặc trạng thái xử lý.

Thư mục này giúp quản lý database rõ ràng hơn, tránh việc script SQL bị để rải rác hoặc thất lạc.

## Cấu Trúc File

```text
database/
├── schema.sql
├── sample-data.sql
├── queries.sql
└── README.md
```

## Ý Nghĩa Từng File

### `schema.sql`

File này dùng để tạo cấu trúc database.

Nội dung thường có:
* Tạo database.
* Tạo bảng.
* Tạo khóa chính.
* Tạo khóa ngoại.
* Tạo ràng buộc dữ liệu.

`Schema` là cấu trúc của database, bao gồm bảng, cột, kiểu dữ liệu và quan hệ giữa các bảng.
`Primary Key`, viết tắt là `PK`, là khóa chính dùng để định danh một dòng dữ liệu.
`Foreign Key`, viết tắt là `FK`, là khóa ngoại dùng để liên kết bảng này với bảng khác.

Ví dụ:
```sql
CREATE TABLE Users (
    user_id INT PRIMARY KEY,
    username VARCHAR(100) NOT NULL
);
```

### `sample-data.sql`

File này dùng để thêm dữ liệu mẫu cho dự án.

Dữ liệu mẫu giúp:
* Test chức năng nhanh hơn.
* Demo dự án dễ hơn.
* Đảm bảo người khác clone repo về có dữ liệu để chạy thử.

`Sample data` là dữ liệu mẫu dùng để kiểm tra hoặc trình bày hệ thống.

Ví dụ:
```sql
INSERT INTO Users (user_id, username)
VALUES (1, 'admin');
```

### `queries.sql`

File này dùng để lưu các câu truy vấn SQL mẫu hoặc câu truy vấn thường dùng.

`Query` là câu truy vấn dùng để lấy, thêm, sửa hoặc xóa dữ liệu trong database.

Ví dụ:
```sql
SELECT * FROM Users;
```

## Quy Tắc Làm Việc Với Database

* Mọi thay đổi cấu trúc bảng nên được cập nhật trong `schema.sql`.
* Dữ liệu mẫu nên được cập nhật trong `sample-data.sql`.
* Các truy vấn quan trọng hoặc truy vấn dùng để test nên được ghi trong `queries.sql`.
* Không lưu mật khẩu thật, token thật hoặc thông tin nhạy cảm trong file SQL.
* Nếu thay đổi database, hãy cập nhật ERD trong `docs/diagrams/ERD/`.
* Nếu thay đổi lớn, hãy cập nhật `CHANGELOG.md`.

`Token` là chuỗi dùng để xác thực hoặc cấp quyền truy cập.
`Thông tin nhạy cảm` là dữ liệu không nên công khai, ví dụ mật khẩu thật, key API, thông tin cá nhân.

## Thứ Tự Chạy File SQL Đề Xuất

Khi setup database cho dự án mới, có thể chạy theo thứ tự:

```text
1. schema.sql
2. sample-data.sql
3. queries.sql
```

Giải thích:
* Chạy `schema.sql` trước để tạo database và bảng.
* Chạy `sample-data.sql` sau để thêm dữ liệu mẫu.
* Dùng `queries.sql` để kiểm tra dữ liệu hoặc test truy vấn.

## Liên Kết Với Tài Liệu Khác

* ERD: `docs/diagrams/ERD/`
* Yêu cầu dự án: `docs/requirements/`
* Tài liệu tổng quan: `README.md`

`ERD` là Entity Relationship Diagram, nghĩa là sơ đồ quan hệ thực thể trong database.

## Ghi Chú

Thư mục `database/` trong template này chỉ chứa các file mẫu ban đầu.
Khi tạo repository mới từ template, hãy cập nhật lại tên database, tên bảng, kiểu dữ liệu và dữ liệu mẫu cho đúng với dự án thực tế.
