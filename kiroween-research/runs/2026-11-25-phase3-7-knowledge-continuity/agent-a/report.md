# Phase 3 — Agent A

## Metadata

- **Agent:** Agent A
- **Model / Effort observed:** Gemini 4 Neon (Medium) (từ cấu hình phiên; không có telemetry token nội bộ)
- **Thời gian bắt đầu (UTC):** 2026-11-25T16:15:48Z
- **Thời gian kết thúc (UTC):** 2026-11-25T16:28:31Z
- **Số lượt tìm kiếm web (ước lượng):** 24 truy vấn `search_web`
- **Nguồn mở trực tiếp vs chỉ snippet:** 27 nguồn mở trực tiếp (HTTP 200 đọc toàn văn); 7 nguồn chỉ snippet (tổng 34 nguồn trong §9; các nguồn chỉ snippet do HTTP 403/404/405 hoặc chặn anti-bot/reCAPTCHA)
- **Lỗi truy cập / giới hạn ghi nhận:**
  - `https://www.iastatedigitalpress.com/jlsc/article/id/16288/` (Eve 2024): bị chặn anti-bot ("Making sure you're not a bot!") → không vượt rào, đánh dấu snippet-only.
  - `https://www.drupal.org/psa-2023-06-07` (Drupal 7 EOL): bị chặn "Client Challenge" → không vượt rào, đánh dấu snippet-only.
  - `https://pmc.ncbi.nlm.nih.gov/articles/PMC5389617/` (Wren 2017): bị chặn reCAPTCHA; `https://academic.oup.com/nar/article/45/7/3627/3064234` trả HTTP 403 → không vượt rào, đánh dấu snippet-only.
  - `https://www.paradisec.org.au/about-us/` (HTTP 403), `https://eap.bl.uk/about-programme` (HTTP 405), `https://mukurtu.org/about/` và `https://mukurtuhosting.org/` (đóng kết nối), `https://www.softwareheritage.org/mission/` (lỗi xác thực chứng chỉ SSL cục bộ), `https://eur-lex.europa.eu/eli/reg/2023/2854/oj` (HTTP 202 rỗng) → thay thế bằng nguồn gốc mở trực tiếp tương đương (`docs.mukurtu.org`, `digital-strategy.ec.europa.eu/en/policies/data-act`, v.v.) hoặc đánh dấu snippet-only.

## 1. Method

- **Phương pháp phân tích nghiệp vụ (Business Analysis) được chọn:**
  1. **Phân tích cây nguyên nhân gốc (Root-Cause Problem Tree):** tách triệu chứng (website chết, dữ liệu mất) khỏi nguyên nhân cấu trúc (kinh tế, kiến trúc phụ thuộc, quản trị, pháp lý) và xác định rõ điều kiện mà bảo tồn *không* có cơ sở.
  2. **Lập bản đồ bên liên quan & Jobs-to-be-Done (Stakeholder / JTBD Matrix):** phân biệt rạch ròi giữa người chịu thiệt hại, người vận hành, người trả tiền (payer) và người duy trì dài hạn (maintainer); kiểm tra nhu cầu **được chứng minh bằng hành vi** (demonstrated demand: chi tiêu, hợp đồng, giờ tình nguyện, di cư thực tế) so với nhu cầu **giả định** (hypothetical).
  3. **Kiểm định giả thuyết Task B & đối chứng quốc tế:** coi các kết luận Task B (`A-O1`, `A-O2`, `B-O2`, `C-O1`, `C-O3`, `H0`, `H2`, `H3`, `H4`, `H8`) là giả thuyết cần kiểm chứng lại trên nguồn gốc mới (NA, EU, Asia, Other).
  4. **Cổng chủ đề Kiroween Resurrection & kiểm định vai trò AI:** kiểm tra từng không gian xem có **công nghệ cụ thể đã ngừng hỗ trợ / bị khai tử chính thức** làm mỏ neo không (theo `rubric-and-anchors.md`, cổng `theme ≥ 3`), và đối chiếu AI với kỹ thuật phần mềm thông thường.
- **Những gì cố ý KHÔNG làm ở Phase 3:** không thiết kế kiến trúc sản phẩm hay đề xuất MVP (thuộc Phase 5); không chấm điểm xếp hạng chính thức hay so sánh với ứng viên Phase 2 (thuộc Phase 6); không gộp 4 không gian trước khi hoàn thành phân tích độc lập §2–§5; không nới lỏng định nghĩa Resurrection để cứu không gian trượt cổng.

---

## 2. S2 — Research apps after funding

### a. Problem and root causes

- **Vấn đề thực tế:** Nhiều ứng dụng web, công cụ tra cứu và cơ sở dữ liệu học thuật (đặc biệt trong tin sinh học và Nhân văn số / Digital Humanities — DH) ngừng hoạt động sau khi chu kỳ tài trợ (grant 2–5 năm) kết thúc, khiến kết quả nghiên cứu gắn với URL/công cụ đó không còn truy cập hoặc tái lập được [A-S2-C1, INFERENCE; kế thừa và kiểm tra lại Task B `A-O1`].
- **Cây nguyên nhân gốc:**
  ```text
  Ứng dụng web nghiên cứu chết sau khi hết grant
  ├─ 1. Cấu trúc tài trợ học thuật
  │   ├─ Grant tài trợ xây dựng ban đầu (2–5 năm), hiếm khi cấp ngân sách bảo trì dài hạn
  │   └─ Khuyến khích công bố bài báo mới hơn là bảo trì phần mềm cũ
  ├─ 2. Kiến trúc phần mềm mong manh
  │   ├─ Phụ thuộc server-side động (DB, PHP/Python/Ruby/Java cũ, máy chủ phòng lab)
  │   └─ Lỗi thời runtime/bảo mật buộc IT đại học tắt máy chủ khi không còn người vá lỗi
  └─ 3. Đứt gãy nhân sự và bàn giao
      ├─ Nghiên cứu sinh/postdoc xây dựng công cụ rời phòng lab sau khi hoàn thành đề tài
      └─ Thiếu quy trình đóng gói "afterlife" (chuyển sang tĩnh hoặc nộp kho lưu trữ) từ đầu dự án
  ```
- **Khi nào bảo tồn KHÔNG có cơ sở:**
  1. Công cụ ít được trích dẫn hoặc đã có công cụ mới tốt hơn thay thế hoàn toàn chức năng. Nghiên cứu của Wren et al. (2017) cho thấy tài nguyên tin sinh học được trích dẫn nhiều có tỷ lệ tự sống sót cao hơn đáng kể so với phần đuôi dài [A-S2-C2, INFERENCE, dựa trên snippet `R25` và Task B `A §11.2`].
  2. Ứng dụng chỉ là giao diện web bọc quanh bộ dữ liệu đã được lưu trữ sạch có DOI/metadata chuẩn (ví dụ kho NBDC LSDB Archive hoặc Zenodo), trong khi giao diện cũ không mang lại năng lực phân tích độc đáo.
  3. Chi phí duy trì máy chủ tính toán nặng (ví dụ pipeline chạy cụm máy chủ / GPU) vượt xa giá trị sử dụng thực tế sau dự án.

### b. Stakeholders and target users

