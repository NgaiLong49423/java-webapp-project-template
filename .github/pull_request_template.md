# Pull Request

> **Pull Request (PR - Yêu cầu gộp code):** Là yêu cầu xem xét và gộp mã nguồn từ một nhánh phát triển riêng biệt vào nhánh chính của dự án. Hãy điền đầy đủ các thông tin dưới đây để người duyệt code (reviewer) dễ dàng kiểm tra và phê duyệt.

---

## 1. Mô Tả Thay Đổi

Mô tả ngắn gọn những thay đổi chính mà Pull Request này mang lại:

- 

## 2. Lý Do Thay Đổi

Giải thích nguyên nhân hoặc mục đích của việc thực hiện những thay đổi này:

- 

## 3. Loại Thay Đổi

*Chọn loại thay đổi phù hợp bằng cách đánh dấu `x` vào ô vuông (ví dụ: `[x]`)*:

- [ ] `feat`: thêm tính năng mới
- [ ] `fix`: sửa lỗi
- [ ] `docs`: cập nhật tài liệu
- [ ] `style`: chỉnh định dạng code, không thay đổi logic
- [ ] `refactor`: tái cấu trúc code, không thay đổi chức năng
- [ ] `test`: thêm hoặc chỉnh sửa test
- [ ] `build`: thay đổi dependency, build tool hoặc cấu hình build
- [ ] `chore`: công việc phụ trợ như setup, cấu hình, dọn dẹp file
- [ ] `ops`: thay đổi liên quan đến deploy, CI/CD hoặc vận hành

## 4. Branch Liên Quan

Ghi tên nhánh đang được yêu cầu gộp (merge):

```text
Branch: 
```

> **Giải thích thuật ngữ:**
> * **Branch (nhánh):** Nhánh mã nguồn song song dùng để phát triển các chức năng hoặc sửa lỗi riêng biệt trước khi gộp vào nhánh chính.
> * **Merge (gộp code):** Thao tác gộp tất cả các thay đổi từ nhánh này vào nhánh khác.

## 5. Issue Liên Quan

Nếu Pull Request này giải quyết một issue (vấn đề) đã được tạo trên GitHub, hãy ghi mã issue tại đây để liên kết:

```text
Closes #
```

*Nếu không có issue liên quan, ghi:*

```text
Không có
```

> **Giải thích thuật ngữ:**
> * **Issue:** Một thẻ ghi nhận đầu việc, lỗi, hoặc yêu cầu thảo luận tính năng được quản lý trên GitHub.

## 6. Những File/Thư Mục Bị Ảnh Hưởng

Liệt kê các tập tin hoặc thư mục chính trực tiếp chịu ảnh hưởng của thay đổi:

- 

*Ví dụ minh họa:*
* `- App/`
* `- database/schema.sql`
* `- README.md`

## 7. Cách Kiểm Tra

Mô tả các bước hoặc phương thức bạn đã kiểm tra (test) thay đổi này trước khi gửi PR:

- [ ] Đã chạy project thành công
- [ ] Đã kiểm tra chức năng liên quan
- [ ] Đã kiểm tra database script nếu có thay đổi database
- [ ] Đã kiểm tra tài liệu nếu có thay đổi documentation

*Nếu chưa kiểm tra được, hãy ghi rõ lý do:*
- 

## 8. Ảnh Chụp Màn Hình Hoặc Demo

Nếu thay đổi của bạn có tác động đến giao diện người dùng (UI), hãy đính kèm ảnh chụp màn hình hoặc cung cấp liên kết video/mô tả demo tại đây:

```text
Không có
```

## 9. Ghi Chú Thêm

Cung cấp bất kỳ thông tin bổ sung nào cần người duyệt code lưu ý:

```text
Không có
```

## 10. Checklist Trước Khi Merge

*Đảm bảo bạn đã tích chọn đầy đủ các mục này trước khi yêu cầu gộp nhánh:*

- [ ] Code chạy thành công
- [ ] Không commit file rác hoặc file không cần thiết
- [ ] Commit message tuân theo Conventional Commits
- [ ] Tên branch rõ ràng và đúng quy ước
- [ ] Đã cập nhật tài liệu nếu cần
- [ ] Đã cập nhật database script nếu cần
- [ ] Không làm ảnh hưởng chức năng cũ
- [ ] Pull Request có mô tả rõ ràng
