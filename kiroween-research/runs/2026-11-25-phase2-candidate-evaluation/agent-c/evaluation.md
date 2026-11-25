# Phase 2A Evaluation — Agent C

## Metadata

- Run: `2026-11-25-phase2-candidate-evaluation`; pha 2A, đánh giá độc lập đủ 8 ứng viên, giữ thứ tự brief, không chọn người thắng hay Top 3.
- Model quan sát từ launch argv của PID 25736: `codex ... -m gpt-6.1-sol -c model_reasoning_effort=high`; effort `high`. Không suy model từ tên vai trò hay metadata P1. Bắt đầu UTC: **2026-11-25T11:07:05.500Z** (thời điểm tiến trình worker từ `/proc`, không phải ước lượng); kết thúc UTC: **2026-11-25T11:32:27Z**.
- Công cụ: đọc các đầu vào chỉ định; web search/open/find; 4 GET HTTP chỉ đọc để kiểm chứng trang công khai; Python chuẩn để tính điểm và kiểm schema. **79 truy vấn tìm kiếm**; không có phỏng vấn, không thử phần cứng, không chạy mã từ repo cộng đồng, không xây sản phẩm. Nhật ký các batch từ giai đoạn mở nguồn và lỗi ở `scratch/tool-audit-final.json`; kiểm HTTP ở `scratch/http-verification.json`.
- Tài liệu tham khảo đánh giá: **55 nguồn được dùng**, trong đó **47 nguồn mới** chưa xuất hiện trong tài liệu P1; các dòng `(P1)` là nguồn đã được P1 dẫn/nhắc, nay được đọc hoặc kiểm lại, không đếm thành nguồn mới. Không tính search result, mỗi lượt fetch hay trang lỗi thành một nguồn mới.
- Cô lập: chỉ đọc ba báo cáo P1 và quality gate dùng chung, brief/rubric/prompts của P2; không đọc thư mục `agent-a/` hoặc `agent-b/` của P2, không liên lạc các evaluator khác. Chỉ ghi `agent-c/` và scratch bên trong; không commit/push, không cập nhật `progress/` vì brief P2 giới hạn vị trí ghi.
- Kiểm tra đầu ra: validator tại `scratch/validate_outputs.py` kiểm schema chính xác, 64 điểm, công thức/gate, thứ tự heading, số dòng nguồn và sự khớp giữa hai tệp; kết quả ở `scratch/validation-result.json`. Kiểm số liệu khảo sát là tính lại mẫu số/tỷ lệ từ số đếm, không tái khảo sát người trả lời.

**Lỗi truy cập và giới hạn kiểm chứng:** 17 lượt web open/find lỗi, cộng **3 GET HTTP lỗi**, tức **20 lượt truy cập không thành công**. Bảng dưới gộp theo URL, không phải theo lượt; lỗi mở lại không xóa lần đọc thành công trước đó.

