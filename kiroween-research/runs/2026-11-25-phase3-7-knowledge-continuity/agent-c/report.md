# Phase 3 — Agent C

## Metadata

- Run: `2026-11-25-phase3-7-knowledge-continuity`; chỉ Phase 3. Bắt đầu UTC: 2026-11-25T16:15:00Z (xấp xỉ); kết thúc và thống kê cuối được ghi sau kiểm tra ở cuối mục này.
- Model/effort thực chạy: **not observable**. Brief yêu cầu gpt-6.1-sol/medium; không coi cấu hình yêu cầu là bằng chứng runtime. Không nâng effort, không gọi worker phụ.
- Khoảng 46 truy vấn web; đếm nguồn tham chiếu duy nhất trong §9, không đếm các lần mở lại. Ngày truy cập tất cả nguồn: **2026-11-25 UTC**. Dùng `better-writing` cho văn bản và `orca-cli` cho thông báo hoàn thành.
- Độc lập: đọc đúng các tài liệu được cấp; không đọc thư mục agent khác của run này, không liên hệ agent khác. Chỉ ghi vào `agent-c/`; không cài đặt, triển khai, commit, gửi thư hay làm thí nghiệm bên ngoài. Không sửa ba tệp progress toàn dự án vì giới hạn ghi của dispatch cụ thể hơn.
- Thất bại truy cập: DOI TAIR 2026 và URL OUP tương ứng lỗi 500/không truy cập; TAIR 2024 OUP lỗi 500; PDF Kyodokinyu lỗi 502; docs PKP bị Anubis; Vectors USC timeout; WSU College of Arts 403; Mastodon URL backing-up không truy cập; Zenodo FAQ không truy cập; Software Heritage mission/home timeout; datatransferproject.dev 404; EUR-Lex trả robot challenge; PDF KeMCo 502; `curl` PDF KeMCo thất bại exit 60, không vô hiệu hóa TLS; Browsertrix.com chỉ trả redirect không có nội dung; truy cập lại phần RedeOT/Colivre trong PDF gov.br timeout hai lần. Các fallback thành công được chỉ rõ trong §9. Không dùng trang lỗi làm bằng chứng đã xác minh.
- Hạn chế: không phỏng vấn, không đo đầy đủ archive hay tái chạy ứng dụng; chưa xác minh độc lập chi phí, số người dùng và tính đầy đủ do tổ chức tự báo cáo. Không có token meter; token và chi phí **not observable**. Khối lượng công việc là desk research, không phải market validation.

- Kiểm tra cuối UTC: **2026-11-25T16:30:18Z**. Claim duy nhất: **66**; **VERIFIED 24**, **INFERENCE 34**, **HYPOTHESIS 4**, **UNKNOWN 4**. Tham chiếu trong §9: **45 direct / 3 snippet-only** (không tính local brief/rubric/rules). Đủ cấu trúc bốn không gian; evidence validation còn partial như từng mục, không báo là đã market-validate.

## 1. Method

Đi theo chuỗi lịch sử công nghệ → công việc người dùng → nguồn lực suy giảm → hành động thay thế → giá trị còn mất. Phân tích từng không gian bằng cây vấn đề, stakeholder/JTBD, hành vi đã xảy ra, đối thủ mạnh nhất và điều kiện bác bỏ. Chỉ sau §2–5 mới kiểm tra cơ chế chung. Không thiết kế kiến trúc, MVP, chọn sản phẩm, tính điểm tổng hay thực hiện Phase 4–7.

Nhãn claim: **VERIFIED / ĐÃ XÁC MINH**, **INFERENCE / SUY LUẬN**, **HYPOTHESIS / GIẢ THUYẾT**, **UNKNOWN / CHƯA RÕ**. Một câu “tổ chức X chính thức nói Y” có thể VERIFIED từ chính tài liệu X; điều đó không biến Y thành phép đo độc lập. P = mở nguồn gốc, I = xác nhận độc lập, M = kiểm tra cơ chế/tái lập. Không gọi tài liệu cùng tác giả, cùng dự án hoặc bản tin chép lại là I độc lập. M trong nghiên cứu này chủ yếu là đối chiếu tài liệu và đường bàn giao, chưa chạy phần mềm.

Các prior claim được kiểm tra: Task B `B-O2-C3` (ArchiveTeam cần hợp tác), `C-G-C1` (DOI không xác nhận bảo tồn không đồng nghĩa đã mất), `C-G-C2` (nguồn lực và kế nhiệm), `C-G-C4` (bảo tồn có chọn lọc), `C-G-C15/C20` (mất ngữ nghĩa), cùng các giả thuyết H2/H3/H4/H8 trong synthesis. Các tài liệu synthesis là đầu mối, không được tính thành xác nhận độc lập. Chỉ tham chiếu claim ID có trong context được cấp; không tự gán mã cho prior findings không có mã.

## 2. S2 — Research apps after funding

### a. Problem and root causes

**C-S2-C1 — VERIFIED.** Nhóm Araport báo cáo tiền hết năm 2016, renewal bị từ chối tháng 12/2018; nhóm chọn chuyển các chức năng được dùng nhiều thay vì duy trì toàn hệ sinh thái. Đây là bằng chứng chính chủ về một dịch vụ tin sinh học sau grant, không phải bằng chứng mọi web app đều như vậy. P: [R1]; I: chưa độc lập; M: bài mô tả cụ thể chủ thể nhận và thành phần chuyển.

**C-S2-C2 — INFERENCE.** Cây vấn đề: tài trợ phát triển kết thúc → mất nhân sự cập nhật/hiểu phụ thuộc → môi trường cũ hoặc dữ liệu ngừng cập nhật → kết quả truy vấn, track và khả năng tái sử dụng suy giảm. Nhánh tài chính và nhánh kỹ thuật có thể tách nhau: thêm bản sao không thuê được biocurator. [R1, R2, R3]. Mở rộng prior `C-G-C2`; không chấp nhận giả định “hết grant = app chết”. Không nên duy trì runtime khi dữ liệu/thuật toán đã được nơi khác cung cấp đầy đủ, không còn người dùng, hoặc chi phí thẩm định khoa học lớn hơn giá trị chức năng còn lại.

### b. Stakeholders and target users

| Actor | Job-to-be-done | Hành vi hiện tại | Góp sức/trả tiền | Mức bằng chứng | Evidence |
|---|---|---|---|---|---|
| PI/nhóm Araport cũ | Giữ các truy vấn/track có ích sau grant | Họp và bàn giao phần hữu dụng | Thời gian chuyên gia; không thấy mua công cụ mới | Demonstrated, C1 | R1 |
| Phoenix Bioinformatics/TAIR | Duy trì tài nguyên sinh học được dùng | Thu subscription, vận hành dịch vụ | Người dùng/tổ chức mua quyền truy cập theo TAIR | Demonstrated dưới dạng tuyên bố chính chủ, C3 | R2 |
| Thư viện/chủ thể kế nhiệm | Nhận tài sản có thể quản lý lâu dài | HDS tái tổ chức sau AHDS | Năng lực tổ chức; ngân sách cụ thể chưa rõ | Demonstrated cho bàn giao, C4 | R5 |
| Nhóm grant nhỏ chưa có người kế nhiệm | Chuyển trách nhiệm trước khi giải tán | Chưa quan sát trực tiếp trong mẫu | WTP cho công cụ mới chưa rõ | Hypothetical, C5 | Không có phỏng vấn |

### c. Documented cases by region

**C-S2-C3 — VERIFIED.** NA: TAIR chính thức nói NSF tài trợ 1999–2013 và từ 2014 nguồn thu là subscriptions từ đại học, công ty và cá nhân. Araport chuyển JBrowse sang TAIR ở Mỹ và ThaleMine sang BAR tại Toronto. [R1, R2]. Đây là hành vi tiếp tục duy trì, không phải tĩnh hóa.

**C-S2-C4 — VERIFIED.** EU: University of Essex ghi AHDS History đóng 31/3/2008 và HDS ở UK Data Archive ra mắt lại 1/4/2008 sau quyết định rút tài trợ. DCC bình luận cùng thời về việc mất chuyên môn và thiếu lộ trình thoát. [R5, R6]. P+I cho việc rút tài trợ; chưa kiểm tra mọi bộ dữ liệu sau chuyển.

**C-S2-C5 — UNKNOWN.** Chưa tìm thấy WTP cho công cụ continuity mới của nhóm app nhỏ; không có ca Other đủ gần với web app sau grant trong lượt tìm này. Truy vấn đã thử: “TAIR subscription funding NSF Araport shutdown”, “AHDS funding ceased March 2008”, “KEGG subscription July 2011 funding grant”. Truy vấn bổ sung ‘Africa research database discontinued funding web application sustainability’ cũng chưa đưa ra ca S2 phù hợp được kiểm tra trực tiếp. Không chuyển bằng chứng trả subscription nội dung thành WTP phần mềm migration.

