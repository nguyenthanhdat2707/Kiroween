# Phase 2A Evaluation — Agent B

## Metadata

| Mục | Giá trị |
|---|---|
| Run | `2026-11-25-phase2-candidate-evaluation`, Phase 2A, Agent B |
| Model | `claude-sonnet-5-5`. Đọc từ `/proc/25696/cmdline`: `claude --dangerously-skip-permissions --model claude-sonnet-5-5 --effort high` |
| Effort | `high` (cùng nguồn trên) |
| Bắt đầu (UTC) | 2026-11-25T11:07:05Z (giờ khởi động tiến trình, `ps -o lstart`) |
| Kết thúc (UTC) | 2026-11-25T11:20:18Z |
| Tìm kiếm | 32 lượt WebSearch (8 đợt × 4) và 16 URL mở trực tiếp qua công cụ fetch, chạy trong 2 lần gọi agent `web-fetch`. Môi trường này không có WebFetch trực tiếp; `web-fetch` là công cụ thay thế, không phải worker phụ. |
| Lỗi truy cập | TechSpot Wemo: HTTP 403. infrastructure.gov.au (3G): timeout 2 lần. TGA (3G): timeout 2 lần. PTS Thụy Điển (`pts.se/.../copper/`): HTTP 404. Trang MIC Nhật mở được nhưng chữ Nhật bị lỗi mã hóa. Trang GOV.UK "Moving landlines…" **không** chứa câu "over 300 known use cases" mà snippet tìm kiếm gán cho nó, nên tôi không dùng câu đó. Trích dẫn Belkin lấy từ phần trang mà công cụ fetch tóm tắt, không phải nguyên văn tôi tự đọc. |
| Đầu vào đã đọc | `AGENTS.md`, `brief.md`, `rubric-and-anchors.md`, `prompts/phase-2-instructions.md`, `prompts/agent-b-2a-spec.md`; các mục ứng viên trong `P1/agent-{a,b,c}/discovery.md`; `P1/quality-gate/{corrections-overlay,claim-verification,overlaps,calibration,human-shortlist,README}.md`. **Không** đọc `agent-a/`, `agent-c/` của run này. |
| Skill | Không nạp `idea-red-team` hay `user-problem-validation`. Tôi áp dụng thủ công nguyên tắc của chúng: tìm phản chứng mạnh nhất và tách bằng chứng vấn đề khỏi bằng chứng muốn giải pháp. Không dùng BMAD. |
| Tham chiếu mới | 50 (`B2-R01` … `B2-R51`; `B2-R45` bỏ trống sau khi loại một nguồn SEO). 12 nguồn mở trực tiếp, 38 nguồn chỉ thấy qua snippet. |

## 1. Method

1. **Đọc đầu vào theo thứ tự bắt buộc.** Mọi claim Phase 1 được coi là claim cần kiểm, không phải sự thật. Khi `corrections-overlay.md` sửa nhãn, tôi dùng nhãn đã sửa và ghi cả nhãn gốc, ví dụ "A-P1-C2 (tách)".
2. **Bổ sung đúng 6 mảng mà brief §3 yêu cầu** cho cả 8 ứng viên: quốc tế, nhu cầu, thương mại, đối thủ, khả thi, câu pitch. Tìm kiếm dùng tiếng Anh, tiếng Nhật và tiếng Trung. Mỗi ứng viên có ít nhất một truy vấn nhắm riêng vào châu Á, vì Phase 1 thiên về nguồn Mỹ/Anh.
3. **Ưu tiên kiểm phản chứng có thể đổi điểm.** Ví dụ: Copilot Vision Highlights với A-P2, Feedly dedup với C-P1, Bose công bố API với B-P1, và doanh thu kỷ lục của Stack Overflow với theme của A-P7.
4. **Nhãn.** ĐÃ XÁC MINH chỉ dùng khi có nguồn gốc đã mở cộng xác nhận độc lập, hoặc phép kiểm tái lập. Nguồn chỉ thấy qua snippet tối đa là SUY LUẬN, dù nhiều snippet khớp nhau.
5. **Chấm điểm.** Dùng anchor và trọng số trong `rubric-and-anchors.md`, không đổi. `weighted_total` = Σ trọng số × điểm / 5, tính bằng script `scratch/build_scores.py`. Điểm 2 và 4 nằm giữa các anchor 1, 3, 5.
6. **Giới hạn.** Không có phỏng vấn hay quan sát người dùng. Tìm kiếm chỉ chạy từ Mỹ (công cụ ghi "US-only"), nên kết quả châu Âu lục địa và châu Á có thể thiếu. Chất lượng điểm reference của tôi có thiên lệch đã biết là chấm thấp (`calibration.md`: offset B −5,1). Tôi không tự hiệu chỉnh điểm này.

## 2. Score table

Bảng chỉ để tham khảo. **Không phải xếp hạng** và không phải dự đoán điểm của giám khảo (rubric §1).

| ID | demand (20) | international (15) | innovation (15) | theme (15) | ai (10) | feasibility (10) | demo (10) | sustainability (5) | Weighted total | Theme gate (≥3) |
|---|---|---|---|---|---|---|---|---|---|---|
| A-P1 | 2 | 3 | 2 | 5 | 3 | 4 | 4 | 3 | 63.0 | PASS |
| A-P2 | 3 | 3 | 2 | 4 | 3 | 4 | 5 | 3 | 66.0 | PASS |
| A-P4 | 3 | 3 | 2 | 5 | 3 | 5 | 4 | 3 | 69.0 | PASS |
| A-P7 | 2 | 3 | 3 | 2 | 4 | 4 | 3 | 3 | 57.0 | **FAIL** |
| B-P1 | 4 | 4 | 3 | 5 | 4 | 2 | 4 | 3 | 75.0 | PASS |
| B-P4 | 3 | 3 | 3 | 4 | 3 | 2 | 3 | 3 | 61.0 | PASS |
| C-P1 | 2 | 3 | 2 | 4 | 4 | 5 | 4 | 3 | 64.0 | PASS |
| C-P4 | 4 | 4 | 2 | 2 | 2 | 3 | 3 | 3 | 59.0 | **FAIL** |

Nhận xét về bảng:

- Không ứng viên nào đạt 4 ở `innovation`. Phần lớn khoảng cách giữa các ứng viên đến từ `demand`, `international` và `theme`.
- Chênh lệch giữa A-P2, A-P4, C-P1 và A-P1 chỉ 3–6 điểm. Mức này nằm trong sai số của một người chấm, vì mỗi bậc điểm ở tiêu chí 15% đã là 3 điểm.
- Điểm B-P1 cao nhưng `feasibility` = 2. Đây là rủi ro lớn nhất của ứng viên này.

## 3. Per-candidate evaluation

### A-P1 — Yahoo! Pipes → lọc và tổng hợp nguồn web do người dùng tự lắp ráp

**Pitch (một câu):** "Yahoo! Pipes from 2007, rebuilt so that anyone can wire up their own news filter from websites that have no RSS, and see exactly why each item was kept or dropped, without an algorithmic feed."

**Người dùng mục tiêu cụ thể theo vùng:**

| Vùng | Người dùng | Bằng chứng | Nhãn |
|---|---|---|---|
| Bắc Mỹ | Nhà báo và nhà nghiên cứu chính sách theo dõi trang chính phủ, thông báo đấu thầu | Pew 2026: 52% người trưởng thành Mỹ "worn out" (A·R06). Đây là mệt mỏi tin tức, **không** phải đo nhu cầu lọc | SUY LUẬN (A-P1-C2 tách) |
| Châu Âu | Nhóm vận hành và người làm tự động hóa đã dùng n8n (Berlin) | n8n ~200.000 người dùng hoạt động (03/2025, B2-R46). Series C 180 triệu USD (B2-R09, đã mở) | ĐÃ XÁC MINH (tài trợ) / SUY LUẬN (áp vào nhóm theo dõi nguồn) |
| Châu Á | Cộng đồng RSSHub/Folo ở Trung Quốc: người tự tạo feed cho trang không có RSS | Folo AGPL, 39,4k sao (B2-R12, đã mở); có gói trả phí (B2-R50, snippet) | ĐÃ XÁC MINH (repo) / SUY LUẬN (quy mô người dùng) |

Rào cản: scraping vi phạm ToS ở một số trang. Trang ở Trung Quốc thường chặn scraper từ nước ngoài, và ngược lại. Bộ lọc ngữ nghĩa cần đa ngôn ngữ.

**Bằng chứng nhu cầu.** Vấn đề: Reuters DNR 2026 (54% so với 51%, 48 thị trường) cho thấy người dùng chuyển sang kênh thuật toán, nhưng không đo nhu cầu kiểm soát. Muốn giải pháp mới: chưa có bằng chứng trực tiếp. Phần tăng trưởng của n8n và Folo chỉ cho thấy có người tự lắp ráp luồng dữ liệu. Nó không chứng minh người không biết lập trình muốn làm việc đó (A-P1-C4 vẫn là GIẢ THUYẾT).

**Ghi chú thương mại (không chấm).**
- Ai trả tiền: cá nhân chuyên môn trả gói reader (Feedly Pro+ ~99 USD/năm theo nhiều nguồn thứ ba, chưa mở trang giá chính thức). Doanh nghiệp trả cho n8n.
- Bằng chứng chi tiêu tương đương: định giá n8n 2,5 tỷ USD (ĐÃ XÁC MINH, B2-R09); Folo có gói Plus/Pro (SUY LUẬN, snippet).
- Rào cản chính: phân khúc giữa "reader" và "automation" đã bị hai nhóm đối thủ chiếm, và chính Yahoo! Pipes đã thất bại thương mại.

**Đối thủ mạnh nhất và khoảng trống.** n8n có node AI, trả phí hoặc tự host (B2-R09, B2-R46). Khoảng trống mà A nêu ở Phase 1 là "người dùng không chuyên phải tự vận hành server". Khoảng trống này còn, nhưng hẹp: n8n Cloud đã bỏ yêu cầu tự host. Feedly đã có dedup mặc định (B2-R11, đã mở) và Leo AI cho lọc chủ đề. Folo là reader AI mã nguồn mở. Phần còn trống: (1) bộ trích xuất tự sửa khi trang đổi cấu trúc, và (2) lý do giữ/loại hiện rõ từng mục trong một đồ thị tất định. Chưa có benchmark nào chứng minh đối thủ thiếu hai năng lực này (SUY LUẬN).

**Điểm theo tiêu chí:**

