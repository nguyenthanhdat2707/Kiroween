# Task B Round 2 — Agent B

## Metadata

| Trường | Giá trị |
|---|---|
| Model | `claude-sonnet-5-5` (quan sát từ runtime của phiên); effort: không quan sát được |
| Bắt đầu / kết thúc (UTC) | 2026-11-25 12:43 / 12:48 |
| Đầu vào đã đọc | `agent-a/report.md`, `agent-a/opportunities.json`, `agent-c/report.md`, `agent-c/opportunities.json`; báo cáo Round 1 của tôi (đóng băng, không sửa) |
| Nguồn mới mở trực tiếp | 11 (N1–N11, bằng `curl`; PDF đọc bằng `pdftotext`) |
| Snippet-only mới | 0 |
| Thất bại | timeextension.com trả 403 (không xác nhận độc lập được claim về keitai); bộ trích xuất HTML của tôi không đọc được PDF ở lần đầu (đã đọc lại bằng `pdftotext`) |
| Số phản biện | 13 với Agent A (A1–A13), 8 với Agent C (C1–C8) |
| Đổi nhãn của chính tôi | 13 (12 VERIFIED→INFERENCE, 1 UNKNOWN→INFERENCE); 8 claim giữ VERIFIED, trong đó 4 claim có bằng chứng mạnh hơn sau Round 2 |
| Cơ hội | 0 giữ nguyên · 4 sửa đổi (B-O1, B-O2, B-O4, B-O5) · 1 rút (B-O3 → gộp vào C-O1) |

**Quy tắc nhãn dùng cho Round 2.** Ở Round 1 tôi tự đặt một quy tắc lỏng: "nguồn X báo cáo Y" thì được tính là VERIFIED. Quy tắc này lệch khỏi brief §3, nên Round 2 dùng quy tắc chặt:

- **VERIFIED** chỉ khi có (i) nguồn sơ cấp mở trực tiếp **và** xác nhận độc lập cũng mở trực tiếp; hoặc (ii) văn bản chính thức mà bản thân văn bản là sự kiện (quyết định của EC, văn bản luật, tài liệu chính thức của dự án về chính nó). Loại (ii) kiểm lại được bằng cách tải lại văn bản.
- Phát hiện của **một** nghiên cứu, **một** bài blog hoặc **một** bài báo duy nhất thì là **INFERENCE**, kể cả khi đã mở trực tiếp nguồn.
- Hai trang của cùng một nhà xuất bản không tính là độc lập. Quy tắc này của Agent C hợp lý và tôi áp dụng theo.

## 1. Challenges to Agent A

