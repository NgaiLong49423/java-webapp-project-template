# Use Case Diagram - Sơ Đồ Ca Sử Dụng

## Mục Đích

`Use Case Diagram` (Sơ đồ ca sử dụng) là sơ đồ mô tả mối quan hệ tương tác giữa những đối tượng bên ngoài (Actor) và các chức năng (Use Case) bên trong hệ thống. Sơ đồ này giúp:
* Xác định rõ những ai sẽ sử dụng hệ thống và họ có quyền làm gì.
* Khái quát hóa toàn bộ các chức năng mà hệ thống cung cấp dưới dạng các ca sử dụng.
* Định hình rõ phạm vi ranh giới của dự án (System Boundary).
* Làm cơ sở để viết bảng yêu cầu chức năng (FR) trong đặc tả yêu cầu dự án.

## Thành Phần Cơ Bản

* **Actor (Tác nhân):** Là người dùng hoặc hệ thống bên ngoài tương tác trực tiếp với ứng dụng (ví dụ: User, Admin, Staff).
* **Use Case (Ca sử dụng):** Một chức năng cụ thể mà actor có thể thực hiện trên hệ thống để đạt được một mục tiêu nào đó (ví dụ: Đăng nhập, Đặt lịch).
* **System Boundary (Ranh giới hệ thống):** Khung giới hạn hiển thị phạm vi của ứng dụng, các use case sẽ nằm bên trong và các actor nằm bên ngoài ranh giới này.
* **Include (Quan hệ bao gồm):** Thể hiện một use case bắt buộc phải chạy qua một use case khác (ví dụ: Đặt lịch hẹn thì *bao gồm* việc xác thực tài khoản).
* **Extend (Quan hệ mở rộng):** Thể hiện một use case phụ chỉ xảy ra dưới một điều kiện cụ thể (ví dụ: Đặt lịch hẹn thành công thì có thể chọn *mở rộng* thêm là Gửi email thông báo).

## Quy Tắc Đặt Tên File

Các file sơ đồ Use Case nên được đặt tên phân loại theo module hoặc vai trò người dùng:
```text
usecase-[ten-module-viet-lien-khong-dau].drawio
usecase-[ten-module-viet-lien-khong-dau].png
```

Ví dụ cụ thể:
* `usecase-auth.drawio` (sơ đồ Use Case phân quyền & đăng nhập)
* `usecase-booking.png` (sơ đồ Use Case chức năng đặt lịch)

---

## Mẫu Mô Tả Use Case

Dưới đây là mẫu tài liệu hóa chi tiết cho từng ca sử dụng:

### ## UC-01: [Tên Use Case, ví dụ: Đặt lịch hẹn dịch vụ]

| Mục | Nội dung |
|---|---|
| **Actor** | [Vai trò người dùng, ví dụ: User (Khách hàng)] |
| **Mục tiêu** | [Mục tiêu của use case, ví dụ: Đặt thành công lịch hẹn sử dụng dịch vụ] |
| **Tiền điều kiện** | [Điều kiện trước khi bắt đầu, ví dụ: Người dùng đã đăng nhập tài khoản thành công] |
| **Hậu điều kiện** | [Kết quả sau khi hoàn thành, ví dụ: Thông tin đặt lịch được lưu vào database và trạng thái là PENDING] |

**Luồng xử lý chính (Main Flow):**  
1. Người dùng chọn dịch vụ, ngày và giờ mong muốn trên giao diện.
2. Người dùng nhấn nút "Xác nhận đặt lịch".
3. Hệ thống kiểm tra tính hợp lệ và lưu thông tin đặt lịch vào database.
4. Hệ thống hiển thị thông báo đặt lịch thành công.

**Luồng thay thế (Alternative Flow):**  
1. Nếu ngày/giờ người dùng chọn đã có người khác đặt trước đó, hệ thống sẽ báo lỗi và yêu cầu chọn lại.
2. Nếu phiên làm việc hết hạn, hệ thống chuyển hướng người dùng đến trang đăng nhập.