| Tiêu chí | Điểm | Conf | Bằng chứng | Nhãn bằng chứng chính | Lý do |
|---|---|---|---|---|---|
| demand | 2 | M | A-P1-C2, A-P1-C3, B2-R09, B2-R46, B2-R12 | SUY LUẬN | Có tín hiệu thứ cấp gián tiếp (mệt mỏi tin tức, tăng trưởng công cụ). Không có bằng chứng từ chính nhóm người dùng mục tiêu |
| international | 3 | M | A·R05, B2-R12, B2-R09, A·R06 | SUY LUẬN | Có tín hiệu ở cả 3 vùng nhưng đều là hành vi lân cận. Không vùng nào đo đúng vấn đề, nên không lên 4 |
| innovation | 2 | M | B2-R09, B2-R11, B2-R12, A·R08c | ĐÃ XÁC MINH (đối thủ tồn tại) / SUY LUẬN (khoảng trống) | n8n, Feedly và Folo phủ phần lớn việc cốt lõi. Khoảng trống chỉ nằm ở tự sửa extractor và giải thích lý do lọc |
| theme | 5 | H | A-P1-C1, A·R02 | ĐÃ XÁC MINH | Pipes đóng 30/09/2015. Canvas kiểu Pipes là trung tâm của cả sản phẩm lẫn demo |
| ai | 3 | M | A-P1 §6 | GIẢ THUYẾT | Extractor tự sửa có oracle (so với nội dung trang thật). Lọc ngữ nghĩa thay được bằng keyword/rule, mất mát vừa phải |
| feasibility | 4 | H | B2-R11, A·R08c | SUY LUẬN | Chạy trên web với feed công khai trong 7 ngày là khả thi. Rủi ro nằm ở ToS khi scrape |
| demo | 4 | M | A-P1 §6 | SUY LUẬN | Trước/sau trên nguồn thật thì dễ hiểu. Nhưng giá trị "minh bạch" khó thấy hơn một bản tóm tắt AI |
| sustainability | 3 | M | B2-R09, B2-R50 | SUY LUẬN | Có người trả tiền cho công cụ cùng loại. Vùng xám pháp lý khi scrape giữ điểm ở mức 3 |

**Phản chứng mạnh nhất.** Thị trường đã giải bài toán theo hai hướng: reader AI (Feedly, Folo) cho người đọc và n8n cho người tự động hóa. n8n tăng từ ~270 triệu lên 2,5 tỷ USD định giá trong 2025. Điều đó cho thấy nhu cầu lắp ráp luồng đã được một sản phẩm sống phục vụ, không còn là giá trị bị mất.

**Điều có thể đổi điểm.** Một phép thử: 5 nhà báo/nhà nghiên cứu dựng luồng trong 15 phút, rồi so với n8n template và Feedly. Nếu họ hoàn thành nhanh hơn rõ rệt, `demand` và `innovation` lên 3. Nếu chỉ ra n8n đã có node "self-healing scraper", `innovation` xuống 1.

### A-P2 — Apple Guide → hướng dẫn thao tác bám trạng thái UI thật

**Pitch:** "Apple Guide in 1994 drew a red circle on the exact button you needed and checked that you had clicked it. We bring that back for any web app, without the vendor having to build it in."

**Người dùng mục tiêu theo vùng:**

| Vùng | Người dùng | Bằng chứng | Nhãn |
|---|---|---|---|
| Bắc Mỹ | Nhân viên văn phòng dùng SaaS thay đổi giao diện liên tục; người lớn tuổi dùng cổng dịch vụ công | Pendo (Mỹ) và thị trường DAP (B2-R30). Microsoft đưa Copilot Vision Highlights ra cho người dùng Mỹ (B2-R01, đã mở) | ĐÃ XÁC MINH (sản phẩm tồn tại) / SUY LUẬN (nhu cầu người dùng cuối) |
| Châu Âu | Nhân viên doanh nghiệp dùng SAP | SAP mua WalkMe (A·R12, ĐÃ XÁC MINH theo overlay); giá 1,5 tỷ USD theo TechCrunch (B2-R32, snippet) | ĐÃ XÁC MINH / SUY LUẬN |
| Châu Á | Nhân viên doanh nghiệp dùng phần mềm do Whatfix (Ấn Độ) hướng dẫn | Whatfix gọi 125 triệu USD (09/2024); doanh thu 2025 tăng 31% theo tự công bố (B2-R30, B2-R32) | SUY LUẬN (tự công bố, snippet) |

Rào cản: hướng dẫn phải theo ngôn ngữ và bản địa hóa của UI. Có rủi ro quyền riêng tư nếu đọc màn hình. Một đầu mối chưa xác minh: snippet cho biết Copilot Vision ban đầu mở cho "non-European countries". Trang Microsoft tôi mở không nêu điều này (CHƯA RÕ).

**Bằng chứng nhu cầu.** Vấn đề có bằng chứng chi tiêu mạnh ở phía doanh nghiệp: thị trường DAP ~1,04 tỷ USD năm 2024 (Gartner qua Whatfix, SUY LUẬN), và thương vụ WalkMe. Còn bằng chứng rằng **người dùng cuối** muốn công cụ phía người dùng thì chưa có. Tín hiệu gián tiếp: Microsoft và Google đều đã đầu tư vào "show me how". Đó là bằng chứng các hãng lớn tin vào nhu cầu, nhưng cũng là đối thủ trực tiếp.

**Ghi chú thương mại.**
- Ai trả tiền: doanh nghiệp, để tăng adoption phần mềm nội bộ.
- Bằng chứng chi tiêu: WalkMe được mua, Whatfix gọi vốn (ĐÃ XÁC MINH cho thương vụ SAP–WalkMe; phần còn lại SUY LUẬN).
- Rào cản chính: người dùng cuối không trả tiền khi Copilot và Gemini đã kèm sẵn trong OS. Kênh B2B thì WalkMe, Whatfix và Pendo đã chiếm.

**Đối thủ mạnh nhất và khoảng trống.** **Copilot Vision with Highlights** (B2-R01, đã mở, 12/06/2025): "it will show you within the app you're in where to click and what to do". Có trên Windows 10/11 tại Mỹ. Đây là phản chứng mà Phase 1.5 ghi "chưa kiểm". Nay đã kiểm, và nó **phủ đúng việc cốt lõi** của A-P2 (chỉ chỗ bấm trên app thật, không cần nhà phát triển tích hợp). Gemini Live tô sáng vật thể khi chia sẻ **camera** (B2-R31). Tôi không tìm thấy nguồn cho thấy Gemini làm việc này trên màn hình chia sẻ. Khoảng trống còn lại: kiểm tra trạng thái **tất định** qua DOM/Accessibility Tree. Tức là xác nhận bước đã xong rồi mới chuyển bước, từ chối khi phần tử không tồn tại, chạy cục bộ, và không gửi luồng màn hình lên cloud. Highlights dựa trên thị giác và không nêu cơ chế xác nhận bước (SUY LUẬN, vì tôi chưa thử).

**Điểm theo tiêu chí:**

| Tiêu chí | Điểm | Conf | Bằng chứng | Nhãn | Lý do |
|---|---|---|---|---|---|
| demand | 3 | M | A-P2-C2 (tách), B2-R30, B2-R32, B2-R01 | ĐÃ XÁC MINH (thương vụ) / SUY LUẬN (thị trường) | Chi tiêu thứ cấp mạnh nhưng ở phía doanh nghiệp. Không có bằng chứng người dùng cuối muốn giải pháp mới |
| international | 3 | M | B2-R30, B2-R32, B2-R01 | SUY LUẬN | Vendor có mặt ở cả 3 vùng, nhưng bằng chứng là của vendor, không phải người dùng cụ thể. Có rào cản ngôn ngữ UI và khả năng giới hạn ở EU |
| innovation | 2 | M | B2-R01, B2-R31, A·R12, A·R13 | ĐÃ XÁC MINH (Copilot Highlights) | Copilot phủ việc cốt lõi. Khoảng trống là xác nhận trạng thái tất định và quyền riêng tư: có giá trị nhưng gần với một tính năng bổ sung |
| theme | 4 | H | A-P2-C1, A·R09–R11 | ĐÃ XÁC MINH | Apple Guide bị bỏ từ Mac OS X là mỏ neo rõ (coachmark đỏ). Phần giá trị nằm ở workflow hướng dẫn được hồi sinh |
| ai | 3 | M | A-P2 §6, B2-R01 | SUY LUẬN | Biên dịch tài liệu thành bước gắn phần tử có oracle (phần tử tồn tại, trạng thái đạt). Nhưng chính Copilot cho thấy AI thị giác chung đã làm được phần lớn |
| feasibility | 4 | M | A-P2 §6 | SUY LUẬN | Browser extension trên 2–3 web app công khai làm được trong 7 ngày. Canvas WebGL ngoài phạm vi |
| demo | 5 | M | A-P2 §6 | SUY LUẬN | Trước/sau trên web app thật, nhìn là hiểu, không cần kiến thức ngành |
| sustainability | 3 | M | B2-R30, B2-R32 | SUY LUẬN | Mô hình B2B DAP có thật. Mô hình cho người dùng cuối chưa có bằng chứng |

**Phản chứng mạnh nhất.** Copilot Vision Highlights đã đưa "Apple Guide cho mọi app" tới người dùng Mỹ từ 06/2025, miễn phí, ở cấp OS. Một bản hackathon sẽ bị so trực tiếp với tính năng này.

**Điều có thể đổi điểm.** Thử 5 tác vụ nhiều bước trên cùng web app với Copilot Highlights và một prototype bám DOM. Nếu Copilot sai bước hoặc không xác nhận bước đã xong trong ≥30% trường hợp, `innovation` lên 3. Nếu Copilot làm tốt, `innovation` xuống 1.

### A-P4 — Del.icio.us và Pocket → kho bookmark/đọc sau chống link rot, không lệ thuộc SaaS

**Pitch:** "Mozilla killed Pocket in 2025 and deleted everyone's saved articles; we rebuild Pocket and Del.icio.us as a local-first library that notices when a saved page has quietly died or been taken over, and keeps your copy."

**Người dùng mục tiêu theo vùng:**

| Vùng | Người dùng | Bằng chứng | Nhãn |
|---|---|---|---|
| Bắc Mỹ | Cựu người dùng Pocket; nhà báo và nhà nghiên cứu trích link | Pocket đóng 08/07/2025 (A-P4-C1, ĐÃ XÁC MINH); Pew: 38% trang 2013 không còn (A-P4-C2, ĐÃ XÁC MINH, đo ở Mỹ) | ĐÃ XÁC MINH |
| Châu Âu | Cựu người dùng Pocket (dịch vụ toàn cầu) | Không tìm được số liệu riêng cho châu Âu. Truy vấn đã thử: "Pocket shutdown migration Raindrop Instapaper Karakeep users moved 2025" | **không tìm thấy bằng chứng riêng** |
| Châu Á | Người dùng Hatena Bookmark (Nhật); phóng viên chính trị ở Ấn Độ | Báo Nhật chỉ đưa lại số liệu Pew (B2-R37). Bài về Ấn Độ là blog cá nhân, tự nhận "India lacks comparable large scale studies" (B2-R36). Truy vấn: "はてなブックマーク リンク切れ … OR link rot Asia study 2025" | **không tìm thấy bằng chứng định lượng** |

Rào cản: lưu bản sao trang có thể vướng bản quyền ở EU và Nhật nếu chia sẻ công khai. Tính năng "folksonomy chia sẻ" làm rủi ro này lớn hơn.

