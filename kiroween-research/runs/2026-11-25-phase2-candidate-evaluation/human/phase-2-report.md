# Phase 2: đánh giá ứng viên — báo cáo kết quả

Run `2026-11-25-phase2-candidate-evaluation`, ngày 25/11/2026. Người đọc: chủ dự án. Người viết: Coordinator.

**Trạng thái:** Phase 2 hoàn tất (2A đánh giá độc lập → 2B tranh luận → 2C tổng hợp). Dừng chờ phê duyệt. Chưa chọn ý tưởng để xây, chưa commit.

Dữ liệu gốc (không sửa):

- `../agent-{a,b,c}/evaluation.md` và `scores.json`: Phase 2A, đã khóa bằng hash (`../coordinator/2a-outputs.sha256`);
- `../agent-{a,b,c}/debate.md` và `scores-revised.json`: Phase 2B;
- `../coordinator/analysis/`: script tổng hợp, kết quả JSON, bảng tiêu chí.

**Rubric này không phải tiêu chí chấm chính thức.** Nó không chấm mức dùng Kiro (20% điểm chính thức) và chỉ chấm một phần Design (20%). Top 3 dưới đây là khuyến nghị dựa trên bằng chứng theo rubric chọn ứng viên. Đây **không** phải dự đoán điểm giám khảo.

---

## 1. Kết luận

| Vị trí | Ứng viên | Mức chắc chắn | Điểm yếu lớn nhất, được cả ba agent thừa nhận |
|---|---|---|---|
| 1–2 | **A-P4** · Del.icio.us/Pocket → kho bookmark chống link rot | **Cao**: vào Top 3 ở 93–100% kịch bản nhiễu | **Innovation 1/2/1.** Obsidian Web Clipper, SingleFile, Karakeep, Linkwarden đã phủ phần lõi |
| 1–2 | **B-P1** · thiết bị bị brick khi tắt cloud | **Cao**: 89–96% kịch bản | **Feasibility 2/2/1.** Chưa có phần cứng và app gốc làm oracle; phương pháp `B·R01` chưa được tái lập |
| 3 | **Hòa, chưa phân xử được:** A-P1 (66,0) · A-P2 (66,0) · C-P1 (65,7) | **Thấp**: mỗi ứng viên chỉ vào Top 3 ở 28–44% kịch bản | Xem mục 4 |

- **Vị trí thứ 3 là hòa thống kê.** Chênh lệch 0,3 điểm trên thang 100 nhỏ hơn nhiều so với độ bất đồng giữa agent. Script tổng hợp xếp A-P1 thứ 3 chỉ vì thứ tự liệt kê khi hai ứng viên bằng điểm, không vì bằng chứng. Coordinator **không** chọn ứng viên thứ 3.
- **A-P1 và C-P1 là cặp trùng O1** (cùng người dùng, cùng đối thủ Feedly). Hai trong ba ứng viên tranh vị trí 3 thuộc cùng một vùng vấn đề.
- **Hai ứng viên trượt cổng chủ đề ở cả ba agent sau tranh luận:**
  - A-P7: Stack Overflow vẫn đang hoạt động;
  - C-P4: quản lý việc rút PSTN, không hồi sinh năng lực cũ.
  - Kết quả của C-P4 phụ thuộc cách hiểu E3. Nếu anh/chị chấp nhận "quản lý việc rút bỏ công nghệ" là Resurrection, C-P4 qua cổng. Tổng điểm 54,3 của C-P4 vẫn thấp hơn mọi ứng viên đang ở Top 3 hoặc vị trí hòa.

---

## 2. Điểm trước và sau tranh luận

Tổng weighted 0–100 theo từng agent, A/B/C.