| # | Claim / cơ hội | Phản biện | Bằng chứng |
|---|---|---|---|
| A1 | A-G-C5, A-G-C10, A-G-C12, A-G-C13, A-G-C14 (đều gắn VERIFIED) | Đây là các khẳng định **tổng hợp/diễn giải** ("nhu cầu mạnh nhất tập trung ở hai cực", "rủi ro ảo tưởng cao nhất", "bài toán kinh tế bất đối xứng"). Không có nguồn đơn lẻ nào xác minh được chúng → **INFERENCE**. Đây là lý do chính khiến A có tỷ lệ 27/30 VERIFIED. | brief §3; nội dung chính của A tại §4, §6, §8 |
| A2 | A-O1-C3 [VERIFIED]: Endings Principles "chứng minh" dự án sống lâu không tốn phí | R09 là bộ **nguyên tắc mang tính quy định**, không phải đo lường độ bền. Nó không chứng minh kết quả → **INFERENCE**. | A-R09 (A tự mô tả là "bộ nguyên tắc v2.2.1") |
| A3 | A-O1-C1, A-O1-C2 [VERIFIED] | Mỗi claim là phát hiện của một nghiên cứu peer-reviewed. Nguồn tin cậy cao, nhưng theo brief §3 thì vẫn chỉ là **INFERENCE** khi chưa có xác nhận độc lập. Các nghiên cứu này cũng xuất bản năm 2008–2019, không phải dữ liệu 2025–2026. | A-R05, A-R07, A-R08 |
| A4 | A-O1 `demand` 4/H | Anchor 4–5 yêu cầu bằng chứng **hành vi hiện tại (2025–2026)** của người dùng mục tiêu. A chỉ có tỷ lệ mất mát lịch sử, đúng kiểu anchor 3. Chính A cũng dẫn Wren 2017: 94% tài nguyên được trích dẫn nhiều tự di dời thành công, tức phần chết phần lớn là tài nguyên ít được dùng. Đề xuất **3/M**. | A-R06; rubric `demand` |
| A5 | A-O2 `demand` 4, `feasibility` 5/H, `ai` load-bearing | (a) Ví dụ người dùng chính là InVision, nhưng chỉ có snippet (A-R23) → không đủ cho mức 4. (b) Tài liệu chính thức của Mastodon nói archive là Activity Streams 2.0, *"can be viewed by any software that understands how to parse"* định dạng này. Đây là schema **có tài liệu công khai**, nên parser truyền thống là đủ; suy luận schema bằng AI không cần thiết với định dạng này. (c) Oracle "toàn vẹn tham chiếu 100%" chỉ đảm bảo khóa ngoại **nhất quán**, không đảm bảo **đúng nghĩa**: ánh xạ sai trường vẫn có thể có 0 bản ghi mồ côi. (d) A chưa kiểm tra file export của Cohost có giữ ID quan hệ hay không, nên feasibility 5/H là quá tự tin. | N3 (Mastodon `moving.md`, mở trực tiếp); A-R23 snippet |
| A6 | A-O3 ai load-bearing; A-O3-C1 [VERIFIED] | (a) Case study EaaSI xác nhận quá trình mất **2 ngày** (N4), nhưng đó là **một** ca năm 2021 → INFERENCE. (b) Trong chính ca này, độ trễ đến từ việc tài liệu game nói về máy Mac đời trước, không khớp với BasiliskII; chuyên viên đã tự xác định Mini vMac là phương án dự phòng. Không gian tìm kiếm (vài emulator × vài phiên bản OS) đủ nhỏ để **quét tất định kèm kiểm tra boot**. EaaSI cũng đã chia sẻ môi trường dựng sẵn giữa các node (C-G-C11). (c) Oracle "boot không crash" yếu: phần mềm boot được chưa chắc đã chạy đúng. → AI **useful**, chưa phải load-bearing. | N4; C-R28/R29 |
| A7 | A-O3-C3 [VERIFIED] (Copyright Office từ chối truy cập từ xa) | **Giữ VERIFIED.** A chỉ dựa vào snippet (A-R21), nhưng tôi đã mở Register's Recommendation tháng 10/2024 (N11). Văn bản ghi rằng với class video game, bên đề xuất muốn cung cấp *"off-premises access"*, và Register kết luận họ không chứng minh được fair use. | N11, B-R4 |
| A8 | A-O4-C1 [VERIFIED] (phản hồi EC) | **Giữ VERIFIED.** Nội dung phản hồi EC trong A chỉ có snippet (A-R21b), nhưng thông cáo IP/26/1369 tôi đã mở ở Round 1 xác nhận EC từ chối nghĩa vụ pháp lý và cam kết xây code of conduct. Số chữ ký 1.294.188 cũng được heise xác nhận độc lập (N1). | B-R2, N1 |
| A9 | A-O4 `demand` 5/H, `international` 5/H | Bằng chứng nhu cầu (chữ ký ECI, Pretendo) đến từ **người chơi**, trong khi target của A-O4 là **nhà phát hành/studio**, nhóm mà chính A ghi là phản đối. Với đúng target đã nêu, nhu cầu được chứng minh là **âm**. Mức `international` 5 đòi điều kiện "không có rào cản pháp lý lớn", nhưng A tự chấm legal_risk "high". Đề xuất demand 3 (cho target nhà phát hành), international 4. | A-O4 commercial note; rubric |
| A10 | A-O4-C3 [VERIFIED]: "Các nền tảng cộng đồng lớn" như Cohost | Wikipedia (chính A-R18, tôi đã mở lại) ghi Cohost có 203.805 tài khoản **đăng ký** nhưng chỉ **21.142 MAU** (11/2023); TechCrunch ghi 30.000 MAU (3/2024). Cohost là nền tảng **nhỏ**. Ngày offline/mở lại của Tianya chỉ đến từ Wikipedia (một nguồn thứ cấp, N6); con số "nợ >10 triệu NDT" chỉ là snippet. → INFERENCE. | N5, N6, B-R14 |
| A11 | A-O5-C3 [VERIFIED] | Phần kết cục vụ Hachette có A-R19c xác nhận, nhưng mệnh đề "bảo tồn công cộng không thể dựa tràn lan vào Fair Use" là diễn giải → INFERENCE. | A-R19c |
| A12 | A-O5 `international` 5/H | Bằng chứng của A ở Nhật/Hàn/Singapore là **hạ tầng thư viện quốc gia**, không phải người dùng mục tiêu (cộng đồng lưu trữ) đang gặp vấn đề. Đề xuất 3–4. Theme 2 thì trượt cổng; A đã tự ghi nhận điều này và tôi đồng ý. | rubric `international` |
| A13 | A-O1 `international` 5/H | Mẫu tạp chí có tính toàn cầu, nhưng anchor 5 yêu cầu **người dùng mục tiêu được nêu tên** ở 3 khu vực. A chưa nêu actor cụ thể ở châu Á → 4/M. | rubric |

