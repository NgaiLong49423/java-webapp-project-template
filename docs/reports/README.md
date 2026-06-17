# Reports - Báo Cáo Dự Án

## Mục Đích

Thư mục `reports/` (Báo cáo) là nơi lưu trữ toàn bộ các biên bản họp nhóm, nhật ký làm việc cá nhân, báo cáo tiến độ định kỳ và tài liệu báo cáo tổng kết môn học. Việc này giúp:
* Lưu lại lịch sử phát triển và đóng góp của từng thành viên trong nhóm.
* Giúp giảng viên hoặc người hướng dẫn theo dõi sát sao tiến trình thực hiện dự án.
* Chuẩn bị sẵn tài liệu hoàn chỉnh để phục vụ cho việc chấm điểm và nghiệm thu dự án.

## Các Loại Báo Cáo Có Thể Lưu

Bạn có thể lưu các loại file sau trong thư mục này:
* **Báo cáo tiến độ:** Ghi nhận kết quả làm việc theo tuần hoặc theo sprint.
* **Báo cáo phân tích yêu cầu:** Tài liệu tóm tắt sau khi khảo sát nghiệp vụ.
* **Báo cáo thiết kế hệ thống:** Tóm tắt kiến trúc và quyết định công nghệ.
* **Báo cáo kiểm thử:** Nhật ký phát hiện lỗi và kết quả xác minh lỗi.
* **Báo cáo tổng kết:** Báo cáo hoàn thiện cuối cùng của môn học.
* **Biên bản họp nhóm:** Ghi chú nội dung phân công công việc sau mỗi buổi họp.

## Quy Tắc Đặt Tên File

Đặt tên các file báo cáo thống nhất theo cú pháp sau để dễ tìm kiếm và quản lý:
```text
report-[noi-dung-viet-tat-khong-dau]-[yyyy-mm-dd].md
```

Ví dụ cụ thể:
* `report-progress-2026-06-15.md` (Báo cáo tiến độ ngày 15/06/2026)
* `report-final-2026-06-20.md` (Báo cáo tổng kết cuối kỳ ngày 20/06/2026)
* `meeting-note-2026-06-15.md` (Biên bản họp nhóm ngày 15/06/2026)

---

## Mẫu Báo Cáo Ngắn

Dưới đây là cấu trúc mẫu cho một file báo cáo tiến độ ngắn hoặc biên bản làm việc:

### # [Tên Báo Cáo, ví dụ: Báo Cáo Tiến Độ Tuần 1]

#### 1. Thông Tin Chung
* **Dự án:** [Tên Dự Án]
* **Ngày thực hiện:** [yyyy-mm-dd]
* **Người thực hiện:** [Họ và tên thành viên thực hiện báo cáo]

#### 2. Nội Dung Đã Làm
* [x] Đã hoàn thành cấu trúc thư mục dự án.
* [x] Đã thiết kế xong sơ đồ ERD phiên bản v1.0.0.
* [ ] Đang phát triển giao diện đăng nhập (JSP).

#### 3. Vấn Đề Gặp Phải
* Gặp lỗi khi cấu hình kết nối database thông qua Tomcat DataSource. (Đã tự sửa bằng cách chuyển sang cấu hình trong file properties).
* Khó khăn khi thống nhất luồng đặt lịch hẹn giữa các thành viên. (Đã họp và chốt phương án).

#### 4. Việc Cần Làm Tiếp Theo
* Phát triển logic xử lý đăng nhập phía Servlet.
* Viết script chèn dữ liệu mẫu cho database.
* Vẽ sơ đồ hoạt động (Activity Diagram) cho chức năng đặt lịch.