**C-S2-C6 — VERIFIED.** Asia: người sáng lập KEGG tại Nhật giải thích từ 2011 nguồn grant thay đổi, không đủ giữ curator/developer, và chuyển FTP học thuật sang cơ chế thuê bao; web/API được nói là không bị thay đổi bởi chuyển đổi đó. [R3]. P; xác minh phạm vi tuyên bố, không kiểm toán thu chi. Bảng giá lưu trữ 2011/2019 tồn tại [R4], không dùng nó như giá 2026.

### d. Demand and consequences of inaction

**C-S2-C7 — INFERENCE.** Nhu cầu giữ chức năng có hành vi thật: chuyển chủ thể, cập nhật phần mềm và thu tiền truy cập. Hệ quả không hành động là track không chạy hoặc tri thức không được cập nhật, ngoài việc URL mất. Bằng chứng gần thời điểm hiện tại cho *nhu cầu một giải pháp mới* còn yếu; snippet bài TAIR 2026 nói có 220 subscriber tổ chức vào 8/2025, nhưng không dùng số này để chấm demand 5 vì mở nguồn thất bại. [R1, R2, R43].

### e. Existing solutions and limits

**C-S2-C8 — VERIFIED.** Zenodo chính thức nhận research artifacts và có bản sao/fixity, đồng thời không cam kết usability/understandability lâu dài. Vì vậy không được gọi việc nộp mã lên Zenodo là cam kết chạy lại web app. [R7]. P, M: đối chiếu mục Functional preservation trong policy; chưa chạy artifact.

**C-S2-C9 — INFERENCE.** Đối thủ/thay thế mạnh nhất trong các ca đã kiểm tra là **bàn giao có chọn lọc cho TAIR/BAR**, rồi nguồn thu bảo trợ; Zenodo xử lý lưu trữ, Browsertrix xử lý phần web quan sát được. [R1, R7, R19]. Khoảng trống “không ai bảo tồn web động” không đứng vững. Chưa chứng minh phần thiếu là tự động hóa tĩnh hóa thay vì nhân sự, quyền và sự đồng ý của đơn vị nhận.

### f. Barriers

**C-S2-C10 — INFERENCE.** Pháp lý: giấy phép phần mềm/dữ liệu và dữ liệu nhạy cảm phải cho phép chuyển; policy Zenodo không chuyển ownership. Tài chính: có chi phí curation định kỳ. Kỹ thuật: phụ thuộc dịch vụ ngoài, version và truy vấn chưa thu trước; tổ chức: người nhận phải nhận trách nhiệm kiểm định và hỗ trợ khoa học. [R1, R2, R7]. Đây là danh mục rủi ro cần kiểm tra theo tài sản, không kết luận pháp lý cho tổ chức cụ thể.

### g. Who pays, who maintains

**C-S2-C11 — INFERENCE.** Người trả có bằng chứng gần nhất là cộng đồng thuê bao TAIR/KEGG; người duy trì là nonprofit hoặc nhóm đại học kế nhiệm. [R2, R3]. Commercial viability: có mô hình tài trợ *tài nguyên và chuyên gia*, chưa có hợp đồng cho *công cụ chuyển giao*. Việc nhắm nhóm đã hết tiền làm payer mặc định là không được bằng chứng hỗ trợ.

### h. AI: meaningful advantage or not

**C-S2-C12 — HYPOTHESIS.** AI có thể giúp đọc mã cũ, mô tả dependency hoặc đề xuất test; chưa có benchmark nào trong mẫu chứng minh giảm chi phí continuity. Baseline là tài liệu, package/version pinning, migration thủ công và regression test. AI không cần cho checksum, sao chép, chọn chủ thể nhận hoặc quyết định độ đúng khoa học. Không chấm “load-bearing”.

### i. Preservation vs restoring functionality

**C-S2-C13 — VERIFIED.** Theo bài của nhóm thực hiện, JBrowse được chuyển và khôi phục track hỏng; ThaleMine được dựng lại trên InterMine mới vì bản cũ không forward-compatible. [R1]. Điều này chứng minh họ chọn phục hồi chức năng; chưa đo causal benefit hay số người dùng được cứu. H8 “đa số tĩnh hóa được” vẫn chưa kiểm chứng: genome browser/truy vấn backend không đồng nghĩa trang HTML tĩnh.

### j. Resurrection theme fit

**C-S2-C14 — INFERENCE.** **Theme 1/M cho S2 hiện tại.** Grant hết không phải công nghệ chết; TAIR, KEGG, InterMine/JBrowse trong các ca này vẫn tiếp tục hoặc đã chuyển. Araport/ADAMA mất hỗ trợ là đầu mối lịch sử, nhưng chưa có thông báo retirement cụ thể đủ chắc và chưa xác lập phần chưa được phục hồi. Không kế thừa điểm 3 Task B chỉ vì app cũ. Chỉ một nhánh có công nghệ/product chính thức retired thật sự làm trung tâm mới có thể đạt ≥3 theo anchor.

### k. Verdict for this space

**C-S2-C15 — INFERENCE.** **Narrow** về vấn đề bàn giao các chức năng nghiên cứu còn được dùng, có quyền chuyển và người nhận xác định; giữ như nghiên cứu BA, **chưa qua theme gate**. C1/C13 hỗ trợ functional continuity; C5/C9 ngăn suy ra thị trường tĩnh hóa hàng loạt. Không chọn sản phẩm. Bác bỏ hướng thiếu tooling nếu các ca đủ quyền/người nhận đều xử lý được bằng chuyển chủ thể và công cụ hiện có, hoặc không ai cần chạy lại chức năng.

## 3. T2 — Small-platform shutdown window

### a. Problem and root causes

**C-T2-C1 — VERIFIED.** Glitch chính thức thông báo tắt hosting/profile ngày 8/7/2025, cho tải mã hết 2025 và đặt redirect; lý do họ nêu gồm chi phí, lạm dụng và kiến trúc legacy không còn lợi thế so với nền tảng thay thế. [R8]. P; đây là lời giải thích công ty, không kiểm toán nguyên nhân.

**C-T2-C2 — INFERENCE.** Cây vấn đề: đơn vị vận hành không muốn/không đủ sức tiếp tục → cửa sổ export hữu hạn → người dùng phải chọn, lấy và chuyển tài sản → sau khi server tắt mất API, tài khoản hoặc URL. Cần tách dữ liệu cá nhân, nội dung công khai và code ứng dụng. [R8, R10, R12]. “Nhỏ” mô tả nguồn lực vận hành tương đối; Glitch thuộc Fastly và GMO không phải doanh nghiệp nhỏ, nên chúng là ca platform/community, không chứng minh riêng thị trường small SaaS. Không nên khôi phục những dự án không được dùng hoặc đã thay được hoàn toàn.

### b. Stakeholders and target users

| Actor | Job-to-be-done | Hành vi hiện tại | Góp sức/trả tiền | Mức bằng chứng | Evidence |
|---|---|---|---|---|---|
| Chủ dự án Glitch | Giữ app/URL còn hữu dụng | Archive, viết lại, rehost một số app; bỏ một số app | Thời gian cá nhân; không có hóa đơn công cụ rescue | Demonstrated, C3 | R9 |
| Cohost staff và ArchiveTeam | Đóng dịch vụ nhưng giữ bản công khai | Kéo dài cửa sổ, thay API, cung cấp danh sách | Thời gian/hosting; không thấy hợp đồng | Demonstrated, C4 | R10–R11 |
| Blogger Nhật | Giữ lịch sử và người đọc khi nhà cung cấp đóng | Di chuyển nhiều lần | Công sức; WTP chưa rõ | Demonstrated như tự báo cáo, C6 | R16 |
| Nhà vận hành small SaaS sắp hết tiền | Kết thúc hợp lệ, giảm công hỗ trợ | Chưa có mẫu hợp đồng shutdown service | Payer còn là giả thuyết | Hypothetical, C10 | Chưa có |

### c. Documented cases by region

**C-T2-C3 — VERIFIED.** NA: Marty McGuire công bố đã archive các dự án Glitch, rehost/viết lại một số, và chủ động không duy trì một số dự án rất ít dùng. [R9]. P về hành động của chính tác giả; thông báo shutdown được R8 xác nhận, không xác nhận độc lập mọi migration của tác giả.