## 2. Challenges to Agent C

| # | Claim / cơ hội | Phản biện | Bằng chứng |
|---|---|---|---|
| C1 | C-O2-C3 (HYPOTHESIS: nhu cầu "bàn giao maintainer") | Có phản chứng trực tiếp. Homecoming (City of Heroes) đã vận hành từ 2019, được NCSoft cấp license năm 2024, và PC Gamer ghi mục tiêu quyên góp hằng tháng *"are filled in days, if not hours"*. Với đội revival trưởng thành, nút thắt là **quyền hợp pháp** chứ không phải kế nhiệm maintainer. C đã bỏ sót tiền lệ license này. | N8, B-R10 |
| C2 | C-O2 `international` 3/M ("Asia chỉ có thông báo vendor") | Châu Á có bằng chứng về **vấn đề**: >70% trong ~2.200 game live‑service ở Nhật dừng trước năm thứ 3 (B-R24), và cộng đồng keitai đang cứu game trên phần cứng chết (B-R8). Bằng chứng về WTP ở châu Á thì vẫn thiếu, như C nói. Điểm 3 vẫn hợp lý, nhưng phần cơ sở nên được cập nhật. | B-R24, B-R8 |
| C3 | C-O2-C2: Pretendo "không thể tự chuyển user account" (C chỉ có snippet) | **Xác nhận.** Tôi đã mở được pretendo.network (C bị 403): *"Will my existing NNIDs work on Pretendo Network? Sadly, no… only Nintendo holds your user data"*. Đây là dữ liệu người dùng bị kẹt ở vendor, một tổn thất mà revival không khôi phục được. | N2 |
| C4 | C-G-C7 (INFERENCE: JASPER) | C có thể nâng lên **VERIFIED** (loại ii): trang chính thức của DOAJ ghi *"DOAJ provides the JASPER service free of charge"* và loại các tạp chí *"supported or funded by an organisation capable of covering the costs"*. Kết hợp với tài liệu PKP mà C đã mở, đây là xác nhận từ hai tổ chức độc lập. | N10; C-R03 |
| C5 | C-G-C1 (Eve 27,64%) | Đồng ý giữ INFERENCE. Tôi mở cùng bản PDF: *"2,056,492 works in our sample (27.64%) that are seemingly unpreserved"*. Từ "seemingly" xác nhận cách diễn giải thận trọng của C, và tôi rút lại cách viết "~28% không được lưu trữ" ở Round 1. | N9 |
| C6 | C-O1 `innovation` 1, `theme` 1 | Đồng ý. Đây là lý do tôi rút B-O3 (§5). | N10 |
| C7 | C-O3 | Đồng ý với theme 1 (trượt cổng). Phản biện thêm: C-O3 và A-O5 về bản chất là **một** không gian (đồng thuận và quyền văn hóa khi lưu trữ/chuyển giao). Bằng chứng của C cụ thể hơn (Mukurtu migration bỏ sót custom field, Ranongga); bằng chứng của A rộng hơn về pháp lý (NDL, GDPR Art 89). Synthesis nên gộp hai cơ hội này. | C-R17, C-R22; A-R15 |
| C8 | Đánh giá AI của C (C-G-C22: không cơ hội nào load-bearing) | Đúng với ba cơ hội của C. Tuy vậy, không nên tổng quát hóa thành "AI không load-bearing trong bảo tồn": matching decompilation có **oracle khớp byte**, và đã có ít nhất một benchmark (B-R15, n=60) cùng một benchmark học thuật (B-R16). Xem §6. | B-R15, B-R16 |

## 3. Overlooked alternatives and counterevidence

**Phương án thay thế mà cả ba agent bỏ sót hoặc chưa xét đủ:**

