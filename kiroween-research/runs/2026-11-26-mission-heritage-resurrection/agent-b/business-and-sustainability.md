# Stage 1 — Agent B: Business Analysis & Sustainability

## Metadata

| Mục | Giá trị |
|---|---|
| Run | `2026-11-26-mission-heritage-resurrection`, Stage 1, Agent B |
| Model | `claude-sonnet-5-5` (do runtime tự báo trong system prompt; không có xác nhận độc lập theo từng request) |
| Effort | không quan sát được từ bên trong phiên |
| Bắt đầu / kết thúc (UTC, theo đồng hồ máy) | 2026-11-26 02:38:50 / 02:47 (theo `date -u` trong phiên; Coordinator nên đối chiếu với log của Orca) |
| Số truy vấn tìm kiếm | 23 (WebSearch) |
| Fetch trực tiếp (curl → text) | 41 lượt, 26 nguồn dùng trong báo cáo được mở trực tiếp |
| Nguồn: mở trực tiếp / chỉ snippet | **26 / 19** (bảng References) |
| Lỗi truy cập | perma.cc (403), opencollective.com (403), chinadigitaltimes.net (403), softwareheritage.org (HTTP 000, hết thời gian), trove.nla.gov.au (418), minister.infrastructure.gov.au (HTTP 000), brochure PDF của Software Heritage (PDF lỗi XRef, không trích được), digitalhumanities.org bản `www` (404; bản không `www` mở được), trang Palabra Clave (mở được nhưng không trích được nội dung bài) |
| Phạm vi | Chỉ miền B. Không đọc `agent-a/`, `agent-c/` của run này. Không sửa gì ngoài `agent-b/`. Không cài đặt, không commit |

---

## 1. Method

1. **Tái sử dụng trước, khám phá sau.** Đọc `stakeholder-analysis.md`, `hypotheses-validation-plan.md` (Task B), `opportunities.json` của ba agent Phase 3 (các trường `payer`, `maintainer`, `cases`) và sổ claim của báo cáo B Phase 3. Claim cũ được trích dưới dạng `P3:B-S2-C4`, `P3:B-T2-C2`…, và **không được chấm lại nhãn**.
2. **Chỉ thêm ca mới khi nhiệm vụ mới cần.** Mission mới đổi trọng tâm sang **người khám phá (explorer)** làm giá trị chính. Phase 3 hầu như chỉ có bằng chứng phía người đóng góp và người trả tiền. Vì vậy phần lớn tìm kiếm mới nhắm vào: (a) bằng chứng nhu cầu phía explorer; (b) mô hình tài chính của tổ chức bảo tồn hiện có, kể cả thất bại; (c) khung pháp lý theo vùng; (d) ca mới ở châu Á (gồm Việt Nam) và Mỹ Latinh, nơi Phase 3 còn mỏng.
3. **Chuỗi bằng chứng:** claim → nguồn gốc → xác nhận độc lập → kiểm tra cơ chế. Mỗi claim ghi đã đi tới bước nào ở sổ claim cuối §12 phần References.
4. **Nhãn.** ĐÃ XÁC MINH (VERIFIED) chỉ khi nguồn gốc được mở trực tiếp và có xác nhận độc lập, hoặc claim được giới hạn dạng "X chính thức tuyên bố Y". Claim chỉ dựa vào snippet tối đa là SUY LUẬN.
5. **Tách hành vi đã chứng minh khỏi nhu cầu giả định.** Hành vi tính được gồm lượt dùng, quyên góp, chữ ký kiến nghị, giờ tình nguyện, hợp đồng, thuê bao. Ý kiến, lời kêu gọi hay số liệu kho lưu (supply) không được tính là nhu cầu explorer.
6. **Không chấm điểm ứng viên.** Bốn mô hình vận hành B-M1…M5 là đầu vào cho Stage 3, không phải xếp hạng.

---

## 2. Documented cases

Bảng dưới gom ca cũ (tham chiếu claim Phase 3) và ca mới. Cột "Ai trả / ai làm" chỉ ghi điều nguồn nói.

### 2a. Website bị bỏ vì suy giảm sử dụng hoặc nền tảng đóng

| Vùng | Ca | Điều đã xảy ra | Ai trả / ai làm | Claim |
|---|---|---|---|---|
| Châu Á (Nhật) | GeoCities Japan | Yahoo! Japan báo đóng ngày 01/10/2018, tắt ngày 01/04/2019. ArchiveTeam crawl được 96 triệu URL, 3,7 TB, trạng thái "Partially saved" | Tình nguyện viên ArchiveTeam; Internet Archive lưu | **B-C1** |
| Châu Á (Việt Nam) | Yahoo! 360° và Yahoo! Blog Việt Nam | Năm 2009 Global Voices mô tả Yahoo! 360 là nền tảng blog phổ biến nhất Việt Nam; người dùng "lo lắng" khi có tin đóng. Bản kế nhiệm Yahoo! Blog cũng đóng: ngày 17/01/2013 Yahoo gửi email yêu cầu người dùng tải dữ liệu trước 09/03/2013 | Yahoo tự cung cấp công cụ tải xuống; không thấy ai lưu trữ hệ thống phần bình luận và quan hệ bạn bè | **B-C2**, **B-C3** |
| Châu Á (Trung Quốc) | Nội dung Internet Trung Quốc thời tiền-mobile | Bài viết của He Jiayan (05/2024) ước lượng hơn 99% nội dung đã biến mất; bài bị gỡ ngay sau đó. Nguyên nhân được nêu gồm chi phí lưu trữ của doanh nghiệp và kiểm duyệt | Không ai | **B-C4** |
| Toàn cầu | Link rot | Pew (05/2024): 38% trang tồn tại năm 2013 không còn truy cập được vào 2023; 25% trang của cả giai đoạn 2013–2023. Internet Archive phân tích lại: Wayback Machine "cứu" được khoảng 15% số trang đã chết | Internet Archive (quyên góp) | **B-C5**, **B-C6** |
| Bắc Mỹ | Cohost (2024–2025), Glitch (2025) | Đã có ở Phase 3 | Không ai trả cho nhà vận hành nhỏ | `P3:B-T2-C1`, `P3:B-T2-C2`, `P3:B-T2-C3` |

### 2b. Ứng dụng nghiên cứu bị bỏ sau khi hết grant

| Vùng | Ca | Điều đã xảy ra | Claim |
|---|---|---|---|
| Châu Âu (Anh) | King's Digital Lab (seed ref Smithies et al. 2019) | Năm tài chính 2016–2017, KDL tiếp nhận khoảng 100 dự án DH tích lũy trong 20 năm. Khoảng một nửa "chất lượng đặc biệt cao hoặc mang tính khai mở", nhưng gần như tất cả gặp vấn đề tài trợ và kỹ thuật. KDL mô tả "thế kẹt đạo đức" gồm ba lựa chọn: tắt dự án, duy trì miễn phí (tự gánh chi phí), hoặc chấp nhận rủi ro bảo mật | **B-C7** |
| Châu Âu (Anh) | KDL sau khi xử lý | KDL đưa SLA ký với PI vào quy trình. Các "sản phẩm lưu trữ" (static site, gỡ front-end, di trú dữ liệu, tắt có kiểm soát) được cân nhắc ngay từ khâu lấy yêu cầu, để thực hiện khi hết tiền | **B-C8** |
| Bắc Mỹ | FlyBase, TAIR | Đã có ở Phase 3 | `P3:B-S2-C4`, `P3:B-S2-C6` |
| Châu Á (Nhật) | PDBj SFAS | Đã có ở Phase 3 (ngừng 02/2024 vì thiếu nhân sự IT) | `P3:B-S2-C7` |
| Toàn cầu | 32/52 Global Core Biodata Resources phụ thuộc tiền liên bang Mỹ | Đã có ở Phase 3 | `P3:B-S2-C5` |

### 2c. Cộng đồng nhỏ đóng cửa

Ca Cohost, Yahoo!ブログ, Xiami, teacup, Soup.io đã có ở Phase 3 (`P3:B-T2-*`, C-T2). Ca mới duy nhất được thêm là Yahoo! 360 Việt Nam (B-C2, B-C3), vì đây là ca của chính thị trường người dùng nhóm dự án. Tôi không tìm thêm ca khác để tránh khám phá lại.

### 2d. Phần mềm bị khai tử

| Vùng | Ca | Điều đã xảy ra | Claim |
|---|---|---|---|
| Bắc Mỹ | Game cổ điển | VGHF và Software Preservation Network (07/2023), mẫu 1.500 game: 87% game cổ điển phát hành tại Mỹ không còn bán chính thức. Không giai đoạn nào vượt 20% | **B-C9** |
| Bắc Mỹ | Đồ họa Flash của New York Times | NYT dùng Ruffle để khôi phục các đồ họa tương tác Flash trong kho bài cũ. Trước đó chúng chỉ còn là ảnh tĩnh (01/2024) | **B-C10** |
| Toàn cầu | Flash, Java applet, Fusion Tables | Đã có ở Phase 3 (PhET, Fusion Tables) | `P3:B-S2-C8`, `P3:B-S2-C9` |
| Bắc Mỹ | Conifer (dịch vụ lưu trữ web có host của Rhizome) | Ngừng nhận tài khoản và thuê bao từ 15/12/2025, ngừng capture từ 05/2026, chuyển sang "tombstone app" từ 06/2026. Lý do: không còn tích hợp được công cụ Webrecorder mới. Người dùng được chọn: để Rhizome tiếp tục host, tải WACZ về tự host, chuyển sang Browsertrix, hoặc xóa | **B-C11** |

Conifer quan trọng với miền B vì nó là **chính một dịch vụ bảo tồn bị khai tử**. Mô hình hosted freemium (miễn phí kèm thuê bao) đã không bền với Rhizome, dù Rhizome là tổ chức có tài trợ. Đây là phản chứng trực tiếp cho mô hình B-M4.

### 2e. Bộ sưu tập di sản số thiếu nguồn lực

