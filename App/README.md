# App

## Mục Đích Thư Mục `App/`

Thư mục `App/` là nơi chứa phần mã nguồn chính của ứng dụng.

`Source code` là mã nguồn do lập trình viên viết để xây dựng chức năng của hệ thống.

Trong template này, thư mục `App/` được để đơn giản để không ép dự án phải theo một kiến trúc cố định. Khi tạo repository mới từ template, người phát triển có thể tự tổ chức thư mục bên trong `App/` theo công nghệ, môn học hoặc design pattern phù hợp.

`Design Pattern` là mẫu thiết kế code giúp giải quyết một vấn đề lập trình thường gặp theo cách có cấu trúc và dễ bảo trì hơn.

## Khi Nào Cần Thêm Nội Dung Vào `App/`

Bạn nên thêm source code vào thư mục này khi bắt đầu phát triển dự án thật.

Ví dụ:

```text
App/
├── src/
├── web/
├── config/
└── tests/
```

Hoặc nếu dự án dùng Java Servlet/JSP:

```text
App/
├── src/
├── webapp/
└── WEB-INF/
```

Hoặc nếu dự án dùng cấu trúc tự thiết kế:

```text
App/
├── controller/
├── service/
├── model/
├── repository/
└── util/
```

## Gợi Ý Tổ Chức Code

Có thể tổ chức code theo một số hướng sau:

### 1. Theo tầng xử lý

```text
controller/
service/
repository/
model/
util/
```

* `controller`: nơi nhận request từ người dùng hoặc trình duyệt.
* `service`: nơi xử lý logic nghiệp vụ.
* `repository`: nơi làm việc với dữ liệu hoặc database.
* `model`: nơi chứa class mô tả dữ liệu chính.
* `util`: nơi chứa các hàm hoặc class tiện ích.

`Request` là yêu cầu gửi từ client lên server.
`Logic nghiệp vụ` là quy tắc xử lý thật của hệ thống, ví dụ kiểm tra quyền, tính tiền, xác nhận trạng thái.

### 2. Theo chức năng

```text
auth/
booking/
payment/
user/
admin/
```

Cách này phù hợp khi dự án có nhiều module chức năng.

`Module` là một phần chức năng tương đối độc lập trong hệ thống.

### 3. Theo yêu cầu môn học

Nếu môn học yêu cầu cấu trúc riêng, hãy tổ chức `App/` theo đúng yêu cầu của giảng viên.

## Quy Tắc Khi Thêm Code

* Không hardcode dữ liệu quan trọng nếu dữ liệu đó nên lấy từ database hoặc file cấu hình.
* Đặt tên file, class và thư mục rõ ràng.
* Không để file build, file tạm hoặc file IDE không cần thiết trong repo.
* Nếu thêm chức năng lớn, hãy cập nhật tài liệu trong `docs/`.
* Nếu thay đổi database, hãy cập nhật thư mục `database/`.
* Nếu thay đổi quan trọng, hãy cập nhật `CHANGELOG.md`.

`Hardcode` là viết cố định dữ liệu trong code thay vì lấy từ database, file cấu hình hoặc input phù hợp.
`Build` là quá trình biên dịch hoặc đóng gói dự án để chạy.

## Ghi Chú

Thư mục `App/` trong template này chỉ là điểm bắt đầu.
Khi tạo repository mới từ template, hãy chỉnh lại cấu trúc bên trong `App/` cho phù hợp với dự án thực tế.