1. **GOG Preservation Program** (N7, mở trực tiếp). Đây là chương trình thương mại hiện có **337 game** cùng 1.763 "game improvements", bán DRM-free và sửa để chạy trên phần cứng hiện đại (ví dụ thêm Glide emulation cho Mortal Kombat 4). Chương trình này **cạnh tranh trực tiếp** với mọi ý tưởng "hồi sinh phần mềm/game cũ" ở phân khúc game offline. Nó cũng là **bằng chứng có người trả tiền** cho nội dung đã được bảo tồn (xem mục 3 bên dưới). Nhãn: INFERENCE (một nguồn, có thiên lệch thương mại).
2. **Pretendo Network** (A, C đã nêu; tôi bỏ sót ở Round 1). Đây là phương án thay thế mạnh nhất cho B-O1 ở nhánh Nintendo. Giới hạn cũng đã rõ: không giữ được NNID (N2).
3. **JASPER / PKP PN / Keepers** (C đã nêu; tôi bỏ sót) cho B-O3. JASPER miễn phí (N10).
4. **Export Activity Streams 2.0 của Mastodon** (A đã nêu). Định dạng có tài liệu, nên phần lớn "khôi phục ngữ nghĩa" chỉ cần parser (N3).
5. **G-MODE Archives / HAMSTER Appli Archives** (trong B-R8). Game keitai đã được tái phát hành thương mại; đây là phương án thay thế và cũng là bằng chứng chi tiêu cho B-O4.

**Phản chứng mới:**
- Cohost chỉ có 21.142 MAU (11/2023, N5). Mọi lập luận lấy Cohost làm "nền tảng lớn" (A-O4-C3) đều bị phóng đại.
- Pretendo không chuyển được tài khoản cũ (N2). Hồi sinh do cộng đồng làm **không** khôi phục được chiều user-data, vì dữ liệu này nằm ở vendor.

### Kiểm tra "không có bằng chứng ai trả tiền" (yêu cầu 3 của Coordinator)

Khẳng định B-G-C10 ở Round 1 (UNKNOWN) **quá rộng** và cần sửa. Kết quả theo từng cơ hội:

| Cơ hội | Ai trả / tài trợ (bằng chứng) | Loại | Kết luận |
|---|---|---|---|
| B-O1 / A-O4 / C-O2 (live-service EOL) | Người chơi **quyên góp** cho Homecoming, đủ mục tiêu tháng "in days, if not hours" (N8). Người mua trả tiền cho game cũ qua GOG (N7). Nhà phát hành (người trả trong A-O4): EC xác nhận họ không chịu nghĩa vụ (B-R2), ESA phản đối (B-R4) | Demonstrated (quyên góp, mua sản phẩm), chỉ có bằng chứng đơn lẻ | Có WTP cho **trải nghiệm được hồi sinh**; **không** có bằng chứng ai trả cho *công cụ/chuẩn* EOL |
| B-O2 / A-O2 (cửa sổ đóng cửa, export) | Cohost: 2.630 người trả phí cho nền tảng *đang sống* (B-R14), không phải cho bảo tồn. EU Data Act tạo áp lực tuân thủ (A-R02), nhưng chưa thấy chi tiêu | Hypothetical | **Không có bằng chứng** WTP |
| B-O3 / C-O1 (tạp chí) | JASPER miễn phí, PKP PN miễn phí; DOAJ loại các tạp chí có khả năng tự trả (N10, C-R03) | Demonstrated, nhưng là tiền **tài trợ cho hạ tầng miễn phí** | Phương án miễn phí làm thị trường trả phí cho công cụ mới khó tồn tại |
| A-O1 (web app học thuật) | Chỉ có grant/thư viện (suy luận của A) | Hypothetical | Không có bằng chứng |
| A-O3 / B-O5 (môi trường, decomp) | EaaSI nhận tài trợ quỹ: Yale 3,5 triệu USD (B-R22). Decomp: không tìm thấy | Grant đã có; với decomp thì chưa rõ | Có grant thể chế; không có giao dịch thương mại |
| A-O5 / C-O3 (di sản có đồng thuận) | **PARADISEC công bố giá** (ví dụ AUD20/file video) và đề nghị dự trù phí lưu trữ trong grant; BBAW €21 triệu cho chương trình 10 năm (C-R20, C-R23, C-R24) | Demonstrated (biểu phí công khai) | **Bằng chứng giá rõ nhất trong cả ba báo cáo**, nhưng đây là phí cho archive hiện có, không phải cho bên mới |
| B-O4 (keitai) | Tái phát hành thương mại (G-MODE Archives; 51 bộ Appli Archives trên PS Mobile, B-R8); quyên góp nhỏ | Demonstrated (sản phẩm) | Có WTP cho **nội dung** đã cứu; không có cho công cụ |

**Kết luận sửa đổi (B-G-C10 → INFERENCE).** Có bằng chứng người dùng trả tiền hoặc quyên góp cho **nội dung/trải nghiệm đã được bảo tồn**. Các tổ chức cũng trả **phí lưu trữ** cho archive hiện có. **Không** có bằng chứng ai trả cho một **công cụ bảo tồn mới** trong bất kỳ cơ hội nào của ba agent. Người hưởng lợi (người chơi, cộng đồng) thường khác người phải trả (nhà phát hành, nhà vận hành sắp chết).

