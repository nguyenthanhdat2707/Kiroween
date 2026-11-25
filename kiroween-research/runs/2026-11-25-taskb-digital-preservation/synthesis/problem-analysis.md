# Phân tích vấn đề — Task B

Tổng hợp của Coordinator từ ba báo cáo độc lập và ba bản phản biện chéo. Tài liệu không lặp lại nội dung gốc; mã claim trỏ về báo cáo của từng agent:

- Agent A: [`../agent-a/report.md`](../agent-a/report.md), [`../agent-a/cross-review.md`](../agent-a/cross-review.md)
- Agent B: [`../agent-b/report.md`](../agent-b/report.md), [`../agent-b/cross-review.md`](../agent-b/cross-review.md)
- Agent C: [`../agent-c/report.md`](../agent-c/report.md), [`../agent-c/cross-review.md`](../agent-c/cross-review.md)

Nhãn được dùng theo **nhãn sau Round 2** của từng agent.

## 1. Câu hỏi trung tâm có đứng vững không?

Câu hỏi của người dùng: *"Can we preserve the value created by digital platforms even when the original platforms can no longer survive?"*

Ba agent làm độc lập. Trong Round 1 không agent nào đọc báo cáo của agent khác. Cả ba **cùng phản bác** câu hỏi ở những điểm sau:

| Phản bác | A | B | C |
|---|---|---|---|
| "Giá trị nền tảng" không đồng nhất với dữ liệu: hiệu ứng mạng đang sống không lưu trữ được | §11.1 | §11.1 | §11.1–2 |
| Không phải nền tảng nào cũng đáng sống. Bảo tồn phải có chọn lọc | §11.2 (Wren 2017: 94% tài nguyên được trích dẫn nhiều tự sống sót) | §11.4 (>70% game gacha Nhật đóng trong 3 năm, `B-G-C5`) | `C-G-C4` |
| Nút thắt ở các ca giá trị cao nhất là **pháp lý/IP**, không phải kỹ thuật | §11.3 (Hachette v. IA; DMCA §1201) | §11.1, §11.6 | §11.5 |
| Duy trì nền tảng chết ở trạng thái chạy sống lặp lại thất bại kinh tế ban đầu | §11.4 | (Cyworld, `B §6`) | §11.4 |
| Chuẩn bị **trước** khi đóng rẻ hơn cứu **sau** khi đóng | — | §11.3 (`B-G-C17`) | khung "bàn giao" của C-O1/C-O2/C-O3 |
| Nhu cầu xã hội khác với thị trường cho một công cụ mới | — | §11.5 | §11.3 |
| AI không phải phần bắt buộc | (hạ A-O2, A-O3 xuống "useful" ở Round 2) | (AI "unnecessary" ở B-O2, B-O3) | §11.6 |

**Kết luận của Coordinator (SUY LUẬN, dựa trên đồng thuận độc lập của ba agent):** câu hỏi trung tâm quá rộng ở dạng hiện tại. Phiên bản đứng vững được qua phản biện là hẹp hơn:

> Với **một số ít** nền tảng có cộng đồng hoặc giá trị chứng cứ rõ ràng, có thể **chuyển giao** một phần giá trị cụ thể (dữ liệu có ngữ nghĩa, phần mềm chạy được, quyền vận hành) sang một chủ thể kế nhiệm **trước hoặc ngay khi** nền tảng đóng, **trong giới hạn pháp lý**.

Cả ba agent đều không chứng minh được rằng có người trả tiền cho công cụ làm việc này.

## 2. Cây nguyên nhân hợp nhất

Mỗi nhánh dẫn tới cây gốc của agent đó.

