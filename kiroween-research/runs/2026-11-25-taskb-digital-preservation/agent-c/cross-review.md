# Task B Round 2 — Agent C

## Metadata

- Run `2026-11-25-taskb-digital-preservation`; model/effort thực tế: **not observable / not observable**; không nâng effort, không helper worker.
- Round 2 bắt đầu khoảng 12:42 UTC, 2026-11-25; mốc đồng hồ đầu được ghi trực tiếp là 12:44:56Z; hoàn tất biên soạn 12:51:06Z, sau đó kiểm tra hợp đồng tệp và hash bản đóng băng. Tổng thời gian khoảng 9 phút; thời điểm bắt đầu chỉ là ước lượng, không phải telemetry.
- Đọc report và opportunities của A/B theo quyền mới; Round 1 của C là bản đóng băng. Chỉ ghi trong agent-c/; không cập nhật progress chung, không commit, không chạy mã cộng đồng.
- **19 challenge có mã: 10 cho A, 9 cho B.** Đề nghị nhãn của peer là khuyến nghị để coordinator xét, không sửa hồ sơ của họ. Tự kiểm cả 6 VERIFIED của C: **đổi 1 nhãn**, giữ 5 với phạm vi diễn đạt rõ hơn. Cả 3 opportunity được revised, không withdrawn; đề nghị merge ở mức bản đồ, không ép các JTBD khác nhau thành một sản phẩm.
- 17 nguồn mới được dùng trong báo cáo đều mở trực tiếp có nội dung; không sử dụng nguồn snippet mới để xác nhận VERIFIED. Có 9 lần không lấy được nội dung dự định: PubMed 28334982 (429), Homecoming announcement (403), PubMed 29228189 dạng pubmed, Oxford NAR và hai NCBI efetch URL không truy cập được qua web tool; EC presscorner trả 0 dòng; lần find tiếp theo trên bài donation N10 trả 403 và trên PDF N17 timeout, dù lần mở đầu của hai nguồn đã có nội dung. Các nguồn Round 1 vẫn được viện dẫn bằng `C:Rxx`, `A:Rxx`, `B:Rxx` để tránh trùng số.
- Không làm reproduction decompilation, không thử boot/gameplay, không lấy collection có dữ liệu cá nhân. Bài blog, repo cùng tác giả, trang EC cùng cơ quan và hai bên cùng cuộc chuyển giao không tự tạo xác nhận độc lập cho tất cả kết luận.

## 1. Challenges to Agent A

### C-R2-A01 — VERIFIED bao phủ suy luận nhân quả và nhiều mệnh đề không được đối chứng

**Đích:** A-G-C1/C2/C3/C5/C7/C8/C10/C11/C12/C13 và các claim opportunity dựa trên chúng. **INFERENCE của reviewer:** “mở nguồn thấy có viết” không đủ theo brief §3. A-G-C1 dựa Wikipedia + snippet; A-G-C13 nói “phần lớn dự án bảo tồn thất bại” nhưng không có mẫu thất bại hoặc tỷ lệ nguyên nhân. A-G-C7 còn gộp số Software Heritage chỉ thấy snippet với đánh giá giá trị/chi phí. Không thể giữ toàn bộ claim là VERIFIED chỉ vì một phần có nguồn. Đề nghị tách fact hẹp khỏi interpretation và hạ nhãn tổng hợp xuống INFERENCE; nhận định thống kê không có mẫu cần UNKNOWN. Bằng chứng trực tiếp mới là Endings vẫn đòi validation/rebuild/release management (N01), và Archive-It là dịch vụ có subscription (N07/N08), phản bác diễn giải vận hành tự biến mất. Đây là vấn đề kỷ luật bằng chứng, không tuyên bố các fact còn lại sai.

### C-R2-A02 — Tỷ lệ sống/citation không xác định nguyên nhân đóng hoặc giá trị bằng không

**Đích:** A-G-C2, A-G-C3, A-O1-C1/C2, A-O1.demand/international. **INFERENCE:** A:R05 chỉ là đo availability; không chứng minh hết grant gây tất cả phần suy giảm. A:R06 cho thấy tương quan citation–relocation, chưa chứng minh tài nguyên ít citation “thực sự không còn được sử dụng”. Citation có thể chậm, thiên lệch ngành/ngôn ngữ hoặc không đo việc dạy học. N03 cho thấy ca Stanford được chọn còn vì giá trị giảng dạy và lưu trữ, không vì citation count. Đề nghị INFERENCE cho causal interpretation, giữ số liệu dưới dạng “nghiên cứu báo cáo”; demand 4/H không có hành vi hiện tại của target user tương ứng, international 5/H không được suy từ tạp chí quốc tế sang actor độc lập ở ba vùng. Chưa tái kiểm số trong A:R05/R06 do lỗi truy cập; không đưa ra số thay thế.

### C-R2-A03 — Endings giảm phụ thuộc, không chứng minh zero-cost hoặc staticization là đường duy nhất

**Đích:** A-O1-C3; A §6 “cách duy nhất”, “không tốn phí vận hành”. **INFERENCE:** N01 yêu cầu staff maintain processing code, kiểm dữ liệu, rebuild và release management; còn cho phép search server bổ sung. Nội dung tĩnh vẫn cần chủ thể giữ bản sao/cung cấp truy cập; chính R1 của C có PARADISEC grant và IPFS pinning (C-G-C10/C13). Đề nghị rút mệnh đề zero-cost/duy nhất, không chỉ đổi nhãn. Tách “không cần application server động để đọc sản phẩm cơ bản” khỏi “không còn chi phí hay trách nhiệm”. N01 ghi version 2.2.1 ngày 2023-03-03, footer revision 2025-01-03: A:R09 nên phân biệt ngày version và ngày sửa trang.