### Tính cần thiết của AI với các cơ hội "load-bearing" (yêu cầu 4)

| Cơ hội | Phương án truyền thống | Có làm tốt bằng không? | Kết luận của tôi |
|---|---|---|---|
| A-O2 | Parser theo schema có tài liệu (AS2.0, các export JSON có tài liệu), kiểm tra toàn vẹn tham chiếu | **Có**, với định dạng có tài liệu (N3). AI chỉ giúp khi export không có tài liệu, và khi đó oracle toàn vẹn không kiểm được nghĩa | **useful**, không load-bearing |
| A-O3 | Quét tất định qua các tổ hợp emulator × OS có kiểm tra boot; tái sử dụng môi trường dựng sẵn của EaaSI | **Phần lớn có**: không gian tổ hợp nhỏ, môi trường dùng chung đã có (N4, C-R28) | **useful** |
| B-O5 (của tôi) | m2c + decomp-permuter + objdiff | **Chưa rõ**. B-R15 cho biết khi pha công cụ không khớp, gần một nửa số hàm khớp được nhờ AI khớp ngay ở lần thử đầu, nhưng không công bố baseline chỉ‑công‑cụ dưới dạng văn bản; DecompileBench cho thấy LLM kém về tính đúng chức năng khi không có oracle | **Giữ load-bearing ở mức GIẢ THUYẾT**, hạ `ai` 5→4/L. Chỉ coi là load-bearing nếu falsifier (≥15 điểm phần trăm so với chỉ công cụ) qua được |

## 4. Self-audit of my VERIFIED labels

| Claim | Round 1 label | Revised label | Reason |
|---|---|---|---|
| B-G-C3 (chi phí Glitch tăng theo tuổi nền tảng, nói chung) | VERIFIED | **INFERENCE** | Lý do là tuyên bố của chính Glitch; việc khái quát hóa ("tăng theo tuổi") là suy luận của tôi |
| B-G-C4 (Cohost nhỏ, thâm hụt) | VERIFIED | VERIFIED (sửa nội dung) | Thêm xác nhận độc lập mở trực tiếp: Wikipedia ghi 21.142 MAU (11/2023, N5), TechCrunch ghi 30.000 MAU (3/2024, B-R14). Con số thâm hụt 17.000 USD chỉ có một nguồn → phần này là INFERENCE |
| B-G-C8 (US Copyright Office từ chối truy cập từ xa) | VERIFIED | VERIFIED (mạnh hơn) | Đã mở chính văn bản Register's Recommendation (N11) cùng với VGHF (B-R4) |
| B-G-C9 (Yale nhận 3,5 triệu USD cho EaaSI) | VERIFIED | **INFERENCE** | Một nguồn sơ cấp tự báo cáo, chưa có xác nhận độc lập |
| B-O1-C1 (1,29 triệu chữ ký ECI) | VERIFIED | VERIFIED (mạnh hơn) | Ở Round 1, R1 và R2 cùng từ EC nên không độc lập. Nay có heise mở trực tiếp (N1): 1.294.188 |
| B-O1-C2 (EC thừa nhận game phụ thuộc server) | VERIFIED | VERIFIED | Loại (ii): văn bản chính thức của EC, bản thân văn bản là sự kiện |
| B-O1-C3 (EC từ chối nghĩa vụ, chọn code of conduct) | VERIFIED | VERIFIED | Loại (ii); A-R01 (sổ đăng ký ECI) cũng dẫn phản hồi C(2026)4110 |
| B-O1-C4 (Homecoming có license, sống bằng quyên góp) | VERIFIED | VERIFIED (mạnh hơn) | Thêm PC Gamer mở trực tiếp (N8) bên cạnh MassivelyOP (B-R10) |
| B-O2-C1 (số liệu Cohost) | VERIFIED | VERIFIED (sửa nội dung) | Giống B-G-C4: MAU được xác nhận, con số thâm hụt chỉ một nguồn |
| B-O2-C2 (Glitch đóng hosting ngày 8/7/2025) | VERIFIED | VERIFIED | Glitch (B-R11) và ArchiveTeam theo dõi độc lập (B-R13). Lý do đóng cửa chỉ là tuyên bố của nhà vận hành |
| B-O2-C3 (ArchiveTeam phụ thuộc hợp tác của nhà vận hành) | VERIFIED | VERIFIED (mạnh hơn) | Wikipedia (N5) trích lời staff Cohost: nhà tài trợ đề nghị *"hold off on shutting down until Archive Team archival has finished"*, khớp với B-R12 |
| B-O2-C5 (Cyworld dừng vì thiếu tiền khôi phục dữ liệu) | VERIFIED | **INFERENCE** | Nguồn mở trực tiếp duy nhất là asiae 2026; bài asiae 2025 chỉ là snippet và cùng nhà xuất bản |
| B-O3-C1 (~28% DOI không được bảo tồn) | VERIFIED | **INFERENCE** | Phát hiện của một nghiên cứu. Văn bản gốc nói "seemingly unpreserved" 27,64% (N9). Thống nhất với C-G-C1 |
| B-O3-C2 (174 tạp chí OA biến mất) | VERIFIED | **INFERENCE** | Một nghiên cứu, có phản biện (Shelomi) và phiên bản sau báo 192 |
| B-O3-C3 (không có đồng thuận về trách nhiệm lưu trữ) | VERIFIED | **INFERENCE** | Ý kiến của tác giả |
| B-O4-C1 (3 nền tảng keitai không tương thích, không có emulator toàn diện) | VERIFIED | **INFERENCE** | Chỉ có Hit Save; Time Extension trả 403 nên chưa xác nhận độc lập được |
| B-O4-C2 (công sức tình nguyện cho keitai) | VERIFIED | **INFERENCE** | Một nguồn cộng đồng |
| B-O4-C5 (Mxit chuyển IP cho Reach Trust) | VERIFIED | **INFERENCE** | Quartz dẫn lại Fin24; xác nhận khác chỉ là snippet |
| B-O5-C1 (pipeline khớp 74%) | VERIFIED ("nguồn báo cáo") | **INFERENCE** | Một blog, n=60, chưa tái lập |
| B-O5-C2 (DecompileBench −52,2%) | VERIFIED | **INFERENCE** | Một nghiên cứu (dù peer-reviewed); tôi mới đọc abstract |
| B-G-C10 (WTP cho bảo tồn) | UNKNOWN | **INFERENCE** (nội dung sửa) | Có WTP cho nội dung đã bảo tồn và phí lưu trữ; không có cho công cụ mới (§3) |