| Ứng viên | 2A (trước) | 2B (sau) | Trung bình 2B | Cổng chủ đề (A/B/C sau 2B) |
|---|---|---|---|---|
| A-P1 | 70 / 63 / 65 | 70 / 63 / 65 | 66,0 | PASS / PASS / PASS |
| A-P2 | 61 / 66 / 71 | 61 / 66 / 71 | 66,0 | PASS ×3 |
| A-P4 | 76 / 69 / 71 | 73 / 72 / 71 | **72,0** | PASS ×3 |
| A-P7 | 61 / 57 / 59 | 58 / 57 / 55 | 56,7 | **FAIL ×3** |
| B-P1 | 81 / 75 / 64 | 76 / 77 / 64 | **72,3** | PASS ×3 |
| B-P4 | 60 / 61 / 56 | 60 / 61 / 56 | 59,0 | PASS ×3 |
| C-P1 | 66 / 64 / 67 | 66 / 64 / 67 | 65,7 | PASS ×3 |
| C-P4 | 52 / 59 / 60 | 49 / 57 / 57 | 54,3 | **FAIL ×3** (2A: PASS / FAIL / PASS) |

Điểm từng tiêu chí sau 2B (A/B/C):

| Ứng viên | demand | international | innovation | theme | ai | feasibility | demo | sustainability |
|---|---|---|---|---|---|---|---|---|
| A-P1 | 3/2/3 | 4/3/3 | 2/2/1 | 4/5/5 | 3/3/3 | 5/4/4 | 4/4/4 | 4/3/4 |
| A-P2 | 3/3/3 | 3/3/4 | 2/2/2 | 4/4/5 | 3/3/4 | 3/4/3 | 4/5/4 | 2/3/4 |
| A-P4 | 4/3/4 | 4/4/4 | 1/2/1 | 5/5/4 | 3/3/3 | 5/5/5 | 4/4/4 | 3/3/4 |
| A-P7 | 2/2/3 | 4/4/3 | 2/2/1 | 2/2/2 | 4/4/3 | 5/4/4 | 3/3/4 | 2/3/3 |
| B-P1 | 4/4/4 | 4/4/3 | 3/3/2 | 5/5/4 | 4/5/5 | 2/2/1 | 4/4/3 | 4/3/3 |
| B-P4 | 3/3/3 | 3/3/3 | 3/3/3 | 4/4/3 | 3/3/3 | 2/2/1 | 3/3/3 | 2/3/3 |
| C-P1 | 3/2/3 | 4/3/3 | 2/2/2 | 3/4/4 | 3/4/4 | 5/5/4 | 4/4/4 | 3/3/4 |
| C-P4 | 3/4/4 | 3/3/3 | 2/2/2 | 2/2/2 | 2/2/2 | 2/3/3 | 3/3/3 | 2/4/4 |

Hai quan sát từ bảng:

- **Innovation thấp gần như toàn bộ** (1–3, đa số 2). Ở cả 8 ứng viên, đối thủ hiện có đã phủ phần lớn việc cốt lõi. Không ứng viên nào đạt innovation 4 sau tranh luận.
- **Hai ứng viên dẫn đầu dẫn theo hai lý do ngược nhau.** A-P4 dễ làm (feasibility 5/5/5) nhưng ít khác biệt. B-P1 có AI chịu tải và nhu cầu mạnh nhất (demand 4/4/4, ai 4/5/5) nhưng khó làm kịp (feasibility 2/2/1).

---

## 3. Phân tích độ nhạy

Script: `../coordinator/analysis/aggregate.py`, seed cố định. Kết quả đầy đủ: `aggregate-results.json`.

