# Task B: tài liệu quyết định

Run `2026-11-25-taskb-digital-preservation`, ngày 25/11/2026. Đọc khoảng 7 phút.

**Trạng thái:**

- Task B hoàn tất (Round 1 độc lập, Round 2 phản biện chéo, Round 3 tổng hợp). Đã dừng tại Exit Gate.
- Chưa chọn ý tưởng, chưa triển khai, chưa commit.
- Không so sánh với ứng viên Phase 2.

---

## 1. Quyết định cần anh/chị đưa ra

| # | Quyết định | Lựa chọn |
|---|---|---|
| G1 | Câu hỏi trung tâm đã bị ba agent phản bác độc lập (mục 2). Có chấp nhận phiên bản hẹp hơn không? | Chấp nhận / giữ câu hỏi gốc / dừng Task B |
| G2 | Cụm nào được đưa sang so với ứng viên Phase 2 (B-P1, A-P4, vị trí 3 còn hòa)? | Bất kỳ trong T1–T5, S1, S2, hoặc không cụm nào |
| G3 | Chạy phép thử kiểm chứng nào trước? (mục 5) | H0 rẻ nhất, khoảng 0,5 ngày; H1a, H5 khoảng 1–2 ngày |
| G4 | Xử lý T3 và T4, đang trượt cổng chủ đề theo chính agent chấm | Giữ làm nghiên cứu, không dùng cho Kiroween / sửa cách hiểu Resurrection (E3 vẫn mở) |
| G5 | Có xây sandbox bubblewrap cho các lần chạy worker sau? | Đã kiểm khả thi; anh/chị chưa chọn dùng |
| G6 | Cập nhật `progress/` theo `AGENTS.md` | Chưa sửa từ Phase 1 |

---

## 2. Phát hiện chính: câu hỏi trung tâm quá rộng

Câu hỏi: *"Có thể giữ giá trị do nền tảng số tạo ra khi chính nền tảng không còn sống được không?"*

Ba agent nghiên cứu độc lập (không đọc của nhau trong Round 1) và **cùng phản bác** những điểm sau. Chi tiết: [`problem-analysis.md` §1](../synthesis/problem-analysis.md).

- **Giá trị không phải là dữ liệu.** Hiệu ứng mạng đang sống của một cộng đồng không lưu trữ được.
- **Không phải nền tảng nào cũng đáng sống.** Hơn 70% game gacha Nhật đóng trong 3 năm (`B-G-C5`). Tài nguyên khoa học được trích dẫn nhiều phần lớn tự sống sót (A §11.2).
- **Ở các ca giá trị cao nhất, nút thắt là pháp lý, không phải kỹ thuật:** game online-only (DMCA §1201), sách số (Hachette v. Internet Archive).
- **Giữ nền tảng chết ở trạng thái chạy sống thường lặp lại đúng thất bại kinh tế đã giết nó.**
- **Chuẩn bị trước khi đóng rẻ hơn cứu sau khi đóng** (B, C).
- **Không tìm thấy ai trả tiền cho một công cụ bảo tồn mới.** Người ta trả cho nội dung và phí lưu trữ (quyên góp, GOG Preservation Program, phí PARADISEC), không trả cho công cụ (B, C).

Phiên bản đứng vững được (SUY LUẬN của Coordinator):

> Với **một số ít** nền tảng có cộng đồng hoặc giá trị chứng cứ rõ, **chuyển giao** một phần giá trị cụ thể sang chủ thể kế nhiệm **trước hoặc ngay khi** đóng cửa, **trong giới hạn pháp lý**.

---

## 3. Bản đồ cơ hội (không xếp hạng)

Chi tiết: [`opportunity-map.md`](../synthesis/opportunity-map.md). Bằng chứng rubric theo từng agent: [`rubric-evidence-table.md`](../synthesis/data/rubric-evidence-table.md).

