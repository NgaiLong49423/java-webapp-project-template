# Hướng Dẫn Đóng Góp

Tài liệu này cung cấp các quy định và hướng dẫn chi tiết về cách đóng góp mã nguồn (code), cách viết thông điệp ghi nhận thay đổi (commit message), cách đặt tên nhánh (branch) và quy trình gửi yêu cầu gộp mã nguồn (pull request) cho dự án. Việc tuân thủ các quy tắc này giúp dự án luôn sạch sẽ, dễ bảo trì và làm việc nhóm hiệu quả hơn.

---

## Quy Tắc Chung

Để giữ cho kho lưu trữ mã nguồn của dự án luôn chuyên nghiệp, hãy tuân thủ các quy tắc cốt lõi sau:

* **Giữ code sạch, dễ đọc:** Viết code rõ ràng, tuân thủ các chuẩn định dạng (coding conventions) của ngôn ngữ lập trình được sử dụng.
* **Không commit file rác:** Tránh đưa các file tạm thời, file build, hoặc các file cấu hình cá nhân không cần thiết vào Git.
* **Viết commit message rõ ràng và có ý nghĩa:** Giúp các thành viên khác hiểu ngay bạn đã thay đổi những gì và tại sao.
* **Cập nhật tài liệu đầy đủ:** Nếu thay đổi của bạn ảnh hưởng đến cách cài đặt, cấu hình hoặc sử dụng dự án, hãy cập nhật lại tài liệu hướng dẫn liên quan.
* **Kiểm tra kỹ trước khi push code:** Hãy chắc chắn rằng mã nguồn được biên dịch thành công và chạy thử không gặp lỗi trước khi đẩy lên GitHub.

**Giải thích thuật ngữ:**
* **Commit** (lần lưu): Hành động lưu lại trạng thái thay đổi của các file mã nguồn vào lịch sử Git tại máy cá nhân.
* **Push** (đẩy code): Hành động gửi các commit từ máy tính cá nhân (local) lên kho lưu trữ trực tuyến trên GitHub.
* **Repository** (kho lưu trữ / repo): Nơi lưu trữ toàn bộ mã nguồn, tài liệu và lịch sử các phiên bản của dự án.

---

## Quy Tắc Đặt Tên Branch

**Branch** (nhánh) là một nhánh mã nguồn độc lập được tách ra từ nhánh chính (như `main` hoặc `master`) để phát triển tính năng hoặc sửa lỗi mà không làm ảnh hưởng trực tiếp đến mã nguồn hiện tại của dự án.

Khi làm việc, bạn cần tạo nhánh mới và đặt tên theo cấu trúc:
`[loại-nhánh]/[tên-ngắn-gọn]`

### Các tiền tố nhánh thông dụng:
* **`feature/`**: Sử dụng khi phát triển một tính năng mới.
* **`fix/`**: Sử dụng khi sửa lỗi (bug).
* **`docs/`**: Sử dụng khi cập nhật, sửa đổi tài liệu hướng dẫn hoặc tài liệu dự án.
* **`refactor/`**: Sử dụng khi tối ưu hóa, tái cấu trúc mã nguồn nhưng không làm thay đổi tính năng hệ thống.
* **`chore/`**: Sử dụng cho các công việc phụ trợ như thiết lập (setup) ban đầu, cấu hình dự án, cập nhật thư viện.

### Ví dụ cụ thể:
```text
feature/login-page
fix/database-connection
docs/update-readme
refactor/user-service
chore/project-setup
```

---

## Quy Tắc Viết Commit Message

Dự án này sử dụng tiêu chuẩn **Conventional Commits** để quản lý lịch sử commit. Định dạng chuẩn của một commit message như sau:

```text
<type>(<optional scope>): <description>

<optional body>

<optional footer>
```

**Giải thích chi tiết các thành phần:**
* **`type`** (bắt buộc): Loại thay đổi của commit (xem chi tiết ở phần bên dưới).
* **`scope`** (không bắt buộc): Phạm vi hoặc thành phần bị ảnh hưởng bởi thay đổi (ví dụ: `auth` - xác thực, `database` - cơ sở dữ liệu, `readme`).
* **`description`** (bắt buộc): Mô tả ngắn gọn về những gì đã thay đổi.
* **`body`** (không bắt buộc): Phần giải thích chi tiết hơn về nguyên nhân và cách thức thực hiện thay đổi.
* **`footer`** (không bắt buộc): Phần ghi chú cuối cùng, dùng để liên kết mã công việc (issue) hoặc đánh dấu thay đổi gây phá vỡ tương thích (breaking change).