| Vùng | Ca | Điều đã xảy ra | Claim |
|---|---|---|---|
| Châu Đại Dương (Úc) | Trove, Thư viện Quốc gia Úc | Tài trợ liên bang cho Trove dự kiến hết ngày 30/06/2023; NLA cảnh báo sẽ đóng dịch vụ. Khoảng 30.000 chữ ký trong 5 e-petition. Tháng 04/2023 chính phủ cấp 33 triệu AUD cho 4 năm, kèm 9,2 triệu AUD/năm có chỉ số hóa từ 07/2027 | **B-C12** |
| Châu Âu (Anh) | UK Web Archive, British Library | Tấn công ransomware tháng 10/2023. Trang BL vẫn ghi "đang khôi phục chức năng đầy đủ". Theo nguồn thứ cấp, UK Web Archive nằm ngoài đợt khôi phục legal deposit điện tử và vẫn không truy cập được | **B-C13** |
| Châu Phi | African Digital Heritage | Tổ chức phi lợi nhuận này tự mô tả: "dựa vào tài trợ của nhà hảo tâm và tài trợ dự án để duy trì hoạt động" | **B-C14** |
| Mỹ Latinh | Archivo de la Web Chilena, Biblioteca Nacional de Chile | BN Chile tự mô tả là kho lưu web tiên phong tại Mỹ Latinh, dùng OpenWayback. Một bài tổng quan năm 2025 (snippet) nêu rào cản pháp lý, kỹ thuật và kinh tế trong khu vực, và cho biết chưa có nghiên cứu quốc tế vững về chủ đề này | **B-C15**, **B-C16** |
| Toàn cầu | Kho di sản Mukurtu, ELAR, PARADISEC | Đã có ở Phase 3 | `P3:B-T4-C1`…`C5` |

---

## 3. Stakeholder map

Mission tách hai nhóm. Bảng dưới giữ đúng cách tách đó và ghi rõ hành vi đã chứng minh với giả định.

### 3a. Explorer (người dùng chính theo mission)

| Explorer | Lợi ích kỳ vọng | Hành vi đã chứng minh | Có trả tiền? | Bằng chứng |
|---|---|---|---|---|
| Người dùng phổ thông tra trang đã chết | Tìm lại nội dung | Có, ở mức tổng: Internet Archive có quy mô truy cập lớn (snippet: "khoảng một triệu lượt truy cập mỗi ngày", OPB 2025) | Quyên góp chiếm 85,2% doanh thu IA năm tài chính 2025, nhưng không tách được phần đến từ explorer | B-C17, B-C18 |
| Người chơi và người hoài niệm Flash hay game | Trải nghiệm lại | Ruffle có 77.723 người dùng trên Firefox Add-ons (snippet); Flashpoint có hơn 190.000 game và animation (snippet) | Quyên góp (Flashpoint qua Open Collective; không mở được trang) | B-C19, B-C20 |
| Độc giả báo chí, người làm visualization | Xem lại đồ họa cũ | NYT chọn tự khôi phục (B-C10) | Chi phí do NYT tự chịu | B-C10 |
| Nhà nghiên cứu, sinh viên | Nguồn trích dẫn, so sánh lịch sử | Gián tiếp: 54% trang Wikipedia có ít nhất một link tham khảo đã chết (Pew). Đây là bằng chứng về **vấn đề**, không phải về hành vi dùng một nền tảng mới | Tổ chức (thư viện) trả | B-C5 |
| Công chúng ủng hộ một kho cụ thể | Giữ kho tồn tại | Khoảng 30.000 chữ ký cho Trove | Thuế (chính phủ) | B-C12 |
| Người xem triển lãm net art hay lịch sử web | Hiểu bối cảnh lịch sử | **Không tìm được số liệu lượt xem** cho Rhizome Net Art Anthology hay ArtBase | — | B-C21 |

### 3b. Contributor và beneficiary

| Bên | Đóng góp gì | Hành vi đã chứng minh | Ai trả | Ai bảo trì | Bằng chứng |
|---|---|---|---|---|---|
| Phòng lab DH và RSE ở đại học (KDL) | Toàn bộ dự án cũ | Tiếp nhận khoảng 100 dự án; ký SLA với PI | Ngân sách lab, SLA với PI | Lab | B-C7, B-C8 |
| Nhà nghiên cứu (PI) | Ứng dụng nghiên cứu | Nhiều PI tự chọn để dự án "chết gọn" (Phase 3) | Grant (đã hết) | Không ai | `P3:B-S2-C2` |
| Nhà xuất bản hay chủ nội dung | Nội dung của chính họ | NYT tự khôi phục bằng Ruffle | Chủ nội dung | Chủ nội dung | B-C10 |
| Nhà vận hành nền tảng sắp đóng | Export, thời gian hoãn tắt | Cohost hoãn tắt cho ArchiveTeam; Yahoo VN cho tải dữ liệu | Nhà vận hành (rất hạn chế) | — | `P3:B-T2-C2`, B-C3 |
| Tình nguyện viên lưu trữ khẩn cấp | Crawl | GeoCities JP 96 triệu URL; Cohost | Không ai (giờ công) | ArchiveTeam, IA | B-C1 |
| Cộng đồng bảo tồn (Flashpoint, Ruffle) | Bản sưu tập, emulator | Hơn 190.000 mục (snippet) | Quyên góp | Tình nguyện viên | B-C20 |
| Tổ chức GLAM và thư viện quốc gia | Crawl theo luật, bộ sưu tập | Archive-It, legal deposit, BN Chile, NLA | Ngân sách công, thuê bao | Tổ chức | B-C12, B-C15, B-C22 |
| Thực thể pháp lý hay luật sư | Trích dẫn ổn định | Perma.cc có gói trả phí cá nhân (snippet) | Cá nhân, tòa án, thư viện luật | Harvard LIL | B-C24 |

### 3c. Ma trận "ai làm gì"

| Vai trò | Explorer | Contributor | Tổ chức GLAM | Quỹ hay nhà nước |
|---|---|---|---|---|
| Hưởng lợi | Có (khuếch tán) | Có (danh tiếng, chứng cứ, tuân thủ) | Có (sứ mệnh) | Gián tiếp |
| Đóng góp artifact | Hiếm | **Chính** | Có (crawl) | Không |
| Trả tiền | **Không có bằng chứng ngoài quyên góp** | Chỉ khi có SLA hoặc nghĩa vụ pháp lý | Có (thuê bao, ngân sách) | Có (grant, ngân sách) |
| Bảo trì | Không | Thường bỏ khi hết tiền | Có | Không trực tiếp |

**Kết luận chính của §3 (B-C25, SUY LUẬN):** dòng tiền chạy theo hướng **contributor và tổ chức → dịch vụ capture**, và **công chúng → quyên góp cho kho đa năng**. Không tìm thấy dòng tiền nào từ explorer cho một **trải nghiệm khám phá được giám tuyển**. Mission đặt explorer làm giá trị chính, nhưng chính nhóm này lại có bằng chứng thanh toán yếu nhất.

---

## 4. Explorer-side demand evidence

| # | Bằng chứng | Loại | Nhãn | Ghi chú |
|---|---|---|---|---|
| 1 | Pew: 38% trang 2013 đã mất vào 2023 (B-C5) | Vấn đề tồn tại | ĐÃ XÁC MINH | Chứng minh **mất mát**, không chứng minh **mong muốn khám phá** |
| 2 | IA: Wayback cứu khoảng 15% trang đã chết (B-C6) | Mức bao phủ của giải pháp hiện có | ĐÃ XÁC MINH (scoped "IA tuyên bố") | Đọc theo hai chiều: 85% còn lại là khoảng trống, nhưng cũng là phần **không còn bản gốc nào để khôi phục** |
| 3 | IA khoảng một triệu lượt/ngày (B-C17) | Hành vi tổng | SUY LUẬN (snippet) | Không tách được người khám phá lịch sử khỏi người tra cứu trích dẫn |
| 4 | Quyên góp chiếm 85,2% doanh thu IA FY2025 (B-C18) | Hành vi chi tiền | ĐÃ XÁC MINH (scoped số liệu 990) | Người quyên góp gồm cả quỹ lớn; không chứng minh explorer cá nhân trả |
| 5 | Ruffle 77.723 user Firefox; Flashpoint hơn 190k mục (B-C19, B-C20) | Hành vi tự cài, tự sưu tập | SUY LUẬN (snippet) | Cho thấy cộng đồng ngách có thật; **nhu cầu đã được phục vụ** bởi công cụ miễn phí |
| 6 | NYT tự khôi phục Flash (B-C10) | Hành vi của chủ nội dung | SUY LUẬN | Chủ nội dung tự làm, không thuê bên thứ ba |
| 7 | Khoảng 30.000 chữ ký cho Trove (B-C12) | Vận động chính sách | SUY LUẬN (snippet) | Người dùng bảo vệ một kho **đang dùng**, không đòi một kho mới |
| 8 | Lượt xem triển lãm net art hay lịch sử web giám tuyển (B-C21) | — | CHƯA RÕ | Truy vấn: "Rhizome Net Art Anthology funding visitors ArtBase preservation". Không có số liệu |
| 9 | Nhu cầu "so sánh quá khứ với hiện tại" | — | CHƯA RÕ | Không truy vấn riêng; đây là câu hỏi cho Agent A (Q-A1) |

**Đánh giá (B-C26, SUY LUẬN):** nhu cầu explorer **đã được chứng minh ở mức tổng quát** (Wayback, Flash, game), và **đang được phục vụ bởi các bên miễn phí, rất lớn** (IA với 1,3 triệu tựa phần mềm "nhiều cái chạy giả lập được" theo IA tự báo, B-C27; Flashpoint; Ruffle). Chưa có bằng chứng về nhu cầu cho **một nền tảng khám phá mới**, và tôi không giả định nhu cầu đó tồn tại.

---

## 5. Existing preservation institutions and funding models