**Bằng chứng nhu cầu.** Vấn đề: Pocket đóng (ĐÃ XÁC MINH). Internet Archive (04/2026, B2-R35, snippet) cho biết Wayback chỉ cứu khoảng 15% URL chết trong mẫu Pew, tức phần lớn link chết không thể phục hồi. Hành vi: người dùng đã phải di chuyển; TechCrunch 08/2026 ghi Matter, Instapaper và Raindrop hưởng lợi (B2-R34, không có số). Muốn giải pháp **mới**: chưa có bằng chứng. Việc di chuyển cho thấy họ đã có nơi đến.

**Ghi chú thương mại.**
- Ai trả tiền: người dùng cá nhân chuyên sâu (Raindrop Pro, Instapaper Premium, Pinboard trả phí).
- Bằng chứng: có gói trả phí (A·R22, SUY LUẬN về quy mô). Del.icio.us bán giá 35.000 USD năm 2017 (A·R18, chưa kiểm).
- Rào cản chính: hai sản phẩm gốc đều thất bại thương mại. Local-first khó thu tiền.

**Đối thủ mạnh nhất và khoảng trống.** Raindrop.io (bản lưu xóa khoảng 1 tháng sau khi hết Pro, A-P4-C3 phần dữ kiện khớp), Karakeep (AI tagging, tự host), Linkwarden (lưu bản sao trang; được nêu trong snippet B2-R34, tôi chưa mở tài liệu), ArchiveBox, Instapaper. Khoảng trống: phát hiện "soft rot", tức trang vẫn trả 200 nhưng đã thành trang đỗ hoặc bị chiếm tên miền. Tôi **chưa kiểm** liệu Linkwarden hay Karakeep đã có tính năng này. Đây là kiểm tra quan trọng còn thiếu.

**Điểm theo tiêu chí:**

| Tiêu chí | Điểm | Conf | Bằng chứng | Nhãn | Lý do |
|---|---|---|---|---|---|
| demand | 3 | M | A-P4-C1, A-P4-C2, B2-R33, B2-R34, B2-R35 | ĐÃ XÁC MINH (sự kiện, link rot) / SUY LUẬN (hành vi di chuyển) | Bằng chứng thứ cấp hiện tại mạnh. Không có bằng chứng muốn giải pháp mới |
| international | 3 | M | A-P4-C1, B2-R37, B2-R36 | ĐÃ XÁC MINH (vendor toàn cầu EOL) | Dữ liệu từ một vùng, cộng lý do cấu trúc đã xác minh (Pocket là dịch vụ toàn cầu). Châu Âu và châu Á không có bằng chứng riêng |
| innovation | 2 | M | A·R22–R24, B2-R34 | SUY LUẬN | Nhiều đối thủ mạnh và miễn phí. Khoảng trống soft-rot chưa đối chiếu với Linkwarden/Karakeep |
| theme | 5 | H | A-P4-C1, A·R19, A·R20, B2-R33 | ĐÃ XÁC MINH | Pocket chết năm 2025 và tệp export của nó là trung tâm cả sản phẩm lẫn demo |
| ai | 3 | M | A-P4 §6 | GIẢ THUYẾT | Có thể có oracle (tập trang đỗ/chiếm tên miền có nhãn). Một phần thay được bằng heuristic (danh sách parking, so DOM) |
| feasibility | 5 | M | B2-R33, B2-R35 | SUY LUẬN | Ứng dụng local, tệp export chuẩn, Wayback API công khai. Không cần đối tác |
| demo | 4 | M | A-P4 §6 | SUY LUẬN | Nhập bookmark thật rồi đánh dấu link chết hoặc bị chiếm: dễ hiểu. Phần "giữ bản sao" ít kịch tính |
| sustainability | 3 | M | A·R22, B2-R34 | SUY LUẬN | Có sản phẩm trả phí tương đương. Mô hình local-first chưa có bằng chứng thu tiền |

**Phản chứng mạnh nhất.** Cả Del.icio.us lẫn Pocket chết vì người dùng đại chúng không duy trì thói quen hoặc không trả tiền (A·R18, A·R19). Nhóm nghiêm túc đã có Karakeep và ArchiveBox miễn phí. Thêm vào đó, đa số bookmark cũ không bao giờ được mở lại (phép thử của A, chưa chạy).

**Điều có thể đổi điểm.** Nếu Linkwarden hoặc Karakeep đã phát hiện soft-404 hay chiếm tên miền, `innovation` xuống 1. Nếu đo trên export thật và thấy ≥10% link cần dùng đã "chết mềm" mà kiểm HTTP bỏ sót, `demand` lên 4 và `ai` lên 4.

### A-P7 — Stack Overflow → lưu lời giải lỗi biên đã được người kiểm chứng

**Pitch:** "Developers stopped posting to Stack Overflow, from 200,000 questions a month to under 1,000. We turn a fix you just verified with your AI agent into a public, reproducible, anonymised record, so the next person, and the next model, can find it."

**Người dùng mục tiêu theo vùng:**

| Vùng | Người dùng | Bằng chứng | Nhãn |
|---|---|---|---|
| Bắc Mỹ | Người duy trì thư viện mã nguồn mở; kỹ sư hạ tầng gặp lỗi phiên bản mới | Sụt câu hỏi (A-P7-C1, ĐÃ XÁC MINH qua API); DevClass 01/2026 (B2-R38) | ĐÃ XÁC MINH |
| Châu Âu | Như trên (khảo sát Stack Overflow có 169 quốc gia) | A·R40 (n=16.985 cho câu hỏi về việc dùng SO). Không có dữ liệu tách riêng châu Âu | SUY LUẬN |
| Châu Á | Người viết Qiita/Zenn (Nhật) | Qiita: bài gắn tag AI tăng 7.477 → 18.779 (2023→2025; B2-R41, tự công bố). CodeZine: diễn giả nói chủ đề và người đọc bài kỹ thuật giảm (B2-R42, ý kiến). CSDN: **không tìm thấy bằng chứng** (truy vấn "Qiita Zenn CSDN 投稿数 減少 生成AI 2025") | SUY LUẬN |

Rào cản: NDA khiến log công việc khó chia sẻ. Tri thức lập trình chủ yếu bằng tiếng Anh; Qiita/Zenn và CSDN là hệ sinh thái riêng theo ngôn ngữ.

**Bằng chứng nhu cầu.** Vấn đề "kho Q&A công khai ngừng tăng" có bằng chứng tái lập (API). Còn vấn đề "lập trình viên mắc kẹt với lỗi biên" là SUY LUẬN (A-P7-C3). Bằng chứng ngược: chính sự sụt giảm cho thấy AI đã đáp ứng nhu cầu hằng ngày. Động cơ đóng góp là CHƯA RÕ (A-P7-C4).

**Ghi chú thương mại.**
- Ai trả tiền: AI lab mua dữ liệu đã kiểm chứng; doanh nghiệp mua kho tri thức nội bộ.
- Bằng chứng: Stack Overflow đạt doanh thu kỷ lục 129 triệu USD trong năm tài chính đến 31/03/2026, chủ yếu từ Stack Internal (B2-R39, SUY LUẬN, một nguồn thứ cấp dẫn báo cáo năm Prosus); Stack Data Licensing hợp tác với các AI lab (B2-R40, tự công bố).
- Rào cản chính: dữ liệu công khai khó thu tiền, và người đóng góp không được trả công.

**Đối thủ mạnh nhất và khoảng trống.** Coding agent trong IDE; Stack Overflow AI Assist (GA 02/12/2025) và MCP server của Stack Overflow (12/2025) (B2-R40); GitHub Issues/Discussions. Khoảng trống: đóng gói tự động một lần sửa lỗi thành bản ghi có test tái lập và đã ẩn danh. Chưa thấy đối thủ làm đúng việc này (SUY LUẬN, chưa quét kỹ các công cụ "agent memory").

**Điểm theo tiêu chí:**

| Tiêu chí | Điểm | Conf | Bằng chứng | Nhãn | Lý do |
|---|---|---|---|---|---|
| demand | 2 | M | A-P7-C1–C3, B2-R38, B2-R39 | ĐÃ XÁC MINH (sụt giảm) / SUY LUẬN (vấn đề người dùng) | Sự kiện có thật. Nỗi đau của người dùng mục tiêu là suy luận, và có phản chứng mạnh |
| international | 3 | M | A·R40, B2-R41, B2-R42 | SUY LUẬN | Khảo sát toàn cầu cộng tín hiệu yếu ở Nhật. Không có bằng chứng châu Âu riêng |
| innovation | 3 | L | B2-R40, A-P7 §5 | SUY LUẬN | Khoảng trống "fix → bản ghi tái lập" có vẻ hợp lý. Đối thủ phủ một phần (AI Assist, MCP) |
| theme | 2 | H | A-P7-C1, B2-R39, B2-R40 | ĐÃ XÁC MINH | Stack Overflow vẫn sống, đang ra tính năng mới và đạt doanh thu kỷ lục. Đây là "công nghệ sống đang suy giảm" (anchor 2). **Gate FAIL** |
| ai | 4 | M | A-P7 §6 | SUY LUẬN | AI cô lập điều kiện lỗi, ẩn danh và sinh test. Oracle rõ (test fail → pass) |
| feasibility | 4 | M | A-P7 §6 | SUY LUẬN | Demo bằng một phiên sửa lỗi thật là khả thi. Dữ liệu thật thì có rủi ro bí mật |
| demo | 3 | M | A-P7 §6 | SUY LUẬN | Cần kiến thức lập trình. Giám khảo kỹ thuật hiểu, nhưng trước/sau ít trực quan |
| sustainability | 3 | L | B2-R39, A-P7-C4 | SUY LUẬN / CHƯA RÕ | Có chi tiêu cho data licensing. Động cơ đóng góp chưa rõ |

**Phản chứng mạnh nhất.** Stack Overflow không chết: năm tài chính 2026 là năm doanh thu cao nhất, và hãng đang làm chính phần AI + MCP (B2-R39, B2-R40). Theme gate thất bại theo anchor đã cho, không phải vì thiếu dữ liệu.

**Điều có thể đổi điểm.** `theme` chỉ lên 3 nếu Stack Overflow công bố ngừng nhận câu hỏi công khai hoặc đóng site. Nếu phép thử 10 lỗi biên năm 2026 cho thấy agent thất bại lặp lại và bản ghi giúp giải ngay, `demand` lên 3.

### B-P1 — Thiết bị bị brick khi nhà sản xuất tắt cloud/app

**Pitch:** "When a company switches off its cloud, devices that still work become bricks; we use AI to recover the device's local protocol from the old app while it still runs, and give owners back control."

**Người dùng mục tiêu theo vùng:**