**C-T2-C4 — VERIFIED.** NA: ArchiveTeam ghi Cohost giữ online đến khi thu thập xong, bỏ TRPC batching và cung cấp danh sách public users; staff xác nhận chuẩn bị tắt server sau khi ArchiveTeam báo hoàn tất. [R10, R11]. P+I cho việc hợp tác và shutdown; M: log mô tả crawl/replay, chưa tự replay toàn bộ. Xác nhận prior `B-O2-C3`, không suy ra archive đầy đủ tuyệt đối.

**C-T2-C5 — VERIFIED.** EU: easyname chính thức nói đã mua Soup.io năm 2017 để ổn định kỹ thuật rồi tìm người vận hành mới năm 2018 vì thiếu thời gian; ArchiveTeam ghi Soup.io Vienna đóng năm 2020 và dự án cứu chỉ được một phần nhỏ. [R12, R13]. Hai sự kiện khác nhau; không dùng tuyên bố 2018 để xác minh nguyên nhân đóng 2020. P cho các lời công bố; chưa kiểm tra archive.

**C-T2-C6 — VERIFIED.** Asia: GMO công bố teacup kết thúc 1/8/2022; blogger `element6` kể chuyển khỏi teacup năm 2022 rồi lại phải chuyển khi goo blog đóng năm 2025. [R14, R16]. P về lời kể cá nhân và thông báo riêng, không đại diện mọi người dùng Nhật. Other: chưa xác minh được ca đủ gần với small platform trong lượt này; có chạy thêm truy vấn ‘South America small social platform shutdown export community archive’. Các đầu mối chưa được kiểm tra đầy đủ không được đưa thành case; truy vấn “Glitch hosting shutdown”, “Soup.io shutdown ArchiveTeam Austria”, “teacup 2022 サービス終了 GMO”.

### d. Demand and consequences of inaction

**C-T2-C7 — INFERENCE.** Hành vi cứu/migration là nhu cầu demonstrated về tài sản, nhưng phần trả tiền cho dịch vụ mới là hypothetical. Soup là cảnh báo cửa sổ ngắn và rescue không toàn diện; Cohost là phản chứng rằng hợp tác có thể đủ để có archive tốt hơn. [R9–R13]. Không archive được không chứng minh cần giữ nguyên cộng đồng tương tác sống mãi; không có số tổn thất kinh tế được kiểm chứng.

### e. Existing solutions and limits

**C-T2-C8 — VERIFIED.** Tài liệu Mastodon cho phép export Activity Streams 2.0 nhưng nói không import posts/media, và chuyển profile không chuyển posts. DTP có framework chuyển giữa nhà cung cấp tham gia. [R17, R18]. P về tính năng được nhà phát triển công bố; chưa test API. Vì vậy “download được = tiếp tục workflow được” không đúng, nhưng cũng sai khi coi migration chưa có hạ tầng.

**C-T2-C9 — INFERENCE.** Các thay thế mạnh nhất: export/redirect gốc của Glitch, migration theo nhà cung cấp mới, Mastodon/DTP cho phạm vi được hỗ trợ, ArchiveTeam và Browsertrix cho truy cập archive. [R8, R17–R19]. Browsertrix đã có QA, replay và WACZ; không nên tuyên bố novelty từ việc bọc chúng. Khoảng trống xuyên nền tảng về reply graph, danh tính hay runtime vẫn cần artifact thật để đo, như H2 đề nghị; chưa chứng minh AI tốt hơn parser schema.

### f. Barriers

**C-T2-C10 — INFERENCE.** Pháp lý: người export không sở hữu mọi reply/media của người khác, dữ liệu riêng và quyền xóa cần được xử lý riêng. Tài chính: bên đóng cửa có ít ngân sách; bên nhận phải có động cơ và tài nguyên. Kỹ thuật: token, URL, dependency/backend và thời hạn; tổ chức: trách nhiệm hỗ trợ/kiểm duyệt không tự chuyển theo ZIP. [R8, R10, R17, R20]. EUR-Lex bị challenge nên không rút kết luận rằng GDPR/Data Act buộc mọi small SaaS phải tài trợ công cụ này.

### g. Who pays, who maintains

**C-T2-C11 — UNKNOWN.** Không tìm thấy giao dịch trực tiếp mua công cụ shutdown-window cho operator nhỏ trong mẫu. Người dùng/archivist đóng góp công là có; nhà vận hành trả phí để kết thúc có trách nhiệm là giả thuyết. Chủ app hoặc dịch vụ kế nhiệm duy trì runtime; Internet Archive/archivist duy trì archive. [R9–R11]. Commercial viability chưa xác lập; paid hosting sau migration là thị trường khác.

### h. AI: meaningful advantage or not

**C-T2-C12 — HYPOTHESIS.** AI có thể hỗ trợ phát hiện field lạ hoặc dependency code, nhưng cần đo với parser và migration guide chuẩn. Đếm tệp, checksum, schema validation và redirect là việc tất định. Không có bằng chứng AI tái tạo người dùng đang sống, đồng thuận hoặc quyền sở hữu.

### i. Preservation vs restoring functionality

**C-T2-C13 — INFERENCE.** Với blog, archive đọc được có thể đủ. Với dự án Glitch hữu dụng, giữ source không tự giữ app chạy; hành động viết lại/rehost của C3 cho thấy phục hồi chức năng có giá trị đối với ít nhất một chủ app. Với Cohost, đọc lại post khác với giữ cộng đồng và moderation. [R9, R10, R17]. Giá trị bổ sung có thật theo ca, không có tỷ lệ phổ quát.

### j. Resurrection theme fit

**C-T2-C14 — INFERENCE.** Generic export trước shutdown chỉ **theme 1**. Nhánh có **Glitch project hosting đã retired và workflow tạo/chạy app phụ thuộc hosting** làm trung tâm của khả năng được hồi sinh có thể **theme 3/L** dựa thông báo R8; không được tự động nâng lên 4–5 khi chưa có product/demo. Chuyển code tới host khác đơn thuần chưa chứng minh “bring dead technology back to life”. Đây là điều kiện cần kiểm tra sau nghiên cứu, không thiết kế tính năng để cứu theme.

### k. Verdict for this space

**C-T2-C15 — INFERENCE.** **Narrow** về tài sản có chủ hợp pháp, cửa sổ bàn giao và nhu cầu tiếp tục sử dụng rõ; lấy Glitch làm ca kiểm tra cụ thể, không chọn nó làm sản phẩm. Bằng chứng hợp tác C4 mạnh hơn giả định thiếu parser. Bác bỏ nếu export chính thức + dịch vụ nhận đã giữ đủ công việc cần làm hoặc không có người trả/nhận trách nhiệm. Small SaaS thương mại ngoài cộng đồng chưa được chứng minh.

## 4. T3 — Disappearing journals

### a. Problem and root causes

**C-T3-C1 — VERIFIED.** Bản published-version trên arXiv của Laakso/Matthias/Jahn báo cáo **174** OA journals biến mất 2000–2019, theo cách xác định của nghiên cứu. [R21]. P; chưa tái lập dataset. Không dùng con số **176** của bản preprint/bản tin cũ hoặc diễn giải mọi bản bài báo đã tuyệt chủng.

**C-T3-C2 — INFERENCE.** Cây vấn đề: publisher ngừng/đổi ưu tiên hoặc không deposit đủ → chỉ một website chứa bản of record → khi hosting chấm dứt, bài/metadata/supplement mất hoặc khó tìm. Một nhánh khác là scholarship tương tác phụ thuộc runtime retired. [R21–R24, R31]. Prior `C-G-C1` vẫn đúng về logic: “không xác nhận bảo tồn DOI” khác “đã mất”; tỷ lệ 27,64% chưa được kiểm tra lại nên không dùng để suy ra số journal cần cứu. Không cần giữ editorial submission system cũ chỉ để đọc bài; tránh giữ bản trùng khi kho khác đủ và xác thực được.

### b. Stakeholders and target users

| Actor | Job-to-be-done | Hành vi hiện tại | Góp sức/trả tiền | Mức bằng chứng | Evidence |
|---|---|---|---|---|---|
| Editor tạp chí nhỏ | Giữ hồ sơ xuất bản dù ngừng | Gửi ZIP/full text vào JASPER | Công nhập liệu; dịch vụ miễn phí cho nhóm đủ điều kiện | Demonstrated như DOAJ báo cáo, C3 | R22–R23 |
| PKP/CLOCKSS và thư viện | Công bố lại khi trigger | Host OJS hoặc bản journal đã lưu | Tổ chức vận hành; phí chương trình không phải WTP công cụ mới | Demonstrated, C4/C6 | R24–R30 |
| Tác giả/độc giả | Đọc và trích dẫn đúng phiên bản | Chưa có telemetry trực tiếp trong mẫu | WTP chưa rõ | Hypothetical cho công cụ mới | C9 |
| Editor/curator scholarship Flash | Truy cập lại lập luận tương tác | Vectors co-editor mô tả mất khả năng do obsolescence | Công restoration/ngân sách cụ thể chưa tìm thấy | Need documented, demand current unknown, C13 | R31–R33 |