| Tổ chức | Mô hình | Con số hoặc cơ chế | Rủi ro hay thất bại đã ghi nhận | Claim |
|---|---|---|---|---|
| Internet Archive (Mỹ) | Phi lợi nhuận, quyên góp, kèm dịch vụ (Archive-It, số hóa) | FY2025 (ProPublica, trích từ 990): doanh thu 23,71 triệu USD, chi 27,77 triệu USD, lỗ ròng 4,06 triệu USD. Quyên góp 20,19 triệu USD (85,2%), dịch vụ chương trình 7,54 triệu USD. Hơn 210 PB dữ liệu duy nhất, tăng khoảng 20%/năm | Thâm hụt năm FY2025; chi phí năm trước dao động 23,5–32,7 triệu USD (`P3`, R20 cũ) | B-C18, B-C27 |
| Archive-It (IA) | Thuê bao tổ chức, tính theo dung lượng capture mỗi năm | COPPUL 2024–2025: 2.100 USD/128 GB … 16.800 USD/2 TB. FAQ (snippet): dữ liệu các năm trước được lưu không tính thêm phí | Giá tăng mạnh so với brochure 2021 (500 USD/128 GB, snippet) | B-C22 |
| Webrecorder Browsertrix | SaaS cho cá nhân và tổ chức | 30 / 60 / 120 USD/tháng cho 100 / 220 / 500 GB đĩa và 180 / 360 / 720 phút chạy | Không rõ doanh thu | B-C23 |
| Perma.cc (Harvard LIL) | Freemium; registrar thư viện và tòa án miễn phí, cá nhân trả | 10 USD/10 link, 25 USD/100, 100 USD/500 mỗi tháng (snippet) | Đã bỏ gói miễn phí định kỳ năm 2019 (snippet) | B-C24 |
| Rhizome Conifer | Hosted freemium kèm thuê bao | Đóng giai đoạn 2025–2026 | **Thất bại mô hình đã ghi nhận** | B-C11 |
| Software Heritage (Pháp, Inria, UNESCO) | Liên minh nhà tài trợ, kèm grant | Tầng thành viên nhóm thư viện từ 2.000 đến 50.000 EUR/năm (snippet). Sloan cấp 575.000 USD cho công cụ dựa trên SWH | Không có ngân sách công khai (snippet) | B-C28, B-C29 |
| Trove (NLA, Úc) | Ngân sách công | 33 triệu AUD/4 năm sau khủng hoảng 2023 | Suýt đóng vì quyết định chính trị | B-C12 |
| British Library, UKWA | Legal deposit, ngân sách công | — | Ransomware; UKWA không truy cập được kéo dài | B-C13 |
| King's Digital Lab | SLA trong đại học | SLA với PI; sản phẩm lưu trữ lên kế hoạch từ đầu | Phải chọn giữa tắt, gánh chi phí và rủi ro bảo mật | B-C7, B-C8 |
| Arweave (permaweb) | Trả một lần, quỹ endowment | ArDrive: phí lần đầu trả cho 200 năm, giả định giá lưu trữ giảm 0,5%/năm | Phê bình (snippet, nguồn web3 không trung lập): endowment phụ thuộc giá token AR | B-C30, B-C31 |
| Rhizome ArtBase, Net Art Anthology | Quỹ tư nhân, Google Arts & Culture | (snippet) | — | B-C32 |
| African Digital Heritage | Donor và tài trợ dự án | Tự mô tả | Phụ thuộc donor | B-C14 |

**Quan sát về kinh tế đơn vị (B-C33, SUY LUẬN, ước tính):**

- Chi phí toàn phần của IA chia cho dữ liệu: 27,77 triệu USD / 210 PB ≈ **0,13 USD/GB/năm**. Con số này gồm mọi hoạt động (số hóa sách, nhân sự, pháp lý), không chỉ lưu trữ. Giả định: 1 PB = 10⁶ GB; dùng chi phí FY2025 và dung lượng do IA tự báo cho năm 2025.
- Giá Archive-It qua COPPUL: 2.100 USD / 128 GB ≈ **16,4 USD/GB** capture trong năm đầu, và các năm sau lưu tiếp miễn phí.
- Hai con số chênh nhau khoảng **100 lần**. Suy luận: phần tốn tiền là **capture, QA, công cụ, hỗ trợ và giám tuyển**, không phải đĩa lưu. Agent C cần kiểm tra lại (Q-C1).

**Điều chỉnh H0 của Task B (B-C34, SUY LUẬN):** Phase 3 kết luận "không thấy ai trả tiền cho **công cụ** bảo tồn của bên thứ ba". Kết luận đó cần thu hẹp lại. **Có** thị trường trả tiền cho **dịch vụ capture web** (Archive-It, Browsertrix, Perma.cc), với người mua là tổ chức GLAM, nhà nghiên cứu và người làm luật. Điều vẫn **không** tìm thấy là người trả tiền cho (a) cứu chức năng của ứng dụng cụ thể sau grant; (b) trải nghiệm khám phá phía explorer.

---

## 6. Operating model alternatives

Mỗi mô hình là **giả thuyết vận hành**, không phải khuyến nghị. Cost driver được nêu định tính; số liệu tính toán chi tiết thuộc Agent C.

### B-M1 · Phi lợi nhuận dựa trên quyên góp (kiểu Internet Archive)

| Mục | Nội dung |
|---|---|
| Ai trả | Cá nhân và quỹ quyên góp; một phần từ dịch vụ |
| Cost driver | Lưu trữ tăng khoảng 20%/năm (B-C27); nhân sự; pháp lý |
| Failure mode | Thâm hụt (FY2025 lỗ 4,06 triệu USD, B-C18); phụ thuộc vài nhà tài trợ lớn (CHƯA RÕ cơ cấu); quy mô cần thiết để gây quỹ hiệu quả |
| Ví dụ thật | Internet Archive, Flashpoint (Open Collective, không mở được), Software Heritage một phần |
| Phản chứng mạnh nhất | Vị trí này đã có chủ. Một tổ chức mới phải cạnh tranh tiền quyên góp với IA, vốn đã có thương hiệu và kho lớn hơn nhiều bậc |

### B-M2 · Cộng đồng tự vận hành (kiểu ArchiveTeam, Flashpoint, Ruffle)

| Mục | Nội dung |
|---|---|
| Ai trả | Giờ tình nguyện; quyên góp nhỏ cho hosting |
| Cost driver | Băng thông và lưu trữ do IA hay cộng đồng gánh; giờ người |
| Failure mode | Kiệt sức; không có SLA; rủi ro pháp lý với nội dung có bản quyền (game: ESA phản đối, B-C35) |
| Ví dụ thật | GeoCities JP (B-C1), Cohost (`P3:B-T2-C2`), Flashpoint (B-C20) |
| Phản chứng mạnh nhất | Cộng đồng đã tự tổ chức mà không cần nền tảng mới. Một nền tảng thêm vào có thể chỉ là một lớp trung gian thừa |

### B-M3 · Tổ chức, liên minh hoặc legal deposit (kiểu Trove, UKWA, KDL, Software Heritage)

| Mục | Nội dung |
|---|---|
| Ai trả | Ngân sách công; phí thành viên; SLA nội bộ đại học |
| Cost driver | Nhân sự chuyên môn; tuân thủ; bảo mật |
| Failure mode | Quyết định chính trị cắt tiền (Trove, B-C12; FlyBase, `P3:B-S2-C4`); một sự cố làm sập toàn bộ (BL, B-C13) |
| Ví dụ thật | NLA Trove, BL UKWA, BN Chile (B-C15), KDL SLA (B-C8), SWH sponsor (B-C28) |
| Phản chứng mạnh nhất | Một sản phẩm hackathon không thể trở thành tổ chức. Phương án duy nhất khả thi là trở thành **công cụ hay quy trình** mà tổ chức chọn dùng, và vì vậy quay lại câu hỏi H0 |

### B-M4 · Freemium hay SaaS capture (kiểu Archive-It, Browsertrix, Perma.cc)

| Mục | Nội dung |
|---|---|
| Ai trả | Tổ chức và cá nhân chuyên nghiệp trả theo dung lượng hoặc theo link |
| Cost driver | Crawl tính bằng phút máy (Browsertrix tính phút chạy, B-C23); hỗ trợ; lưu trữ vĩnh viễn kèm theo |
| Failure mode | **Conifer đóng** (B-C11). Gói miễn phí bị cắt (Perma.cc, B-C24). Lưu trữ "vĩnh viễn" là cam kết đuôi dài không có doanh thu tương ứng |
| Ví dụ thật | Archive-It (B-C22), Browsertrix (B-C23), Perma.cc (B-C24) |
| Phản chứng mạnh nhất | Thị trường đã có ba nhà cung cấp trưởng thành, và người trả là **phía capture**, không phải explorer. Mô hình này phục vụ mission phụ (bảo tồn cho contributor), không phải mission chính |

### B-M5 · Bring-your-own-storage (BYOS): nền tảng chỉ giữ chỉ mục và trình phát

| Mục | Nội dung |
|---|---|
| Cơ chế | Contributor giữ gói tự chứa (ví dụ WACZ) trên lưu trữ của mình: S3, máy chủ đại học, IPFS hay Arweave. Nền tảng chỉ lưu metadata, chỉ mục và giao diện phát lại phía client |
| Ai trả | Contributor trả lưu trữ của mình; nền tảng chỉ trả chỉ mục và phát lại tĩnh |
| Cost driver | Thấp ở phía nền tảng (giả định, Q-C2); toàn bộ rủi ro lưu trữ chuyển sang contributor |
| Failure mode | **Link rot quay lại**: lưu trữ của contributor chính là thứ sẽ biến mất khi họ hết tiền, đúng vấn đề gốc (B-C5). Với Arweave: rủi ro token và endowment (B-C31) |
| Ví dụ thật | Phương án "tải về và tự host, đặt redirect" mà Conifer đưa ra cho người dùng (B-C11); Arweave và ArDrive (B-C30) |
| Phản chứng mạnh nhất | BYOS tối ưu chi phí cho nền tảng bằng cách chuyển rủi ro sang chính bên ít khả năng duy trì nhất. Nếu không có bản sao dự phòng (ví dụ gửi kèm vào IA hay một tổ chức), mô hình này mâu thuẫn với mục tiêu "khôi phục độc lập" |

### So sánh nhanh

| | M1 Quyên góp | M2 Cộng đồng | M3 Tổ chức | M4 SaaS | M5 BYOS |
|---|---|---|---|---|---|
| Có người trả đã chứng minh | Có (IA) | Rất ít | Có (công) | **Có** (capture) | Một phần (Arweave; quy mô CHƯA RÕ) |
| Phục vụ explorer | Có | Có | Có | Không trực tiếp | Có nếu có trình phát |
| Rủi ro tồn tại đã ghi nhận | Thâm hụt | Kiệt sức, pháp lý | Chính trị, sự cố | Đóng dịch vụ (Conifer) | Link rot của contributor |
| Phù hợp sản phẩm mới, nhóm nhỏ | Thấp | Trung bình | Thấp | Thấp (thị trường đã đông) | **Trung bình đến cao** về chi phí; thấp về độ bền |

