# Phase 1: tài liệu quyết định

Run `2026-11-25-phase1-discovery`, ngày 25/11/2026. Người đọc: chủ dự án. Người viết: Coordinator.

Tài liệu này là bản trình bày cho người. Nó **không thay thế** và **không sửa** dữ liệu nghiên cứu gốc của agent:

- `../agent-a/discovery.md`, `../agent-b/discovery.md`, `../agent-c/discovery.md`: báo cáo gốc, giữ nguyên;
- `../coordinator/phase-1-completion-report.md`: kết quả kiểm tra của Coordinator;
- `../coordinator/execution-log.md`: tham số chạy.

Mọi mã claim (ví dụ `B-P1-C2`) và mã nguồn đều trỏ về báo cáo gốc. Mã nguồn được ghi kèm agent, ví dụ `A·R17` là R17 trong báo cáo của Agent A, vì số R của ba agent trùng nhau.

**Tài liệu không xếp hạng.** Các problem space được liệt kê theo thứ tự agent rồi theo mã. Thứ tự này không phản ánh chất lượng.

---

## 1. Các quyết định cần anh/chị đưa ra

Phase 2 chưa bắt đầu. Cần năm quyết định trước khi khởi động bất kỳ phase nào tiếp theo.

| #   | Quyết định                                                                 | Lựa chọn                                                                                                                                          | Hệ quả nếu chọn                                                                                                                                      |
| --- | -------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| D1  | Chấp nhận Phase 1 hay yêu cầu sửa trước                                    | (a) Chấp nhận như hiện tại · (b) Gửi lại ba agent các lỗi cụ thể ở mục 3.3                                                                        | (b) tốn thêm một lượt chạy ngắn. Nhãn claim và metadata sẽ đúng trước khi Cross Review dùng chúng.                                                   |
| D2  | Hiệu chuẩn lại điểm reference                                              | (a) Có, trước Cross Review · (b) Không, chỉ dùng điểm trong nội bộ từng agent                                                                     | Điểm giữa agent hiện không so được (mục 3.2). Nếu chọn (b), Cross Review không được dùng điểm để so nguồn giữa agent.                                |
| D3  | Cách hiểu chủ đề Resurrection cho workflow, tập quán, hệ chữ (giả định A2) | (a) Chỉ chấp nhận khi neo vào một công nghệ/nền tảng cụ thể đã chết hoặc suy tàn · (b) Chấp nhận cả workflow/tập quán · (c) Để Phase 2 kiểm chứng | Ba agent không thống nhất (mục 4). Luật chỉ ghi "dead technology" và "obsolete tech". Quyết định này ảnh hưởng trực tiếp đến B-P3, B-P6, C-P1, C-P4. |
| D4  | Phạm vi Phase 2                                                            | (a) Deep Research trên toàn bộ 17 space · (b) Cross Review giữa ba agent trước · (c) Chọn một tập con để đào sâu                                  | Chọn tập con là quyết định của anh/chị, không phải của Coordinator. Tài liệu này không đề xuất tập con.                                              |
| D5  | Cập nhật `progress/` theo `AGENTS.md`                                      | (a) Ghi chu kỳ 27 = Phase 1, không đổi sổ 41/31/10/0/0 · (b) Chờ đến sau Cross Review                                                             | `AGENTS.md` yêu cầu cập nhật sau mỗi chu kỳ. Phase 1 cấm gộp nên Coordinator chưa sửa.                                                               |

Câu hỏi thời gian thuộc về anh/chị: còn khoảng 9 ngày đến hạn nộp 04/12/2026 14:00 PT. Theo rules, sản phẩm phải chạy được, có video dưới 3 phút và repo có `/.kiro`.

---

## 2. Phase 1 đã tạo ra gì

Ba agent làm độc lập, cùng một brief, không đọc kết quả của nhau. Coordinator không phát hiện vi phạm cách ly, nhưng điều này chỉ là kiểm tra trên transcript, không phải bảo đảm.

