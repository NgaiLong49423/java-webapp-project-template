# Project Requirements - [Tên Dự Án]

## 1. Tổng Quan Dự Án

[Tên dự án] là một hệ thống [loại hệ thống, ví dụ: website quản lý đặt phòng, app đặt xe...] được xây dựng nhằm [mục tiêu chính của dự án, ví dụ: giúp tối ưu hóa luồng đặt chỗ, kết nối khách hàng...].
Dự án này phục vụ cho [đối tượng sử dụng chính] và được phát triển trong bối cảnh [môn học / đồ án / dự án cá nhân / dự án nhóm].

## 2. Vấn Đề Cần Giải Quyết

Mô tả các vấn đề thực tế hoặc hạn chế trong quy trình cũ cần được hệ thống này giải quyết:
* Quy trình hiện tại đang gặp khó khăn gì? (Ví dụ: ghi chép thủ công dễ sai sót, mất thời gian...)
* Tại sao quy trình cũ lại kém hiệu quả?
* Hệ thống mới sẽ mang lại cải tiến gì để khắc phục các nhược điểm đó?

## 3. Mục Tiêu Dự Án

* Mục tiêu 1 (Ví dụ: Số hóa 100% quy trình đặt lịch của cửa hàng).
* Mục tiêu 2 (Ví dụ: Giảm thiểu sai sót thông tin đặt hàng).
* Mục tiêu 3 (Ví dụ: Cung cấp hệ thống báo cáo doanh thu trực quan cho quản lý).

## 4. Đối Tượng Người Dùng

Dưới đây là danh sách những vai trò người dùng tương tác trực tiếp với hệ thống:

| Vai trò | Mô tả |
|---|---|
| Guest | Khách vãng lai, chưa đăng nhập vào hệ thống, chỉ có thể xem thông tin cơ bản. |
| User | Người dùng thông thường đã đăng nhập, có quyền sử dụng các dịch vụ cốt lõi của hệ thống. |
| Admin | Người quản trị hệ thống, có toàn quyền quản lý tài khoản, cấu hình và xem báo cáo. |
| [Vai trò khác] | [Mô tả vai trò khác nếu có, ví dụ: Staff - Nhân viên cửa hàng] |

## 5. Functional Requirements

`Functional Requirement` (viết tắt là `FR`) là yêu cầu chức năng. Yêu cầu này mô tả cụ thể những gì hệ thống phải làm được để đáp ứng nghiệp vụ người dùng.

| Mã FR | Tên yêu cầu | Mô tả chi tiết | Độ ưu tiên |
|---|---|---|---|
| FR-01 | [Tên chức năng, ví dụ: Đăng nhập] | [Mô tả chức năng, ví dụ: Người dùng đăng nhập bằng email và mật khẩu] | High / Medium / Low |
| FR-02 | [Tên chức năng] | [Mô tả chức năng] | High / Medium / Low |

## 6. Non-Functional Requirements

`Non-Functional Requirement` (viết tắt là `NFR`) là yêu cầu phi chức năng. Yêu cầu này không mô tả hệ thống làm chức năng gì, mà chỉ rõ hệ thống phải hoạt động thế nào về mặt kỹ thuật và chất lượng (như hiệu năng, bảo mật, tính tương thích, độ ổn định).

| Mã NFR | Loại yêu cầu | Mô tả chi tiết | Tiêu chí đo lường / Kiểm tra |
|---|---|---|---|
| NFR-01 | Security (Bảo mật) | Mã hóa mật khẩu người dùng trước khi lưu trữ. | Sử dụng thuật toán BCrypt trong code Java để mã hóa mật khẩu trong database. |
| NFR-02 | Performance (Hiệu năng) | Tốc độ phản hồi trang web phải nhanh. | Thời gian tải trang web không quá 2 giây khi kết nối mạng bình thường. |

## 7. Phạm Vi Dự Án

Xác định rõ những gì dự án sẽ làm và những gì nằm ngoài tầm kiểm soát của dự án.

### Trong Phạm Vi
* Phát triển các chức năng cốt lõi được liệt kê trong bảng Functional Requirements.
* Thiết kế và cấu hình cơ sở dữ liệu lưu trữ tương ứng.
* Triển khai giao diện web tương thích với các trình duyệt phổ biến.

### Ngoài Phạm Vi
* Không tích hợp thanh toán trực tuyến qua các ngân hàng quốc tế (chỉ hỗ trợ thanh toán khi nhận hàng/chuyển khoản thủ công).
* Không xây dựng ứng dụng di động native trên iOS/Android (chỉ làm web responsive hiển thị tốt trên điện thoại di động).

## 8. Giả Định Và Ràng Buộc

* **Giả định** (`Assumption`): Các giả thiết làm tiền đề khi thực hiện dự án.
  * Giả định người dùng đã có kết nối internet khi sử dụng ứng dụng web.
  * Giả định người dùng có kiến thức cơ bản để sử dụng trình duyệt web.
* **Ràng buộc** (`Constraint`): Các giới hạn hoặc quy định bắt buộc phải tuân theo.
  * Ràng buộc công nghệ: Phải sử dụng JDK 8, Java Servlet/JSP và cơ sở dữ liệu quan hệ theo yêu cầu môn học.
  * Ràng buộc thời gian: Dự án phải hoàn thành và nộp trước ngày hạn định của môn học.