### c. Documented cases by region

**C-T3-C3 — VERIFIED.** DOAJ báo cáo năm 2023 có 32 journal được chọn, 126 ZIP gửi và ca Colombo Business Journal ở Sri Lanka, Fafnir ở Phần Lan, Alphaville ở Ireland. [R23]. Chỉ xác minh “DOAJ báo cáo”, không coi đây là audit độc lập. Những journal này là **phòng ngừa**, không phải đã biến mất; không nhập chúng vào số journal mất.

**C-T3-C4 — VERIFIED.** NA: CLOCKSS nói Archives of Family Medicine của AMA ngừng xuất bản 2000, quyền truy cập tại publisher chấm dứt 2012; họ trigger 9 volumes và nêu các link search/citation/login cũ có thể không dùng được. [R27]. Cơ chế đã tồn tại cho nội dung, không phải runtime editorial.

**C-T3-C5 — VERIFIED.** EU: CLOCKSS công khai Cardiovascular Medicine/EMH Swiss được trigger, và liệt kê các issue/article còn thiếu do publisher không deposit đủ. [R28]. Ví dụ 2019 thiếu 65/71 bài theo bảng của CLOCKSS. Đây là phản chứng cụ thể đối với cách nói vấn đề *chỉ* là đăng ký tham gia; chưa chứng minh lỗi do công cụ, hay supplement luôn bị mất. Mở rộng H3 theo hướng cần kiểm tra completeness; chưa chạy H3.

**C-T3-C6 — VERIFIED.** Asia: CLOCKSS công bố Heterocycles của Japan Institute for Heterocyclic Chemistry được trigger 2024, volumes 1–106. Other: họ cũng công bố Nigerian Journal of Surgical Research được trigger. [R26, R29, R30]. Đây là ca phục hồi truy cập; chưa có nguồn đủ để kết luận các nhà xuất bản này hết tiền. Không đồng nhất quốc gia nội dung và quốc gia máy chủ.

### d. Demand and consequences of inaction

**C-T3-C7 — INFERENCE.** Hành vi gửi nội dung và phục hồi đã chứng minh nhu cầu bảo vệ scholarly record, chưa chứng minh nhu cầu công cụ mới hay thiệt hại định lượng. C5 cho thấy chỉ kiểm tra journal “có Keeper” là chưa đủ để biết giữ đủ bài. C4 cho thấy khôi phục dịch vụ search cũ không nhất thiết cần để tiếp tục đọc/cite. [R23, R27, R28].

### e. Existing solutions and limits

**C-T3-C8 — VERIFIED.** PKP tài liệu hóa dark archive và phục hồi nội dung sang OJS sau trigger; nó không thay backup của site đang vận hành. Trang PKP restored journals đang liệt kê nhiều journal được phục hồi, nên không dựa con số hai journal trong nguồn cũ. [R24, R25]. P + kiểm tra trang restored; chưa kiểm tra toàn bộ bài.

**C-T3-C9 — UNKNOWN.** Chưa xác lập khoảng trống sản phẩm so với **PKP PN, JASPER, CLOCKSS, Portico**. Ba cơ chế đầu đã được đọc tài liệu và ca; Portico có danh sách publisher nhưng chưa đánh giá trọn quy trình/giá. [R22–R30, R44]. WTP mới và mức completeness từng công cụ chưa rõ. Một số journal không đủ điều kiện JASPER hoặc không chạy OJS phù hợp; không đồng nghĩa không có bất kỳ giải pháp nào.

### f. Barriers

**C-T3-C10 — INFERENCE.** Pháp lý: OA vẫn cần kiểm tra license từng thành phần. Tài chính/tổ chức: editor cần thời gian tạo deposit, người chịu trách nhiệm và chủ thể trigger. Kỹ thuật: identifier/version, full-text/supplement, dependency tương tác. [R22, R24, R28, R31]. Bản thiếu ngay từ nguồn không được phép “điền” bằng AI để coi là bài gốc.

### g. Who pays, who maintains

**C-T3-C11 — INFERENCE.** Nhà xuất bản và consortium/thư viện là chủ thể ngân sách khả dĩ; JASPER/PKP có tuyến miễn phí đối với nhóm phù hợp. Maintainer là tổ chức preservation có governance, không phải editor đã giải thể. [R22, R24–R25]. Commercial viability: có đầu tư tổ chức vào preservation, chưa có bằng chứng small journals mua tooling mới; miễn phí hiện có làm WTP yếu hơn, không làm nhu cầu xã hội biến mất.

### h. AI: meaningful advantage or not

**C-T3-C12 — HYPOTHESIS.** AI có thể hỗ trợ OCR/đối chiếu metadata của backfile khó đọc; với PDF/metadata có cấu trúc, manifest/ISSN/DOI check là baseline tốt hơn. AI không cần cho replication, trigger và integrity; không có bằng chứng load-bearing. Với Flash cần bảo toàn semantics và provenance, không chỉ tạo một giao diện “giống”.

### i. Preservation vs restoring functionality

**C-T3-C13 — VERIFIED.** Vectors co-editor Steve F. Anderson mô tả early Vectors dùng Flash và chịu obsolescence/lack of interoperability; Adobe chính thức nêu Flash Player EOL 31/12/2020 và chặn chạy từ 12/1/2021. [R31, R32]. P cho hai tuyên bố, liên hệ nhân quả với tình trạng *hiện tại* của từng essay vẫn là inference vì site USC timeout. Với scholarship có lập luận trong tương tác, PDF/screenshot không giữ hết hành vi; với bài tĩnh, nội dung + metadata + discovery có thể đủ.

### j. Resurrection theme fit

**C-T3-C14 — INFERENCE.** **Generic T3 theme 1/H**, giữ kết luận trượt của Task B. Có góc **C-T3a: scholarly works dựa Flash, như early Vectors**, theme **3/M** vì runtime cụ thể đã chính thức retired và quyết định khôi phục interactivity liên quan trực tiếp tác phẩm. Không nói cả tạp chí nhỏ là công nghệ chết. Ruffle đã thực hiện chính việc chạy Flash; tài liệu compatibility thừa nhận còn sai khác/thiếu API [R33]. Chưa có artifact hợp pháp, kiểm tra baseline hay nhu cầu 2025–2026 cho phần chưa được cứu; không chấm 4–5.

### k. Verdict for this space

**C-T3-C15 — INFERENCE.** **Drop T3 generic khỏi đường ứng viên Resurrection**; vấn đề bảo tồn vẫn có thật và đáng vận hành. Ghi thêm **narrow C-T3a** để cross-review kiểm tra, không chọn sản phẩm. C5 mở một câu hỏi completeness có ích nhưng không tự giải quyết theme. C-T3a phải bị bác bỏ nếu Ruffle/kho phục hồi hiện có đã đáp ứng essay cần đọc, không có tài sản được quyền phục hồi, hoặc curator không cần thêm khả năng tương tác.

## 5. T4 — Heritage archive transfer

### a. Problem and root causes

**C-T4-C1 — VERIFIED.** Mark Turin kể Digital Himalaya dễ xin tài trợ giai đoạn phát triển nhưng khó tìm nguồn duy trì sau khi nội dung đã online; chủ thể phải dựa vào donations và nhân sự mỏng. [R34]. P, không có kiểm toán hay causal comparison.

**C-T4-C2 — INFERENCE.** Cây vấn đề: phụ thuộc một curator/tổ chức và tài trợ dự án → nhân sự/ngữ cảnh/quyền truy cập không có kế nhiệm → tệp còn nhưng cộng đồng không tìm/đọc hợp lệ hoặc không được quản trị. Tài trợ chỉ là một nhánh: chuyển trả quyền điều hành cho cộng đồng nguồn có thể là mục tiêu tích cực. [R34–R37, R40]. Không nên “cứu” bằng công khai hóa tài liệu bị hạn chế, ghi đè tiếng nói cộng đồng, hay sao chép nội dung đã được nơi phù hợp duy trì.

### b. Stakeholders and target users

