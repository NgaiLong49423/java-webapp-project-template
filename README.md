# [Tên Dự Án]

<!-- 
Tech Badges:
Badge là biểu tượng nhỏ hiển thị công nghệ sử dụng trong dự án.
Khi tạo repo mới từ template này, hãy giữ lại badge đúng với dự án và xóa badge không dùng.
Có thể tạo thêm badge tại: https://shields.io/
-->

![Java](https://img.shields.io/badge/Java-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white)
![Servlet](https://img.shields.io/badge/Servlet-007396?style=for-the-badge&logo=java&logoColor=white)
![JSP](https://img.shields.io/badge/JSP-007396?style=for-the-badge&logo=java&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![SQL Server](https://img.shields.io/badge/SQL_Server-CC2927?style=for-the-badge&logo=microsoftsqlserver&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![Apache Tomcat](https://img.shields.io/badge/Apache_Tomcat-F8DC75?style=for-the-badge&logo=apachetomcat&logoColor=black)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)

> Ghi chú: Đây là danh sách badge mẫu. Khi dùng template cho dự án thật, hãy xóa công nghệ không dùng và thêm công nghệ phù hợp.

## 1. Giới Thiệu

Viết phần mô tả ngắn về dự án tại đây.

[Dự án] là một ứng dụng [loại ứng dụng] được xây dựng nhằm [mục tiêu chính của dự án].
Dự án này phục vụ cho [đối tượng sử dụng] và được phát triển trong bối cảnh [môn học / đồ án / dự án cá nhân / dự án nhóm].

## 2. Mục Tiêu Dự Án

Liệt kê các mục tiêu chính của dự án:
- Mục tiêu 1
- Mục tiêu 2
- Mục tiêu 3

## 3. Chức Năng Chính

Ghi các chức năng chính của hệ thống.
`Feature` là chức năng mà hệ thống cung cấp cho người dùng.

- [ ] Chức năng 1
- [ ] Chức năng 2
- [ ] Chức năng 3

## 4. Công Nghệ Sử Dụng

Ghi các công nghệ, ngôn ngữ lập trình, framework hoặc công cụ được dùng.
`Framework` là bộ khung hỗ trợ phát triển ứng dụng nhanh hơn.
`Database` là cơ sở dữ liệu dùng để lưu thông tin của hệ thống.

- Programming Language: [Java / Python / JavaScript / ...]
- Framework: [Servlet / Spring Boot / ...]
- Database: [MySQL / SQL Server / PostgreSQL / ...]
- Frontend: [HTML / CSS / JavaScript / JSP / ...]
- Build Tool: [Maven / Gradle / None]
- IDE: [NetBeans / IntelliJ IDEA / VS Code / ...]

## 5. Cấu Trúc Thư Mục

Giải thích ngắn cấu trúc thư mục chính của repo (repository - kho lưu trữ mã nguồn).

```text
.
├── App/
├── .agent/
├── docs/
├── database/
├── .github/
├── README.md
├── CONTRIBUTING.md
├── CHANGELOG.md
└── LICENSE
```

Giải thích:
* `App/`: nơi chứa source code (mã nguồn) chính của ứng dụng.
* `.agent/`: nơi chứa các skill, orchestrator, rules và tài liệu liên quan để agent làm việc 
* `docs/`: nơi chứa tài liệu dự án.
* `database/`: nơi chứa script (kịch bản mã lệnh) database.
* `.github/`: nơi chứa cấu hình GitHub như issue template (mẫu báo lỗi/công việc), pull request template (mẫu yêu cầu gộp nhánh) và label template (mẫu nhãn phân loại).
* `CONTRIBUTING.md`: hướng dẫn cách đóng góp, đặt tên branch (nhánh phát triển) và viết commit (lịch sử lưu thay đổi).
* `CHANGELOG.md`: nhật ký thay đổi của dự án.
* `LICENSE`: giấy phép sử dụng mã nguồn.

## 6. Tài Liệu Dự Án

Ghi vị trí các tài liệu quan trọng:
- Yêu cầu dự án: `docs/requirements/`
- Sơ đồ ERD: `docs/diagrams/ERD/`
- Sơ đồ Use Case: `docs/diagrams/UseCase/`
- Báo cáo: `docs/reports/`

`ERD` là Entity Relationship Diagram, nghĩa là sơ đồ quan hệ thực thể trong database.
`Use Case` là mô tả cách người dùng tương tác với hệ thống.

## 7. Database

Ghi thông tin liên quan đến database (cơ sở dữ liệu):
- File tạo bảng: `database/schema.sql`
- File dữ liệu mẫu: `database/sample-data.sql`
- File truy vấn mẫu: `database/queries.sql`

Ghi chú:
* Cập nhật script database mỗi khi thay đổi cấu trúc bảng.
* Không hardcode dữ liệu quan trọng trực tiếp trong source code nếu dữ liệu đó nên lấy từ database.

`Hardcode` là viết cố định dữ liệu trong code thay vì lấy từ database hoặc file cấu hình.

## 8. Cách Chạy Dự Án

Viết hướng dẫn chạy dự án sau này:
1. Clone repository về máy.
2. Mở dự án bằng IDE (môi trường phát triển tích hợp).
3. Cấu hình database nếu cần.
4. Chạy script trong thư mục `database/`.
5. Build và chạy ứng dụng.
6. Truy cập ứng dụng qua trình duyệt hoặc terminal (giao diện dòng lệnh).

`Clone` là tải repository từ GitHub về máy.
`Build` là quá trình biên dịch hoặc đóng gói dự án để chạy.

## 9. Quy Trình Làm Việc Với GitHub

Ghi quy trình làm việc đề xuất:
1. Tạo issue để mô tả công việc.
2. Tạo branch mới từ issue.
3. Code và commit theo quy tắc trong `CONTRIBUTING.md`.
4. Tạo pull request để review.
5. Merge vào branch chính sau khi kiểm tra.

`Issue` là ticket công việc hoặc lỗi cần xử lý.
`Branch` là nhánh code dùng để phát triển riêng.
`Pull Request` là yêu cầu gộp code từ branch này sang branch khác.
`Merge` là thao tác gộp code.

## 10. Quy Tắc Commit

Ghi ngắn gọn rằng dự án dùng Conventional Commits.
`Conventional Commits` là quy ước viết commit theo dạng rõ ràng để lịch sử Git dễ đọc hơn.

Cú pháp:
```text
<type>(<scope>): <description>
```

Ví dụ:
* `feat(auth): thêm chức năng đăng nhập`
* `fix(database): sửa lỗi kết nối database`
* `docs: cập nhật README`
* `refactor(user): đơn giản hóa logic xử lý user`

Xem chi tiết quy ước tại file [CONTRIBUTING.md](file:///d:/Github-Projects/java-webapp-project-template/CONTRIBUTING.md).

## 11. Issue Và Label

Giải thích repo (kho chứa) có sẵn issue form và label mẫu.

Repo này có sẵn các issue form trong `.github/ISSUE_TEMPLATE/`:
- Bug Report (báo cáo lỗi)
- Feature Request (yêu cầu tính năng)
- Non-Functional Requirement (yêu cầu phi chức năng)
- Task (công việc kỹ thuật)

Danh sách label mẫu nằm trong `.github/labels.yml`.
Lưu ý: GitHub không tự động tạo label từ file này. Cần dùng agent hoặc GitHub CLI (công cụ dòng lệnh của GitHub) để tạo label theo danh sách đó.

## 12. Changelog

Lịch sử thay đổi quan trọng của dự án được ghi trong [CHANGELOG.md](file:///d:/Github-Projects/java-webapp-project-template/CHANGELOG.md).
Hãy cập nhật file này khi thêm chức năng lớn, sửa lỗi quan trọng, thay đổi database hoặc thay đổi cấu trúc dự án.

## 13. License

Dự án này sử dụng giấy phép trong file [LICENSE](file:///d:/Github-Projects/java-webapp-project-template/LICENSE).
`License` là giấy phép quy định người khác được sử dụng, chỉnh sửa hoặc phân phối mã nguồn như thế nào.

## 14. Thành Viên / Tác Giả

| Họ tên | Vai trò | GitHub |
|---|---|---|
| [Tên thành viên] | [Vai trò] | [GitHub username] |

## 15. Ghi Chú

README này là mẫu khởi đầu cho dự án.
Khi tạo repository mới từ template, hãy cập nhật lại nội dung cho đúng với dự án thực tế.