| Kịch bản | Top 3 | Khác cơ sở? |
|---|---|---|
| Cơ sở (trung bình ba agent, trọng số gốc, có cổng) | B-P1, A-P4, *(hòa: A-P1 / A-P2 / C-P1)* | — |
| Trung vị thay trung bình | B-P1, A-P4, A-P1 | Giữ Top 2 |
| Trọng số bằng nhau | A-P4, B-P1, A-P1 | Giữ Top 2 |
| Bỏ cổng chủ đề | B-P1, A-P4, A-P1 | Không đổi (A-P7 và C-P4 vốn điểm thấp) |
| Từng trọng số ±5 điểm % (16 kịch bản) | 7/16 thay vị trí 3 bằng A-P2; 1/16 bằng C-P1 (theme −5) | **Chỉ vị trí 3 đổi** |
| Bỏ hẳn một tiêu chí (8 kịch bản) | 3/8 đổi vị trí 3 (theme → C-P1; feasibility, sustainability → A-P2) | **Chỉ vị trí 3 đổi** |
| Top 3 riêng của từng agent | A: B-P1, A-P4, A-P1 · B: B-P1, A-P4, A-P2 · C: A-P2, A-P4, C-P1 | C không xếp B-P1 vào Top 3 |

Tần suất vào Top 3 qua 20.000 lần mô phỏng mỗi loại:

| Ứng viên | Nhiễu trọng số (Dirichlet, α=40) | Nhiễu điểm (mỗi tiêu chí lấy ngẫu nhiên điểm của một agent) | Nhiễu cả hai, thêm ±1 ở ô độ tin cậy L |
|---|---|---|---|
| A-P4 | 99,9% | 95,6% | 92,9% |
| B-P1 | 96,0% | 95,7% | 89,0% |
| A-P1 | 35,0% | 43,6% | 40,9% |
| A-P2 | 40,4% | 35,3% | 37,1% |
| C-P1 | 28,5% | 29,8% | 36,9% |
| B-P4 | 0,2% | 0% | 3,3% |
| A-P7, C-P4 | 0% | 0% | 0% |

**Kết luận độ nhạy:**

- Thay đổi trọng số hợp lý **không** làm đổi Top 2.
- Vị trí thứ 3 đổi dễ dàng theo cả trọng số lẫn bất đồng điểm. Không thể khẳng định vị trí 3 từ dữ liệu hiện có.

---

## 4. Thứ cần để phân xử vị trí thứ 3

Các phép thử dưới đây do agent đề xuất trong `debate.md` §5.

| Ứng viên | Điểm then chốt chưa rõ | Phép thử phân xử |
|---|---|---|
| A-P1 | **Tiền lệ GhostPipes**: dự án Kiroween 2025 có thể đã làm visual pipes kèm AI node. Agent không mở được trang Devpost (403). | Mở trang Devpost của GhostPipes trên trình duyệt của anh/chị. Nếu đã có canvas trực quan cùng AI lọc và trích web, innovation của A-P1 sẽ xuống 1. |
| A-P2 | Microsoft Copilot Vision Highlights đã phủ phần lõi (A, B, C cùng ghi) | So 5 tác vụ giữa lớp phủ DOM và Copilot Vision Highlights. Kiểm giới hạn theo vùng (EU) và theo gói trả phí. |
| C-P1 | Feedly dedup bật mặc định; khoảng trống "so sánh phần thay đổi" chưa được benchmark | 3 người, 30–50 bài, so với Feedly/Inoreader |

A-P1 và C-P1 có thể được xét **gộp** (quyết định E2 từ Phase 1.5, vẫn mở).

---

## 5. Tranh luận: điều đã đổi, điều còn bất đồng

### 5.1 Điểm đã đổi (13 thay đổi)