| Actor | Job-to-be-done | Hành vi hiện tại | Góp sức/trả tiền | Mức bằng chứng | Evidence |
|---|---|---|---|---|---|
| Chủ thể cộng đồng/Tribal Nation | Quyết định ai có thể xem và giải thích tư liệu | Cultural protocols, cộng tác với hub | Thời gian/quản trị; WTP phần mềm riêng chưa rõ | Demonstrated về mô hình đang dùng, C7 | R40–R42 |
| Curator sáng lập Digital Himalaya | Bàn giao để dự án bớt phụ thuộc cá nhân | Chuyển quản lý cho Archive Nepal | Hợp tác và công tổ chức; phí hợp đồng chưa rõ | Demonstrated như tự báo cáo, C3 | R35–R36 |
| Tổ chức archive kế nhiệm | Nhận nội dung và trách nhiệm bền vững | BBAW nhận ELAR; Archive Nepal nhận DH | Grant cho chương trình có thật, C4 | Demonstrated | R35–R38 |
| Fieldworker/di sản người đã mất | Đưa recordings đến custodian phù hợp | PARADISEC yêu cầu deposit và hướng dẫn kế nhiệm | Có thể dự trù tiền chuyển; chưa là giao dịch | Hướng dẫn chính thức, C6 | R39 |

### c. Documented cases by region

**C-T4-C3 — VERIFIED.** Asia/NA: Digital Himalaya chính thức thông báo vào Archive Nepal năm 2024; Turin mô tả bàn giao quản lý ngày 29/5/2024 cho nonprofit có cơ sở New York/Kathmandu. [R35, R36]. Đây là ca quốc tế có người nhận cụ thể, không phải hai ca độc lập. Hai nguồn có quan hệ dự án, nên chỉ xác minh phạm vi lời công bố; chưa audit hợp đồng hay toàn bộ migration.

**C-T4-C4 — VERIFIED.** EU: BBAW và SOAS thông báo ELDP/ELAR chuyển London→Berlin năm 2021; CLARIN-UK xác nhận ELAR hiện ở Berlin. BBAW nêu grant 21 triệu euro/10 năm cho **ELDP programme**, không phải giá công cụ chuyển kho. SOAS nói access rules và website riêng tiếp tục. [R37, R38, R45]. P+I cho nơi lưu trú; nguồn không chứng minh SOAS hết tiền hoặc rights bị mất khi chuyển.

**C-T4-C5 — INFERENCE.** Other: PARADISEC ở Australia cung cấp deposit cho recordings và có dịch vụ cho vùng Pacific; tài liệu flyer được tìm thấy mô tả digitisation tại PNG/Solomon, nhưng PDF không trích được text nên không dùng số grant như xác minh. [R39, R46]. Đây là tương đồng về stewardship, chưa phải ca tổ chức phá sản. NA còn có WiLS hỗ trợ Tribal archives theo grant [R40]. Không cộng một kho toàn cầu thành bằng chứng mọi quốc gia có cùng nhu cầu hoặc payer.

### d. Demand and consequences of inaction

**C-T4-C6 — INFERENCE.** Bàn giao DH và ELAR là demonstrated demand cho continuity; khả năng mất chuyên môn/custody có cơ chế rõ. [R34–R39]. Snippet KeMCo 2025 nói Archive Nepal gặp lượng download và chi phí tăng sau nhận DH, nhưng mở PDF/curl thất bại nên chỉ coi là đầu mối cần kiểm tra [R47]. Chưa dùng số GB hoặc số tiền để kết luận kinh tế. Không có bằng chứng một migration làm mất cultural protocols trong các ca đã đọc, nên H4 vẫn chưa xác nhận.

### e. Existing solutions and limits

**C-T4-C7 — VERIFIED.** Mukurtu tài liệu hóa import communities/cultural protocols và migration Mukurtu 3→4 cho site content; cảnh báo custom theme/module/data structure cần làm lại hoặc hỗ trợ. WiLS nêu Roundtrip giữ metadata/context và cung cấp support/training. [R40–R42]. P, M ở mức đối chiếu trường và quy trình, chưa migration test. Phản bác cách mặc định “công cụ hiện tại không giữ quyền” từ prior `C-G-C15/C20`; chỉ còn giả thuyết về custom cases và verification.

**C-T4-C8 — INFERENCE.** Thay thế mạnh nhất là **Mukurtu + hubs** cho protocol-based stewardship, **PARADISEC/ELAR** cho language records, và bàn giao institutional repository như Digital Himalaya. [R34, R37–R42]. Chưa chứng minh một lớp tooling mới tốt hơn việc cấp tiền, huấn luyện hoặc thỏa thuận custody. PKP/ArchiveTeam không thay thế trực tiếp cơ quan thẩm quyền cộng đồng.

### f. Barriers

**C-T4-C9 — INFERENCE.** Pháp lý/đạo đức: copyright, consent, thẩm quyền truyền thống và access restrictions có thể khác; quyền truy cập không chỉ là giấy phép mở. Tài chính: người nhận có thêm vận hành lâu dài. Kỹ thuật: custom protocols, media và tài khoản; tổ chức: ai quyết định khi các nhóm bất đồng, ai có quyền kế nhiệm curator. [R35–R42]. Pháp lý đánh giá high vì nhiều chủ thể và quyền, không khẳng định một dự án đã vi phạm.

### g. Who pays, who maintains

**C-T4-C10 — VERIFIED.** WiLS công bố hỗ trợ miễn phí nhờ grant đến xuân 2027; nếu không có nguồn tiếp có thể tính phí một số dịch vụ. [R40]. P về tuyên bố tài trợ và điều kiện, không xác minh việc gia hạn. Đây là bằng chứng trả cho năng lực support có kỳ hạn, không chứng minh cộng đồng mua SaaS mới.

**C-T4-C11 — INFERENCE.** Payer có thể là foundation/cơ quan văn hóa/đại học; maintainer phải là custodian được thừa nhận và có nhân lực. [R37–R40]. Commercial viability: có dòng tiền chương trình preservation, nhưng nhãn “có grant” không đảm bảo unit economics sau bàn giao. Tài trợ hạ tầng và quản trị phù hợp hơn giả định mọi cộng đồng tự trả subscription.

### h. AI: meaningful advantage or not

**C-T4-C12 — HYPOTHESIS.** AI có thể giảm công OCR, gợi ý metadata hoặc transcription khi cộng đồng cho phép và có mẫu kiểm tra. Chưa chứng minh lợi thế cho ngôn ngữ ít tài nguyên ở các ca này. AI không nên suy quyền công khai, tự tạo lời người đã mất hoặc xác lập cultural authority; baseline là mapping schema, rule-based ACL tests và curator review. Không có load-bearing AI cho bàn giao.

### i. Preservation vs restoring functionality

**C-T4-C13 — INFERENCE.** Giữ bytes có thể đủ cho kho kín chỉ cần bảo quản; nếu cộng đồng cần tra cứu theo ngôn ngữ/quyền, runtime và ngữ cảnh có giá trị thêm. [R39–R42]. Naga Videodisc là ca lịch sử cụ thể: Digital Himalaya nói vật liệu từng không truy cập được, rồi đã chuyển toàn nội dung sang database XML với retrieval Bamboo [R48]. Việc đã khôi phục là phản chứng chống đề xuất làm lại cùng công việc; chưa test retrieval hiện nay.

### j. Resurrection theme fit

**C-T4-C14 — INFERENCE.** **T4 transfer generic theme 1/H**. Không dùng “ngôn ngữ chết” hay “di sản cũ” để thay “dead technology”. Có tiền lệ Resurrection thật trong **Naga Videodisc**, cùng bằng chứng Pioneer chính thức chấm dứt sản xuất LaserDisc players [R48–R49], nhưng chưa xác minh model/format của chính Naga trùng các model đó, và quan trọng hơn dự án nói đã khôi phục. Không thấy một nhánh T4 còn nhu cầu phục hồi công nghệ cụ thể đủ rõ để nâng T4 qua gate. Mukurtu migration hiện có cũng không tự có nghĩa hồi sinh công nghệ retired.

### k. Verdict for this space

**C-T4-C15 — INFERENCE.** **Drop khỏi đường ứng viên Resurrection ở phạm vi hiện tại**; tiếp tục coi đây là vấn đề stewardship đáng nghiên cứu ngoài cuộc thi. C3/C4 xác nhận bàn giao khả thi; C7/C8 làm yếu giả định thiếu nền tảng; C14 chưa cho unmet resurrection job. Bác bỏ khoảng trống tooling nếu migration chính thức giữ đủ semantics trên ca được quyền dùng và phần còn lại chỉ là funding/governance. Không thiết kế thêm chức năng để cứu điểm theme.

## 6. Cross-space analysis

**C-G-C1 — INFERENCE.** Có cơ chế chung hẹp: **giá trị sử dụng còn tồn tại lâu hơn cam kết của custodian hiện tại**, rồi phải chọn giá trị nào chuyển cho ai cùng nguồn lực nào. Araport, Cohost, journal trigger và DH đều có bước chuyển trách nhiệm. [R1, R10–R11, R24–R28, R35–R38]. Đây là lớp phân tích BA; không đủ để kết luận một thị trường hoặc sản phẩm chung.

