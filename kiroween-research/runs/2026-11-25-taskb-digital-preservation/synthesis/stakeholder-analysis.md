# Phân tích bên liên quan — Task B

Bảng gốc nằm ở §3 của từng báo cáo: [`A`](../agent-a/report.md), [`B`](../agent-b/report.md), [`C`](../agent-c/report.md). Tài liệu này chỉ hợp nhất và phân loại theo **loại nhu cầu**.

## 1. Nhu cầu đã chứng minh và nhu cầu giả định

"Đã chứng minh" nghĩa là có hành vi quan sát được (ký, quyên góp, giờ tình nguyện, chi tiêu, chuyển đổi). Ý kiến hay khảo sát thái độ không tính.

| Bên liên quan | Ví dụ cụ thể | Hành vi đã chứng minh | Sẵn sàng **trả tiền**? | Nguồn |
|---|---|---|---|---|
| Người chơi game online-only (EU) | 1.294.188 chữ ký ECI "Stop Destroying Videogames" | Ký kiến nghị (chính sách) | **Không chứng minh.** Chữ ký không phải willingness to pay | C §3; B §3 (`B-O1`) |
| Cộng đồng hồi sinh game | Homecoming (City of Heroes), Pretendo (3DS/Wii U) | Tự chạy server nhiều năm; "funded every month by the playerbase"; 170 repo GitHub (Pretendo) | **Quyên góp** cho hosting, không mua công cụ | B §3; A §5.7; C-O2-C2 |
| Nhóm bảo tồn kỹ thuật châu Á | Kahvibreak / Keitai Wiki | Brute-force khóa CPRM 20 ngày GPU, desolder eMMC | Không | B §3 (`B-O4`) |
| Tình nguyện viên lưu trữ khẩn cấp | ArchiveTeam (Cohost, Glitch) | Chạy warrior và ArchiveBot trước hạn đóng | Không; Internet Archive lưu | B §3 (`B-O2-C3`) |
| Nhà vận hành nền tảng nhỏ | Cohost (ASSC), Glitch (Fastly) | Xây export, giữ server thêm cho ArchiveTeam | Giới hạn bởi tiền; **không ai trả cho họ** | B §3, §6 |
| Nhà phát hành game | ESA, NCSoft | Phản đối miễn trừ truy cập từ xa (ESA); một lần cấp license miễn phí (NCSoft) | — | B §3 |
| Thư viện, GLAM, tổ chức di sản | Yale EaaSI, VGHF, SPN, Archive-It, PARADISEC, ELDP/ELAR | Mua Archive-It; nhận grant (Yale 3,5 triệu USD từ Mellon/Sloan); thu phí lưu trữ (PARADISEC) | **Có ngân sách tổ chức**, chủ yếu qua grant và phí thành viên | A §3; B §6; C §3, §6 |
| Tạp chí OA nhỏ, biên tập viên OJS | Texas Digital Library | Bật plugin PKP PN (miễn phí) | PKP PN miễn phí cho tạp chí | C §3 (`C-O1`) |
| Nhà nghiên cứu, web app học thuật | Phòng lab tin sinh học, dự án Digital Humanities | Web app chết sau grant (A) | **Giả định** | A §3 (`A-O1`) |
| Cộng đồng bản địa / nguồn | Người giữ cultural protocols (Mukurtu); Kulu Language Institute (Ranongga) | Mang kho ghi âm về cộng đồng; thử Raspberry Pi | Grant số hóa; không có dòng doanh thu | C §3 (`C-O3`) |
| Tổ chức di sản quốc gia | NDL (Nhật), NLK (Hàn), NLB (Singapore) | Lưu chiểu web theo luật | Ngân sách công | A §3 |

## 2. Ai trả tiền, ai hưởng lợi, ai bảo trì

Nguồn: §6 của ba báo cáo.

- **Hưởng lợi:** khuếch tán (người chơi, nhà nghiên cứu, cộng đồng, công chúng). SUY LUẬN, B §6.
- **Trả tiền** (theo nguồn đã mở, nhãn sau Round 2):
  - quỹ tư nhân và grant (Yale EaaSI);
  - quyên góp của người dùng (Homecoming, Internet Archive);
  - phí thành viên hoặc phí lưu trữ (PARADISEC, Archive-It).
- **Không ai trả** cho nhà vận hành sắp chết (Cohost, B §6).
- **Bảo trì:** tình nguyện viên kỹ năng cao và tổ chức phi lợi nhuận (B §6; C §6, failure mode "burnout").
- **Chi phí liên tục:** Internet Archive chi 23,5–32,7 triệu USD/năm, theo Form 990 (B §6, `R20`).

**Phát hiện then chốt, đồng thuận sau Round 2 giữa B và C, A không phản đối:**

- Có người trả tiền cho **nội dung đã được bảo tồn** và cho **phí lưu trữ** (quyên góp, GOG Preservation Program, phí PARADISEC).
- **Không** tìm thấy bằng chứng có người trả tiền cho **một công cụ bảo tồn mới** (B, cross-review; C §11.3).
- Ảnh hưởng: tiêu chí `sustainability` của mọi cơ hội dạng "sản phẩm" là yếu. Mô hình khả thi nhất là tổ chức, grant hoặc cộng đồng, không phải SaaS.

## 3. Ma trận quyền lực và lợi ích (SUY LUẬN của Coordinator)

|  | Lợi ích **cao** từ bảo tồn | Lợi ích **thấp** hoặc ngược chiều |
|---|---|---|
| **Quyền cao** | Thư viện và tổ chức di sản quốc gia; Ủy ban châu Âu (đặt code of conduct, B: phản hồi EC 16/06/2026) | **Nhà phát hành game, chủ IP** (giữ thị trường re-release, rủi ro pháp lý) |
| **Quyền thấp** | Cộng đồng hồi sinh, tình nguyện viên lưu trữ, người chơi, cộng đồng nguồn | Nhà vận hành nhỏ sắp đóng (muốn đóng rẻ nhất) |

**Hệ quả:** các ca có lợi ích xã hội lớn nhất (game) có bên giữ quyền phủ quyết mạnh nhất (chủ IP). Nhà vận hành nhỏ sắp đóng có quyền với dữ liệu và động cơ hợp tác, nhưng không có tiền. Đây là điểm đòn bẩy "trước khi chết" mà B và C cùng nêu.