### C-R2-A04 — Không import vào Mastodon không đồng nghĩa không có viewer hậu xuất

**Đích:** A-O2-C2/C3, A §5 portability, innovation 4. **INFERENCE:** tài liệu Mastodon mở trực tiếp N02 xác nhận chưa import posts/media nhưng nói rõ archive có thể xem bằng phần mềm hiểu Activity Streams. N16, repo chính thức của MARL, mô tả viewer offline cho posts/media và nhiều archive, đồng thời công bố hạn chế về dữ liệu bên ngoài. Chưa chạy MARL, nên chỉ xác nhận lựa chọn đã được công bố, không hứa mọi export chạy hoàn hảo. Đề nghị bỏ claim “không có công cụ” và đánh giá lại khác biệt với viewer/migration/reconstruction thành ba jobs riêng. MARL không giải quyết remote post đã thiếu hoặc import vào server mới; phản chứng này làm hẹp gap, không xóa mọi gap.

### C-R2-A05 — Referential integrity không phải oracle đủ cho ngữ nghĩa hay tính cần thiết của AI

**Đích:** A-O2.ai_role load-bearing, ai 4/M, A §7. **INFERENCE:** script theo Activity Streams và mapping schema có thể duyệt/đổi dữ liệu còn trong export (N02/N16). Khóa ngoại hợp lệ vẫn có thể nối nhầm người, thread, thời gian hoặc quyền; dữ liệu không được export không thể được xác nhận bằng việc AI tạo quan hệ hợp lệ. N13 nhấn mạnh software, standards, schemas và trust, không cung cấp benchmark lợi ích AI vượt ETL. Đề nghị **useful hoặc unnecessary theo phạm vi**, còn load-bearing là HYPOTHESIS; cần mẫu có ground truth và so với deterministic parser + mapping thủ công, tính cả phút review. AI không được lấp khoảng trống lịch sử bằng quan hệ tưởng tượng.

### C-R2-A06 — Một ca emulation năm 2021 không chứng minh khoảng trống hiện tại, hoặc AI thắng preset/catalog

**Đích:** A-O3-C1, A-O3 innovation 4 và load-bearing. **INFERENCE:** N03 thực sự ghi hai ngày, nhưng môi trường dùng cuối cùng **đã có ở Yale**, chưa publish để Stanford dùng; nguồn mô tả một archivist phối hợp preservation analyst, không chứng minh cả hai làm trọn hai ngày liên tục. Đây có thể là discovery/sharing, không nhất thiết suy OS bằng AI. N17 ghi templates, metadata và reuse trong EaaS/EaaSI từ 2020; C:R29 cũng mô tả versioned environments. Đề nghị INFERENCE cho chi phí tổng quát, hạ assertion “không có công cụ end-to-end” xuống UNKNOWN nếu chưa khảo sát hiện tại; AI useful giả định. Baseline phải gồm reuse catalog, header identification và bounded boot search, không chỉ cấu hình tay từ đầu; boot được chưa xác nhận logic ứng dụng đúng.

### C-R2-A07 — Giới hạn remote videogames không phải lệnh cấm remote mọi software

**Đích:** A-O3-C3 và A §5/§8 emulation. **INFERENCE với mệnh đề pháp lý hẹp từ nguồn sơ cấp:** Final Rule mở trực tiếp N11 phân biệt (b)(19) videogames và (b)(20) computer programs **except video games**; nhóm sau có remote access theo điều kiện. Vì vậy câu §5 “cấm … game/phần mềm” quá rộng; sự từ chối mở rộng cho game không đủ bác bỏ ROI của môi trường phần mềm học thuật. N12 là xác nhận độc lập về đối tượng game của quyết định 2024. Không coi exemption là license copyright tổng quát hoặc clearance hiện hành cho mọi artefact; không rà mọi sửa đổi sau 2024. Đề nghị thu hẹp A-O3-C3 và tách đánh giá game khỏi non-game software.

### C-R2-A08 — Chữ ký, repo và sự kiện ba vùng không đạt demand 5 hoặc international 5 cho nhà phát hành

**Đích:** A-G-C5, A-O4-C1/C2/C3 và A-O4.demand/international. **INFERENCE:** C-G-C19 VERIFIED chỉ xác nhận số chữ ký được công bố; người ký không phải studio được hỏi nhận bàn giao. Repo count không đo số người duy trì, active use hoặc willingness to pay. C-G-C18 chứng minh shutdown, chưa có hành vi adopter ở Nhật; A:Tianya/Cohost không chứng minh nhu cầu publisher EOL kit. N09 cho một tiền lệ license thực, nhưng không cho tỷ lệ studio chấp thuận. Đề nghị demand 3/M và international 3–4/M cho phạm vi publisher-handover hiện tại, không tự áp điểm cho mọi nhánh. Giữ theme tốt, không dùng theme để nâng demand.

### C-R2-A09 — Data Act không xác nhận B2B preservation revenue hay feasibility của export thật

**Đích:** A-O2-C1, A-G-C9, A-O2 sustainability 4, feasibility/demo 5/H. **INFERENCE:** N04 xác nhận ngày áp dụng và switching data-processing services; không chứng minh mọi SaaS/community export thuộc cùng nghĩa vụ, không xác nhận controller đã biến mất sẽ cung cấp dữ liệu, cũng không xác nhận khách hàng mua rehydrator. Native importers và MARL tạo áp lực lên giá (N16; A-O2.strongest_counterevidence). Đề nghị sustainability 3/L cho mô hình chưa có buyer; feasibility/demo cần file thật có quyền và tiêu chí ngữ nghĩa trước mức 5. Không suy “phí switching bị cấm” thành “provider chắc chắn mua compliance tool”.