**C-G-C2 — INFERENCE.** Bằng chứng chống nguyên nhân chung “tổ chức không đủ nguồn lực”: Glitch nêu cả thay thế tốt hơn; ELAR chuyển với grant mới, không có bằng chứng insolvency; DH muốn bớt phụ thuộc cá nhân và trả quyền điều hành về vùng nguồn; journal có thể ngừng xuất bản nhưng vẫn đủ nội dung trong Keeper. [R8, R27, R35–R38]. Nguồn lực gồm người/quyền/chính danh, không chỉ hosting bill.

**C-G-C3 — INFERENCE.** Những chỗ gộp sẽ sai:

| Chiều quyết định | S2 | T2 | T3 | T4 |
|---|---|---|---|---|
| Công việc cần giữ | Truy vấn/tính toán và tính đúng khoa học | Tài sản người dùng, có thể runtime | Hồ sơ of record, discovery | Custody/context và truy cập được phép |
| Ai chấp nhận thành công | Nhà khoa học/chủ thể kế nhiệm | Chủ tài sản và dịch vụ nhận | Publisher/library/preservation body | Cộng đồng và custodian được công nhận |
| Có thể chỉ giữ snapshot? | Tùy app; Araport chọn chức năng | Đủ cho một số nội dung | Thường đủ cho bài tĩnh với metadata | Có thể; phải giữ restrictions/context |
| Chu kỳ quyết định | Grant/bàn giao khoa học | Deadline ngắn và nhiều user | Deposit sớm, trigger muộn | Đàm phán dài và quyền nhiều lớp |

Nguồn cho bảng: [R1, R8–R11, R24, R27–R28, R35–R42]. Các giao thức, người mua và tiêu chí kiểm thử khác nhau; reuse khả năng checksum/export không chứng minh reuse sản phẩm.

**C-G-C4 — UNKNOWN.** Chưa có bằng chứng người mua chung, ngân sách chung hoặc một loại thất bại parser gây phần lớn tổn thất ở cả bốn. H0 Task B về “mua công cụ bảo tồn” chưa được xác nhận. Cũng không được kết luận **không có thị trường** chỉ vì lượt desk research chưa tìm được giao dịch.

**C-G-C5 — INFERENCE.** Preservation có chọn lọc là yêu cầu thực tế: Araport chọn chức năng; chủ Glitch bỏ dự án ít dùng; PARADISEC yêu cầu giảm bản trùng và tôn trọng restrictions. [R1, R9, R39]. Điều này hỗ trợ prior `C-G-C4` bằng cơ chế/ca mới. “Cứu mọi thứ” có thể tăng nghĩa vụ mà không giữ thêm giá trị.

## 7. Challenges to the human's framing

**C-G-C6 — INFERENCE.** Câu hỏi umbrella đúng như câu hỏi điều tra nhưng quá rộng như kết luận kinh doanh. Bốn sửa đổi cần giữ khi đọc kết quả:

- “Sắp biến mất” không đồng nghĩa “chưa có bản thay thế”, như T3 đã có restored journals và T4 đã có Naga online [R25, R48].
- “Không đủ nguồn lực” không chứng minh “cần công cụ mới”; TAIR/KEGG, Mukurtu hubs và ELAR cho thấy finance, curation và governance có thể quyết định [R2–R3, R37–R42].
- Hồi sinh chức năng và chuyển nội dung là hai job khác; theme không được suy ra từ sự đáng quý của nội dung [R7, R27, R31–R32].
- Nhu cầu có bằng chứng lịch sử quốc tế nhưng demand 5 cần hành vi đúng target trong 2025–2026. Không chuyển lượng đọc toàn cầu thành payer toàn cầu; không chuyển funder giàu của ELDP thành khả năng trả tiền của community archive nhỏ.

Không xếp hạng bốn không gian và không so với các Phase 2 leaders. Điểm JSON là tóm tắt bằng chứng thận trọng cho phạm vi ghi trong từng entry, không dự đoán giải thưởng.

## 8. Unresolved questions

Các câu hỏi sau là thiếu dữ kiện, chưa phải kế hoạch triển khai hay thí nghiệm đã được duyệt:

| Không gian | Câu hỏi quyết định | Điều kiện khiến hướng phải dừng | Trạng thái |
|---|---|---|---|
| S2 | App nào còn người dùng nhưng không có nơi nhận, có quyền và công nghệ retired cụ thể? | Nhu cầu được host hiện tại/nhóm kế nhiệm đáp ứng hoặc không ai cần runtime | UNKNOWN, C-S2-C5/C14 |
| T2 | Small operator/user nào thực sự mua hỗ trợ exit; export làm mất đúng công việc nào? | Official export + host mới đủ, không có payer/maintainer | UNKNOWN, C-T2-C11 |
| T3 | Backfile thiếu do không gửi, lỗi đóng gói hay bản chưa bao giờ được lưu? | Tool hiện có đã kiểm tra đầy đủ, chỉ thiếu thực thi | UNKNOWN, C-T3-C5/C9 |
| T3a | Essay Flash cụ thể còn hỏng sau Ruffle và có curator muốn phục hồi? | Đã chạy đủ, không có quyền/artifact, hoặc không còn nhu cầu tương tác | UNKNOWN, C-T3-C13/C14 |
| T4 | Migration custom nào thật sự mất access semantics; ai có thẩm quyền xác nhận? | Mukurtu/Roundtrip giữ đủ, thiếu hụt chỉ là tiền/quản trị | UNKNOWN, C-T4-C7 |
| Tất cả | Giá trị nào có thể ngừng phục vụ, ai có quyền quyết định, ai gánh vận hành? | Không có chủ thể nhận hợp lệ hoặc chi phí không được cam kết | UNKNOWN, C-G-C4 |

Handoff: cross-review nên kiểm tra các claim nguồn đơn trước, đặc biệt scope theme của Glitch/Flash và việc “đã có tool” có thật sự loại nhu cầu. Không ép đồng thuận. Runtime security vẫn chỉ là prompt-only isolation trong process unsandboxed, chưa là bảo đảm kỹ thuật; coordinator cần audit phạm vi thay đổi. Không có sự cố lộ dữ liệu được quan sát. Giảm lỗi harness: lưu snapshot source có ngày, phân biệt source requested/usable, và cấp evidence ledger có claim→source→pipeline để tránh coi snippet như direct open.

## 9. References

Mọi ngày truy cập: **2026-11-25 UTC**. `direct` nghĩa là đọc được nội dung, không chỉ gửi request. Điểm theo thứ tự **A/T/M/C/F/R/B** = Authority/Technical Evidence/Mechanism/Context/Freshness/Reproducibility/Bias, 0–5; weighted = 20A/5+20T/5+20M/5+15C/5+10F/5+10R/5+5B/5. Reliability và Relevance là đánh giá riêng cho claim ghi trong hàng; nguồn chính chủ rất đáng tin về tuyên bố tính năng nhưng chỉ liên quan vừa phải đến WTP/nhu cầu thị trường. Không dùng điểm reference để tính điểm candidate.

