# Phase 1.5: tài liệu quyết định sau Quality Gate

Run `2026-11-25-phase1-discovery`, ngày 25/11/2026. Người đọc: chủ dự án. Người viết: Coordinator.

Tài liệu này thay bản `phase-1-decision-brief.md` làm đầu vào cho quyết định Phase 2. Bản Phase 1 vẫn được giữ.

- Chi tiết kiểm tra nằm trong `../quality-gate/`.
- Dữ liệu gốc của agent không bị sửa.

**Tài liệu không xếp hạng và không loại ứng viên.** Shortlist bên dưới là **phán đoán của anh/chị**, chưa phải kết luận đã kiểm chứng. Thứ tự liệt kê là theo agent rồi theo mã.

---

## 1. Các quyết định cần anh/chị đưa ra trước Phase 2

| #   | Quyết định                                         | Lựa chọn                                                                                            | Ghi chú                                                                                                             |
| --- | -------------------------------------------------- | --------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| E1  | Phạm vi Phase 2                                    | Tám space shortlist / một tập con / thêm lại space ngoài shortlist                                  | Coordinator không đề xuất tập con                                                                                   |
| E2  | Xử lý chỗ trùng                                    | O1 (A-P1, C-P1) và O2 (B-P1, B-P4): nghiên cứu chung hay riêng                                      | Xem mục 3                                                                                                           |
| E3  | Cách hiểu theme Resurrection cho workflow/tập quán | Vẫn mở từ Phase 1 (D3)                                                                              | Trong shortlist, câu hỏi này ảnh hưởng chủ yếu C-P1 và C-P4. C tự ghi C-P4 là "PSTN đang rút, chưa chết hoàn toàn". |
| E4  | Chấp nhận hiệu chuẩn một người chấm                | Chấp nhận / thêm một người chấm khác model / anh/chị tự chấm một phần anchor                        | Coordinator cùng model với Agent B (mục 4)                                                                          |
| E5  | Thực thi an toàn cho worker ở Phase 2              | Siết cài đặt quyền của Orca trước / tiếp tục chỉ Coordinator / chấp nhận rủi ro sau khi được nêu rõ | Hiện cả ba worker chạy không sandbox                                                                                |
| E6  | Cập nhật `progress/` theo `AGENTS.md`              | Ghi Phase 1 và 1.5 thành chu kỳ 27, sổ 41/31/10/0/0 không đổi / chờ                                 | Coordinator chưa sửa                                                                                                |

Thời gian: còn khoảng 9 ngày đến hạn nộp 04/12/2026 14:00 PT.

---

## 2. Quality Gate đã làm gì

Option (a): **Coordinator làm một mình, không khởi chạy worker.** Lý do: trước khi dùng worker, Coordinator kiểm và xác nhận Orca đặt `agentPermissionDefault = "full-access"`, và lệnh khởi chạy worker không có cờ sandbox nào.

| Việc                  | Kết quả tóm tắt                                                                           | Tệp                        |
| --------------------- | ----------------------------------------------------------------------------------------- | -------------------------- |
| Kiểm claim quyết định | 23 mục được kiểm: 18 khớp, 3 khớp một phần, 2 chưa kiểm được                              | `claim-verification.md`    |
| Giải mâu thuẫn        | 5 mâu thuẫn được giải; không còn mâu thuẫn dữ kiện nào chưa giải trong shortlist          | `claim-verification.md` §2 |
| Hiệu chuẩn điểm       | A +8, B −5, C ≈ 0 so với Coordinator, trên 22 anchor                                      | `calibration.md`           |
| Sửa nhãn và metadata  | 3 claim tách nhãn, 1 claim thu hẹp phạm vi, 1 sửa trình bày; metadata của B và C được sửa | `corrections-overlay.md`   |
| Chỗ trùng             | 2 chỗ trùng trong shortlist, 2 chỗ trùng với space ngoài shortlist                        | `overlaps.md`              |

---

## 3. Tám space sau Quality Gate

Mỗi mục ghi:

- trạng thái bằng chứng sau kiểm tra;
- hiệu chỉnh nhãn (nếu có);
- phản chứng do agent nêu (giữ nguyên);
- điều còn chưa biết;
- phép thử bác bỏ nhỏ nhất do agent đề xuất.

Câu chữ đầy đủ nằm trong báo cáo gốc.

### A-P1 · Yahoo! Pipes → lọc và tổng hợp nguồn web do người dùng tự lắp ráp

