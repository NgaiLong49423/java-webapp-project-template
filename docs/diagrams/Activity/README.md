# Activity Diagram - Sơ Đồ Hoạt Động

## Mục Đích

`Activity Diagram` (Sơ đồ hoạt động) mô tả trực quan luồng xử lý và các bước thực hiện của một chức năng nghiệp vụ cụ thể từ lúc bắt đầu cho tới khi kết thúc. Sơ đồ này giúp:
* Làm rõ quy trình hoạt động của các chức năng phức tạp trong hệ thống.
* Giúp các thành viên phát triển hiểu đúng logic nghiệp vụ để viết code chính xác.
* Tránh tình trạng hardcode (viết cố định giá trị trong code thay vì lấy từ dữ liệu/tham số đầu vào) dẫn đến luồng xử lý sai thực tế.

## Khi Nào Cần Vẽ

Bạn nên thiết kế sơ đồ hoạt động cho các chức năng có nhiều bước xử lý hoặc có rẽ nhánh logic phức tạp. Ví dụ:
* Đăng nhập / Đăng ký hệ thống.
* Đặt lịch hẹn (Booking) hoặc Tạo đơn hàng mới.
* Thanh toán (Checkout) trực tuyến.
* Quản lý dữ liệu lớn (CRUD) có ràng buộc vai trò phức tạp.

## Quy Tắc Đặt Tên File

Mã nguồn sơ đồ và hình ảnh xuất ra của Activity Diagram nên được đặt tên thống nhất và lưu trữ trong thư mục này theo định dạng:
```text
activity-[ten-chuc-nang-viet-lien-khong-dau].drawio
activity-[ten-chuc-nang-viet-lien-khong-dau].png
```

Ví dụ cụ thể:
* `activity-login.drawio` (file sơ đồ gốc vẽ trên Draw.io)
* `activity-create-booking.png` (ảnh xuất ra từ sơ đồ để nhúng vào tài liệu)

---

## Mẫu Mô Tả Sơ Đồ

Dưới đây là mẫu ghi chú kèm theo cho mỗi sơ đồ hoạt động được đưa vào tài liệu:

### ## [Tên Activity Diagram, ví dụ: Luồng Đăng Nhập Hệ Thống]

**Chức năng liên quan:**  
[Mã chức năng, ví dụ: FR-01 - Đăng nhập]

**Vai trò người dùng (Actor):**  
[Guest / User / Admin / ...]

**Luồng xử lý chính (Main Flow):**  
1. Người dùng nhập thông tin đăng nhập và gửi request (yêu cầu) đi.
2. Servlet kiểm tra dữ liệu đầu vào thông qua DAO kết nối database.
3. Servlet xác thực đúng thông tin và chuyển hướng (redirect) người dùng về trang Dashboard.

**Luồng thay thế (Alternative Flow):**  
1. Nếu mật khẩu nhập sai, Servlet chuyển hướng quay lại trang đăng nhập kèm theo thông báo lỗi.
2. Nếu tài khoản bị khóa, hệ thống hiển thị thông báo lỗi trạng thái tài khoản.

**Ghi chú:**  
*(Ghi thêm các lưu ý kỹ thuật hoặc quy tắc đặc biệt nếu có).*