### C-R2-A10 — Consent-aware heritage khác với PII redaction, và phép chọn miễn phí không kiểm được chủ quyền

**Đích:** A-O5-C1/C2/C3, A-O5 innovation/feasibility/legal risk và falsifier. **INFERENCE:** C:R17/R18/R19 nêu cultural protocols, custom fields và quyền cộng đồng; C:R22 có genealogy/đất có thể gây xung đột dù không chỉ là email/tên nhạy cảm. Một admin thích public Wayback hơn phương án setup hai giờ không chứng minh họ có quyền đồng ý thay mọi chủ thể. N07 đã có restricted access, nên “gated archive” không tự là novelty. Đề nghị test người có thẩm quyền và loss of protocol semantics, không dùng public-vs-gated preference làm falsifier của nghĩa vụ consent; legal risk nên high ở dữ liệu nhạy cảm, tương tự C-O3. Nguồn A:R15 phải tách e-legal deposit và WARP thay vì suy một loại ngoại lệ blog thành toàn bộ thẩm quyền lưu web.

## 2. Challenges to Agent B

### C-R2-B01 — “VERIFIED theo nguồn” là quy ước khác brief, và nguồn thứ cấp không trở thành sơ cấp khi trích staff

**Đích:** B metadata; B-G-C4/C8/C9; B-O1-C1–C4; B-O2-C1/C3/C5; B-O3-C1–C3; B-O4-C1/C2/C5; B-O5-C1/C2. **INFERENCE:** tự công bố 15/20 là “nguồn nói Y” minh bạch nhưng không đáp ứng brief §3. Với các claim chỉ một nguồn hoặc độc lập snippet, đề nghị INFERENCE. B-O2-C2/B-G-C3 có primary Glitch + ArchiveTeam trực tiếp, có thể giữ **nội dung được hai nguồn xác nhận**, không tự giữ toàn bộ causal attribution. B-O1-C1 có thể được nâng sau khi dùng C:R15/R16 đã mở trực tiếp; hai EC docs cùng cơ quan không tự là independent. N11+N12 cho phép củng cố kết luận hẹp về quyết định game năm 2024; N06 vẫn không đối chứng độc lập N05 vì khác benchmark. Không đề nghị hạ mọi số thành sai; hạ mức xác tín về thực tế theo đúng hợp đồng.

### C-R2-B02 — Claim không có phương án nào bảo tồn server-side tự mâu thuẫn với Homecoming

**Đích:** B-G-C12, B-O1.innovation basis. **INFERENCE:** N09 mô tả Homecoming được license và vận hành/phát triển City of Heroes; C:R14 có server library nex-go. Tái dựng thủ công và code được cấp phép vẫn là existing alternatives, không được loại khỏi tập đối thủ vì chưa tự động. Sửa thành “chưa xác nhận phương án **tổng quát, hợp pháp, chi phí thấp** cho server bất kỳ”, với các thuộc tính ấy UNKNOWN. Không dùng thiếu universal tool làm bằng chứng commercial gap. N09 là báo thứ cấp, primary announcement 403, nên không gắn VERIFIED mới cho điều khoản hợp đồng.

### C-R2-B03 — Đọc được DOI hôm nay không bác bỏ rủi ro bảo tồn dài hạn

**Đích:** B-O3-C1/C2/C3 và falsifier 80% accessible. **INFERENCE:** C:R02 phân biệt không xác nhận được trong archive được lấy mẫu với bài đã biến mất; site nhà xuất bản còn sống có thể chưa có independent preservation copy. Kiểm IA Scholar là hữu ích để cập nhật coverage nhưng “80% vẫn truy cập được” riêng lẻ không bác bỏ nhu cầu khi site ngừng. C:R03/R05 đã mở official docs về dark archive/trigger; đây là nguồn đối thủ mạnh hơn danh sách chưa mở của B. N14 là bình luận về phân loại journal, chưa đủ kết luận mọi artefact predatory không có giá trị chứng cứ lịch sử. Đề nghị falsifier kiểm có bản bảo tồn độc lập, completeness và trigger/access path, không đồng nhất live availability với persistence.

### C-R2-B04 — Tỷ lệ thiếu revival không xác định nút thắt là pháp lý

**Đích:** B-O1-C6 và falsifier `<10% -> legal, not technical`; B-G-C11/G-C16. **INFERENCE:** N03 cho thấy uncertainty kỹ thuật thật; N09 cho một ca có license; C:R14 cho engineering/reuse thật. Low revival coverage cũng có thể do mất server logic, thiếu phần cứng, ít volunteer, moderation hoặc không đủ giá trị sử dụng. Ngược lại ≥50% có lối thoát không chứng minh phần còn lại không bị hại. Đề nghị đo nguyên nhân từng ca và JTBD chưa đáp ứng, không dùng ngưỡng coverage để nhận dạng nhân quả hay kết luận software+operational “giá trị cao nhất” khi chưa đo giá trị so các chiều.

### C-R2-B05 — Giữ kết luận hẹp về công cụ mới, bác bỏ nếu bị mở rộng thành không ai trả cho preservation

**Đích:** B-G-C10, B §11.5, B-O1–B-O5 sustainability và kết luận WTP chung; đồng thời C-O1/2/3-C4. **INFERENCE:** B thật ra nói chưa tìm thấy **cá nhân trả cho công cụ mới**, không nói không có bất kỳ ngân sách preservation nào. N07/N08 cho dịch vụ Archive-It có annual subscription và mức hợp đồng consortium lịch sử; N10 đưa tín hiệu donation thực cho server; C:R20/R23/R24 cho funding/giá archive. Các bằng chứng này bác bỏ “không ai chi gì”, nhưng **không bác bỏ** UNKNOWN về buyer cho khoảng trống mới. Chi tiết từng opportunity ở bảng §3. Mặt khác một Cohost thiếu tiền không chứng minh mọi operator sắp đóng không có ngân sách. Không lấy comparable spending làm xác nhận một sales pipeline chưa tồn tại.