| Ref ID | URL | Title | Publisher | Pub date | Accessed | Opened directly or snippet | Claims | 7 scores A/T/M/C/F/R/B | Weighted /100 | Source Reliability | Reference Relevance |
|---|---|---|---|---|---|---|---|---|---|---|---|
| R1 | [R1](https://academic.oup.com/plcell/article/32/9/2683/6115718) | Araport Lives | Pasha et al., The Plant Cell | 2020-07-22 | 2026-11-25 UTC | direct | C-S2-C1/C2/C3/C7/C9/C10/C13; C-G-C1/C3/C5 | 5/4/5/5/2/3/3 | 84 | H cho lời nhóm thực hiện; chưa audit | H chức năng/bàn giao; L thị trường |
| R2 | [R2](https://phoenixbioinformatics.atlassian.net/wiki/spaces/COM/pages/42216453) | TAIR Funding | Phoenix Bioinformatics | 2024-04-04 | 2026-11-25 UTC | direct | C-S2-C2/C3/C7/C10/C11; C-G-C6 | 5/3/4/5/3/3/3 | 78 | H tuyên bố chính chủ | H funding; L công cụ mới |
| R3 | [R3](https://www.genome.jp/kegg/docs/plea.html) | Plea to Support KEGG | Minoru Kanehisa / KEGG | 2011-05-16; cập nhật 2022-04-01 | 2026-11-25 UTC | direct | C-S2-C2/C6/C11; C-G-C6 | 5/3/4/5/2/3/3 | 76 | H lời người vận hành; chưa audit | H finance/curation |
| R4 | [R4](https://www.kanehisa.jp/npo/docs/subscription_fees.pdf) | KEGG FTP subscription fees | NPO Bioinformatics Japan | hiệu lực 2011/2019 | 2026-11-25 UTC | direct | C-S2-C6 | 5/3/3/4/1/4/3 | 69 | H giá lịch sử | M; không phải giá hiện hành |
| R5 | [R5](https://hds.essex.ac.uk/history/about/more.php) | History Data Service: History | University of Essex | không ghi; lịch sử 2008 | 2026-11-25 UTC | direct | C-S2-C4 | 5/3/4/5/1/3/4 | 75 | H tổ chức nhận | H transfer; M app |
| R6 | [R6](https://www.dcc.ac.uk/news/arts-and-humanities-data-service-decision) | Arts and Humanities Data Service decision | Chris Rusbridge / DCC | 2007-06-06 | 2026-11-25 UTC | direct | C-S2-C4 | 4/3/4/5/1/3/3 | 70 | M-H; ý kiến đương thời, có quan hệ DCC/AHDS | H quyết định rút tiền; L hiện trạng 2026 |
| R7 | [R7](https://about.zenodo.org/policies/) | General Policies v1.0 | CERN / Zenodo | không ghi | 2026-11-25 UTC | direct | C-S2-C8/C9/C10; C-G-C6 | 5/4/5/5/3/4/4 | 89 | H cam kết chính thức | H giới hạn functional preservation |
| R8 | [R8](https://blog.glitch.com/post/changes-are-coming-to-glitch) | Important Changes are Coming to Glitch | Anil Dash / Glitch | 2025-05-22 | 2026-11-25 UTC | direct | C-T2-C1/C2/C9/C10/C14; C-G-C2/C3 | 5/4/5/5/4/4/2 | 89 | H lịch shutdown; M nguyên nhân tự báo cáo | H retirement; L small-SaaS WTP |
| R9 | [R9](https://martymcgui.re/2025/06/07/glitched-out/) | Glitched out | Marty McGuire | 2025-06-07 | 2026-11-25 UTC | direct | C-T2-C3/C7/C11/C13; C-G-C5 | 3/4/4/5/4/4/4 | 79 | M-H hành vi chính tác giả | H user work; L đại diện thị trường |
| R10 | [R10](https://wiki.archiveteam.org/index.php/Cohost) | Cohost | ArchiveTeam | log 2024-2025; không ghi ngày bản hiện tại | 2026-11-25 UTC | direct | C-T2-C2/C4/C7/C10/C11/C13; C-G-C1/C3 | 4/5/5/5/4/4/3 | 90 | H log tham gia; thiếu audit đầy đủ | H rescue cooperation |
| R11 | [R11](https://bsky.app/profile/staff.cohost.org/post/3lfhto6542k2q) | Final shutdown announcement | Cohost staff | 2025-01-11 | 2026-11-25 UTC | direct | C-T2-C4/C7/C11; C-G-C1/C3 | 5/3/4/5/4/4/3 | 82 | H lời operator | H xác nhận phối hợp; L completeness |
| R12 | [R12](https://wiki.archiveteam.org/index.php/Soup.io) | Soup.io | ArchiveTeam | không ghi; ca 2020 | 2026-11-25 UTC | direct | C-T2-C2/C5/C7 | 4/4/4/4/1/3/3 | 71 | H rescue tự báo cáo; M thông báo được dẫn lại | H cửa sổ/giới hạn rescue |
| R13 | [R13](https://www.presseportal.de/pm/118109/4061757) | Österreichisches Microblogging Portal Soup.io steht zum Verkauf | easyname GmbH / Presseportal | 2018-09-14 | 2026-11-25 UTC | direct | C-T2-C5/C7 | 5/3/4/5/1/3/2 | 73 | H lời chủ sở hữu; không kiểm toán | H succession; L shutdown 2020 cause |
| R14 | [R14](https://www.gmo.media/teacup/) | teacup. byGMO サービス終了のお知らせ | GMO Media | 2022-08-01 | 2026-11-25 UTC | direct | C-T2-C6 | 5/2/3/4/2/4/4 | 68 | H retirement notice | H kết thúc; L nguyên nhân/quy mô nhỏ |
| R16 | [R16](https://sonnet.hatenablog.com/entry/acd5ecc226b4ea1eade440a6b5929151) | 彷徨うブログ | element6 / 言の葉 | 2025-09-28 | 2026-11-25 UTC | direct | C-T2-C6 | 3/3/4/5/4/3/4 | 73 | M lời kể người dùng | H migration cá nhân; L WTP |
| R17 | [R17](https://docs.joinmastodon.org/user/moving/) | Moving or leaving accounts | Mastodon | 2025-11-27 theo trang | 2026-11-25 UTC | direct | C-T2-C8/C9/C10/C13 | 5/4/5/5/5/4/4 | 93 | H tài liệu chính thức; chưa chạy | H alternative và giới hạn import |
| R18 | [R18](https://github.com/dtinit/data-transfer-project) | Data Transfer Project README | Data Transfer Initiative | không ghi | 2026-11-25 UTC | direct | C-T2-C8/C9 | 5/4/4/4/3/4/3 | 81 | H mục tiêu framework; README có thể chậm cập nhật | M-H; không hứa hỗ trợ mọi service |
| R19 | [R19](https://webrecorder.net/browsertrix/) | Browsertrix | Webrecorder | không ghi | 2026-11-25 UTC | direct | C-S2-C9; C-T2-C9 | 5/4/5/5/4/4/2 | 89 | H capability công bố; chưa test | H alternative; L gap/WTP |
| R20 | [R20](https://docs.browsertrix.com/user-guide/workflow-setup/) | Crawl Workflow Settings | Webrecorder | không ghi | 2026-11-25 UTC | direct | C-T2-C10 | 5/5/5/5/4/4/4 | 95 | H cấu hình chính thức | H privacy/crawl mechanism |
| R21 | [R21](https://arxiv.org/abs/2008.11933) | Open is not forever: a study of vanished open access journals, v4 | Laakso, Matthias, Jahn | 2021-02-22 v4 | 2026-11-25 UTC | direct | C-T3-C1/C2 | 5/4/4/5/2/4/4 | 83 | H published study; chưa tái lập | H vấn đề lịch sử; M hiện trạng |
| R22 | [R22](https://doaj.org/preservation/) | JASPER preservation service | DOAJ | không ghi | 2026-11-25 UTC | direct | C-T3-C2/C9/C10/C11 | 5/4/5/5/4/4/3 | 90 | H eligibility/route chính thức | H alternative; L willingness to buy |
| R23 | [R23](https://blog.doaj.org/2023/12/06/jasper-a-cross-industry-collaboration-making-a-real-difference/) | JASPER: a cross-industry collaboration making a real difference! | DOAJ | 2023-12-06; trang ghi sửa 2025-08-22 | 2026-11-25 UTC | direct | C-T3-C3/C7 | 5/4/4/5/2/3/2 | 79 | H tổ chức tự báo cáo; chưa độc lập | H hành vi editor; M demand hiện tại |
| R24 | [R24](https://github.com/pkp/pkp-docs/blob/main/pkp-pn/en/index.md) | PKP Preservation Network documentation | Public Knowledge Project | không ghi | 2026-11-25 UTC | direct | C-T3-C2/C8/C9/C10/C11; C-G-C1/C3 | 5/5/5/5/4/4/4 | 95 | H source documentation; fallback Anubis | H alternative/trigger vs backup |
| R25 | [R25](https://ojs-preservation.publicknowledgeproject.org/) | PKP Preservation Network: Restored Journals | Public Knowledge Project | không ghi | 2026-11-25 UTC | direct | C-T3-C8/C11; C-G-C6 | 5/4/4/5/5/4/3 | 88 | H trang observed; chưa kiểm đủ articles | H phục hồi đã tồn tại |
| R26 | [R26](https://clockss.org/triggered-content/) | Triggered Journals | CLOCKSS | danh sách có mốc 2026 | 2026-11-25 UTC | direct | C-T3-C6 | 5/4/4/5/5/4/3 | 88 | H trigger list | H journal cases; L cause funding |
| R27 | [R27](https://clockss.org/triggered-content/archives-of-family-medicine/) | Archives of Family Medicine | CLOCKSS | trigger 2012; không ghi ngày trang | 2026-11-25 UTC | direct | C-T3-C4/C7/C9; C-G-C1/C2/C3/C6 | 5/5/5/5/2/4/3 | 90 | H quy trình và giới hạn được công bố | H preservation/restoration distinction |
| R28 | [R28](https://clockss.org/triggered-content/cardiovascular-medicine/) | Cardiovascular Medicine | CLOCKSS | trigger 2025; không ghi ngày trang | 2026-11-25 UTC | direct | C-T3-C5/C7/C9/C10; C-G-C1/C3 | 5/5/5/5/4/5/4 | 97 | H manifest thiếu tự công bố; chưa diff nguồn | H counterexample completeness |
| R29 | [R29](https://clockss.org/triggered-content/heterocycles/) | Heterocycles | CLOCKSS | trigger 2024 | 2026-11-25 UTC | direct | C-T3-C6/C9 | 5/4/4/5/3/4/3 | 84 | H tuyên bố trigger | H Asia case; L failure cause |
| R30 | [R30](https://clockss.org/triggered-content/nigerian-journal-of-surgical-research/) | Nigerian Journal of Surgical Research | CLOCKSS | trigger 2020 | 2026-11-25 UTC | direct | C-T3-C6/C9 | 5/4/4/5/2/4/3 | 82 | H tuyên bố trigger | H Other case; L failure cause |
| R31 | [R31](https://www.thecine-files.com/videographic-scholarship-and-as-digital-humanities/) | videographic scholarship and/as digital humanities | Steve F. Anderson / The Cine-Files 15 | fall 2020 | 2026-11-25 UTC | direct | C-T3-C2/C10/C13/C14; C-G-C6 | 5/4/4/5/2/3/3 | 80 | H co-editor testimony; có lợi ích gắn dự án | H Flash/Vectors mechanism; L current demand |
| R32 | [R32](https://www.adobe.com/products/flashplayer/end-of-life-alternative.html) | Flash Player EOL General Information | Adobe | FAQ updated 2021-01-13 | 2026-11-25 UTC | direct | C-T3-C13/C14; C-G-C6 | 5/4/5/5/2/4/4 | 87 | H retirement dates trong FAQ | H theme; L customer demand |
| R33 | [R33](https://ruffle.rs/compatibility) | ActionScript Compatibility | Ruffle | không ghi | 2026-11-25 UTC | direct | C-T3-C14/C15 | 5/5/5/5/5/4/3 | 96 | H implementation scope tự báo cáo | H strongest baseline; không chứng minh essay chạy |
| R34 | [R34](https://handbook.pubpub.org/pub/case-digital-himalaya/release/2) | The Digital Himalaya Project: Collection, Protection & Connection | Mark Turin / Digital Project Handbook | 2021-02-14; release 2021-02-18 | 2026-11-25 UTC | direct | C-T4-C1/C2/C6/C8 | 5/4/5/5/2/3/3 | 84 | H founder account; chưa audit | H maintenance funding/succession |
| R35 | [R35](https://www.digitalhimalaya.com/index.php) | Digital Himalaya: Home | Digital Himalaya / Archive Nepal | news 2024-04 | 2026-11-25 UTC | direct | C-T4-C2/C3/C6/C9; C-G-C1/C2/C3 | 5/4/5/5/3/4/3 | 88 | H official announcement | H transfer; L current tooling gap |
| R36 | [R36](https://nepalitimes.com/a-homecoming-for-digital-himalaya) | A homecoming for Digital Himalaya | Mark Turin / Nepali Times | 2024-10-15 | 2026-11-25 UTC | direct | C-T4-C2/C3/C6/C9; C-G-C2/C3 | 5/4/5/5/3/3/3 | 86 | H direct participant; không independent với R34 | H succession motives |
| R37 | [R37](https://www.bbaw.de/files-bbaw/presse/pressemitteilungen/pressemitteilungen-2021/PM-18_Dokumentation_bedrohter_Sprachen_englisch/BBAW_PM_ELDP_engl.pdf) | New Berlin Center for the Documentation of Endangered Languages | BBAW | 2021-07-19 | 2026-11-25 UTC | direct | C-T4-C2/C4/C6/C8/C11; C-G-C1/C2/C3/C6 | 5/4/5/5/2/4/3 | 86 | H host/grant announcement | H transfer; L insolvency/new-tool WTP |
| R38 | [R38](https://www.soas.ac.uk/about/news/soas-marks-eldp-move-new-base-berlin) | SOAS marks ELDP move to new base in Berlin | SOAS | 2021 theo sự kiện; không ghi ngày trong trích đoạn | 2026-11-25 UTC | direct | C-T4-C4/C6/C8/C9/C11; C-G-C1/C2/C3/C6 | 5/4/5/5/2/4/3 | 86 | H old-host terms | H access continuity; L source of financial distress |
| R39 | [R39](https://www.paradisec.org.au/deposit/) | Depositing material with PARADISEC | PARADISEC | không ghi | 2026-11-25 UTC | direct | C-T4-C5/C6/C8/C9/C11/C13; C-G-C5 | 5/5/5/5/4/4/4 | 95 | H deposit/access policy | H governance and maintenance; M organizational failure |
| R40 | [R40](https://wils.org/do/digital-projects/mukurtu/) | Mukurtu Midwest | WiLS | không ghi; grant đến spring 2027 | 2026-11-25 UTC | direct | C-T4-C2/C5/C7/C8/C9/C10/C11/C13; C-G-C3/C6 | 5/4/5/5/5/4/3 | 92 | H provider terms; chưa funding audit | H support/current counterevidence |
| R41 | [R41](https://docs.mukurtu.org/roundtrip/ImportingCommunitiesAndCulturalProtocols/) | Importing Communities and Cultural Protocols | Mukurtu / WSU | không ghi | 2026-11-25 UTC | direct | C-T4-C7/C8/C9/C13; C-G-C3/C6 | 5/5/5/5/5/4/4 | 97 | H official docs; chưa test | H rights semantics counterevidence |
| R42 | [R42](https://docs.mukurtu.org/migration/) | Migration Overview | Mukurtu / WSU | không ghi | 2026-11-25 UTC | direct | C-T4-C7/C8/C9/C13/C14; C-G-C3/C6 | 5/5/5/5/5/4/4 | 97 | H official docs; custom caveat | H existing migration vs new product |
| R43 | [R43](https://doi.org/10.1093/genetics/iyaf248) | Recent major changes to TAIR | TAIR authors / GENETICS | 2026 theo search metadata | 2026-11-25 UTC | snippet only | C-S2-C7 | 5/3/3/5/5/1/3 | 74 | M vì chưa đọc toàn văn | M current demand; L new-tool WTP |
| R44 | [R44](https://www.portico.org/coverage/publishers/) | Publishers | Portico | không ghi | 2026-11-25 UTC | direct | C-T3-C9 | 5/3/3/4/5/4/3 | 77 | H participation list | M alternative; chưa kiểm hết workflow/fees |
| R45 | [R45](https://www.clarin.ac.uk/endangered-languages-archive) | Endangered Languages Archive | CLARIN-UK | không ghi | 2026-11-25 UTC | direct | C-T4-C4 | 4/3/4/5/4/4/4 | 79 | H consortium confirms location | H confirmation Berlin; L cause/finance |
| R46 | [R46](https://www.paradisec.org.au/wp-content/uploads/2020/10/Paradisec_Flyer_Final.pdf) | PARADISEC: What we have done | PARADISEC | 2020 path; ca 2019 | 2026-11-25 UTC | snippet only | C-T4-C5 | 5/3/3/4/1/1/3 | 63 | M; PDF opened nhưng không đọc được text | M Other analog; L digital transfer |
| R47 | [R47](https://kemco.keio.ac.jp/wp/wp-content/uploads/2025/04/46c09d7d0b88494aa7d70b059533cd45.pdf) | Walking A Digital Humanities Project Home, or Landing Digital Himalaya | Mark Turin / The KeMCo Review 03 | 2025 | 2026-11-25 UTC | snippet only | C-T4-C6 | 5/4/4/5/4/1/3 | 80 | M; web 502 và TLS fallback thất bại | H hậu chuyển giao finance; chưa kiểm số liệu |
| R48 | [R48](https://www.digitalhimalaya.com/collections/naga/) | Naga Videodisc | Digital Himalaya | không ghi | 2026-11-25 UTC | direct | C-T4-C13/C14/C15; C-G-C6 | 5/4/5/5/2/4/3 | 86 | H official restoration account; chưa test | H historical resurrection/counterevidence |
| R49 | [R49](https://jpn.pioneer/ja/corp/news/press/index/422/rel=_2012_6) | レーザーディスクプレーヤー生産終了のお知らせ | Pioneer | 2009-01-14 | 2026-11-25 UTC | direct | C-T4-C14 | 5/4/5/5/1/4/4 | 85 | H manufacturer retirement notice | M carrier EOL; L exact Naga implementation |