| Vùng | Người dùng | Bằng chứng | Nhãn |
|---|---|---|---|
| Bắc Mỹ | Chủ thiết bị Wemo, Nest đời đầu, Neato, Car Thing; người dùng Home Assistant | Belkin dừng cloud/app cho một số Wemo từ 31/01/2026 (B2-R07, đã mở, cộng snippet TechSpot/Slashdot): **ĐÃ XÁC MINH**. Neato mất điều khiển qua app (B2-R02, đã mở; nguồn gốc là The Verge, chưa mở): SUY LUẬN. FTC: 161/184 sản phẩm không công bố thời hạn hỗ trợ (B2-R13, snippet): SUY LUẬN | ĐÃ XÁC MINH / SUY LUẬN |
| Châu Âu | Chủ hub Futurehome (Na Uy); chủ loa Bose SoundTouch; người dùng Neato/Vorwerk (Đức) | Futurehome buộc thuê bao 1.188 NOK/năm từ 26/06/2025 (B2-R14, snippet, nhiều báo khớp). Khách chuyển sang Homey (snippet tek.no). Bose tắt cloud 06/05/2026 (B2-R04, đã mở). EU CRA bắt khai thời hạn hỗ trợ (B2-R16) | ĐÃ XÁC MINH (Bose) / SUY LUẬN (Futurehome) |
| Châu Á | Chủ thiết bị của vendor toàn cầu ở Nhật | Impress Watch đưa tin Belkin và Bose dừng cloud (B2-R15, snippet). Trung Quốc: MIIT nêu tên 20 thiết bị thông minh vi phạm quyền người dùng, gồm tự gia hạn bắt buộc (B2-R49). Đây là vấn đề lân cận, không phải brick. **Không tìm được** ca brick do vendor châu Á (truy vấn tiếng Nhật và "停服 智能设备 无法使用 2025") | SUY LUẬN |

Rào cản: DMCA §1201 ở Mỹ; luật EU về interoperability rộng hơn nhưng phụ thuộc từng trường hợp; khóa chữ ký firmware. Giao thức khác nhau theo từng vendor, nên không có giải pháp chung cho mọi thiết bị.

**Bằng chứng nhu cầu.** Vấn đề: chuỗi sự kiện 2025–2026 dày và độc lập với nhau (Wemo, Neato, Nest 25/10/2025 [B-P1-C4], Futurehome, Bose, Hive, iRobot phá sản [B2-R51]). Hành vi: Home Assistant tăng từ 1 lên hơn 2 triệu cài đặt hoạt động trong 2024 (B2-R08, tự báo cáo, SUY LUẬN). Đây là thời gian và tiền người dùng bỏ ra để có quyền điều khiển cục bộ. Thêm: dự án No Longer Evil (B-P1-C4); khách Futurehome chuyển sang Homey; 17 tổ chức kiến nghị FTC (B2-R47). Muốn giải pháp **mới** cho thiết bị ngách: chưa có bằng chứng trực tiếp. Điểm 4 là mức trần cho bằng chứng hành vi thứ cấp mạnh (anchor).

**Ghi chú thương mại.**
- Ai trả tiền hoặc tài trợ: cộng đồng và quỹ phi lợi nhuận (Open Home Foundation), người dùng (Nabu Casa, Homey), và có thể chính vendor đang đóng cửa, như Bose đã tự công bố API (B2-R04).
- Bằng chứng chi tiêu: quy mô Home Assistant (SUY LUẬN, tự báo cáo). Người dùng Futurehome trả thuê bao hoặc mua hub khác (SUY LUẬN).
- Rào cản chính: mỗi thiết bị là một dự án riêng; rủi ro pháp lý; nhu cầu phân tán.

**Đối thủ mạnh nhất và khoảng trống.** Home Assistant cùng integration cộng đồng; No Longer Evil; vendor tự công bố API (Bose). Về phương pháp, đối thủ là chính HotNets '26 (B·R01), đã chứng minh pipeline trên AirPort. Khoảng trống: biến pipeline thành **quy trình lặp lại được cho thiết bị ngách**, kèm báo cáo độ phủ hành vi ("đã thấy / chưa thấy"). Ca Bose cho thấy khi vendor hợp tác thì không cần AI. Như vậy khoảng trống chỉ nằm ở các vendor không hợp tác (SUY LUẬN).

**Điểm theo tiêu chí:**

| Tiêu chí | Điểm | Conf | Bằng chứng | Nhãn | Lý do |
|---|---|---|---|---|---|
| demand | 4 | M | B-P1-C1, B-P1-C4, B2-R07, B2-R02, B2-R04, B2-R14, B2-R13, B2-R08 | ĐÃ XÁC MINH (Wemo, Bose, Car Thing) / SUY LUẬN (hành vi HA) | Nhiều sự kiện độc lập năm 2025–2026 cộng hành vi khắc phục. Không có bằng chứng sơ cấp từ người dùng, nên không lên 5 |
| international | 4 | M | B2-R13, B2-R14, B2-R04, B2-R16, B2-R15, B2-R49 | ĐÃ XÁC MINH (NA, EU) / SUY LUẬN (Asia) | Bằng chứng độc lập ở Bắc Mỹ và châu Âu. Châu Á chỉ có tin về vendor toàn cầu và vấn đề lân cận |
| innovation | 3 | M | B·R01, B2-R08, B2-R04, B-P1-C4 | ĐÃ XÁC MINH (B·R01 báo cáo) / SUY LUẬN (khoảng trống) | Phương pháp đã có người công bố. Khoảng trống là đóng gói lặp lại được cho long tail |
| theme | 5 | H | B-P1-C1, B-P1-C2, B2-R07, B2-R04 | ĐÃ XÁC MINH | Một sản phẩm cụ thể đã bị khai tử (Car Thing, Wemo cloud, SoundTouch cloud) là trung tâm cả sản phẩm lẫn demo |
| ai | 4 | M | B-P1-C5, B-P1-C6, B·R01 | ĐÃ XÁC MINH (bài báo báo cáo) / GIẢ THUYẾT (chi phí, tổng quát hóa) | AI chịu tải, có oracle (replay so với app gốc), có cơ chế trong bài báo. Chưa tái lập độc lập và tốn "billions of tokens", nên không cho 5 |
| feasibility | 2 | M | B·R01, B-P1-C6 | GIẢ THUYẾT | Cần thiết bị thật và app gốc còn chạy. Bài báo ước lượng 4–5 ngày công cho người có kinh nghiệm, cộng token rất lớn. Có hai rủi ro vật chất (phương pháp, phần cứng) |
| demo | 4 | M | B-P1 §6 | SUY LUẬN | "Thiết bị chết sống lại" rất dễ hiểu. Nhưng phụ thuộc phần cứng hoạt động trên sân khấu |
| sustainability | 3 | M | B2-R08, B2-R48, B2-R16 | SUY LUẬN | Có hệ sinh thái OSS và quỹ duy trì. Pháp lý không rõ cho từng thiết bị, nên không lên 4–5 |

**Phản chứng mạnh nhất.** (1) Vendor có thể tự giải: Bose công bố API, và EU CRA buộc khai thời hạn hỗ trợ từ 12/2027. Hướng này làm vấn đề thu hẹp theo thời gian. (2) Matter/HomeKit giúp thiết bị mới chạy cục bộ. (3) Toàn bộ giá trị AI dựa trên một bài báo chưa tái lập (overlap O2).

**Điều có thể đổi điểm.** Chọn một thiết bị rẻ còn app gốc chạy được và đo thời gian để replay một workflow. Nếu làm được trong ≤2 ngày, `feasibility` lên 3–4. Nếu không, `feasibility` xuống 1. Một bằng chứng brick do vendor châu Á sẽ đưa `international` lên 5.

### B-P4 — Thiết bị khoa học bị khóa vào PC/OS hết hỗ trợ

**Pitch:** "A working microscope or chromatograph often costs more than a house, but it is tied to a Windows XP or Windows 10 PC that can no longer be patched; we keep the instrument alive by moving its control to a modern machine."

**Người dùng mục tiêu theo vùng:**

| Vùng | Người dùng | Bằng chứng | Nhãn |
|---|---|---|---|
| Bắc Mỹ | Bộ phận IT của khoa hóa và sinh ở đại học | Khoa Hóa UW–Madison 2024 (B-P4-C2, ĐÃ XÁC MINH, thu hẹp về một khoa) | ĐÃ XÁC MINH |
| Châu Âu | Lab đại học và QC dược | **Không tìm thấy bằng chứng riêng.** Truy vấn: "Windows 10 end of support laboratory instrument control software chromatography 2025 labs", "legacy lab instrument Windows XP … SiLA 2 LADS". Copa-Data có bài "Connecting legacy pharma equipment … 2026" (vendor, chưa mở) | không tìm thấy |
| Châu Á | Kỹ thuật viên phòng thí nghiệm ở đại học Nhật | ĐH Kyoto: PC điều khiển máy hóa lỏng heli chạy XP; nhà cung cấp không có PC thay, phải mua PC XP cũ (B2-R18, snippet, không rõ năm). ĐH Osaka City 2014: PC XP bị ngắt mạng, kiểm USB riêng (snippet, cũ) | SUY LUẬN |

Rào cản: lab GxP cần validation; EULA của vendor; giao thức khác nhau theo từng hãng và đời máy.

**Bằng chứng nhu cầu.** Vấn đề: vendor đang thúc nâng cấp quanh mốc Windows 10 EOL. Thermo Fisher (B2-R06, đã mở) viết "Microsoft's end of support for Windows 10 has accelerated workstation replacement planning across many organizations". Agilent (B2-R17) và Waters (snippet) nói tương tự. Vì có nguồn đã mở cộng hai vendor độc lập, tôi đề xuất nâng **B-P4-C3** từ SUY LUẬN lên **ĐÃ XÁC MINH** cho phát biểu "vendor thúc nâng cấp quanh Windows 10 EOL". Nhãn gốc là SUY LUẬN. Đây là đề xuất, Coordinator quyết. Hành vi lab: giữ PC cũ, tách VLAN, mua PC XP cũ (UW–Madison, Kyoto). Quy mô: CHƯA RÕ (B-P4-C5). Muốn giải pháp mới: chưa có bằng chứng.

**Ghi chú thương mại.**
- Ai trả tiền: ngân sách thiết bị của lab và core facility; QC dược.
- Bằng chứng: chi phí nâng cấp phần mềm sắc ký 10.000 USD (Nature 2021, chỉ là SUY LUẬN theo overlay). Snippet tiếng Nhật nói chi phí cập nhật "từ vài triệu yên" (bài livedoor cũ, không dùng làm bằng chứng). Thị trường middleware tích hợp lab tồn tại (vendor LIMS, Integration Objects), SUY LUẬN.
- Rào cản chính: vendor sở hữu giao thức và chi phối validation; mỗi đời máy là một dự án.

**Đối thủ mạnh nhất và khoảng trống.** Nâng cấp từ vendor; gateway SiLA 2 mã nguồn mở (HardwareX 2020, B2-R19); chuẩn OPC UA LADS (B2-R20); device server nối serial qua IP; PyMeasure/QCoDeS (chưa kiểm). Khoảng trống: các chuẩn trên giả định đã biết giao thức thiết bị. Việc **suy giao thức không có tài liệu** từ trace, với PC cũ làm oracle, chưa có đối thủ công cụ hóa (SUY LUẬN). Còn việc AI làm được điều này trong miền thiết bị khoa học vẫn là GIẢ THUYẾT (B-P4-C4).

