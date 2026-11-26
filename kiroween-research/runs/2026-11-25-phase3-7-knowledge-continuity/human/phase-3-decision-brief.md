# Phase 3: tài liệu quyết định

Run `2026-11-25-phase3-7-knowledge-continuity`, ngày 25/11/2026. Đọc khoảng 5 phút.

**Trạng thái:**

- Phase 3 hoàn tất, đã dừng tại cổng duyệt.
- Phase 4 chưa chạy. Chưa chọn ý tưởng, chưa triển khai, chưa commit.
- Phê duyệt "Accept risk, scoped" chỉ áp dụng cho Phase 3. Phase 4 cần anh/chị duyệt lại.

---

## 1. Quyết định cần anh/chị đưa ra

| # | Quyết định | Lựa chọn |
|---|---|---|
| P3-1 | Chạy Phase 4 (phản biện chéo)? Nếu có, chế độ an ninh nào? | Accept risk, scoped / xây sandbox bwrap trước / dừng |
| P3-2 | Phase 4 phản biện những mục nào? | Cả 16 mục, kể cả mục bị drop (Coordinator đề xuất), hoặc chỉ các mục `narrow` và `continue` |
| P3-3 | Có chấp nhận rằng chỉ các nhánh **hẹp gắn công nghệ đã khai tử** mới còn cơ hội qua cổng chủ đề không? | Chấp nhận / giữ ô dù rộng (khi đó T3, T4 tiếp tục trượt cổng) |
| P3-4 | Ngân sách thời gian: còn khoảng 9 ngày, với 4 cổng duyệt nữa | Giữ đủ 4 phase / gộp Phase 5 vào Phase 4 / khác |
| G6 | Cập nhật `progress/` theo `AGENTS.md` | Vẫn chưa sửa từ Phase 1 |

---

## 2. Phát hiện chính

Ba agent nghiên cứu độc lập, không đọc chéo (đã kiểm transcript), và **cùng đi đến bốn kết luận**:

1. **Câu hỏi ô dù đúng khi dùng để mô tả, nhưng quá rộng để hành động.** "Thiếu nguồn lực" gom nhiều thứ khác nhau vào một chỗ: cắt tài trợ vì chính trị (FlyBase 2025), quyết định của tập đoàn (Glitch), ban biên tập tình nguyện kiệt sức, và công nghệ bị khai tử (Drupal 7). Mỗi loại có người trả tiền và cách xử lý riêng (`B-G-C1`, `C-G-C2`).
2. **Gộp bốn không gian thành một sản phẩm là sai.** Mục tiêu bảo tồn của chúng xung đột nhau: T3 mặc định công khai, còn T4 mặc định hạn chế theo cultural protocol, nên một bản sao công khai ở T4 là có hại (`A-G-C3`, `B-G-C3`, `C-G-C3`).
3. **Vẫn chưa thấy ai trả tiền cho một công cụ bảo tồn của bên thứ ba.** Chi tiêu có thật đều đi vào dịch vụ và con người: SLA của King's Digital Lab, subscription của TAIR, phí CLOCKSS, grant Arcadia, hợp đồng HeroDevs cho Drupal 7. H0 của Task B vẫn đứng (`B-G-C5`, `A-G-C2`, `C-G-C4`).
4. **Một không gian chỉ có mỏ neo Resurrection hợp lệ khi được thu hẹp về một công nghệ cụ thể đã khai tử chính thức.** B gọi đây là cơ chế chung hẹp hơn: một runtime bên ngoài bị khai tử, và chi phí di trú đổ lên người giữ ít nguồn lực (`B-G-C2`).

Mỏ neo mà các agent hội tụ là **Flash, Java applet và các runtime đã khai tử** đứng sau công cụ nghiên cứu và tác phẩm học thuật tương tác (A-S2a, B-S2a, C-T3a). Hai điểm cần lưu ý thẳng thắn:

- Ruffle (Flash) và CheerpJ (Java applet) là đối thủ mạnh. B và C đều nêu ra, nhưng **chưa ai đo** phần việc còn thiếu sau khi đã dùng chúng.
- Flash/SWF nằm trong danh sách "đã khám phá" của Task B. Phase 3 không nhận danh sách này (Coordinator chọn vậy), nên các agent không biết mình đang quay lại vùng cũ. Góc mới ở đây là *công cụ nghiên cứu sau grant*, không phải Flash nói chung.

---

## 3. Verdict từng không gian

Chi tiết: [`execution-log.md` §3](../coordinator/execution-log.md). Điểm `theme` là điểm tạm do agent tự chấm theo anchor Phase 2, chưa phải điểm đánh giá.