### C-R2-B06 — Baseline decomp thực ra có trong thân bài, nhưng chưa đủ kết luận AI cần thiết toàn dự án

**Đích:** B-O5-C1/C3/C4, B-O5.ai_role/ai=5, B §7 và §12.1. **INFERENCE:** đọc trực tiếp mục “Programmatic Tools” N05 thấy tác giả báo **SA3 không hàm nào match chỉ bằng công cụ**; AF m2c match 4 hàm mỗi run, Permuter thêm 3–4, và có thảo luận hiệu ứng compiler. Do đó UNKNOWN “không có baseline trích được” có thể cập nhật thành baseline **do tác giả báo**, chưa tái lập. Repo reports/config có thật (N15). Đây là bằng chứng tích cực mạnh hơn A-O2/A-O3 cho vai trò AI ở mẫu đó. Tuy nhiên byte-match chỉ kiểm tiêu chí đó trong toolchain/context cố định; không chứng minh whole-program portability/readability, không có ablation cùng thời gian/tổng chi phí và mẫu độc lập. Đề nghị useful hoặc load-bearing **conditional hypothesis**, ai 3–4/L thay 5/M trước reproduction. Không nói conventional tools làm tốt ngang mẫu đã công bố; hiện nguồn cho kết quả ngược lại.

### C-R2-B07 — DecompileBench không phải đối chứng trực tiếp của pipeline matching với oracle

**Đích:** B-O5-C2, strongest_counterevidence “52,2% khi không có oracle”. **INFERENCE:** N06 có runtime-aware/fuzzing validation, 23.400 functions từ 130 programs và so nhiều decompiler. Khác architecture/data/model/budget với N05. Cụm “khi không có oracle” không phải một treatment/control experiment loại bỏ oracle của Mizuchi; không suy ra thêm oracle sẽ giải toàn bộ lỗi. Giữ cảnh báo functional correctness dưới nhãn nghiên cứu báo cáo, bỏ causal gloss. Readability dùng LLM-as-Judge với giới hạn được tác giả nêu, không thay kiểm maintainability bởi lập trình viên.

### C-R2-B08 — Keitai, web Trung Quốc và Mxit chưa là một market hoặc một falsifier

**Đích:** B-O4-C1/C2/C4/C5, B-O4.international và falsifier top100. **INFERENCE:** nguồn B:R8/B:R9/B:R19 nói các artefact, actor và cơ chế rất khác; không thể dùng Africa/Mxit để xác nhận demand cho tool dump keitai Nhật. “Top 100” thiên về nội dung phổ biến và không bác bỏ giá trị phần hiếm; 70% chạy được không xóa 30% còn mất. C:R22 cho counterexample giá trị của collection nhỏ có ngữ cảnh, không dựa popular rank. Đề nghị tách ca hardware extraction khỏi web censorship và community archive trước chấm international. Không giữ VERIFIED của ca chỉ có một tác giả hoặc báo; cần kiểm model máy/game, quyền và nhóm người dùng thật. Kết luận phân phối luôn bị chặn cũng cần phân biệt game được license/re-release và binary chưa có quyền.

### C-R2-B09 — Hạn chế §1201 cần gắn đúng nhóm artefact, không dùng chung cho EaaSI

**Đích:** B-G-C8, B §5/§8 “software/game chỉ tại chỗ”, B-O5 legal/feasibility. **INFERENCE:** N11/N12 giới hạn xác nhận của tôi ở quyết định 2024 cho videogames; quy tắc computer programs except games khác như C-R2-A07. Ngay cả byte-identical code cũng không tự có quyền phân phối, và license của một server không cấp cho mọi server. Đề nghị làm rõ phạm vi thay vì tăng/giảm mọi legal risk đồng loạt. C-G-C21 của tôi cũng chỉ đọc recommendation ở Round 1; Round 2 mới đọc final rule để giảm bất định về văn bản 2024, vẫn chưa là legal clearance cho ca hiện hành.

## 3. Overlooked alternatives and counterevidence

**Bản đồ hội tụ: trùng câu hỏi không đồng nghĩa trùng opportunity.** Các đánh giá “mạnh hơn” dưới đây là INFERENCE của reviewer trên phạm vi evidence chỉ định.