| URL/trang | Kết quả thực tế | Cách xử lý và ảnh hưởng |
|---|---|---|
| [PyMeasure domain thử ban đầu](https://docs.pymeasure.org/en/latest/) | Không truy cập được | Dùng đúng Read the Docs và repo chính thức R37/R54. |
| [CSCS/Cambridge](https://cscs-itsupport.atlassian.net/wiki/spaces/FAQ/pages/21365608/Supported+Operating+Systems+for+Non-UMD+Devices) | Timeout; đường dẫn có thể bị encode dấu `+` | Không coi snippet là chứng cứ đã đọc cho EU; B-P4 international không lên 5. |
| [JAIST bản Nhật](https://www.jaist.ac.jp/iscenter/security/security-notices/eol/) và [bản Anh](https://www.jaist.ac.jp/iscenter/en/security/security-notices/eol/) | Nhật 503; Anh lần đầu mở được phần đầu nhưng các lần lấy đoạn liên quan và GET đều 503 | Không dùng câu về máy đo/Win11 chỉ có trong snippet; thay bằng Metrohm Japan đã lấy đủ nội dung. |
| [Fauquier County](https://www.fauquiercounty.gov/government/departments-a-g/county-administration/verizon-copper-line-phase-out) | 403 cả web và GET | Không nâng thành xác nhận medical-alarm migration ở NA. |
| [AARP copper retirement](https://www.aarp.org/personal-technology/phasing-out-copper-phone-lines/) | 403 | Chỉ là đầu mối, không dùng làm bằng chứng tích cực. |
| [UT Austin RSS](https://sites.utexas.edu/cofawebteam/getting-started/rss-feeds/) | Timeout | Dùng nguồn Concordia R51 đã mở; không lấy mốc cập nhật trong snippet làm quan sát sử dụng. |
| Metrohm Japan R36 | Web mở đầu thành công nhưng find/open tiếp timeout | GET chuẩn trả 200, trích được đoạn Win11, hỗ trợ 2029 và model bị loại; bản text nằm trong scratch. |
| [URL blog Mozilla thử sai](https://blog.mozilla.org/en/mozilla/pocket/) | Không mở được | Dùng Mozilla Support R21; không coi URL đoán này là một tham khảo. |
| [Google Reader blog gốc](https://googlereader.blogspot.com/2013/03/powering-down-google-reader.html), [Google spring cleaning](https://googleblog.blogspot.com/2013/03/a-second-spring-of-cleaning.html) | Redirect sang Google anti-bot, tool báo 500 | Lịch sử dựa trên claim C-P1-C1 đã được quality gate kiểm, không tuyên bố tự mở lại thành công. |
| [PCMag Yahoo! Pipes](https://uk.pcmag.com/web-sites/42482/yahoo-shutting-down-maps-and-pipes) | Non-retryable open error | Dùng A-P1-C1 đã được quality gate đối chiếu; lịch sử không phải nghiên cứu nhu cầu mới. |
| Hillingdon PDF R42 | Mở ban đầu thành công, lần mở theo dòng timeout | Giữ nguồn gốc và đoạn quyết định hiện trong kết quả tìm kiếm; số tiền là **giá trị được phê duyệt**, không là tiền đã giải ngân. |
| [Patrick Meenan blog](https://webperftest.org/) | Web timeout; GET lỗi chứng chỉ hostname | Không tắt kiểm TLS, không dùng bài 2026 chỉ thấy qua snippet làm hành vi đã xác minh của C-P1. |
| Bài Copilot ngày 12/6/2025 | URL bỏ query redirect sang blog index | Không dùng redirect như đã đọc bài cũ; R11 là tài liệu hiện hành xác nhận highlight. |

Ba lỗi cục bộ đã khắc phục: tìm `prompts/phase-2-instructions.md` từ sai cấp thư mục; `rg --files` bị môi trường phân giải thành grep không hỗ trợ flag; một patch nhật ký bị từ chối vì cùng xóa/thêm một path, trước khi thay đổi được áp dụng. Sau đó đọc đúng prompt trong run bằng Python và ghi nhật ký cuối sang tệp riêng. Không lỗi nào làm thiếu đầu vào bắt buộc hoặc thiếu ứng viên.

## 1. Method

Đã đọc theo thứ tự yêu cầu: project AGENTS → brief → rubric. Sau đó đọc các phần ứng viên ở cả ba báo cáo P1, `corrections-overlay.md`, `claim-verification.md`, `overlaps.md`, và prompt chung trong `prompts/phase-2-instructions.md`. Dùng `idea-red-team` và `user-problem-validation` để tìm đối thủ, phản chứng và phép bác bỏ; không mở workflow chờ người dùng. Chỉ đánh giá tám problem spaces đã giao, không thêm Task B hay gộp các cặp chồng lấn.

Đi theo chuỗi công nghệ lịch sử → công việc ban đầu → nghỉ/suy giảm → thay thế → phần giá trị có thể mất → hành vi hiện tại → giả thuyết. Một lời phàn nàn, giá niêm yết hay dự án nguồn mở không tự chứng minh thị trường. Tách **vấn đề tồn tại**, **người dùng đã hành động**, **họ muốn giải pháp mới này**, và **có người trả tiền**. Giá chào bán không phải doanh thu; hợp đồng được duyệt không phải hóa đơn đã trả. Không ứng viên nào đạt demand 5: chưa có hai nguồn hành vi độc lập, trong đó một nguồn định lượng, cùng đo đúng nhóm và công việc còn thiếu của đề xuất.

Nhãn dùng xuyên báo cáo: **VERIFIED / ĐÃ XÁC MINH** cho dữ kiện có nguồn chính + đối chiếu độc lập hoặc kiểm tái lập; **INFERENCE / SUY LUẬN** cho suy ra từ tài liệu; **HYPOTHESIS / GIẢ THUYẾT** cho giá trị/thiết kế/chấp nhận chưa thử; **UNKNOWN / CHƯA RÕ** cho dữ liệu không có. Xác minh rằng tài liệu *công bố* một feature không đồng nghĩa đã benchmark feature ấy. Điểm, dự toán 7 ngày và kết luận gap đều là phán đoán của evaluator; cột nhãn chỉ căn cứ chính, không biến con số điểm thành dữ kiện khách quan. H/M/L là độ tin cậy của **điểm với bằng chứng hiện có**, không phải xác suất sản phẩm thành công.

Áp dụng nguyên overlay và giữ dấu vết nhãn gốc:

- **A-P1-C2:** gốc VERIFIED → VERIFIED chỉ cho số liệu khảo sát, INFERENCE cho suy diễn overload/tệp chuyên môn. Không dùng mệt mỏi tin tức đại chúng làm demand trực tiếp.
- **A-P2-C2:** gốc VERIFIED → VERIFIED cho SAP–WalkMe/TipKit, INFERENCE cho quy mô kinh tế hay động cơ Apple. Dùng triển khai hiện tại R13 thay vì suy nhu cầu mua từ thương vụ 2024.
- **B-P4-C1:** gốc ĐÃ XÁC MINH → tách hiện tượng lab giữ OS EOL được xác minh khỏi giá 10.000 USD và chi tiết XP/eBay chỉ được kể năm 2021, giữ SUY LUẬN. Không dùng con số cũ như chi phí hiện tại. B-P4-C2 chỉ đại diện khoa Hóa UW–Madison, không mọi lab.
- **A-P7-C2:** 30.903 là toàn khảo sát, 16.985 là câu hỏi khác. R22 dùng một câu hỏi riêng **n=14.304**; phép cộng sáu số đếm và 6.872/14.304 có thể kiểm lại, không trộn mẫu. Không cần suy giảm câu hỏi lần nữa để chứng minh nền tảng đã đóng.
- **B-P1-C5:** VERIFIED chỉ rằng bài báo báo cáo kết quả; chưa tái lập độc lập. **C-P4-C3** giữ INFERENCE cho suy rộng từ mẫu ARC; **C-P4-C4** không dựa vào lần mở cũ bị chặn. Phần Delicious của A-P4-C1 chưa được quality gate kiểm lại, nên không tăng độ chắc chắn cho mốc đó.

Hai kiểm tra mới sửa cách hiểu quan trọng mà không sửa tệp P1: Mozilla hiện ghi **12/11/2025** là mốc tắt export/API, thay mốc kế hoạch 08/10 trong lớp kiểm cũ (R21, đối chiếu R53); và hiện có bằng chứng chính thức về đối thủ SO for Agents, Copilot highlight, Feedly cross-language event grouping. Đây là cập nhật chứng cứ, không phải thay trọng số.

Mỗi ứng viên nhận đủ tám điểm nguyên 0–5; tổng = Σ(weight × score / 5), làm tròn một chữ số. Trọng số: 20/15/15/15/10/10/10/5; theme gate duy nhất được brief quy định là **theme ≥3**. Không thêm gate pháp lý/innovation thành quy định chính thức. Các đánh giá “NEEDS EVIDENCE” là trạng thái nghiên cứu, không tự loại hàng khỏi bảng. Official judging và Kiro implementation score của bài đã xây là rubric khác.

Quét tiền lệ hackathon theo tên công nghệ/công việc: A-P1 có GhostPipes (R05), C-P1 có Watcher (R55), cả hai có trang submission Kiroween 2025 đã mở. Với A-P2/A-P4/A-P7, các truy vấn Devpost theo Apple Guide/coachmarks/Pocket/verified Stack Overflow chưa cho analogue trực tiếp đủ kiểm; với B-P1/B-P4/C-P4 đã thử `Kiroween (Nest OR Wemo OR cloud shutdown)` và `Kiroween (scientific instrument OR laboratory OR telecare)`, chỉ gặp trùng từ hoặc bài khác công việc. **UNKNOWN**, không suy vắng kết quả thành tính mới. Mã OSS, bài báo và sản phẩm thương mại vẫn là đối chứng chính; không chạy demo hay code của các bài hackathon.

Feasibility giả định một nhóm nhỏ có thể dùng Kiro bình thường, bắt đầu ngay và làm core tối đa 7 ngày; deadline được R49 ghi **04/12/2026 14:00 PST = 22:00 UTC**. Không xác nhận tài khoản/credits hoặc thiết bị nào của nhóm. Mọi lịch 7 ngày dưới đây là **HYPOTHESIS**, không cam kết delivery hay kế hoạch được phê duyệt triển khai. Nguồn công khai không tự cho quyền tái phân phối: core demo chỉ dùng dữ liệu tự sở hữu, giấy phép mở phù hợp hoặc quyền cấp riêng được xác nhận.

## 2. Score table

Điểm tham khảo theo **thứ tự brief**, không phải thứ hạng. PASS không đồng nghĩa đã vượt mọi câu hỏi về nhu cầu/khác biệt hay được bảo đảm đủ điều kiện cuộc thi.

| ID | Ứng viên | Demand 20 | Intl 15 | Innovation 15 | Theme 15 | AI 10 | Feasibility 10 | Demo 10 | Sustainability 5 | Tổng /100 | Theme gate |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
| A-P1 | Yahoo! Pipes | 3 | 3 | 1 | 5 | 3 | 4 | 4 | 4 | 65.0 | PASS |
| A-P2 | Apple Guide | 3 | 4 | 2 | 5 | 4 | 3 | 4 | 4 | 71.0 | PASS |
| A-P4 | Del.icio.us và Pocket | 4 | 4 | 1 | 4 | 3 | 5 | 4 | 4 | 71.0 | PASS |
| A-P7 | Stack Overflow | 4 | 3 | 1 | 2 | 3 | 4 | 4 | 3 | 59.0 | FAIL |
| B-P1 | Thiết bị mất cloud/app | 4 | 3 | 2 | 4 | 5 | 1 | 3 | 3 | 64.0 | PASS |
| B-P4 | Thiết bị khoa học khóa vào OS EOL | 3 | 3 | 3 | 3 | 3 | 1 | 3 | 3 | 56.0 | PASS |
| C-P1 | Google Reader | 3 | 3 | 2 | 4 | 4 | 4 | 4 | 4 | 67.0 | PASS |
| C-P4 | Telecare khi rút PSTN | 4 | 3 | 2 | 3 | 2 | 3 | 3 | 4 | 60.0 | PASS |

## 3. Per-candidate evaluation

### A-P1 — Yahoo! Pipes

**Câu cho hội đồng quốc tế:** “Người theo dõi nhiều website có thể tự lắp một đường ống nhìn thấy được để chỉ nhận những cập nhật họ thực sự cần.”

**Lịch sử → hiện tại.** Pipes đã đóng là dữ kiện được P1 A-P1-C1 và quality gate xác minh; người dùng ban đầu kéo thả nguồn, nối module lọc và xuất feed. Giá trị mong hồi sinh là quyền lắp và kiểm từng bước, không phải RSS đã chết. **INFERENCE:** quyền kiểm soát ấy có thể hữu ích hiện nay, nhưng n8n và Inoreader đã kế nhiệm phần lớn công việc (R01–R04).

| Vùng | Người dùng đích cụ thể và mức chứng cứ |
|---|---|
| NA | Nhà nghiên cứu/thủ thư tại Concordia, Canada theo dõi journal/database alerts (R51). Có công việc theo nguồn; **chưa có bằng chứng họ thiếu visual pipe mới**. |
| EU | Người làm veille tại mạng URFIST Rennes và Association La Courroie, Pháp (R09). Tư liệu xác nhận công việc, không xác nhận demand 2025 vì ngày bìa/path mâu thuẫn. |
| Asia | Người duy trì route Bilibili/Weibo/Zhihu và người theo dõi nguồn Trung Quốc trong hệ sinh thái RSSHub (R08): **INFERENCE** về nhóm việc, không suy nơi cư trú từ ngôn ngữ route. **No evidence found** cho người không chuyên tại châu Á muốn chuyển sang pipe này; đã thử `site.n8n.io 2025 Japan research RSS workflow customers`, `site.inoreader.com/blog 2025 customer monitoring Japan university`. |

**Rào cản:** nhãn/format ngày, tokenization tiếng CJK, múi giờ và tên tổ chức đa ngữ; quyền trích nội dung, điều khoản website, chặn bot/API và yêu cầu host nội địa phải kiểm riêng. Không coi việc có route Trung Quốc là đã giải được quyền truy cập quốc tế.

**Demand 2025–26.** R06 cho thấy Lilly thực sự thử nhiều cấu hình lọc RSS và quay lại báo workaround chạy được; R07 cho thấy Marios đã nối nhiều feed với lịch sử Google Sheets và nhận lời giải. **VERIFIED** rằng có các lời kể và workflow công khai; hành vi ngoài lời kể là **INFERENCE**, không có đo thời gian hay mẫu đại diện. Hai ca cũng là phản chứng: công cụ hiện hữu giải được vấn đề. Chưa ai được quan sát chuyển sang một builder mới.

**Đối thủ/gap.** n8n là đối thủ trực tiếp mạnh nhất cho lắp luồng; Inoreader mạnh với người chỉ muốn kết quả theo dõi. R03/R04 có web feeds, filters, rules và output; không giữ giả định “phải tự host để có chức năng đó”. Đặc biệt **GhostPipes** đã tự mô tả Yahoo! Pipes + AI, có trang Kiroween 2025 (R05). Điều được kiểm là trang và framing có tồn tại; chất lượng chạy chưa rõ. Self-healing extractor chưa có đối chứng với các phương án hiện hữu nên không dùng nó để cứu novelty.

**Commercial viability — không chấm riêng.** Người có thể trả: nhóm nghiên cứu, thư viện, analyst theo dõi chuyên đề. **VERIFIED** giá chào Inoreader Pro 7,50 USD/tháng tính năm hoặc 9,99 USD tính tháng (R04); không xác nhận số khách thực trả. **HYPOTHESIS:** họ trả cho builder này. Rào cản chính là đổi thói quen, maintenance connector và chi phí AI/crawler trên công việc đối thủ đã phục vụ.

**Core ≤7 ngày và dữ liệu hợp lệ.** HYPOTHESIS: ngày 1–2 fetch ba RSS được phép và provenance; 3–4 graph/filter; 5 predicate có xác nhận và export; 6–7 đối chiếu đầu ra, lỗi và demo. RSSHub có AGPL hiện tại (R08), cần tôn trọng nếu tái sử dụng; cũng có thể chỉ viết adapter RSS chuẩn. Không cần API Yahoo đã mất; không giả định được phép scrape mọi trang.

| Tiêu chí | Điểm | Tin cậy | Nhãn hỗ trợ chính | Căn cứ và giới hạn |
|---|---:|:---:|---|---|
| `demand` | 3 | M | INFERENCE | Hai người dùng đã bỏ công cấu hình và hỏi hỗ trợ năm 2025–26; các ca đều được giải trong n8n, chưa chứng minh muốn đổi công cụ. (R06, R07) |
| `international` | 3 | M | INFERENCE | Có công việc theo dõi nguồn ở Canada/Pháp và hệ sinh thái route châu Á; chưa có ba mẫu độc lập của nỗi đau đích. (R51, R09, R08) |
| `innovation` | 1 | H | INFERENCE | Trộn/lọc trực quan đã có; chính framing Yahoo! Pipes + AI đã xuất hiện ở Kiroween 2025. (R01, R02, R03, R05) |
| `theme` | 5 | H | VERIFIED | Pipes cụ thể đã ngừng; mô hình module, dây nối và đầu ra inspectable là trung tâm cả trải nghiệm lẫn demo giả định. (A-P1-C1, R05) |
| `ai` | 3 | M | HYPOTHESIS | Predicate ngữ nghĩa hữu ích; phần fetch/merge/rule vẫn làm được không cần AI; chưa đo self-healing extractor. (R03, R10) |
| `feasibility` | 4 | M | HYPOTHESIS | 7 ngày cho 3 feed công khai, 4 loại node và RSS/JSON export; tự sửa mọi website chưa khả thi trong phạm vi đó. (R01, R08) |
| `demo` | 4 | M | HYPOTHESIS | Có thể cho thấy 3 feed thật thành 1 đầu ra trong 3 phút; chưa có phép thử user/fixture hoàn chỉnh. (R01, R02) |
| `sustainability` | 4 | M | INFERENCE | Có giá chào bán và cộng đồng duy trì; crawler ngoài nguồn được phép làm tăng chi phí và rủi ro điều khoản. (R04, R08) |


**Phản chứng mạnh nhất / thay đổi điểm.** Core đã có sản phẩm và tiền lệ cùng cuộc thi, không phải ngách chưa ai nghĩ đến. Trạng thái **NEEDS EVIDENCE** về phần việc còn thiếu; muốn nâng innovation cần cùng một tác vụ và nguồn thật cho thấy n8n/Inoreader/GhostPipes không làm được trong điều kiện công bằng. Năm người theo dõi ≥5 nguồn không RSS nếu đều dùng giải pháp sẵn có đủ tốt sẽ bác bỏ giả thuyết; thêm node mới không tự thay đổi kết luận.

### A-P2 — Apple Guide

**Câu cho hội đồng quốc tế:** “Khi hướng dẫn không giống màn hình đang mở, một Apple Guide mới chỉ đúng bước tiếp theo và kiểm tra người dùng đã làm xong.”

**Lịch sử → hiện tại.** R14 là nghiên cứu gốc của Apple: giúp ngay trong app, chia nhỏ bước, bỏ qua việc đã xong và chỉ đúng vật thể. Mốc loại khỏi OS hiện đại kế thừa từ P1 A-P2-C1; không tự suy nguyên nhân chỉ từ sự xuất hiện TipKit. **INFERENCE:** AI có thể giảm công viết kịch bản, song bài 1995 không xác nhận demand 2026.

| Vùng | Người dùng đích cụ thể và mức chứng cứ |
|---|---|
| NA | Nhân viên Salesforce/HR/procurement trong triển khai Schneider Electric tại Bắc Mỹ, có lời kể vận hành R13. Người dùng cá nhân phần mềm OSS ngoài DAP là **HYPOTHESIS** mở rộng, chưa có mẫu trực tiếp. |
| EU | Nhân viên tại doanh nghiệp Pháp Schneider Electric học SAP/Coupa/Salesforce (R13); định vị tổ chức được xác nhận, không có breakdown số ca khó UI ở Pháp. |
| Asia | Đội adoption tại Ấn Độ và Philippines được người vận hành nêu trong phỏng vấn R13. Đây là người xây/hỗ trợ nội bộ, không đại diện toàn bộ người dùng cổng công châu Á. |

**Rào cản:** ngôn ngữ/naming UI, accessibility, mức thành thạo số; màn hình có dữ liệu cá nhân/bí mật, chính sách gửi ảnh lên cloud, quyền extension và UI canvas/iframe. Tính phổ biến của “khó dùng phần mềm” không chứng minh cùng một lớp phủ được chấp nhận ở ba vùng.

**Demand.** R13 mô tả tổ chức mở rộng rollout và đầu tư con người, còn dùng để hỗ trợ thay đổi liên tục. Đây là bằng chứng hành động hiện tại qua phỏng vấn một khách hàng có tên; hiệu quả tự báo cáo chưa được audit. **UNKNOWN:** người dùng Blender/GIMP hay cổng thuế có tự cài và trả tiền cho lớp phủ khác hay không. Không dùng thương vụ SAP 2024 như proxy cho ý định mua của họ.

**Đối thủ/gap.** **Copilot Vision** là đối chứng consumer mạnh nhất cần dùng ngay, thay vì chỉ WalkMe. R11 xác nhận đọc màn hình thời gian thực và highlight; có điều kiện tài khoản/subscription và rollout, nên không gọi mọi Copilot Vision hiện tại miễn phí. Google công bố miễn phí screen sharing Gemini Live năm 2025 (R12), chưa kiểm mọi thiết bị/vùng hôm nay. Gap “AI chỉ mô tả bằng lời” ở P1 quá rộng. **HYPOTHESIS:** bộ điều kiện pre/post và khả năng từ chối bước sai tốt hơn; chưa có trial chứng minh.

**Commercial viability.** Bên trả có thể là IT/đào tạo nội bộ hoặc bên duy trì phần mềm. R13 hỗ trợ **INFERENCE** về ngân sách comparable đang được dùng; không có mức giá giao dịch công khai cho case. Động cơ mua của tổ chức có DAP không tự chuyển sang người dùng tự cài; rào cản là bảo trì mỗi app và cạnh tranh với trợ lý đã tích hợp.

**Core ≤7 ngày.** HYPOTHESIS: một web app DOM có quyền dùng, một tài liệu hướng dẫn được cấp phép và 3 trạng thái thật. Ngày 1–2 mô hình trạng thái/fixture; 3–4 grounding và highlight; 5 kiểm chứng bước; 6–7 thử UI đổi và trường hợp không tìm thấy phần tử. Không làm desktop đa OS hay tự động thao tác tài khoản thật. Dữ liệu hợp lệ là UI/tài liệu tự tạo hoặc mã nguồn mở được phép; **chưa chọn app và có baseline chạy**, nên feasibility 3.

| Tiêu chí | Điểm | Tin cậy | Nhãn hỗ trợ chính | Căn cứ và giới hạn |
|---|---:|:---:|---|---|
| `demand` | 3 | M | INFERENCE | Triển khai DAP và ngân sách là thật ở phân khúc doanh nghiệp; người dùng OSS/cổng công tự cài coachmark vẫn chưa được quan sát. (R13) |
| `international` | 4 | M | INFERENCE | Công việc học UI xuất hiện tại tổ chức Pháp, NA và các trung tâm châu Á; chưa đủ ba mẫu độc lập của phân khúc ngoài DAP. (R13, R12) |
| `innovation` | 2 | M | INFERENCE | Copilot đã highlight chỗ cần thao tác; lợi thế state pre/postcondition là giả thuyết hẹp, chưa chứng minh hơn công cụ đó. (R11, R12) |
| `theme` | 5 | H | VERIFIED | Apple Guide cụ thể là mỏ neo; bỏ qua bước đã làm và khoanh vật thể thật khôi phục đúng cơ chế lịch sử. (A-P2-C1, R14) |
| `ai` | 4 | M | INFERENCE | Grounding giao diện sống và kiểm tra trạng thái có oracle DOM; giảm công viết script có giá trị nhưng chưa đo độ chính xác. (R11, R14) |
| `feasibility` | 3 | M | HYPOTHESIS | 7 ngày chỉ đủ extension trên một web app DOM có quyền dùng; canvas, iframe, đa OS là rủi ro vật chất. (R11, R14) |
| `demo` | 4 | M | HYPOTHESIS | Một tác vụ thật với bước bị bỏ sót/đã hoàn tất cho before/after rõ; chưa có benchmark trên app đã chọn. (R14) |
| `sustainability` | 4 | M | INFERENCE | Ngân sách adoption có bằng chứng; người trả tiền cho user-side extension và chi phí support từng app vẫn chưa rõ. (R13, R11) |


**Phản chứng / thay đổi điểm.** Copilot đã làm phần thị giác được cho là khác biệt; một demo đẹp chưa chứng minh ít lỗi hơn. **NEEDS EVIDENCE**. Quan sát cùng tác vụ trên cùng app, đảo thứ tự công cụ với ít nhất 5 người, đo hoàn thành/sai bước/thời gian; không cải thiện so với Copilot hoặc hướng dẫn sẵn có thì không nâng innovation. Chỉ nâng feasibility khi chọn app thật, có quyền và thử được việc bám DOM sau UI thay đổi.

### A-P4 — Del.icio.us và Pocket

**Câu cho hội đồng quốc tế:** “Thư viện bài đọc của bạn phải còn mở được khi liên kết chết hoặc dịch vụ lưu bài đóng cửa.”

**Lịch sử → hiện tại.** Pocket phục vụ đọc sau và lưu nội dung; Delicious phục vụ bookmark/tags xã hội. Pocket đóng 8/7/2025 là **VERIFIED** qua P1 và R21. **Cập nhật được đối chiếu:** export/API tắt 12/11/2025 (R21/R53), nên bản core phải nhập tệp đã có, không hứa lấy lại thư viện từ Pocket hiện nay. Phần social graph của Delicious không tự phục hồi từ CSV.

| Vùng | Người dùng đích cụ thể và mức chứng cứ |
|---|---|
| NA | Thành viên Ottawa PC Users’ Group, Canada, được hướng dẫn chuyển Pocket sang Instapaper tháng 7/2025 (R18). Đó là hành động hỗ trợ thực; không biết có bao nhiêu người hoàn tất. |
| EU | Người đọc dùng wallabag/managed host Pháp muốn giữ archive xuất được (R15/R16). Có sản phẩm vận hành, nhưng bằng chứng hành vi EU ở đây chủ yếu từ bên cung cấp, không có cohort độc lập. |
| Asia | Kỹ sư kouki_dan ở Hatena Nhật tự viết, dùng và công bố công cụ migration; nêu cả bài đã mất (R17). Một người là một trường hợp trực tiếp, không là thị trường Nhật. |

**Rào cản:** vertical text/CJK và hình ảnh, paywall/đăng nhập, quyền tác giả khi chia sẻ toàn văn, quy định dữ liệu và năng lực sao lưu. Lưu cục bộ không đồng nghĩa quyền công bố lại. Demo có thể dùng tài liệu tự sở hữu hoặc CC/OGL; public collection nên chỉ xuất metadata/link khi chưa có quyền toàn văn.

**Demand.** Có bằng chứng người dùng bỏ công di dời ở Nhật và nhóm hỗ trợ ở Canada. **INFERENCE:** tránh mất archive là nhu cầu thực của một phân khúc; **UNKNOWN:** có đủ người muốn chuyển tiếp sang local-first sau khi đã ổn với Instapaper/wallabag hay không. Không suy việc Mozilla đóng Pocket thành “đa số người dùng không muốn trả tiền”; dữ kiện ấy không đo willingness-to-pay.

**Đối thủ/gap.** Đối thủ trực tiếp mạnh nhất cho “không phải vận hành Docker vẫn giữ dữ liệu” là **Obsidian Web Clipper** (R19); **SingleFile** cho bản sao HTML độc lập (R20); wallabag cho read-later đầy đủ (R15/R16). R16 có managed host và export, nên thế lưỡng nan “SaaS mất dữ liệu hoặc phải làm sysadmin” không đầy đủ. Chưa chứng minh semantic rot và chia sẻ folksonomy là vấn đề còn thiếu khiến người dùng đổi sản phẩm.

**Commercial viability.** Người trả có thể là cá nhân lưu nghiên cứu lâu năm, nhóm thư viện hoặc tổ chức tài trợ OSS. R16 có giá chào từ 11 EUR/năm, R20 có cộng đồng duy trì; **INFERENCE**, không có dữ liệu doanh thu hay số payer. Rào cản: tiện ích local miễn phí đủ tốt, nội dung không có quyền chia sẻ, ngân sách support/extraction nhỏ. Không giả định một lần migration năm 2025 tạo recurring revenue năm 2026.

**Core ≤7 ngày.** HYPOTHESIS: 1 ngày importer HTML/CSV; 2–3 capture và checksum; 4 offline reader/export; 5 so URL với bản cũ; 6–7 xử lý lỗi và demo. Browser bookmark export tự tạo và trang có giấy phép mở tồn tại ngay; **chưa có tệp Pocket thật được cấp quyền**. Không hồi phục byte chưa từng được lưu, không cần API Pocket, không tái tạo social network.

| Tiêu chí | Điểm | Tin cậy | Nhãn hỗ trợ chính | Căn cứ và giới hạn |
|---|---:|:---:|---|---|
| `demand` | 4 | M | INFERENCE | Có người tự viết migration và nhóm người dùng tổ chức hướng dẫn năm 2025; chưa có hai bộ dữ liệu định lượng về chọn local-first. (R17, R18, R21) |
| `international` | 4 | M | INFERENCE | Nhật, Canada, hệ sinh thái Pháp có đối tượng cụ thể; bằng chứng EU chủ yếu từ bên cung cấp, chưa đạt ba mẫu độc lập. (R17, R18, R15) |
| `innovation` | 1 | H | INFERENCE | Lưu local không Docker, bản sao HTML và export managed đã tồn tại; soft-rot/sharing chưa chứng minh là job bị bỏ trống. (R16, R19, R20) |
| `theme` | 4 | H | VERIFIED | Pocket đóng cụ thể; nhập tệp và giữ thư viện là hồi sinh workflow, không phải toàn bộ Delicious social graph. (A-P4-C1, R21) |
| `ai` | 3 | M | HYPOTHESIS | Phân loại soft-404 hữu ích nhưng rules và so fingerprint vẫn giải phần lớn; chưa có tập gán nhãn đánh giá semantic rot. (R19, R20) |
| `feasibility` | 5 | M | HYPOTHESIS | Một core local nhập HTML/CSV, chụp trang được phép, mở offline có thể làm trong 7 ngày; không cần Pocket API đã tắt. (R20, R15) |
| `demo` | 4 | M | HYPOTHESIS | Bản sao thật còn đọc khi nguồn mất rất dễ thấy; chưa có thư viện Pocket của người dùng được cấp quyền. (R20, R17) |
| `sustainability` | 4 | M | INFERENCE | Giá dịch vụ và OSS duy trì có thật; quyền phân phối lại toàn văn khi chia sẻ cần được giải quyết theo từng tài liệu. (R16, R20) |


**Phản chứng / thay đổi điểm.** Nhu cầu có thật nhưng cốt lõi đã được ứng dụng local và export giải. **NEEDS EVIDENCE** về khác biệt. Lấy thư viện ≥100 liên kết trên hai năm của 5 người có quyền dùng; đo số mục thực cần mở lại trong 30 ngày và lỗi đối thủ không xử lý. Nếu họ không cần bài cũ hoặc SingleFile/Obsidian/wallabag đã đủ, không thêm AI tags để cứu điểm. Một gói dữ liệu thật cùng lỗi soft-404 có nhu cầu sửa và baseline thất bại mới làm innovation tăng.

### A-P7 — Stack Overflow

**Câu cho hội đồng quốc tế:** “Một lỗi khó đã sửa nên trở thành lời giải có phiên bản và test để người khác kiểm lại, thay vì biến mất trong cuộc chat riêng.”

**Lịch sử → hiện tại.** P1 A-P7-C1 có số câu hỏi API được quality gate tái lập; giữ đúng là số câu hỏi **không bị xóa**, không là toàn bộ tri thức mới trên Internet. Stack Overflow vẫn hoạt động, khảo sát và ra sản phẩm (R24/R25). Theo rubric, **theme 2 và FAIL gate**; không thay “official retirement” bằng từ chết lâm sàng. Không chuyển sang một sản phẩm khác đã chết để cứu gate trong đợt này.

| Vùng | Người dùng đích cụ thể và mức chứng cứ |
|---|---|
| NA | Người duy trì thư viện/dev ở Mỹ và Canada gặp lời giải AI khó xác minh; hai nước có trong nhóm mẫu lớn của survey R24. Không có thống kê lỗi biên riêng từng nước. |
| EU | Maintainer và kỹ sư tích hợp ở Đức/Anh/Pháp cần chỉ rõ version/test; các nước có trong survey R24. Cần phân biệt suy luận dùng chung cơ chế với quan sát lỗi của từng nơi. |
| Asia | Maintainer/kỹ sư ở Ấn Độ; survey có người trả lời từ đây. **No evidence found** cho hành vi đóng góp bản sửa lỗi đã ẩn danh sang kho mới tại châu Á; đã thử `site.survey.stackoverflow.co/2026 AI trust Stack Overflow countries`, `site.stackoverflow.blog 2026 human verified AI answers Stack Overflow`. |

**Rào cản:** tiếng Anh kỹ thuật, NDA/mã nguồn riêng, khả năng chạy lại môi trường, giấy phép code/log và thông tin nhận dạng. Scan token chỉ là một lớp (R27), không bảo đảm loại mọi bí mật hoặc quyền của bên thứ ba. Chỉ dùng bug OSS có license rõ hoặc ca do nhóm tự sở hữu, có human review trước khi chia sẻ.

**Demand.** R22 có n=14.304 và số đếm kiểm được; 6.872 chọn tin AI khi dễ xác minh. R23 hỏi về attribution và context; các mẫu không được trộn. R07 cho thấy một người thật phải làm MRE trong diễn đàn khác năm 2025. **INFERENCE:** xác minh và chuẩn hóa lời giải có chi phí; **UNKNOWN:** willingness-to-contribute/pay cho kho công khai mới. Khảo sát về trust không tự chứng minh nhu cầu một mạng xã hội kỹ thuật mới.

**Đối thủ/gap.** **Stack Overflow for Agents** là đối thủ trực tiếp hơn chỉ chatbot hoặc GitHub Issues: R25 nêu TIL, Playbooks, verification, quyền duyệt và privacy. Tài liệu chính hãng tự thừa nhận giá trị vẫn đang được kiểm chứng. **INFERENCE:** khoảng trống P1 “không có vòng chia sẻ bugfix từ agent” đã bị thu hẹp mạnh; chưa có benchmark chứng minh bản ghi test tự tái lập của ứng viên vượt SOFA + GitHub (R26). Không coi lời quảng cáo SOFA là bằng chứng mọi vấn đề được giải, nhưng cũng không bỏ qua nó.

**Commercial viability.** Payer giả định là đội dev, maintainer sponsor hoặc tổ chức tài trợ knowledge commons. Có hạ tầng cộng đồng duy trì R25/R26, nhưng **UNKNOWN** dòng tiền cho kho mới; dữ liệu giá/khách hàng enterprise khác không xác nhận tính sống được của commons. Rào cản lớn nhất là động cơ đóng góp và quyền chia sẻ, không chỉ chi phí hosting.

**Core ≤7 ngày.** HYPOTHESIS: một bug OSS, fix có license phù hợp, lockfile và test fail/pass; 1–2 ngày chụp provenance, 3–4 thu nhỏ ca lỗi, 5 dựng note, 6–7 kiểm lại với môi trường sạch và human review. Chỉ **xuất file**, không cần công bố lên dịch vụ. Không tuyên bố “ẩn danh an toàn tự động” hay “chi phí đóng góp gần 0”. Dữ liệu công khai được đọc không mặc nhiên được relicensing.

| Tiêu chí | Điểm | Tin cậy | Nhãn hỗ trợ chính | Căn cứ và giới hạn |
|---|---:|:---:|---|---|
| `demand` | 4 | M | INFERENCE | Khảo sát hiện tại cho thấy cần kiểm chứng và có ca tốn công tạo MRE; ý định đóng góp công khai sang kho mới chưa rõ. (R22, R23, R07) |
| `international` | 3 | M | INFERENCE | Khảo sát gồm Mỹ/Đức/Ấn Độ nhưng không có phân tách nỗi đau lỗi biên từng vùng; cơ chế chung có căn cứ, không nhận điểm 5. (R24, R22) |
| `innovation` | 1 | H | INFERENCE | SO for Agents đã chia sẻ TIL/Playbooks và verification; GitHub đã có answers; gói test tái lập chỉ là khoảng trống chưa benchmark. (R25, R26) |
| `theme` | 2 | H | VERIFIED | Stack Overflow còn hoạt động và ra sản phẩm mới; giảm câu hỏi không phải thông báo nghỉ chính thức theo anchor. (A-P7-C1, R24, R25) |
| `ai` | 3 | M | HYPOTHESIS | Cô lập lỗi, kiểm test và provenance có độ sâu; khả năng AI tự rút MRE/ẩn danh an toàn chưa được chứng minh ở đây. (R07, R27) |
| `feasibility` | 4 | M | HYPOTHESIS | 7 ngày cho một bug OSS có phép dùng, test fail/pass và xuất note có người duyệt; không chứng minh tự động hóa mọi codebase. (R07, R26) |
| `demo` | 4 | M | HYPOTHESIS | Một lỗi thật và test fail/pass có before/after; hiệu quả cộng đồng cần người dùng thứ hai nên không chấm 5. (R07, R25) |
| `sustainability` | 3 | L | HYPOTHESIS | OSS hoặc đội dev tài trợ là hợp lý; chưa có người trả tiền cho kho công khai mới hay động cơ chia sẻ qua NDA. (R25, R26) |


**Phản chứng / thay đổi điểm.** Chính nền tảng đang bị gọi chết đã ra đối thủ gần cùng cơ chế. **REJECTED cho điều kiện theme của run**, còn nghiên cứu nhu cầu đứng độc lập. Chỉ thông báo nghỉ chính thức hoặc thay anchor được người dùng cho phép mới đổi gate; một bugfix tốt không đổi theme. Innovation tăng chỉ khi phép thử cùng bug/repo cho thấy gap cụ thể trong SOFA/GitHub; demand tăng khi có hành vi đóng góp lặp lại sau human review, không chỉ nói thích provenance.

### B-P1 — Thiết bị bị bỏ cloud/app

**Câu cho hội đồng quốc tế:** “Một thiết bị bạn đã mua vẫn phải điều khiển được khi nhà sản xuất tắt ứng dụng hoặc máy chủ.”

**Lịch sử → hiện tại.** **VERIFIED:** Belkin tắt cloud/app một số Wemo 31/1/2026 qua R28 và nguồn độc lập R52; ngoại lệ HomeKit đã cấu hình/Thread còn hoạt động. Nest mất app/cloud trên model cụ thể nhưng vẫn chỉnh tại máy (R31). Vì vậy “brick hoàn toàn” không đúng cho mọi ví dụ: cần chỉ rõ chức năng mất và model, không dùng cả nhóm IoT như một công nghệ đã chết.

| Vùng | Người dùng đích cụ thể và mức chứng cứ |
|---|---|
| NA | Chủ Nest gen 1/2 ở Mỹ/Canada; R31 nêu offer cho hai nước. Chủ Wemo dùng cloud/app là nhóm cụ thể; forum R30 không đủ dữ liệu gán quốc tịch. |
| EU | Chủ Nest gen 2 bản Europe 2014 được Google liệt kê (R31). Không suy chính sách thermostat/mạng điện giống Mỹ. |
| Asia | Hộ gia đình sở hữu thiết bị Wemo/Nest nhập khẩu là **HYPOTHESIS** phân khúc. **No evidence found** cho demand độc lập ở châu Á; đã thử `Wemo サービス 終了 2026 Home Assistant 日本` và các truy vấn Google/Belkin EOL. Menu chọn quốc gia trên website hãng không là bằng chứng sử dụng tại đó. |

**Rào cản:** model/firmware, điện áp/radio, heating plant và ngôn ngữ; quyền sửa, EULA/firmware, khả năng phân phối client và bảo mật phải kiểm theo thiết bị/thị trường. Không có kết luận pháp lý chung cho reverse engineering. Local control không tự thay được secret/attestation hay trạng thái cloud đã mất.

**Demand.** R30 là hành vi hiện tại: người dùng cố giữ thiết bị, thử pywemo để đổi Wi-Fi và tìm trợ giúp; sau đó tự báo đã chạy được. R33 là dự án sửa firmware có installer và các chế độ self-host. **INFERENCE:** có người bỏ công cứu phần cứng; quy mô payer chưa rõ. Ca R30 đồng thời cho thấy giải pháp đã có thể đủ, không chỉ cho thấy nhu cầu chưa đáp ứng.

**Đối thủ/gap.** **Home Assistant + pywemo** mạnh nhất cho Wemo; NLE mạnh cho Nest cũ (R29/R33). R33 đã có lựa chọn cloud hoặc local server, nên “mọi cứu hộ lại bắt buộc SaaS khác” cũng sai. Paper R32 là đối thủ về phương pháp; một wrapper của pipeline đã công bố không thành innovation 5. Gap long tail chỉ có nghĩa khi chỉ được thiết bị không có client hoạt động; chưa có model đó trong tay.

**Commercial viability.** Chủ thiết bị, tổ chức repair/OSS hoặc bên đặt bounty có thể tài trợ. R33 tự nêu bounty; đã kiểm trang dự án, **chưa kiểm độc lập số tiền/điều khoản**, không dùng như doanh thu chắc chắn. Google offer mua thiết bị mới (R31) là lựa chọn thay thế về chi phí, không là bằng chứng ai trả tiền cho cứu hộ. Bảo trì nhiều firmware và đường pháp lý là rào cản chính.

**Core ≤7 ngày.** **UNKNOWN ở điều kiện tiên quyết:** chưa xác nhận hardware, app gốc còn chạy và quyền thu trace. Nguồn giấy R32 có CC BY, HA có tài liệu local và NLE có mã/firmware công khai, nhưng quyền dùng binary/phân phối và độ phủ phải kiểm riêng. Nếu có thiết bị + oracle ngày 1, có thể thử **một** read-only operation hoặc toggle an toàn, so trace và gắn báo cáo coverage trong 7 ngày; hiện không chấm như điều kiện ấy đã được đáp ứng. Không chạy code cộng đồng hoặc flash thiết bị trong run nghiên cứu này.

| Tiêu chí | Điểm | Tin cậy | Nhãn hỗ trợ chính | Căn cứ và giới hạn |
|---|---:|:---:|---|---|
| `demand` | 4 | M | INFERENCE | Người dùng bỏ công giữ thiết bị và dự án cứu Nest tồn tại; ca Wemo đã tự báo giải xong, chưa có quy mô chi trả cứu thiết bị. (R28, R30, R33) |
| `international` | 3 | M | INFERENCE | Nest có bản NA/EU bị ảnh hưởng; chưa mở được bằng chứng độc lập về người dùng châu Á, không suy từ bán hàng toàn cầu. (R31, R28) |
| `innovation` | 2 | M | INFERENCE | HA/NLE đã cứu nhiều model và paper đã mô tả cơ chế AI; long tail không có client là khoảng trống plausible nhưng chưa chọn model. (R29, R33, R32) |
| `theme` | 4 | M | VERIFIED | Wemo cloud/app đã tắt có xác nhận chính thức và độc lập; cần chọn một model thật làm mỏ neo thay vì kể chung IoT. (R28, R52) |
| `ai` | 5 | M | INFERENCE | Paper chứng minh được phương pháp có oracle hành vi và replay; điểm cho cơ chế được báo cáo, không phải đã tái lập hay cứu cloud mất state. (R32) |
| `feasibility` | 1 | L | UNKNOWN | Chưa xác nhận có thiết bị và app gốc/trace trong tay; code công khai không thay được oracle phần cứng, tổng quát hóa chưa được chỉ ra. (R32, R33) |
| `demo` | 3 | L | HYPOTHESIS | Bật thiết bị thật khi ngắt cloud sẽ rõ; hiện không có hardware để bảo đảm demo dưới 3 phút. (R29, R33) |
| `sustainability` | 3 | M | INFERENCE | Cộng đồng có duy trì và hình thức bounty; chưa có pháp lý/license rõ cho mọi firmware và chưa có kinh tế bảo trì long tail. (R29, R33) |


**Phản chứng / thay đổi điểm.** Phương pháp R32 cần nhiều can thiệp và tài nguyên, không chứng minh khôi phục cloud đã biến mất; đối thủ local đã giải nhiều ví dụ. **NEEDS EVIDENCE**. Nâng feasibility chỉ sau khi có model/firmware hợp lệ, app/trace, chức năng baseline và test lặp trên phần cứng; nếu model đã dùng HA/NLE đủ tốt thì hạ innovation. Không đổi sang thêm model/tính năng để né phép bác bỏ đó.

### B-P4 — Thiết bị khoa học khóa vào OS EOL

**Câu cho hội đồng quốc tế:** “Một máy đo còn tốt không nên bị loại chỉ vì máy tính và phần mềm điều khiển cũ không thể thay.”

**Lịch sử → hiện tại.** Giữ nguyên overlay về B-P4-C1/C2: hiện tượng lab giữ máy OS EOL đã được xác minh, chi phí 10.000 USD là câu chuyện 2021, không phải giá 2026. R50 neo một OS cụ thể đã nghỉ hỗ trợ. R34 là cập nhật quan trọng: Agilent **không** tuyên bố OpenLab hết hỗ trợ theo Windows; R39 cũng phân biệt retail Windows 10 với instrument editions. Không biến mốc 14/10/2025 thành mọi lab buộc đổi máy ngay.

| Vùng | Người dùng đích cụ thể và mức chứng cứ |
|---|---|
| NA | Lab life sciences/chemistry tại UCSB giữ instrument-control computers sau firewall khi không nâng được (R35); UW–Madison trong P1 chỉ đại diện khoa đó. |
| EU | Lab hóa/sinh tại Cambridge là nhóm đích giả định hợp lý, **chưa xác nhận được ca độc lập đã mở**. **No evidence found** đạt chuẩn trong time box; đã thử `site.cam.ac.uk "Windows 10" "instruments" "2025"`, `site.ox.ac.uk "Windows 10" "instruments" "2025"`, và nguồn CSCS bị timeout. Không suy quốc gia từ trụ sở vendor. |
| Asia | Người vận hành tiamo 1.x/2.x/3.0 và các titrator đời cũ tại Nhật: Metrohm Japan thông báo không Win11 và liệt kê model không qua OMNIS (R36, GET 200). Đây là thông báo cho khách hàng, không là khảo sát số lab còn sử dụng. |

**Rào cản:** driver/board/cáp độc quyền, thuật ngữ và manual đa ngữ, đơn vị/hiệu chuẩn; quyền dùng app/firmware và yêu cầu validation theo loại lab. Không áp GxP lên mọi lab, cũng không gọi một graph đẹp là dữ liệu đo hợp lệ. Không có chứng nhận hay kiểm metrology trong run.

**Demand.** R35 cho phép workaround cụ thể và tính phí support/migration, R34/R36 xác nhận các đường nâng cấp và giới hạn. Đó là bằng chứng vấn đề còn được vận hành hiện tại, không có cohort chi tiền mua client độc lập 2025–26. **UNKNOWN:** tỷ lệ máy mắc kẹt, thiệt hại và người muốn đổi workflow. Cô lập mạng là lựa chọn có chủ đích, không chỉ là lỗi chờ app mới sửa.

**Đối thủ/gap.** Đối thủ mạnh nhất trên thiết bị được hỗ trợ là **upgrade/service của vendor**, không phải không có giải pháp; R38/R39 cho engineer và service contracts. Đối thủ OSS mạnh là **PyMeasure/PyVISA** với driver và SCPI/GPIB/serial đã có (R37/R54). Gap đáng kiểm là thiết bị chưa có driver/tài liệu hoặc model không qua successor (R36), nhưng suy protocol từ router sang instrument vẫn là **HYPOTHESIS**. Không chọn một driver đã có rồi gọi là hồi sinh mới.

**Commercial viability.** Trưởng lab/facility, trường đại học hoặc quỹ duy trì hạ tầng nghiên cứu là payer/funder giả định. R38 có dịch vụ theo quote và validation tùy chọn; R39 có nâng cấp nằm trong service contract. **VERIFIED về dịch vụ chào bán/điều khoản**, **UNKNOWN giá giao dịch và demand cho đội độc lập**. Procurement, hiệu chuẩn, hỗ trợ lâu dài và license là rào cản, không lấy giá cũ 10.000 USD để khẳng định ROI.

**Core ≤7 ngày.** Chưa có instrument thật, app/license và trace số đo được cấp quyền. Tài liệu PyMeasure và mã MIT (R54) dùng được theo license; simulator có thể kiểm serialization, không làm oracle về số đo/hành vi điện. Nếu không có thiết bị/oracle ngay ngày đầu thì core “cứu instrument” không được chứng minh trong 7 ngày. Một trình đọc file mẫu có phép dùng có thể làm được nhưng là scope khác, không tự nâng điểm cho bài điều khiển thiết bị đã giao.

| Tiêu chí | Điểm | Tin cậy | Nhãn hỗ trợ chính | Căn cứ và giới hạn |
|---|---:|:---:|---|---|
| `demand` | 3 | M | INFERENCE | Chính sách cô lập máy và vendor chuyển OS xác nhận vấn đề hiện tại; chưa có chi tiêu/đơn đặt thay client độc lập năm 2025–26. (R34, R35, R36) |
| `international` | 3 | M | INFERENCE | NA và Nhật có nguồn chính cụ thể; EU chỉ thấy tài liệu không mở đủ, không suy mọi lab đều giống nhau. (R35, R36) |
| `innovation` | 3 | M | INFERENCE | Driver mở và nâng cấp vendor che phủ phần lớn; model không qua bản mới còn là khoảng trống có căn cứ nhưng chưa được thử. (R37, R36, R39) |
| `theme` | 3 | M | VERIFIED | OS cụ thể như XP đã nghỉ hỗ trợ neo workflow điều khiển thiết bị; chưa chọn instrument EOL cụ thể, không gọi mọi Windows10 là chết. (R50, B-P4-C1) |
| `ai` | 3 | L | HYPOTHESIS | Suy giao thức từ trace có tiềm năng; chuyển từ router sang GPIB/USB khoa học chưa có bằng chứng thực nghiệm. (R32, R37) |
| `feasibility` | 1 | L | UNKNOWN | Chưa có instrument, app hợp lệ, trace và oracle số đo trong tay; simulator không kiểm được sai số thật hay driver riêng. (R37, R39) |
| `demo` | 3 | L | HYPOTHESIS | Đồ thị đo trước/sau có thể kể được nhưng cần hardware và giải thích sai số; mô phỏng không đủ bằng chứng cứu thiết bị thật. (R37) |
| `sustainability` | 3 | M | INFERENCE | Có ngân sách dịch vụ instrument tương đương, nhưng license, validation và trách nhiệm số đo của client thay thế còn mở. (R38, R39, R54) |


**Phản chứng / thay đổi điểm.** Nhiều máy được vendor tiếp tục hỗ trợ hoặc có extended OS lifecycle; lab có thể nhận rủi ro bằng firewall. **NEEDS EVIDENCE** và điều kiện dữ liệu/phần cứng còn thiếu. Nâng điểm khi lab cung cấp một model cụ thể, quyền dùng app/trace, phép đo chuẩn, baseline PyMeasure/vendor thất bại và lỗi có thể tái lập. Nếu đã có driver hoặc vendor upgrade hợp ngân sách thì hạ novelty/demand của client mới, không mở rộng tính năng để tránh đối chứng.

### C-P1 — Google Reader

**Câu cho hội đồng quốc tế:** “Theo dõi những nguồn bạn chọn, đọc một sự kiện một lần và thấy rõ điều gì vừa mới thay đổi.”

**Lịch sử → hiện tại.** C-P1-C1 được P1/quality gate xác minh Reader đóng 1/7/2013; mở lại blog bị Google chặn nên không nhận là kiểm lại thành công. Khôi phục subscriptions và trạng thái đọc có mỏ neo cụ thể, nhưng **RSS vẫn hoạt động**. Giá trị “chỉ đọc phần mới của cùng sự kiện” là **HYPOTHESIS** phát triển workflow chứ không phải một tính năng lịch sử Reader đã làm tốt rồi bị mất.

| Vùng | Người dùng đích cụ thể và mức chứng cứ |
|---|---|
| NA | Nhà nghiên cứu Canada nhận journal/database alerts tại Concordia (R51); đây là bằng chứng công việc theo nguồn, chưa đo đọc lặp event. |
| EU | Người làm veille tại URFIST Rennes/La Courroie (R09); cần định nghĩa task multilingual theo nghề chứ không dùng thống kê news fatigue đại chúng. |
| Asia | Đội R&D news aggregator/analyst tại Ấn Độ là nhóm đích **HYPOTHESIS**; R47 của TCS Research xác nhận bài toán kỹ thuật, không nêu nơi cư trú người đọc hay phân bố dataset theo vùng. R10 hỗ trợ nhu cầu xử lý ngôn ngữ châu Á ở mức sản phẩm. **No evidence found** cho cohort trực tiếp muốn semantic delta. Đã thử `site.inoreader.com/blog 2025 user story`, `site.feedly.com customers Asia Japan intelligence 2025`, và các truy vấn duplicates 2025–26; bài Patrick 2026 không đọc được nên loại khỏi chứng cứ hành vi. |

**Rào cản:** tên/sự kiện khác ngôn ngữ, bản cập nhật có nội dung mâu thuẫn chứ không lặp, paywall và quyền dùng full text. Có nguồn tiếng Nhật/Việt không bảo đảm model phân biệt đúng mọi chi tiết mới. Không được tự đánh dấu “đã biết” rồi giấu tin quan trọng khi model chưa chắc.

**Demand.** R07 có người làm history/filter để không nhận lại mục đã gửi năm 2025, nhưng job là trùng URL và đã được n8n giải. R47 nghiên cứu near-duplicate hiện tại, không đo demand mua UI mới. **INFERENCE:** giảm lặp là vấn đề có thật; **UNKNOWN:** người dùng cần delta giữa hai bản cùng sự kiện hơn mức các reader đã làm. Không dùng bài/blog chỉ thấy search snippet để tăng demand lên 4–5.

**Đối thủ/gap.** **Feedly** là đối chứng mạnh nhất. R48 chỉ mô tả một feature ngưỡng >85%/31 ngày và ngoại lệ, **không bao quát toàn sản phẩm**. R10 còn công bố grouping cùng event xuyên 15 ngôn ngữ. Inoreader có duplicate filters theo URL/title và edit history (R03/R04). **Watcher** ở Kiroween 2025 đã tự mô tả UI Reader, LLM selectors và key/value state diff (R55); đó là theo dõi thay đổi một website, chưa phải delta factual giữa nhiều nguồn. Do đó cả revival framing và “gom cùng sự kiện” đều không mới. **HYPOTHESIS:** delta có trích nguồn và provenance đọc có thể khác; chưa benchmark Feedly/Ask AI hay chi phí, không chấm gap đã được chứng minh.

**Commercial viability.** Cá nhân reader chuyên sâu hoặc nhóm intelligence có thể trả. R04 có giá và R10 có plan enterprise; **INFERENCE** về comparable business model, không là doanh thu mới. Rào cản là chênh lệch chất lượng ít thấy, đổi reader, quyền nội dung và inference cost. Không gộp vào A-P1: ứng viên này chấm công việc **đọc/nhớ điều đã biết**, A-P1 là **lắp luồng đầu vào**.

**Core ≤7 ngày.** HYPOTHESIS: 1–2 ngày lấy 3 RSS được phép và lưu trạng thái; 3–4 ghép cặp/cụm; 5 delta gắn câu nguồn và abstain; 6–7 đối chiếu nhãn do người tạo, lỗi và demo. Dữ liệu tin do nhóm tự viết hoặc nguồn giấy phép mở có thể dùng ngay, RSS công khai chỉ là đường nhận không phải license toàn văn. Paper R47 có mô tả phương pháp, dữ liệu industrial không mặc nhiên tải/dùng được; không hứa benchmark gốc đã tái lập.

| Tiêu chí | Điểm | Tin cậy | Nhãn hỗ trợ chính | Căn cứ và giới hạn |
|---|---:|:---:|---|---|
| `demand` | 3 | M | INFERENCE | Có workaround lọc lặp hiện tại và vấn đề kỹ thuật được nghiên cứu; chưa có hành vi trực tiếp muốn giao diện semantic delta. (R07, R03, R47) |
| `international` | 3 | M | INFERENCE | Nhà nghiên cứu Canada/Pháp, nhóm xử lý feed Ấn Độ là đối tượng cụ thể; chưa đo độc lập nỗi đau người đọc ở ba vùng. (R51, R09, R47) |
| `innovation` | 2 | M | INFERENCE | Feedly có nhóm cùng event xuyên ngôn ngữ; Watcher đã hồi sinh Reader với state diff; delta giữa nhiều nguồn còn chưa đối chứng. (R10, R48, R03, R55) |
| `theme` | 4 | H | VERIFIED | Google Reader đã đóng; nguồn tự chọn, trạng thái đã đọc là mỏ neo workflow. RSS còn sống, không gọi giao thức đã chết. (C-P1-C1) |
| `ai` | 4 | M | INFERENCE | Embeddings/metadata có phương pháp được công bố, oracle nhãn cặp bài khả thi; delta factual đúng hơn baseline vẫn chưa chứng minh. (R47, R48) |
| `feasibility` | 4 | M | HYPOTHESIS | 7 ngày đủ một cụm nguồn RSS được phép và trạng thái đọc; full-text paywall và đánh giá đa ngữ phải bỏ khỏi core. (R47, R51) |
| `demo` | 4 | M | HYPOTHESIS | Một sự kiện, nhiều bài và một chi tiết mới dễ thấy; chưa có corpus thật được cấp phép/gán nhãn hoàn chỉnh để chấm 5. (R48, R47) |
| `sustainability` | 4 | M | INFERENCE | Có mô hình reader trả phí và nhu cầu tổ chức; lợi thế riêng và kinh tế inference mỗi bài chưa kiểm chứng. (R04, R10) |


**Phản chứng / thay đổi điểm.** Phần lớn công việc đã được reader sống phục vụ, và paper/Feedly đã xử lý nhiều hơn hash. **NEEDS EVIDENCE**. Cần cùng một corpus ≥30 cặp gần trùng/có chi tiết mới, quyền rõ, so Feedly và baseline rule; đo missed-new-fact, false-new và công sức người đọc. Nếu delta không giúp hoàn thành một task thật nhanh/đúng hơn, không thêm chatbot/tóm tắt để nâng innovation.

### C-P4 — Telecare continuity khi rút PSTN

**Câu cho hội đồng quốc tế:** “Khi đổi đường điện thoại của người cần chăm sóc, phải có bằng chứng chiếc nút gọi cứu trợ vẫn tới đúng người nhận.”

**Lịch sử → hiện tại.** **VERIFIED** lịch nghỉ PSTN UK 31/1/2027 qua R40/R43; không gọi mạng đã tắt ngày nghiên cứu. Công việc cũ là chuỗi alarm → ARC → người phản hồi. Giá trị cần giữ là continuity và xác nhận đầu cuối, không phải phục dựng dây đồng. Một checklist bàn giao chung không tự thành hồi sinh nếu demo không gắn rõ thiết bị/workflow PSTN đang bị rút.

| Vùng | Người dùng đích cụ thể và mức chứng cứ |
|---|---|
| NA | Người vận hành chăm sóc tại nhà/đơn vị medical alert phục vụ người cao tuổi ở Virginia là nhóm giả định từ đầu mối Fauquier. **No evidence found** đạt chuẩn mở trực tiếp về migration telecare trong time box: Fauquier và AARP 403; thử `Canada medical alarms copper retirement 2025`, `site.fcc.gov medical alert copper retirement alarms 2025`, `"medical alarms" "copper" "2026" site:fcc.gov`, `"medical alert" "copper" "2025" site:verizon.com`. Không dùng bài copper theft để chứng minh switchover. |
| EU | Housing provider, ARC và đội telecare tại Hillingdon/Scotland, UK (R40–R44). Đây là trường hợp được chứng minh mạnh nhất; không suy mọi nước EU cùng mốc UK. “EU” trong bảng vùng theo brief được hiểu là Europe, có UK. |
| Asia | Người phụ trách fire-alarm tại cơ sở ở Nhật bị thay đổi callback khi NTT chuyển IP, có FDMA và NTT (R45/R46). Đó là **analogue về báo động và migration**, không là bằng chứng tỷ lệ telecare lỗi tại Nhật. **No evidence found** cho cùng workflow telecare/PSTN Anh trong châu Á; đã thử `medical alarm copper network retirement 2025 Singapore Japan` và `site.ntt-east.co.jp 2025 緊急通報 装置 IP網 移行`. |

**Rào cản:** ownership giữa nhà mạng/housing/ARC, consent và dữ liệu dễ tổn thương, cơ chế báo động/nguồn dự phòng/tiêu chuẩn từng nơi, ngôn ngữ và khả năng dùng UI của người cao tuổi. R46 là chuyển core IP của Nhật, không đồng nghĩa cắt copper last mile cùng kiểu UK. Phần mềm hồ sơ không chứng nhận compatibility hay bảo đảm đầu cuối hoạt động.

**Demand.** R41 xác nhận mức phạt năm 2025 cho hành vi **2022–23**, đồng thời mô tả biện pháp sửa; không đếm lại thành sự cố mới 2026. R40 có nghiên cứu mẫu ARC năm 2025–26: giữ nhãn suy rộng **INFERENCE**, không TAM toàn quốc. R42 có quyết định cấp ngân sách telecare/transition trong 2026. Có hành động hiện tại và comparable spend; **UNKNOWN** nhu cầu mua công cụ bàn giao riêng sau khi đã có những quy trình ấy.

**Đối thủ/gap.** **Openreach Prove Telecare**, kỹ sư + test ARC + quy trình hiện hữu, là đối chứng mạnh hơn app checklist đơn lẻ. R43 tự báo hơn 70.000 khách được nâng cấp, R44 độc lập xác nhận quy trình đang được triển khai, không còn chỉ pilot 1.000 ở P1. Không nâng số 70.000 thành hiệu quả an toàn đã audit. Gap hồ sơ qua nhiều bên có thể còn, nhưng chưa quan sát workflow sau khi dùng dịch vụ và chưa xác nhận thiếu tính năng.

**Commercial viability.** Housing provider, council, nhà mạng hoặc ARC có thể chi. **VERIFIED** rằng Hillingdon phê duyệt hợp đồng Appello 12 tháng cho 2026 trị giá **235.364 GBP**, kèm phí setup trong quyết định (R42); đây không là giá tracker riêng, doanh thu startup hay bằng chứng đã thanh toán. Rào cản là procurement/tích hợp, quyền dữ liệu, trách nhiệm và nhu cầu còn lại sau deadline chuyển đổi.

**Core ≤7 ngày.** HYPOTHESIS: 1–2 ngày mô hình hóa bằng chứng/ownership từ hướng dẫn OGL R40; 3–4 tracker; 5 phát hiện trường thiếu bằng rule; 6–7 traceability và demo 3 bên. Tài liệu công khai dùng theo OGL, ca tự tạo có thể dùng ngay; **chưa có hồ sơ thật đã ẩn danh, API ARC hoặc thiết bị được cấp quyền**. Vì vậy chỉ demo quản lý bằng chứng giả lập, không tuyên bố kiểm chứng alarm thật. AI không được điền bằng suy đoán mục “an toàn/tương thích”.

| Tiêu chí | Điểm | Tin cậy | Nhãn hỗ trợ chính | Căn cứ và giới hạn |
|---|---:|:---:|---|---|
| `demand` | 4 | H | INFERENCE | Có nghiên cứu mẫu, hành động điều tiết và ngân sách triển khai 2026; chưa thấy người mua yêu cầu tracker bàn giao mới. (R40, R41, R42) |
| `international` | 3 | L | INFERENCE | UK được xác nhận; Nhật có analogue fire alarm/PSTN khác kiến trúc; nguồn NA về medical alert bị 403 nên chưa có bằng chứng đã mở. (R45, R46, R40) |
| `innovation` | 2 | M | INFERENCE | Prove Telecare thực hiện test và bàn giao, không còn chỉ pilot 1000; lỗ hổng phối hợp sau khi dùng dịch vụ đó chưa được chứng minh. (R43, R44) |
| `theme` | 3 | H | VERIFIED | PSTN có lịch nghỉ chính thức; phục hồi continuity trong transition đạt đúng anchor 3, không phải hồi sinh toàn mạng đồng. (R40, R43) |
| `ai` | 2 | H | INFERENCE | Checklist và test đầu cuối chịu tải; AI OCR hồ sơ giúp phần nhập liệu, không thể xác nhận alarm an toàn. (R40, R44) |
| `feasibility` | 3 | M | HYPOTHESIS | 7 ngày đủ tracker dùng tài liệu OGL và ca mô phỏng; hồ sơ được ẩn danh/ARC API và test thật chưa có quyền truy cập. (R40, R44) |
| `demo` | 3 | M | HYPOTHESIS | Phiếu bàn giao có thiếu xác nhận dễ hiểu nhưng chưa có hồ sơ khách hàng/thiết bị thật; dùng synthetic phải ghi rõ. (R42, R44) |
| `sustainability` | 4 | M | INFERENCE | Hợp đồng và dịch vụ hiện hữu có ngân sách; thị trường tracker riêng sau chuyển đổi, tích hợp và trách nhiệm vẫn chưa rõ. (R42, R43) |


**Phản chứng / thay đổi điểm.** Có nguồn lực và quy trình mạnh đang làm việc đó; tracker không sửa lỗi nguồn điện, signaling hay thiếu người chịu trách nhiệm. **NEEDS EVIDENCE**. Muốn nâng innovation cần một housing provider/ARC cho quan sát đã cấp quyền, chỉ ra failure cụ thể còn tồn tại sau Prove Telecare và workflow hiện hữu. Nếu nguyên nhân chỉ là thiếu thiết bị/kỹ sư hoặc phân quyền tổ chức thì phần mềm 7 ngày không giải quyết; không thêm AI để cứu candidate.

## 4. Rubric challenges

Các nhận xét sau **không thay điểm, anchor hay trọng số đã áp dụng**:

1. Theme gate làm một vấn đề có nhu cầu mạnh nhưng công nghệ còn sống mất điều kiện; A-P7 minh họa rõ. Đây là hệ quả đúng của anchor hiện tại, không lý do lách “giảm traffic” thành retirement. Nếu sau này chấp nhận workflow đã mất, cần thay anchor công khai cho mọi ứng viên, không chỉ một ca.
2. International 5 đòi đủ ba vùng và không rào cản lớn, nhưng một khảo sát toàn cầu hoặc vendor nhiều ngôn ngữ không chứng minh pain ở từng vùng. Rubric nên định nghĩa “bằng chứng độc lập” và cách đánh giá cùng mechanism khác deployment. Trong điểm hiện tại, UK telecare và Nhật fire alarm chỉ giúp structural generalisation, không coi là cùng thị trường.
3. Innovation có thể khiến một problem space rộng bị chấm thấp vì core đã có giải pháp, trong khi một ngách hẹp chưa được chọn còn có thể mới. Tôi chấm đúng core được giao; không cho điểm 5 dựa vào phần feature phụ chưa chứng minh. Có thể sau này tách điểm “remaining unmet job” khỏi novelty câu chuyện.
4. Feasibility và demo là dự báo trước khi có sản phẩm; thiếu hardware/oracle làm confidence thấp dù code nhỏ. Rubric nên buộc ghi bảng điều kiện “có trong tay / có thể lấy / chưa xác nhận”. Run này ghi điều kiện từng ca, không mặc định nhóm sở hữu thiết bị chỉ vì có repo online.
5. Demand 5 có quantitative evidence nhưng chưa định nghĩa định lượng nào đủ gần quyết định mua/đổi giải pháp. Counts downloads/stars, số incident và số lượt survey không thay được task cost hay adoption. Tôi không dùng chúng để chấm 5; commercial note giữ riêng theo yêu cầu.
6. Sustainability chỉ 5% dễ che rủi ro license/operation ở hardware và care. Tuy nhiên tôi không tự tạo legal gate, không tăng trọng số; các điểm 3–4 giữ nguyên và nêu giả thuyết. Điểm AI của rubric này cũng không phải điểm dùng Kiro của official judging.

Không làm sensitivity analysis hay chốt Top 3 trong pha 2A; đó là bước tổng hợp/debate được giao sau, cần giữ các điểm độc lập trước.

## 5. Unresolved questions

- **A-P1:** người không chuyên có thực sự muốn tự dựng pipe thay vì một feed đã lọc? Một tác vụ nào còn thất bại với n8n/Inoreader và đã có giấy phép dữ liệu?
- **A-P2:** state verification hơn Copilot Vision ở metric nào? Web app thật nào có DOM dùng được, quyền cài extension và user task tương đương tại các vùng?
- **A-P4:** sau migration, người dùng cần truy hồi bao nhiêu bài cũ có giá trị? Họ cần bản archive mới hay công cụ hiện có chỉ chưa được khám phá? Quyền chia sẻ toàn văn đã có chưa?
- **A-P7:** người dùng có quyền và động cơ đóng góp MRE/test không? SOFA hiện thiếu chính xác capability nào? Theme chỉ đổi nếu có quyết định về anchor, không do điểm kỹ thuật cao.
- **B-P1:** model/firmware/app/trace nào thực sự có trong tay, không được HA/NLE giải rồi? Phân phối firmware/client thế nào theo license và thị trường? Oracle có còn không?
- **B-P4:** lab và model cụ thể nào, chuẩn đo nào và ai xác nhận kết quả? Chi phí nâng cấp hiện tại và lựa chọn existing driver/vendor là gì? Không có dữ liệu đo hợp lệ thì không kết luận feasibility cao.
- **C-P1:** người đọc cần giảm lặp URL, cùng event, hay chỉ cập nhật factual delta? Có corpus hợp lệ và nhãn đối chứng baseline không? Ai trả tiền cho phần chênh lệch so Feedly?
- **C-P4:** đơn vị nào còn coordination gap sau Prove Telecare; họ có quyền cung cấp hồ sơ ẩn danh không? Có analogue trực tiếp ở NA/Asia hay chỉ cùng họ migration? Sau 2027 ai duy trì và trả tiền cho tracker?
- **Chung:** chưa có phỏng vấn hoặc session quan sát thực, chưa có cross-region task benchmark, chưa có xác nhận Kiro account/budget và hardware inventory. Thiếu bằng chứng được ghi vào confidence, không được thay bằng ý kiến evaluator khác.

## 6. References

Mỗi nguồn dưới đây chấm cho claim ở cột Claims: Authority 20%, Technical Evidence 20%, Mechanism 20%, Context 15%, Freshness 10%, Reproducibility 10%, Bias 5% (điểm bias cao = ít thiên lệch). Weighted = `4A + 4T + 4M + 3C + 2F + 2R + B`; không nhập các điểm chất lượng nguồn vào tổng ứng viên. Source Reliability và Reference Relevance tách biệt: giấy tờ chính thức có thể đáng tin nhưng chỉ liên quan gián tiếp tới demand. Ngày không có trên trang được ghi thẳng, không lấy copyright làm publication date. Điểm freshness của nguồn lịch sử đánh giá độ phù hợp với claim lịch sử, không coi nguồn ấy là khảo sát hiện tại.

Nguồn lỗi ở Metadata không được dùng để xác minh claim và không được đếm vào bảng tham khảo tích cực. Các claim lịch sử chỉ kế thừa P1 được dẫn bằng claim ID và tuân overlay; không giả vờ đã mở lại URL bị chặn. R36 được kiểm thêm bằng GET 200; R42 có lần đọc thành công trước lần truy cập theo dòng bị lỗi. Giá/tính năng là snapshot, chưa thực hiện giao dịch hay chạy sản phẩm đối thủ.

| Ref ID | URL | Title | Publisher | Pub date | Accessed | Claims | 7 scores A/T/M/C/F/R/B | Weighted /100 | Source Reliability | Reference Relevance |
|---|---|---|---|---|---|---|---|---:|---|---|
| R01 (mới) | [Nguồn](https://docs.n8n.io/integrations/builtin/core-nodes/n8n-nodes-base.rssfeedread) | RSS Read | n8n | Không ghi ngày | 2026-11-25 | A-P1: đọc RSS trong workflow | 5/4/4/5/4/4/3 | 86 | High | High |
| R02 (mới) | [Nguồn](https://n8n.io/workflows/1160-merge-data-for-multiple-executions/) | Merge data for multiple executions | n8n / Harshil Agrawal | Không ghi ngày tuyệt đối; trang nói updated 4 days ago | 2026-11-25 | A-P1: trộn đầu vào đã có | 4/4/4/5/4/4/3 | 82 | High | High |
| R03 (mới) | [Nguồn](https://www.inoreader.com/blog/2026/01/save-time-with-automations.html) | Save time with automations | Inoreader | 2026-01-27 | 2026-11-25 | A-P1/C-P1: rules, filters, duplicate filters | 5/4/4/5/5/4/2 | 87 | High | High |
| R04 (mới) | [Nguồn](https://www.inoreader.com/pricing) | Pricing | Inoreader | Không ghi ngày; giá quan sát 2026-11-25 | 2026-11-25 | A-P1/C-P1: giá chào bán và tính năng | 5/4/4/5/5/4/2 | 87 | High | High |
| R05 (mới) | [Nguồn](https://devpost.com/software/ghostpipes-yahoo-pipes-reborn-with-ai-intelligence) | GhostPipes — Yahoo Pipes Reborn with AI Intelligence | Anil Kumar / Devpost | 2025-12-05 (mốc project started) | 2026-11-25 | A-P1: tiền lệ Kiroween 2025; chưa chạy thử | 3/3/3/5/5/3/2 | 69 | Medium | High |
| R06 (mới) | [Nguồn](https://community.n8n.io/t/cannot-get-any-time-filters-to-work/295902) | Cannot get ANY time filters to work | Lilly / n8n Community | 2026-05-16; phản hồi đến 2026-05-18 | 2026-11-25 | A-P1: thử cấu hình và workaround; đã có lời giải | 2/4/4/5/5/4/4 | 77 | Medium | High |
| R07 (mới) | [Nguồn](https://community.n8n.io/t/problem-filtering-new-rss-items-with-code-node-and-google-sheets-input-multiple-inputs/141143) | Problem Filtering New RSS Items | Marios Tzanetakis / n8n Community | 2025-06-30; giải quyết 2025-07-02 | 2026-11-25 | A-P1/C-P1/A-P7: lọc lặp, công sức tạo MRE; solved bằng n8n | 2/4/4/5/5/4/4 | 77 | Medium | High |
| R08 (P1) | [Nguồn](https://github.com/DIYgod/RSSHub) | RSSHub | DIYgod và cộng tác viên | Không ghi ngày bài; snapshot 2026-11-25 | 2026-11-25 | A-P1: routes nguồn châu Á; AGPL, không chứng minh nơi cư trú người dùng | 4/4/4/4/5/5/4 | 84 | High | Medium |
| R09 (mới) | [Nguồn](https://urfist.univ-rennes2.fr/sites/default/files/2025-01/Stage%20Veille%20association%20Courroie.pdf) | Démarche et outils pour développer une veille numérique personnelle | URFIST Rennes / Rémi Joinville | Bìa ghi 2024-01-16; thư mục 2025-01: mâu thuẫn chưa giải | 2026-11-25 | A-P1/C-P1: người làm veille tại Pháp; không làm chứng nhu cầu mới 2025 | 4/3/4/4/2/4/5 | 73 | High | Medium |
| R10 (mới) | [Nguồn](https://feedly.com/new-features/posts/multilingual_ai_market_intelligence) | Unlock market intelligence insights in 15 languages | Feedly | 2025-07-16 | 2026-11-25 | C-P1: gom cùng sự kiện xuyên ngôn ngữ; A-P1 lọc ngữ nghĩa | 5/4/4/5/5/4/2 | 87 | High | High |
| R11 (mới) | [Nguồn](https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-vision-microsoft-365-copilot) | Get started with vision in Microsoft Copilot | Microsoft Support | Không ghi ngày; bản hiện tại 2026-11-25 | 2026-11-25 | A-P2: màn hình trực tiếp, highlight, điều kiện tài khoản | 5/4/4/5/5/4/3 | 88 | High | High |
| R12 (mới) | [Nguồn](https://blog.google/products-and-platforms/products/gemini/gemini-app-updates-io-2025/) | Gemini gets more personal, proactive and powerful | Google / Josh Woodward | 2025-05-20 | 2026-11-25 | A-P2: screen sharing miễn phí được công bố; không benchmark hiệu quả | 5/3/3/4/5/4/2 | 76 | High | Medium |
| R13 (mới) | [Nguồn](https://www.itpro.com/business/digital-transformation/how-schneider-electric-is-streamlining-onboarding-with-walkme) | How Schneider Electric is streamlining onboarding with WalkMe | ITPro / Rory Bathgate; phỏng vấn người vận hành | 2026-04-02 | 2026-11-25 | A-P2: triển khai/budget ở NA, tổ chức Pháp, CoE tại Ấn Độ/Philippines | 4/4/4/5/5/3/4 | 83 | High | High |
| R14 (mới) | [Nguồn](https://www.chi1995.chistatic.hosting.acm.org/proceedings/shortppr/kjk_bdy.htm) | Apple Guide: A Case Study in User-Aided Design of Online Help | Apple / Kevin Knabe; ACM CHI | 1995 (CHI) | 2026-11-25 | A-P2: vòng chỉ dẫn, bỏ qua bước đã xong, chỉ vật thể thật | 5/4/5/5/5/3/4 | 91 | High | High |
| R15 (mới) | [Nguồn](https://wallabag.org/migrate-from-pocket/) | Migrate from Pocket to wallabag | wallabag | Không ghi ngày; trang đã nói Pocket export đóng | 2026-11-25 | A-P4: nhập file cũ, self-host hoặc managed hosting | 5/4/4/5/5/4/3 | 88 | High | High |
| R16 (mới) | [Nguồn](https://wallabag.it/en/faq/) | Frequently asked questions | wallabag.it | Không ghi ngày; snapshot 2026-11-25 | 2026-11-25 | A-P4: lưu full text, export, hosted từ 11 EUR/năm | 5/4/4/5/5/4/2 | 87 | High | High |
| R17 (mới) | [Nguồn](https://labo.hatenastaff.com/entry/2025/05/30/094517) | Pocketのデータをはてなブックマークに移行するツールをはてラボで提供します | Hatena / kỹ sư kouki_dan | 2025-05-30 | 2026-11-25 | A-P4: người dùng Nhật tự viết và dùng công cụ migration | 4/4/4/5/5/4/3 | 84 | High | High |
| R18 (mới) | [Nguồn](https://opcug.ca/qa_recordings/20250730_PowerPoint.pdf) | Q&A: Goodbye Pocket — Hello Instapaper | Ottawa PC Users’ Group | 2025-07-30 | 2026-11-25 | A-P4: hoạt động hướng dẫn di dời ở Canada; không đếm người migration | 4/4/4/5/5/4/5 | 86 | High | High |
| R19 (mới) | [Nguồn](https://obsidian.md/help/web-clipper) | Introduction to Obsidian Web Clipper | Obsidian | Không ghi ngày; redirect hợp lệ từ help.obsidian.md | 2026-11-25 | A-P4: lưu local, templates, reader; phản chứng không cần Docker | 5/4/4/5/5/4/2 | 87 | High | High |
| R20 (mới) | [Nguồn](https://github.com/gildas-lormeau/SingleFile) | SingleFile | Gildas Lormeau và cộng tác viên | Không ghi ngày bài; snapshot 2026-11-25 | 2026-11-25 | A-P4: bản HTML độc lập, extension; AGPL hiện tại | 4/4/5/5/5/5/4 | 91 | High | High |
| R21 (mới) | [Nguồn](https://support.mozilla.org/en-US/kb/future-of-pocket) | Pocket has shut down — What you need to know | Mozilla Support | Không ghi ngày cập nhật; bảng mốc đến 2025-11-12 | 2026-11-25 | A-P4: đóng 8/7; export/API tắt 12/11/2025; dữ liệu queued deletion | 5/4/4/5/5/5/4 | 91 | High | High |
| R22 (mới) | [Nguồn](https://survey.stackoverflow.co/2026/ai/data/ai-trust) | Trust in AI tools — data 2026 | Stack Overflow Developer Survey | 2026; khảo sát công bố 2026-10-06 | 2026-11-25 | A-P7: 6872/14304 tin khi dễ kiểm chứng; ODbL | 5/5/4/5/5/5/3 | 94 | High | High |
| R23 (mới) | [Nguồn](https://survey.stackoverflow.co/2026/knowledge) | Knowledge 2026 | Stack Overflow Developer Survey | 2026; công bố 2026-10-06 | 2026-11-25 | A-P7: attribution, ngữ cảnh, nguồn kiến thức; không đo muốn đóng góp | 5/5/4/4/5/5/3 | 91 | High | High |
| R24 (mới) | [Nguồn](https://stackoverflow.co/company/press/archive/stack-overflow-annual-developer-survey-ai-trust-conditional) | 2026 Developer Survey: trust remains conditional | Stack Overflow | 2026-10-06 | 2026-11-25 | A-P7: 169 nước, các nước dẫn đầu, cộng đồng vẫn hoạt động | 5/3/4/4/5/4/2 | 80 | High | Medium |
| R25 (mới) | [Nguồn](https://stackoverflow.blog/2026/09/16/here-s-what-s-new-on-stack-overflow-for-agents) | What’s new on Stack Overflow for Agents | Stack Overflow / Phoebe Sajor, David Gibson | 2026-09-16 | 2026-11-25 | A-P7: TIL, Playbooks, verification, approval/privacy; hiệu quả còn tự đánh giá | 5/4/4/5/5/4/2 | 87 | High | High |
| R26 (mới) | [Nguồn](https://docs.github.com/en/discussions/collaborating-with-your-community-using-discussions/participating-in-a-discussion) | Participating in a discussion | GitHub Docs | Không ghi ngày | 2026-11-25 | A-P7: câu trả lời cộng đồng được đánh dấu; thay thế hiện hữu | 5/4/4/5/4/5/3 | 88 | High | High |
| R27 (mới) | [Nguồn](https://docs.github.com/en/code-security/concepts/secret-security/push-protection) | Push protection | GitHub Docs | Không ghi ngày | 2026-11-25 | A-P7: scan secret là một phần, không bảo đảm xóa hết thông tin riêng | 5/4/4/4/5/5/3 | 87 | High | Medium |
| R28 (P1) | [Nguồn](https://www.belkin.com/support-article/?articleNum=335419) | Wemo Support Ending — What You Need to Know | Belkin | Cập nhật 2026-01 | 2026-11-25 | B-P1: cloud/app tắt 31/1/2026; ngoại lệ HomeKit/Thread | 5/4/5/5/5/5/3 | 94 | High | High |
| R29 (mới) | [Nguồn](https://www.home-assistant.io/integrations/wemo/) | Belkin WeMo integration | Home Assistant | Không ghi ngày; bản docs 2026.11.3 | 2026-11-25 | B-P1: local push/poll, các loại thiết bị; chưa chạy hardware | 5/4/5/5/5/5/4 | 95 | High | High |
| R30 (mới) | [Nguồn](https://community.home-assistant.io/t/with-the-end-of-belkin-wemo-support-i-need-help-with-pywemo/980634) | With the end of Belkin Wemo Support I need help with Pywemo | Joe / Home Assistant Community | 2026-01-29; cập nhật 2026-02-01 | 2026-11-25 | B-P1: cố gắng tái cấu hình; sau đó báo đã chạy được | 2/4/4/5/5/4/4 | 77 | Medium | High |
| R31 (mới) | [Nguồn](https://support.google.com/googlehome/answer/16233096?hl=en) | End of support for Nest Learning Thermostats (1st & 2nd gen) | Google Home and Nest Help | Không ghi ngày; mốc hiệu lực 2025-10-25 | 2026-11-25 | B-P1: cả bản EU bị mất kết nối app; điều khiển cục bộ còn | 5/4/5/5/5/4/3 | 92 | High | High |
| R32 (P1) | [Nguồn](https://cs.stanford.edu/~jhumphri/documents/you-bought-it-they-bricked-it.pdf) | You Bought It, They Bricked It: A Call for Reclaiming Local Control | Jack Tigar Humphries / ACM HotNets | 2026-11-16–17 | 2026-11-25 | B-P1 AI và giới hạn; B-P4 chỉ giả thuyết chuyển giao | 5/5/4/5/5/3/3 | 90 | High | High |
| R33 (mới) | [Nguồn](https://github.com/codykociemba/NoLongerEvil-Thermostat) | NoLongerEvil-Thermostat | Cody Kociemba / Hack House | Không ghi ngày bài; snapshot 2026-11-25 | 2026-11-25 | B-P1: installer, cloud/self-host; bounty là tự báo cáo ở README | 4/4/4/5/5/5/3 | 86 | High | High |
| R34 (mới) | [Nguồn](https://community.agilent.com/cfs-file/__key/telligent-evolution-components-attachments/01-39-00-00-00-00-05-59/Windows-10-End-of-Life-1.pdf) | Windows 10 End of Life — Impact on OpenLab Support | Agilent / Linda Johnson | 2025-10-02 | 2026-11-25 | B-P4: OS security hết; OpenLab lifecycle vẫn tiếp tục | 5/4/5/5/5/5/3 | 94 | High | High |
| R35 (mới) | [Nguồn](https://cit.ucsb.edu/policies) | Policies — Desktop Operating System Support Guidelines | UC Santa Barbara / College IT | Không ghi ngày; bảng có mốc Windows 10 tháng 12/2025 | 2026-11-25 | B-P4: cho máy điều khiển không nâng được ở sau firewall | 5/4/5/5/4/5/5 | 94 | High | High |
| R36 (mới) | [Nguồn](https://www.metrohm.com/ja_jp/service/quality-service/repair-service/tiamo_service_end.html) | ソフトウェアtiamoのWindows対応について | Metrohm Japan | Không ghi ngày; điều khoản từ 2025-01, hỗ trợ 3.0 đến 2029 | 2026-11-25 | B-P4: phần mềm không lên Win11; một số model không qua OMNIS | 5/4/5/5/4/5/3 | 92 | High | High |
| R37 (mới) | [Nguồn](https://pymeasure.readthedocs.io/en/latest/introduction.html) | Introduction — PyMeasure | PyMeasure | Không ghi ngày; build docs 2026-11-20 | 2026-11-25 | B-P4: VISA/SCPI/GPIB/serial và driver sẵn có; không phải tự suy mọi giao thức | 4/4/5/5/5/5/4 | 91 | High | High |
| R38 (mới) | [Nguồn](https://contact.perkinelmer.com/upgrade-to-windows11) | Upgrade Your Laboratory to Windows 11 | PerkinElmer | Không ghi ngày; trang nêu Windows 10 đã hết hỗ trợ | 2026-11-25 | B-P4: dịch vụ theo quote, engineer, IQ/OQ là đối chứng thương mại | 5/3/4/5/5/4/2 | 83 | High | High |
| R39 (mới) | [Nguồn](https://knowledge.illumina.com/instrumentation/general/instrumentation-general-faq-list/000002247) | Windows 10 Upgrade for Illumina Instruments FAQ | Illumina | Không ghi ngày | 2026-11-25 | B-P4: upgrade theo hợp đồng; retail Windows10 EOL không áp mọi máy | 5/4/5/5/4/5/3 | 92 | High | High |
| R40 (P1) | [Nguồn](https://www.gov.uk/government/publications/telecare-and-the-digital-switchover-guidance-for-housing-providers/telecare-and-the-digital-switchover-guidance-for-housing-providers) | Telecare and the digital switchover: guidance for housing providers | UK DHSC | 2026-10-08 | 2026-11-25 | C-P4: PSTN nghỉ 31/1/2027; mẫu nghiên cứu, trách nhiệm và OGL | 5/4/5/5/5/5/5 | 96 | High | High |
| R41 (P1) | [Nguồn](https://www.ofcom.org.uk/phones-and-broadband/vulnerable-customers/ofcom-fines-virgin-media-23.8-million-for-putting-vulnerable-customers-at-risk-of-harm) | Ofcom fines Virgin Media £23.8 million | Ofcom | 2025-12-01 | 2026-11-25 | C-P4: phạt, vi phạm 2022–23, biện pháp sửa và 42991 lượt liên hệ | 5/5/5/5/5/5/5 | 100 | High | High |
| R42 (mới) | [Nguồn](https://modgov.hillingdon.gov.uk/documents/g5055/Printed%20minutes%2018th-Sep-2025%2019.00%20CABINET.pdf?T=1) | Cabinet Minutes & Decisions — Telecare transition | London Borough of Hillingdon | Họp 2025-09-18; công bố 2025-09-19 | 2026-11-25 | C-P4: phê duyệt hợp đồng 2026 235364 GBP; không phải hóa đơn đã trả | 5/5/5/5/5/5/5 | 100 | High | High |
| R43 (mới) | [Nguồn](https://www.openreach.com/news/openreach-to-protect-broadband--connections-as-pstn-closure---approaches/) | Openreach to protect broadband connections as PSTN closure approaches | Openreach | 2026-09-24 | 2026-11-25 | C-P4: Prove Telecare; tự báo cáo hơn 70000 khách hàng | 5/4/4/5/5/3/2 | 85 | High | High |
| R44 (mới) | [Nguồn](https://telecare.digitaloffice.scot/news/march-2026-housing-blog-preparing-for-the-january-2027-deadline-318) | March 2026 Housing Blog: Preparing for the January 2027 Deadline | Scottish Local Government Digital Office | 2026-03-24 | 2026-11-25 | C-P4: triển khai Prove Telecare, booking và data sharing; độc lập nguồn vendor | 5/4/5/5/5/4/5 | 94 | High | High |
| R45 (mới) | [Nguồn](https://www.fdma.go.jp/mission/prevention/landline.html) | NTT固定電話のIP網移行に伴って火災通報装置に発生する事象への対応について | Japan Fire and Disaster Management Agency | Thông báo gốc 2019-12-23; trang không ghi cập nhật | 2026-11-25 | C-P4: analogue Nhật là fire alarm, không đồng nhất telecare Anh | 5/4/5/4/3/5/5 | 89 | High | Medium |
| R46 (mới) | [Nguồn](https://journal.ntt.co.jp/article/36705) | PSTNからのネットワーク移行・固定電話発信切替 | NTT Technical Journal | 2025-10 | 2026-11-25 | C-P4: Nhật chuyển core IP; khác kiến trúc dây thuê bao ở Anh | 5/4/5/4/5/4/3 | 89 | High | Medium |
| R47 (P1) | [Nguồn](https://aclanthology.org/2025.naacl-industry.73.pdf) | Improved Near-Duplicate Detection for Aggregated and Paywalled News-Feeds | TCS Research / NAACL Industry | 2025-04-30 | 2026-11-25 | C-P1: cơ chế embeddings/metadata; không kiểm chứng semantic delta | 5/5/4/5/5/3/4 | 91 | High | High |
| R48 (P1) | [Nguồn](https://developers.feedly.com/docs/how-does-deduplication-work) | How does Deduplication work | Feedly developer docs | Không ghi ngày tuyệt đối; updated 15 days ago | 2026-11-25 | C-P1: ngưỡng >85%, 31 ngày, ngoại lệ; phạm vi riêng feature | 5/4/5/5/5/4/2 | 91 | High | High |
| R49 (P1) | [Nguồn](https://kiroween.devpost.com/rules) | Kiroween 2026 Official Rules | AWS / Devpost | Cập nhật 2026-11-16 | 2026-11-25 | Chung: Resurrection, deadline, dự án mới; không chọn thắng giải | 5/5/5/5/5/5/5 | 100 | High | High |
| R50 (mới) | [Nguồn](https://learn.microsoft.com/en-us/lifecycle/products/windows-xp) | Windows XP — Microsoft Lifecycle | Microsoft | Không ghi ngày bài; xác nhận đã hết hỗ trợ | 2026-11-25 | B-P4: mỏ neo OS cụ thể đã nghỉ; không suy mọi driver đã chết | 5/4/5/5/5/5/4 | 95 | High | High |
| R51 (mới) | [Nguồn](https://library.concordia.ca/help/using/rss/index.php) | How to use RSS | Concordia University Library | Cập nhật 2025-10-06 | 2026-11-25 | A-P1/C-P1: nhà nghiên cứu Canada; RSS alerts, không đo khó khăn | 5/3/4/4/4/4/5 | 81 | High | Medium |
| R52 (mới) | [Nguồn](https://www.macrumors.com/2025/07/10/belkin-ending-wemo-support/) | Belkin Ending Support for Most Wemo Devices | MacRumors / Juli Clover | 2025-07-10 | 2026-11-25 | B-P1: xác nhận độc lập lịch Wemo và ngoại lệ | 4/3/4/5/5/4/4 | 81 | High | High |
| R53 (mới) | [Nguồn](https://www.vice.com/en/article/mozilla-pocket-shutting-down-soon/) | Pocket export deadline extension | VICE / Matt Jancer | 2025-11-09 | 2026-11-25 | A-P4: đối chiếu 12/11 | 3/2/3/5/5/3/4 | 67 | Medium | High |
| R54 (mới) | [Nguồn](https://github.com/pymeasure/pymeasure) | PyMeasure repository | PyMeasure contributors | Không ghi ngày bài; snapshot 2026-11-25 | 2026-11-25 | B-P4: MIT, cộng đồng hiện hữu; không đo nhu cầu trả phí | 4/4/4/5/5/5/4 | 87 | High | High |
| R55 (mới) | [Nguồn](https://devpost.com/software/watcher-5kfz4r) | Watcher | Benson Mugure / Devpost | 2025-12-05 (project started) | 2026-11-25 | A-P1/C-P1: tiền lệ Reader + LLM selectors + state diff; chưa thử chạy | 3/3/4/5/5/3/2 | 73 | Medium | High |