**Điểm theo tiêu chí:**

| Tiêu chí | Điểm | Conf | Bằng chứng | Nhãn | Lý do |
|---|---|---|---|---|---|
| demand | 3 | M | B-P4-C1 (tách), B-P4-C2, B2-R06, B2-R17, B2-R18 | ĐÃ XÁC MINH (vendor notice, UW) | Tài liệu chính thức và vendor EOL hiện tại. Không có định lượng, không có bằng chứng muốn giải pháp mới |
| international | 3 | M | B-P4-C2, B2-R18, B2-R06 | ĐÃ XÁC MINH (NA) / SUY LUẬN (Asia) | Có bằng chứng ở 2 vùng (Mỹ, Nhật) cộng vendor EOL toàn cầu. Châu Âu chưa có |
| innovation | 3 | L | B2-R19, B2-R20, B·R01, B-P4-C4 | SUY LUẬN | Chuẩn mở phủ phần "kết nối". Phần "suy giao thức" khả dĩ nhưng chưa chứng minh |
| theme | 4 | M | B-P4-C2, B2-R06, B2-R17 | ĐÃ XÁC MINH | Windows XP/7/10 đã hết hỗ trợ chính thức và là mỏ neo rõ. Giá trị nằm ở việc hồi sinh khả năng điều khiển |
| ai | 3 | L | B-P4-C4, B·R01 | GIẢ THUYẾT | Có oracle (PC cũ), nhưng chuyển giao từ B·R01 chưa có ví dụ nào |
| feasibility | 2 | M | B-P4 §6 | SUY LUẬN | Không có thiết bị trong tay. Cần lab đối tác, hoặc thay bằng một thiết bị serial rẻ (mất tính thuyết phục) |
| demo | 3 | M | B-P4 §6 | SUY LUẬN | Cần giải thích miền. Nếu dùng thiết bị giả lập thì demo yếu |
| sustainability | 3 | M | B2-R06, B2-R17 | SUY LUẬN | Có ngân sách tổ chức. Validation GxP và EULA là rào cản |

**Phản chứng mạnh nhất.** Lab coi cô lập mạng và giữ PC cũ là "đủ tốt" (UW–Madison: "We replace instruments as funding allows"). Vendor đã có lộ trình nâng cấp trả phí. Nhu cầu trả tiền cho bên thứ ba chưa có bằng chứng.

**Điều có thể đổi điểm.** Nếu có lab đồng ý cho ghi trace một thiết bị trước 01/12, `feasibility` lên 3 và `demo` lên 4. Một khảo sát 2025–2026 về tỷ lệ thiết bị chạy OS EOL sẽ nâng `demand`.

### C-P1 — Google Reader → theo dõi nguồn đã chọn mà không đọc lặp cùng sự kiện

**Pitch:** "Google Reader let you follow the sources you chose; we bring it back, but when ten sources report the same event, you read it once and see only what each later report adds."

**Người dùng mục tiêu theo vùng:**

| Vùng | Người dùng | Bằng chứng | Nhãn |
|---|---|---|---|
| Bắc Mỹ | Nhà phân tích ngành, nhóm threat-intel và nghiên cứu nhỏ dùng Feedly/Inoreader | Pew news fatigue (A·R06); Feedly có dedup mặc định (B2-R11) | SUY LUẬN |
| Châu Âu | Người dùng Inoreader (công ty Bulgaria); người dùng NetNewsWire | Không có số liệu người dùng. Inoreader monitoring feeds (C·R05) | SUY LUẬN |
| Châu Á | Người dùng Folo (Trung Quốc); người dùng cũ của livedoor Reader (Nhật) | Folo 39,4k sao, có gói trả phí (B2-R12, B2-R50). Live Dwango Reader (livedoor Reader) đóng; Dwango gợi ý chuyển sang Feedly/Inoreader (B2-R43, 2017) | ĐÃ XÁC MINH (repo) / SUY LUẬN |

Rào cản: so "phần mới" giữa các bản tin đa ngôn ngữ khó hơn đơn ngôn ngữ. Bản quyền nội dung nếu hiển thị toàn văn.

**Bằng chứng nhu cầu.** Vấn đề "đọc lặp" được vendor và nghiên cứu xử lý (C-P1-C2, ĐÃ XÁC MINH ở mức vấn đề kỹ thuật). Các bài "RSS revival 2026" chủ yếu là blog SEO hoặc vendor, nên tôi không dùng làm bằng chứng. Muốn giải pháp mới: không có bằng chứng. Tần suất và chi phí đọc lặp: CHƯA RÕ (C-P1-C8).

**Ghi chú thương mại.**
- Ai trả tiền: người dùng chuyên môn (Feedly Pro+, Inoreader Pro, Folo Plus) và doanh nghiệp (Feedly Enterprise).
- Bằng chứng: có gói trả phí (SUY LUẬN; trang giá chính thức chưa mở).
- Rào cản chính: Feedly đã làm dedup; Google Reader chết vì lượng dùng giảm (C-P1-C1).

**Đối thủ mạnh nhất và khoảng trống.** Feedly dedup (B2-R11, đã mở, cập nhật 10/11/2026): trùng >85%, 31 ngày, không áp trong cùng nguồn, bật mặc định. Particle gom bài cùng sự kiện thành "story" tổng hợp (B2-R44). Inoreader có rule; Folo là AI reader. Khoảng trống của C (C-P1-C5) vẫn đứng: Feedly xóa bản gần trùng, còn sản phẩm này **chỉ ra phần mới** của bản tin sau so với điều người dùng **đã đọc**. Particle tổng hợp nhưng không gắn với trạng thái đã đọc của từng người. Tôi chưa thử Particle (SUY LUẬN).

**Điểm theo tiêu chí:**

| Tiêu chí | Điểm | Conf | Bằng chứng | Nhãn | Lý do |
|---|---|---|---|---|---|
| demand | 2 | M | C-P1-C2, C-P1-C3, B2-R12, B2-R50 | SUY LUẬN | Vendor xử lý vấn đề, nhưng không có đo đạc từ người dùng mục tiêu |
| international | 3 | M | B2-R12, B2-R43, A·R05, B2-R11 | SUY LUẬN | Thói quen dùng reader có ở cả 3 vùng. Vấn đề cụ thể chưa có bằng chứng ở vùng nào |
| innovation | 2 | M | B2-R11, C-P1-C5, B2-R44 | ĐÃ XÁC MINH (Feedly) / SUY LUẬN (khoảng trống) | Feedly và Particle phủ gần. Khoảng trống "delta theo trạng thái đã đọc" hẹp, gần mức tính năng |
| theme | 4 | H | C-P1-C1, C·R01 | ĐÃ XÁC MINH | Google Reader là mỏ neo rõ. Nhưng RSS reader vẫn sống, nên phần giá trị nằm ở workflow |
| ai | 4 | M | C-P1-C7, C·R03 | SUY LUẬN | Phát hiện phần mới vượt hash/embedding là việc AI chịu tải, có thể đo trên tập gán nhãn (NAACL 2025) |
| feasibility | 5 | H | B2-R11 | SUY LUẬN | Feed công khai, không cần đối tác, làm được trong 7 ngày |
| demo | 4 | M | C-P1-C6 | SUY LUẬN | 10 bài thật về một sự kiện, gom thành "đọc một lần, thấy phần mới": dễ hiểu |
| sustainability | 3 | M | B2-R50, A·R08e | SUY LUẬN | Có người trả tiền cho reader. Chính Google Reader chết vì lượng dùng |

**Phản chứng mạnh nhất.** Feedly bật dedup mặc định cho mọi người, Particle đã làm tổng hợp nhiều nguồn, và Folo đưa AI vào reader mã nguồn mở. "Reader + AI" là thị trường đông, không phải giá trị bị mất.

**Điều có thể đổi điểm.** Phép thử của C (C-P1-C8): 30–50 bài thật, so Feedly với Particle. Nếu bản "delta" giảm ≥30% thời gian đọc mà không bỏ sót thông tin mới, `innovation` lên 3 và `demand` lên 3.

### C-P4 — Telecare khi rút PSTN ở Anh

**Pitch:** "As countries switch off the old copper phone network, personal alarms for older people can silently stop reaching help; we make sure every alarm's path to the response centre is checked and signed off before and after the switch."

**Người dùng mục tiêu theo vùng:**

| Vùng | Người dùng | Bằng chứng | Nhãn |
|---|---|---|---|
| Châu Âu (Anh) | Housing provider, đội telecare của hội đồng địa phương, ARC | Ofcom phạt Virgin Media £23,8 triệu (C-P4-C2, ĐÃ XÁC MINH). DHSC: ~3/4 báo động grouped living còn analog (C-P4-C3, SUY LUẬN theo overlay). Which?: 3/7 nhà cung cấp lớn vẫn bán thiết bị chỉ analog (B2-R03, đã mở, 21/08/2025). LGA: 4 hội đồng không xác nhận được trạng thái ARC (B2-R26). Checklist bắt buộc 03/2026 (B2-R27) | ĐÃ XÁC MINH / SUY LUẬN |
| Châu Âu (khác) | Thụy Điển: báo động an toàn do khu tự quản (kommun) cung cấp | Snippet trang PTS; URL trả 404 khi mở | SUY LUẬN (không mở được) |
| Bắc Mỹ | Nhà cung cấp PERS và người cao tuổi nông thôn | FCC nới quy định rút dây đồng (B2-R22); AARP khuyên thử thiết bị báo động y tế khi chuyển (B2-R21); Verizon xin dừng ~277.000 đường dây (snippet) | SUY LUẬN |
| Châu Á | Bên vận hành dịch vụ báo động ở Nhật | NTT chuyển PSTN sang IP; thiết bị hoàn tất khoảng 01/2025 (B2-R10, đã mở nhưng lỗi chữ). MIC 09/2024: một số cuộc gọi khẩn cấp thiếu chức năng sau chuyển (B2-R25). **Không tìm thấy** bằng chứng riêng về báo động hay telecare (truy vấn "警備 緊急通報 IP網移行 影響") | SUY LUẬN |
| (Tham khảo, Úc) | Người dùng báo động cá nhân 3G | Tắt 3G ngày 28/10/2024 ảnh hưởng báo động cá nhân (B2-R23, B2-R24, snippet; trang chính phủ timeout) | SUY LUẬN |

Rào cản: giao thức báo động khác nhau theo nước (BS 8521 ở Anh, SCAIP ở Bắc Âu; tôi chưa mở nguồn cho cả hai). Dữ liệu sức khỏe nhạy cảm. Trách nhiệm pháp lý cao nếu công cụ báo sai là "an toàn".

**Bằng chứng nhu cầu.** Đây là ứng viên có bằng chứng **hành động** của regulator và tổ chức mạnh nhất: án phạt, checklist bắt buộc, hướng dẫn mua sắm, khảo sát hội đồng, điều tra của Which?. Người dùng mục tiêu (housing provider, hội đồng) đang bỏ công sức thật. Bằng chứng họ muốn **công cụ phần mềm mới**: không có. C tự nêu khả năng nút thắt là thiết bị, nguồn điện và lịch kỹ sư (C-P4-C8).