**Tổng kết nhãn của tôi sau Round 2** (41 claim): VERIFIED 20 → **8**, INFERENCE 18 → **31**, HYPOTHESIS 2, UNKNOWN 1 → **0**.

**Kiểm tra các claim VERIFIED then chốt của agent khác:**

| Claim | Kết luận của tôi |
|---|---|
| A-O4-C1 | Giữ VERIFIED (B-R2, N1) |
| A-O4-C2 | Giữ VERIFIED (N2 xác nhận NNID; C-R13/R14) |
| A-O2-C2 | Giữ VERIFIED (loại ii, N3) |
| A-O5-C1, A-O5-C2 | Giữ VERIFIED (văn bản chính thức) |
| A-O3-C3 | Giữ VERIFIED (N11) |
| A-O3-C1 | → INFERENCE (một ca) |
| A-O1-C1, A-O1-C2 | → INFERENCE (nghiên cứu đơn lẻ) |
| A-O1-C3 | → INFERENCE (nguyên tắc ≠ bằng chứng) |
| A-O4-C3 | → INFERENCE (Tianya chỉ có Wikipedia; Cohost bị phóng đại) |
| A-O5-C3 | → INFERENCE (diễn giải) |
| A-G-C5, C10, C12, C13, C14 | → INFERENCE |
| C-G-C5, C-G-C12, C-G-C18, C-G-C19 | Giữ VERIFIED (C-G-C19 có thêm N1) |
| C-G-C7 | Có thể nâng lên VERIFIED (N10) |

## 5. Revisions to my opportunities