| Cụm | Agent tìm ra | Bằng chứng mạnh nhất | Phản chứng mạnh nhất | Cổng chủ đề |
|---|---|---|---|---|
| **T1 · Kết thúc vòng đời game live-service** | **Cả ba**, độc lập | 1.294.188 chữ ký ECI; EC (16/06/2026) cam kết code of conduct end-of-life; Homecoming chạy bằng quyên góp | Chủ IP có quyền phủ quyết (ESA phản đối); AI không cần thiết theo 2/3 agent; feasibility 1–3 | Qua (4–5) |
| **T2 · Cửa sổ đóng cửa của nền tảng nhỏ/SaaS** | A, B | Cohost thâm hụt ~17.000 USD/tháng; ArchiveTeam phụ thuộc nhà vận hành hợp tác; EU Data Act | DTI/DTP, trình xem archive Mastodon; không thấy nhà vận hành trả tiền | Sát (3) |
| **T3 · Hồ sơ tạp chí học thuật nhỏ** | B, C (A liền kề) | 174 tạp chí OA biến mất (2000–2019); 27,64% DOI không xác nhận được bảo tồn | Hạ tầng đã có (PKP PN miễn phí); vấn đề là tham gia | **Trượt** (1) |
| **T4 · Chuyển giao kho di sản giữ quyền/ngữ cảnh** | A, C | Mukurtu protocols; ELAR đổi chủ trì | Nút thắt có thể là governance; A tự rút A-O5 vì trượt cổng | **Trượt** (1) |
| **T5 · Tái dựng/chạy lại phần mềm bị bỏ rơi** | A, B | Benchmark giải mã có LLM (B, chưa tái lập); khuyến nghị §1201 của US Copyright Office | Baseline `m2c` + `decomp-permuter`; demand của B-O5 là giả định, chỉ có bằng chứng ở Bắc Mỹ | Qua (3–5) |
| **S1 · Di sản nền tảng vùng đã chết** (keitai Nhật, web Trung Quốc thời đầu, Mxit) | B | Kahvibreak: brute-force CPRM, ktdumper. Bằng chứng hành vi mạnh **ở châu Á** | Pháp lý cao (DRM); người dùng là cộng đồng kỹ năng cao | Qua (5) |
| **S2 · Tĩnh hóa web app học thuật sau grant** | A | A ghi demand "demonstrated" ở ba vùng | Phần lớn nhãn bị A tự hạ; B đòi bằng chứng hành động 2025–2026 | Sát (3) |

**Ba điểm chung của cả bảng:**

- Sau phản biện, **không cơ hội nào có AI chịu tải đã được chứng minh**. B-O5 là ứng viên duy nhất, và chỉ ở mức giả thuyết.
- **Không cơ hội nào có bằng chứng người dùng sẵn sàng trả tiền cho công cụ.**
- Cụm có theme tốt nhất (T1, S1) cũng có rủi ro pháp lý cao nhất.

Liên hệ với Phase 2 (mô tả, không so sánh): T1 cùng cơ chế "server tắt thì sản phẩm đã mua chết" với B-P1; T2 cùng vùng với A-P4.

---

## 4. Giả định chưa được kiểm chứng

1. Có người trả tiền cho **công cụ** bảo tồn (H0). Hiện chưa có bằng chứng nào.
2. Nút thắt end-of-life game là thiếu chuẩn kỹ thuật, không chỉ IP. A và B bất đồng.
3. Export của nền tảng nhỏ mất ngữ nghĩa mà parser thông thường không khôi phục được (T2).
4. LLM tạo cải thiện đo được so với công cụ giải mã cổ điển (T5).
5. Bằng chứng quốc tế theo đúng người dùng mục tiêu. Agent C nhắc: không gộp nhu cầu keitai với Mxit, không lấy quỹ EU làm người mua ở Nhật.
6. Có artifact hoặc dữ liệu được phép dùng cho demo công khai, ở mọi cụm.