- **Đã kiểm:** Pipes đóng 30/09/2015 (`A-P1-C1`, khớp). Reuters 2026: mạng xã hội/video lần đầu là kênh tin trực tuyến phổ biến nhất, 54% so với 51%. Pew 2026: 52% người Mỹ "worn out by the news".
- **Hiệu chỉnh:** `A-P1-C2` tách nhãn. Hai số liệu là VERIFIED. "Quá tải thông tin gia tăng ở nhóm người theo dõi chuyên môn" là INFERENCE.
- **Phản chứng (A):** n8n, Huginn, RSSHub, Feedly đã trưởng thành. Mệt mỏi tin tức không chứng minh người dùng muốn tự cấu hình đường ống.
- **Chưa biết:** nhu cầu tự lắp ráp (`A-P1-C4`, HYPOTHESIS); giá và giới hạn AI của Feedly.
- **Phép thử (A):** 5 người dựng một luồng trong 15 phút, so với Feedly/Google Alerts.
- **Trùng:** O1 với C-P1.

### A-P2 · Apple Guide → hướng dẫn thao tác bám trạng thái UI thật

- **Đã kiểm:** SAP ký thỏa thuận mua WalkMe ngày 05/06/2024.
- **Hiệu chỉnh:** `A-P2-C2` tách nhãn. Thương vụ và TipKit là VERIFIED. "Giá trị kinh tế rất lớn" là INFERENCE. Thương vụ thuộc phân khúc doanh nghiệp, còn khoảng trống A nêu là người dùng cuối (`A-P2-C3`, INFERENCE).
- **Phản chứng (A):** Copilot Vision và Gemini Live đang phổ cập. Đọc DOM gặp giới hạn trên ứng dụng canvas/WebGL.
- **Chưa kiểm:** năng lực thực tế của Copilot Vision/Gemini Live cuối 2026. Đây là phản chứng quyết định của space này.
- **Phép thử (A):** 5 người làm cùng một tác vụ trên giao diện vừa đổi, so AI chia sẻ màn hình với coachmark.

### A-P4 · Del.icio.us và Pocket → kho bookmark/đọc sau chống link rot

- **Đã kiểm:**
  - Pocket đóng 08/07/2025; dữ liệu bị xóa vĩnh viễn sau 08/10/2025.
  - Pew 2024: 38% trang năm 2013 không còn truy cập được; 54% trang Wikipedia có link tham chiếu chết.
  - Raindrop xóa bản lưu khoảng một tháng sau khi hết Pro.
- **Hiệu chỉnh:** không. Lưu ý: Pew đo trang web chung, không đo kho bookmark cá nhân.
- **Phản chứng (A):** cả Del.icio.us và Pocket đều thất bại thương mại. Karakeep và ArchiveBox miễn phí và mạnh cho người dùng kỹ thuật.
- **Chưa biết:** người dùng có cần mở lại link cũ không (`A-P4-C4`, HYPOTHESIS).
- **Phép thử (A):** đo tỷ lệ link hỏng mà 5 người thật sự cần mở lại trong 30 ngày.
- **Trùng:** O3, cùng cơ chế phát hiện link rot "mềm" với A-P6 và B-P6 (ngoài shortlist).

### A-P7 · Stack Overflow → lưu lời giải lỗi biên đã được người kiểm chứng (xem lại)

- **Đã kiểm:** Coordinator tự gọi Stack Exchange API và nhận đúng 843 câu hỏi (10/2026), 940 (09/2026), 123.257 (03/2022). Claim `A-P7-C1` tái lập được.
- **Mâu thuẫn đã giải:** khảo sát 2026 có 30.903 người trả lời. n=16.985 là số người trả lời câu hỏi về việc dùng Stack Overflow. Hai con số không mâu thuẫn.
- **Phản chứng (A, giữ nguyên):** chính sự sụt giảm cũng là bằng chứng coding agent đã đáp ứng phần lớn nhu cầu. Log sửa lỗi ở nơi làm việc vướng NDA.
- **Chưa biết:** động lực đóng góp khi không còn hệ reputation (`A-P7-C4`, UNKNOWN).
- **Phép thử (A):** 10 lỗi biên thật trên thư viện phát hành năm 2026; đếm số lỗi coding agent thất bại lặp lại.

### B-P1 · Thiết bị bị brick khi nhà sản xuất tắt cloud/app

- **Đã kiểm:**
  - Car Thing bị vô hiệu hóa, hạn hoàn tiền 14/01/2025.
  - AirPort Utility bị bỏ với iOS 27.
  - Nest cũ ngừng app control ngày 25/10/2025.
  - Bài HotNets '26 báo cáo Codex với GPT-5.5, khoảng 870 vòng replay, 650 test, 6 model, 4 firmware.
- **Hiệu chỉnh:** không. `B-P1-C5` giữ phạm vi "bài báo báo cáo" và chưa tái lập độc lập.
- **Phản chứng (B):** chính bài báo ghi chưa chứng minh tổng quát hóa và đã tiêu tốn "billions of model tokens". "Bốn đến năm ngày công" là ước lượng hồi cứu của tác giả. Matter có thể làm vấn đề thu hẹp dần.
- **Chưa biết:** số người và thiết bị bị ảnh hưởng (`B-P1-C8`); phạm vi DMCA 1201(f).
- **Phép thử (B):** chọn một thiết bị rẻ, ghi một workflow, đo thời gian đến khi replay tương đương.
- **Trùng:** O2 với B-P4. Cả hai phụ thuộc một nguồn cơ chế duy nhất (`B·R01`).