| Cơ hội | Trạng thái | Thay đổi | Lý do | Ai kích hoạt |
|---|---|---|---|---|
| B-O1 | **revised**; đề xuất gộp với A-O4, C-O2 | Phương án thay thế: thêm Pretendo và GOG Preservation Program. Target: tách rõ *người có nhu cầu* (người chơi, cộng đồng) khỏi *người phải hành động/trả tiền* (nhà phát hành). Thêm phản chứng NNID. Sustainability 3/L → 3/M | Ba agent hội tụ độc lập vào cùng một vấn đề gốc. Bằng chứng của A (Pretendo, sổ đăng ký ECI) và C (thông báo của Nintendo/Capcom) bổ sung cho B (nội dung phản hồi EC, Homecoming, dữ liệu Nhật) | A, C, own |
| B-O2 | **revised**; liền kề A-O2 (khác giai đoạn), không gộp | Phản chứng: Cohost là nền tảng nhỏ. Phương án thay thế: thêm Mastodon export/move. B-O2-C5 → INFERENCE | B-O2 xét *nhà vận hành trước khi đóng cửa*; A-O2 xét *người dùng sau khi có file export*. Hai hướng khác giả thuyết nên không gộp | A, own |
| B-O3 | **withdrawn**; gộp vào C-O1 | — | C đã kiểm tra các phương án thay thế mà tôi bỏ sót (JASPER, PKP PN, Keepers) và đọc kết quả của Eve thận trọng hơn. Bằng chứng của C mạnh hơn | C |
| B-O4 | **revised** | Phương án thay thế: thêm tái phát hành thương mại G-MODE/Appli Archives. Sustainability 1 → 2. Ba claim → INFERENCE | Có bằng chứng chi tiêu cho nội dung keitai (B-R8); chưa xác nhận độc lập được | own |
| B-O5 | **revised**; liền kề A-O3, không gộp | `ai` 5/M → 4/L; B-O5-C1/C2 → INFERENCE. Phản chứng: thêm việc baseline còn thiếu | Yêu cầu của Coordinator về tính cần thiết của AI; tự kiểm tra lại | own |

## 6. Positions I keep despite challenge

1. **B-O5 có thể là trường hợp duy nhất AI thực sự load-bearing** (đi ngược nhận định chung của C-G-C22 và hướng của A §7).
   - Phản biện mạnh nhất: bằng chứng chỉ là một blog với n=60 và không có baseline; DecompileBench cho thấy LLM kém về tính đúng chức năng.
   - Lý do tôi giữ: oracle khớp byte là **kiểm chứng cơ học tuyệt đối**, khác hẳn oracle "boot không crash" của A-O3 hay "toàn vẹn tham chiếu" của A-O2. Ràng buộc DecompileBench chỉ nói về decompile *không có* oracle. Tôi giữ ở mức GIẢ THUYẾT, có falsifier rõ ràng, và đã hạ điểm `ai`.
2. **Giữ B-O4 (keitai) là không gian riêng, không gộp vào A-O5/C-O3.**
   - Phản biện mạnh nhất: legal risk cao, sustainability thấp, chỉ có một nguồn.
   - Lý do tôi giữ: B-O4 là cơ hội duy nhất trong nhóm "di sản" có **theme 5** (i-mode đã chấm dứt dịch vụ), và có bằng chứng tái phát hành thương mại. A-O5/C-O3 là về quản trị đồng thuận, không có công nghệ chết làm neo (cả hai tự chấm theme ≤2).
3. **Suy giảm người dùng là triệu chứng chứ không phải nguyên nhân gốc** (B-G-C1). A (§2) và C (C-G-C2) đi tới kết luận tương tự; chưa agent nào phản bác.
4. **"Bảo tồn trước khi chết rẻ hơn hồi sinh sau khi chết"** (B-G-C17).
   - Phản biện có thể có: Pretendo cho thấy hồi sinh sau khi chết vẫn làm được.
   - Lý do tôi giữ: Pretendo không lấy lại được NNID (N2), tức một phần giá trị mất vĩnh viễn. Cohost cần nhà vận hành hợp tác ngay trong lúc đang đóng cửa (N5).

## 7. Remaining disagreements

| Bất đồng | Các bên | Bằng chứng sẽ giải quyết |
|---|---|---|
| AI có load-bearing ở A-O2 không | A vs B | Lấy 3 file export thật (Mastodon AS2.0, export Cohost, 1 SaaS không có tài liệu). So parser viết tay theo tài liệu với cách AI suy luận schema: đo độ chính xác ngữ nghĩa trên mẫu gán nhãn tay, không chỉ đo toàn vẹn tham chiếu |
| AI có load-bearing ở A-O3 không | A vs B | Với 15 phần mềm cổ, so quét tất định (emulator × OS × boot check) với cấu hình do AI đề xuất; oracle là chạy hết một kịch bản tương tác, không chỉ boot |
| AI có load-bearing ở B-O5 không | B vs A/C | Chạy lại benchmark có baseline chỉ‑công‑cụ trên một dự án decomp khác (falsifier của B-O5) |
| Điểm `demand` của A-O1 và A-O4 | A vs B | A-O1: bằng chứng 2025–2026 rằng nhóm nghiên cứu/thư viện hành động (yêu cầu migration, chi tiêu). A-O4: bằng chứng ít nhất một nhà phát hành hoặc studio tự nguyện cam kết EOL sau phản hồi EC |
| Ngưỡng VERIFIED cho văn bản chính thức (loại ii) | B (và C, ngầm định) vs quy tắc chặt nhất | Coordinator quyết định văn bản chính thức là sự kiện tự thân có được VERIFIED hay không |
| C-O2: nhu cầu bàn giao maintainer | C vs B | Đối chiếu lịch sử maintainer của Pretendo và Homecoming (commit, thay người duy trì) để xem có sự cố kế nhiệm nào được ghi nhận |
| Gộp A-O5 với C-O3 | B đề xuất | Synthesis xác nhận hai cơ hội có cùng JTBD (giữ quyền/đồng thuận khi lưu trữ hoặc chuyển giao) |