**Đề xuất cho Stage 3 (B-C36, GIẢ THUYẾT):** mô hình ít mâu thuẫn nhất với bằng chứng là **lai M5 với M3**. Nền tảng làm lớp khám phá, chỉ mục và phát lại phía client, không host bản gốc. Bản gốc được gửi vào kho có nghĩa vụ bảo tồn sẵn có (IA, Software Heritage, thư viện quốc gia), hoặc do contributor giữ. Tính bền vững của nền tảng khi đó chỉ phụ thuộc chi phí chỉ mục và web tĩnh. Mô hình này **chưa có ví dụ thật nào được chứng minh**.

---

## 7. Why use this instead of existing archives

| Giá trị một nền tảng mới có thể cung cấp | Giải pháp đã có | Khoảng trống còn lại (giả thuyết) | Nhãn |
|---|---|---|---|
| Tìm trang đã chết | Wayback (bao phủ khoảng 15% trang đã chết, B-C6) | Không giải được: thứ không được capture thì không khôi phục được | B-C6 ĐÃ XÁC MINH |
| Chạy lại Flash hay phần mềm cũ | IA Emularity kèm Ruffle; Flashpoint; NYT tự làm (B-C10, B-C27) | Rất nhỏ với Flash. Lớn hơn với ứng dụng có backend (Q-C3) | SUY LUẬN |
| Giám tuyển, bối cảnh, so sánh quá khứ với hiện tại | Rhizome Net Art Anthology (100 tác phẩm); bài blog IA | **Có thể có**: Wayback là công cụ tra cứu, không phải trải nghiệm có câu chuyện. Chưa có bằng chứng explorer muốn điều này (B-C21) | GIẢ THUYẾT |
| Bảo tồn theo yêu cầu của chủ sở hữu | Archive-It, Browsertrix, Perma.cc, KDL SLA | Nhỏ với web tĩnh; lớn hơn với chức năng ứng dụng | SUY LUẬN |
| Đáng tin cậy lâu dài | IA đã 30 năm | Một nền tảng mới **kém tin cậy hơn** IA về mặt này | B-C37 SUY LUẬN |

**Kết luận §7 (B-C37, SUY LUẬN):** lý do duy nhất chưa bị bác bỏ là **trải nghiệm giám tuyển và so sánh** dựa trên dữ liệu của các kho đã có. Một nền tảng mới thua IA về độ bền, quy mô và độ tin cậy. Vì vậy nó không nên cạnh tranh ở tầng lưu trữ, mà nên **xây trên** các kho đó. Điểm này cần Agent A xác nhận về phía trải nghiệm (Q-A1, Q-A2).

---

## 8. Selection: what deserves preservation, and who decides

| Cơ chế chọn | Ai quyết | Ví dụ | Hệ quả kinh tế |
|---|---|---|---|
| Thu thập toàn bộ theo luật | Nhà nước (legal deposit) | NDL WARP (Phase 3), BL, BN Chile | Không cần chọn; chi phí công |
| Thu thập rộng tự động | Tổ chức (IA) | Wayback | Rẻ trên mỗi GB, nhưng chỉ khoảng 15% trang chết được cứu |
| Đánh giá chất lượng và tác động | Lab cùng PI, theo SLA | KDL: khoảng một nửa trong 100 dự án được đánh giá chất lượng cao (B-C7) | Chọn lọc để giới hạn chi phí bảo trì |
| Giám tuyển nghệ thuật | Curator | Rhizome ArtBase (hơn 2.200 tác phẩm, snippet), Net Art Anthology (100 tác phẩm) | Nhỏ, sâu, tốn công |
| Khẩn cấp, cộng đồng | Tình nguyện viên | ArchiveTeam GeoCities JP | Không chọn, cứu được gì thì cứu |
| Đồng thuận hay giao thức văn hóa | Cộng đồng nguồn | Mukurtu, Local Contexts TK Labels (B-C38) | Mặc định hạn chế truy cập |
| Do chủ sở hữu khởi xướng | Contributor | NYT; Conifer users | Chỉ những ai còn nguồn lực |

**Tiêu chí đề xuất cho Stage 3 (B-C39, GIẢ THUYẾT):** một artifact đáng được nền tảng ưu tiên khi đồng thời (1) có giá trị đã được ghi nhận: trích dẫn, giải thưởng, được curator chọn, hoặc tạo bước ngoặt công nghệ; (2) bị đe dọa bởi một **công nghệ đã khai tử có ngày chính thức**, khớp với anchor theme; (3) có quyền sử dụng rõ ràng hoặc giấy phép từ chủ sở hữu; (4) có **người bảo trợ ngoài nền tảng** giữ bản gốc. Tiêu chí (4) xuất phát trực tiếp từ bài học của KDL (B-C8) và Conifer (B-C11).

Cảnh báo: chọn lọc là nơi thiên lệch vùng và ngôn ngữ xuất hiện. Bằng chứng ở §11 cho thấy hạ tầng lưu trữ tập trung ở Bắc Mỹ, châu Âu và Nhật Bản.

---

## 9. Copyright, privacy, consent and cultural restrictions

| Khu vực | Quy định hay sự kiện | Ý nghĩa cho nền tảng | Nhãn |
|---|---|---|---|
| Mỹ | Copyright Office (10/2024) **không** cấp miễn trừ §1201 cho thư viện cung cấp truy cập từ xa tới game đã ngừng bán. Theo VGHF, ESA tuyên bố "sẽ không bao giờ ủng hộ truy cập từ xa cho nghiên cứu dưới bất kỳ điều kiện nào". Phần mềm không phải game được truy cập từ xa từ 2021, giới hạn một người một lúc (snippet) | Game là vùng rủi ro pháp lý cao nhất cho trải nghiệm "chơi lại online" | B-C35 ĐÃ XÁC MINH (scoped "VGHF tuyên bố"); chi tiết 2021 SUY LUẬN |
| EU | DSM Directive 2019/790 Điều 6: ngoại lệ **bắt buộc** cho tổ chức di sản văn hóa sao chép tác phẩm trong **bộ sưu tập thường trực** để bảo tồn (snippet nội dung) | Ngoại lệ chỉ áp dụng cho CHI và chỉ cho việc sao chép bảo tồn, **không** cho truy cập công khai. Một nền tảng tư nhân có lẽ không đủ điều kiện là CHI | B-C40 SUY LUẬN |
| EU | GDPR Điều 17(3)(d): quyền xóa không áp dụng cho lưu trữ vì lợi ích công cộng, nghiên cứu khoa học hay lịch sử **theo Điều 89(1)**, trong chừng mực việc xóa làm mục đích đó không thể đạt được | Lưu trang có dữ liệu cá nhân (diễn đàn, blog) cần biện pháp bảo vệ theo Điều 89. Việc một nền tảng tư nhân có được coi là "lưu trữ vì lợi ích công cộng" hay không thì CHƯA RÕ | B-C41 ĐÃ XÁC MINH (scoped văn bản); khả năng áp dụng CHƯA RÕ |
| Nhật Bản | Luật Bản quyền Điều 43: giới hạn quyền để NDL sao chép tài liệu Internet theo Luật NDL (snippet CRIC) | Đặc quyền thuộc về NDL, không phải bên tư nhân | B-C42 SUY LUẬN |
| Việt Nam | Thư viện Quốc gia nhận lưu chiểu; lưu chiểu điện tử cho báo chí do Bộ TT&TT thực hiện. **Không tìm thấy chương trình lưu trữ web quốc gia.** Nghị định 13/2023 về bảo vệ dữ liệu cá nhân được báo là bị thay bằng Nghị định 356/2025 từ 01/01/2026 (snippet) | Lưu trữ blog cũ của người Việt (Yahoo! 360) chạm vào dữ liệu cá nhân, và không có ngoại lệ lưu trữ nào được tìm thấy | B-C43 SUY LUẬN; chương trình web archive: CHƯA RÕ |
| Trung Quốc | Kiểm duyệt là một nguyên nhân mất nội dung (B-C4) | Truy cập và lưu trữ xuyên biên giới có rủi ro chính trị | SUY LUẬN |
| Bản địa (toàn cầu) | CARE Principles; Local Contexts TK/BC Labels (snippet); Mukurtu (Phase 3) | Mặc định hạn chế; bản sao công khai có thể gây hại (`P3`: A-G-C3, B-G-C3) | B-C38 SUY LUẬN |
| Kiroween | Bài nộp không được vi phạm quyền sở hữu trí tuệ hoặc quyền riêng tư của người khác. Repo phải công khai và có giấy phép nguồn mở. Tiêu chí Potential Impact hỏi "Would someone actually use this?" | Demo **chỉ dùng nội dung có quyền rõ ràng**: nội dung của chính nhóm, giấy phép mở, hoặc có đồng ý bằng văn bản | B-C44 ĐÃ XÁC MINH (scoped "rules chính thức nêu") |

**Kết luận §9 (B-C45, SUY LUẬN):** ở mọi khu vực đã xem, đặc quyền pháp lý để sao chép bảo tồn thuộc về **tổ chức di sản và thư viện quốc gia**, không thuộc về nền tảng tư nhân. Điều này củng cố hướng B-M5/M3 ở §6: nền tảng nên dẫn tới, chỉ mục hoặc phát lại nội dung **từ kho có đặc quyền**, hoặc nội dung **do chủ sở hữu tự đưa lên**, thay vì tự sao chép.

---

## 10. Adoption barriers

