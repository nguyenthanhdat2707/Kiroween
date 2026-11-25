# Kiểm tra claim quyết định

Mọi nguồn trong tệp này được Coordinator mở trực tiếp ngày 25/11/2026 (UTC+7), trừ các dòng ghi khác.

Kết quả dùng các mức:

- **Khớp**: nguồn nói đúng điều claim nói;
- **Khớp một phần**: một phần claim vượt quá nguồn;
- **Chưa kiểm**: không mở được nguồn hoặc không thuộc phạm vi.

## 1. Kết quả theo claim

### A-P1 · Yahoo! Pipes

| Claim | Nhãn của A | Nguồn đã mở | Kết quả |
|---|---|---|---|
| A-P1-C1: Pipes đóng 30/09/2015, ngừng tạo pipe từ 30/08/2015 | VERIFIED | A·R02 (PCMag, 04/06/2015): "use Yahoo Pipes until its Sept. 30 closure date, you won't be able to create any new pipes past Aug. 30" | **Khớp** |
| A-P1-C2: quá tải thông tin và lệ thuộc thuật toán là hiện tượng toàn cầu, gia tăng 2025–2026 | VERIFIED | A·R05 (Reuters DNR 2026): mạng xã hội/video lần đầu là cách tiếp cận tin trực tuyến phổ biến nhất, 54% so với 51% (48 thị trường). A·R06 (Pew, 11/02/2026): 52% người trưởng thành Mỹ "worn out by the news" | **Khớp một phần.** Hai số liệu khớp. "Quá tải thông tin" và "gia tăng" là diễn giải. Pew đo mệt mỏi tin tức ở Mỹ, Reuters đo kênh tiếp cận, không nguồn nào đo trực tiếp nhóm người theo dõi chuyên môn. |

### A-P2 · Apple Guide

| Claim | Nhãn của A | Nguồn đã mở | Kết quả |
|---|---|---|---|
| A-P2-C2: in-app guidance có giá trị kinh tế lớn, thể hiện qua thương vụ SAP–WalkMe 05/06/2024 và TipKit | VERIFIED | A·R12 (SAP News, 05/06/2024): "definitive agreement under which SAP will acquire WalkMe" | **Khớp một phần.** Thương vụ khớp. "Giá trị kinh tế rất lớn" và "Apple phải giới thiệu TipKit" là diễn giải. Thương vụ thuộc phân khúc doanh nghiệp, trong khi khoảng trống A nêu (`A-P2-C3`) là người dùng cuối. |
| Phản chứng: Copilot Vision và Gemini Live phổ cập | (phản chứng của A) | — | **Chưa kiểm.** Đây là đối thủ quyết định của A-P2. |

### A-P4 · Del.icio.us và Pocket

| Claim | Nhãn của A | Nguồn đã mở | Kết quả |
|---|---|---|---|
| A-P4-C1: Pocket đóng 08/07/2025 | VERIFIED | A·R19 (Mozilla): "Pocket shuts down July 8, 2025 … export saves anytime until October 8, 2025, after which their data will be permanently deleted". A·R20 (Nieman Lab) xác nhận độc lập | **Khớp.** Phần Del.icio.us (A·R18, Pinboard) chưa được Coordinator mở. |
| A-P4-C2: 38% trang web năm 2013 không còn truy cập được; 23% trang tin và 21% trang chính phủ có link hỏng; 54% trang Wikipedia có link tham chiếu chết | VERIFIED | A·R21 (Pew, 17/05/2024): cả bốn số khớp nguyên văn | **Khớp.** Pew đo trang web chung, không đo kho bookmark cá nhân. |
| A-P4-C3: Raindrop xóa bản lưu khoảng một tháng sau khi hết Pro | INFERENCE | A·R22 (Raindrop help): "When the subscription expires, archived copies become inaccessible and are permanently deleted after about a month" | **Khớp** phần dữ kiện. Phần "người dùng mắc kẹt giữa hai cực" vẫn là SUY LUẬN, đúng nhãn A gắn. |

### A-P7 · Stack Overflow

| Claim | Nhãn của A | Nguồn đã mở | Kết quả |
|---|---|---|---|
| A-P7-C1: 843 câu hỏi (10/2026), 940 (09/2026), 123.257 (03/2022) | VERIFIED | Stack Exchange API v2.3, `filter=total`, Coordinator tự gọi lại: **843 / 940 / 123.257** | **Khớp chính xác.** Tái lập được. |
| A-P7-C2: Developer Survey 2026 ">30.000 người" và n=16.985 | VERIFIED / INFERENCE | A·R40 (survey.stackoverflow.co/2026) | **Mâu thuẫn đã giải**, xem mục 2.1 |

### B-P1 · Thiết bị bị brick