---

## Các Loại Commit Type

Hãy chọn đúng loại `type` phù hợp với thay đổi của bạn:

* **`feat`** (feature): Thêm mới, cập nhật hoặc loại bỏ một chức năng/tính năng cho ứng dụng hoặc API/UI.
* **`fix`**: Sửa lỗi của một tính năng hay logic đã có trước đó.
* **`docs`**: Chỉ thực hiện thay đổi liên quan đến tài liệu (ví dụ: cập nhật file `README.md`, `CONTRIBUTING.md`).
* **`style`**: Chỉnh sửa định dạng hiển thị của code như khoảng trắng, xuống dòng, dấu chấm phẩy, thụt lề... mà không làm thay đổi logic hoạt động của chương trình.
* **`refactor`**: Tái cấu trúc mã nguồn nhằm tối ưu hóa, làm sạch code nhưng không làm thay đổi chức năng.
* **`perf`** (performance): Một dạng đặc biệt của `refactor` giúp tăng tốc độ xử lý hoặc tiết kiệm tài nguyên hệ thống.
* **`test`**: Thêm mới các bài kiểm tra tự động hoặc sửa đổi các bài kiểm tra (test) hiện có.
* **`build`**: Thay đổi liên quan đến công cụ xây dựng dự án (build tools), quản lý thư viện phụ thuộc (dependencies) hoặc phiên bản dự án (ví dụ: Maven, Gradle, npm).
* **`chore`**: Các tác vụ phụ trợ, không trực tiếp thay đổi code chạy của ứng dụng (ví dụ: sửa file `.gitignore`, cấu hình ban đầu).
* **`ops`**: Thay đổi liên quan đến vận hành, triển khai (deploy), hạ tầng, CI/CD (quy trình tự động xây dựng, kiểm thử và triển khai), giám sát hệ thống.

---

## Scope (Phạm vi)

* **`scope`** là phạm vi hoặc mô-đun bị tác động bởi commit đó.
* Việc điền `scope` là không bắt buộc, nhưng được khuyến khích sử dụng khi thay đổi chỉ nằm trong một khu vực cụ thể để dễ theo dõi.

### Quy tắc viết Scope:
* Không sử dụng mã công việc/lỗi (issue ID) để làm scope.
* Viết scope ngắn gọn, dễ hiểu và dùng chữ thường (lowercase).

### Ví dụ:
```text
feat(auth): thêm form đăng nhập
fix(database): xử lý lỗi mất kết nối database
docs(readme): cập nhật hướng dẫn sử dụng
```

---

## Quy Tắc Viết Description

**`description`** là mô tả ngắn gọn về các thay đổi, được viết ngay sau dấu hai chấm và khoảng trắng `: `. Đây là phần bắt buộc của mỗi commit message.

### Quy tắc khi viết Description:
* Viết ngắn gọn, rõ nghĩa và đi thẳng vào vấn đề.
* Không viết hoa chữ cái đầu tiên của description.
* Không sử dụng dấu chấm (`.`) ở cuối câu.
* Nên viết theo dạng mệnh lệnh (ví dụ: dùng các từ như `thêm`, `sửa`, `xóa` thay vì `đã thêm`, `đã sửa`).
* Tránh viết các commit mô tả chung chung, vô nghĩa.

### Ví dụ SAI:
```text
fix(auth): Fixed login bug.
update
aaa
```

### Ví dụ ĐÚNG:
```text
fix(auth): sửa lỗi đăng nhập khi password rỗng
feat(cart): thêm chức năng lưu giỏ hàng
docs: cập nhật hướng dẫn sử dụng README
```

---

## Commit Body (Nội dung chi tiết)

* **`body`** là phần không bắt buộc.
* Được sử dụng khi thay đổi phức tạp và bạn cần giải thích rõ **LÝ DO** thực hiện thay đổi đó hoặc cách giải quyết so với phiên bản trước.
* Giữa dòng tiêu đề và phần `body` cần có 1 dòng trống làm dấu phân cách.