| # | Rào cản | Bên chịu | Bằng chứng | Nhãn |
|---|---|---|---|---|
| 1 | **Thời điểm cần cũng là lúc hết tiền.** Contributor nghĩ tới bảo tồn khi grant hay doanh thu đã cạn | Contributor | KDL (B-C7); Cohost (`P3:B-T2-C1`) | ĐÃ XÁC MINH (KDL) |
| 2 | Lựa chọn "để chết gọn" là hợp lý với nhiều PI | Contributor | `P3:B-S2-C2` | ĐÃ XÁC MINH (scoped) |
| 3 | Đối thủ miễn phí và mạnh: IA, Flashpoint, Ruffle | Explorer | B-C27, B-C20, B-C19 | SUY LUẬN |
| 4 | Thiếu niềm tin vào độ bền của nền tảng mới, sau khi chính dịch vụ bảo tồn (Conifer) cũng đóng | Cả hai | B-C11 | ĐÃ XÁC MINH |
| 5 | Pháp lý: game và phần mềm thương mại | Explorer | B-C35 | ĐÃ XÁC MINH (scoped) |
| 6 | Dữ liệu cá nhân trong cộng đồng cũ (blog, diễn đàn) | Contributor, nền tảng | B-C41, B-C43 | SUY LUẬN |
| 7 | Phần không capture được thì không khôi phục được; khoảng 85% trang chết không có bản lưu | Explorer | B-C6 | ĐÃ XÁC MINH (scoped) |
| 8 | Ngôn ngữ và vùng: hạ tầng lưu trữ và giám tuyển tập trung ở Bắc Mỹ, EU, Nhật | Explorer ngoài các vùng đó | §11 | SUY LUẬN |
| 9 | Explorer chưa chứng minh sẵn sàng trả tiền hay quay lại thường xuyên | Nền tảng | §4 | CHƯA RÕ |

---

## 11. International relevance

| Vùng | Ca và bằng chứng | Mức bằng chứng | Khoảng trống |
|---|---|---|---|
| **Bắc Mỹ** | IA (B-C18, B-C27); VGHF 87% (B-C9); NYT kèm Ruffle (B-C10); Conifer (B-C11); FlyBase, TAIR (`P3`) | Mạnh, nhiều nguồn mở trực tiếp | Nhu cầu explorer cho trải nghiệm giám tuyển |
| **Châu Âu** | KDL (B-C7, B-C8); BL/UKWA (B-C13); DSM Điều 6, GDPR (B-C40, B-C41); Software Heritage (B-C28) | Mạnh về pháp lý và tổ chức | Số liệu sử dụng của UKWA sau sự cố |
| **Châu Á – Nhật** | GeoCities JP (B-C1); NDL Điều 43 (B-C42); PDBj (`P3`) | Trung bình | — |
| **Châu Á – Việt Nam** | Yahoo! 360 và Yahoo! Blog (B-C2, B-C3); pháp lý (B-C43) | Yếu đến trung bình | Không tìm thấy chương trình lưu trữ web quốc gia. Không có số liệu về lượng blog Yahoo 360 đã mất. Truy vấn: "Vietnam national library web archiving legal deposit electronic publications Nghị định 13/2023…", "Yahoo! 360 Vietnam closure 2009 blogs lost users" |
| **Châu Á – Trung Quốc** | He Jiayan 2024 (B-C4) | Yếu (snippet; nguồn dịch bị chặn 403) | Nghiên cứu định lượng |
| **Châu Đại Dương** | Trove (B-C12) | Trung bình (nhiều snippet nhất quán; trang gốc bị 418) | — |
| **Mỹ Latinh** | BN Chile (B-C15); tổng quan khu vực 2025 (B-C16, snippet) | Yếu | Không có ca đóng cửa cụ thể. Truy vấn: "archivo web América Latina preservación sitios web desaparecidos biblioteca nacional México archivo web" |
| **Châu Phi** | African Digital Heritage dựa vào donor (B-C14) | Yếu | **Không tìm thấy ca kho di sản số châu Phi đóng vì hết tiền.** Truy vấn: "African digital heritage archive website lost funding ended offline case" |

**Kết luận §11 (B-C46, SUY LUẬN):** vấn đề mất nội dung số mang tính toàn cầu (Pew, He Jiayan, GeoCities JP, Yahoo VN). Nhưng **năng lực bảo tồn** (legal deposit web, emulator, SaaS capture) tập trung ở Bắc Mỹ, EU, Nhật và Úc. Nơi có chênh lệch lớn nhất giữa mất mát và năng lực, như Việt Nam, Trung Quốc, Mỹ Latinh và châu Phi, cũng là nơi bằng chứng mỏng nhất và người trả tiền ít nhất. Ý nghĩa quốc tế có thật ở phía **vấn đề**. Ở phía **mô hình bền vững** thì chưa được chứng minh.

---

## 12. Validation experiments

Mỗi thí nghiệm: giả thuyết, phép thử nhỏ nhất có thể bác bỏ, công sức (ước lượng, SUY LUẬN), tiêu chí dừng. Không thí nghiệm nào đã chạy.

| ID | Giả thuyết | Phép thử nhỏ nhất | Công sức | Kill criterion |
|---|---|---|---|---|
| **V1** | Explorer muốn trải nghiệm **so sánh quá khứ với hiện tại có giám tuyển**, chứ không chỉ tra Wayback | Landing page kèm 3 câu chuyện mẫu dùng nội dung có quyền. Đăng ở 2 cộng đồng (một tiếng Anh, một tiếng Việt). Đo click-through, thời gian xem và đăng ký nhận tin | 1–1,5 ngày | Ít hơn 2% người xem bấm vào câu chuyện, hoặc dưới 20 đăng ký sau 72 giờ. Ngưỡng tùy ý, cần Coordinator chốt trước |
| **V2** | Khoảng trống so với IA/Flashpoint/Ruffle đủ lớn | Lấy 20 artifact ứng viên (Flash, applet, web app DH). Kiểm tra mỗi cái đã có bản chạy được trên IA, Flashpoint hoặc bản tự khôi phục của chủ hay chưa | 0,5–1 ngày | ≥ 80% đã chạy được ở nơi khác. Trùng với phép thử Phase 3 |
| **V3** | Contributor (PI, chủ site) sẽ **đóng góp** gói khi được hướng dẫn | Gửi thư cho 15 chủ dự án DH hay web app đã ngưng (từ KDL, Endings, danh sách Phase 3), mời gửi gói lưu trữ kèm giấy phép | 1 ngày gửi, 3–5 ngày chờ | Dưới 2 phản hồi đồng ý trên 15 |
| **V4** | BYOS (B-M5) không làm link rot quay lại | Kiểm tra trạng thái các collection Conifer đã "tự host kèm redirect" sau 6 tháng (nếu có danh sách công khai); hoặc tỷ lệ URL tự host trong một mẫu WACZ được chia sẻ công khai còn sống | 0,5 ngày | > 20% liên kết tự host đã chết sau ≤ 12 tháng |
| **V5** | Có tổ chức sẵn sàng trả hoặc cam kết giữ bản gốc cho nền tảng (lai M3) | Hỏi 5 tổ chức (một thư viện đại học, SWH, IA/Archive-It, một thư viện quốc gia châu Á, Rhizome) về khả năng nhận bản sao. Chỉ dùng kênh công khai | 1 ngày kèm thời gian chờ | Không tổ chức nào có quy trình nhận |
| **V6** | Có ít nhất một bộ nội dung **có quyền rõ ràng** đủ hấp dẫn cho demo | Kiểm kê nội dung giấy phép mở (CC, public domain, tác phẩm của chính nhóm) gắn với công nghệ đã khai tử | 0,5 ngày | Không tìm được bộ nào đủ cho 3 câu chuyện demo. Khi đó concept vi phạm rule Kiroween (B-C44) |
| **V7** | Nhu cầu ở Việt Nam hay châu Á tồn tại cho nội dung của khu vực | Khảo sát hành vi (không phải thái độ): đếm bài đăng hay nhóm đang tìm lại blog Yahoo! 360 trên các diễn đàn tiếng Việt | 0,5 ngày | Không có hoạt động nào trong 2 năm gần nhất |

**Thứ tự đề xuất:** V6 và V2 trước, vì rẻ và có thể loại ý tưởng ngay. Sau đó V1, rồi V3. V4, V5 và V7 là kiểm tra bổ trợ.

---

## Questions for the other domains

1. **(C)** Chi phí toàn phần của IA khoảng 0,13 USD/GB/năm, còn giá Archive-It khoảng 16 USD/GB capture (B-C33). Phân tích của C có xác nhận rằng capture, QA và công cụ, chứ không phải lưu trữ, mới là cost driver chính không? Con số cho một nền tảng chỉ làm chỉ mục kèm phát lại phía client (B-M5) là bao nhiêu?
2. **(C)** Với B-M5, chi phí thực của nền tảng khi chỉ giữ metadata, chỉ mục và trình phát tĩnh, so với khi host WACZ, là bao nhiêu với 1.000 artifact?
3. **(C)** Với ứng dụng có backend (web app nghiên cứu), phần nào chạy lại được mà không cần runtime phía server? Đây là khoảng trống duy nhất có thể chưa bị IA, Flashpoint hay Ruffle lấp (§7).
4. **(C)** WACZ kèm ReplayWeb.page có cho phép "gửi bản gốc vào IA/SWH, nền tảng chỉ phát lại" mà không cần sao chép lại không? Có rào cản CORS hay giấy phép nào không?
5. **(A)** Có bằng chứng hành vi (lượt xem, thời gian, lượt quay lại) cho trải nghiệm giám tuyển về lịch sử web hay phần mềm, kiểu Net Art Anthology hay triển lãm bảo tàng số, không? Tôi không tìm được (B-C21).
6. **(A)** Persona explorer nào có thể **trả tiền hoặc đóng góp công**, thay vì chỉ xem?
7. **(A)** Với nội dung có giao thức văn hóa hay dữ liệu cá nhân, trải nghiệm nào vẫn có giá trị khi truy cập bị hạn chế?
8. **(A)** Các tiêu chí chọn lọc ở §8 có khớp với tiêu chí "đáng bảo tồn" theo kinh nghiệm bảo tàng và lưu trữ không?

## Challenges to the human's vision