| Cụm | Trùng phần nào / khác phần nào | Bằng chứng ai mạnh hơn và xử lý đề xuất |
|---|---|---|
| A-O4 / B-O1 / C-O2 | Cùng loss of live service; A nhắm publisher handover trước EOL, B phạm vi broad game continuity, C nhắm maintainer succession sau revival | B mạnh hơn về một tiền lệ license/funding (B:R10, N09/N10); C mạnh hơn về shutdown cụ thể có hai bên xác nhận và ghi rõ chưa biết maintainer demand; A đặt đúng câu hỏi publisher nhưng demand 5 quá xa nguồn. Merge **family** để không đếm ECI ba lần; giữ ba actor/JTBD riêng. |
| B-O3 / C-O1; A-O1 adjacent | B/C cùng scholarly record, C nhấn completeness/bàn giao; A là computation và DH app còn chạy, khác PDF/citation | C mạnh hơn ở đối thủ official PKP/JASPER/ISSN và paper Eve đầy đủ C:R02; B có phản biện journal classification nên bổ sung, không coi predatory = vô giá trị; A có riêng decay studies nhưng không chứng minh causal grant failure. Đề nghị merge B-O3/C-O1 trong map, A-O1 là nhánh khác. |
| A-O2 / B-O2 | Cùng giai đoạn mất platform, A sau export tái dùng semantics, B trước shutdown xin export/cooperation | B mạnh hơn về hành vi operator/ArchiveTeam (B:R11–14); A mạnh hơn về official Mastodon/Data Act nhưng thiếu cạnh tranh MARL và bằng chứng purchaser. N02/N16 làm hẹp post-export gap. Giữ hai giai đoạn, không gộp thành generic migration tool. |
| A-O5 / C-O3; B-O4 adjacent | A giữ consent khi capture, C giữ quyền/ngữ cảnh qua chuyển giao; B phục hồi regional artefact, không nhất thiết indigenous governance | C mạnh hơn về protocol migration limitations/offline và hành vi cộng đồng C:R17–24; A mở rộng quốc gia/lưu chiểu nhưng không xác nhận demand chung cho một tool. B có keitai technical case khác. Merge A-O5/C-O3 ở family stewardship, giữ việc cấp quyền và kiểm quyền sau chuyển riêng; không merge B-O4 chỉ vì cùng heritage. |
| A-O3 / B-O5 | Cùng muốn dùng lại software; A tìm environment chạy binary gốc, B tái dựng source để port/maintain | A có institutional workflow thực N03/N17; B có AI benchmark cụ thể N05/N06 mạnh hơn về cơ chế AI. Hai hướng có thể là alternatives: emulation có thể hoàn thành access mà không cần decompile. Không merge; trước tiên hỏi có cần source reconstruction để làm JTBD hay không. |

**Đối thủ/bằng chứng bị bỏ sót đáng xử lý:** MARL cho A-O2 (N16); JASPER/PKP/Keepers cho B-O3 (C:R03–07); reuse environments/templates cho A-O3 (N03/N17/C:R29); Homecoming được license cho khẳng định universal server gap (N09); Archive-It đã có restricted access và downloadable WARCs cho consent/gated archive (N07/N08). Không suy rằng các đối thủ giải toàn bộ semantics hay tất cả workflow. Không chạy thử nên mức kết luận là documented capability.

**Willingness to pay/sustain, kiểm từng opportunity:** mỗi hàng gắn ID gốc; “công cụ mới” ở đây là khoảng trống được mô tả, không phải mọi sản phẩm preservation mới ra thị trường. Tất cả buyer cho khoảng trống mới vẫn **UNKNOWN**, các comparable dưới đây là INFERENCE trừ phần văn bản hợp đồng đọc được.

| Opportunity | Tiền/nguồn lực đã có | Điều chưa chứng minh và kết luận |
|---|---|---|
| A-O1 | Ngân sách thư viện và dịch vụ web archiving N07/N08 | Chưa thấy lab mua retrofit staticization; grant không bằng đơn hàng. |
| A-O2 | Data Act switching framework N04; competitor importers/viewer giảm nhu cầu trả thêm | Chưa thấy buyer mua generic semantic rehydration; rõ đường B2B là HYPOTHESIS. |
| A-O3 | Institutional workflow thật N03/N17; ngân sách EaaSI trong B-G-C9 | Chưa thấy mua environment inference riêng; so giờ archivist tiết kiệm và procurement. |
| A-O4 | N10 là donor trả để tiếp tục chơi game | Không có studio mua EOL governance kit hoặc maintainer trả succession tool. |
| A-O5 | N07/N08 có subscription và restricted collections | Không chứng minh cộng đồng mua consent/PII triage bổ sung, cũng không thay người có thẩm quyền. |
| B-O1 | N09/N10 cho legal revival/donor case lịch sử | Có willingness to fund dịch vụ cụ thể, chưa có willingness to buy công cụ EOL mới. |
| B-O2 | Operator bỏ engineering time làm export, B-O2-C2/C3 | Chi phí nội bộ không bằng thuê nhà cung cấp; dying operator không mặc nhiên là người trả. |
| B-O3 | PKP miễn phí; consortium subscriptions có tiền lệ N08/C:R03–07 | Việc tham gia dịch vụ miễn phí không xác nhận mua tool mới. |
| B-O4 | B:R8 có volunteer effort; re-release là một alternative B nêu | Mua lại game không bằng trả tool dump; chưa có doanh thu preservation buyer được kiểm. |
| B-O5 | N05 có công cụ/thử nghiệm cá nhân, chưa có giao dịch khách hàng | Nghiên cứu tốn token là researcher expenditure, chưa phải market demand cho provider mới. |
| C-O1 | C:R03–07 và N07/N08 cho loại funding | C-O1-C4 vẫn UNKNOWN: ai trả nghiệm thu completeness riêng? |
| C-O2 | C:R12 trước chỉ snippet; N10 bổ sung donor case khác có số tiền thứ cấp | C-O2-C4 vẫn UNKNOWN: donor của Homecoming không tự tài trợ maintainer succession cho Pretendo. |
| C-O3 | C:R20/R23/R24 cho grants và giá archive được công bố | C-O3-C4 vẫn UNKNOWN: không suy budget chương trình €21m là phần mềm hoặc ngân sách assurance. |

**C-G-C25 — INFERENCE:** N08 là bản service agreement consortium ghi phí subscription 2022–2023, N07 xác nhận annual service model. Đây là bằng chứng mạnh hơn một bảng giá marketing cho tồn tại mô hình có hợp đồng, nhưng không phải bank receipt, không phải giá 2026 và không chứng minh thị trường cho bất kỳ trong 13 khoảng trống. Tiêu đề N10 báo donation round khoảng $8,6K lấp trong ba giờ năm 2024; primary bị 403, nên chỉ dùng làm tín hiệu thứ cấp, không VERIFIED financial result hoặc số thu chính xác.