```text
Hệ quả: giá trị do người dùng/cộng đồng tạo ra không còn truy cập, chạy, hay kiểm chứng được
│
├─ A. Kinh tế vận hành (cả ba agent)
│   ├─ chi phí hạ tầng, kiểm duyệt, pháp lý tăng; doanh thu ở quy mô ngách không bù
│   │    Cohost: 30.000 MAU, thâm hụt ~17.000 USD/tháng [B-G-C4]; Glitch [B-G-C3]
│   ├─ tài trợ có kỳ hạn: grant 2–5 năm cho web app học thuật [A §2]; ngân sách hữu hạn [C-G-C2]
│   └─ vòng đời ngắn có chủ đích: game gacha Nhật [B-G-C5]
│
├─ B. Kiến trúc phụ thuộc (A, B)
│   ├─ phần mềm chỉ chạy khi server/DRM của nhà phát hành còn sống [B-O1-C2; A §2]
│   └─ export bị phẳng hóa, mất quan hệ và ngữ nghĩa [A §2; C-G-C15/C20]
│
├─ C. Quyết định thương mại và tái cấu trúc (A, C)
│   └─ thâu tóm rồi khai tử, đổi mô hình kinh doanh [A §2]; chủ thể đổi ưu tiên [C-G-C2]
│
└─ D. Thiếu cơ chế bàn giao (C; B ở "trước khi chết")
    └─ không có quyền, bản sao đủ, kiến thức vận hành hay người kế nhiệm khi chủ thể rút [C-G-C2]
```

**Suy giảm người dùng là nguyên nhân hay triệu chứng?** Ba agent đều trả lời "**không phải nguyên nhân chính duy nhất**":

- B, §2.2: Glitch đóng khi vẫn còn hàng triệu người dùng; City of Heroes đóng khi cộng đồng còn sẵn sàng trả tiền.
- C, `C-G-C2`: Nintendo nêu lý do giảm sử dụng cho eShop, nhưng nguồn đó không chứng minh đây là nguyên nhân chung.

Ca quan trọng nhất là **giá trị vẫn còn sống, nhưng mô hình kinh doanh thì không** (B §11.2).

## 3. Khi nào bảo tồn **không** đáng làm

Tiêu chí của C (`C-G-C4`), được A và B bổ sung. Bảo tồn không đáng làm khi:

1. một bản thay thế đã giữ được công việc người dùng cần làm;
2. nội dung chỉ là bản trùng;
3. không có chủ thể hợp pháp nào nhận quản lý;
4. chi phí vận hành vượt giá trị sử dụng và giá trị chứng cứ (A §11.4, B §6: Cyworld khôi phục thất bại vì chi phí);
5. sao chép sẽ vi phạm quyền được quên, quyền cộng đồng hoặc giới hạn tái phát hành (C §11.5).

## 4. Bảy chiều bảo tồn: giá trị và tính khả thi

Mỗi agent phân tích ở §4 báo cáo của mình. Bảng dưới là đánh giá tổng hợp của Coordinator (SUY LUẬN).

| Chiều | Hạ tầng hiện có | Nút thắt chính | Ghi chú |
|---|---|---|---|
| Nội dung | Mạnh: Internet Archive, Archive-It, Webrecorder/WACZ, CLOCKSS/LOCKSS/PKP PN | Tham gia và tài trợ, không phải kỹ thuật (B §11.1) | ~28% DOI không xác nhận được bảo tồn (`C-G-C1`: không suy ra là đã mất) |
| Tri thức | Như trên, thêm Software Heritage | Ngữ cảnh và chọn lọc | |
| Chức năng phần mềm | EaaSI, emulator, Software Heritage | **IP (§1201)**, server backend không có sẵn | Truy cập EaaSI chỉ tại chỗ ở Mỹ (B §5) |
| Dữ liệu và workflow người dùng | GDPR Art. 20, DTI/DTP, EU Data Act (A) | Chỉ phục vụ nền tảng lớn còn sống; nền tảng nhỏ phá sản không được phủ (B §5) | Ngữ nghĩa bị mất khi export (C-O3) |
| Cộng đồng | Mastodon, Lemmy, Discord… làm nơi di cư | Đồ thị xã hội mất; người dùng tự tìm nhau (B §5, Cohost) | Khó bảo tồn nhất về bản chất (A §11.1) |
| Di sản văn hóa | NDL WARP, NLK OASIS, Mukurtu, PARADISEC, ELAR | Quyền cộng đồng, đồng thuận, kế nhiệm tổ chức | Theme Resurrection yếu nếu không có công nghệ chết làm mỏ neo |
| Vận hành liên tục | Private server cộng đồng (Homecoming, Pretendo) | Lặp lại thất bại kinh tế; burnout; IP | Homecoming có license từ NCSoft, nhưng NCSoft giữ quyền buộc đóng (B §5) |

**Nơi giá trị cao nhất gặp khả thi thấp nhất:** chức năng phần mềm và vận hành liên tục (game) có bằng chứng hành vi mạnh nhất, nhưng cũng là nơi rủi ro pháp lý cao nhất (B §11.6).