1. **Giá trị chính (explorer) là nhóm có bằng chứng trả tiền yếu nhất.** Dòng tiền có thật đi vào capture (tổ chức, contributor) và quyên góp cho kho đa năng (§3, §5). Một mission đặt explorer lên trước cần một nguồn tài trợ không đến từ explorer, hoặc cần chấp nhận rằng nền tảng là dự án phi lợi nhuận hay tổ chức.
2. **"Không để biến mất" đã được IA làm ở quy mô mà một sản phẩm mới không thể sánh.** IA có hơn 210 PB và 1,3 triệu tựa phần mềm. Phần không có trong IA phần lớn không còn bản gốc. Cạnh tranh ở tầng lưu trữ là vô ích. Chỉ tầng trải nghiệm, giám tuyển và so sánh còn để ngỏ, và nhu cầu ở tầng này chưa được chứng minh.
3. **"Khi chủ sở hữu không còn duy trì được" là thời điểm tệ nhất để bắt đầu.** KDL, Cohost và Conifer cho thấy bảo tồn thành công khi được lên kế hoạch **trước**: SLA, sản phẩm lưu trữ từ khâu thiết kế, thời gian báo trước dài. Mission phụ nên đổi từ "cứu khi chết" sang "chuẩn bị trước khi chết".
4. **Chi phí bền vững không chỉ là lưu trữ.** Ngay cả một tổ chức có tài trợ (Rhizome) cũng đóng dịch vụ hosted của mình. Các tầng chi phí cao gồm công cụ, tương thích với web thay đổi, hỗ trợ và pháp lý.
5. **"Trải nghiệm chức năng" xung đột với pháp lý** ở vùng hấp dẫn nhất là game (§9). Nền tảng tư nhân không có đặc quyền sao chép bảo tồn như tổ chức di sản ở Mỹ, EU hay Nhật.
6. **Rule Kiroween yêu cầu không vi phạm IP hay quyền riêng tư.** Demo phải dùng nội dung có quyền rõ ràng, và điều này giới hạn mạnh những gì có thể "hồi sinh" trên sân khấu.

## Unresolved questions

1. Cơ cấu nhà tài trợ của IA: tỷ lệ cá nhân nhỏ so với quỹ lớn (CHƯA RÕ; chưa mở được Schedule B, thường không công khai).
2. Số lượt dùng thực của Archive-It hay Browsertrix collection từ phía explorer: tổ chức trả để capture, nhưng có ai xem không?
3. Trạng thái hiện tại (11/2026) của UK Web Archive sau sự cố 2023 (chỉ có snippet).
4. Ngân sách hằng năm của Software Heritage (không công khai trong nguồn tìm được).
5. Việt Nam có chương trình lưu trữ web quốc gia hay không; Nghị định 356/2025 có ngoại lệ cho lưu trữ hay nghiên cứu không.
6. Lượng nội dung Yahoo! 360 hay Yahoo! Blog Việt Nam còn tồn tại trong các kho lưu.
7. Arweave hay kho phi tập trung có thực sự được tổ chức di sản dùng cho bảo tồn không (chỉ có nguồn từ hệ sinh thái crypto).
8. Ngưỡng của V1 (2%, 20 đăng ký) là tùy ý; Coordinator hay người dùng cần chốt trước khi chạy.

## References

Ngày truy cập của mọi ref: 2026-11-26. Điểm 0–5: Authority(20) / Technical Evidence(20) / Mechanism(20) / Context(15) / Freshness(10) / Reproducibility(10) / Bias(5). Weighted = Σ weight × score / 5. SR = Source Reliability, RR = Reference Relevance (H/M/L). "Direct" = mở trực tiếp bằng curl và đọc text; "snippet" = chỉ thấy trong kết quả tìm kiếm.

