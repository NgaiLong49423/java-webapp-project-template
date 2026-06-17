# Software Requirements Specification - [Tên Dự Án]

## 1. Introduction

### 1.1 Purpose
Tài liệu SRS (Software Requirements Specification - đặc tả yêu cầu phần mềm) này nhằm mục đích mô tả chi tiết tất cả các yêu cầu chức năng, phi chức năng, môi trường vận hành cũng như thiết kế giao diện của hệ thống [Tên dự án].
Tài liệu này được sử dụng làm cơ sở thống nhất thông tin giữa các thành viên trong nhóm phát triển, giảng viên hướng dẫn và các bên liên quan trong suốt quá trình xây dựng dự án.

### 1.2 Scope
Tài liệu đặc tả cho hệ thống [Tên dự án], một ứng dụng web monolith được triển khai trên nền tảng Java Servlet/JSP và cơ sở dữ liệu quan hệ. Hệ thống sẽ giúp tự động hóa quy trình nghiệp vụ [mô tả ngắn nghiệp vụ, ví dụ: đặt lịch hẹn, mua bán hàng...] và cải thiện hiệu suất vận hành của người dùng.

### 1.3 Definitions
Dưới đây là một số thuật ngữ viết tắt được sử dụng trong tài liệu:

| Thuật ngữ | Giải thích |
|---|---|
| SRS | Software Requirements Specification - Tài liệu đặc tả yêu cầu phần mềm. |
| FR | Functional Requirement - Yêu cầu chức năng (hệ thống làm được gì). |
| NFR | Non-Functional Requirement - Yêu cầu phi chức năng (hệ thống hoạt động chất lượng thế nào). |
| UI/UX | User Interface / User Experience - Giao diện người dùng / Trải nghiệm người dùng. |
| DB | Database - Cơ sở dữ liệu của ứng dụng. |

## 2. Overall Description

### 2.1 Product Perspective
Hệ thống [Tên dự án] hoạt động độc lập theo kiến trúc monolith (kiến trúc một khối hợp nhất mã nguồn và giao diện), sử dụng Tomcat làm web server kết nối với máy chủ cơ sở dữ liệu.

### 2.2 User Classes
Các nhóm đối tượng người dùng chính sử dụng hệ thống bao gồm:
* **Guest (Khách vãng lai):** Truy cập tự do, xem thông tin và thực hiện tìm kiếm dịch vụ cơ bản.
* **User (Thành viên):** Khách hàng đã đăng ký tài khoản, có quyền thực hiện giao dịch cốt lõi (ví dụ: đặt phòng, đặt đơn...).
* **Admin (Quản trị viên):** Có toàn quyền điều hành hệ thống, cấu hình tham số cơ sở dữ liệu và quản lý các tài khoản khác.

### 2.3 Operating Environment
Môi trường vận hành dự kiến cho ứng dụng:
- Operating System: [Windows 10/11 / Linux (Ubuntu/CentOS)]
- Programming Language: [Java SDK 8]
- Server: [Apache Tomcat 9.0]
- Database: [MySQL 8.0 / SQL Server 2019 / ...]
- Web Browser: [Google Chrome, Microsoft Edge, Firefox...]

## 3. System Features

Dưới đây là đặc tả chi tiết cho từng chức năng chính của hệ thống:

### FR-01: [Tên chức năng, ví dụ: Đăng nhập hệ thống]

**Mô tả:**  
[Mô tả chức năng này làm gì, ví dụ: Cho phép khách hàng hoặc quản trị viên đăng nhập vào tài khoản của mình bằng email và mật khẩu đã đăng ký để sử dụng các chức năng cá nhân hóa].

**Người dùng liên quan:**  
[Guest / User / Admin / ...]

**Luồng xử lý chính (Main Flow):**  
1. Người dùng truy cập trang đăng nhập và điền email cùng mật khẩu vào form.
2. Người dùng nhấn nút "Đăng nhập".
3. Servlet tiếp nhận thông tin, mã hóa kiểm tra so khớp mật khẩu trong database thông qua DAO.
4. Nếu thông tin khớp, hệ thống lưu thông tin người dùng vào session và redirect (chuyển hướng) người dùng sang trang chủ tương ứng với vai trò của họ.

**Điều kiện hoàn thành (Acceptance Criteria):**  
- [ ] Cho phép đăng nhập thành công nếu nhập đúng tài khoản.
- [ ] Hiển thị thông báo lỗi rõ ràng ở giao diện nếu nhập sai email hoặc mật khẩu.
- [ ] Chặn truy cập trái phép bằng cách sử dụng filter kiểm tra session đối với các URL bắt buộc đăng nhập.

## 4. External Interface Requirements

`External Interface` là giao diện hoặc điểm kết nối giữa hệ thống với người dùng hoặc phần mềm bên ngoài.

### User Interface
* Giao diện web được thiết kế thân thiện, responsive hiển thị tốt trên cả màn hình máy tính và thiết bị di động.
* Sử dụng JSP làm trang giao diện chính nhúng mã HTML/CSS và Javascript.

### Software Interface
* Kết nối với JDK 8 và chạy trên nền web server Apache Tomcat 9.
* Sử dụng thư viện JDBC Driver tương ứng để kết nối Java với cơ sở dữ liệu.

### Database Interface
* Hệ thống kết nối và thực hiện các câu truy vấn SQL thông qua JDBC kết nối với Database Server.

## 5. Non-Functional Requirements

Yêu cầu chất lượng kỹ thuật của hệ thống:

| Mã NFR | Loại yêu cầu | Mô tả chi tiết | Tiêu chí kiểm tra |
|---|---|---|---|
| NFR-01 | Security (Bảo mật) | Bảo mật thông tin đăng nhập và phiên làm việc. | Sử dụng HTTPS cho phiên kết nối và mã hóa mật khẩu khi lưu trữ vào database. |
| NFR-02 | Reliability (Độ ổn định) | Hệ thống hoạt động liên tục, không bị lỗi tắt server đột ngột. | Đảm bảo bắt lỗi (try-catch) kỹ lưỡng trong code Java để không làm crash (sập) Tomcat. |

## 6. Database Requirements
* Cơ sở dữ liệu thiết kế theo chuẩn quan hệ thực thể, được mô tả chi tiết tại sơ đồ ERD đặt ở thư mục: [docs/diagrams/ERD/](file:///d:/Github-Projects/java-webapp-project-template/docs/diagrams/ERD/).
* Các câu lệnh SQL khởi tạo cấu trúc bảng được định nghĩa trong file: [database/schema.sql](file:///d:/Github-Projects/java-webapp-project-template/database/schema.sql).

## 7. Appendix
Phần phụ lục ghi các chú thích bổ sung hoặc thuật ngữ chuyên ngành khi làm dự án thực tế.
*(Người dùng có thể bổ sung các ghi chú riêng tại đây).*