| Tác nhân (Actor) | Job-to-be-Done (JTBD) | Hành vi hiện tại | Sẵn lòng đóng góp / trả tiền | Demonstrated vs Hypothetical | Bằng chứng |
|---|---|---|---|---|---|
| Phòng lab Nhân văn số / Thư viện đại học (ví dụ UVic, King's Digital Lab) | Lưu trữ và duy trì truy cập dài hạn danh mục dự án web sau grant trong ngân sách IT hữu hạn | Áp dụng nguyên tắc tĩnh hóa (Project Endings), ký SLA 2–5 năm hoặc lưu VM/kho dữ liệu (KDL) | **Có** (ngân sách tổ chức, grant hạ tầng, SLA tính trong đề xuất grant) | **Demonstrated** | `R1` (mở trực tiếp), `R2` (mở trực tiếp) |
| Trung tâm hạ tầng dữ liệu khoa học quốc gia / khu vực (NBDC Nhật Bản, ELIXIR châu Âu) | Đảm bảo dữ liệu/công cụ khoa học sự sống tồn tại như tài sản công dài hạn | Lưu trữ bộ dữ liệu tĩnh kèm metadata chuẩn hóa (NBDC: 89 DB) và danh mục `bio.tools` (ELIXIR) | **Có** (ngân sách nhà nước / liên chính phủ) | **Demonstrated** | `R3` (mở trực tiếp), `R4` (mở trực tiếp) |
| Nhóm nghiên cứu / PI hết grant | Giữ công cụ trích dẫn trong bài báo không bị hỏng link mà không tốn thêm công sức vận hành | Bỏ mặc trên server trường đến khi bị tắt, hoặc đưa code lên GitHub/Zenodo mà không chạy được | **Thấp / Hầu như không** (hết tiền grant) | **Mixed** (chỉ hành động nếu có yêu cầu từ tạp chí/quỹ tài trợ) | `R1`, `R25` (snippet) |
| Công ty Dược / Biotech & NXB khoa học | Tái lập kết quả tính toán có kiểm chứng từ bài báo | Trả phí cho nền tảng SaaS thương mại như Code Ocean (Compute Capsules) | **Có** (WTP thương mại rõ cho *reproducibility*, không phải cho web app DH cũ) | **Demonstrated** (cho compute reproducibility) | `R5` (mở trực tiếp) |

### c. Documented cases by region

- **North America (NA):**
  - *Project Endings (University of Victoria, Canada):* Dự án được SSHRC tài trợ nhằm giải quyết nguy cơ mất khả năng truy cập các dự án Nhân văn số sau grant; ban hành bộ *Endings Principles for Digital Longevity* (v2.2.1, ngày 2023-03-03) yêu cầu lưu dữ liệu ở định dạng chuẩn mở (TEI XML, GML, ODF, TXT), kiểm soát phiên bản và tạo sản phẩm tĩnh không phụ thuộc cơ sở dữ liệu server-side [A-S2-C3, VERIFIED — tài liệu chính thức mở trực tiếp `R1`, tuyên bố phạm vi về nguyên tắc chính thức của UVic].
  - *EaaSI (Software Preservation Network, Mỹ):* Bảo tồn và chạy lại phần mềm nghiên cứu/giảng dạy cũ qua giả lập (ví dụ Case Study #1 *The Would-Be Gentleman*) [A-S2-C4, VERIFIED — `R6` mở trực tiếp].
- **Europe (EU):**
  - *King's Digital Lab (King's College London, Anh):* Công bố tích cực đến năm 2026 về chuyển đổi di sản số (*"Transforming digital legacy estates to create a more sustainable future"*, 12/06/2026) và tham gia dự án EPSRC STEP-UP hỗ trợ đội ngũ Research Technical Professionals (RTPs) [A-S2-C5, VERIFIED — `R2` mở trực tiếp; chi tiết SLA 2–5 năm và lưu trữ VM từ snippet tìm kiếm → INFERENCE].
  - *ELIXIR Tools Platform (châu Âu):* Tổ chức liên chính phủ điều phối bền vững công cụ và cơ sở dữ liệu tin sinh học xuyên các node quốc gia châu Âu [A-S2-C6, VERIFIED — `R4` mở trực tiếp].
- **Asia:**
  - *NBDC Life Science Database Archive (JST, Nhật Bản):* Chính thức duy trì và lưu trữ **89 cơ sở dữ liệu khoa học sự sống** của các nhà nghiên cứu Nhật Bản dưới dạng tài sản công quốc gia (ví dụ *Coral Reef Network WEB System* từng đặt tại `godac.jp/coral/`, *DoBISCUIT* của NITE), chuẩn hóa metadata CSV/JSON và giấy phép mở (như CC BY-SA) [A-S2-C7, VERIFIED — `R3` mở trực tiếp].
- **Other:** Không tìm thấy bằng chứng sơ cấp trực tiếp cho khu vực châu Phi hoặc Mỹ Latinh trong lượt tìm kiếm này (các truy vấn: `academic bioinformatics web tools URL decay database survival study 2023 2024 2025 2026`, `"Project Endings" UVic digital humanities static web preservation grant funding`, `"Software Heritage" OR "Code Ocean" OR "mybinder" OR "EaaSI"`).

### d. Demand and consequences of inaction

- **Nhu cầu được chứng minh (Demonstrated):** Có bằng chứng hành vi rõ ràng ở cấp **tổ chức** (không phải cá nhân PI): UVic (Canada) xây bộ nguyên tắc Endings, King's Digital Lab (Anh) đầu tư chương trình chuyển đổi di sản số (2026), JST/NBDC (Nhật Bản) vận hành kho lưu trữ quốc gia cho 89 DB khoa học sự sống, và khu vực thương mại/NXB chi trả cho Code Ocean (`R1`, `R2`, `R3`, `R5`).
- **Hệ quả nếu không hành động:** (1) Đứt gãy khả năng tái lập và kiểm chứng khoa học (link rot trong bài báo đã xuất bản); (2) Lãng phí đầu tư công nhiều năm cho các bộ dữ liệu/công cụ chuyên ngành; (3) Tuy nhiên, **phản chứng quan trọng:** một phần lớn công cụ web học thuật có lượt trích dẫn thấp tự nhiên trở nên lỗi thời và được thay thế bởi công cụ tốt hơn — không phải mọi web app chết đều gây thiệt hại khoa học đáng kể (`A-S2-C2`, INFERENCE).

### e. Existing solutions and limits

| Giải pháp mạnh nhất đã kiểm tra | Cơ chế hoạt động | Giới hạn thực tế |
|---|---|---|
| **Project Endings / Wax / tĩnh hóa thủ công** (`R1`) | Thiết kế từ đầu hoặc biên dịch dự án DH thành HTML/CSS/JS tĩnh + XML chuẩn mở | Đòi hỏi thiết kế ngay từ đầu hoặc công sức kỹ sư lớn để chuyển đổi ứng dụng legacy đã viết động; không áp dụng được cho tính toán server-side nặng |
| **NBDC LSDB Archive / Zenodo** (`R3`) | Lưu trữ bộ dữ liệu phẳng (CSV/JSON/dump) kèm metadata và giấy phép rõ ràng | Chỉ giữ được **dữ liệu**, mất hoàn toàn giao diện tra cứu tương tác và logic ứng dụng web ban đầu |
| **Webrecorder / Browsertrix / ReplayWeb.page** (`R7`) | Thu thập qua trình duyệt thực (WACZ) và phát lại không cần server | Không tái tạo được truy vấn động vào cơ sở dữ liệu lớn hoặc tính toán mới ngoài các đường dẫn đã crawl |
| **Code Ocean** (`R5`) | Đóng gói Compute Capsules (code + data + môi trường) chạy trên cloud | Mô hình SaaS thương mại giá cao hướng tới pharma/NXB và pipeline phân tích; không thiết kế để hồi sinh web app tương tác công cộng sau grant |
| **EaaSI** (`R6`) | Giả lập hệ điều hành và phần mềm cũ | Nặng về vận hành/cấp phép, tập trung vào phần mềm desktop/OS cũ hơn là web app hiện đại |

### f. Barriers

- **Pháp lý:** Giấy phép mã nguồn không rõ ràng (nhiều dự án học thuật không gắn license), dữ liệu bên thứ ba có điều khoản hạn chế tái phân phối (ví dụ dữ liệu y sinh/con người), hoặc thương hiệu đại học.
- **Tài chính:** Lệch pha thời điểm — khi ứng dụng cần bảo tồn nhất (sau khi hết grant) là lúc không còn ngân sách. Chưa tìm thấy bằng chứng giao dịch mua **công cụ phần mềm thương mại** riêng lẻ cho việc "tĩnh hóa ứng dụng sau grant" (kiểm định `H0` của Task B: tổ chức trả tiền cho **nhân sự kỹ thuật nội bộ / SLA / lưu trữ**, không thấy thị trường công cụ đóng gói sẵn) [A-S2-C8, INFERENCE].
- **Kỹ thuật:** Độ đa dạng cực cao của ngăn xếp cũ (PHP 5, Python 2, Java Applets, Flash, MySQL/PostgreSQL tùy biến); nhiều ứng dụng tin sinh học cần backend tính toán nặng không thể chuyển thành static/WASM.
- **Tổ chức:** Thiếu người sở hữu (owner) sau khi PI đổi hướng hoặc nghiên cứu sinh tốt nghiệp; phòng IT đại học ưu tiên cắt rủi ro bảo mật (tắt server cũ) hơn là bảo tồn.

### g. Who pays, who maintains

- **Ai trả tiền (Payer):** Không phải PI cá nhân. Người có ngân sách thực tế là **thư viện đại học / phòng lab Digital Scholarship** (như KDL, UVic), **quỹ tài trợ nghiên cứu** (nếu yêu cầu đưa chi phí "afterlife" vào đề xuất grant từ đầu), và **hạ tầng quốc gia** (NBDC, ELIXIR).
- **Ai duy trì (Maintainer):** Đội ngũ Research Technical Professionals (RTPs) / kỹ sư thư viện số tại đại học, hoặc cộng đồng mã nguồn mở nếu công cụ đủ phổ biến.

### h. AI: meaningful advantage or not

- **Đánh giá trung thực:** Với tĩnh hóa thuần túy (crawl HTML, xuất dump dữ liệu, chạy container), kỹ thuật phần mềm tất định (Browsertrix, HTTrack, Docker, static site generators) **không cần AI**.
- **Nơi AI có thể tạo lợi thế thực chất (cần kiểm chứng):** Phân tích mã nguồn legacy không tài liệu (PHP/Python 2/Perl CGI cũ) để sinh đặc tả schema, tự động viết lớp chuyển đổi sang giao diện tĩnh / SQLite-WASM, và kiểm chứng hồi quy hành vi so với ứng dụng gốc (có oracle kiểm thử rõ ràng: kết quả truy vấn khớp giữa bản gốc và bản tĩnh/WASM) [A-S2-C9, HYPOTHESIS — chưa có benchmark kiểm chứng].

### i. Preservation vs restoring functionality

- **Phục hồi chức năng có tạo thêm giá trị không?** **Có, nhưng có điều kiện.** NBDC LSDB Archive (`R3`) cho thấy lưu trữ dữ liệu phẳng giữ được giá trị cốt lõi cho nhà tin sinh học có kỹ năng lập trình. Tuy nhiên, với người dùng liên ngành (nhà sử học, ngôn ngữ học, nhà sinh học thực nghiệm không viết code), một file dump SQL/XML mất khả năng tra cứu, lọc, trực quan hóa — khôi phục chức năng tra cứu/tương tác ở dạng tĩnh hoặc WASM tạo giá trị sử dụng thực sự mà không gánh chi phí server [A-S2-C10, INFERENCE]. Ngược lại, khôi phục chức năng tính toán server-side nặng là không bền vững về chi phí.

### j. Resurrection theme fit

- **Kiểm định nghiêm ngặt theo anchor `theme`:**
  - Nếu đặt S2 ở phạm vi rộng ("duy trì web app học thuật sau grant"): **không có một công nghệ chết cụ thể làm trung tâm** → chỉ đạt **`theme` = 2** (trượt cổng ≥ 3), vì bản chất là bài toán tài trợ/DevOps.
  - Nếu **thu hẹp (`A-S2a`)** vào hồi sinh các ứng dụng nghiên cứu bị kẹt trên **runtime/công nghệ web đã chính thức khai tử** (ví dụ Python 2 EOL 2020, PHP 5/7 EOL, Adobe Flash / Java Applets trong công cụ DH & sinh học cũ) sang dạng tĩnh/WASM chạy trực tiếp trên trình duyệt hiện đại: có mỏ neo công nghệ đã nghỉ hưu chính thức → đạt **`theme` = 3** (vừa qua cổng). Tuy nhiên, đây vẫn yếu hơn các ý tưởng hồi sinh một sản phẩm chết mang tính biểu tượng (`theme` = 4–5).

### k. Verdict for this space

- **Kết luận:** **Thu hẹp (`narrow`) sang `A-S2a` — Chuyển đổi/hồi sinh các ứng dụng tra cứu nghiên cứu nhẹ (Digital Humanities & bộ dữ liệu nhỏ) đang chạy trên ngăn xếp đã khai tử sang gói tĩnh/WASM tự chạy cho thư viện đại học & phòng lab nghiên cứu.**
- **Bằng chứng quyết định:** Có nhu cầu tổ chức được chứng minh ở cả 3 khu vực NA (UVic Endings), EU (KDL), Asia (NBDC); khôi phục chức năng tra cứu nhẹ tạo giá trị rõ hơn lưu dump tĩnh; nhưng phải loại bỏ các app tính toán server-side nặng (không tĩnh hóa được — cần chạy phép thử `H8` trước khi cam kết) và phải neo chặt vào runtime đã khai tử để vượt cổng `theme ≥ 3`.

---

## 3. T2 — Small-platform shutdown window

### a. Problem and root causes

- **Vấn đề thực tế:** Khi các nền tảng SaaS nhỏ, dịch vụ hosting ứng dụng hoặc mạng xã hội/cộng đồng ngách đóng cửa, người dùng và người quản trị chỉ có một **cửa sổ thời gian ngắn** (thường 1–6 tháng) để di chuyển nội dung, mã nguồn và ngữ cảnh sang nơi kế nhiệm trước khi mọi thứ bị xóa vĩnh viễn hoặc biến thành bản lưu phẳng mất cấu trúc [A-T2-C1, VERIFIED — xác nhận độc lập qua 2 ca chính thức mở trực tiếp: Glitch `R8` và Cohost `R10`].
- **Cây nguyên nhân gốc:**
  ```text
  Tài sản cộng đồng / người dùng mất hoặc bị phẳng hóa khi nền tảng nhỏ đóng cửa
  ├─ 1. Kinh tế vận hành không bền vững ở quy mô ngách
  │   ├─ Chi phí hạ tầng + chống lạm dụng (bad actors) tăng theo tuổi nền tảng (Glitch [R8])
  │   └─ Doanh thu thuê bao không bù chi phí (Cohost: thâm hụt ~17.000 USD/tháng [R26, snippet])
  ├─ 2. Cửa sổ đóng cửa ngắn và công cụ export chắp vá
  │   ├─ Đội ngũ kiệt sức/giải thể chỉ kịp làm export cơ bản (thiếu media, bình luận, liên kết nội bộ)
  │   └─ Cào dữ liệu từ bên ngoài (ArchiveTeam) gặp rate-limit, API động (tRPC), timeout [R10]
  └─ 3. Khoảng trống pháp lý và chuẩn chuyển đổi
      ├─ DTI/DTP chỉ kết nối nền tảng lớn đang sống [R12]
      └─ EU Data Act điều chỉnh nhà cung cấp đang hoạt động, không cứu nền tảng phá sản [R11]
  ```
- **Khi nào bảo tồn KHÔNG có cơ sở:**
  1. Nền tảng không có cộng đồng gắn kết hoặc nội dung chủ yếu là bản sao chéo từ nền tảng khác.
  2. Người dùng không muốn dữ liệu cá nhân/bài đăng của mình bị sao lưu công khai sang nơi khác (vi phạm quyền riêng tư / quyền được xóa).
  3. Đã có đường di cư chuẩn 1-nhấp hoạt động tốt (ví dụ dự án mã nguồn mở trên Glitch vốn có thể xuất sang GitHub và triển khai lại trên Netlify/Fly.io như chính Glitch hướng dẫn `R8`).

### b. Stakeholders and target users

| Tác nhân (Actor) | Job-to-be-Done (JTBD) | Hành vi hiện tại | Sẵn lòng đóng góp / trả tiền | Demonstrated vs Hypothetical | Bằng chứng |
|---|---|---|---|---|---|
| Nhà vận hành nền tảng nhỏ sắp đóng cửa (ví dụ Cohost, Glitch, Ameba Ownd) | Đóng cửa có trách nhiệm, giảm phản ứng dữ dội và tuân thủ nghĩa vụ hoàn tiền/dữ liệu với chi phí tối thiểu | Dành 1–3 tháng cuối mở chế độ read-only, viết script export cơ bản, tạo redirect tạm thời hoặc hợp tác với ArchiveTeam | **Gần như bằng 0** (đang thua lỗ/giải thể; chỉ bỏ giờ kỹ sư nội bộ tối thiểu) | **Demonstrated** (về hành vi đóng cửa, **không** có WTP mua công cụ) | `R8` (mở trực tiếp), `R10` (mở trực tiếp), `R13` (mở trực tiếp) |
| Tình nguyện viên lưu trữ cộng đồng (ArchiveTeam, cộng đồng tự lưu trữ) | Cứu toàn bộ nội dung công khai trước ngày tắt server | Tự viết crawler/grabber thủ công (`cohost-grab`, `ArchiveBot`), xử lý tRPC/pagination, xin nhà vận hành gia hạn | **Giờ công tình nguyện cao**, **không** trả tiền mua phần mềm thương mại | **Demonstrated** | `R9` (mở trực tiếp), `R10` (mở trực tiếp) |
| Người sáng tạo nội dung / quản trị cộng đồng ngách (blogger, nghệ sĩ, chủ site nhỏ) | Chuyển bài viết, hình ảnh, liên kết sang nền tảng kế nhiệm (WordPress, Mastodon, GitHub Pages) mà không vỡ link/mất ảnh | Tự tải file export, dùng script cộng đồng hoặc mất trắng ảnh/bình luận khi export chỉ chứa URL ảnh | **Thấp / Chưa chứng minh** (nhu cầu xảy ra 1 lần đột xuất, ít sẵn sàng trả thuê bao) | **Mixed** (hành vi tải export có thật; WTP cho công cụ trả phí chưa chứng minh) | `R8`, `R27` (snippet Ameba Ownd) |
| Doanh nghiệp SME dùng SaaS (EU) | Chuyển dữ liệu sang nhà cung cấp mới không bị khóa chặt (vendor lock-in) | Dựa vào quy định chuyển đổi của EU Data Act (có hiệu lực 12/09/2025) | **Có** (cho dịch vụ di cư B2B), nhưng thuộc nhóm *SaaS đang sống*, không phải *shutdown* | **Demonstrated** (quy định), **Hypothetical** (cho công cụ shutdown) | `R11` (mở trực tiếp) |

### c. Documented cases by region

- **North America (NA):**
  - *Glitch (Mỹ, 2025):* Ngày 22/05/2025, Glitch chính thức thông báo ngừng dịch vụ hosting ứng dụng và hồ sơ người dùng vào **08/07/2025** ("hàng triệu người dùng chạy hàng chục triệu ứng dụng") do chi phí vận hành và chống lạm dụng tăng cao; mở bảng điều khiển đến hết 31/12/2025 để tải mã nguồn và cài đặt subdomain redirect (duy trì tối thiểu hết 2026) [A-T2-C2, VERIFIED — thông báo chính thức mở trực tiếp `R8`, đối chứng độc lập bởi ArchiveTeam `R9`].
  - *Cohost (Mỹ, 2024–2025):* Nền tảng mạng xã hội phi lợi nhuận (Anti Software Software Club) thông báo đóng cửa tháng 09/2024 do kiệt sức và thâm hụt tài chính (~17.000 USD/tháng, snippet `R26`), chuyển read-only 01/10/2024 và tắt hẳn tháng 01/2025. Nhật ký kỹ thuật ArchiveTeam cho thấy tốc độ crawl chỉ ~15 mục/phút, lỗi timeout trên mục lớn, phụ thuộc tRPC batch, và **ngày 01/01/2025 đội ngũ Cohost phải thông báo giữ server sống cho đến khi ArchiveTeam thu thập xong** [A-T2-C3, VERIFIED — `R10` mở trực tiếp; xác nhận Task B `B-O2-C3`].
  - *Skiff (Mỹ, 2024):* Bị Notion mua lại 02/2024 và đóng toàn bộ dịch vụ 08/2024, buộc người dùng xuất MBOX/EML trong cửa sổ 6 tháng [A-T2-C4, INFERENCE — snippet].
- **Europe (EU):**
  - *EU Data Act (Regulation (EU) 2023/2854):* Có hiệu lực từ 11/01/2024 và **áp dụng chính thức từ 12/09/2025**, đặt quy tắc hài hòa về quyền truy cập và chuyển đổi dữ liệu đám mây/SaaS tại EU [A-T2-C5, VERIFIED — trang chính sách Ủy ban châu Âu mở trực tiếp `R11`; chi tiết lộ trình cấm phí egress 12/01/2027 từ snippet pháp lý → INFERENCE]. Lưu ý: chưa tìm thấy trường hợp đóng cửa nền tảng cộng đồng nhỏ *cụ thể tại châu Âu* năm 2024–2026 có nhật ký kỹ thuật export mở trực tiếp trong lượt tìm kiếm này (truy vấn: `"European" community platform OR SaaS shutdown export migration 2024 2025 2026`).
- **Asia:**
  - *Ameba Ownd (CyberAgent, Nhật Bản, 2026):* Dịch vụ tạo website/blog thông báo ngừng hoạt động (dự kiến 24/12/2026, sau đó gia hạn đến 31/03/2027 theo các nguồn tổng hợp Nhật Bản `R27`, snippet; cổng trợ giúp chính thức `help.amebaownd.com` mở trực tiếp `R13`). Tính năng export ra mắt tháng 11/2026 nhưng **không đính kèm file ảnh** (chỉ xuất URL ảnh — sẽ chết sau ngày đóng cửa nếu người dùng không kịp nhập sang WordPress/Ameblo) và loại trừ thiết kế, bình luận, tên miền riêng [A-T2-C6, INFERENCE — chi tiết kỹ thuật từ snippet `R27`].
  - *Cyworld (Hàn Quốc):* Đóng/gián đoạn nhiều lần; nỗ lực hồi sinh thương mại (Cy Communications tiếp quản cuối 2024) vẫn kẹt ở khâu khôi phục dữ liệu cũ [A-T2-C7, INFERENCE — snippet].
- **Other:** Không tìm thấy bằng chứng sơ cấp trực tiếp cho châu Phi hoặc Mỹ Latinh (các truy vấn trên).

### d. Demand and consequences of inaction

- **Nhu cầu được chứng minh (Demonstrated):** Hành vi cứu hộ khẩn cấp mỗi khi nền tảng đóng là **có thật và lặp đi lặp lại** (ArchiveTeam huy động hạ tầng cho cả Cohost lẫn Glitch; Glitch phải xây tính năng subdomain redirect; Ameba Ownd phải gia hạn ngày tắt và mở công cụ export).
- **Hệ quả nếu không hành động:** Mất vĩnh viễn tài liệu hướng dẫn, tác phẩm sáng tạo, mã nguồn nhỏ và hàng triệu liên kết web bị gãy (link rot) — ví dụ các URL ảnh trên Ameba Ownd hoặc redirect trên Glitch sau năm 2026.
- **Phản chứng quan trọng:** Hành vi tải export khi bị ép buộc **không** đồng nghĩa với nhu cầu mua một công cụ mới. Trong ca Glitch, các đối thủ đang sống (Fly.io, Netlify, GitHub Pages, Val Town) trực tiếp hỗ trợ importer để hút người dùng (`R8`).

### e. Existing solutions and limits

| Giải pháp mạnh nhất đã kiểm tra | Cơ chế hoạt động | Giới hạn thực tế |
|---|---|---|
| **Data Transfer Initiative (DTI) / Data Transfer Project (DTP)** (`R12`) | Khung mã nguồn mở kết nối API trực tiếp giữa các nền tảng lớn (hơn một chục dịch vụ như Google Photos, Facebook) + Data Trust Registry | Chỉ bao phủ nền tảng lớn **đang hoạt động**; nền tảng nhỏ sắp phá sản không có nguồn lực tích hợp adapter DTP hay tham gia registry |
| **ArchiveTeam + Wayback Machine** (`R9`, `R10`) | Thu thập phân tán từ bên ngoài (WARC) lưu trên Internet Archive | Chậm, dễ vỡ trước SPA/tRPC/rate-limit, không lưu được dữ liệu riêng tư/đăng nhập, và phụ thuộc sự hợp tác giờ chót của nhà vận hành |
| **Webrecorder / Browsertrix** (`R7`) | Thu thập bằng trình duyệt thực tạo gói WACZ phát lại không cần server | Tốt cho lưu trữ tĩnh để *đọc*, không chuyển đổi dữ liệu có cấu trúc (bài viết, thẻ, quan hệ) để *nhập* sang nền tảng kế nhiệm |
| **Export gốc của từng nền tảng** (`R8`, `R13`) | Tải ZIP/JSON/WXR/Git từ dashboard trước khi tắt | Không đồng nhất; thường mất ảnh nhúng (Ameba Ownd), mất đồ thị bình luận/tương tác, không có trình xem offline sẵn |

### f. Barriers

- **Pháp lý:** Quyền riêng tư (GDPR — đặc biệt quyền được xóa và dữ liệu của người dùng thứ ba trong bình luận/repost), điều khoản sử dụng cấm cào dữ liệu nếu không có sự đồng ý của nhà vận hành, bản quyền nội dung người dùng.
- **Tài chính:** **Rào cản chí tử.** Nền tảng sắp đóng đang cạn tiền; người dùng cá nhân chịu sự kiện đột xuất 1 lần nên rất khó thu phí định kỳ.
- **Kỹ thuật:** Mỗi nền tảng có lược đồ (schema) nội bộ, cách nhúng media và cấu trúc hội thoại khác nhau; không thể bảo tồn đồ thị xã hội sống (ai theo dõi ai trên nền tảng mới).
- **Tổ chức:** Quyết định đóng cửa thường được giữ kín đến phút chót vì lý do pháp lý/kinh doanh, để lại cửa sổ chuẩn bị quá ngắn.

### g. Who pays, who maintains

- **Ai trả tiền (Payer):** **Chưa tìm thấy người trả tiền rõ ràng (`none found`)** cho một công cụ thương mại chuyên xử lý cửa sổ đóng cửa của nền tảng nhỏ [A-T2-C8, VERIFIED — không có giao dịch/hợp đồng công cụ nào được ghi nhận sau khi kiểm tra Glitch, Cohost, DTI và EU Data Act; đồng thuận với giả thuyết `H0` của Task B].
- **Kịch bản tài trợ khả dĩ duy nhất:** (1) Các nền tảng kế nhiệm trả tiền làm importer để thu hút người dùng di cư (nhưng họ tự xây importer riêng, như gợi ý trong bài blog Glitch `R8`); (2) Quỹ phi lợi nhuận / mã nguồn mở (tương tự Webrecorder, Internet Archive, DTI).
- **Ai duy trì (Maintainer):** Cộng đồng mã nguồn mở hoặc tổ chức phi lợi nhuận bảo tồn web.

### h. AI: meaningful advantage or not

- **Đánh giá trung thực:** **Không bắt buộc (`unnecessary` cho trường hợp có chuẩn, `useful` cho export hỗn loạn).**
- Khi nền tảng có định dạng chuẩn (Git repo trên Glitch, ActivityPub/AS2.0 trên Mastodon, WXR trên blog), bộ chuyển đổi tất định (deterministic parser) nhanh, rẻ, chính xác 100% và không bị ảo giác.
- AI chỉ có thể hữu ích khi phải suy diễn lược đồ từ gói export JSON/HTML không tài liệu hoặc tái liên kết tài sản bị rời rạc — nhưng ngay cả điều này vẫn là **giả thuyết chưa kiểm chứng** (cần phép thử `H2` của Task B so sánh với parser viết tay).

### i. Preservation vs restoring functionality

- **Phục hồi chức năng có tạo thêm giá trị không?** **Có ở mức "khả năng đọc/tra cứu & di cư" (`restoration-adds-value`), KHÔNG ở mức "chạy lại mạng xã hội sống".**
- Một file JSON/ZIP thô hay WXR chứa URL ảnh chết (như Ameba Ownd) gần như vô dụng với người dùng phổ thông. Chuyển gói export thành một **kho lưu trữ cục bộ tự chạy có tìm kiếm, giữ nguyên ảnh/luồng hội thoại** hoặc **đóng gói sẵn để nhập vào nền tảng kế nhiệm** tạo giá trị thực tế hơn hẳn lưu file thô. Ngược lại, cố giữ nền tảng cũ chạy sống lặp lại đúng thất bại kinh tế ban đầu (Task B `problem-analysis.md §1`).

### j. Resurrection theme fit

- **Kiểm định theo anchor `theme`:**
  - Mỗi nền tảng đóng cửa (Cohost, Glitch, Ameba Ownd, Skiff) là một **dịch vụ/sản phẩm cụ thể đã chính thức ngừng hoạt động**. Nếu công cụ neo vào việc hồi sinh gói export của các nền tảng đã chính thức khai tử (ví dụ Cohost / Glitch / nền tảng blog đóng cửa) thành kho tương tác cục bộ hoặc chuyển sang chuẩn mở hiện đại, không gian này đạt **`theme` = 3** (khớp với Task B: một công nghệ/nền tảng có thông báo nghỉ hưu chính thức làm mỏ neo cho quy trình được hồi sinh).

### k. Verdict for this space

- **Kết luận:** **Thu hẹp (`narrow`) sang `A-T2a` — Công cụ/quy trình chuyển đổi gói export trước khi đóng cửa (của nền tảng cộng đồng/blog/web nhỏ đã chính thức thông báo tắt) thành kho tĩnh có thể tìm kiếm hoặc gói di cư bảo toàn media & ngữ nghĩa.**
- **Bằng chứng quyết định:** Bằng chứng ca thực tế rất mạnh và mới (2024–2026) trên cả 3 khu vực NA (Glitch, Cohost), EU (EU Data Act), Asia (Ameba Ownd), vượt cổng `theme` (= 3). **Tuy nhiên, cảnh báo nghiêm trọng:** không có người trả tiền rõ ràng (`payer: none found`) và vai trò AI yếu — cần chạy phép thử `H2` để chứng minh tổn thất ngữ nghĩa trong export thật có đáng để xây công cụ mới vượt qua parser viết tay hay không.

---

## 4. T3 — Disappearing journals

### a. Problem and root causes

- **Vấn đề thực tế:** Một tỷ lệ đáng kể tạp chí học thuật trực tuyến — đặc biệt các tạp chí Truy cập mở Kim cương (Diamond OA, không thu phí tác giả/độc giả), tạp chí quy mô nhỏ do học giả hoặc hội khoa học địa phương vận hành — biến mất khỏi web hoặc không có bản sao lưu được xác nhận trong các kho bảo tồn dài hạn [A-T3-C1, VERIFIED — Laakso, Matthias & Jahn `R14` mở trực tiếp].
- **Cây nguyên nhân gốc:**
  ```text
  Tạp chí học thuật nhỏ biến mất khỏi web
  ├─ 1. Thiếu tham gia vào hạ tầng bảo tồn ĐÃ CÓ SẴN
  │   ├─ Ban biên tập thiếu nhận thức hoặc thiếu nhân lực kỹ thuật tối thiểu để đăng ký (DOAJ/JASPER [R15])
  │   └─ Chi phí thiết lập/phí thường niên ở kho thương mại (CLOCKSS/Portico) vượt ngân sách tạp chí nhỏ
  ├─ 2. Đứt gãy tài trợ và nhân sự tình nguyện
  │   ├─ Tạp chí phụ thuộc 1–2 tổng biên tập hoặc một khoa/hội khoa học; nghỉ hưu hoặc hết tài trợ là sập web
  │   └─ Quên gia hạn tên miền hoặc tắt máy chủ trường đại học
  └─ 3. Lỗi thời phần mềm xuất bản (nguyên nhân thứ cấp)
      └─ Một số tạp chí vẫn kẹt trên OJS 2.x (đã EOL từ 2021) nên không cài được plugin mới/dễ bị hack [R28, snippet]
  ```
- **Khi nào bảo tồn KHÔNG có cơ sở:**
  1. Tạp chí săn mồi (predatory journals) hoặc tạp chí không có quy trình bình duyệt thực chất, nội dung rác/đạo văn (tranh luận học thuật ngay sau bài Laakso 2021 cũng nêu câu hỏi về tỷ lệ tạp chí săn mồi trong mẫu).
  2. Nội dung đã được lưu trữ đầy đủ tại kho quốc gia/khu vực (như J-STAGE, SciELO, PubMed Central) hoặc ít nhất 3 Keepers.

### b. Stakeholders and target users

| Tác nhân (Actor) | Job-to-be-Done (JTBD) | Hành vi hiện tại | Sẵn lòng đóng góp / trả tiền | Demonstrated vs Hypothetical | Bằng chứng |
|---|---|---|---|---|---|
| Tổng biên tập / NXB tạp chí Diamond OA nhỏ | Xuất bản và giữ bài báo tồn tại lâu dài với ngân sách ≈ 0 và ít kỹ năng IT | Dùng OJS (hơn 58.000 tạp chí toàn cầu, snippet `R28`), nhiều nơi chưa bật PKP PN hoặc chưa đăng ký JASPER | **Rất thấp / 0** (tạp chí không thu APC) | **Demonstrated** (về thiếu nguồn lực) | `R15` (mở trực tiếp), `R17` (mở trực tiếp) |
| Thư viện nghiên cứu & liên minh bảo tồn (CLOCKSS, Portico, PKP, DOAJ, ISSN Keepers) | Bảo vệ toàn vẹn hồ sơ học thuật toàn cầu, mở công khai khi có "trigger event" | Vận hành hạ tầng quy mô lớn: Portico (1.479 NXB, 1.318 thư viện, 235 trigger events, 43.934 tạp chí `R20`), CLOCKSS (12 node `R19`), PKP PN (miễn phí `R16`), JASPER (`R15`) | **Có** (ngân sách thành viên thư viện & phí NXB) | **Demonstrated** | `R15`, `R16`, `R18`, `R19`, `R20` (đều mở trực tiếp) |
| Nền tảng khu vực / quốc gia (J-STAGE Nhật, SciELO Mỹ Latinh, AJOL châu Phi) | Lưu trữ, chuẩn hóa và tăng tiếp cận cho tạp chí trong khu vực | Vận hành nền tảng tập trung: J-STAGE (JST tài trợ `R21`), SciELO (`R22`), AJOL (phi lợi nhuận chạy bằng quyên góp, hàng triệu lượt tải/tháng `R23`) | **Có** (nhà nước / tài trợ phi lợi nhuận) | **Demonstrated** | `R21`, `R22`, `R23` (đều mở trực tiếp) |

### c. Documented cases by region

- **Global / Europe (EU):**
  - *Laakso, Matthias & Jahn (2020/2021):* Nghiên cứu sơ cấp đối chiếu Scopus, Ulrichsweb, DOAJ và Wayback Machine xác định **174 tạp chí OA đã biến mất hoàn toàn khỏi web trong giai đoạn 2000–2019**, trải rộng trên tất cả các lĩnh vực nghiên cứu chính và mọi khu vực địa lý [A-T3-C2, VERIFIED — bản arXiv:2008.11933 mở trực tiếp `R14`].
  - *Martin Paul Eve (2024):* Phân tích 7,4 triệu bài báo có Crossref DOI, ghi nhận **27,64% (~2,05 triệu) không tìm thấy xác nhận lưu trữ** trong các kho khảo sát (lưu ý: không đồng nghĩa đã biến mất; phù hợp kiểm định `C-G-C1` của Task B) [A-T3-C3, INFERENCE — bài gốc `jlsc.16288` bị chặn anti-bot, chỉ đọc qua snippet `R29`].
  - *Project JASPER (DOAJ, CLOCKSS, IA, Keepers, PKP):* Ra mắt năm 2020 để khắc phục trực tiếp tình trạng NXB nhỏ không nhận thức được hoặc thiếu nguồn lực tham gia bảo tồn [A-T3-C4, VERIFIED — `R15` mở trực tiếp].
- **North America (NA):**
  - *PKP Preservation Network (Simon Fraser University, Canada) & Portico (Mỹ):* PKP PN cung cấp bảo tồn miễn phí cho tạp chí dùng OJS (`R16`); Portico đã kích hoạt **235 sự kiện "trigger event"** mở quyền truy cập cho nội dung có nguy cơ mất (`R20`) [A-T3-C5, VERIFIED — `R16`, `R20` mở trực tiếp].
- **Asia:**
  - *J-STAGE (JST, Nhật Bản):* Hạ tầng quốc gia lưu trữ và xuất bản điện tử cho hàng nghìn tạp chí hội khoa học Nhật Bản (vẫn cập nhật số mới tháng 11/2026) [A-T3-C6, VERIFIED — `R21` mở trực tiếp].
- **Other (Latin America & Africa):**
  - *SciELO (Brazil / Mỹ Latinh):* Mạng lưới xuất bản và bảo tồn khoa học mở khu vực (`R22` mở trực tiếp).
  - *AJOL (châu Phi):* Tổ chức phi lợi nhuận (từ 1998) vận hành bằng quyên góp, phục vụ hàng triệu lượt tải bài báo châu Phi mỗi tháng (>50% từ người dùng lặp lại tại châu Phi) với khung đánh giá chất lượng JPPS (`R23` mở trực tiếp) [A-T3-C7, VERIFIED — `R22`, `R23` mở trực tiếp].

### d. Demand and consequences of inaction

- **Nhu cầu được chứng minh (Demonstrated):** Có bằng chứng định lượng rất mạnh ở cấp **hệ thống học thuật** (174 tạp chí biến mất, 235 trigger events của Portico, 1.318 thư viện trả phí thành viên Portico, hàng triệu lượt tải trên AJOL).
- **Hệ quả nếu không hành động:** Mất vĩnh viễn trích dẫn khoa học, đặc biệt là tri thức bản địa/khu vực (y tế công cộng, lịch sử, sinh thái địa phương) vốn tập trung ở tạp chí Diamond OA nhỏ không thuộc các tập đoàn lớn.
- **Phản chứng quyết định:** Nhu cầu này **đã được đáp ứng về mặt hạ tầng kỹ thuật** bởi PKP PN (miễn phí), Project JASPER, CLOCKSS, Portico, J-STAGE, SciELO, AJOL. Nút thắt không nằm ở thiếu một ứng dụng/công cụ phần mềm mới, mà ở **tỷ lệ đăng ký tham gia và nhận thức của ban biên tập** (đồng thuận với Task B `B-O3`).

### e. Existing solutions and limits

| Giải pháp mạnh nhất đã kiểm tra | Cơ chế hoạt động | Giới hạn thực tế |
|---|---|---|
| **PKP Preservation Network (PKP PN)** (`R16`) | Plugin LOCKSS **miễn phí** tích hợp sẵn trong OJS | Chỉ hỗ trợ tạp chí chạy OJS (phiên bản còn hỗ trợ); nhiều tạp chí nhỏ không bật plugin hoặc chạy phiên bản quá cũ |
| **Project JASPER** (`R15`) | Cầu nối miễn phí của DOAJ + CLOCKSS + IA + Keepers + PKP cho tạp chí Diamond OA trong DOAJ | Quy mô onboarding còn chậm (chỉ áp dụng tạp chí đã vào DOAJ); vẫn cần ban biên tập chủ động tham gia |
| **CLOCKSS & Portico** (`R19`, `R20`) | Lưu trữ tối (dark archive) phân tán, mở truy cập khi có trigger event; CLOCKSS gắn giấy phép CC OA | Có phí thiết lập/thường niên (CLOCKSS: phí thiết lập tối thiểu $1.000 + $242/năm cho NXB nhỏ theo snippet; Portico theo doanh thu) — vượt khả năng tạp chí không ngân sách |
| **Keepers Registry (ISSN)** (`R18`) | Giám sát toàn cầu tình trạng bảo tồn của ấn phẩm có ISSN | Chỉ theo dõi/báo cáo, không tự lưu trữ nội dung |

### f. Barriers

- **Pháp lý:** Thấp hơn các không gian khác đối với tạp chí OA (đã có giấy phép Creative Commons); phức tạp hơn với tạp chí đóng bản quyền không ký thỏa thuận lưu trữ trước khi ngừng hoạt động.
- **Tài chính:** Tạp chí Diamond OA nhỏ không có doanh thu để trả phí lưu trữ thương mại hay thuê kỹ sư nâng cấp OJS.
- **Kỹ thuật:** Thiếu chuẩn metadata nhất quán (JATS XML, DOI, tệp dữ liệu bổ sung / supplementary files) ở tạp chí nhỏ không dùng OJS; nâng cấp từ OJS 2.x (EOL 2021) sang OJS 3.x đòi hỏi di chuyển kiến trúc.
- **Tổ chức:** **Rào cản số 1.** Ban biên tập làm việc kiêm nhiệm, thiếu nhận thức về bảo tồn số, và không có kế hoạch kế nhiệm khi tổng biên tập nghỉ hưu.

### g. Who pays, who maintains

- **Ai trả tiền (Payer):** Thư viện đại học (phí thành viên Portico/CLOCKSS/PKP), quỹ khoa học công (JST cho J-STAGE, chính phủ/quỹ khu vực cho SciELO), và nhà tài trợ phi lợi nhuận (AJOL). **Không** phải tạp chí nhỏ.
- **Ai duy trì (Maintainer):** Các liên minh tổ chức lâu đời (PKP, CLOCKSS, Portico, DOAJ, ISSN International Centre). Một công cụ hackathon mới rất khó chen vào chuỗi tin cậy học thuật này.

### h. AI: meaningful advantage or not

- **Đánh giá trung thực:** **Không cần thiết (`unnecessary`).**
- Quy trình bảo tồn tạp chí (thu thập OAI-PMH, đóng gói BagIt/LOCKSS, kiểm tra toàn vẹn checksum, đối chiếu Keepers Registry/DOI) hoàn toàn là kỹ thuật tất định chuẩn hóa. Việc bổ sung AI (ví dụ trích xuất metadata từ PDF cũ thiếu XML) chỉ là tiện ích phụ, không giải quyết nút thắt chính là tỷ lệ tham gia tổ chức.

### i. Preservation vs restoring functionality

- **Bảo tồn nội dung đã đủ (`preservation-sufficient`).**
- Khác với web app tương tác (S2), bài báo học thuật có giá trị cốt lõi nằm ở **văn bản, bảng biểu, hình ảnh, trích dẫn, DOI và tệp dữ liệu bổ sung** (PDF/HTML/JATS XML). Portico (`R20`) chứng minh rõ điều này: trong hơn 3,069 tỷ tệp được bảo tồn, chỉ có **160 tệp thực thi (executable files)**. Khi một tạp chí biến mất, người đọc cần tìm và tải lại bài báo có trích dẫn chuẩn (như trang trigger của CLOCKSS/Portico), không cần hồi sinh giao diện CMS cũ của tạp chí đó.

### j. Resurrection theme fit

- **Kiểm định nghiêm ngặt theo anchor `theme`:**
  - **Không tìm thấy góc độ Resurrection chính đáng.** Tạp chí học thuật (PDF/HTML/OJS) **không phải** công nghệ đã chết.
  - Đã kiểm tra giả thuyết phụ: *"Liệu OJS 2.x (EOL 2021) có phải mỏ neo Resurrection không?"* → **Bác bỏ.** OJS 2.x chỉ là phiên bản cũ của một phần mềm vẫn đang sống mạnh (OJS 3.5 LTS với >58.000 tạp chí), và OJS 2 EOL không phải nguyên nhân chính làm tạp chí biến mất (Laakso `R14` và DOAJ `R15` cho thấy nguyên nhân chính là tài chính và không tham gia lưu trữ). Cố gán OJS 2 thành "dead technology" sẽ bóp méo tinh thần cuộc thi.
  - **Điểm `theme` tạm thời:** **1** (trượt cổng ≥ 3, xác nhận kết quả Task B).

### k. Verdict for this space

- **Kết luận:** **Loại (`drop`).**
- **Bằng chứng quyết định:** (1) **Trượt cổng chủ đề Kiroween (`theme` = 1)** — không có công nghệ đã khai tử thực sự làm trung tâm; (2) Hạ tầng kỹ thuật bảo tồn đã trưởng thành và miễn phí cho đối tượng yếu thế (PKP PN, JASPER, J-STAGE, SciELO, AJOL) — nút thắt là nhận thức/tổ chức, không phải thiếu công cụ mới; (3) AI không cần thiết (`unnecessary`) và bảo tồn nội dung đã đủ (`preservation-sufficient`).

---

## 5. T4 — Heritage archive transfer

### a. Problem and root causes

- **Vấn đề thực tế:** Các kho lưu trữ di sản số (ngôn ngữ có nguy cơ tuyệt chủng, văn hóa bản địa, lịch sử cộng đồng) đối mặt nguy cơ gián đoạn hoặc mất quyền kiểm soát ngữ cảnh khi đơn vị chủ quản (trường đại học, viện nghiên cứu, tổ chức cơ sở) hết tài trợ, đổi ưu tiên, hoặc phần mềm lưu trữ cũ hết vòng đời hỗ trợ [A-T4-C1, INFERENCE — tổng hợp từ tài liệu Mukurtu `R24`, Kulu `R31`, ELAR `R30` snippet].
- **Cây nguyên nhân gốc:**
  ```text
  Kho di sản số gặp rủi ro khi chuyển giao hoặc bảo trì
  ├─ 1. Chuyển dịch chủ quản và tài trợ có kỳ hạn
  │   ├─ Viện/trường chủ quản thay đổi chiến lược hoặc hết dự án (ví dụ ELAR chuyển từ SOAS London sang BBAW Berlin năm 2021 [R30, snippet])
  │   └─ Tổ chức cộng đồng cơ sở thiếu hạ tầng IT ổn định (Kulu Language Institute, quần đảo Solomon [R31])
  ├─ 2. Yêu cầu quản trị quyền văn hóa phức tạp (không thể "lưu mở đại trà")
  │   ├─ Cultural Protocols, Traditional Knowledge (TK) Labels, phân quyền theo vai trò cộng đồng (Mukurtu [R24])
  │   └─ Chuyển đổi hệ thống dễ làm phẳng hóa hoặc sai lệch quy tắc truy cập nhạy cảm
  └─ 3. Lỗi thời nền tảng CMS nguồn mở
      └─ Drupal 7 chính thức EOL ngày 05/01/2025 [R32, snippet], ảnh hưởng trực tiếp Mukurtu 3 và Islandora 7 -> buộc xây lại (replatform) sang Drupal 10/11
  ```
- **Khi nào bảo tồn/chuyển giao KHÔNG có cơ sở:**
  1. Không có sự đồng thuận rõ ràng (Free, Prior and Informed Consent) từ cộng đồng sở hữu di sản — việc tự ý sao lưu/mở công khai kho di sản nhạy cảm gây tổn hại văn hóa và vi phạm đạo đức/pháp lý.
  2. Không có chủ thể kế nhiệm hợp pháp được cộng đồng ủy thác đứng ra tiếp nhận quyền quản trị.

### b. Stakeholders and target users

| Tác nhân (Actor) | Job-to-be-Done (JTBD) | Hành vi hiện tại | Sẵn lòng đóng góp / trả tiền | Demonstrated vs Hypothetical | Bằng chứng |
|---|---|---|---|---|---|
| Tổ chức cộng đồng / bản địa quản lý kho di sản (ví dụ cộng đồng dùng Mukurtu, Kulu Language Institute) | Lưu giữ ngôn ngữ/văn hóa và thực thi đúng quy tắc truy cập truyền thống (Cultural Protocols, TK Labels) | Dùng Mukurtu CMS (miễn phí), phối hợp với kho khu vực như PARADISEC/ELAR hoặc thuê Mukurtu Hosting / Reclaim Hosting | **Rất hạn chế** (phụ thuộc grant; phí migration cơ bản Mukurtu Hosting ~$350, Reclaim ~$100/năm theo snippet) | **Demonstrated** (hành vi lưu trữ & hợp tác) | `R24` (mở trực tiếp), `R31` (mở trực tiếp) |
| Trung tâm lưu trữ ngôn ngữ & di sản học thuật (ELAR/BBAW, PARADISEC, British Library EAP, CDSC WSU) | Tiếp nhận, chuẩn hóa và bảo quản dài hạn bộ sưu tập có nguy cơ mất | Chuyển đơn vị chủ quản (ELAR: SOAS → BBAW nhờ Arcadia Fund), xây tài liệu di chuyển Mukurtu 3 → 4, cấp grant số hóa | **Có** (tài trợ từ quỹ từ thiện như Arcadia Fund & ngân sách đại học) | **Demonstrated** | `R24`, `R30` (snippet) |
| Thư viện quốc gia (NDL WARP Nhật Bản, NLK OASIS Hàn Quốc) | Thu thập và lưu trữ di sản web/tài liệu quốc gia theo luật định | Vận hành kho lưu trữ nhà nước quy mô lớn (`warp.da.ndl.go.jp`) | **Có** (ngân sách quốc gia) | **Demonstrated** | `R33` (mở trực tiếp) |
| Thư viện đại học vận hành Islandora / Drupal 7 | Di chuyển bộ sưu tập số khỏi Drupal 7 (EOL 01/2025) sang nền tảng được hỗ trợ | Tự di chuyển hoặc thuê nhà cung cấp dịch vụ Drupal/Islandora (replatform sang Islandora 2 / Drupal 10–11) | **Có** (ngân sách IT thư viện / hợp đồng tư vấn Drupal) | **Demonstrated** | `R34` (mở trực tiếp), `R32` (snippet) |

### c. Documented cases by region

- **North America (NA):**
  - *Mukurtu CMS (Center for Digital Scholarship and Curation, Washington State University, Mỹ):* Tài liệu chính thức *Mukurtu User Manual* (`docs.mukurtu.org`) ghi nhận mô hình phân quyền chi tiết gồm **Communities, Cultural Protocols, Community Records, Legacy Traditional Knowledge Labels** và có hẳn mục riêng **"Mukurtu 3 Migration"** (Pre-Migration, Self-Hosted) để hỗ trợ các kho di sản chuyển từ Mukurtu 3 (nền Drupal 7) lên Mukurtu 4 [A-T4-C2, VERIFIED — `R24` mở trực tiếp].
  - *Islandora (Canada / Quốc tế):* Nền tảng quản lý tài sản số nguồn mở kết hợp Drupal + Solr + Fedora Commons + IIIF được nhiều thư viện và kho di sản sử dụng [A-T4-C3, VERIFIED — `R34` mở trực tiếp].
- **Europe (EU):**
  - *ELAR (Endangered Languages Archive):* Thành lập năm 2002 tại SOAS (London, Anh) và chuyển giao toàn bộ chủ quản cùng chương trình ELDP sang **Berlin-Brandenburg Academy of Sciences and Humanities (BBAW, Đức)** vào tháng 07/2021 với tài trợ của Arcadia Fund [A-T4-C4, INFERENCE — trang `/about/` yêu cầu đăng nhập và trang BBAW trả 404; thông tin xác nhận qua nhiều snippet `R30`].
  - *British Library Endangered Archives Programme (EAP, Anh):* Tài trợ số hóa tài liệu nguy cấp tại chỗ trên toàn cầu (URL `eap.bl.uk` trả HTTP 405 khi truy cập tự động → snippet-only).
- **Asia:**
  - *NDL WARP (National Diet Library Web Archiving Project, Nhật Bản):* Chương trình lưu trữ di sản web quốc gia do Thư viện Quốc hội Nhật Bản vận hành [A-T4-C5, VERIFIED — `R33` mở trực tiếp]. (Lưu ý: WARP tập trung di sản web công cộng theo luật, không chuyên về chuyển giao quyền văn hóa cộng đồng như Mukurtu.)
- **Other (Pacific / Australia):**
  - *Kulu Language Institute (Đảo Ranongga, Quần đảo Solomon):* Tổ chức cơ sở bản địa phục hồi hai ngôn ngữ **Kubokota (~3.400 người nói)** và **Luqa (~3.900 người nói)** [A-T4-C6, VERIFIED — trang chính thức `R31` mở trực tiếp; chi tiết hợp tác số hóa >100 giờ băng cassette với PARADISEC/ELDP từ snippet → INFERENCE].
  - *PARADISEC (Úc — Thái Bình Dương):* Liên minh 3 đại học Úc bảo quản tư liệu văn hóa/ngôn ngữ nguy cấp khu vực Thái Bình Dương (`paradisec.org.au` trả HTTP 403 → snippet-only).

### d. Demand and consequences of inaction

- **Nhu cầu được chứng minh (Demonstrated):** Có bằng chứng thực tế rõ ràng về **sự kiện chuyển giao và di cư nền tảng** (ELAR chuyển từ Anh sang Đức; Mukurtu phải xây quy trình di cư Mukurtu 3 → 4 sau Drupal 7 EOL ngày 05/01/2025; Kulu Language Institute hợp tác số hóa tư liệu bản địa).
- **Hệ quả nếu không hành động:** (1) Mất ngôn ngữ và tri thức văn hóa không thể thay thế; (2) Nếu kho Drupal 7 không được di chuyển, rủi ro bị tấn công bảo mật tăng cao (không còn bản vá sau 01/2025) dẫn đến lộ lọt tư liệu nhạy cảm hoặc bị đơn vị hosting tắt máy chủ; (3) Nếu sao lưu thô không giữ Cultural Protocols, cộng đồng mất chủ quyền dữ liệu.

### e. Existing solutions and limits

| Giải pháp mạnh nhất đã kiểm tra | Cơ chế hoạt động | Giới hạn thực tế |
|---|---|---|
| **Mukurtu 4 & Mukurtu 3 Migration Docs** (`R24`) | CMS nguồn mở chuyên biệt cho di sản bản địa (Cultural Protocols, TK Labels) + quy trình di cư chính thức từ Mukurtu 3 | Nâng cấp từ Drupal 7 sang Drupal 11 là **xây lại (replatform)**; các site có tùy biến (non-stock) vẫn cần hỗ trợ kỹ thuật chuyên sâu |
| **Islandora (Drupal + Fedora + IIIF)** (`R34`) | Kho quản lý tài sản số nguồn mở cấp tổ chức | Phức tạp về vận hành IT, vượt khả năng tự quản trị của tổ chức cộng đồng nhỏ |
| **ELAR / PARADISEC** (`R30`, snippet) | Kho lưu trữ ngôn ngữ học thuật được quỹ lớn tài trợ lâu dài | Năng lực tiếp nhận có giới hạn theo lĩnh vực (ngôn ngữ học) và phụ thuộc tài trợ tập trung |
| **Extended Security Support (Tag1 / HeroDevs) & Backdrop CMS** (`R32`, snippet) | Mua bản vá mở rộng cho Drupal 7 hoặc chuyển sang fork Drupal 7 | Chỉ là giải pháp tạm thời (ESS) hoặc không tương thích module đặc thù (Mukurtu) |

### f. Barriers

- **Pháp lý & Đạo đức (Rủi ro cao — `high`):** Chủ quyền dữ liệu bản địa (CARE Principles, Indigenous Data Sovereignty), quyền riêng tư, tư liệu thiêng/hạn chế giới tính hoặc dòng tộc; **không thể** dùng dữ liệu thật để demo hackathon công khai nếu không có sự đồng thuận bằng văn bản từ cộng đồng.
- **Tài chính:** Cộng đồng cơ sở không có ngân sách IT thường xuyên; phụ thuộc gần như hoàn toàn vào quỹ từ thiện (Arcadia, SSHRC, IMLS) và đại học.
- **Kỹ thuật:** Ánh xạ chính xác quyền truy cập (roles, Cultural Protocols, TK Labels) khi chuyển nền tảng mà không rò rỉ dữ liệu; dữ liệu đa phương tiện dung lượng lớn (audio/video/ảnh độ phân giải cao).
- **Tổ chức:** **Nút thắt lớn nhất.** Chuyển giao kho di sản đòi hỏi niềm tin lâu dài, đàm phán quản trị giữa cộng đồng và đơn vị tiếp nhận, và đào tạo nhân sự tại chỗ — công cụ phần mềm chỉ giải quyết phần rất nhỏ.

### g. Who pays, who maintains

- **Ai trả tiền (Payer):** Quỹ từ thiện văn hóa/ngôn ngữ (Arcadia Fund), quỹ nghiên cứu công, thư viện đại học và bộ văn hóa quốc gia.
- **Ai duy trì (Maintainer):** Trung tâm học thuật được tài trợ (WSU CDSC cho Mukurtu, BBAW cho ELAR, liên minh đại học Úc cho PARADISEC) cùng đội ngũ quản trị cộng đồng được đào tạo.

### h. AI: meaningful advantage or not

- **Đánh giá trung thực:** **Không cần thiết (`unnecessary`) cho lõi bài toán chuyển giao quyền & ngữ cảnh.**
- Ánh xạ quyền truy cập (ACL / Cultural Protocols / TK Labels) **đòi hỏi độ chính xác 100% mang tính tất định** — sai sót xác suất (hallucination) của AI trong phân quyền có thể làm rò rỉ tư liệu thiêng/nhạy cảm, gây hậu quả nghiêm trọng không thể đảo ngược. AI có thể hỗ trợ ở rìa (ví dụ phiên âm/dịch ngôn ngữ ít tài nguyên), nhưng đó là bài toán NLP/ASR riêng, không phải bài toán chuyển giao kho di sản.

### i. Preservation vs restoring functionality

- **Khôi phục chức năng quản trị quyền tạo giá trị bắt buộc (`restoration-adds-value`).**
- Lưu tệp media thô ra ổ cứng hay Wayback Machine **phá hủy** lớp quy tắc truy cập (Cultural Protocols, Community Records, TK Labels) — thứ quyết định liệu cộng đồng có chấp nhận đưa tư liệu vào kho hay không (`R24`). Do đó, bảo tồn nội dung thuần túy là **không đủ** trong T4.

### j. Resurrection theme fit

- **Kiểm định nghiêm ngặt theo anchor `theme`:**
  - **T4 tổng quát:** **Không có công nghệ đã khai tử làm trung tâm** → **`theme` = 1** (trượt cổng ≥ 3, xác nhận Task B).
  - **Đã kiểm tra giả thuyết thu hẹp `A-T4a` ("Di cư/hồi sinh kho di sản Mukurtu 3 / Islandora 7 bị kẹt trên Drupal 7 sau khi Drupal 7 chính thức EOL ngày 05/01/2025"):**
    - Drupal 7 thực sự có ngày nghỉ hưu chính thức (`05/01/2025`, `R32` snippet).
    - **Tuy nhiên, nói thẳng:** Chuyển một website từ Drupal 7 sang Drupal 11 (Mukurtu 4) là **nâng cấp/di cư CMS truyền thống để xử lý nợ kỹ thuật (legacy migration)**, *không phải* "mang công nghệ chết sống lại hay tái tưởng tượng công nghệ lỗi thời" theo tinh thần Kiroween Resurrection. Hơn nữa, Drupal vẫn đang phát triển mạnh (Drupal 11) và Mukurtu 4 đã có tài liệu di cư chính thức (`R24`).
    - Do đó, ngay cả góc nhìn thu hẹp `A-T4a` cũng chỉ đạt tối đa **`theme` = 2** (vẫn trượt cổng ≥ 3).

### k. Verdict for this space

- **Kết luận:** **Loại (`drop`).**
- **Bằng chứng quyết định:** (1) **Trượt cổng chủ đề Kiroween** (T4 tổng quát `theme` = 1; ngay cả góc Drupal 7 EOL cũng chỉ đạt `theme` = 2 và mang tính nâng cấp CMS hơn là Resurrection); (2) Nút thắt cốt lõi là quản trị cộng đồng, niềm tin và tài trợ nhân sự — không phải thiếu công cụ phần mềm hay AI; (3) Rủi ro pháp lý/đạo đức cao (`high`) và bất khả thi để kiểm chứng trên dữ liệu cộng đồng thật trong khung thời gian hackathon trước 04/12/2026.

---

## 6. Cross-space analysis

Sau khi điều tra độc lập S2, T2, T3 và T4, câu hỏi xuyên suốt là: **Bốn không gian này có thực sự chia sẻ một vấn đề nền tảng chung không?**

### Bằng chứng ủng hộ (Điểm chung ở tầng chẩn đoán kinh tế–xã hội)

1. **Đứt gãy chủ thể quản lý (Stewardship Discontinuity):** Cả bốn không gian đều xuất hiện khi tổ chức tạo lập/vận hành (nhóm nghiên cứu hết grant ở S2, startup/hợp tác xã cạn tiền ở T2, ban biên tập tình nguyện ở T3, viện chủ quản đổi ưu tiên ở T4) mất nguồn lực duy trì **trước khi** giá trị sử dụng hoặc giá trị chứng cứ của tài sản số chấm dứt [A-G-C1, INFERENCE — rút từ bằng chứng độc lập ở §2–§5].
2. **Hành động trước khi đóng rẻ hơn cứu sau khi đóng:** Ở cả S2 (KDL/Endings đưa kế hoạch afterlife vào ngay đề xuất grant `R1`, `R2`), T2 (Cohost phải giữ server sống cho ArchiveTeam; Glitch mở redirect trước khi tắt `R8`, `R10`) và T3 (đăng ký PKP PN/JASPER khi tạp chí còn sống `R15`, `R16`), chi phí và độ toàn vẹn đều tốt hơn hẳn khi có sự hợp tác trước thời điểm tắt.
3. **Thiếu thị trường trả tiền trực tiếp cho "công cụ bảo tồn":** Trên cả 4 không gian, không tìm thấy bằng chứng rõ ràng về việc tổ chức/cá nhân sẵn sàng mua phần mềm đóng gói riêng cho bảo tồn hậu-tài-trợ (kiểm định `H0` của Task B); chi tiêu thực tế chỉ xuất hiện ở **lưu trữ/hạ tầng tổ chức** (Portico, CLOCKSS, NBDC), **dịch vụ tư vấn/SLA nhân sự** (KDL, Mukurtu Hosting) hoặc **tái lập thương mại** (Code Ocean) [A-G-C2, INFERENCE].

### Bằng chứng phản bác & Tại sao gộp thành một sản phẩm sẽ SAI LẦM

| Chiều so sánh | S2 (Research apps) | T2 (Small-platform shutdown) | T3 (Disappearing journals) | T4 (Heritage archives) |
|---|---|---|---|---|
| **Bản chất tài sản** | Mã nguồn + logic ứng dụng/DB tương tác | Dữ liệu người dùng + media + đồ thị hội thoại | Tài liệu học thuật chuẩn hóa (PDF/XML/DOI) | Bộ sưu tập đa phương tiện gắn quy tắc văn hóa |
| **Nút thắt số 1** | Kiến trúc server-side nặng & thiếu RTPs | Zero WTP & schema export phân mảnh | Tham gia/nhận thức tổ chức (hạ tầng đã đủ) | Quản trị cộng đồng, đồng thuận & quyền sở hữu |
| **Chế độ truy cập mong muốn** | Công khai để tái lập khoa học | Hỗn hợp (công khai vs riêng tư/GDPR) | **Tối đa hóa mở công khai** (CC OA) | **Hạn chế có kiểm soát** (Cultural Protocols) |
| **Bảo tồn nội dung có đủ?** | Không (cần chức năng tra cứu nhẹ) | Không (cần đọc/tìm kiếm hoặc di cư) | **Có** (`preservation-sufficient`) | **Không** (bắt buộc giữ quy tắc phân quyền) |
| **Cổng Resurrection (`theme ≥ 3`)** | **Có điều kiện** (3 nếu neo runtime đã khai tử) | **Đạt** (3 — nền tảng đóng cửa cụ thể) | **Trượt** (1) | **Trượt** (1; tối đa 2 nếu ép Drupal 7 EOL) |

- **Kết luận §6:** Bốn không gian chia sẻ một **chẩn đoán vĩ mô** ("tài sản số chết vì đứt gãy nguồn lực duy trì"), nhưng **KHÔNG chia sẻ cùng một bài toán sản phẩm, người dùng mục tiêu, mô hình trả tiền, hay yêu cầu pháp lý–kỹ thuật** [A-G-C3, INFERENCE]. Đặc biệt, **T3 và T4 mâu thuẫn trực tiếp về triết lý truy cập** (T3 hướng tới mở công khai tối đa kiểu CLOCKSS/CC, còn T4 yêu cầu khóa quyền theo giao thức văn hóa bản địa). Gộp chúng vào một "nền tảng bảo tồn số đa năng" sẽ tạo ra kiến trúc cồng kềnh mà không giải quyết đúng nút thắt của bất kỳ không gian nào.

---

## 7. Challenges to the human's framing

Để giữ tính khách quan tối đa, cần chỉ rõ 4 điểm mà khung đặt vấn đề ban đầu (umbrella question) quá rộng hoặc chưa đứng vững trước bằng chứng:

1. **Đánh đồng "mất tài nguyên" với "cần công cụ kỹ thuật mới":** Ở T3 và T4, bằng chứng cho thấy hạ tầng/công cụ nguồn mở mạnh đã tồn tại (PKP PN, JASPER, CLOCKSS, Portico, Mukurtu 4, Islandora). Vấn đề không phải "không có phần mềm", mà là thiếu tiền nuôi nhân sự, thiếu nhận thức quản trị, hoặc thiếu thỏa thuận kế nhiệm. Một công cụ phần mềm mới (đặc biệt do một nhóm nhỏ xây trong hackathon) không giải quyết được vấn đề quản trị tổ chức.
2. **Giả định ngầm rằng mọi tài sản số biến mất đều đáng giữ:** Wren (2017) ở S2 và tranh luận về tạp chí chất lượng thấp ở T3 cho thấy một phần lớn tài sản số chết đi vì không còn ai dùng hoặc đã có phương án thay thế tốt hơn. Khung phân tích cần ưu tiên cơ chế **chọn lọc (triage)** thay vì giả định bảo tồn mặc định.
3. **Đặt T3 và T4 vào đường đua Kiroween Resurrection:** Khi kiểm tra lại với nỗ lực tìm góc độ hợp lệ (OJS 2 EOL ở T3; Drupal 7 EOL / Mukurtu 3 ở T4), cả hai vẫn **trượt cổng `theme ≥ 3`** nếu không cố tình bóp méo định nghĩa "dead technology". Giữ T3/T4 trong khuôn khổ Kiroween Resurrection là lãng phí thời gian nghiên cứu ở các pha sau; nếu người dùng vẫn quan tâm T3/T4 vì giá trị xã hội, chúng nên được tách thành dự án ngoài phạm vi hạng mục Resurrection.
4. **Kỳ vọng vai trò AI ở những nơi tính tất định là bắt buộc:** Ở T3 (lưu trữ học thuật chuẩn hóa) và T4 (phân quyền Cultural Protocols — sai một bit là rò rỉ tư liệu thiêng), AI không những không cần thiết mà còn gây rủi ro. Chỉ ở **S2 thu hẹp (`A-S2a`)** (chuyển đổi mã nguồn legacy không tài liệu sang tĩnh/WASM có kiểm thử hồi quy) và một phần hẹp của **T2 (`A-T2a`)** (suy diễn schema export hỗn loạn) mới có giả thuyết hợp lý để kiểm chứng vai trò của AI ở Phase 5/7.

---

## 8. Unresolved questions

1. **Cho `A-S2a` (tĩnh hóa/WASM hóa research apps trên runtime đã khai tử):** Tỷ lệ thực tế các ứng dụng web Digital Humanities và tin sinh học mã nguồn mở hiện nay có thể chuyển sang dạng tĩnh/WASM mà vẫn giữ công năng tra cứu cốt lõi là bao nhiêu? (Tương ứng phép thử `H8` của Task B — chưa chạy.)
2. **Cho `A-S2a`:** Thư viện đại học hoặc phòng lab Digital Scholarship (như KDL, UVic) có thực sự thiếu công cụ tự động hỗ trợ chuyển đổi (có AI hoặc không), hay họ coi quy trình chuyển đổi thủ công theo SLA là đã đủ?
3. **Cho `A-T2a` (cửa sổ đóng cửa nền tảng nhỏ):** Trong các gói export thực tế (Cohost, Glitch, Ameba Ownd, một SaaS nhỏ bất kỳ), mức độ mất ngữ nghĩa lớn đến đâu và AI có thực sự vượt trội so với parser viết tay không? (Tương ứng phép thử `H2` của Task B — chưa chạy.)
4. **Cho `A-T2a`:** Có mô hình tài chính bền vững nào khả thi ngoài tài trợ phi lợi nhuận/mã nguồn mở không, khi cả nhà vận hành sắp đóng cửa lẫn người dùng cá nhân đều có WTP gần bằng 0?
5. **Cho phạm vi khu vực:** Chưa tìm thấy bằng chứng sơ cấp trực tiếp cho S2 ở châu Phi/Mỹ Latinh và cho T2 (ca đóng cửa nền tảng nhỏ cụ thể) ở châu Âu/châu Phi/Mỹ Latinh. Cần xác minh thêm nếu các không gian này đi tiếp sang Phase 5–6.

---

## 9. References

*Ghi chú công thức điểm tham khảo (7 tiêu chí): `Weighted = (20×Auth + 20×Tech + 20×Mech + 15×Ctx + 10×Fresh + 10×Repro + 5×Bias) / 5` (thang 0–100; mỗi tiêu chí 0–5).*

| Ref ID | URL | Title | Publisher | Pub Date | Accessed | Opened Directly / Snippet | Claims | 7 Scores (A/T/M/C/F/R/B) | Weighted | Source Reliability | Reference Relevance |
|---|---|---|---|---|---|---|---|---|---|---|---|
| R1 | https://endings.uvic.ca/principles.html | The Endings Project: Principles (v2.2.1) | University of Victoria (SSHRC) | 2023-03-03 | 2026-11-25 | Opened directly | A-S2-C3, A-G-C1 | 5/4/5/5/4/5/4 | 93.0 | High (academic project primary spec) | High (direct mechanism for post-grant DH apps) |
| R2 | https://kdl.kcl.ac.uk/ | King's Digital Lab (Home & Legacy Estates 2026) | King's College London | 2026-06-12 | 2026-11-25 | Opened directly | A-S2-C5 | 5/3/3/4/5/4/4 | 78.0 | High (leading UK DH lab official site) | Medium-High (confirms 2026 EU institutional activity) |
| R3 | https://dbarchive.biosciencedbc.jp/index-e.html | Life Science Database Archive (LSDB Archive) | NBDC / JST (Japan) | 2026 (live) | 2026-11-25 | Opened directly | A-S2-C7, A-S2-C10 | 5/4/4/5/5/5/5 | 92.0 | High (national government science agency) | High (direct Asian evidence of 89 archived DBs) |
| R4 | https://elixir-europe.org/platforms/tools | Tools Platform — ELIXIR | ELIXIR Europe | 2026 (live) | 2026-11-25 | Opened directly | A-S2-C6 | 5/3/3/4/5/4/4 | 78.0 | High (intergovernmental European infrastructure) | Medium (shows EU institutional bioinformatics support) |
| R5 | https://codeocean.com/ | Code Ocean version 4 - Trusted Agents | Code Ocean | 2026 (live) | 2026-11-25 | Opened directly | A-S2-C8 | 3/3/3/4/5/3/2 | 66.0 | Medium (commercial vendor homepage) | Medium (evidence of commercial reproducibility SaaS) |
| R6 | https://www.softwarepreservationnetwork.org/eaasi/ | EaaSI Case Study #1: The Would-Be Gentleman | Software Preservation Network | 2024–2026 | 2026-11-25 | Opened directly | A-S2-C4 | 5/4/4/4/4/4/4 | 84.0 | High (academic preservation consortium) | Medium (shows emulation alternative & limits) |
| R7 | https://webrecorder.net/ | Webrecorder: Web Archiving for All | Webrecorder | 2026 (live) | 2026-11-25 | Opened directly | A-S2-C10, A-T2-C1 | 4/4/5/4/5/5/4 | 88.0 | High (leading OSS web archiving org) | High (strongest technical baseline for web replay) |
| R8 | https://blog.glitch.com/post/changes-are-coming-to-glitch/ | Important changes are coming to Glitch | Glitch (Fastly) | 2025-05-22 | 2026-11-25 | Opened directly | A-T2-C1, A-T2-C2, A-T2-C8 | 5/4/4/5/5/5/4 | 91.0 | High (primary operator shutdown notice) | High (exact causes, timeline & redirect mechanism) |
| R9 | https://wiki.archiveteam.org/index.php/Glitch | Glitch - Archiveteam | ArchiveTeam | 2025 | 2026-11-25 | Opened directly | A-T2-C2 | 4/5/5/4/5/5/4 | 92.0 | High (primary community archiving log) | High (independent confirmation & API enumeration) |
| R10 | https://wiki.archiveteam.org/index.php/Cohost | Cohost - Archiveteam | ArchiveTeam | 2025-01 | 2026-11-25 | Opened directly | A-T2-C1, A-T2-C3 | 4/5/5/5/5/5/4 | 95.0 | High (primary technical rescue log) | High (direct evidence of scraping limits & operator cooperation) |
| R11 | https://digital-strategy.ec.europa.eu/en/policies/data-act | Data Act — Shaping Europe's digital future | European Commission | 2025–2026 | 2026-11-25 | Opened directly | A-T2-C5 | 5/3/4/5/5/5/5 | 88.0 | High (official EU policy authority) | High (confirms Sept 12, 2025 application date) |
| R12 | https://dtinit.org/ | Data Transfer Initiative (Home) | Data Transfer Initiative | 2026 (live) | 2026-11-25 | Opened directly | A-T2-C8 | 4/3/4/4/5/4/3 | 77.0 | High (non-profit industry consortium) | High (proves DTI/DTP focuses on living major platforms) |
| R13 | https://help.amebaownd.com/ | Ameba Ownd Help | CyberAgent, Inc. | 2026 (live) | 2026-11-25 | Opened directly | A-T2-C6 | 5/2/2/3/5/4/4 | 67.0 | High (official platform portal) | Low-Medium (portal only; shutdown details from R27) |
| R14 | https://arxiv.org/abs/2008.11933 | Open is not forever: a study of vanished open access journals | Laakso, Matthias, Jahn (arXiv/JASIST) | 2021-02-22 | 2026-11-25 | Opened directly | A-T3-C1, A-T3-C2 | 5/5/5/5/3/5/5 | 96.0 | High (peer-reviewed seminal study) | High (direct count of 174 vanished OA journals) |
| R15 | https://doaj.org/preservation/ | JASPER preservation service – DOAJ | DOAJ | 2024–2026 | 2026-11-25 | Opened directly | A-T3-C4 | 5/3/4/5/5/4/4 | 85.0 | High (primary scholarly infrastructure) | High (directly documents root cause & existing free path) |
| R16 | https://pkp.sfu.ca/pkp-pn/ | PKP Preservation Network | Public Knowledge Project (SFU) | 2026 (live) | 2026-11-25 | Opened directly | A-T3-C5 | 5/4/4/4/5/4/4 | 86.0 | High (official academic OSS provider) | High (proves free preservation exists for OJS) |
| R17 | https://pkp.sfu.ca/software/ojs/ | Open Journal Systems (OJS) | Public Knowledge Project (SFU) | 2026 (live) | 2026-11-25 | Opened directly | A-T3-C5 | 5/3/3/4/5/4/4 | 78.0 | High (official software page) | Medium (confirms OJS ecosystem) |
| R18 | https://keepers.issn.org/ | Welcome to The Keepers registry | ISSN International Centre | 2026 (live) | 2026-11-25 | Opened directly | A-T3-C4 | 5/3/4/4/5/5/5 | 85.0 | High (international bibliographic authority) | Medium-High (global preservation monitoring layer) |
| R19 | https://clockss.org/ | Home - Digital Preservation Services - CLOCKSS | CLOCKSS | 2026 (live) | 2026-11-25 | Opened directly | A-T3-C5 | 5/4/5/5/5/4/4 | 93.0 | High (primary preservation archive) | High (12 nodes, LOCKSS, CC OA trigger license) |
| R20 | https://www.portico.org/coverage/facts-and-figures/ | Facts and figures - Portico | Portico (ITHAKA) | 2026 (live) | 2026-11-25 | Opened directly | A-T3-C5, A-G-C3 | 5/5/4/5/5/5/4 | 95.0 | High (primary operational metrics) | High (235 triggers, 43,934 journals, only 160 executables) |
| R21 | https://www.jstage.jst.go.jp/browse/-char/en | J-STAGE Home | JST (Japan) | 2026-11-25 | 2026-11-25 | Opened directly | A-T3-C6 | 5/3/3/4/5/5/5 | 81.0 | High (national scientific platform) | Medium-High (Asian regional journal infrastructure) |
| R22 | https://scielo.org/en/about-scielo/ | About SciELO | SciELO (Brazil) | 2026 (live) | 2026-11-25 | Opened directly | A-T3-C7 | 5/3/3/4/4/4/4 | 76.0 | High (regional scholarly network) | Medium-High (Latin America infrastructure) |
| R23 | https://www.ajol.info/index.php/ajol | African Journals Online (AJOL) | AJOL (NPO) | 2026 (live) | 2026-11-25 | Opened directly | A-T3-C7 | 5/3/3/5/5/4/4 | 81.0 | High (audited African scholarly NPO) | High (African demand & donation funding model) |
| R24 | https://docs.mukurtu.org/ | Mukurtu User Manual | CDSC, Washington State Univ. | 2026 (live) | 2026-11-25 | Opened directly | A-T4-C1, A-T4-C2 | 5/4/5/5/5/5/5 | 96.0 | High (official technical manual) | High (Cultural Protocols, TK Labels & Mukurtu 3 Migration) |
| R25 | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5389617/ | Use it or lose it: citations predict continued online availability | Wren et al., Nucleic Acids Research | 2017 | 2026-11-25 | Snippet only (reCAPTCHA / 403) | A-S2-C2 | 5/4/4/4/2/3/5 | 79.0 | High (peer-reviewed paper, limited by snippet access) | High (key counterevidence on citation-driven survival) |
| R26 | https://techcrunch.com/ (via search) | Cohost shutdown & $17,000 monthly deficit coverage | TechCrunch / Wikipedia | 2024-09 | 2026-11-25 | Snippet only | A-T2-C3 | 3/2/2/4/4/2/3 | 55.0 | Medium (secondary tech press snippet) | Medium (financial deficit context for Cohost) |
| R27 | https://ascii.jp/ & https://amebaownd.com/ (via search) | Ameba Ownd service termination & export limitations | ASCII.jp / Ameba Ownd | 2026-11 | 2026-11-25 | Snippet only | A-T2-C6 | 3/3/3/4/5/2/4 | 66.0 | Medium (Japanese tech press & help snippets) | High (Asian 2026 shutdown case & missing image files) |
| R28 | https://pkp.sfu.ca/ (via search) | OJS 2 EOL (2021) & 58,000+ OJS journals | PKP / OJS Academy | 2024–2026 | 2026-11-25 | Snippet only | A-T3-C1 | 3/2/2/3/4/2/3 | 52.0 | Medium (secondary & search snippets) | Medium (context on OJS 2 EOL test) |
| R29 | https://doi.org/10.31274/jlsc.16288 | Digital Scholarly Journals Are Poorly Preserved: A Study of 7M Articles | Martin Paul Eve, JLSC | 2024 | 2026-11-25 | Snippet only (anti-bot block) | A-T3-C3 | 5/4/4/4/5/3/5 | 85.0 | High (peer-reviewed paper, limited by anti-bot) | High (27.64% unconfirmed DOI preservation stat) |
| R30 | https://www.bbaw.de/ & https://www.elararchive.org/ (via search) | ELAR relocation from SOAS to BBAW (2021, Arcadia Fund) | BBAW / ELAR | 2021–2026 | 2026-11-25 | Snippet only (login/404) | A-T4-C1, A-T4-C4 | 4/2/3/4/3/2/4 | 62.0 | Medium-High (institutional summary via snippets) | High (concrete EU heritage archive transfer case) |
| R31 | https://kululanguage.com/ | Kulu Language Institute | Kulu Language Institute | 2026 (live) | 2026-11-25 | Opened directly | A-T4-C1, A-T4-C6 | 5/2/2/5/4/4/4 | 71.0 | High (primary community org site) | High (grassroots Pacific language preservation) |
| R32 | https://www.drupal.org/psa-2023-06-07 | Drupal 7 End of Life (January 5, 2025) | Drupal.org | 2023-06-07 | 2026-11-25 | Snippet only (Client Challenge) | A-T4-C1 | 5/3/3/4/4/3/5 | 75.0 | High (official PSA, limited by anti-bot) | High (tests Drupal 7 EOL Resurrection angle) |
| R33 | https://warp.da.ndl.go.jp/info/warp_abstract_en.html | Web Archiving Project (WARP) | National Diet Library, Japan | 2026 (live) | 2026-11-25 | Opened directly | A-T4-C5 | 5/3/3/4/4/4/5 | 77.0 | High (national library primary site) | Medium (Asian national web heritage archive) |
| R34 | https://www.islandora.ca/ | Islandora Open-Source Digital Asset Management | Islandora Foundation | 2026 (live) | 2026-11-25 | Opened directly | A-T4-C3 | 5/3/4/4/5/4/4 | 82.0 | High (official OSS foundation) | Medium-High (major Drupal-based digital archive) |
