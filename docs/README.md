# Tài Liệu Dự Án - [Tên Dự Án]

## Mục Đích Thư Mục `docs/`

Thư mục `docs/` (viết tắt của documents - tài liệu) là nơi lưu trữ toàn bộ tài liệu chính thức liên quan đến dự án.
* Tài liệu giúp các thành viên trong nhóm, giảng viên hoặc người đánh giá dễ dàng hiểu được yêu cầu nghiệp vụ, kiến trúc thiết kế, sơ đồ hoạt động và báo cáo tiến độ của dự án.
* Việc lưu trữ tập trung tại đây giúp đảm bảo tài liệu luôn đi kèm với mã nguồn, tránh tình trạng thất lạc hoặc mâu thuẫn giữa tài liệu và mã nguồn thực tế.

## Cấu Trúc Thư Mục

Dưới đây là cấu trúc tổ chức các thư mục tài liệu trong dự án:

```text
docs/
├── requirements/
│   ├── SRS.md
│   └── project-requirements.md
│
├── diagrams/
│   ├── Activity/
│   │   └── README.md
│   ├── ERD/
│   │   └── README.md
│   └── UseCase/
│       └── README.md
│
└── reports/
    └── README.md
```

## Ý Nghĩa Các Thư Mục

* **`requirements/`** (Requirement - yêu cầu): Lưu trữ các yêu cầu của dự án, bao gồm cả yêu cầu nghiệp vụ chi tiết và đặc tả kỹ thuật.
* **`diagrams/`** (Diagram - sơ đồ): Chứa các sơ đồ mô tả kiến trúc, luồng hoạt động và thiết kế cơ sở dữ liệu của hệ thống.
  * **`Activity/`** (Sơ đồ hoạt động): Chứa sơ đồ luồng đi của các chức năng nghiệp vụ chi tiết.
  * **`ERD/`** (Sơ đồ quan hệ thực thể): Chứa thiết kế bảng và mối quan hệ giữa các bảng trong cơ sở dữ liệu.
  * **`UseCase/`** (Sơ đồ ca sử dụng): Chứa sơ đồ mô tả sự tương tác giữa người dùng (Actor) và các chức năng hệ thống.
* **`reports/`** (Report - báo cáo): Chứa các báo cáo tiến độ, nhật ký làm việc nhóm, biên bản họp hoặc tài liệu nộp môn học.

## Quy Tắc Viết Tài Liệu

Khi cập nhật tài liệu trong thư mục này, vui lòng tuân thủ các checklist (danh sách kiểm tra) sau:
- [ ] Viết rõ ràng, ngắn gọn và dễ hiểu.
- [ ] Cập nhật tài liệu kịp thời mỗi khi thay đổi chức năng.
- [ ] Không để tài liệu mâu thuẫn với mã nguồn thực tế đang chạy.
- [ ] Nếu thay đổi cấu trúc bảng cơ sở dữ liệu, phải cập nhật đồng thời file ERD và script tạo bảng tại `database/schema.sql`.
- [ ] Nếu thay đổi luồng xử lý hoặc nghiệp vụ, phải cập nhật sơ đồ hoạt động (Activity Diagram) tương ứng.