**Ghi chú thương mại.**
- Ai trả tiền: hội đồng địa phương và housing provider, qua ngân sách mua sắm telecare.
- Bằng chứng: có hướng dẫn mua sắm chính thức của DHSC cho ARC số (B2-R28); các nhà cung cấp lớn (Tunstall, Appello) đang bán giải pháp số (B2-R29). SUY LUẬN.
- Rào cản chính: hạn ở Anh là 31/01/2027, nên cửa sổ thị trường ở Anh đóng sớm; incumbent nắm ARC software; mua sắm công chậm.

**Đối thủ mạnh nhất và khoảng trống.** Openreach Prove Telecare (C-P4-C5); checklist của LGA và chính phủ; dịch vụ kỹ sư bắt buộc; nền tảng ARC số của Tunstall và Appello. Khoảng trống "hồ sơ bàn giao xuyên bên có người xác nhận" chưa được chứng minh. Tôi không tìm thấy công cụ chuyên cho việc này (truy vấn "telecare digital switchover platform software ARC migration tracking"), nhưng không tìm thấy không có nghĩa là không có (CHƯA RÕ).

**Điểm theo tiêu chí:**

| Tiêu chí | Điểm | Conf | Bằng chứng | Nhãn | Lý do |
|---|---|---|---|---|---|
| demand | 4 | M | C-P4-C2, C-P4-C3, B2-R03, B2-R26, B2-R27 | ĐÃ XÁC MINH (Ofcom, Which?) / SUY LUẬN (DHSC mẫu) | Regulator hành động, người dùng mục tiêu bỏ công sức. Không có bằng chứng sơ cấp, nên tối đa 4 |
| international | 4 | M | B2-R05, B2-R21, B2-R22, B2-R25, B2-R10 | ĐÃ XÁC MINH (UK) / SUY LUẬN (US, JP) | Việc rút PSTN và dây đồng có ở cả 3 vùng. Phần ảnh hưởng tới báo động chỉ có bằng chứng ở Anh và Mỹ (cộng Úc tham khảo) |
| innovation | 2 | L | C-P4-C5, B2-R28, B2-R29, B2-R27 | SUY LUẬN | Quy trình chính thức và dịch vụ incumbent phủ phần lớn. Khoảng trống chưa kiểm |
| theme | 2 | M | C-P4-C1, C-P4-C7 | ĐÃ XÁC MINH (lịch rút) / SUY LUẬN (yếu tố hồi sinh) | PSTN có lịch rút chính thức. Nhưng sản phẩm **quản lý việc chuyển đi**, không hồi sinh công nghệ, workflow hay năng lực nào của PSTN. Anchor 3 cần "anchors a revived workflow or capability". **Gate FAIL** |
| ai | 2 | H | C-P4-C7 | SUY LUẬN | C tự ghi AI không bắt buộc; rule/checklist làm đủ. AI chỉ trích xuất tài liệu |
| feasibility | 3 | M | C-P4-C8 | SUY LUẬN | Phần mềm làm được trong 7 ngày nhưng chỉ với dữ liệu tổng hợp. Không có đối tác hay hồ sơ thật |
| demo | 3 | M | C-P4-C6 | SUY LUẬN | Câu chuyện mạnh (tính mạng), nhưng thứ hiện trên màn hình là tracker với dữ liệu tổng hợp |
| sustainability | 3 | M | B2-R28, B2-R26 | SUY LUẬN | Có ngân sách công. Cửa sổ ở Anh đóng 01/2027; Mỹ và EU kéo dài hơn |

**Phản chứng mạnh nhất.** Hệ thống chính thức đã dồn lực vào đúng vấn đề này: Openreach, checklist bắt buộc, kỹ sư, hướng dẫn mua sắm. Hạn ở Anh còn khoảng 2 tháng. Và chính C ghi yếu tố Resurrection "thuần workflow chưa chứng minh".

**Điều có thể đổi điểm.** Nếu Coordinator hoặc người dùng diễn giải E3 rằng "giữ năng lực của công nghệ đang bị rút" (ví dụ: bảo đảm tín hiệu báo động tới ARC như đường analog từng làm) là đủ, `theme` lên 3 và gate PASS. Tổng điểm không đổi nhiều (+3). Một housing provider cho xem 10 hồ sơ ẩn danh có lỗ hổng sẽ nâng `innovation` và `demo`.

## 4. Rubric challenges

Tôi vẫn chấm theo trọng số và anchor đã cho. Các điểm dưới đây là ý kiến, không áp vào bảng.

1. **`theme` anchor 3 mơ hồ với ứng viên "quản lý việc rút bỏ" (C-P4).** Câu "anchors a revived workflow or capability" không nói phải hồi sinh **cái gì**. Một công cụ chuyển đổi khỏi công nghệ cũ có thể bị đọc là đạt (công nghệ có lịch rút chính thức) hoặc không đạt (không có gì được hồi sinh). Tôi chấm 2. Đề xuất ghi rõ: năng lực được hồi sinh phải là năng lực **của** công nghệ bị rút.
2. **`theme` thưởng cho sự kiện đóng cửa, không cho mức "chết".** A-P1 và A-P4 được 5 vì sản phẩm gốc đã đóng, dù việc cốt lõi đang được đối thủ phục vụ tốt (n8n, Raindrop). Điều này đẩy các bản "clone có AI" của dịch vụ đã đóng lên cao. Rubric đã đẩy phần này sang `innovation`, nhưng khi theme 15% và innovation 15% bằng nhau thì hai tiêu chí triệt tiêu nhau.
3. **`demand` trần 4 khi không có phỏng vấn làm phẳng phần trên.** Cả 8 ứng viên đều không thể lên 5, nên khoảng điểm thực tế của 20% trọng số chỉ là 2–4. Tác dụng phân biệt của tiêu chí nặng nhất bị giảm. Đề xuất: cho 5 khi có bằng chứng hành vi định lượng độc lập (ví dụ số cài đặt, số đơn khiếu nại) dù không có phỏng vấn.
4. **`international` không tính rào cản pháp lý vào điểm số.** Anchor 5 có "no major cross-cultural or legal barrier", nhưng anchor 3 và 4 không nhắc. Hai ứng viên cùng 4 điểm có thể khác hẳn về rào cản (B-P1 vướng DMCA; C-P4 vướng quy chuẩn từng nước).
5. **`feasibility` 10% có thể quá thấp so với hạn 4/12/2026.** B-P1 đạt điểm cao nhất dù feasibility = 2. Nếu dùng `feasibility` như một gate thứ hai (≥3), B-P1 và B-P4 sẽ bị loại khỏi Top 3. Đề xuất đưa vào phân tích độ nhạy ở Phase 2B.
6. **Không có tiêu chí cho thời hạn của vấn đề.** C-P4 ở Anh có cửa sổ khoảng 2 tháng; vấn đề của B-P1 sẽ thu hẹp khi EU CRA có hiệu lực năm 2027. `sustainability` 5% không đủ để phản ánh điều này.

## 5. Unresolved questions

1. **A-P2:** Copilot Vision Highlights có xác nhận bước đã xong không, và có ở EU không? Chưa thử trực tiếp. Đây là câu hỏi quyết định `innovation`.
2. **A-P4:** Linkwarden hoặc Karakeep đã phát hiện soft-404 hay chiếm tên miền chưa? Chưa mở tài liệu.
3. **A-P1, C-P1:** Bảng giá chính thức của Feedly và gói nào có Leo AI? Trang docs dedup không nêu gói, trang giá chưa mở. Particle có gắn với trạng thái đã đọc không?
4. **B-P1:** Có thiết bị rẻ nào còn app gốc chạy được để làm oracle trong 7 ngày? Phạm vi DMCA §1201(f) và luật EU cho client thay thế? Có ca brick nào do vendor châu Á gây ra năm 2025–2026?
5. **B-P4:** Có bằng chứng ở châu Âu không? Có khảo sát 2025–2026 về tỷ lệ thiết bị chạy OS EOL? Có lab nào cho phép ghi trace?
6. **C-P4:** Thụy Điển, Hà Lan và Đức xử lý báo động an toàn khi rút dây đồng thế nào (trang PTS 404)? Ở Nhật, báo động an ninh có bị ảnh hưởng khi chuyển IP không? Câu "over 300 known use cases for the PSTN" thật sự nằm ở nguồn nào?
7. **A-P7:** Con số doanh thu 129 triệu USD cần đối chiếu với báo cáo năm Prosus gốc.
8. **Chung:** Overlap O1 (A-P1/C-P1) và O2 (B-P1/B-P4) vẫn được chấm riêng. Nếu gộp O2, ứng viên gộp thừa hưởng demand/international của B-P1 nhưng feasibility vẫn thấp. Quyết định E2 và E3 vẫn thuộc người dùng.

## 6. References

Tham chiếu Phase 1 dùng mã gốc (`A·Rxx`, `B·Rxx`, `C·Rxx`) và mã claim; danh sách đầy đủ nằm trong `P1/agent-*/discovery.md`. Bảng dưới chỉ liệt kê **tham chiếu mới** của Phase 2A, Agent B.

Cách chấm reference-quality (0–5 mỗi tiêu chí): Authority 20, Technical Evidence 20, Mechanism 20, Context 15, Freshness 10, Reproducibility 10, Bias 5. Weighted = Σ trọng số × điểm / 5. Cột "Truy cập" ghi `opened` khi trang được mở trực tiếp, và `snippet` khi chỉ thấy qua kết quả tìm kiếm. Nguồn snippet có Reproducibility ≤ 3 và không đủ để gắn ĐÃ XÁC MINH khi đứng một mình. Theo `calibration.md`, điểm của Agent B có xu hướng thấp hơn Coordinator khoảng 5 điểm.