| Agent | Model thực tế                    | Problem space                 | Claim | Reference được chấm |
| ----- | -------------------------------- | ----------------------------- | ----- | ------------------- |
| A     | `gemini-4-neon-high`             | 7 (6 mới, 1 xem lại)          | 28    | 45                  |
| B     | `claude-sonnet-5-5`, effort high | 6 (5 mới, 1 xem lại một phần) | 38    | 22                  |
| C     | `gpt-6.1-sol`, effort high       | 4 (4 mới)                     | 32    | 27                  |

Tổng cộng có 17 problem space. **Không có space nào đã được nâng lên PROMISING.** Phase 1 không có nhiệm vụ đó. Sổ cũ vẫn giữ 41/31/10/0/0.

---

## 3. Độ tin cậy của bằng chứng

### 3.1 Điều chung cho cả 17 space

- **Không agent nào có phỏng vấn hay quan sát người dùng.** Mọi nhận định "vấn đề vẫn tồn tại" dựa trên tài liệu công khai, khảo sát của bên thứ ba hoặc dữ liệu API. Mỗi space có một phép thử bác bỏ nhỏ nhất (mục 5), nhưng chưa phép thử nào được chạy.
- **Không phát hiện nguồn bịa.** 117/118 URL tồn tại. URL còn lại (knowledgebase.vcu.edu, Agent C) không phản hồi sau hai lần thử.
- Có khoảng 23 lượt truy cập nguồn thất bại được các agent tự ghi: A 10, B 10, C 3.

### 3.2 Điểm reference không so được giữa agent

Median điểm weighted là A 94, C 86, B 77. Cùng thang 0–100, nhưng ba agent chấm với độ khắt khe khác nhau. Một nguồn được A chấm 90 không chắc tốt hơn một nguồn được B chấm 75. Điểm trong nội bộ một agent vẫn dùng được.

### 3.3 Lỗi cụ thể đã phát hiện