| Ref | URL | Title | Publisher | Pub date | Accessed | Opened | Claims | Au | TE | Me | Co | Fr | Re | Bi | Weighted | SR | RR |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R1 | https://kclpure.kcl.ac.uk/portal/en/publications/managing-100-digital-humanities-projects-digital-scholarship-amp-/ | Managing 100 Digital Humanities Projects (record and abstract) | King's College London Pure | 2019-04-26 | 2026-11-26 | direct | B-C7 | 5 | 3 | 4 | 4 | 2 | 3 | 4 | 72 | H | H |
| R2 | https://digitalhumanities.org/dhq/vol/13/1/000411/000411.html | Managing 100 Digital Humanities Projects: Digital Scholarship & Archiving in King's Digital Lab (full text) | DHQ 13(1), Smithies et al. | 2019 | 2026-11-26 | direct | B-C7, B-C8 | 5 | 4 | 5 | 5 | 2 | 3 | 4 | 82 | H | H |
| R3 | https://www.dpconline.org/handbook/organisational-activities/preservation-action | Preservation action (Digital Preservation Handbook) | Digital Preservation Coalition | n.d. (hiện hành) | 2026-11-26 | direct | §6 bối cảnh (emulation kéo theo vấn đề license và chi phí chuyên gia) | 5 | 3 | 4 | 3 | 2 | 2 | 5 | 68 | H | M |
| R4 | https://kiroween.devpost.com/rules | Kiroween 2026 Official Rules | Devpost / Sponsor | 2026 | 2026-11-26 | direct (đối chiếu snapshot của Coordinator) | B-C44 | 5 | 1 | 3 | 5 | 5 | 4 | 5 | 74 | H | H |
| R5 | https://blog.conifer.rhizome.org/2025/12/15/twilight-announcement.html | Conifer Twilight Announcement | Rhizome | 2025-12-15 | 2026-11-26 | direct | B-C11 | 5 | 3 | 5 | 5 | 5 | 3 | 4 | 86 | H | H |
| R6 | https://webrecorder.net/blog/2025-12-18-conifer-twilight | Our statement on Conifer sunset announcement | Webrecorder (I. Kreymer) | 2025-12-18 | 2026-11-26 | direct | B-C11 (xác nhận độc lập) | 4 | 2 | 4 | 5 | 5 | 2 | 2 | 68 | H | H |
| R7 | https://projects.propublica.org/nonprofits/organizations/943242767 | Internet Archive — Nonprofit Explorer | ProPublica (dữ liệu IRS 990) | FY2025 | 2026-11-26 | direct | B-C18, B-C33 | 4 | 4 | 3 | 4 | 5 | 5 | 5 | 79 | H | H |
| R8 | https://siviq.co/nonprofits/organizations/943242767/internet-archive/returns/202532629349300733/2024 | IA 2024 return (aggregator) | Civic Intelligence / philanthropy.org | 2024 | 2026-11-26 | snippet | B-C18 (xác nhận năm trước: 26,8 triệu USD doanh thu, 23,5 triệu USD chi) | 2 | 3 | 2 | 4 | 4 | 3 | 4 | 54 | M | M |
| R9 | https://coppul.ca/preservation/archive-it | Archive-It (consortium pricing 2024–2025) | COPPUL | 2024–2025 | 2026-11-26 | direct | B-C22, B-C33 | 4 | 3 | 3 | 4 | 5 | 4 | 4 | 72 | H | H |
| R10 | https://archive-it.org/blog/products-and-services/archive-it-faqs | Archive-It FAQs; Archive-It Basic brochure 2021 | Internet Archive | 2021–n.d. | 2026-11-26 | snippet (trang FAQ trả về 269 ký tự) | B-C22 | 4 | 2 | 3 | 4 | 2 | 2 | 3 | 57 | H | M |
| R11 | https://webrecorder.net/browsertrix/pricing/ | Browsertrix Pricing | Webrecorder | hiện hành | 2026-11-26 | direct | B-C23 | 5 | 2 | 3 | 4 | 5 | 4 | 3 | 69 | H | H |
| R12 | https://perma.cc/docs/accounts | Perma.cc accounts / FAQ; blog Harvard LIL 2019 | Harvard LIL | 2019–hiện hành | 2026-11-26 | snippet (403) | B-C24 | 4 | 2 | 3 | 3 | 4 | 2 | 3 | 58 | H | M |
| R13 | https://softwareheritage.org/?p=41161 | Archives and Libraries Interest Group Members; SWH DIG membership brochure | Software Heritage | 2024–2025 | 2026-11-26 | snippet (fetch thất bại) | B-C28 | 4 | 2 | 3 | 4 | 4 | 2 | 3 | 61 | H | M |
| R14 | https://en.wikipedia.org/wiki/Software_Heritage | Software Heritage | Wikipedia | hiện hành | 2026-11-26 | direct | B-C28 | 2 | 2 | 3 | 4 | 4 | 3 | 4 | 56 | M | M |
| R15 | https://sloan.org/grant-detail/g-2025-25188 | Grant G-2025-25188 | Alfred P. Sloan Foundation | 2025 | 2026-11-26 | direct | B-C29 | 5 | 2 | 3 | 3 | 5 | 4 | 5 | 67 | H | M |
| R16 | https://www.pewresearch.org/data-labs/2024/05/17/when-online-content-disappears/ | When Online Content Disappears | Pew Research Center | 2024-05-17 | 2026-11-26 | direct | B-C5 | 5 | 5 | 4 | 4 | 4 | 5 | 5 | 90 | H | H |
| R17 | https://blog.archive.org/tag/pew/ | (bài phân tích link rot và Wayback rescue) | Internet Archive | 2025–2026 | 2026-11-26 | direct | B-C5 (xác nhận), B-C6 | 3 | 4 | 4 | 4 | 5 | 4 | 2 | 72 | M | H |
| R18 | https://wiki.archiveteam.org/index.php/GeoCities_Japan | GeoCities Japan | ArchiveTeam wiki | 2018–2019 | 2026-11-26 | direct | B-C1 | 3 | 4 | 4 | 4 | 2 | 4 | 4 | 69 | M | H |
| R19 | https://www.engadget.com/2018/10/02/yahoo-japan-geocities-shutting-down/ | Yahoo Japan GeoCities shutting down; bài GIGAZINE | Engadget / GIGAZINE | 2018 | 2026-11-26 | snippet | B-C1 (xác nhận ngày) | 3 | 1 | 3 | 3 | 2 | 2 | 4 | 49 | M | M |
| R20 | https://globalvoices.org/2009/03/22/vietnam-yahoo-360-to-close-blog-service/ | Vietnam: Yahoo! 360 to close blog service | Global Voices (M. Palatino) | 2009-03-22 | 2026-11-26 | direct | B-C2 | 3 | 1 | 3 | 5 | 1 | 2 | 4 | 52 | M | H |
| R21 | https://vietnamnet.vn/en/vietnamese-bloggers-still-awaiting-service-providers-E65776.html | Vietnamese bloggers still awaiting service providers | VietNamNet | 2013-02-04 | 2026-11-26 | direct | B-C3 | 3 | 2 | 3 | 5 | 1 | 2 | 4 | 55 | M | H |
| R22 | https://m.hanoitimes.vn/vietnamese-social-networks-in-the-post-yahoo-360-era-44729.html | Vietnamese social networks in the post-Yahoo 360 era; TechCrunch | Hanoi Times / TechCrunch | 2009 | 2026-11-26 | snippet | B-C2 (85% người dùng MXH Việt Nam ở Yahoo 360, theo Yahoo VN) | 3 | 1 | 2 | 5 | 1 | 1 | 3 | 46 | M | M |
| R23 | https://gamehistory.org/87percent/ | 87% Missing: the Disappearance of Classic Video Games | Video Game History Foundation | 2023-07 | 2026-11-26 | direct (kèm dataset Zenodo 8161056 qua snippet) | B-C9 | 4 | 5 | 4 | 3 | 3 | 5 | 3 | 79 | H | M |
| R24 | https://gamehistory.org/dmca-2024-statement/ | Statement on the DMCA 2024 triennial review ruling | VGHF | 2024-10 | 2026-11-26 | direct | B-C35 | 3 | 2 | 4 | 4 | 4 | 2 | 2 | 60 | M | H |
| R25 | https://www.infodocket.com/2024/10/25/u-s-copyright-office-rejects-dmca-exemption-to-support-game-preservation/ | U.S. Copyright Office rejects DMCA exemption…; Game Developer | InfoDocket / Game Developer | 2024-10 | 2026-11-26 | snippet | B-C35 (xác nhận độc lập) | 3 | 2 | 3 | 4 | 4 | 2 | 4 | 58 | M | H |
| R26 | https://flowingdata.com/2024/01/10/nyt-flash-based-visualizations-work-again/ | NYT Flash-based visualizations work again | FlowingData (N. Yau) | 2024-01-10 | 2026-11-26 | direct | B-C10 | 3 | 2 | 4 | 4 | 4 | 3 | 4 | 63 | M | H |
| R27 | https://www.digitalpreservation.gov/meetings/DSA2026/0117_jonah_edwards_ia_dsa_2026.pdf | Internet Archive 2025 Materials/Storage Update | Library of Congress DSA 2026 (J. Edwards, IA) | 2026-01 | 2026-11-26 | direct (PDF) | B-C27, B-C33 | 4 | 4 | 4 | 4 | 5 | 3 | 3 | 77 | H | H |
| R28 | https://www.opb.org/article/2025/03/23/a-peek-inside-the-busy-home-of-the-internet-archive/ | A peek inside the busy home of the Internet Archive | OPB | 2025-03-23 | 2026-11-26 | snippet | B-C17 | 3 | 1 | 2 | 4 | 4 | 1 | 4 | 49 | M | M |
| R29 | https://addons.mozilla.org/firefox/addon/ruffle_rs/ | Ruffle — Flash Emulator | Mozilla Add-ons | hiện hành | 2026-11-26 | snippet | B-C19 | 4 | 2 | 2 | 3 | 5 | 3 | 5 | 61 | H | M |
| R30 | https://flashgaming.fandom.com/wiki/Flashpoint_Archive | Flashpoint Archive | Flash Gaming wiki (Fandom) | hiện hành | 2026-11-26 | snippet | B-C20 | 2 | 1 | 2 | 4 | 4 | 1 | 3 | 42 | L | M |
| R31 | https://blog.archive.org/2025/08/06/vanishing-culture-why-preserve-flash/ | Vanishing Culture: Why Preserve Flash? | Internet Archive | 2025-08-06 | 2026-11-26 | direct | §4 bối cảnh (cộng đồng Flash vẫn hoạt động) | 3 | 1 | 2 | 4 | 5 | 1 | 2 | 47 | M | L |
| R32 | https://minister.infrastructure.gov.au/burke/media-release/securing-future-trove | Securing the future of Trove; NLA announcement 2023-04-03; Canberra Times | Bộ trưởng Burke / NLA / Canberra Times | 2023 | 2026-11-26 | snippet (fetch 000 và 418) | B-C12 | 5 | 2 | 3 | 4 | 3 | 2 | 4 | 64 | H | H |
| R33 | https://bl.uk/cyber-incident | Cyber-attack recovery update; Varsity, Cambridge UL | British Library | 2023–2026 | 2026-11-26 | direct (trang BL); chi tiết UKWA chỉ snippet | B-C13 | 5 | 1 | 3 | 4 | 5 | 2 | 4 | 64 | H | M |
| R34 | https://africandigitalheritage.org/?p=4092 | Frequently Asked Questions | African Digital Heritage | n.d. | 2026-11-26 | direct | B-C14 | 3 | 1 | 3 | 4 | 3 | 1 | 3 | 49 | M | M |
| R35 | https://www.memoriachilena.gob.cl/602/w3-article-127972.html | Biblioteca Nacional presentó Archivo de la Web Chilena | Biblioteca Nacional de Chile | n.d. (khoảng 2015) | 2026-11-26 | direct | B-C15 | 5 | 2 | 3 | 4 | 2 | 2 | 4 | 61 | H | M |
| R36 | https://www.palabraclave.fahce.unlp.edu.ar/article/view/PCe269/21483 | (Cerdán Medina 2025, web archiving in Latin America) | Palabra Clave (UNLP) | 2025 | 2026-11-26 | snippet (mở được trang nhưng không trích được nội dung) | B-C16 | 4 | 3 | 3 | 4 | 5 | 2 | 5 | 70 | H | M |
| R37 | https://chinadigitaltimes.net/2024/06/translation-he-jiayan-on-the-accelerating-collapse-of-the-chinese-internet/ | Translation: He Jiayan on the accelerating collapse of the Chinese internet | China Digital Times | 2024-06 | 2026-11-26 | snippet (403) | B-C4 | 2 | 1 | 3 | 4 | 4 | 1 | 2 | 49 | L | M |
| R38 | https://gdpr-info.eu/art-17-gdpr/ | Art. 17 GDPR — Right to erasure | gdpr-info.eu (văn bản GDPR) | 2016/679 | 2026-11-26 | direct | B-C41 | 4 | 2 | 4 | 4 | 3 | 5 | 5 | 74 | H | H |
| R39 | https://www.legislation.gov.uk/eudr/2019/790/article/6/data.htm | Directive (EU) 2019/790, Article 6 | legislation.gov.uk / LawPlayer | 2019 | 2026-11-26 | snippet (LawPlayer mở được tiêu đề nhưng không có nội dung điều) | B-C40 | 5 | 2 | 4 | 4 | 3 | 4 | 5 | 74 | H | H |
| R40 | https://www.cric.or.jp/english/clj/ocl.html | Copyright Law of Japan (outline) | CRIC | hiện hành | 2026-11-26 | snippet | B-C42 | 4 | 2 | 3 | 3 | 3 | 3 | 5 | 62 | H | M |
| R41 | https://creativecommons.org/wp-content/uploads/2026/09/Guidance-for-Indigenous-Collections-and-Data_English_Final.pdf | Guidance for Indigenous Collections and Data | Creative Commons / Local Contexts | 2026-09 | 2026-11-26 | snippet | B-C38 | 4 | 2 | 3 | 4 | 5 | 2 | 4 | 65 | H | M |
| R42 | https://ardrive.io/articles/can-data-really-be-stored-forever/ | Can data really be stored forever? | ArDrive | n.d. | 2026-11-26 | direct | B-C30 | 2 | 2 | 3 | 3 | 3 | 2 | 1 | 47 | L | M |
| R43 | https://www.chainscorelabs.com/blog/developer-ecosystem-tools-languages-and-grants/decentralized-compute-and-storage/why-arweaves-endowment-model-is-flawed-but-necessary | Why Arweave's endowment model is flawed but necessary | Chainscore Labs | n.d. | 2026-11-26 | snippet | B-C31 | 1 | 2 | 3 | 3 | 3 | 1 | 2 | 41 | L | M |
| R44 | https://nlv.gov.vn/ef/legal-deposit-division.html | Legal deposit division (NLV); LuatVietnam về Nghị định 356/2025 | Thư viện Quốc gia VN / LuatVietnam | hiện hành | 2026-11-26 | snippet | B-C43 | 4 | 1 | 2 | 5 | 4 | 2 | 4 | 58 | H | H |
| R45 | https://old.rhizome.org/editorial/2020/jun/24/artbase-in-2020 | ArtBase in 2020; Net Art Anthology credits | Rhizome | 2020 | 2026-11-26 | snippet | B-C21, B-C32 | 4 | 1 | 2 | 4 | 2 | 1 | 3 | 50 | H | M |

### Seed references (mission §7) — đánh giá

| Seed | Đã mở | Weighted | Xác nhận độc lập / cạnh tranh / phê bình / thất bại | Verdict |
|---|---|---|---|---|
| Smithies et al. 2019 (R1, R2) | Có (abstract trên kclpure và full text trên DHQ) | 82 (R2) | Xác nhận: trang KDL "Archiving and sustainability" (`P3` R2) mô tả cùng quy trình. Cách tiếp cận cạnh tranh: Endings Principles (UVic, `P3` R3), loại bỏ phụ thuộc server ngay từ đầu. Hạn chế: đây là mô tả tự báo của chính lab, chỉ ở một tổ chức, và dữ liệu 2016–2017 đã cũ | Nguồn gốc mạnh cho cơ chế "bảo tồn cần SLA và kế hoạch từ đầu". Không chứng minh mô hình đó nhân rộng được ngoài một lab có ngân sách đại học |
| DPC Handbook, Preservation action (R3) | Có | 68 | Tự trích Rosenthal 2015: rào cản của emulation là công cụ tạo image và pháp lý, cả hai làm chi phí "vượt tầm". Handbook tự nhận "tương đối ít tiến bộ về chiến lược mới" kể từ cuối thập niên 1990 | Tham chiếu chuẩn tốt cho phân loại chiến lược (migration, emulation, computer museum), nhưng phần lớn nội dung cũ và không có số liệu chi phí. Ít liên quan trực tiếp tới kinh tế |
| Kiroween rules (R4) | Có (trang live; đối chiếu snapshot của Coordinator, khác vài dòng, các điều khoản liên quan không đổi) | 74 | Không cần xác nhận độc lập (văn bản chính thức) | Ràng buộc trực tiếp với miền B: Potential Impact ("real problem for a real audience… would someone actually use this?") và điều khoản IP và quyền riêng tư (B-C44) |