| Ref ID | URL | Tiêu đề | Nhà xuất bản | Ngày xuất bản | Truy cập (cách) | Claim hỗ trợ | Auth | Tech | Mech | Ctx | Fresh | Repro | Bias | Weighted | Source Reliability | Reference Relevance |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| B2-R01 | https://blogs.windows.com/windowsexperience/2025/06/12/copilot-vision-on-windows-with-highlights-now-available-in-us/ | Copilot Vision on Windows with Highlights now available in US | Microsoft (Windows Experience Blog) | 2025-06-12 | 2026-11-25 (opened) | A-P2 đối thủ: Highlights chỉ chỗ bấm trong app được chia sẻ; có ở Mỹ | 5 | 4 | 4 | 4 | 5 | 4 | 3 | 85.0 | H | H |
| B2-R02 | https://9to5mac.com/2025/10/27/neato-cloud-shutdown-is-the-latest-example-of-a-failed-company-bricking-smart-products/ | Neato cloud shutdown is the latest example of a failed company bricking smart products | 9to5Mac | 2025-10-27 | 2026-11-25 (opened) | B-P1: robot Neato mất điều khiển qua app khi cloud tắt | 3 | 3 | 4 | 4 | 5 | 3 | 4 | 72.0 | M | H |
| B2-R03 | https://which.co.uk/news/article/major-telecare-providers-putting-vulnerable-customers-at-risk-during-digital-landline-switchover-afFqN9b63QEB | Major telecare providers putting vulnerable customers at risk during digital landline switchover | Which? | 2025-08-21 | 2026-11-25 (opened) | C-P4: 3/7 nhà cung cấp telecare lớn ở Anh vẫn bán thiết bị chỉ analog | 4 | 4 | 4 | 5 | 5 | 4 | 3 | 84.0 | H | H |
| B2-R04 | https://www.bose.com/soundtouch-end-of-life | Bose SoundTouch support discontinued | Bose | update 2026-05-06 | 2026-11-25 (opened) | B-P1: cloud SoundTouch tắt 06/05/2026; Bose công bố tài liệu API cho nhà phát triển độc lập | 5 | 4 | 4 | 4 | 5 | 4 | 3 | 85.0 | H | H |
| B2-R05 | https://gov.uk/government/publications/uk-transition-from-analogue-to-digital-landlines-guidance-for-local-authorities/uk-transition-from-analogue-to-digital-landlines-guidance-for-local-authorities | Moving landlines to digital technologies | DCMS / DSIT (GOV.UK) | 2025-05-28 | 2026-11-25 (opened) | C-P4: thiết bị phụ thuộc PSTN (alarm, telecare) cần nâng cấp. KHÔNG chứa câu "over 300 use cases" mà snippet tìm kiếm gán cho trang này | 5 | 3 | 4 | 4 | 5 | 5 | 4 | 84.0 | H | M |
| B2-R06 | https://www.thermofisher.com/blog/connectedlab/windows-11-instrument-workstation-upgrade/ | Preparing for Windows 11: An upgrade guide for your laboratory instrument | Thermo Fisher Scientific (The Connected Lab) | 09.01.2026 (có thể 2026-09-01) | 2026-11-25 (opened) | B-P4: Windows 10 EOL "accelerated workstation replacement planning" | 4 | 2 | 3 | 4 | 5 | 4 | 2 | 68.0 | M | H |
| B2-R07 | https://www.belkin.com/support-article/?articleNum=335419 | Wemo Support Ending – What You Need to Know | Belkin | last updated 2026-01 | 2026-11-25 (opened (trích dẫn lấy từ phần tóm tắt của công cụ fetch)) | B-P1: Belkin dừng cloud/app cho một số sản phẩm Wemo từ 31/01/2026 | 5 | 4 | 4 | 5 | 5 | 4 | 3 | 88.0 | H | H |
| B2-R08 | https://home-assistant.io/blog/2025/04/16/state-of-the-open-home-recap/ | 2 million homes strong: State of the Open Home 2025 | Home Assistant / Open Home Foundation | 2025-04-16 | 2026-11-25 (opened) | B-P1: >2 triệu cài đặt Home Assistant hoạt động (số 2024) | 4 | 4 | 3 | 3 | 4 | 4 | 3 | 72.0 | M | M |
| B2-R09 | https://blog.n8n.io/series-c/ | n8n raises $180m to get AI closer to value with orchestration | n8n | 2025-10-09 | 2026-11-25 (opened) | A-P1: n8n gọi 180 triệu USD Series C, định giá 2,5 tỷ USD | 5 | 4 | 4 | 3 | 5 | 4 | 3 | 82.0 | H | M |
| B2-R10 | https://www.soumu.go.jp/menu_seisaku/ictseisaku/telephone_network/ | 固定電話網の円滑な移行 (tiêu đề đọc từ bản mã hóa lỗi) | MIC Nhật Bản (総務省) | không rõ | 2026-11-25 (opened (văn bản tiếng Nhật bị lỗi mã hóa)) | C-P4: mạng PSTN của NTT chuyển sang IP, thiết bị hoàn tất trước 01/2025 | 5 | 3 | 3 | 3 | 3 | 3 | 5 | 70.0 | H | M |
| B2-R11 | https://developers.feedly.com/docs/how-does-deduplication-work | How does Deduplication work | Feedly | updatedAt 2026-11-10 | 2026-11-25 (opened) | C-P1/A-P1: dedup >85% trùng, cửa sổ 31 ngày, không áp trong cùng nguồn; bật mặc định; trang không nêu gói | 5 | 4 | 4 | 5 | 5 | 4 | 3 | 88.0 | H | H |
| B2-R12 | https://github.com/RSSNext/folo | RSSNext/Folo: Folo is the AI RSS Reader | GitHub (RSSNext) | không có ngày dự án | 2026-11-25 (opened) | A-P1/C-P1: reader AI mã nguồn mở AGPL-3.0, 39,4k sao | 4 | 3 | 3 | 3 | 5 | 5 | 3 | 72.0 | M | M |
| B2-R13 | https://www.ftc.gov/news-events/news/press-releases/2024/11/smart-products-surveyed-fail-provide-consumers-information-how-long-companies-will-provide-software | Smart products surveyed fail to provide consumers information on how long companies will provide software | US FTC | 2024-11 (ngày 26/11/2024 theo TechCrunch) | 2026-11-25 (snippet) | B-P1: 161/184 sản phẩm không công bố thời hạn hỗ trợ phần mềm | 5 | 4 | 4 | 4 | 4 | 3 | 5 | 83.0 | H | H |
| B2-R14 | https://www.techdirt.com/?p=511300 | Smart Home Device Maker Renders Devices Dumb Unless A New Subscription Is Paid For | Techdirt (kèm tek.no, Slashdot) | 2025-07 | 2026-11-25 (snippet) | B-P1 (Na Uy): Futurehome buộc thuê bao 1.188 NOK/năm từ 26/06/2025 cho hub đã bán đứt | 3 | 3 | 3 | 4 | 5 | 2 | 3 | 65.0 | M | H |
| B2-R15 | https://internet.watch.impress.co.jp/category/topic/trend/end_of_service/index.html | Impress Watch: chuyên mục サービス終了 | Impress Watch (Nhật) | tiêu đề 2025-07-16, 2025-10-15, 2026-01-09 | 2026-11-25 (snippet) | B-P1 (châu Á): báo Nhật đưa tin Belkin, Bose dừng cloud | 3 | 2 | 2 | 3 | 5 | 2 | 4 | 55.0 | M | M |
| B2-R16 | https://eur-lex.europa.eu/eli/reg/2024/2847/2024-11-20/eng | Regulation (EU) 2024/2847 (Cyber Resilience Act) | EUR-Lex | 2024-11-20 | 2026-11-25 (snippet) | B-P1 (EU): nhà sản xuất phải khai thời hạn hỗ trợ, thường ≥5 năm; nghĩa vụ chính từ 11/12/2027 | 5 | 4 | 4 | 3 | 4 | 3 | 5 | 80.0 | H | M |
| B2-R17 | https://www.agilent.com/en/product/software-informatics/analytical-software-suite/chromatography-data-systems/openlab-cds/outdated-software-risks | Outdated software risks (OpenLab CDS) | Agilent | không rõ (nhắc mốc 14/10/2025) | 2026-11-25 (snippet) | B-P4: Agilent không hỗ trợ đầy đủ CDS cũ trên Windows hết hỗ trợ | 4 | 2 | 3 | 4 | 4 | 2 | 2 | 62.0 | M | M |
| B2-R18 | https://repository.kulib.kyoto-u.ac.jp/dspace/bitstream/2433/283416/1/tec_20_23.pdf | Báo cáo kỹ thuật (máy hóa lỏng heli, PC điều khiển XP) | Đại học Kyoto (KURENAI) | không rõ | 2026-11-25 (snippet) | B-P4 (châu Á): nhà cung cấp không có PC thay thế, lab phải mua PC XP cũ để phục hồi | 4 | 3 | 3 | 3 | 2 | 2 | 5 | 62.0 | M | M |
| B2-R19 | https://doaj.org/article/7953c8efd5e344a389a581fcc1e048e7 | HardwareX: open-source SiLA 2 gateway cho thiết bị cũ | HardwareX (qua DOAJ) | 2020-10 | 2026-11-25 (snippet) | B-P4 đối thủ: gateway mở đưa thiết bị cũ vào SiLA 2 | 5 | 4 | 4 | 3 | 1 | 2 | 5 | 72.0 | H | M |
| B2-R20 | https://reference.opcfoundation.org/LADS/v100/docs/4 | OPC UA LADS v1.00 | OPC Foundation | không rõ | 2026-11-25 (snippet) | B-P4 đối thủ: chuẩn OPC UA cho thiết bị phân tích | 5 | 3 | 3 | 3 | 4 | 3 | 4 | 71.0 | H | M |
| B2-R21 | https://www.aarp.org/personal-technology/phasing-out-copper-phone-lines/ | Phasing out copper phone lines | AARP | không rõ (2025–2026) | 2026-11-25 (snippet) | C-P4 (Mỹ): báo động y tế dựa trên dây đồng cần kiểm tra khi chuyển | 4 | 2 | 3 | 4 | 4 | 2 | 4 | 64.0 | M | M |
| B2-R22 | https://broadbandbreakfast.com/fcc-loosens-copper-retirement-rules.md | FCC loosens copper retirement rules | Broadband Breakfast | 2025-03 | 2026-11-25 (snippet) | C-P4 (Mỹ): FCC nới quy định rút dây đồng | 3 | 3 | 3 | 4 | 5 | 2 | 4 | 66.0 | M | M |
| B2-R23 | https://www.tga.gov.au/news/news-articles/medical-devices-affected-3g-network-closure-october-2024 | Medical devices affected by 3G network closure October 2024 | TGA (Úc) | 2024-10 | 2026-11-25 (snippet (fetch timeout 2 lần)) | C-P4 (tương tự, Úc): tắt 3G ảnh hưởng báo động cá nhân | 5 | 3 | 3 | 3 | 4 | 1 | 5 | 68.0 | H | M |
| B2-R24 | https://telstra.com.au/business-enterprise/support/3g-service-closure | 3G Network Service Closure | Telstra | 2024 | 2026-11-25 (snippet) | C-P4 (Úc): thiết bị bị ảnh hưởng gồm báo động khẩn cấp cá nhân | 4 | 3 | 3 | 3 | 4 | 2 | 3 | 64.0 | M | M |
| B2-R25 | https://www.soumu.go.jp/main_content/000969369.pdf | Báo cáo MIC về cuộc gọi khẩn cấp sau chuyển IP | MIC Nhật Bản | 2024-09-26 | 2026-11-25 (snippet) | C-P4 (châu Á): sau chuyển IP phát hiện thiếu chức năng cho một số cuộc gọi khẩn cấp | 5 | 3 | 3 | 3 | 4 | 2 | 5 | 70.0 | H | M |
| B2-R26 | https://www.local.gov.uk/publications/digital-switchover-insights-partners-care-and-health-pch-digital-switchover-survey | Digital switchover: insights from the PCH survey | Local Government Association | không rõ (2025–2026) | 2026-11-25 (snippet) | C-P4: 6,3% hội đồng (4) không xác nhận được trạng thái ARC | 4 | 4 | 3 | 5 | 5 | 2 | 4 | 77.0 | H | H |
| B2-R27 | https://www.gov.uk/government/publications/telecoms-modernisation-non-voluntary-migration-checklist/telecoms-modernisation-non-voluntary-migration-checklist | Telecoms modernisation: non-voluntary migration checklist | GOV.UK | bản 2026-03 | 2026-11-25 (snippet) | C-P4: checklist bắt buộc trước khi chuyển khách hàng không chủ động | 5 | 3 | 3 | 5 | 5 | 2 | 4 | 77.0 | H | H |
| B2-R28 | https://www.gov.uk/government/publications/digital-telecare-commissioning-guidelines-alarm-receiving-centres/digital-telecare-commissioning-guidelines-alarm-receiving-centre-solutions | Digital telecare commissioning guidelines: ARC solutions | GOV.UK | không rõ | 2026-11-25 (snippet) | C-P4: hướng dẫn mua sắm ARC số, tránh giải pháp chỉ gọi thoại | 5 | 3 | 3 | 4 | 5 | 2 | 4 | 74.0 | H | M |
| B2-R29 | https://www.tunstall.co.uk/news-events/blog/2026/01/the-analogue-to-digital-switchover-housing-cannot-afford-to-drift/ | The Analogue to Digital Switchover: Housing Cannot Afford to Drift | Tunstall | 2026-01 | 2026-11-25 (snippet) | C-P4 đối thủ: nhà cung cấp lớn nhắm housing provider | 3 | 2 | 2 | 4 | 5 | 2 | 2 | 56.0 | L | M |
| B2-R30 | https://whatfix.com/resources/analyst-reports/gartner-market-guide-dap-2025/ | Gartner Market Guide for DAP 2025 (trang Whatfix) | Whatfix (trích Gartner) | 2025 | 2026-11-25 (snippet) | A-P2: thị trường DAP ~1,042 tỷ USD năm 2024, +27,7% | 3 | 3 | 2 | 3 | 5 | 2 | 2 | 57.0 | M | M |
| B2-R31 | https://blog.google/products/gemini/gemini-live-updates-august-2025/ | Gemini Live: A more helpful, natural and visual assistant | Google | 2025-08 | 2026-11-25 (snippet) | A-P2 đối thủ: Gemini Live tô sáng vật thể khi chia sẻ camera | 5 | 3 | 3 | 3 | 5 | 2 | 3 | 70.0 | H | M |
| B2-R32 | https://techcrunch.com/2024/09/25/whatfix-raises-125m-to-provide-in-app-guides-to-users | Whatfix raises $125M to provide in-app guides to users | TechCrunch | 2024-09-25 | 2026-11-25 (snippet) | A-P2: Whatfix (gốc Ấn Độ) gọi 125 triệu USD; SAP mua WalkMe 1,5 tỷ USD | 3 | 3 | 3 | 3 | 4 | 2 | 4 | 61.0 | M | M |
| B2-R33 | https://support.mozilla.org/ml/kb/future-of-pocket | Pocket has shut down - What you need to know | Mozilla Support | 2025 | 2026-11-25 (snippet) | A-P4: Pocket đóng 08/07/2025; xuất dữ liệu đến 08/10/2025 | 5 | 4 | 4 | 4 | 5 | 2 | 4 | 82.0 | H | H |
| B2-R34 | https://techcrunch.com/2026/08/14/read-it-later-app-pocket-is-shutting-down-here-are-the-best-alternatives/ | Read-it-later app Pocket is shutting down: here are the best alternatives | TechCrunch | 2026-08-14 | 2026-11-25 (snippet) | A-P4: đóng cửa Pocket thúc đẩy Matter, Instapaper, Raindrop (không có số) | 3 | 2 | 2 | 4 | 5 | 2 | 4 | 58.0 | M | M |
| B2-R35 | https://blog.archive.org/2026/04/23/gone-but-not-forgotten-recovering-the-dead-web/ | Gone but Not Forgotten: Recovering the Dead Web | Internet Archive | 2026-04-23 | 2026-11-25 (snippet) | A-P4: Wayback cứu khoảng 15% URL chết trong mẫu Pew | 4 | 4 | 4 | 3 | 5 | 2 | 3 | 74.0 | H | M |
| B2-R36 | https://dev.to/iojas/when-links-disappear-how-quiet-link-rot-is-eroding-accountability-in-indian-political-reporting-3me8 | When links disappear: link rot in Indian political reporting | dev.to (cá nhân) | không rõ | 2026-11-25 (snippet) | A-P4 (châu Á): tác giả tự nói Ấn Độ không có nghiên cứu quy mô lớn | 1 | 1 | 2 | 3 | 4 | 2 | 3 | 40.0 | L | L |
| B2-R37 | https://internet.watch.impress.co.jp/docs/yajiuma/1593161.html | Bài Impress Watch về nghiên cứu Pew link rot | Impress Watch | 2024-05 | 2026-11-25 (snippet) | A-P4: báo Nhật đưa lại số liệu Mỹ (không phải bằng chứng Nhật) | 3 | 3 | 3 | 2 | 4 | 2 | 4 | 58.0 | M | L |
| B2-R38 | https://devclass.com/ai-ml/2026/01/05/dramatic-drop-in-stack-overflow-questions-as-devs-look-elsewhere-for-help/4079575 | Dramatic drop in Stack Overflow questions as devs look elsewhere for help | DevClass | 2026-01-05 | 2026-11-25 (snippet) | A-P7: xác nhận độc lập xu hướng giảm | 3 | 3 | 3 | 4 | 5 | 2 | 4 | 66.0 | M | M |
| B2-R39 | https://officechai.com/ai/stack-overflow-revenue-hits-record-high-of-129-million-even-as-ai-causes-usage-to-crater/ | Stack Overflow revenue hits record high of $129 million | OfficeChai (dẫn báo cáo năm Prosus) | 2026 | 2026-11-25 (snippet) | A-P7: doanh thu FY đến 31/03/2026 là 129 triệu USD, chủ yếu từ Stack Internal | 2 | 3 | 3 | 4 | 5 | 2 | 3 | 61.0 | L | H |
| B2-R40 | https://stackoverflow.co/company/press/archive/stack-overflow-ai-assist/ | AI for Developers, by Developers: Stack Overflow AI Assist | Stack Overflow | 2025-12-02 (GA) | 2026-11-25 (snippet) | A-P7 đối thủ: AI Assist GA; tháng 12/2025 có MCP server (stackoverflow.blog 2025-12-01) | 5 | 3 | 3 | 4 | 5 | 2 | 2 | 72.0 | H | H |
| B2-R41 | https://prtimes.jp/main/html/rd/p/000002735.000001348.html | Thông cáo Qiita về bài viết gắn tag AI | Qiita (PR TIMES) | 2025–2026 | 2026-11-25 (snippet) | A-P7 (châu Á): bài tag AI trên Qiita tăng 7.477 (2023) → 18.779 (2025) | 4 | 3 | 3 | 3 | 5 | 2 | 2 | 65.0 | M | M |
| B2-R42 | https://codezine.jp/article/detail/29652 | Báo cáo phiên thảo luận về bài viết kỹ thuật thời AI | CodeZine (Shoeisha) | 2025–2026 | 2026-11-25 (snippet) | A-P7 (châu Á): ý kiến diễn giả về giảm chủ đề và người đọc bài kỹ thuật | 3 | 1 | 2 | 3 | 5 | 2 | 4 | 51.0 | M | L |
| B2-R43 | https://www.itmedia.co.jp/news/articles/1707/27/news046.html | RSSリーダーは"オワコン"なのか? | ITmedia | 2017-07-27 | 2026-11-25 (snippet) | C-P1 (châu Á): Live Dwango Reader (livedoor Reader) đóng; Dwango gợi ý Feedly/Inoreader | 3 | 2 | 2 | 3 | 1 | 2 | 4 | 47.0 | M | L |
| B2-R44 | https://techcrunch.com/2024/11/12/particle-launches-an-ai-news-app-to-help-publishers-instead-of-just-stealing-their-work | Particle launches an AI news app | TechCrunch | 2024-11-12 | 2026-11-25 (snippet) | C-P1 đối thủ: gom nhiều bài cùng sự kiện thành một "story" | 3 | 3 | 3 | 3 | 4 | 2 | 4 | 61.0 | M | M |
| B2-R46 | https://techcrunch.com/2025/03/24/fair-code-pioneer-n8n-raises-60m-for-ai-powered-workflow-automation | Fair-code pioneer n8n raises $60M for AI-powered workflow automation | TechCrunch | 2025-03-24 | 2026-11-25 (snippet) | A-P1: n8n ~200.000 người dùng hoạt động, >3.000 khách doanh nghiệp | 3 | 4 | 3 | 3 | 5 | 2 | 4 | 67.0 | M | M |
| B2-R47 | https://advocacy.consumerreports.org/press_release/ftc-software-tethering | CR, U.S. PIRG and 15 groups call on FTC for software tethering guidance | Consumer Reports Advocacy | 2024-09 | 2026-11-25 (snippet) | B-P1 (Mỹ): 17 tổ chức yêu cầu FTC ra hướng dẫn về software tethering | 4 | 2 | 3 | 4 | 4 | 2 | 2 | 62.0 | M | M |
| B2-R48 | https://www.openhomefoundation.org/media-room/factsheet/ | Open Home Foundation factsheet | Open Home Foundation | 2026 | 2026-11-25 (snippet) | B-P1: 2,28M+ hộ dùng Home Assistant, +28%/năm | 4 | 3 | 2 | 3 | 5 | 2 | 3 | 62.0 | M | M |
| B2-R49 | https://www.caixinglobal.com/2025-10-23/tech-brief-oct-23-huawei-launches-harmonyos-6-102374640.html | Tech Brief Oct. 23 | Caixin Global | 2025-10-23 | 2026-11-25 (snippet) | B-P1 (châu Á, lân cận): MIIT nêu tên 20 thiết bị thông minh vi phạm quyền người dùng (gồm tự gia hạn bắt buộc) | 3 | 3 | 2 | 2 | 5 | 2 | 4 | 56.0 | M | L |
| B2-R50 | https://apps.apple.com/au/app/id6739802604 | Folo - AI Reader (App Store) | Apple App Store | 2026 | 2026-11-25 (snippet) | C-P1/A-P1: Folo có gói trả phí (Plus 14,99 USD/tháng) | 4 | 3 | 2 | 3 | 5 | 2 | 3 | 62.0 | M | M |
| B2-R51 | https://www.rte.ie/news/business/2025/1228/1550424-smart-home | Smart home (iRobot bankruptcy) | RTÉ | 2025-12-28 | 2026-11-25 (snippet) | B-P1: nhà sản xuất Roomba vào bảo hộ phá sản, nghi ngại hỗ trợ thiết bị | 3 | 2 | 2 | 3 | 5 | 2 | 4 | 55.0 | M | L |