**Kiểm mọi ai_role load-bearing của A/B:**

| ID | Conventional approach | Có làm ngang không? | Kết luận hiện tại |
|---|---|---|---|
| A-O2 | Parser Activity Streams, schema mapping/ETL, viewer MARL, human mapping review | Với dữ liệu/schema đã biết, có đường đạt cùng kết quả; chưa benchmark schemas lạ | Không có bằng chứng AI bắt buộc; useful hoặc unnecessary theo JTBD. Referential integrity không đủ oracle semantics. N02/N13/N16 |
| A-O3 | Catalog/template reuse, executable header metadata, manual compatibility rules và bounded boot tests | N03 reuse môi trường đã có giải ca gốc; chưa biết tốc độ trên mẫu khó | Useful hypothesis; load-bearing chưa chứng minh, boot success chỉ oracle hẹp. N03/N17 |
| B-O5 | m2c + permuter + objdiff + specialist | N05 báo conventional **không ngang** ở SA3 và chỉ đạt phần mẫu AF; chưa biết với budget công bằng/mẫu độc lập | Tiềm năng có evidence tốt nhất trong ba role, nhưng score 5 cần reproduction/generalisation và chi phí; chưa kết luận bắt buộc cho preservation nói chung. N05/N06/N15 |

**C-G-C26 — INFERENCE:** Có oracle giúp từ chối output sai, không chứng minh AI vượt baseline hoặc cần cho JTBD. Với matching decomp, oracle byte-match mạnh hơn chỉ boot/render, nhưng không tự chứng minh source dễ bảo trì, quyền phân phối hoặc whole-program equivalence khi chỉ kiểm một hàm có context cố định.

## 4. Self-audit of my VERIFIED labels

| Claim | Round 1 label | Revised label | Reason |
|---|---|---|---|
| C-G-C5 | VERIFIED | VERIFIED, phạm vi tài liệu/cơ chế được triển khai | C:R03 primary PKP và C:R04 operator TDL mở trực tiếp, mô tả independently quy trình bảo tồn/status. Giữ fact lựa chọn và đường phục hồi **được tài liệu hóa**; không xác nhận đã thử một restoration hoặc mọi deposit đủ. |
| C-G-C12 | VERIFIED | **INFERENCE** | C:R24/R25 cùng là hai bên cuộc chuyển, thông cáo BBAW còn nói archive sẽ chuyển. Đồng thuận về move chương trình không xác nhận độc lập kỹ thuật archive đã hoàn tất hoặc tiếp tục truy cập đủ. Claim ghép cũ quá rộng; có thể giữ fact hẹp “hai bên công bố chuyển”, không dùng nó thay completion evidence. |
| C-G-C18 | VERIFIED | VERIFIED | Nintendo source + Capcom là bên phát hành game chịu ảnh hưởng độc lập, xác nhận ngày dừng và local/online. Nintendo JP chỉ thêm đối chiếu múi giờ, không đếm thành nguồn độc lập thứ ba. C:R08–10. |
| C-G-C19 | VERIFIED | VERIFIED, phạm vi con số công bố | EC primary + Heise opened trực tiếp (C:R15/R16) đủ independent reporting về số chữ ký **được EC công bố đã xác nhận**. Không có independent recount của tôi và không suy người ký là buyer. |
| C-G-C24 | VERIFIED | VERIFIED, phạm vi published rules | Live Devpost đã mở, nội dung đối chiếu local snapshot/kiểm tra text lặp lại được C:R34. Chỉ xác nhận wording/deadline/required Kiro trong bản đọc; không dự đoán eligibility/judging, không coi snapshot cùng nguồn là xác nhận độc lập. Đây là nhánh reproducible document check của brief. |
| C-O2-C1 | VERIFIED | VERIFIED | Shutdown và local còn hoạt động cùng cơ sở C:R08/R09 như C-G-C18. Không dùng hai claim trùng này làm hai bằng chứng độc lập về demand; suy “emulation chưa đủ multiplayer” chỉ là phân tích cơ chế. |

Kết quả trên danh mục 42 claim đóng băng của C: **5 VERIFIED, 26 INFERENCE, 7 HYPOTHESIS, 4 UNKNOWN** nếu áp revision; không ghi đè Round 1. Nhãn cho C-G-C25/C26 mới tách riêng, không cộng vào số 42. Việc có 6 hay 27 VERIFIED không phải xếp hạng chất lượng agent; phải kiểm từng mệnh đề và phạm vi.

## 5. Revisions to my opportunities

| Opportunity | Status | Sửa gì / vì sao / tác nhân |
|---|---|---|
| C-O1 | revised; proposed merge_with B-O3 ở map | AI useful→unnecessary cho core completeness; ai score 3→2 và ghi rõ optional metadata help chưa đo. B-O3 nhấn core không cần AI, own audit C-R2-A05/B03 yêu cầu baseline công bằng; không đổi demand/theme vì B cũng chưa có buyer/dead-tech anchor. C-G-C12 hạ nhãn không nâng sustainability. |
| C-O2 | revised; proposed family merge_with A-O4/B-O1 | Thêm Homecoming vào strongest alternative; counterevidence và sustainability basis thừa nhận donor/license case nhưng không suy ra buyer của succession. AI useful→unnecessary cho core handover; ai 3→2. Trigger B-O1/B:R10 và own oracle audit. Giữ legal high, feasibility 1, demand 3, sustainability 1 cho phạm vi maintainer chưa có partner/quyền riêng. |
| C-O3 | revised; proposed family merge_with A-O5 | AI useful chỉ là hỗ trợ review, ai 3→2 vì chưa có measured lift; giữ legal high và quyền người có thẩm quyền. C-G-C12 revised khiến tiền lệ công bố chuyển ELAR không dùng như restoration hoàn tất. Trigger A-O5 và own causal/provenance audit. Không merge B-O4 keitai vì JTBD khác. |

