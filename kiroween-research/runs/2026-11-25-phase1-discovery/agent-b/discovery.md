# Discovery Report — Agent B

## Metadata

- **Run:** `2026-11-25-phase1-discovery`, Agent B (Orca task `task_ed5f22a1aa57`).
- **Model id:** `claude-sonnet-5-5` (Claude Code CLI).
- **Effort:** mức suy luận do phiên cấu hình (thấp–trung bình); brief không quy định effort.
- **Thời gian:** bắt đầu khoảng 07:55 UTC (ước lượng, không ghi lại chính xác), kết thúc khoảng 08:12 UTC, ngày 2026-11-25.
- **Công cụ đã dùng:** WebSearch (khoảng 20 truy vấn); `curl` + trích văn bản bằng Python (khoảng 30 lần tải trang); `pdftotext` cho 2 PDF (HotNets'26, Nature 2021). Không chạy mã cộng đồng, không cài gói, không dùng subagent hay skill BMAD. Có đọc và áp dụng phương pháp của hai skill dự án `historical-technology-discovery` và `user-problem-validation`.
- **Ngày truy cập mọi nguồn:** 2026-11-25.
- **Lỗi/thất bại (10):**
  1. `familysearch.org/vi/giapha/` bị chặn bởi Incapsula, không đọc được.
  2. Trang hỗ trợ Belkin Wemo (`articleNum=335419`) render bằng JS; chỉ tải được menu, không có nội dung.
  3. Bài 9to5Mac về Neato: chỉ trích được menu, không trích được thân bài.
  4. Bài TechSpot về No Longer Evil: không trích được thân bài; đã thay bằng 9to5Google.
  5. API eCFR trả về 404; đã thay bằng bản sao 37 CFR 201.40 trên Cornell LII.
  6. Bài Unit 42 (Palo Alto) về thiết bị y tế chạy XP: lệnh tải lỗi (zsh glob), không thử lại.
  7. Trang SCIEX về Analyst end of support: tải được nhưng không có đoạn ngày/chính sách đọc được.
  8. Không tìm được thống kê GNSS cả năm 2025 của Traficom; con số 2024 chỉ có qua snippet.
  9. Chưa mở thông cáo gốc IP/26/1369 của European Commission; nội dung trả lời dựa trên trang ECI chính thức và phân tích của Lewis Silkin.
  10. Chưa kiểm tra trạng thái AB 1921 (California) trên leginfo chính thức; các nguồn thứ cấp mâu thuẫn nhau.

## 1. Research methodology

1. **Chống hội tụ sớm theo brief §4.** Tôi đọc `progress/current-state.md` và `ideas/all-candidates.md` chỉ để biết vùng đã khảo sát và lý do bác bỏ, rồi cố tình tìm ở ngoài các vùng đó. Tôi tìm ở **thiết bị/phần mềm bị nhà cung cấp "giết"** (chưa có trong sổ), **chữ viết và tập quán xã hội lỗi thời** (thử A2), **người dùng kỹ thuật/phòng thí nghiệm** (thử A4), **hạ tầng bị tháo bỏ nay cần lại** (LORAN) và **cấu trúc cộng đồng web** (webring).
2. **Quy trình cho mỗi problem space:** công nghệ/tập quán lịch sử → người dùng ban đầu → nguyên nhân suy giảm (tách nguyên nhân đã công bố và suy đoán) → thay thế hiện tại → giá trị mất → bằng chứng vấn đề còn tồn tại năm 2025–2026 → đối thủ mạnh nhất → bằng chứng ngược → vai trò thực của AI.
3. **Kiểm chứng claim:** `Claim → Primary → Independent → Mechanism`. Mỗi claim ghi bước đã đạt. **Claim chỉ dựa trên snippet kết quả tìm kiếm** (chưa mở được trang) thì không bao giờ được gắn ĐÃ XÁC MINH; nhãn cao nhất của nó là SUY LUẬN. Nguồn chỉ thấy qua snippet không được chấm điểm ở §10 mà được liệt kê riêng.
4. **Chấm nguồn:** dùng rubric 7 tiêu chí §5.2 và tính điểm trọng số bằng script. Source Reliability và Reference Relevance được ghi tách nhau.
5. **Giới hạn phương pháp:** thời gian ngắn (một phiên). Không phỏng vấn người dùng nào. Mọi nhận định về nhu cầu đều dựa trên tài liệu, không có quan sát trực tiếp. Môi trường tìm kiếm là WebSearch hướng Mỹ; nguồn tiếng Việt và Bắc Âu được tìm bổ sung bằng truy vấn riêng.

## 2. Discovered problem spaces

| ID | Problem space | Ai bị ảnh hưởng | Công nghệ/quy trình | Mới hay xem lại |
|---|---|---|---|---|
| B-P1 | Thiết bị phần cứng còn tốt bị "brick" hoặc mất quyền quản trị khi nhà sản xuất tắt cloud/app | Chủ thiết bị smart home, router, phụ kiện (Car Thing, Wemo, Nest đời đầu, AirPort) | Thiết bị phụ thuộc cloud; app quản lý độc quyền | **Mới.** Không có trong `all-candidates.md`. Cơ chế "khôi phục hành vi từ trace" gần với ý tưởng Behavioral Resurrection (chu kỳ 26), nhưng người dùng và đối tượng khác: chủ thiết bị thay vì quy tắc nghiệp vụ. |
| B-P2 | Game online mua rồi nhưng không chơi được khi publisher tắt server | Người chơi đã trả tiền; cộng đồng bảo tồn game | Game phụ thuộc server (ví dụ The Crew) | **Mới.** |
| B-P3 | Gia phả, sắc phong, văn tự gia đình viết bằng Hán Nôm mà con cháu không đọc được | Dòng họ/gia đình Việt Nam và kiều bào; người giữ gia phả | Chữ Hán Nôm (hệ chữ lỗi thời) và tập quán chép/tục gia phả | **Mới.** Sổ cũ có C30–C33 về mã TCVN3/VNI, khác hẳn. Thử A1 và A2. |
| B-P4 | Thiết bị khoa học còn tốt nhưng bị khóa vào PC/OS hết hỗ trợ | Phòng thí nghiệm đại học, nhóm nghiên cứu ít kinh phí, IT khoa | Phần mềm điều khiển và driver độc quyền trên Windows XP/7, DOS | **Mới.** Thử A4. Cơ chế liên quan B-P1. |
| B-P5 | Định vị không phụ thuộc vệ tinh khi GNSS bị gây nhiễu/giả mạo | Tàu thuyền, bao gồm thuyền giải trí, và hàng không ở Baltic/Vịnh Phần Lan | LORAN-C/Decca (đã tháo bỏ), kỹ năng dead reckoning và hải đồ giấy | **Mới.** Thử A1: người dùng ngoài khung gia đình Mỹ–Âu. |
| B-P6 | Khám phá web độc lập do con người tuyển chọn khi AI summary làm giảm click và link mục nát | Người viết blog cá nhân, người đọc muốn nguồn do người viết | Webring/blogroll/RSS directory như một **cấu trúc cộng đồng** | **Xem lại một phần.** Có liên quan tới C14 (GeoCities, bị loại vì Neocities) và chu kỳ 15 (AI lấn website). **Góc mới:** dùng webring như cơ chế tuyển chọn và duy trì liên kết, không phải hosting; có số liệu Pew 2024–2025 mới. |

5/6 problem space là mới. Như vậy vượt yêu cầu "ít nhất một nửa".

## 3. Historical context

### B-P1 — Thiết bị phụ thuộc cloud

- **Thời kỳ và chức năng ban đầu:** từ thập niên 2010, nhiều thiết bị tiêu dùng chuyển phần điều khiển sang app và cloud của nhà sản xuất. Đó là router AirPort (Apple ngừng bán từ 2018, quản lý chỉ qua AirPort Utility), hub Revolv, ổ cắm Wemo, Car Thing (ra mắt 4/2021).
- **Suy giảm/chấm dứt (đã công bố):** Spotify ngừng sản xuất Car Thing 5 tháng sau ra mắt "do nhu cầu thấp và chuỗi cung ứng", rồi tắt toàn bộ thiết bị tháng 12/2024 [R02]. Apple bỏ AirPort Utility khỏi App Store với iOS 27 và "không đảm bảo hoạt động" [R03]. Google ngừng app control cho ba đời Nest Thermostat cũ ngày 25/10/2025 [R04].
- **Nguyên nhân sâu (SUY LUẬN, có nguồn bàn luận):** duy trì cloud tốn chi phí liên tục, trong khi doanh thu chỉ đến một lần lúc bán. R01 nêu thêm động cơ "khiến chủ sở hữu mua thay thế"; đây là lập luận của tác giả, không phải dữ kiện.
- **Giá trị mất đi:** phần cứng còn chạy tốt nhưng chủ sở hữu mất quyền cấu hình. Thiết bị thành rác điện tử "không đồng thuận" (thuật ngữ của R01).

### B-P2 — Game online bị tắt server

- **Lịch sử:** game bán dưới dạng "license" nhưng cần server để chơi, kể cả phần chơi đơn. The Crew (Ubisoft) tắt server năm 2024. Sau đó Ubisoft thu hồi license trong thư viện người chơi [R07].
- **Phản ứng xã hội:** chiến dịch "Stop Killing Games" dẫn tới European Citizens' Initiative "Stop Destroying Videogames": hơn 1,29 triệu chữ ký hợp lệ, đạt ngưỡng ở 24 nước [R05]. Ngày 16/6/2026, Ủy ban châu Âu trả lời: không đề xuất nghĩa vụ pháp lý mới, chỉ khởi động đối thoại hướng tới code of conduct tự nguyện và báo cáo về Directive 2019/770 trước cuối 2026 [R06].
- **Nguyên nhân suy giảm (đã công bố):** Ubisoft nêu "ràng buộc hạ tầng server và license" (qua snippet các báo; R07 đã mở xác nhận việc thu hồi license).

### B-P3 — Hán Nôm và gia phả

- **Thời kỳ:** chữ Hán, và chữ Nôm cho tiếng Việt, là hệ chữ hành chính, học thuật và gia đình trong nhiều thế kỷ. Gia phả, sắc phong, khế ước, văn bia đều viết bằng hai loại chữ này.
- **Suy giảm (đã công bố):** khoa thi Hội/Đình cuối cùng diễn ra mùa hạ 1919. Vua Khải Định nói "đường khoa cử từ đây dứt hẳn" [R12], làm mất con đường đào tạo người đọc chữ Hán. Năm 1945, chữ Quốc ngữ được nâng lên địa vị quốc gia (chỉ thấy qua snippet một bài vjol; SUY LUẬN).
- **Hệ quả hiện tại:** theo HCMUS, Hội Bảo tồn di sản chữ Nôm ước tính hơn 90% tư liệu Hán Nôm chưa dịch sang Quốc ngữ, còn số người đọc được Hán Nôm tiếp tục giảm [R09]. Con số 90% này là trích dẫn lại.
- **Giá trị mất đi:** dòng họ vẫn giữ và thờ gia phả nhưng không đọc được. Tập quán **tục biên** (chép tiếp đời mới vào gia phả) bị đứt, vì người đời sau không viết được cùng hệ chữ (SUY LUẬN).

### B-P4 — Thiết bị phòng thí nghiệm khóa vào OS cũ

- **Lịch sử:** máy sắc ký, kính hiển vi confocal, SEM và máy phân tích được bán kèm PC điều khiển, phần mềm và driver độc quyền. Vòng đời thiết bị (10–30 năm) dài hơn vòng đời OS.
- **Suy giảm:** OS hết hỗ trợ (XP 2014, Windows 7 2020, Windows 10 ngày 14/10/2025 theo snippet vendor), trong khi driver và phần mềm không chạy trên OS mới [R14]. Ví dụ đã công bố: nâng phần mềm sắc ký để hỗ trợ OS mới tốn **$10.000**. Một phòng thí nghiệm mua laptop Toshiba 1987 trên eBay với giá $10–12 để lấy linh kiện [R13].
- **Giá trị mất đi:** phần cứng đo lường đắt tiền còn tốt nhưng phụ thuộc vào một PC không thể vá bảo mật.

### B-P5 — Định vị mặt đất (LORAN-C/Decca)

- **Lịch sử:** LORAN-C là hệ định vị vô tuyến mặt đất cho người dùng hàng hải, hàng không và đất liền. USCG chấm dứt phát tín hiệu từ khoảng 8/2/2010 và dự kiến mọi trạm ngừng trước 1/10/2010 [R15]. Các trạm châu Âu đóng ngày 31/12/2015 (Wikipedia/Maritime Executive, chỉ có snippet → SUY LUẬN). Châu Âu nêu nguyên nhân là chi phí, khi GNSS được coi là đủ.
- **Giá trị mất đi:** một lớp định vị độc lập với vệ tinh, khó gây nhiễu vì công suất phát mặt đất cao. Kỹ năng dead reckoning và hải đồ giấy cũng mai một (SUY LUẬN, chưa có số liệu).

### B-P6 — Webring/blogroll

- **Lịch sử:** EUROPa (1994, Imperial College), WebRing (1995). GeoCities mua lại năm 1998, Yahoo năm 1999. Yahoo ngừng hỗ trợ ngày 15/4/2001. Khi đó công cụ tìm kiếm đã đủ tốt nên webring bớt hữu ích [R22, Wikipedia dẫn Salon 2001].
- **Nguyên nhân suy giảm:** vừa do tổ chức (Yahoo đại tu, ringmaster mất quyền), vừa do công nghệ thay thế (search). Cả hai được ghi qua Wikipedia; chưa mở nguồn Salon gốc.
- **Giá trị mất đi:** khám phá do người tuyển chọn theo chủ đề, và trách nhiệm duy trì liên kết sống thuộc về một người cụ thể (ringmaster).

## 4. Evidence of contemporary relevance

Ký hiệu bước: **P** = có nguồn gốc, **I** = có xác nhận độc lập, **M** = đã kiểm tra cơ chế. "snippet" = chỉ thấy qua kết quả tìm kiếm.

### B-P1

| Claim | Nội dung | Bước đạt | Nhãn | Nguồn |
|---|---|---|---|---|
| B-P1-C1 | Car Thing ($90) bị vô hiệu hóa hoàn toàn tháng 12/2024; Spotify hướng dẫn tái chế, hoàn tiền nếu liên hệ trước 14/1/2025. | P+I | **ĐÃ XÁC MINH** | R02, R01 |
| B-P1-C2 | Apple bỏ AirPort Utility khỏi App Store với iOS 27 và không đảm bảo hoạt động trên macOS mới; AirPort ngừng bán từ 2018. | P (trích release notes) + I | **ĐÃ XÁC MINH** | R03, R01 |
| B-P1-C3 | Belkin kết thúc dịch vụ cloud/app Wemo (đầu 2026); thiết bị đã gắn HomeKit vẫn chạy cục bộ nhưng không cài lại được. | Một nguồn học thuật mở được (R01). Trang Belkin không đọc được; chi tiết HomeKit chỉ có qua snippet. | **SUY LUẬN** | R01; snippet BGR, Belkin |
| B-P1-C4 | Google ngừng app control cho ba đời Nest Thermostat cũ ngày 25/10/2025; dự án No Longer Evil flash bootloader/kernel để chuyển traffic tới server thay thế chứa bản sao API đã reverse-engineer. | P (bài báo trích dự án) + snippet TechSpot/Tom's Hardware | **SUY LUẬN** | R04 |
| B-P1-C5 | Một nghiên cứu HotNets'26 dùng AI (Codex/GPT-5.5) cùng trace UI, PCAP và phân tích binary chọn lọc để khôi phục hai phiên bản giao thức AirPort ACP đã mã hóa. Nhóm xây client tương thích, thử trên 6 model và 4 firmware, khoảng 870 vòng replay, 650 test. | P, M (phương pháp mô tả đủ chi tiết); I: không có | **ĐÃ XÁC MINH** (về việc bài báo báo cáo kết quả); bản thân kết quả **chưa được tái lập độc lập** | R01 |
| B-P1-C6 | AI giảm chi phí khôi phục từ "hàng tháng" xuống "4–5 ngày công" và phương pháp có thể tổng quát hóa sang thiết bị khác. | Chỉ có ước lượng hồi cứu của chính tác giả. Bài báo tự ghi chưa chứng minh tổng quát hóa và chưa tái dựng được cloud đã mất. | **GIẢ THUYẾT** | R01 |
| B-P1-C7 | Năm 2026 vẫn có người dùng AirPort, kể cả trong "production rigs" không nối Internet. | Bình luận người dùng trên R03 (giai thoại) | **SUY LUẬN** (tồn tại người dùng); quy mô **CHƯA RÕ** | R03 |
| B-P1-C8 | Số người/thiết bị bị ảnh hưởng mỗi năm. | Không tìm được số liệu đáng tin | **CHƯA RÕ** | — |

### B-P2

| Claim | Nội dung | Bước đạt | Nhãn | Nguồn |
|---|---|---|---|---|
| B-P2-C1 | ECI "Stop Destroying Videogames" có hơn 1,29 triệu chữ ký hợp lệ, đạt ngưỡng ở 24 nước thành viên (nộp ngày 26/1/2026, con số chính xác 1.294.188 theo snippet ECI/heise). | P (trang ECI chính thức) + I (R06) | **ĐÃ XÁC MINH** | R05, R06 |
| B-P2-C2 | Ngày 16/6/2026, Ủy ban châu Âu không đề xuất nghĩa vụ pháp lý giữ game chơi được. Ủy ban sẽ khởi động đối thoại hướng tới code of conduct tự nguyện và báo cáo Directive 2019/770 trước cuối 2026. | P (ECI xác nhận đã trả lời) + phân tích luật sư mở được; tiêu đề nhiều báo (PC Gamer, Dexerto) qua snippet; thông cáo gốc chưa mở | **ĐÃ XÁC MINH** (hướng quyết định); chi tiết câu chữ **SUY LUẬN** | R05, R06 |
| B-P2-C3 | Ubisoft thu hồi license The Crew sau khi tắt server; nhóm The Crew Unlimited làm *server emulator* (không crack) và đã chụp "Network Communications Data" **trước** khi server tắt. | P (phỏng vấn trong bài) | **SUY LUẬN** (một nguồn báo chí; chưa xác nhận độc lập trạng thái dự án năm 2026) | R07 |
| B-P2-C4 | Miễn trừ DMCA 37 CFR 201.40(b)(19)(i) chỉ cho phép sửa game để khôi phục chơi cá nhân khi server **xác thực** ngừng, và chỉ với "complete games" không cần nội dung lưu trên server. | P (văn bản luật, bản sao LII) | **ĐÃ XÁC MINH** (văn bản) | R08 |
| B-P2-C5 | Vì vậy, emulator tái tạo logic server cho game có nội dung server-side **không** nằm trong miễn trừ cá nhân này ở Mỹ. Rủi ro pháp lý là ràng buộc lớn với bất kỳ revival nào. | Suy từ C4; chưa có ý kiến luật sư | **SUY LUẬN** | R08 |
| B-P2-C6 | Luật California AB 1921 "Protect Our Games Act" sẽ áp nghĩa vụ báo trước và cung cấp bản offline hoặc hoàn tiền. | Mâu thuẫn: R06 viết "will impose", trong khi snippet BakerLaw (9/2026) nói vẫn nằm ở ủy ban Thượng viện; leginfo chưa kiểm tra | **CHƯA RÕ** | R06; snippet |

### B-P3

| Claim | Nội dung | Bước đạt | Nhãn | Nguồn |
|---|---|---|---|---|
| B-P3-C1 | Khoa thi Hội/Đình cuối cùng năm 1919 chấm dứt con đường khoa cử chữ Hán. | P (báo dẫn sách Nguyễn Thị Chân Quỳnh 2007) + snippet các bài vjol | **ĐÃ XÁC MINH** (mốc lịch sử; các nguồn thống nhất) | R12 |
| B-P3-C2 | Hơn 90% tư liệu Hán Nôm chưa dịch; số người đọc được tiếp tục giảm. | HCMUS trích Hội Bảo tồn di sản chữ Nôm; chưa có xác nhận độc lập hay phương pháp đếm | **SUY LUẬN** (xu hướng); con số 90% **CHƯA RÕ** | R09 |
| B-P3-C3 | Kim Hán Nôm (HCMUS) đã có web/Android/iOS, nhận dạng ảnh, phiên âm hai chiều Hán Nôm ↔ Quốc ngữ, API. Hệ thống nhắm **cả công chúng chụp gia phả/văn tự gia đình**. | P (tuyên bố của nhà phát triển) + I (site công cụ đang hoạt động khi truy cập) | **ĐÃ XÁC MINH** (công cụ tồn tại, có phạm vi công bố) | R09, R10 |
| B-P3-C4 | Độ chính xác OCR trên 95% với bản in Khải thư chất lượng cao. Chữ viết tay, bia mòn và thư pháp lạ vẫn cần chuyên gia hiệu đính. | P (tự công bố) + I về hướng (arXiv cũng nói chữ viết tay khó); con số 95% chưa kiểm độc lập | **ĐÃ XÁC MINH** (chữ viết tay vẫn khó); con số 95% **CHƯA RÕ** | R09, R11 |
| B-P3-C5 | Fine-tune PaddleOCRv5 trên thủ bản Hán Nôm chỉ nâng exact accuracy từ 37,5% lên 50% (một tập con). | P (preprint, có demo) | **SUY LUẬN** (preprint; thước đo khác R09, không so trực tiếp) | R11 |
| B-P3-C6 | Gia phả thường là bản viết tay do trưởng họ giữ; Viện Nghiên cứu Hán Nôm và Thư viện Quốc gia có danh mục gia phả (GCR WP 2025). | Chỉ có snippet (Kyoto GCR WP6, blog MyHeritage) | **SUY LUẬN** | snippet |
| B-P3-C7 | Có dịch vụ dịch thuật thương mại nhận dịch gia phả viết tay; các app gia phả Việt (VNGP, "Gia phả Việt") quản lý cây và ngày giỗ nhưng không đọc Hán Nôm. | Snippet (thaonco, sourceforge, App Store) | **SUY LUẬN** | snippet |
| B-P3-C8 | Số gia đình còn giữ gia phả Hán Nôm và muốn đọc hoặc tục biên năm 2026. | Không có khảo sát | **CHƯA RÕ** | — |

### B-P4

| Claim | Nội dung | Bước đạt | Nhãn | Nguồn |
|---|---|---|---|---|
| B-P4-C1 | Phòng thí nghiệm giữ PC Windows XP, Windows 3.x, DOS để điều khiển kính hiển vi confocal và máy sắc ký. Nâng phần mềm sắc ký tốn $10.000; linh kiện thay thế mua trên eBay. | P (Nature feature 2021, nhiều nhân chứng có tên) + I (R14) | **ĐÃ XÁC MINH** | R13, R14 |
| B-P4-C2 | Khoa Hóa UW–Madison (KB tạo ngày 26/11/2024): nhiều thiết bị đã EOL; phần mềm điều khiển/driver "thường không chạy" trên OS mới; "thay thiết bị khi có kinh phí". Khoa xử lý bằng VLAN riêng và share SMB riêng vì OS cũ chỉ hỗ trợ SMB2. | P (đơn vị vận hành) + M (mô tả cấu hình) | **ĐÃ XÁC MINH** | R14 |
| B-P4-C3 | Vendor (Waters, Instron, Agilent, SCIEX) đang thúc nâng cấp quanh mốc Windows 10 hết hỗ trợ (14/10/2025). | Chỉ có snippet | **SUY LUẬN** | snippet |
| B-P4-C4 | Cơ chế AI-assisted trace recovery của B-P1-C5 áp dụng được cho giao thức PC ↔ thiết bị (serial/GPIB/USB) hoặc định dạng file đầu ra độc quyền. | Suy từ R01; chưa có ví dụ trong lĩnh vực thiết bị khoa học | **GIẢ THUYẾT** | R01 |
| B-P4-C5 | Quy mô năm 2025–2026 (tỷ lệ thiết bị khoa học chạy OS EOL). | Không tìm được khảo sát | **CHƯA RÕ** | — |

### B-P5

| Claim | Nội dung | Bước đạt | Nhãn | Nguồn |
|---|---|---|---|---|
| B-P5-C1 | USCG chấm dứt LORAN-C từ khoảng 8/2/2010 (Federal Register, 7/1/2010), sau khi Quốc hội cho phép trong luật ngân sách FY2010. | P + snippet I (NIST, DVIDS) | **ĐÃ XÁC MINH** | R15 |
| B-P5-C2 | Các trạm Loran-C châu Âu đóng ngày 31/12/2015 vì chi phí. | Snippet Wikipedia/Maritime Executive | **SUY LUẬN** | snippet |
| B-P5-C3 | Nhiễu GNSS ở Vịnh Phần Lan "tăng đáng kể" trong nửa đầu 2025 và tăng mạnh hơn trong tháng 6, đã gây near miss, ảnh hưởng autopilot và AIS. Phần Lan và Estonia ra cảnh báo hàng hải chung. | P (Traficom) + I (IALA 2024 về Baltic; DLR 39C3) | **ĐÃ XÁC MINH** | R16, R17, R18 |
| B-P5-C4 | R-Mode (dùng beacon MF và VDES có sẵn) đang được DLR và đối tác phát triển từ 2017 làm backup mặt đất ở Baltic (dự án ORMOBASS). | P (IALA) + I (DLR) | **ĐÃ XÁC MINH** | R17, R18 |
| B-P5-C5 | Thuyền giải trí cũng bị ảnh hưởng; Traficom nhận khoảng 7.000 báo cáo nhiễu GNSS trong hàng không năm 2024. | Snippet Traficom | **SUY LUẬN** | snippet |
| B-P5-C6 | Người lái thuyền giải trí ở Baltic thiếu kỹ năng hoặc công cụ nhận biết bị spoof và chuyển sang định vị độc lập. | Không có dữ liệu | **GIẢ THUYẾT** | — |

### B-P6

| Claim | Nội dung | Bước đạt | Nhãn | Nguồn |
|---|---|---|---|---|
| B-P6-C1 | Khi Google hiển thị AI summary, người dùng click kết quả truyền thống ở 8% lượt truy cập, so với 15% khi không có summary. Click vào link trong summary chỉ khoảng 1% (900 người lớn Mỹ, 68.879 truy vấn, tháng 3/2025). | P (dữ liệu duyệt web thật, phương pháp công bố) | **ĐÃ XÁC MINH** | R19 |
| B-P6-C2 | 38% trang web tồn tại năm 2013 không còn truy cập được năm 2023/2024; 23% trang tin tức có ít nhất một link hỏng. | P (Common Crawl, tái lập được) | **ĐÃ XÁC MINH** | R20 |
| B-P6-C3 | Phong trào hồi sinh đã tồn tại: Kagi Small Web (repo MIT, khoảng 1,7k sao, chỉ nhận blog cá nhân một tác giả), XXIIVV webring (trần 256 site), Hotline Webring, Warp Point (2026). | P (Kagi repo mở được) + snippet các webring khác | **ĐÃ XÁC MINH** (Kagi); các webring khác **SUY LUẬN** | R21; snippet |
| B-P6-C4 | AI summary làm giảm click về nguồn, nên người viết độc lập mất người đọc. | Suy từ C1 (Pew chỉ đo click từ Google, không đo traffic blog nhỏ) | **SUY LUẬN** | R19 |
| B-P6-C5 | Có nhu cầu đáng kể ngoài nhóm người đam mê với khám phá do người tuyển chọn. | Không có số liệu | **CHƯA RÕ** | — |

## 5. Existing alternatives

| Space | Thay thế mạnh nhất | Hạn chế cụ thể (có nguồn hoặc nhãn) |
|---|---|---|
| B-P1 | **Home Assistant / Open Home Foundation** cùng integration cộng đồng (pywemo, Open Wemo); firmware thay thế (No Longer Evil); khuyến nghị mua thiết bị Matter/HomeKit. | Mỗi thiết bị cần một người reverse-engineer riêng, tốn hàng tháng nếu làm thủ công (R01). Firmware thay thế có thể bị chặn bởi kiểm tra chữ ký (R01). Integration chỉ có cho thiết bị phổ biến; thiết bị ngách như AirPort ACP đầy đủ chưa có trước R01 (R01 nêu AirPyrt Tools 2017 mới hỗ trợ một phần). Matter chỉ giúp thiết bị **mới**. **Đối thủ trực tiếp nhất về phương pháp** là chính R01: nhóm nghiên cứu đã chứng minh pipeline, nên một bản demo hackathon sẽ khó tạo khác biệt về ý tưởng (SUY LUẬN). |
| B-P2 | Dự án server emulator cộng đồng (The Crew Unlimited, R07); kiện tụng/chính sách (UFC-Que Choisir, ECI, AB 1921); GOG/bản offline do publisher tự phát hành. | Emulator cần trace chụp **trước** khi tắt server (R07). Rủi ro DMCA nằm ngoài miễn trừ 201.40(b)(19) (R08). Chính sách EU chỉ dừng ở mức tự nguyện (R06). Chưa có công cụ phổ thông để người chơi "chụp trace trước khi game chết" (GIẢ THUYẾT; chưa tìm kỹ). |
| B-P3 | **Kim Hán Nôm** (HCMUS): OCR, phiên âm, dịch, API, nhắm công chúng chụp gia phả (R09, R10). Dịch giả thuê ngoài. Viện Nghiên cứu Hán Nôm. App gia phả Việt (VNGP, Gia phả Việt). | Chữ viết tay vẫn cần chuyên gia (R09, R11). Kim Hán Nôm trả ra **văn bản**, chưa thấy công bố gì về trích xuất **cấu trúc phả hệ** (ai là con ai, đời thứ mấy, ngày giỗ) để nạp vào app gia phả. App gia phả lại không đọc Hán Nôm (SUY LUẬN từ snippet). Chưa có bằng chứng về quy trình **tục biên** song ngữ (GIẢ THUYẾT). |
| B-P4 | Nâng cấp phần mềm của vendor (tốn kém, R13); cô lập mạng (R14); giữ PC cũ và săn linh kiện (R13); máy ảo, nếu driver cho phép (chưa kiểm). | Nâng cấp có thể tốn $10.000 hoặc buộc thay cả thiết bị (R13). Cô lập mạng chỉ giảm rủi ro, không giải quyết hỏng phần cứng PC (R14). Ở lab GxP, mọi phần mềm thay thế phải qua validation (GIẢ THUYẾT; chưa mở nguồn). Bibliography về thư viện điều khiển mở (PyMeasure, QCoDeS) **chưa kiểm** trong run này. |
| B-P5 | Radar, la bàn, hải đồ ENC có cảnh báo nhiễu (R16, R17); R-Mode ở giai đoạn thử nghiệm (R17, R18); eLoran (UK MOD, theo snippet); hướng dẫn chung của Traficom. | R-Mode chưa phổ cập và cần máy thu riêng (R18). Hệ vệ tinh backup của ESA "có cùng điểm yếu" (nhận định của DLR, R18). Thuyền nhỏ có thể không có radar (GIẢ THUYẾT). Một app phần mềm không thể thay hạ tầng vô tuyến; cùng lắm chỉ hỗ trợ phát hiện spoof và luyện dead reckoning (SUY LUẬN). |
| B-P6 | Kagi Small Web (R21), Marginalia (chưa mở), webring hiện có, RSS reader (Feedly, NetNewsWire), Wayback Machine cho link chết. | Kagi là sản phẩm thương mại gắn công cụ tìm kiếm trả phí (R21). Webring duy trì thủ công, ringmaster phải tự phát hiện site chết hoặc chuyển thành trang đỗ (SUY LUẬN từ quy tắc XXIIVV "site go dark sẽ bị thay"). Không có bằng chứng người đọc phổ thông muốn dùng (CHƯA RÕ). |

## 6. Potential revival opportunities

Phần này chỉ mô tả cơ hội, không xếp hạng hay chọn. Mỗi cơ hội ghi rõ AI có **chịu tải** hay chỉ **trang trí**.

### B-P1 — "End-of-life control transfer" cho thiết bị bị bỏ rơi
- **Hồi sinh gì:** khả năng quản trị cục bộ của thiết bị đã mất hỗ trợ, bằng một client thay thế. Không cần thay firmware.
- **AI chịu tải (SUY LUẬN, dựa trên R01):** suy giao thức từ trace UI + PCAP, sinh code client, so sánh hành vi với oracle trong vòng lặp. R01 cho thấy nút thắt chuyển từ "sinh giả thuyết" sang "chọn trace nào để phân biệt giả thuyết". Đây là chỗ AI và thiết kế thí nghiệm có giá trị thật.
- **Lát cắt nhỏ có thể demo (GIẢ THUYẾT):** một thiết bị cụ thể còn app gốc, ghi trace, rồi có client mở tương thích với báo cáo độ phủ ("hành vi đã thấy / chưa thấy").
- **Rủi ro:** cần phần cứng thật; phạm vi pháp lý (DMCA 1201) chưa rõ với từng thiết bị; R01 đã công bố phương pháp, nên tính mới phụ thuộc vào ngách được chọn.

### B-P2 — "Capture trước khi chết" cho game/dịch vụ sắp tắt
- **Hồi sinh gì:** khả năng chơi game có server, bắt đầu từ việc **ghi lại hành vi server trước ngày tắt**. R07 cho thấy cộng đồng đã làm thủ công.
- **AI chịu tải (GIẢ THUYẾT):** suy schema và state machine từ traffic để dựng emulator. Cùng cơ chế với B-P1 nhưng không có "app gốc làm oracle" sau ngày tắt, nên khó hơn (R01 tự nhận chưa tái dựng được cloud đã mất).
- **AI trang trí:** chatbot giải thích chính sách sunset.
- **Rủi ro lớn:** DMCA (C4–C5), bản quyền nội dung server, thời điểm (phải có trace trước khi tắt).

### B-P3 — Từ gia phả Hán Nôm sang phả hệ có cấu trúc và tục biên song ngữ
- **Hồi sinh gì:** khả năng đọc **và tiếp tục** gia phả. Đây là tập quán xã hội (A2), không chỉ là công nghệ.
- **AI chịu tải (SUY LUẬN):** OCR chữ viết tay, phiên âm, dịch (Kim Hán Nôm đã làm phần lõi); trích quan hệ phả hệ từ văn bản dịch (đời, tên húy, tên tự, ngày giỗ âm lịch) thành dữ liệu cây; hàng đợi hiệu đính cho chuyên gia ở các chỗ có độ tin cậy thấp. Trước đây việc này cần người đọc Hán Nôm cho từng trang.
- **AI trang trí:** chatbot "hỏi tổ tiên".
- **Rủi ro:** Kim Hán Nôm có API và nhắm đúng người dùng này (đối thủ/nền tảng mạnh). Chất lượng trên chữ viết tay thấp (R11). Gia phả là dữ liệu riêng tư. Thiếu mẫu gia phả có quyền dùng để demo.

### B-P4 — Giữ thiết bị khoa học sống sau khi OS chết
- **Hồi sinh gì:** khả năng điều khiển/đọc dữ liệu của thiết bị cũ từ máy hiện đại.
- **AI chịu tải (GIẢ THUYẾT):** suy giao thức serial/GPIB/USB hoặc định dạng file độc quyền từ trace, theo cơ chế R01. Lợi thế so với B-P1: phần mềm gốc **vẫn chạy** trên PC cũ, nên có oracle.
- **AI trang trí:** trợ lý hỏi đáp tài liệu thiết bị.
- **Rủi ro:** thiết bị đắt, demo khó nếu không có phòng thí nghiệm đối tác; lab có quy định (GxP) sẽ không dùng phần mềm chưa validate; điều khoản EULA của vendor.

### B-P5 — Kỹ năng và lớp kiểm tra định vị độc lập
- **Hồi sinh gì:** tinh thần LORAN/dead reckoning, tức một lớp định vị không tin hoàn toàn vào GNSS.
- **Vai trò AI: chủ yếu trang trí (SUY LUẬN).** Phát hiện spoof bằng kiểm tra nhất quán giữa GNSS, la bàn, tốc độ và depth là bài toán lọc cổ điển (Kalman), không cần AI tạo sinh. Một hackathon không thể dựng lại hạ tầng phát sóng.
- **Rủi ro:** an toàn hàng hải; phần mềm trên điện thoại cũng lấy vị trí từ GNSS; người dùng ở Baltic, xa người dùng Việt Nam.

### B-P6 — Webring có người giữ và kiểm tra liên kết
- **Hồi sinh gì:** cấu trúc cộng đồng (ringmaster), không phải giao diện thập niên 90.
- **AI chịu tải một phần (GIẢ THUYẾT):** phát hiện site đã chết, chuyển thành trang đỗ (như CodeProject năm 2026 trong sổ cũ), đổi chủ hoặc chuyển thành nội dung spam, để ringmaster duyệt. Có thể làm bằng heuristic, nhưng phân loại "trang đỗ/đổi chủ" là chỗ mô hình có ích.
- **AI trang trí:** tóm tắt bài blog (đi ngược mục tiêu đưa người đọc về nguồn).
- **Rủi ro:** đối thủ miễn phí rất nhiều; nhu cầu phổ thông CHƯA RÕ.

## 7. Counterevidence and limitations

1. **B-P1:** R01 tự ghi chưa chứng minh tổng quát hóa, dùng "hàng tỷ token", và nhiều bước vẫn phải làm thủ công. Lợi ích "4–5 ngày" là ước lượng hồi cứu của chính tác giả. Bài báo mang tính vận động chính sách (đề xuất quy định), nên điểm Bias chỉ 3. Matter/HomeKit giảm vấn đề cho thiết bị mới, nên vấn đề có thể **thu hẹp dần** theo thời gian (SUY LUẬN).
2. **B-P2:** Ủy ban EU đã từ chối nghĩa vụ bắt buộc và nêu quyền sở hữu trí tuệ (R06). Như vậy môi trường pháp lý ở EU không thuận lợi trong ngắn hạn. Rủi ro DMCA tại Mỹ là thật (R08). Nguồn thứ cấp có lúc phóng đại: Lewis Silkin viết AB 1921 "will impose", trong khi nguồn khác nói dự luật bị kẹt (C6).
3. **B-P3:** Kim Hán Nôm đã nhắm đúng người dùng (chụp gia phả bằng điện thoại). Lý do "chưa có công cụ" **không đứng vững**; chỉ còn khoảng trống ở cấu trúc phả hệ và hiệu đính chữ viết tay, và khoảng trống này chưa được xác nhận. Con số 90% chưa dịch là trích lại, không có phương pháp. Không có bằng chứng trực tiếp rằng gia đình muốn tự làm thay vì thuê dịch giả.
4. **B-P4:** Nature 2021 đã cũ cho claim "còn tồn tại", nhưng KB UW–Madison 2024 giúp làm mới. Không có khảo sát định lượng. Lab có thể chọn cô lập mạng và chấp nhận rủi ro. Đó là "đủ tốt" với nhiều nơi (R14).
5. **B-P5:** Giải pháp thật là hạ tầng (R-Mode/eLoran) và đang được nhà nước, tổ chức tiêu chuẩn làm. Phần mềm hackathon khó tạo tác động thật. Có rủi ro an toàn nếu sản phẩm khuyến khích tin vào ước lượng sai.
6. **B-P6:** Hồi sinh webring **đã diễn ra** (Kagi, XXIIVV, Hotline, Warp Point), nên tính mới thấp. Pew 2025 đo click từ Google ở Mỹ, không đo trực tiếp thiệt hại của blog cá nhân. Pew 2024 đo link rot nói chung, không đo riêng webring.
7. **Chung:** không có phỏng vấn hay quan sát người dùng nào. Mọi nhận định nhu cầu đều từ tài liệu. Tìm kiếm thiên về nguồn tiếng Anh/Mỹ. Một số claim chỉ có snippet nên được hạ nhãn. Thời gian tìm kiếm ngắn, nên đối thủ của B-P2, B-P4 và B-P6 chưa được quét hết.

## 8. Challenged assumptions

| Giả định | Kết luận của Agent B | Bằng chứng |
|---|---|---|
| **A1** Người dùng mục tiêu là cá nhân/gia đình Mỹ–Âu, vấn đề phổ biến | **Bác bỏ như một ràng buộc bắt buộc.** Bằng chứng nhu cầu mạnh nhất của run này đến từ (a) phòng thí nghiệm (R13, R14), (b) hàng hải Baltic (R16), (c) dòng họ Việt Nam (R09). Đều không phải gia đình Mỹ–Âu. Tiêu chí "Potential Impact" của Rules chỉ cần "real audience", không đòi phổ biến. Nhóm hẹp nhưng có nỗi đau chi phí rõ ($10.000 nâng phần mềm) có thể thuyết phục hơn một nhu cầu đại trà mơ hồ (SUY LUẬN). | R13, R14, R16, R09; Rules §3 brief |
| **A2** Yếu tố Resurrection phải là công nghệ lỗi thời | **Bác bỏ một phần.** Câu chữ chính thức nói "dead technology"/"obsolete tech". Hệ chữ Hán Nôm (B-P3) và cấu trúc webring (B-P6) vẫn có phần công nghệ, nhưng giá trị nằm ở **tập quán** (tục biên gia phả, ringmaster). Đây vẫn là diễn giải; giám khảo Stage One có thể xem khác, nên rủi ro theme fit **CHƯA RÕ**. Riêng B-P1, B-P2 và B-P4 thì khớp nghĩa đen "dead technology" rất rõ (thiết bị/game bị giết). | R05, R09, R22 |
| **A3** Có đối thủ là bị loại | **Bác bỏ.** Trong mọi space đều có đối thủ (Kim Hán Nôm, Home Assistant, R01, Kagi). Đối thủ chứng tỏ vấn đề có thật; câu hỏi đúng là **khoảng trống cụ thể nào chưa được phủ** (ví dụ cấu trúc phả hệ, trace trước ngày tắt, oracle hành vi). | R09, R01, R21 |
| **A4** Vấn đề hướng developer là kém phù hợp | **Bác bỏ cho dạng "người kỹ thuật có tài sản bị khóa".** B-P1 và B-P4 có người dùng kỹ thuật với tài sản vật lý cụ thể và chi phí cụ thể. Khác với Stack Overflow, nơi nền tảng còn sống và chính chủ đang làm AI. Yếu tố "dead" ở đây rất rõ (thiết bị/app bị khai tử chính thức, R02, R03). Lưu ý: R01 cho thấy giới nghiên cứu đã vào cuộc. | R01, R02, R03, R13, R14 |
| **A5** "0 PROMISING" nghĩa là không gian đã cạn | **Không đồng ý; nhiều khả năng do bộ lọc.** Chỉ trong một phiên, run này tìm được 3 space (B-P1, B-P2, B-P4) có bằng chứng chính thức 2024–2026 về sự kiện "khai tử" và có cơ chế AI chịu tải được công bố (R01). Các vòng trước giới hạn ở gia đình Mỹ–Âu (A1), media cũ và nền tảng Q&A. Đây là SUY LUẬN, vì tôi chưa áp lại rubric cũ lên các space mới. | R01, R05, R14 |

## 9. Unresolved questions

1. **B-P1/B-P4:** phương pháp R01 có lặp lại được trên một thiết bị khác, rẻ, dễ mua (không phải AirPort) trong vài ngày không? Thiết bị nào còn app gốc chạy được để làm oracle? Cách kiểm tra nhỏ nhất có thể bác bỏ: chọn 1 thiết bị, ghi 1 workflow, đo thời gian đến khi replay tương đương.
2. **B-P1:** phạm vi DMCA 1201(f) (interoperability) và luật EU cho client quản lý thay thế, khi không phá firmware. Chưa tra.
3. **B-P2:** trạng thái chính thức của AB 1921; câu chữ thông cáo IP/26/1369; dự án The Crew Unlimited năm 2026 còn hoạt động không.
4. **B-P3:** Kim Hán Nôm có trích cấu trúc phả hệ không, và API có điều khoản cho phép bên thứ ba dùng không? Có mẫu gia phả công khai, có quyền dùng không (ví dụ trong danh mục GCR/Viện Hán Nôm)? Phép thử nhỏ nhất: hỏi 5 người giữ gia phả họ đã làm gì với bản Hán Nôm, đã thuê dịch chưa, giá bao nhiêu.
5. **B-P4:** có khảo sát 2025–2026 nào về tỷ lệ thiết bị lab chạy OS EOL không? Thư viện mở (PyMeasure, QCoDeS, ProteoWizard) đã phủ bao nhiêu thiết bị? Chưa kiểm.
6. **B-P5:** thuyền giải trí ở Baltic thực sự xử lý nhiễu thế nào? Có dữ liệu sự cố cho thuyền nhỏ không?
7. **B-P6:** ngoài cộng đồng IndieWeb, có người đọc nào chủ động tìm nguồn do người tuyển chọn không? Có dữ liệu traffic của blog nhỏ trước và sau AI Overviews không?
8. **Theme fit (A2):** giám khảo Stage One có chấp nhận "tập quán/hệ chữ" như dead technology không? Cần Coordinator quyết định cách diễn giải.

## 10. Evaluated references

Điểm: Auth = Source Authority, Tech = Technical Evidence, Mech = Mechanism Correctness, Ctx = Context Fit, Fresh = Freshness, Repro = Reproducibility, Bias = Commercial/Opinion Bias (cao = ít thiên lệch). Weighted = Σ(trọng số × điểm/5) × 100. Mọi nguồn trong bảng **đã được mở và đọc** ngày 2026-11-25.

| Ref ID | URL | Title | Publisher | Pub date | Accessed | Claims supported | Auth | Tech | Mech | Ctx | Fresh | Repro | Bias | Weighted | Source Reliability | Reference Relevance |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R01 | https://cs.stanford.edu/~jhumphri/documents/you-bought-it-they-bricked-it.pdf | You Bought It, They Bricked It: A Call for Reclaiming Local Control | HotNets '26 (ACM), J. T. Humphries | 2026-11 (HotNets 16–17/11/2026) | 2026-11-25 | B-P1-C1,C2,C3,C5,C6; B-P4-C4 | 4 | 5 | 4 | 5 | 5 | 3 | 3 | 86 | High | High |
| R02 | https://www.macrumors.com/2024/12/10/spotify-car-thing-officially-dead/ | Spotify's Car Thing Accessory is Officially Dead | MacRumors | 2024-12-10 | 2026-11-25 | B-P1-C1 | 3 | 2 | 3 | 5 | 4 | 4 | 4 | 67 | Medium | High |
| R03 | https://www.macrumors.com/2026/06/22/apple-airport-utility-ios-27/ | Apple Dropping AirPort Utility From the App Store With iOS 27 | MacRumors | 2026-06-22 | 2026-11-25 | B-P1-C2, C7 | 3 | 3 | 4 | 5 | 5 | 4 | 4 | 77 | Medium | High |
| R04 | https://9to5google.com/2025/11/03/google-nest-thermostat-old-revive-project/ | (Old Nest Thermostat revive project — No Longer Evil) | 9to5Google | 2025-11-03 | 2026-11-25 | B-P1-C4 | 3 | 3 | 4 | 4 | 5 | 4 | 4 | 74 | Medium | Medium |
| R05 | https://citizens-initiative.europa.eu/news/european-commission-replies-stop-destroying-videogames-initiative-2026-06-16_en | European Commission replies to 'Stop Destroying Videogames' initiative | European Commission, Secretariat-General (ECI) | 2026-06-16 | 2026-11-25 | B-P2-C1, C2 | 5 | 3 | 3 | 5 | 5 | 5 | 5 | 84 | High | High |
| R06 | https://www.lewissilkin.com/insights/2026/06/24/european-commission-stops-short-of-imposing-mandatory-requirements-following-citi-102n4yy | European Commission stops short of imposing mandatory requirements following citizens' Stop Destroying Videogames initiative | Lewis Silkin LLP | 2026-06-24 | 2026-11-25 | B-P2-C1, C2, C6 | 3 | 2 | 4 | 5 | 5 | 3 | 4 | 71 | Medium | High |
| R07 | https://pcgamer.com/games/racing/ubisoft-is-stripping-peoples-licences-for-the-crew-weeks-after-its-shutdown-nearly-squandering-hopes-of-private-servers-and-acting-as-a-stark-reminder-of-how-volatile-digital-ownership-is | Ubisoft is stripping people's licences for The Crew weeks after its shutdown… | PC Gamer (Mollie Taylor) | 2024-04-12 | 2026-11-25 | B-P2-C3 | 3 | 2 | 3 | 4 | 3 | 3 | 4 | 60 | Medium | Medium |
| R08 | https://www.law.cornell.edu/cfr/text/37/201.40 | 37 CFR § 201.40 — Exemptions to prohibition against circumvention | Cornell LII (bản sao eCFR, US Copyright Office) | hiện hành (không ghi ngày trên trang đã trích) | 2026-11-25 | B-P2-C4, C5 | 5 | 3 | 5 | 4 | 4 | 5 | 5 | 87 | High | High |
| R09 | https://en.hcmus.edu.vn/ai-unlocks-han-nom-heritage-opening-the-door-to-a-millennium-of-knowledge-for-wider-public-access/ | AI Unlocks Hán Nôm Heritage: Opening the Door to a Millennium of Knowledge for Wider Public Access | ĐH Khoa học Tự nhiên, ĐHQG-HCM | 2026-07-19 | 2026-11-25 | B-P3-C2, C3, C4 | 4 | 3 | 4 | 5 | 5 | 3 | 2 | 77 | Medium | High |
| R10 | https://tools.clc.hcmus.edu.vn/ | Kim Hán Nôm (công cụ web) | HCMUS – CLC | không rõ | 2026-11-25 | B-P3-C3 | 4 | 2 | 2 | 4 | 5 | 4 | 3 | 65 | Medium | Medium |
| R11 | https://arxiv.org/abs/2510.04003v1 | Enhancing OCR for Sino–Vietnamese Language Processing via Fine-Tuned PaddleOCRv5 | arXiv (preprint) | 2025-10 | 2026-11-25 | B-P3-C4, C5 | 3 | 4 | 4 | 4 | 5 | 4 | 4 | 78 | Medium | Medium |
| R12 | https://tuoitre.vn/duong-khoa-cu-tu-day-dut-han-500717.htm | Đường khoa cử từ đây dứt hẳn | Tuổi Trẻ (dẫn *Khoa cử Việt Nam*, Nguyễn Thị Chân Quỳnh, 2007) | 2012-07-08 | 2026-11-25 | B-P3-C1 | 3 | 2 | 3 | 4 | 3 | 4 | 5 | 63 | Medium | Medium |
| R13 | https://media.nature.com/original/magazine-assets/d41586-021-01431-y/d41586-021-01431-y.pdf | Old-school computing: when your lab PC is ancient | Nature (J. Nowogrodzki) | 2021 | 2026-11-25 | B-P4-C1 | 4 | 3 | 4 | 5 | 2 | 4 | 5 | 76 | High | High |
| R14 | https://kb.wisc.edu/uwmadchem/144993 | (Lab instrument computers with EOL operating systems — restricted network) | UW–Madison Chemistry Dept. KB | 2024-11-26 (Created) | 2026-11-25 | B-P4-C1, C2 | 4 | 4 | 5 | 5 | 4 | 4 | 5 | 88 | High | High |
| R15 | https://www.govinfo.gov/content/pkg/FR-2010-01-07/html/2010-84.htm | Terminate Long Range Aids to Navigation (Loran-C) Signal | Federal Register 75(4), USCG | 2010-01-07 | 2026-11-25 | B-P5-C1 | 5 | 3 | 4 | 5 | 5 | 5 | 5 | 88 | High | High |
| R16 | https://traficom.fi/en/news/finland-and-estonia-warn-vessels-gulf-finland-increase-gnss-disruptions | Finland and Estonia warn vessels in the Gulf of Finland of an increase in GNSS disruptions | Traficom (Phần Lan) | 2025-06 | 2026-11-25 | B-P5-C3 | 5 | 3 | 4 | 4 | 4 | 4 | 5 | 81 | High | High |
| R17 | https://www.iala.int/e-bulletin/gnss-jamming-and-spoofing-navigating-challenges-in-the-baltic-sea/ | GNSS Jamming and Spoofing: Navigating Challenges in the Baltic Sea | IALA | 2024-09-12 | 2026-11-25 | B-P5-C3, C4 | 5 | 3 | 5 | 4 | 3 | 4 | 4 | 82 | High | High |
| R18 | https://events.ccc.de/congress/2025/hub/en/event/detail/who-cares-about-the-baltic-jammer-terrestrial-navigation-in-the-baltic-sea-region | Who cares about the Baltic Jammer? – Terrestrial Navigation in the Baltic Sea Region | 39C3 (CCC), nhóm DLR | 2025-12 (39C3) | 2026-11-25 | B-P5-C3, C4 | 4 | 2 | 4 | 4 | 5 | 3 | 3 | 71 | Medium | Medium |
| R19 | https://www.pewresearch.org/short-reads/2025/07/22/google-users-are-less-likely-to-click-on-links-when-an-ai-summary-appears-in-the-results/ | Google users are less likely to click on links when an AI summary appears in the results | Pew Research Center | 2025-07-22 | 2026-11-25 | B-P6-C1, C4 | 5 | 5 | 4 | 4 | 5 | 4 | 5 | 91 | High | Medium |
| R20 | https://www.pewresearch.org/data-labs/2024/05/17/when-online-content-disappears/ | When Online Content Disappears | Pew Research Center | 2024-05-17 | 2026-11-25 | B-P6-C2 | 5 | 5 | 4 | 3 | 4 | 5 | 5 | 88 | High | Medium |
| R21 | https://github.com/kagisearch/smallweb | Kagi Small Web | Kagi (GitHub) | không rõ (repo đang hoạt động) | 2026-11-25 | B-P6-C3 | 4 | 3 | 3 | 4 | 5 | 5 | 2 | 74 | Medium | Medium |
| R22 | https://en.wikipedia.org/wiki/Webring | Webring | Wikipedia (dẫn Salon 2001) | không rõ (bản hiện hành) | 2026-11-25 | B-P6 lịch sử (§3) | 2 | 2 | 3 | 4 | 3 | 4 | 4 | 58 | Low | Medium |

### 10.1 Nguồn chỉ thấy qua snippet tìm kiếm, không chấm điểm

Các nguồn này **chưa được mở hoặc không đọc được nội dung**. Claim dựa vào chúng có nhãn tối đa là SUY LUẬN.

| Nguồn (URL) | Dùng cho | Trạng thái |
|---|---|---|
| https://www.belkin.com/support-article/?articleNum=335419 | B-P1-C3 | Tải được nhưng nội dung render bằng JS; không đọc được |
| https://www.bgr.com/2312274/what-to-do-with-old-belkin-wemo-smart-home/ | B-P1-C3, B-P1 §5 | Chỉ snippet |
| https://9to5mac.com/2025/10/27/neato-cloud-shutdown-is-the-latest-example-of-a-failed-company-bricking-smart-products/ | bối cảnh B-P1 | Mở được nhưng không trích được thân bài |
| https://newsletter.openhomefoundation.org/you-dont-own-it-if-they-can-break-it/ | B-P1 §5 | Chỉ snippet |
| https://citizens-initiative.europa.eu/news/14th-valid-initiative-stop-destroying-videogames-submitted-commission-examination-2026-01-26_en ; https://heise.de/-11154579 | B-P2-C1 (ngày nộp, 1.294.188) | Chỉ snippet |
| https://www.pcgamer.com/gaming-industry/the-stop-killing-games-movement-hits-another-major-milestone-as-a-game-preservation-bill-passes-california-state-assembly-vote/ ; https://www.bakerlaw.com/insights/sunsetting-video-games-california-considering-increasing-longevity/ | B-P2-C6 | Chỉ snippet; mâu thuẫn trạng thái |
| https://gcr.cseas.kyoto-u.ac.jp/wp-content/uploads/2025/05/GCR_WP6.pdf | B-P3-C6 | Chỉ snippet |
| https://thaonco.com/vi/translation-times/ngon-ngu/dich-chu-nom-sang-tieng-viet/ ; https://vngp.sourceforge.io | B-P3-C7 | Chỉ snippet (trang dịch vụ mang tính quảng cáo) |
| https://www.familysearch.org/vi/giapha/ | B-P3 | Bị chặn (Incapsula) |
| https://traficom.fi/en/news/flight-safety-remained-good-various-occurrences-increased-finnish-transport-and-communications-agency-traficom-published-finnish-aviation-safety-review-2024 | B-P5-C5 | Chỉ snippet |
| https://maritime-executive.com/article/europe-gives-up-on-eloran ; https://en.wikipedia.org/wiki/Rantum_Loran-C_transmitter | B-P5-C2 | Chỉ snippet |
| https://www.instron.com/en/resources/blog/2025/june/is-your-testing-lab-windows-11-ready/ ; https://www.waters.com/blog/staying-current-why-upgrading-matters-for-your-labs-future/ ; https://sciex.com/support/software-support/analyst-software-end-of-support | B-P4-C3 | Chỉ snippet (SCIEX mở được nhưng không có đoạn liên quan) |
| https://github.com/XXIIVV/webring ; https://readonlymemo.com/warp-point-announcement-gaming-webring/ | B-P6-C3 | Chỉ snippet |
| https://vjol.info.vn/ssir/article/download/114967/96223 | B-P3 §3 (mốc 1945) | Chỉ snippet |

### 10.2 Tổng hợp số lượng

- Problem spaces: **6** (5 mới, 1 xem lại một phần với góc mới).
- Claims: **38** (B-P1: 8, B-P2: 6, B-P3: 8, B-P4: 5, B-P5: 6, B-P6: 5). Phân bố nhãn: ĐÃ XÁC MINH 17, SUY LUẬN 13, GIẢ THUYẾT 3, CHƯA RÕ 5. Claim có nhãn kép được tính theo nhãn đứng đầu.
- References đã chấm điểm: **22**. Nguồn chỉ có snippet, không chấm: **14 mục** (một số mục gộp nhiều URL).
- Failures: **10** (xem Metadata).
