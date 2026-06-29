# Changelog

`CHANGELOG.md` (nhật ký thay đổi) là file dùng để ghi lại lịch sử tất cả những thay đổi quan trọng của dự án qua từng mốc thời gian hoặc phiên bản.

* File này giúp người đọc (thành viên trong team, giảng viên hoặc người đóng góp) nhanh chóng nắm bắt dự án đã được thêm mới, chỉnh sửa, loại bỏ hoặc khắc phục những vấn đề gì mà không cần phải duyệt qua từng commit trong lịch sử Git.
* Không cần thiết phải ghi lại mọi thay đổi nhỏ nhặt (như sửa lỗi chính tả hay định dạng code), chỉ tập trung vào các cập nhật có ý nghĩa đối với người dùng hoặc hệ thống.

---

## Cách Sử Dụng File Này

* Mỗi khi dự án có các thay đổi đáng chú ý hoặc khi phát hành một phiên bản mới, hãy cập nhật thông tin tương ứng vào phần trên cùng của nhật ký thay đổi (theo thứ tự thời gian mới nhất ở trên).
* Việc phân chia lịch sử thay đổi nên được ghi nhận rõ ràng theo ngày tháng (YYYY-MM-DD) hoặc số phiên bản (version).

**Giải thích ý nghĩa phiên bản (version):**
* **`0.1.0`**: Phiên bản khởi tạo ban đầu, đang trong quá trình xây dựng hoặc thử nghiệm.
* **`1.0.0`**: Phiên bản đầu tiên hoàn chỉnh, có đầy đủ các chức năng cơ bản ổn định và sẵn sàng sử dụng.
* Quy tắc tăng phiên bản: Hãy tăng số phiên bản khi dự án có các nâng cấp lớn, thêm chức năng quan trọng hoặc sửa đổi lớn cấu trúc database/hệ thống.

---

## Các Nhóm Thay Đổi Thường Dùng

Để dễ theo dõi, các thay đổi trong mỗi phiên bản thường được phân loại vào các nhóm dưới đây:

* **`Added`** (Thêm mới): Ghi nhận các tính năng, tài liệu hoặc thành phần mới được tích hợp vào dự án.
* **`Changed`** (Thay đổi): Ghi nhận các thay đổi, tối ưu hóa hoặc nâng cấp trên các tính năng hiện có.
* **`Fixed`** (Sửa lỗi): Ghi nhận các lỗi lập trình hoặc sự cố đã được khắc phục.
* **`Removed`** (Loại bỏ): Ghi nhận các chức năng hoặc thành phần đã bị xóa khỏi dự án.
* **`Docs`** (Tài liệu): Ghi nhận các thay đổi hoặc bổ sung liên quan đến tài liệu dự án.
* **`Security`** (Bảo mật): Ghi nhận các bản vá hoặc cập nhật giúp khắc phục các lỗ hổng bảo mật.

---

## Mẫu Ghi Changelog

Bạn có thể sao chép đoạn mã Markdown dưới đây để bắt đầu viết nhật ký thay đổi cho phiên bản mới:

```md
## [version] - YYYY-MM-DD

### Added
- 

### Changed
- 

### Fixed
- 

### Removed
- 
```

---

## Ví Dụ

Dưới đây là một ví dụ minh họa về cách ghi chép nhật ký thay đổi:

```md
## [0.1.0] - 2026-06-15

### Added
- Khởi tạo cấu trúc GitHub template repository.
- Thêm thư mục `App/`, `docs/`, `database/` và `.github/`.
- Thêm file `CONTRIBUTING.md` để ghi quy tắc đóng góp và quy tắc commit.
- Thêm file `LICENSE` để xác định giấy phép sử dụng mã nguồn.
```

---

## Lưu Ý Khi Cập Nhật

* **Ngắn gọn và rõ ràng:** Diễn đạt súc tích, dễ hiểu về thay đổi cốt lõi.
* **Mỗi dòng một thay đổi:** Tránh viết gộp nhiều thay đổi khác nhau vào cùng một dòng.
* **Lọc bỏ chi tiết thừa:** Tránh ghi chép các thay đổi quá nhỏ không tác động đến cách thức vận hành của dự án (ví dụ: đổi tên biến nội bộ, sửa khoảng trắng...).
* **Cập nhật đúng thời điểm:** Nên cập nhật changelog ngay trước khi tạo một release (phiên bản mới), nộp dự án hoặc gộp nhánh chính.
* **Ghi nhận thay đổi quan trọng:** Bất kỳ thay đổi nào liên quan trực tiếp đến cấu trúc thư mục, tài liệu, hay tập tin script cơ sở dữ liệu (`database/`) đều cần được ghi lại cẩn thận.

---