| Claim | Nhãn của B | Nguồn đã mở | Kết quả |
|---|---|---|---|
| B-P1-C1: Car Thing bị vô hiệu hóa 12/2024, hoàn tiền nếu liên hệ trước 14/01/2025 | ĐÃ XÁC MINH | B·R02 (MacRumors, 10/12/2024): "Contact customer service by no later than January 14, 2025 to discuss your refund options" | **Khớp** |
| B-P1-C2: Apple bỏ AirPort Utility với iOS 27 | ĐÃ XÁC MINH | B·R03 (MacRumors, 22/06/2026) | **Khớp** (kiểm ở Phase 1) |
| B-P1-C4: Google ngừng app control cho ba đời Nest cũ ngày 25/10/2025 | SUY LUẬN | B·R04 (9to5Google): "ended software support … for three of its oldest Nest Thermostats on October 25, 2025" | **Khớp.** Nhãn SUY LUẬN của B thận trọng hơn mức nguồn cho phép, nhưng đó là lựa chọn của B. |
| B-P1-C5: phương pháp HotNets '26 (Codex với GPT-5.5, ~870 vòng replay, 650 test, 6 model, 4 firmware) | ĐÃ XÁC MINH (bài báo báo cáo) | B·R01 PDF: "approximately 870 replay iterations, Codex produced roughly 50,000 lines … and 650 tests"; "six models and four firmware versions"; "Codex [46] with GPT-5.5 Medium" | **Khớp.** Phạm vi đúng: xác minh rằng bài báo báo cáo như vậy; kết quả chưa được tái lập độc lập. |
| B-P1-C6: chi phí giảm từ "hàng tháng" xuống "4–5 ngày công" | GIẢ THUYẾT | B·R01: "We retrospectively estimate … four to five days of human work"; "consumed billions of model tokens" | **Khớp** câu chữ. Đây là ước lượng hồi cứu của tác giả, nên nhãn GIẢ THUYẾT của B phù hợp. |

### B-P4 · Thiết bị khoa học khóa vào OS EOL

| Claim | Nhãn của B | Nguồn đã mở | Kết quả |
|---|---|---|---|
| B-P4-C1: lab giữ PC XP/3.x/DOS; nâng phần mềm sắc ký tốn 10.000 USD; mua linh kiện trên eBay | ĐÃ XÁC MINH | B·R13 (Nature, **2021**): "cost $10,000", "Windows XP", "eBay". B·R14 (UW–Madison, 2024) **không** nêu 10.000 USD, XP hay eBay | **Khớp một phần.** Hiện tượng lab giữ OS EOL được hai nguồn (2021, 2024) xác nhận. Con số 10.000 USD và các chi tiết XP/eBay chỉ có một nguồn năm 2021. Xem đề xuất sửa nhãn. |
| B-P4-C2: UW–Madison mô tả thiết bị EOL, driver không chạy trên OS mới, tách VLAN, dùng SMB2 | ĐÃ XÁC MINH | B·R14: "instrument control software, or the hardware drivers, often do not work on later OS versions. We replace instruments as funding allows"; nhắc SMB version 2 | **Khớp** cho phát biểu của **một khoa**. Không tổng quát hóa được. |

### C-P1 · Google Reader

| Claim | Nhãn của C | Nguồn đã mở | Kết quả |
|---|---|---|---|
| C-P1-C1: Reader đóng 01/07/2013 vì giảm sử dụng và tập trung ít sản phẩm hơn | ĐÃ XÁC MINH | C·R01 (blog Google Reader): "the actual date is July 1, 2013 … usage of Google Reader has declined, and … pouring all of our energy into fewer products" | **Khớp.** Lý do là lời công bố của Google, không kèm số liệu. |
| C-P1-C5: Feedly dedup có ngưỡng >85%, cửa sổ 31 ngày, không dedup trong cùng nguồn hay app sync bên thứ ba | SUY LUẬN | C·R04 (Feedly docs): "over 85% content overlap published within the same 31-day window … doesn't apply within a single source or in third-party sync apps" | **Khớp** phần dữ kiện. Khoảng trống "so sánh phần thay đổi" vẫn là SUY LUẬN. |

### C-P4 · Telecare khi rút PSTN