| Agent | Lỗi                                                                                                                                                                                                                                                                                          | Mức độ                    |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------- |
| A     | `A-P7-C2` dẫn Developer Survey 2026 là ">30.000 người", đồng thời dẫn n=16.985 từ chu kỳ 18. A không giải thích chênh lệch.                                                                                                                                                                  | Mâu thuẫn chưa giải       |
| A     | Giới hạn của Discord Server Web Pages trong `A-P3` (chỉ máy chủ ≥1.000 thành viên, không xuất bản lịch sử trước 12/2026) dựa trên `A·R17`. Trang hỗ trợ của Discord bị chặn 403, nên A đối chiếu qua nguồn thứ cấp `serverfront.app` (log lỗi #4 của A).                                     | Phụ thuộc nguồn thứ cấp   |
| A     | `A-P7-C1`: Stack Overflow còn 843 câu hỏi tháng 10/2026. Coordinator **chưa tự kiểm lại** vì Stack Exchange API chặn rate-limit. Con số nhất quán về độ lớn với nguồn thứ hai `A·R39` (969 câu hỏi tháng 9).                                                                                 | Chưa kiểm độc lập         |
| B     | 8 claim gắn ĐÃ XÁC MINH chỉ có một reference. Một số chấp nhận được vì là văn bản luật hoặc dữ liệu tái lập được (`B-P2-C4`, `B-P6-C2`). Một số dựa thêm vào snippet (`B-P3-C1`, `B-P5-C1`, `B-P6-C3`) hoặc không có xác nhận độc lập (`B-P4-C2`, `B-P6-C1`). B ghi minh bạch loại chứng cứ. | Nhãn cao hơn mức chứng cứ |
| B, C  | Metadata tự khai sai. B ghi effort "thấp–trung bình"; C ghi model/effort "CHƯA RÕ". Tham số thực đã được Coordinator ghi ở mục 2.                                                                                                                                                            | Không ảnh hưởng nội dung  |

### 3.4 Claim đã được Coordinator kiểm mẫu và khớp nguồn

- `A-P5-C1`: InfoPath 2013 và InfoPath Forms Services hết hỗ trợ 14/07/2026. Phần "xóa khỏi SharePoint SE bằng bản cập nhật 13/07/2027" chưa được kiểm.
- `B-P1-C2`: Apple bỏ AirPort Utility khỏi App Store với iOS 27 (MacRumors, 22/06/2026).
- `B·R01`: bài HotNets '26 "You Bought It, They Bricked It" tồn tại và mô tả AI hỗ trợ reverse engineering giao thức AirPort.
- `C-P4-C2`: Ofcom phạt Virgin Media £23,8 triệu ngày 01/12/2025 vì migration telecare.

---

## 4. Ba agent bất đồng ở đâu

Brief yêu cầu thử năm giả định cũ thay vì kế thừa. Kết luận của ba agent được giữ nguyên nhãn và mức chắc chắn của từng agent.

| Giả định | Agent A | Agent B | Agent C |
|---|---|---|---|
| **A1** Người dùng phải là cá nhân/gia đình Mỹ–Âu | Bác bỏ: rules chỉ đòi "real audience" | Bác bỏ như ràng buộc bắt buộc. Bằng chứng nhu cầu mạnh nhất của B đến từ lab, hàng hải Baltic, dòng họ Việt Nam | SUY LUẬN: ràng buộc này thu hẹp discovery quá sớm |
| **A2** Resurrection phải là công nghệ lỗi thời | Điều chỉnh: giá trị nằm ở workflow, nhưng mỗi space vẫn cần neo vào một công nghệ cụ thể đã chết để qua Stage One | Bác bỏ một phần. Rủi ro theme fit của tập quán/hệ chữ là **CHƯA RÕ**. B đề nghị Coordinator quyết định cách diễn giải | **CHƯA RÕ** với workflow thuần túy. Không tự sửa lời rule thành "mọi workflow" |
| **A3** Có đối thủ là bị loại | Bác bỏ: đối thủ là dấu hiệu có nhu cầu | Bác bỏ: câu hỏi đúng là khoảng trống cụ thể nào chưa được phủ | SUY LUẬN: có đối thủ không đủ để loại, **cũng không đủ để giữ** |
| **A4** Vấn đề hướng developer là kém phù hợp | Bác bỏ một phần: Stack Overflow giảm 99,59%. Cảnh báo kèm theo: phải vượt được coding agent | Bác bỏ, nhưng chỉ cho dạng "người kỹ thuật có tài sản bị khóa" (B-P1, B-P4) | **CHƯA RÕ**: run này không kiểm định trực tiếp |
| **A5** "0 PROMISING" nghĩa là đã cạn ý tưởng | Bác bỏ: do bộ lọc giao hội quá chặt | Không đồng ý; SUY LUẬN là do bộ lọc. B chưa áp lại rubric cũ lên space mới | SUY LUẬN: chưa thể kết luận đã cạn, nhưng đây **không** phải bằng chứng có ứng viên mạnh |

Điểm đồng thuận: cả ba không coi A1 là ràng buộc bắt buộc, và không coi A5 là kết luận đã chứng minh.

Điểm bất đồng thật: A2 và A4. Mức chắc chắn cũng khác nhau. A dùng nhãn "bác bỏ" dứt khoát. C giữ CHƯA RÕ hoặc SUY LUẬN cho cùng giả định.

---

## 5. Mười bảy problem space

Mỗi mục gồm năm phần: vấn đề; thay thế mạnh nhất do agent tìm được; phản chứng mạnh nhất; vai trò AI theo nhận định của agent; phép thử nhỏ nhất có thể bác bỏ. Câu chữ là tóm lược của Coordinator. Câu chữ và nhãn đầy đủ nằm ở mục 5–7 và 9 của báo cáo gốc.

### Agent A

**A-P1 · Yahoo! Pipes → lọc và tổng hợp nguồn web do người dùng tự lắp ráp**
- Vấn đề: người theo dõi nguồn chuyên biệt bị quá tải. Nhiều nguồn không có RSS.
- Thay thế: n8n, Huginn, RSSHub/RSS-Bridge, Feedly Leo (`A·R07`, `A·R08`).
- Phản chứng: các công cụ trên đã trưởng thành. Mệt mỏi tin tức (`A·R06`, Pew 2026) không chứng minh người mệt mỏi muốn tự cấu hình đường ống dữ liệu.
- AI: A cho rằng AI chịu tải ở bộ trích xuất tự sửa khi trang nguồn đổi cấu trúc, và ở bộ lọc ngữ nghĩa. Chat hỏi tin tức là trang trí.
- Phép thử: 5 nhà nghiên cứu/nhà báo dựng một luồng trong 15 phút. Nếu họ quay về kiểm tra thủ công hoặc thấy Feedly/Google Alerts đủ, nhu cầu bị bác bỏ.

**A-P2 · Apple Guide → hướng dẫn thao tác bám trạng thái giao diện thật**
- Vấn đề: phần mềm phức tạp đổi giao diện thường xuyên. Hướng dẫn tĩnh nhanh lỗi thời.
- Thay thế: WalkMe/SAP (`A·R12`), Apple TipKit (`A·R13`), Scribe/Tango, Copilot Vision/Gemini Live.
- Phản chứng: AI chia sẻ màn hình đang phổ cập. Đọc DOM/Accessibility Tree gặp giới hạn cứng trên canvas WebGL.
- AI: A cho rằng AI chịu tải khi biên dịch tài liệu hoặc mục tiêu thành chuỗi bước gắn vào phần tử UI sống.
- Phép thử: 5 người làm cùng tác vụ trên giao diện vừa đổi, so Copilot Vision với lớp coachmark. Không cải thiện rõ thì bác bỏ.

**A-P3 · Usenet/diễn đàn mở → tri thức cộng đồng chat có thể lập chỉ mục và mang đi được**
- Vấn đề: tri thức hỗ trợ của cộng đồng nhỏ bị khóa trong Discord/Slack. Google Groups dừng Usenet từ 22/02/2024 (`A-P3-C1`).
- Thay thế: Discord Server Web Pages (`A·R17`, xem lưu ý nguồn ở mục 3.3), Answer Overflow đang thu hẹp, Discourse/GitHub Discussions/Zulip.
- Phản chứng: Discord tự làm phần lõi cho máy chủ lớn. Nhiều thành viên chủ động **không muốn** lời mình lên Google.
- AI: A cho rằng AI chịu tải ở việc tách các luồng hội thoại đan xen thành cặp vấn đề → lời giải.
- Phép thử: hỏi 5 quản trị viên máy chủ 100–900 thành viên xem họ có muốn xuất bản lịch sử công khai không.

**A-P4 · Del.icio.us và Pocket → kho bookmark/đọc sau chống link rot, không phụ thuộc SaaS**
- Vấn đề: Pocket đóng 08/07/2025 (`A·R19`). Raindrop.io xóa bản lưu khoảng một tháng sau khi hết Pro (`A·R22`).
- Thay thế: Raindrop.io, Karakeep (`A·R23`), ArchiveBox (`A·R24`).
- Phản chứng: cả Del.icio.us (bán 35.000 USD năm 2017, `A·R18`) và Pocket thất bại thương mại. Theo A, đây là bằng chứng đa số người dùng không sẵn lòng trả tiền.
- AI: A cho rằng AI chịu tải khi phát hiện trang vẫn trả HTTP 200 nhưng đã thành trang đỗ hoặc spam.
- Phép thử: đo tỷ lệ link hỏng mà 5 người **thật sự cần mở lại** trong 30 ngày.

**A-P5 · InfoPath → cứu biểu mẫu và dữ liệu XML cũ sau hạn khai tử**
- Vấn đề: InfoPath hết hỗ trợ 14/07/2026 (`A-P5-C1`, Coordinator đã kiểm). Tổ chức còn kho `.xsn`/`.xml`.
- Thay thế: Power Apps (không chuyển `.xsn` tự động, Premium 20 USD/người/tháng, `A·R29`), Microsoft Forms, Plumsail/Nintex.
- Phản chứng: thông báo khai tử có từ hơn mười năm trước, nhiều nơi đã di dời xong. Tệp thật chứa dữ liệu nhạy cảm, khó lấy trong 9 ngày. Khách hàng B2B chấp nhận chậm.
- AI: A cho rằng AI chịu tải khi giải thích các quy tắc XPath lồng nhau không có tài liệu.
- Phép thử: hỏi 5 quản trị viên SharePoint còn bao nhiêu biểu mẫu tồn đọng và có được phép chạy công cụ bên thứ ba không.

**A-P6 · DMOZ và Webrings → danh mục web có người kiểm định**
- Vấn đề: affiliate SEO spam và nội dung AI hàng loạt làm khó tìm nguồn phi thương mại.
- Thay thế: Curlie (`A·R30`), Kagi (`A·R36`), Marginalia (`A·R37`), GitHub Awesome Lists.
- Phản chứng: Ahrefs 07/2025 (`A·R35`) cho thấy bức tranh "AI chiếm trọn tìm kiếm" không đơn giản. Mọi danh mục cộng đồng đều gặp khởi động lạnh và vấn đề giữ chân biên tập viên.
- AI: A cho rằng AI chịu tải ở kiểm toán định kỳ: trang đổi chủ, nhồi link tiếp thị.
- Phép thử: so 20 truy vấn giữa tìm kiếm thường, Kagi/Marginalia và một danh mục nhỏ. Đo xem người dùng có quay lại không.

**A-P7 · Stack Overflow → lưu lời giải lỗi biên đã được người kiểm chứng (xem lại)**
- Vấn đề: lượng câu hỏi mới giảm mạnh (`A-P7-C1`, chưa kiểm độc lập, mục 3.3). Lời giải lỗi biên nằm rải rác trong lịch sử chat riêng.
- Thay thế: coding agent trong IDE, Stack Overflow AI Assist/Stack Internal, GitHub Issues/Discussions.
- Phản chứng do chính A nêu: sự sụt giảm cũng là bằng chứng coding agent đã giải đủ phần lớn nhu cầu. Log sửa lỗi ở nơi làm việc vướng NDA.
- Phép thử: ghi 10 lỗi biên thật của 5 lập trình viên trên thư viện phát hành năm 2026. Đếm số lỗi mà coding agent thất bại lặp lại.

### Agent B

**B-P1 · Thiết bị còn tốt bị "brick" khi nhà sản xuất tắt cloud/app**
- Vấn đề: Car Thing bị vô hiệu hóa 12/2024 (`B-P1-C1`). AirPort Utility bị bỏ với iOS 27 (`B-P1-C2`, Coordinator đã kiểm).
- Thay thế: Home Assistant và integration cộng đồng, firmware thay thế, thiết bị Matter/HomeKit.
- Phản chứng: bài HotNets '26 (`B·R01`) tự ghi là chưa chứng minh tổng quát hóa và tốn "hàng tỷ token". Bài mang tính vận động chính sách. Matter có thể làm vấn đề thu hẹp dần (SUY LUẬN).
- AI: B ghi SUY LUẬN là AI chịu tải ở việc suy giao thức từ trace UI và PCAP, rồi so hành vi với app gốc dùng làm oracle.
- Phép thử: chọn một thiết bị rẻ, ghi một workflow, đo thời gian đến khi replay tương đương.

**B-P2 · Game online đã mua nhưng không chơi được khi publisher tắt server**
- Vấn đề: ví dụ The Crew. Emulator cộng đồng cần trace chụp **trước** ngày tắt.
- Thay thế: The Crew Unlimited (`B·R07`), kiện tụng/chính sách (ECI, AB 1921), bản offline do publisher phát hành.
- Phản chứng: Ủy ban EU từ chối nghĩa vụ bắt buộc (`B·R06`). Rủi ro DMCA tại Mỹ là thật (`B-P2-C4`). Trạng thái AB 1921 chưa rõ, các nguồn thứ cấp mâu thuẫn.
- AI: B ghi GIẢ THUYẾT. Cùng cơ chế với B-P1 nhưng không còn oracle sau ngày tắt, nên khó hơn.

**B-P3 · Gia phả Hán Nôm mà con cháu không đọc được**
- Vấn đề: chữ Hán Nôm là hệ chữ lỗi thời. Gia phả cần tục biên.
- Thay thế: Kim Hán Nôm của HCMUS đã nhắm đúng người dùng chụp gia phả (`B·R09`, `B·R10`); dịch giả thuê ngoài.
- Phản chứng do chính B nêu: lý do "chưa có công cụ" **không đứng vững**. Khoảng trống còn lại (trích cấu trúc phả hệ, hiệu đính chữ viết tay) chưa được xác nhận. Con số "90% chưa dịch" là trích lại, không có phương pháp.
- Theme fit: phụ thuộc quyết định D3.
- Phép thử: hỏi 5 người giữ gia phả họ đã làm gì với bản Hán Nôm, đã thuê dịch chưa, giá bao nhiêu.

**B-P4 · Thiết bị khoa học còn tốt nhưng bị khóa vào PC/OS hết hỗ trợ**
- Vấn đề: nâng cấp có thể tốn khoảng 10.000 USD hoặc buộc thay thiết bị (`B·R13`).
- Thay thế: nâng cấp từ vendor, cô lập mạng (`B·R14`), giữ PC cũ, máy ảo (chưa kiểm).
- Phản chứng: nhiều lab chọn cô lập mạng và coi như "đủ tốt". Không có khảo sát định lượng. Thư viện mở PyMeasure/QCoDeS chưa được kiểm.
- AI: B ghi GIẢ THUYẾT là AI chịu tải ở việc suy giao thức. Khác với B-P1, phần mềm gốc vẫn chạy nên có oracle.

**B-P5 · Định vị không phụ thuộc vệ tinh khi GNSS bị gây nhiễu**
- Vấn đề: gây nhiễu/giả mạo GNSS ở Baltic. LORAN-C/Decca đã bị tháo bỏ.
- Thay thế: radar, la bàn, hải đồ ENC, R-Mode đang thử nghiệm, eLoran.
- Phản chứng: giải pháp thật là hạ tầng do nhà nước làm. Có rủi ro an toàn nếu sản phẩm khiến người dùng tin vào ước lượng sai.
- AI: **B ghi SUY LUẬN là AI chủ yếu trang trí.** Phát hiện spoof là bài toán lọc cổ điển.

**B-P6 · Webring/blogroll → khám phá web do người tuyển chọn (xem lại một phần)**
- Vấn đề: AI summary giảm click (`B-P6-C1`, Pew). Link rot (`B-P6-C2`).
- Thay thế: Kagi Small Web (`B·R21`), Marginalia, các webring hiện có, RSS reader, Wayback Machine.
- Phản chứng do chính B nêu: hồi sinh webring **đã diễn ra**, nên tính mới thấp. Không có bằng chứng người đọc phổ thông muốn dùng.
- AI: B ghi GIẢ THUYẾT là AI chịu tải một phần, ở việc phân loại trang đỗ hoặc đổi chủ để ringmaster duyệt.

### Agent C

**C-P1 · Google Reader → theo dõi nguồn đã chọn mà không đọc lặp cùng sự kiện**
- Thay thế: Feedly AI dedup, Inoreader monitoring (`C-P1-C4`).
- Phản chứng: reader hiện đại vẫn hoạt động, và AI dedup đã là sản phẩm. Khoảng trống có thể có là so sánh phần **thay đổi** giữa các bản tin, khác với xóa bài trùng (`C-P1-C5`, SUY LUẬN, chưa benchmark).
- AI: C ghi AI chỉ chịu tải nếu nhận diện phần mới tốt hơn rule/hash và tốt hơn đối thủ (`C-P1-C7`).
- Phép thử: 3 người, 30–50 bài, so Feedly/Inoreader với cách họ đang làm (`C-P1-C8`).

**C-P2 · Flash/SWF → tái sử dụng tư liệu tương tác khi runtime mất hỗ trợ**
- Thay thế: Ruffle, Flashpoint, nội dung chuyển sang HTML5 (`C-P2-C4`, ĐÃ XÁC MINH). C coi đây là baseline.
- Phản chứng: emulator và archive đã giải phần đáng kể. Phần trăm API được hỗ trợ không phải phần trăm tác phẩm chạy đúng (`C-P2-C5`).
- AI: C ghi GIẢ THUYẾT là AI giúp chỉ mục hành vi ("tìm ở đâu, bấm gì"), có chuyên gia kiểm tra. AI không phục hồi được byte hay asset đã mất (`C-P2-C6`, `C-P2-C7`).

**C-P3 · Jamboard → dùng lại hoạt động dạy học khi chỉ còn bản PDF tĩnh**
- Thay thế: Miro import Jamboard (`C-P3-C4`; còn chạy năm 2026 hay không: CHƯA RÕ), Jotboard, Miro Stickies capture.
- Phản chứng do chính C nêu: Miro Stickies capture đã chuyển ảnh thành sticky chỉnh sửa được (`C-P3-C7`). Đây là phần lõi trùng đáng kể với ý tưởng.
- Phép thử: 3 giáo viên làm lại một hoạt động trên 5 board, đo số phút chỉnh tay (`C-P3-C8`).

**C-P4 · Telecare khi rút đường dây analog tại Anh**
- Vấn đề: Ofcom phạt Virgin Media £23,8 triệu vì migration telecare (`C-P4-C2`, Coordinator đã kiểm). Digital landline cần nguồn điện tại nhà (`C-P4-C4`).
- Thay thế: Openreach Prove Telecare (`C-P4-C5`, CHƯA RÕ về độ bao phủ), Telecare National Action Plan.
- Phản chứng: chuyển sang digital có lý do chính đáng. Dịch vụ kỹ sư và hướng dẫn hiện có đã mạnh.
- AI: **C ghi SUY LUẬN là AI không bắt buộc** (`C-P4-C7`). Quy trình và test thực tế mới là phần chịu tải.
- Ràng buộc do C nêu: không gọi thử alarm thật. PSTN đang rút, chưa chết hoàn toàn.

---

## 6. Chỗ trùng giữa các agent (quan sát, chưa gộp)

- **Danh mục web do người tuyển chọn:** A-P6 và B-P6 đến độc lập. Cả hai đều dẫn Kagi và Marginalia.
- **Tổng hợp và đọc feed:** A-P1 và C-P1. Góc khác nhau: A nhấn vào tự lắp ráp đường ống, C nhấn vào giảm đọc lặp.
- **Suy giao thức từ trace bằng AI:** B-P1, B-P2, B-P4 cùng dựa vào cơ chế của `B·R01`. Nếu cơ chế đó không tái lập được, cả ba bị ảnh hưởng cùng lúc.

Việc gộp hay tách các cặp này thuộc Cross Review/Synthesis và cần phê duyệt (D4).

---

## 7. Câu hỏi mở xuyên suốt

1. **Theme fit cho workflow và tập quán** (D3). Cả ba agent đều nêu câu hỏi này, và không agent nào tự giải.
2. **Quyền dữ liệu.** Lịch sử chat cộng đồng (A-P3), tệp InfoPath của tổ chức (A-P5), gia phả (B-P3), hồ sơ telecare (C-P4), SWF (C-P2): chưa space nào có bộ dữ liệu được phép dùng.
3. **Mức độ dùng Kiro** (tiêu chí Technological Implementation 20%). A nêu câu hỏi này và tự gác lại cho phase sau (`A §9.6`). Chưa agent nào đánh giá.
4. **Nhu cầu ở Việt Nam.** C ghi rõ các trường hợp Anh/Úc/Bồ Đào Nha không phải bằng chứng thị trường Việt Nam. B-P3 là space duy nhất nhắm người dùng Việt Nam.