### Sổ claim

Chuỗi: P = nguồn gốc mở trực tiếp; I = xác nhận độc lập; M = kiểm tra cơ chế hoặc tính toán.

| Claim | Nhãn | Nội dung | Refs | Chuỗi |
|---|---|---|---|---|
| B-C1 | ĐÃ XÁC MINH | GeoCities JP đóng 01/04/2019; ArchiveTeam crawl 96 triệu URL, 3,7 TB, "Partially saved" | R18, R19 | P + I (snippet về ngày) |
| B-C2 | SUY LUẬN | Yahoo! 360 là nền tảng blog phổ biến nhất VN (2009); tin đóng gây lo lắng; con số 85% chỉ ở snippet | R20, R22 | P (một nguồn báo chí công dân) + snippet |
| B-C3 | ĐÃ XÁC MINH (scoped "VietNamNet đưa tin") | Yahoo yêu cầu người dùng blog VN tải dữ liệu trước 09/03/2013 | R21 | P |
| B-C4 | SUY LUẬN | Phần lớn nội dung Internet Trung Quốc thời tiền-mobile đã mất (ước lượng của He Jiayan, không phải nghiên cứu) | R37, `P3` R36 | snippet |
| B-C5 | ĐÃ XÁC MINH | 38% trang 2013 không truy cập được vào 2023; 54% trang Wikipedia có link tham khảo chết | R16, R17 | P + I |
| B-C6 | ĐÃ XÁC MINH (scoped "IA phân tích") | Wayback cứu khoảng 15% trang đã chết trong mẫu Pew | R17 | P (bên có lợi ích) |
| B-C7 | ĐÃ XÁC MINH | KDL tiếp nhận khoảng 100 dự án; khoảng một nửa chất lượng cao; gần như tất cả gặp vấn đề tài trợ và kỹ thuật; thế kẹt ba lựa chọn | R1, R2, `P3` R2 | P + I (trang KDL) |
| B-C8 | ĐÃ XÁC MINH (scoped "KDL tuyên bố") | KDL dùng SLA với PI; sản phẩm lưu trữ được lên kế hoạch từ khâu yêu cầu | R2 | P |
| B-C9 | ĐÃ XÁC MINH (scoped nghiên cứu) | 87% game cổ điển phát hành ở Mỹ không còn bán chính thức (n = 1.500) | R23 | P + dataset công khai (M chưa chạy lại) |
| B-C10 | SUY LUẬN | NYT dùng Ruffle để khôi phục đồ họa Flash trong kho bài | R26 | nguồn thứ cấp mở trực tiếp; trang NYT không mở |
| B-C11 | ĐÃ XÁC MINH | Conifer ngừng tài khoản và thuê bao từ 15/12/2025, ngừng capture 05/2026, tombstone 06/2026; có bốn lựa chọn, kể cả tự host WACZ | R5, R6 | P + I |
| B-C12 | SUY LUẬN | Trove suýt hết tiền 06/2023; khoảng 30.000 chữ ký; 33 triệu AUD/4 năm | R32 | nhiều snippet nhất quán; trang gốc bị chặn |
| B-C13 | SUY LUẬN | BL bị ransomware 10/2023, vẫn đang khôi phục; UKWA không truy cập được | R33 | P (trang BL, không nêu UKWA) + snippet |
| B-C14 | ĐÃ XÁC MINH (scoped "ADH tuyên bố") | African Digital Heritage dựa vào donor và tài trợ dự án | R34 | P |
| B-C15 | ĐÃ XÁC MINH (scoped "BN Chile tuyên bố") | Archivo de la Web Chilena, tiên phong ở Mỹ Latinh, dùng OpenWayback | R35 | P |
| B-C16 | SUY LUẬN | Mỹ Latinh có rào cản pháp lý, kỹ thuật, kinh tế; thiếu nghiên cứu quốc tế | R36 | snippet |
| B-C17 | SUY LUẬN | IA khoảng một triệu lượt truy cập/ngày | R28 | snippet |
| B-C18 | ĐÃ XÁC MINH (scoped số liệu 990 do ProPublica trích) | IA FY2025: doanh thu 23,71 triệu USD, chi 27,77 triệu USD, quyên góp 20,19 triệu USD (85,2%) | R7, R8 | P + I (năm trước, snippet) |
| B-C19 | SUY LUẬN | Ruffle có 77.723 người dùng trên Firefox Add-ons | R29 | snippet |
| B-C20 | SUY LUẬN | Flashpoint lưu hơn 190.000 game và animation | R30 | snippet, nguồn yếu |
| B-C21 | CHƯA RÕ | Không có số liệu lượt xem cho trải nghiệm giám tuyển (Rhizome) | R45 | truy vấn ghi ở §4 |
| B-C22 | ĐÃ XÁC MINH (scoped "giá COPPUL") | Archive-It 2.100 USD/128 GB … 16.800 USD/2 TB (2024–2025); dữ liệu cũ lưu không thêm phí (snippet) | R9, R10 | P + snippet |
| B-C23 | ĐÃ XÁC MINH (scoped "Webrecorder niêm yết") | Browsertrix 30 / 60 / 120 USD/tháng | R11 | P |
| B-C24 | SUY LUẬN | Perma.cc thu 10–100 USD/tháng với cá nhân; registrar thư viện và tòa án miễn phí | R12 | snippet |
| B-C25 | SUY LUẬN | Không có dòng tiền từ explorer cho trải nghiệm khám phá giám tuyển | §3, §4 | tổng hợp |
| B-C26 | SUY LUẬN | Nhu cầu explorer tổng quát có thật và đã được phục vụ miễn phí; nhu cầu cho nền tảng mới chưa được chứng minh | §4 | tổng hợp |
| B-C27 | ĐÃ XÁC MINH (scoped "IA tự báo") | IA có 1,3 triệu tựa phần mềm, nhiều cái giả lập được; hơn 210 PB dữ liệu duy nhất; tăng khoảng 20%/năm | R27 | P |
| B-C28 | SUY LUẬN | SWH dựa trên nhà tài trợ, Inria, UNESCO; tầng thành viên 2.000–50.000 EUR/năm | R13, R14 | Wikipedia mở được + snippet |
| B-C29 | ĐÃ XÁC MINH (scoped "Sloan niêm yết") | Sloan cấp 575.000 USD cho công cụ dựa trên SWH | R15 | P |
| B-C30 | ĐÃ XÁC MINH (scoped "ArDrive tuyên bố") | Arweave: phí trả trước cho 200 năm; giả định giá lưu trữ giảm 0,5%/năm | R42 | P (nguồn có lợi ích) |
| B-C31 | SUY LUẬN | Endowment của Arweave có rủi ro từ giá token | R43 | snippet, nguồn web3 |
| B-C32 | SUY LUẬN | Rhizome được tài trợ bởi quỹ tư nhân và Google Arts & Culture | R45 | snippet |
| B-C33 | SUY LUẬN (ước tính) | IA khoảng 0,13 USD/GB/năm toàn phần, Archive-It khoảng 16,4 USD/GB capture; chênh khoảng 100 lần; cost driver là capture và con người | R7, R27, R9 | M (tính toán; giả định ghi ở §5) |
| B-C34 | SUY LUẬN | Thu hẹp H0: có người trả cho dịch vụ capture; không có cho cứu chức năng hay trải nghiệm explorer | R9, R11, R12, §3 | tổng hợp |
| B-C35 | ĐÃ XÁC MINH (scoped "VGHF tuyên bố") | Copyright Office 10/2024 không cấp miễn trừ truy cập từ xa cho game; ESA phản đối | R24, R25 | P + I (snippet) |
| B-C36 | GIẢ THUYẾT | Lai M5 và M3 là mô hình ít mâu thuẫn nhất với bằng chứng | §6 | — |
| B-C37 | SUY LUẬN | Lý do khác biệt duy nhất còn đứng được là trải nghiệm giám tuyển xây trên kho có sẵn | §7 | tổng hợp |
| B-C38 | SUY LUẬN | CARE và Local Contexts Labels là cơ chế thực thi giao thức văn hóa trong kho số | R41 | snippet |
| B-C39 | GIẢ THUYẾT | Bốn tiêu chí chọn lọc (giá trị, công nghệ khai tử, quyền, người bảo trợ ngoài) | §8 | — |
| B-C40 | SUY LUẬN | DSM Điều 6: ngoại lệ bắt buộc cho CHI sao chép bảo tồn bộ sưu tập thường trực | R39 | snippet văn bản |
| B-C41 | ĐÃ XÁC MINH (scoped văn bản luật) | GDPR 17(3)(d) loại trừ quyền xóa với lưu trữ vì lợi ích công cộng theo Điều 89(1) | R38 | P |
| B-C42 | SUY LUẬN | Luật Bản quyền Nhật Điều 43 cho phép NDL sao chép tài liệu Internet | R40 | snippet |
| B-C43 | SUY LUẬN | VN: lưu chiểu điện tử chỉ cho báo chí; không tìm thấy chương trình web archive; Nghị định 356/2025 thay Nghị định 13/2023 | R44 | snippet |
| B-C44 | ĐÃ XÁC MINH (scoped "rules chính thức nêu") | Bài nộp không vi phạm IP hay quyền riêng tư; repo nguồn mở; tiêu chí Potential Impact | R4 | P (kèm snapshot) |
| B-C45 | SUY LUẬN | Đặc quyền sao chép bảo tồn thuộc về tổ chức di sản, không thuộc nền tảng tư nhân | B-C35, B-C40, B-C41, B-C42 | tổng hợp |
| B-C46 | SUY LUẬN | Mất mát mang tính toàn cầu; năng lực và người trả tập trung ở Bắc Mỹ, EU, Nhật, Úc | §11 | tổng hợp |

**Đếm nhãn:** ĐÃ XÁC MINH 19 · SUY LUẬN 24 · GIẢ THUYẾT 2 · CHƯA RÕ 1 (tổng 46).