## 8. New references

Thang điểm và công thức tính giống Round 1. Ngày truy cập là 2026-11-25 cho tất cả.

| Ref | URL | Title | Publisher | Pub date | Accessed | Opened / snippet | Claims | Auth | Tech | Mech | Ctx | Fresh | Repro | Bias | Weighted | Src Rel | Ref Rel |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| N1 | https://www.heise.de/en/news/Citizens-initiative-1-294-188-signatures-for-Stop-Destroying-Videogames-11154579.html | Citizens' initiative: 1,294,188 signatures for "Stop Destroying Videogames" | heise online | 2026-01 | 2026-11-25 | Opened | B-O1-C1, A8, C-G-C19 | 4 | 3 | 4 | 5 | 5 | 4 | 4 | 81 | H | H |
| N2 | https://pretendo.network/ | Pretendo Network (homepage, FAQ, progress) | Pretendo Network | live 2026 | 2026-11-25 | Opened | C3, A-O4-C2, §3 | 3 | 4 | 4 | 5 | 5 | 4 | 3 | 80 | M | H |
| N3 | https://raw.githubusercontent.com/mastodon/documentation/main/content/en/user/moving.md | Moving or leaving accounts | Mastodon (official docs) | live 2026 | 2026-11-25 | Opened | A5, A-O2-C2 | 5 | 4 | 5 | 4 | 5 | 5 | 4 | 92 | H | H |
| N4 | https://www.softwarepreservationnetwork.org/eaasi-case-study-1-the-would-be-gentleman/ | EaaSI Case Study #1: The Would-Be Gentleman | Software Preservation Network | 2021-01 | 2026-11-25 | Opened | A6, A-O3-C1 | 4 | 4 | 4 | 4 | 2 | 3 | 4 | 74 | H | H |
| N5 | https://en.wikipedia.org/wiki/Cohost | Cohost | Wikipedia | sửa đổi 2026 | 2026-11-25 | Opened | B-G-C4, B-O2-C1, B-O2-C3, A10 | 3 | 3 | 4 | 4 | 5 | 4 | 5 | 75 | M | H |
| N6 | https://en.wikipedia.org/wiki/Tianya_Club | Tianya Club | Wikipedia | sửa đổi 2026-09-22 | 2026-11-25 | Opened | A10 | 3 | 2 | 3 | 3 | 5 | 3 | 5 | 62 | M | M |
| N7 | https://www.gog.com/en/gog-preservation-program | GOG Preservation Program | GOG | live 2026 | 2026-11-25 | Opened | §3 (phương án thay thế, WTP) | 4 | 3 | 3 | 4 | 5 | 4 | 1 | 71 | M | H |
| N8 | https://www.pcgamer.com/after-five-years-ncsoft-officially-grants-a-licence-to-popular-city-of-heroes-private-server-homecoming-your-accounts-and-characters-are-safe/ | After five years, NCSoft officially grants a licence to … Homecoming | PC Gamer | 2024-01 | 2026-11-25 | Opened | B-O1-C4, C1, §3 | 3 | 3 | 4 | 5 | 4 | 3 | 4 | 73 | M | H |
| N9 | https://microblogging.infodocs.eu/wp-content/uploads/2024/01/jlsc-16288-eve.pdf | Digital Scholarly Journals Are Poorly Preserved: A Study of 7 Million Articles (PDF mirror) | JLSC (Eve) / mirror | 2024-01 | 2026-11-25 | Opened (pdftotext) | B-O3-C1, C5 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 91 | H | M |
| N10 | https://doaj.org/preservation/ | JASPER — Preservation | DOAJ | live 2026 | 2026-11-25 | Opened | C4, C6, §3 | 5 | 4 | 5 | 5 | 5 | 4 | 5 | 94 | H | H |
| N11 | https://www.copyright.gov/1201/2024/2024_Section_1201_Registers_Recommendation.pdf | Section 1201 Rulemaking: Ninth Triennial Proceeding — Recommendation of the Register of Copyrights | U.S. Copyright Office | 2024-10 | 2026-11-25 | Opened (pdftotext) | B-G-C8, A7 | 5 | 5 | 5 | 4 | 4 | 5 | 5 | 95 | H | H |