### Ví dụ:
```text
fix(auth): kiểm tra password trước khi đăng nhập

Trước đây hệ thống cho phép password rỗng đi qua bước kiểm tra.
Thay đổi này bổ sung điều kiện bắt buộc nhập password trước khi xác thực.
```

---

## Commit Footer (Chân trang)

* **`footer`** là phần cuối cùng của commit message, không bắt buộc.
* Thường dùng để liên kết mã công việc/lỗi hoặc ghi chú các thay đổi đột phá.
* Giữa phần `body` (hoặc tiêu đề nếu không có body) và phần `footer` cần có 1 dòng trống làm dấu phân cách.

**Giải thích thuật ngữ:**
* **Issue**: Các thẻ ghi nhận công việc, lỗi, hoặc yêu cầu tính năng được quản lý trên GitHub hoặc các công cụ quản lý dự án (như Jira, Trello).
* **Breaking Change**: Thay đổi lớn làm phá vỡ tính tương thích ngược, có khả năng làm mã nguồn cũ hoặc API cũ không hoạt động được nữa.

### Ví dụ:
```text
Closes #123
Fixes JIRA-456
BREAKING CHANGE: xóa endpoint user profile cũ
```

---

## Breaking Changes (Thay đổi đột phá)

Khi thay đổi của bạn làm ảnh hưởng trực tiếp đến khả năng chạy của hệ thống cũ (ví dụ: đổi tên hàm cốt lõi, đổi cấu trúc bảng database quan trọng):
* Đặt dấu chấm than `!` ngay trước dấu hai chấm ở tiêu đề commit: `<type>(<scope>)!: <description>`.
* Bắt buộc khai báo thông tin chi tiết bằng cụm từ `BREAKING CHANGE:` ở phần footer.

### Ví dụ:
```text
feat(api)!: xóa endpoint user cũ

BREAKING CHANGE: `/api/v1/users` đã bị xóa và được thay bằng `/api/v2/users`.
```

---

## Ví Dụ Commit Chuyên Nghiệp

Dưới đây là một số ví dụ thực tế chuẩn hóa theo Conventional Commits:

```text
chore: init
feat(auth): thêm trang đăng nhập
fix(database): xử lý lỗi mất kết nối database
docs: cập nhật mô tả dự án
refactor(user): đơn giản hóa logic kiểm tra dữ liệu
style: định dạng lại các file Java
test(auth): thêm test kiểm tra đăng nhập
build: cập nhật dependency của dự án
perf: giảm số lần truy vấn database lặp lại
chore: cập nhật .gitignore
```

---

## Quy Tắc Pull Request

**Pull Request** (yêu cầu gộp code / PR) là cách bạn yêu cầu những người quản lý dự án xem xét và gộp mã nguồn từ nhánh của bạn vào nhánh chính.

Để gửi một pull request thành công:
1. **Đặt tiêu đề rõ ràng:** Tiêu đề PR nên tuân theo định dạng tương tự commit message (ví dụ: `feat(auth): thêm trang đăng nhập`).
2. **Mô tả chi tiết nội dung:** Điền đầy đủ thông tin vào mẫu PR, mô tả rõ các thay đổi bạn đã thực hiện và lý do thay đổi.
3. **Liên kết Issue:** Sử dụng các từ khóa như `Closes #123` để tự động đóng issue liên quan khi PR được gộp.
4. **Kiểm tra hoạt động:** Chắc chắn rằng dự án của bạn vẫn chạy được và không làm hỏng các tính năng cũ.
5. **Dọn dẹp code:** Đảm bảo không có code thừa, comment nháp hay các file rác trước khi gửi PR.

---

## Checklist Trước Khi Push Code

Trước khi thực hiện lệnh `git push` để đẩy code lên GitHub, hãy kiểm tra danh sách sau:

- [ ] Code đã biên dịch và chạy thành công trên máy cá nhân.
- [ ] Không có file rác, file build tạm hoặc file cấu hình cá nhân trong danh sách commit.
- [ ] Tất cả các commit message đều tuân thủ đúng định dạng Conventional Commits.
- [ ] Tài liệu hướng dẫn liên quan đã được cập nhật đầy đủ (nếu có thay đổi cách sử dụng).
- [ ] Các tập tin script cơ sở dữ liệu đã được cập nhật đầy đủ (nếu có thay đổi schema database).