| Agent | Ứng viên · tiêu chí | Đổi | Do ai thúc đẩy | Lý do (tóm tắt) |
|---|---|---|---|---|
| A | A-P4 · innovation | 2 → 1 | C | Obsidian Web Clipper và SingleFile (AGPL, mở trực tiếp) phá thế lưỡng nan "SaaS hay tự host" |
| A | A-P7 · innovation | 3 → 2 | C | Stack Overflow for Agents (16/09/2026) đã lưu TIL/Playbook gỡ lỗi |
| A | B-P1 · innovation | 4 → 3 | B | Bose công bố tài liệu API SoundTouch; Home Assistant/pywemo đã có |
| A | B-P1 · feasibility | 3 → 2 | B | Chưa có phần cứng và app gốc; quy trình `B·R01` chưa tái lập |
| A | C-P4 · theme | 3 → 2 | B | Anchor 3 cần cả "retirement" lẫn "revived capability" |
| B | A-P4 · international | 3 → 4 | C | Các ca ở cả ba vùng: Hatena (Nhật), OPCUG (Canada), wallabag (châu Âu) |
| B | A-P7 · international | 3 → 4 | A | Tự gọi API: ja.stackoverflow 4 và ru.stackoverflow 36 câu hỏi tháng 10/2026 |
| B | A-P7 · innovation | 3 → 2 | C | Stack Overflow for Agents |
| B | B-P1 · ai | 4 → 5 | C | Áp lại anchor: AI chịu tải, có oracle, có cơ chế được công bố |
| B | C-P4 · international | 4 → 3 | tự sửa | Bằng chứng Bắc Mỹ chỉ là snippet; không được vượt 3 |
| B | C-P4 · sustainability | 3 → 4 | C | Biên bản Hillingdon: hợp đồng ARC £235.364/12 tháng |
| C | A-P7 · demand | 4 → 3 | B | Khảo sát thái độ chưa phải bằng chứng hành vi |
| C | C-P4 · theme | 3 → 2 | B | Phiếu bàn giao chỉ quản lý migration, chưa phục hồi năng lực của PSTN |

Không agent nào đổi điểm của A-P1, A-P2, B-P4 hay C-P1.

### 5.2 Bất đồng còn lại (giữ nguyên, không ép đồng thuận)

| Bất đồng | A / B / C | Bằng chứng sẽ phân xử |
|---|---|---|
| B-P1 · innovation | 3 / 3 / 2 | Một model thiết bị cụ thể chưa có integration Home Assistant hay No Longer Evil, còn app gốc chạy được. Không tìm ra trong 1–2 ngày thì khoảng trống chỉ còn trên giấy (B). |
| B-P1 · feasibility | 2 / 2 / 1 | **Thử 48 giờ:** ghi trace trên phần cứng thật, cho AI suy một lệnh read-only, replay khớp oracle. Thành công → 3, thất bại → 1 (cả ba agent đề xuất). |
| A-P7 · demand | 2 / 2 / 3 | Bằng chứng hành vi đóng góp (số bài TIL/Playbook, tỷ lệ chịu xuất bản qua rào NDA) |
| A-P2 · sustainability | 2 / 3 / 4 | Một tổ chức trả tiền cho hướng dẫn phía người dùng, không do vendor tích hợp |
| C-P4 · sustainability | 2 / 4 / 4 | Ngân sách riêng cho bàn giao/đối soát sau 31/01/2027 |
| A-P4 · demand | 4 / 3 / 4 | Đo trên export Pocket thật: tỷ lệ link cần dùng lại đã "chết mềm" mà công cụ hiện có không báo |
| C-P4 · theme | 2 / 2 / 2 | **Không phải bằng chứng: quyết định E3** của anh/chị |

### 5.3 Lập luận phản bác mạnh nhất với hai ứng viên dẫn đầu

- **A-P4.** Nhiều công cụ miễn phí đã lưu trang cục bộ (SingleFile, Obsidian Web Clipper) và tự host (Karakeep, Linkwarden). Phần còn lại là phát hiện link "chết mềm" (trang vẫn trả 200 nhưng đã thành trang đỗ hoặc spam). Chưa có agent nào kiểm Linkwarden/Karakeep có làm việc này hay không. Nếu có, innovation còn 1 ở cả ba agent.
- **B-P1.** Thiết bị dễ demo nhất (Wemo, SoundTouch) đã có integration cục bộ. Thiết bị chưa có integration thì đội thi chưa có trong tay. Phương pháp chính tốn "billions of model tokens" và chưa được tái lập. Feasibility 2/2/1 là đồng thuận, không phải bất đồng.