`merge_with` là đề nghị tổng hợp evidence, không yêu cầu tạo sản phẩm gộp và không withdrawal các câu hỏi còn kiểm được. File `opportunities-revised.json` chứa diff field-level với `from/to/reason/triggered_by`; không tạo opportunity mới chỉ để có theme hoặc AI cao.

## 6. Positions I keep despite challenge

- **C-O1/C-O3 vẫn dưới theme gate.** Phản biện mạnh nhất từ A là workflow được neo vào nền tảng nghỉ hưu cũng có thể Resurrection. Tôi giữ điểm 1 vì hai phạm vi C chưa có artefact công nghệ chết cụ thể ở trung tâm; nguy cơ biến mất hoặc thông cáo đổi đơn vị không đủ anchor theo rubric. Có thể đổi nếu tìm ca thích hợp thực sự là vấn đề, không chọn tên chết để trang trí.
- **Không kết luận mọi game preservation phải bị loại vì pháp lý.** B có Homecoming, A có publisher-side option; đó là phản chứng đáng giữ. Tôi vẫn chấm rủi ro cao cho C-O2 vì license của một đội không chuyển cho đội khác, và chưa có artefact/partner của mình. N09 hỗ trợ đường có điều kiện, không cấp phép phổ quát.
- **Không nâng donor/grant thành willingness to buy công cụ mới.** N08/N10 và C:R23 là phản biện mạnh với thái cực “không ai chi”; tôi giữ C-O1/2/3-C4 UNKNOWN vì loại chi tiêu, người trả và công việc không khớp đầy đủ. Cần transaction/commitment cho đúng scope.
- **Tôi không đồng ý loại B-O5 chỉ vì DecompileBench kém hơn.** N05 có baseline programmatic cụ thể và result của một mẫu; N06 khác benchmark. Giữ là hướng cơ chế đáng tái lập, đồng thời phản đối nhãn load-bearing đã chắc chắn và score 5 chỉ vì có oracle.
- **Bảo tồn bản ghi nhạy cảm có thể cần giữ hạn chế thay vì mở công khai.** Phản biện A là consent quá nặng làm coverage thấp; C:R22 là bằng chứng harm cụ thể. Độ dễ setup không thay quyết định người có quyền; không lấy preservation coverage làm mục tiêu duy nhất.

## 7. Remaining disagreements

| Bất đồng | Evidence sẽ phân xử | Trạng thái |
|---|---|---|
| A-O2/A-O3 AI load-bearing hay chỉ hữu ích | Mẫu artefact đúng quyền, ground truth, baseline parser/catalog đủ mạnh, cùng thời gian/chi phí, lỗi semantics và giờ review | UNKNOWN; không làm trong Round 2 |
| B-O5 có measured lift đủ lớn và tổng quát | Tái lập N15 ở project khác; ablation cùng budget; kiểm byte-match không cho cheat/inline asm; tính expert time và tokens | HYPOTHESIS về toàn project; N05 đã giúp giảm UNKNOWN baseline nguồn báo |
| A-O4 publisher adoption vs public advocacy | Interview/decision của studio có quyền middleware, chi phí EOL thực và willingness to adopt/pay; không dùng chữ ký thay câu trả lời | UNKNOWN |
| B-O3 participation-only hay C-O1 còn loss-of-completeness | Manifest trước/sau, article/supplement/version state, quyền trigger, đối chiếu PKP/JASPER/Keepers hiện có | HYPOTHESIS; không suy từ site còn sống |
| A-O5/C-O3 cần thêm tooling hay chủ yếu staff/governance | Ca chuyển thật có custom protocols, role/access ground truth và quyết định cộng đồng; so tool chính thức | HYPOTHESIS; không chỉ survey admin chọn phương án rẻ |
| Nhu cầu quốc tế cho đúng target | Actor và hành vi độc lập cùng JTBD ở từng vùng; không gộp Mxit vào demand keitai hoặc funding EU vào buyer Nhật | UNKNOWN theo từng nhánh |
| C-G-C12 archive đã chuyển đủ hay mới công bố | Acceptance/completion record, URL/object access continuity, scope/counts trước/sau hoặc báo cáo operator độc lập | INFERENCE; đã hạ nhãn |
| Legal path hiện hành cho từng artefact | Final/current instrument và license đúng phạm vi/jurisdiction, quyền asset, controller/cultural authority | Chỉ xác nhận text 2024 đã mở; không blanket clearance |

Không có quyết định xếp hạng Task B với Phase 2, không chọn finalist, không thiết kế ứng dụng. Các proposed tests là cách thu bằng chứng tiếp theo, chưa thực hiện hay liên hệ bất kỳ bên nào.

## 8. New references

Nguồn mới **so với Round 1 của C**, dù một số đã có trong A/B; mọi dòng dưới đã mở trực tiếp nội dung, ngày truy cập 2026-11-25 UTC. Không lặp các C:R01–34 đã có. Thang A/T/M/C/F/R/B 0–5; weighted 0–100 theo 20/20/20/15/10/10/5, SR/RR 0–5 tách reliability/relevance đối với challenge chỉ định. Điểm không biến một báo/blog thành independent verification của chính thử nghiệm mà nó thuật.