| Claim | Nhãn của C | Nguồn đã mở | Kết quả |
|---|---|---|---|
| C-P4-C1: chuyển đổi hướng tới 01/2027 | ĐÃ XÁC MINH | C·R27 và C·R24 trả 403 với Coordinator. Đối chiếu thay bằng C·R21 (DHSC, 08/10/2026): "phasing out … PSTN by January 2027", "switch-off date on 31 January 2027"; và C·R26 (Action Plan): "by the end of January 2027" | **Khớp** qua nguồn chính phủ thay thế |
| C-P4-C2: Ofcom phạt Virgin Media £23,8 triệu ngày 01/12/2025 | ĐÃ XÁC MINH | Trang Ofcom và nhiều báo độc lập (kiểm ở Phase 1) | **Khớp** |
| C-P4-C3: khoảng ba phần tư báo động grouped living và một phần ba báo động cá nhân vẫn analog | SUY LUẬN | C·R21: "Based on DHSC commissioned research with a sample of alarm receiving centres … around three-quarters of grouped living scheme telecare alarms are still analogue. For personal alarms, around one-third are analogue" | **Khớp nguyên văn.** Chỉ một nguồn chính thức (nghiên cứu mẫu do DHSC đặt). Nhãn SUY LUẬN của C thận trọng. Coordinator không nâng nhãn. |
| C-P4-C4: digital landline cần điện tại nhà | ĐÃ XÁC MINH | C·R24 và C·R27 trả 403 | **Chưa kiểm** |
| C-P4-C5: Openreach pilot migrate 1.000 khách hàng, ra mắt toàn quốc tháng 10/2025 | CHƯA RÕ (hiệu quả) | C·R25 (Openreach, 17/09/2025): "pilot successfully migrated 1,000 customers"; "launch … this October" | **Khớp** dữ kiện. Hiệu quả và độ bao phủ vẫn CHƯA RÕ, đúng nhãn C. Nguồn là thông cáo của chính nhà cung cấp. |

## 2. Mâu thuẫn đã giải quyết

### 2.1 A-P7-C2: ">30.000 người" so với n=16.985

- A·R40 ghi tổng "**30,903 Responses**, 169 Countries".
- Câu hỏi về việc dùng Stack Overflow thay đổi thế nào có "**n = 16,985**": 64,1% vào ít hơn cho câu hỏi đơn giản, 28,9% hỏi ít hơn, 26,5% đóng góp ít hơn, khoảng 16% dùng để kiểm chứng.
- **Kết luận:** hai con số đều đúng. Một là tổng người trả lời khảo sát, một là số người trả lời một câu hỏi. Không có mâu thuẫn dữ kiện, chỉ có trình bày thiếu ngữ cảnh trong báo cáo của A.

### 2.2 A-P7-C1 (940 câu hỏi tháng 9) và A·R39 (969)

- MACCUS (A·R39, 31/10/2026) báo 969 câu hỏi tháng 9. API ngày 25/11/2026 trả 940.
- **Kết luận (SUY LUẬN):** chênh lệch 29 câu khớp với việc câu hỏi bị xóa sau ngày MACCUS đếm, vì `filter=total` chỉ đếm câu chưa xóa. Không ảnh hưởng độ lớn: cả hai đều dưới 1.000.

### 2.3 B-P4-C1: số liệu 2021 dùng cho vấn đề 2026

- Con số 10.000 USD và chi tiết XP/eBay chỉ có trong Nature 2021. Nguồn 2024 (UW–Madison) xác nhận hiện tượng, không xác nhận con số.
- **Kết luận:** hiện tượng còn tồn tại đến 2024 là được hỗ trợ. Chi phí hiện tại là CHƯA RÕ.

### 2.4 C-P4-C1: "hướng tới tháng 1/2027"

- Hướng dẫn DHSC ngày 08/10/2026 ghi rõ ngày tắt là 31/01/2027. Không mâu thuẫn.

### 2.5 Cùng nguồn, khác điểm (Pew link rot)

- A·R21 được A chấm 98, B·R20 được B chấm 88. Xem `calibration.md`.

## 3. Claim quyết định chưa kiểm được

| Space | Điều chưa kiểm | Vì sao quan trọng |
|---|---|---|
| A-P2 | Mức sẵn có và năng lực của Copilot Vision / Gemini Live cuối 2026 | Là phản chứng chính của A-P2 |
| A-P1, C-P1 | Bảng giá và tính năng AI của Feedly | A nói AI bị khóa ở bản miễn phí; C không nêu giá |
| A-P4 | Del.icio.us chỉ còn đọc từ 15/06/2017 (A·R18) | Mỏ neo lịch sử |
| B-P1 | Wemo dừng cloud đầu 2026 (B-P1-C3, chỉ snippet) | Một ví dụ thứ ba về thiết bị bị brick |
| B-P4 | Vendor thúc nâng cấp quanh mốc Windows 10 EOL (B-P4-C3, chỉ snippet) | Động lực hiện tại của vấn đề |
| C-P4 | C-P4-C4 phụ thuộc nguồn điện (nguồn 403) | Một phần lý do quy trình cũ không còn đủ |
| Tất cả 8 | Nhu cầu người dùng trực tiếp | Không space nào có phỏng vấn hay quan sát người dùng |