---

## 5. Phép thử kiểm chứng đề xuất

Chi tiết và điều kiện bác bỏ: [`hypotheses-validation-plan.md`](../synthesis/hypotheses-validation-plan.md).

| Thứ tự gợi ý theo chi phí | Phép thử | Bác bỏ điều gì | Công sức |
|---|---|---|---|
| 1 | **H0:** tìm một giao dịch hoặc hợp đồng mua công cụ bảo tồn trong từng cụm | Mô hình "sản phẩm" | ~0,5 ngày |
| 2 | **H1b:** lịch sử kế nhiệm maintainer của Pretendo và Homecoming | Hướng của C-O2 | ~0,5 ngày |
| 3 | **H1a:** phân loại rào cản của 20 game live-service đóng cửa 2024–2026 | Cách đặt vấn đề "chuẩn kỹ thuật" của T1 | 1–2 ngày |
| 4 | **H5:** tái lập benchmark giải mã có LLM so với `m2c` + `decomp-permuter` trên ≥30 hàm | AI chịu tải ở T5 | 1–2 ngày, có chi phí API |
| 5 | **H2:** 3–5 gói export thật, parser viết tay so với AI | AI ở T2 | 1–2 ngày, cần dữ liệu có quyền |

Còn khoảng 9 ngày đến hạn nộp. Các phép thử cần đối tác (H4 di sản, H7 keitai) khó làm kịp.

---

## 6. Bài học AI Engineering (tóm tắt)

Đầy đủ, có phân biệt đo được và suy luận: [`ai-engineering-lessons.md`](../synthesis/ai-engineering-lessons.md). Số liệu: [`execution-log.md`](../coordinator/execution-log.md).

- **Phản biện chéo đổi kết luận [đo được].** A hạ 24/27 nhãn VERIFIED, B hạ 12/20. Số cơ hội "AI chịu tải" giảm từ 3 xuống 1. Hai cơ hội bị rút.
- **Lệch nhãn theo model ổn định qua các phase [đo được].** A rộng tay, C chặt, B ở giữa. Gộp điểm nhiều model cần hiệu chuẩn.
- **Không nâng effort [đo được].** Mọi bất đồng còn lại cần bằng chứng mới, không cần suy luận sâu hơn.
- **Coordinator là bên tốn token nhất [đo được].** 20,9M token đầu vào trong 30 phút của Task B, so với 8–10M của mỗi worker cho cả hai round. Nguyên nhân là phiên dài mang lịch sử của mọi phase trước.
- **Không đo được token của Antigravity [đo được].** Log và DB của agy không có trường token.
- **Cô lập worker mới dựa vào chỉ dẫn [đo được].** Kiểm tra sau chạy sạch ở cả bốn lần. Sandbox bubblewrap đã được chứng minh khả thi nhưng chưa dùng.

---

## 7. Nguồn gốc

| Loại | Đường dẫn |
|---|---|
| Chỉ dẫn nguyên văn và quyết định | [`prompts/taskb-instructions.md`](../prompts/taskb-instructions.md) |
| Báo cáo độc lập (Round 1, khóa bằng hash) | [`agent-a/report.md`](../agent-a/report.md) · [`agent-b/report.md`](../agent-b/report.md) · [`agent-c/report.md`](../agent-c/report.md) |
| Phản biện chéo (Round 2) | [`agent-a/cross-review.md`](../agent-a/cross-review.md) · [`agent-b/cross-review.md`](../agent-b/cross-review.md) · [`agent-c/cross-review.md`](../agent-c/cross-review.md) |
| Tổng hợp | [`synthesis/`](../synthesis/): problem-analysis, stakeholder-analysis, alternatives-gap-analysis, opportunity-map, hypotheses-validation-plan, ai-engineering-lessons |
| Nhật ký kỹ thuật | [`coordinator/execution-log.md`](../coordinator/execution-log.md) |