---

## 6. Phạm vi quốc tế (theo yêu cầu International Market Orientation)

Tóm tắt từ `evaluation.md` và `debate.md`. Chi tiết theo vùng nằm trong từng báo cáo.

- **A-P4:** có ca trực tiếp ở cả ba vùng (Hatena Nhật, OPCUG Canada, wallabag châu Âu). International 4/4/4.
- **B-P1:** có bằng chứng 2025–2026 ở nhiều vùng: Belkin Wemo, Bose SoundTouch, Futurehome (Na Uy), FTC (Mỹ); Home Assistant có telemetry ở 212 quốc gia. Agent B ghi **ca brick ở châu Á vẫn là câu hỏi mở**.
- **A-P7:** sụt giảm có ở cả site tiếng Nhật và tiếng Nga (tái lập qua API), nhưng ứng viên trượt cổng chủ đề.
- **C-P4:** bằng chứng mở trực tiếp chủ yếu ở châu Âu (Anh, Pháp). Bắc Mỹ chỉ có snippet.

---

## 7. Giới hạn

- **Không ứng viên nào có bằng chứng người dùng trực tiếp** (phỏng vấn, quan sát). Demand cao nhất là 4, từ bằng chứng hành vi thứ cấp.
- **Một vòng tranh luận đồng thời.** Agent không phản hồi được phản bác nhắm vào mình. Một số bảng "bất đồng còn lại" ghi điểm cũ của agent khác (ví dụ A vẫn ghi C-P4 theme của C = 3 trong khi C đã hạ về 2). Bảng ở mục 5.2 dùng điểm thực tế trong `scores-revised.json`.
- **Chất lượng nguồn.** B ghi 38/50 tham khảo 2A chỉ là snippet. Ở 2B, B mở trực tiếp toàn bộ 13 nguồn mới. Quy tắc "snippet không đủ để vượt 3" chỉ áp dụng từ 2B.
- **Thiên lệch tổng hợp.** Coordinator chạy cùng model với Agent B. Coordinator không chấm điểm ứng viên ở Phase 2, chỉ tổng hợp điểm của ba agent.
- **An toàn thực thi.** Ba worker chạy không sandbox theo lựa chọn của anh/chị. Kiểm tra sau chạy:
  - không tệp nào ngoài thư mục agent bị sửa;
  - tệp 2A không đổi sau tranh luận;
  - không thấy agent đọc thư mục của agent khác trong 2A.
- **Quota.** Trước Phase 2, Codex đã dùng 66% quota tuần.

---

## 8. Quyết định cần anh/chị đưa ra

| # | Quyết định | Ghi chú |
|---|---|---|
| F1 | Chấp nhận Top 2 (A-P4, B-P1) làm đầu vào cho bước tiếp theo? | Cả hai đều có điểm yếu được đồng thuận: innovation của A-P4, feasibility của B-P1 |
| F2 | Phân xử vị trí 3 thế nào? | (a) chạy các phép thử ở mục 4 · (b) gộp A-P1 và C-P1 (E2) rồi chấm lại · (c) anh/chị chọn theo phán đoán, được ghi là phán đoán của người |
| F3 | E3: "quản lý việc rút bỏ công nghệ" có tính là Resurrection? | Chỉ ảnh hưởng gate của C-P4; không đổi Top 3 vì điểm C-P4 thấp |
| F4 | Thời gian | Còn khoảng 9 ngày đến 04/12/2026 14:00 PT. Thử 48 giờ cho B-P1 sẽ dùng khoảng một phần tư thời gian còn lại. |
| F5 | Task B (di sản số, cộng đồng trực tuyến sắp mất) | Đã định nghĩa là track riêng, chưa chạy |
| F6 | Cập nhật `progress/` theo `AGENTS.md` | Coordinator chưa sửa từ Phase 1 |