### B-P4 · Thiết bị khoa học khóa vào PC/OS hết hỗ trợ

- **Đã kiểm:** Khoa Hóa UW–Madison (2024) ghi rằng driver và phần mềm điều khiển "often do not work on later OS versions" và họ thay thiết bị "as funding allows".
- **Hiệu chỉnh:**
  - `B-P4-C1` tách nhãn. Việc lab giữ PC OS EOL là ĐÃ XÁC MINH (2021 + 2024). Chi phí 10.000 USD và chi tiết XP/eBay chỉ từ một nguồn năm 2021, nên là SUY LUẬN cho hiện tại.
  - `B-P4-C2` thu hẹp phạm vi: phát biểu của một khoa.
- **Phản chứng (B):** nhiều lab chọn cô lập mạng và coi là đủ. Không có khảo sát định lượng. Thư viện mở PyMeasure/QCoDeS chưa được kiểm.
- **Chưa biết:** quy mô 2025–2026 (`B-P4-C5`); cơ chế AI chuyển giao từ B-P1 (`B-P4-C4`, GIẢ THUYẾT).
- **Trùng:** O2 với B-P1.

### C-P1 · Google Reader → theo dõi nguồn đã chọn không đọc lặp

- **Đã kiểm:**
  - Reader đóng 01/07/2013 với lý do Google công bố.
  - Feedly dedup ẩn bài trùng trên 85% trong cửa sổ 31 ngày, không áp dụng trong cùng nguồn hay app sync bên thứ ba.
- **Hiệu chỉnh:** không.
- **Phản chứng (C):** reader hiện đại vẫn hoạt động, AI dedup đã là sản phẩm. Khoảng trống "so sánh phần thay đổi" (`C-P1-C5`) là SUY LUẬN, chưa benchmark.
- **Theme fit:** C tự ghi rằng RSS chưa chết; việc hồi sinh riêng Google Reader cần được cân nhắc theo E3.
- **Phép thử (C):** 3 người, 30–50 bài, so Feedly/Inoreader với cách họ đang làm.
- **Trùng:** O1 với A-P1.

### C-P4 · Telecare khi rút PSTN tại Anh

- **Đã kiểm:**
  - Ngày tắt PSTN là 31/01/2027 (DHSC, 08/10/2026).
  - Ofcom phạt Virgin Media £23,8 triệu ngày 01/12/2025.
  - DHSC: khoảng ba phần tư báo động grouped living và một phần ba báo động cá nhân vẫn analog.
  - Openreach pilot migrate 1.000 khách hàng.
- **Hiệu chỉnh:** không. `C-P4-C3` có nhãn SUY LUẬN thận trọng hơn mức nguồn cho phép; Coordinator không nâng nhãn.
- **Phản chứng (C):** chuyển sang digital có lý do chính đáng; dịch vụ kỹ sư và hướng dẫn hiện có đã mạnh. **C tự ghi AI không bắt buộc** (`C-P4-C7`).
- **Ràng buộc (C):** không gọi thử báo động thật; chưa có đối tác hay quyền dữ liệu.
- **Chưa kiểm:** `C-P4-C4` (phụ thuộc nguồn điện), vì nguồn trả 403.
- **Phép thử (C):** một housing provider xem 10 hồ sơ ẩn danh và đối chiếu với checklist hiện có.

---

## 4. Độ tin cậy của chính Quality Gate

- **Một người chấm.** Hiệu chuẩn dùng Coordinator làm tham chiếu. Coordinator chạy cùng model với Agent B, nên offset −5 của B có thể bị đánh giá thấp.
- **Ít cặp trùng nguồn.** Chỉ một cặp claim–source trùng thật giữa hai agent (Pew link rot: A chấm 98, B chấm 88, Coordinator chấm 95).
- **Phạm vi kiểm.** Chỉ claim quyết định của shortlist được kiểm. Ba claim quyết định chưa kiểm được và được liệt kê ở `claim-verification.md` §3.
- **Không có bằng chứng người dùng trực tiếp ở cả 8 space.** Quality Gate kiểm nguồn, không kiểm nhu cầu.

## 5. Dữ liệu tham chiếu

| Loại | Đường dẫn |
|---|---|
| Báo cáo gốc (không sửa) | `../agent-{a,b,c}/discovery.md` |
| Kết quả Quality Gate | `../quality-gate/` |
| Báo cáo hoàn tất Phase 1 | `../coordinator/phase-1-completion-report.md` |
| Shortlist nguyên văn | `../quality-gate/human-shortlist.md` |