| Ref ID | URL | Title | Publisher | Pub date | Accessed | Opened directly or snippet | Claims/challenges | 7 scores | Weighted | Source Reliability | Reference Relevance |
|---|---|---|---|---|---|---|---|---|---:|---:|---:|
| N01 | https://endings.uvic.ca/principles.html | Endings Principles for Digital Longevity | UVic Endings Project | version 2023-03-03, page revision 2025-01-03 | 2026-11-25 | direct | A01/A03 | 5/4/5/5/3/5/4 | 91 | 4.5 | 5 |
| N02 | https://raw.githubusercontent.com/mastodon/documentation/main/content/en/user/moving.md | Moving or leaving accounts | Mastodon official docs | n.d., current branch | 2026-11-25 | direct | A04/A05 | 5/4/5/5/4/5/4 | 93 | 4.5 | 5 |
| N03 | https://www.softwarepreservationnetwork.org/eaasi-case-study-1-the-would-be-gentleman/ | EaaSI Case Study #1 | SPN/Stanford, Schweikert and Gates | 2021-01-11 | 2026-11-25 | direct | A02/A06/B04 | 5/5/5/5/2/4/4 | 91 | 4.5 | 5 |
| N04 | https://digital-strategy.ec.europa.eu/en/policies/data-act | Data Act | European Commission DG CONNECT | n.d., current policy page | 2026-11-25 | direct | A09 | 5/3/5/4/5/5/4 | 88 | 5 | 4 |
| N05 | https://gambiconf.substack.com/p/can-llms-really-do-matching-decompilation | Can LLMs Really Do Matching Decompilation? | Macabeus/Gambiconf | 2026-03-10 | 2026-11-25 | direct | B06/B07/C-G-C26 | 3/4/4/5/5/4/3 | 80 | 3 | 5 |
| N06 | https://arxiv.org/html/2505.11340v1 | DecompileBench | Gao et al., arXiv | 2025-05-16 | 2026-11-25 | direct | B01/B07 | 5/5/4/4/4/5/4 | 90 | 4.5 | 4 |
| N07 | https://support.archive-it.org/hc/en-us/articles/208111766-Want-to-know-more-about-Archive-It | Want to know more about Archive-It? | Internet Archive/Archive-It | updated 2024-02-27 | 2026-11-25 | direct | A10/B05/C-G-C25 | 5/4/5/5/3/4/3 | 88 | 4 | 5 |
| N08 | https://www.concan.ca/sites/default/files/license/2017%20ConCan%20Archive-It_agreement_COPPUL_OCUL_BCI_CAUL_Exhibit%20A%206.29.2022.pdf | Archive-It Service Agreement, Exhibit A | ConCan/consortium service agreement | 2022-06-29 | 2026-11-25 | direct | B05/C-G-C25 | 5/4/5/5/2/5/4 | 89 | 4.5 | 5 |
| N09 | https://massivelyop.com/2024/01/04/ncsoft-has-officially-granted-a-city-of-heroes-server-license-to-the-homecoming-crew/ | NCsoft has officially granted a City of Heroes server license | Massively Overpowered, Bree Royce | 2024-01-04 | 2026-11-25 | direct | A08/B02/B09 | 4/3/4/5/3/4/3 | 76 | 3.5 | 5 |
| N10 | https://massivelyop.com/2024/01/29/city-of-heroes-players-filled-homecomings-latest-8-6k-monthly-donation-round-in-three-hours/ | Homecoming's latest $8.6K monthly donation round | Massively Overpowered | 2024-01-29 | 2026-11-25 | direct | B05/C-G-C25 | 4/3/4/5/3/3/3 | 74 | 3.5 | 5 |
| N11 | https://www.govinfo.gov/content/pkg/FR-2024-10-28/pdf/2024-24563.pdf | Exemption to Prohibition on Circumvention, Final Rule | Library of Congress/Federal Register | 2024-10-28 | 2026-11-25 | direct | A07/B09 | 5/5/5/5/3/5/5 | 96 | 5 | 5 |
| N12 | https://gamehistory.org/dmca-2024-statement/ | Statement on DMCA 2024 triennial review ruling | VGHF, Phil Salvador | 2024-10-25 | 2026-11-25 | direct | A07/B01/B09 | 4/3/4/5/3/4/2 | 75 | 3.5 | 5 |
| N13 | https://dtinit.org/ | Data Transfer Initiative | DTI | n.d., current page | 2026-11-25 | direct | A05 | 4/3/4/4/4/3/3 | 73 | 4 | 4 |
| N14 | https://arxiv.org/abs/2009.07561 | Comment on Open is not forever | Matan Shelomi, arXiv | 2020-09-16 | 2026-11-25 | direct, abstract page only | B03 | 3/2/3/3/1/3/3 | 52 | 3 | 3 |
| N15 | https://github.com/macabeus/mizuchi-benchmark-reports | Mizuchi benchmark reports | Macabeus official repo | n.d., current branch | 2026-11-25 | direct, README listing reports/config | B06 | 4/4/4/5/5/5/3 | 86 | 3.5 | 5 |
| N16 | https://github.com/s427/MARL | Mastodon Archive Reader Lite | s427 official repository | n.d., current branch | 2026-11-25 | direct, docs only; not run | A04/A05 | 4/5/5/5/4/5/4 | 93 | 4 | 5 |
| N17 | https://publications.beeldengeluid.nl/pub/1858/Emulation-as-a-Service-Test-Report.pdf | Emulation as a Service for Heritage Institutions, Test Report | Dutch NDE/Beeld en Geluid | 2020-10, v1.0 | 2026-11-25 | direct | A06 | 5/5/5/5/1/4/4 | 89 | 4.5 | 5 |

Các page chỉ đọc abstract/README được ghi rõ: không nói đã đọc full paper hoặc tái lập repo. N14 chỉ giúp kiểm sự tồn tại của phản biện, không đủ định lượng predatory hay bác giá trị bảo tồn. N05/N15 cùng tác giả không tính hai xác nhận độc lập; N11/N12 chỉ dùng xác nhận quyết định **năm 2024**.