| Không gian | A | B | C | Đồng thuận |
|---|---|---|---|---|
| **S2 · Web app nghiên cứu sau grant** | narrow: tĩnh hóa/WASM app trên runtime đã khai tử (theme 3) | narrow → **B-S2a**: công cụ Flash, Java applet, Fusion Tables (theme 3, continue) | narrow: bàn giao chức năng (theme **1**, không có mỏ neo) | Cả ba giữ, nhưng bất đồng về theme |
| **T2 · Cửa sổ đóng cửa nền tảng nhỏ** | narrow: cầu export trước khi tắt (theme 3; không có payer; AI không cần) | **drop**: lúc cần công cụ cũng là lúc không ai trả được tiền | narrow: Glitch retirement (theme 3, có điều kiện, độ tin cậy thấp) | **Bất đồng** |
| **T3 · Tạp chí biến mất** | **drop** (theme 1) | narrow → **B-T3a**: tạp chí kẹt trên OJS 2.x (EOL 2021) (theme 2, có điều kiện) | drop; nhánh **C-T3a**: học thuật tương tác dựa trên Flash như Vectors (theme 3, demand 1) | T3 chung trượt cổng theo cả ba |
| **T4 · Chuyển giao kho di sản** | **drop** (theme 1; Drupal 7 → Mukurtu 4 chỉ là migration thường, ≤ 2) | narrow → **B-T4a**: Mukurtu 3 tùy biến trên Drupal 7 (theme 3, continue) | **drop** (theme 1) | 2/3 drop; B giữ một nhánh hẹp |

**Phản chứng mạnh nhất cho từng nhánh còn sống:**

- **S2a:** Wren (2017) cho thấy công cụ được trích dẫn nhiều phần lớn tự sống sót. KDL báo cáo nhiều PI tự chọn để dự án chết gọn.
- **T2:** Cohost thâm hụt khoảng 17.000 USD/tháng. Không có payer ở thời điểm tắt, và các đối thủ còn sống tự xây importer.
- **B-T3a:** OJS 2.x không phải lý do chính khiến tạp chí biến mất. Chưa ai đếm số tạp chí còn chạy OJS 2.x.
- **B-T4a:** chưa biết số site Mukurtu 3 tùy biến. Đội Mukurtu có tài trợ và đã hỗ trợ migration tùy biến.
- **C-T3a:** nhu cầu 2025–2026 chưa xác nhận. Ruffle có thể đã đủ.

---

## 4. Câu hỏi còn mở (đầu vào cho Phase 4)

1. Sau Ruffle và CheerpJ, bao nhiêu công cụ học thuật Flash/applet vẫn không chạy được? Phép thử B đề xuất: lấy 20 công cụ, drop nếu ≥ 80% đã chạy đủ.
2. Drupal 7 → Mukurtu 4: là Resurrection hợp lệ (B) hay migration CMS thông thường (A)? Đây là bất đồng về diễn giải anchor trên cùng bằng chứng, loại duy nhất mà nâng effort có thể đáng.
3. Bao nhiêu tạp chí còn chạy OJS 2.x, và bao nhiêu site Mukurtu 3 còn sống?
4. T2: có nhà vận hành hay quỹ nào từng trả tiền cho việc chuyển giao cộng đồng lúc đóng cửa không?
5. Bằng chứng châu Á còn mỏng ở mọi không gian.
6. A gắn VERIFIED cho 59% claim, B và C khoảng 36–37%. A vẫn rộng tay nhất, dù đã giảm so với Task B (90%).

---

## 5. Số liệu kỹ thuật

| Agent | Thời gian | Token đầu vào (cache) | Token đầu ra | Claim V/I/H/U | Nguồn mở trực tiếp / snippet |
|---|---|---|---|---|---|
| A · gemini-4-neon-medium | ~13 phút | không đo được | không đo được | 20/13/1/0 | 27 / 7 |
| B · claude-sonnet-5-5, medium | 9 phút 32 giây | 3,25M (3,08M cache) | 66,8k | 18/22/5/4 | 23 / 14 |
| C · gpt-6.1-sol, medium | 14 phút 57 giây | 7,26M (6,99M cache) | 34,0k | 24/34/4/4 | 45 / 3 |

- **Kiểm tra toàn vẹn sạch:** không tệp trước-launch nào đổi, ngoài log của Coordinator. Không có ghi ngoài thư mục agent, không đọc chéo. Output đã khóa bằng hash (`p3-outputs.sha256`).
- **Không nâng effort.**
- **Bất thường:** log agy của A ghi lỗi "model gemini-4-neon-medium is not recognized" lúc khởi động, rồi một giây sau lại áp dụng "Gemini 4 Neon (Medium)". Coordinator suy luận model đúng đã được dùng, nhưng agy không ghi model theo từng request, nên đây vẫn là khoảng trống quan sát.
- **Lỗi truy cập nguồn:** drupal.org, Adobe, EUR-Lex, tài liệu Mukurtu và JLSC bị chặn hoặc trả lỗi. Vì vậy một số claim quan trọng, như ngày EOL của Drupal 7, mới ở mức snippet.

---

## 6. Nguồn gốc

| Loại | Đường dẫn |
|---|---|
| Chỉ dẫn nguyên văn và quyết định | [`prompts/cycle-instructions.md`](../prompts/cycle-instructions.md) |
| Brief và hợp đồng đầu ra | [`brief-phase3.md`](../brief-phase3.md) |
| Kế hoạch Phase 3–7 | [`coordinator/workflow-plan.md`](../coordinator/workflow-plan.md) |
| Báo cáo agent (khóa bằng hash) | [`agent-a/report.md`](../agent-a/report.md) · [`agent-b/report.md`](../agent-b/report.md) · [`agent-c/report.md`](../agent-c/report.md) |
| Dữ liệu cơ hội | `agent-{a,b,c}/opportunities.json` |
| Nhật ký kỹ thuật | [`coordinator/execution-log.md`](../coordinator/execution-log.md) |
