# Phase 3 — Agent B

## Metadata

| Mục | Giá trị |
|---|---|
| Run | `2026-11-25-phase3-7-knowledge-continuity`, Phase 3 |
| Model | Harness báo `claude-sonnet-5-5`; effort: not observable |
| Bắt đầu / kết thúc (UTC, theo `date -u` trong phiên) | 2026-11-25T16:15:59Z / 2026-11-25T16:25Z (theo `date -u`; đồng hồ trong phiên có vẻ không khớp với lượng công việc đã làm, nên coi hai mốc là gần đúng) |
| Số lượt tìm kiếm (WebSearch) | 18 |
| Trang tải về bằng `curl` | 38 lượt tải; 30 trang/PDF đọc được nội dung |
| Nguồn trong §9 | 37 ref: **23 mở trực tiếp**, **14 chỉ snippet** |
| Thất bại | drupal.org và bản full-text JLSC của Eve 2024 bị chặn bởi Anubis (trang chống bot); adobe.com 403; EUR-Lex trả 202 rỗng (không đọc được văn bản Data Act); docs.mukurtu.org migration overview 404; trang GBC bản URL đầu 404 (đọc được qua `?p=5165`); siarchives.si.edu 403; PDF dự án tạp chí LIS Indonesia tải được nhưng không trích được văn bản. Các ý dựa vào những nguồn này bị hạ xuống INFERENCE và đánh dấu "snippet only". |
| Không làm | Không phỏng vấn, không chạy thí nghiệm, không thiết kế sản phẩm, không đọc thư mục agent khác của run này, không cài đặt gì. Skill `historical-technology-discovery` được đọc và dùng cho §j. |

Toàn bộ trang đã tải và công cụ trích văn bản nằm trong `agent-b/scratch/` (`pages/`, `tools/`).

## 1. Method

**Phương pháp BA đã chọn và lý do**

1. **Cây vấn đề (problem tree)** cho từng không gian: tách triệu chứng (link chết, site tắt) khỏi nguyên nhân gốc (tài trợ có kỳ hạn, thiếu nhân sự, nền tảng/runtime bị khai tử, quyết định thương mại). Cần cho câu hỏi ô dù của người dùng: "thiếu nguồn lực" có thật là nguyên nhân chung không.
2. **Bảng stakeholder với hành vi đã quan sát**: tách nhu cầu **đã chứng minh** (tiền, quyên góp, giờ tình nguyện, di trú) khỏi nhu cầu **giả định**. Đây là điểm yếu lớn nhất của Task B (H0: chưa ai trả tiền cho *công cụ*).
3. **Phân tích phương án thay thế mạnh nhất** trước khi tuyên bố khoảng trống.
4. **Kiểm tra cổng theme** theo skill `historical-technology-discovery`: chỉ chấp nhận mỏ neo Resurrection khi có một công nghệ cụ thể đã được **tuyên bố chính thức** là ngừng/hết vòng đời, và công nghệ đó **gây ra** vấn đề chứ không chỉ xuất hiện bên cạnh.
5. **Chuỗi bằng chứng**: claim → nguồn gốc mở trực tiếp → xác nhận độc lập → kiểm tra cơ chế. Mỗi claim ghi mức đã đi tới.

**Thứ tự**: điều tra S2, T2, T3, T4 riêng rẽ (§2–§5), chỉ sau đó mới so sánh (§6).

**Không làm**: không đề xuất kiến trúc; không chấm điểm cuối (chỉ ghi `provisional_score` trong JSON như tóm tắt bằng chứng); không so với ứng viên Phase 2.

**Giới hạn chính**: độ sâu mỗi không gian ~10–12 nguồn. Bằng chứng châu Á và "vùng khác" mỏng ở mọi không gian; tôi ghi rõ "không tìm thấy" kèm truy vấn thay vì suy rộng.

---

## 2. S2 — Research apps after funding

### a. Problem and root causes

```text
Hệ quả: công cụ/CSDL nghiên cứu được trích dẫn không còn truy cập hoặc không chạy được
│
├─ A. Tài trợ có kỳ hạn hoặc bị cắt
│   ├─ grant kết thúc theo lịch (TAIR: NSF dừng 2013)            [B-S2-C6]
│   └─ cắt đột ngột (FlyBase: NIH chấm dứt 05/2025)               [B-S2-C4, B-S2-C5]
├─ B. Thiếu nhân sự kỹ thuật dù còn tiền
│   └─ PDBj SFAS tạm ngừng 02/2024 vì "lack of IT personnel"       [B-S2-C7]
├─ C. Nền tảng/runtime bị khai tử từ bên ngoài
│   ├─ Flash hết hạn 01/01/2021 (PhET)                             [B-S2-C8]
│   └─ Google Fusion Tables ngừng, dữ liệu xóa sau 03/03/2020      [B-S2-C9]
├─ D. Chuẩn xuất bản không yêu cầu duy trì
│   └─ không tạp chí nào buộc đảm bảo phần mềm tiếp tục chạy      [B-S2-C1]
└─ E. Nợ di sản tích lũy ở cấp tổ chức
    └─ KDL thừa hưởng gần 100 dự án, đa số không có tiền đi kèm    [B-S2-C2]
```

Quy mô: Mangul et al. 2019 khảo sát 36.702 URL tài nguyên phần mềm omics (2005–2017); gần 28% không truy cập được qua URL in trong bài báo; 28% trong 98 công cụ thử không cài được (`B-S2-C1`, VERIFIED, scoped vào kết quả nghiên cứu).

**Khi nào bảo tồn KHÔNG đáng làm:**

- Khi PI tự nói dự án đã xong vai trò: KDL ghi nhận "in many cases PIs responded promptly, asking us to gracefully archive their project because it had fulfilled its purpose" (`B-S2-C2`).
- Khi tài nguyên trùng lặp hoặc đã được tài nguyên lớn hơn hấp thụ (FlyBase đang được kế hoạch gộp vào Alliance of Genome Resources; snippet R6).
- Với công cụ ít dùng thuộc "đuôi dài": Task B (A §11.2, Wren 2017) cho rằng tài nguyên được trích dẫn nhiều phần lớn tự sống sót. Tôi **không** mở lại Wren 2017; giữ ở INFERENCE (`B-S2-C10`).

### b. Stakeholders and target users

| Actor | Job-to-be-done | Hành vi hiện tại | Sẵn sàng đóng góp/trả | Chứng minh / giả định | Bằng chứng |
|---|---|---|---|---|---|
| Đơn vị vận hành CSDL lõi (FlyBase, TAIR, GCBR) | Giữ dịch vụ và curation | Xin tài trợ khẩn cấp, quyên góp, phí người dùng, đóng băng cập nhật | Có, tự gánh | **Chứng minh** | R4, R5, R7 |
| Cộng đồng người dùng (nhà sinh học ruồi, thực vật) | Tiếp tục tra cứu | Quyên góp (cộng đồng ruồi châu Âu), mua subscription TAIR | Có, nhỏ và không đều | **Chứng minh** | R5, R7 |
| Lab DH / RSE trong đại học (KDL, UVic HCMC) | Xử lý "nợ di sản" | Phân loại: SLA, di chuyển, chuyển tĩnh, lưu tối thiểu | Có, qua ngân sách lab; chuyển tĩnh miễn phí cho dự án phù hợp | **Chứng minh** | R2, R3 |
| PI của dự án đã hết grant | Giữ trích dẫn sống hoặc kết thúc gọn | Thường chọn lưu tối thiểu hoặc để chết | Thấp | Chứng minh (ở KDL); chưa rõ nơi khác | R2 |
| Nhà tài trợ (NIH, NSF, Wellcome, SSHRC, Moore) | Giảm lãng phí đầu tư | Tài trợ dự án bền vững (Endings), cứu khẩn cấp (Wellcome cho FlyBase) | Có, chọn lọc | **Chứng minh** | R3, R5 |
| Giáo viên dùng mô phỏng cũ (PhET Flash/Java) | Dạy học | Dùng bản HTML5 hoặc CheerpJ; PhET xin quyên góp để chuyển đổi | Quyên góp | Chứng minh một phần | R8 |
| Nhà nghiên cứu muốn tái lập kết quả cũ | Chạy lại công cụ đã trích dẫn | Không có đường chuẩn | Không thấy | **Giả định** | — |

### c. Documented cases by region

- **NA:** FlyBase (Harvard, Mỹ): NIH chấm dứt grant 05/2025, grant NHGRI > 2 triệu USD/năm, 8 nhân viên Harvard bị cho nghỉ (`B-S2-C4`, R5 + R6 độc lập). TAIR chuyển sang subscription qua Phoenix Bioinformatics sau khi NSF dừng 2013 (`B-S2-C6`, R7). PhET (Colorado): mô phỏng Flash không chạy từ 01/01/2021 (`B-S2-C8`, R8). Endings Project, UVic (Canada): rút từ việc bảo trì dự án ấn bản số "unsustainable" (R3; câu "rescued over a dozen projects" chỉ snippet, R34).
- **EU:** KDL (King's College London, UK) thừa hưởng gần 100 dự án năm 2015 (`B-S2-C2`, R2). Nhóm FlyBase Cambridge sống nhờ quyên góp cộng đồng ruồi châu Âu và tài trợ khẩn cấp của Wellcome Trust (R5).
- **Asia:** PDBj SFAS (Nhật): tạm ngừng 02/2024 vì thiếu nhân sự IT, kêu gọi đơn vị khác nhận host (`B-S2-C7`, R9). TAIR: 42% lượt truy cập năm 2014 đến từ châu Á (R7): người dùng châu Á bị ảnh hưởng bởi quyết định tài trợ của Mỹ. **Không tìm thấy** nghiên cứu định lượng về suy giảm công cụ nghiên cứu ở châu Á (truy vấn: "Asia bioinformatics database discontinued after funding China Japan web server unavailable study") (`B-S2-C14`, UNKNOWN).
- **Toàn cầu:** GBC ước tính 32/52 Global Core Biodata Resources nhận tiền liên bang Mỹ, 26 phụ thuộc chính; một số đã mở chiến dịch gây quỹ khẩn cấp, thu phí người dùng, đóng băng cập nhật (`B-S2-C5`, R4, ngày 16/06/2025).
- **Other:** không tìm thấy (không chạy truy vấn riêng cho châu Phi/Mỹ Latinh trong S2).

### d. Demand and consequences of inaction

- **Demand đã chứng minh** ở đầu "lớn": cộng đồng trả tiền thật cho TAIR từ 2014 và TAIR tự duy trì được (R7); cộng đồng ruồi châu Âu quyên góp và Wellcome cấp tiền khẩn cấp cho FlyBase (R5); KDL dùng ngân sách lab để chuyển tĩnh miễn phí (R2).
- **Demand giả định** ở đầu "đuôi dài": không có bằng chứng rằng PI của các công cụ nhỏ (28% URL chết của Mangul) muốn hay sẽ trả để giữ chúng (`B-S2-C11`, INFERENCE).
- **Hệ quả nếu không làm**: tài nguyên curation lớn mất người duy trì (FlyBase: "remaining funds would keep the website online for about one more year", snippet R6); với công cụ nhỏ, link chết và kết quả không tái lập được. Mức thiệt hại cho khoa học của phần đuôi dài: CHƯA RÕ.

### e. Existing solutions and limits

| Phương án mạnh nhất đã kiểm tra | Làm được | Giới hạn |
|---|---|---|
| **KDL Archiving & Sustainability** (R2) | Quy trình 6 lựa chọn: SLA, di chuyển ITS, di chuyển host ngoài, chuyển tĩnh, nộp dataset, lưu tối thiểu | Chỉ cho dự án KCL; chuyển tĩnh làm thủ công theo từng dự án |
| **Endings Principles** (R3) | Chuẩn "không phụ thuộc phần mềm phía server: site tĩnh, không database" (nguyên tắc 4.1) | Áp dụng tốt cho ấn bản văn bản; không giải quyết công cụ tính toán hoặc truy vấn động |
| **Mô hình subscription (TAIR/Phoenix)** (R7) | Tự duy trì sau 1 năm | Chỉ khả thi với tài nguyên đã có cộng đồng lớn; đóng một phần truy cập |
| **Tài trợ hạ tầng (GBC, ELIXIR, Wellcome)** (R4, R5) | Cứu tài nguyên lõi | Chọn lọc 52 GCBR; đuôi dài không được phủ |
| **Emulation runtime (CheerpJ cho Java, Ruffle cho Flash)** (R8; R33 snippet) | Chạy lại applet/SWF không cần viết lại | Không đầy đủ: "Some simulations have specific features that are not supported in the CheerpJ version" (R8) |
| Software Heritage, Zenodo, Wayback (biết từ Task B; không mở lại) | Lưu mã nguồn, lưu bản chụp trang | Không giữ được công năng phía server |

**Khoảng trống còn lại (INFERENCE):** không thấy công cụ nào tự động hóa đánh giá "dự án này chuyển tĩnh được không, mất gì" cho một **danh mục** dự án. KDL và Endings làm thủ công. Đây là khoảng trống quy trình, chưa chứng minh có người muốn trả để lấp.

### f. Barriers

- **Pháp lý:** thấp với mã/dữ liệu do chính nhóm làm; trung bình nếu dữ liệu có giấy phép bên thứ ba hoặc dữ liệu cá nhân. TAIR cho thấy đóng truy cập là một đánh đổi hợp pháp nhưng gây tranh cãi.
- **Tài chính:** grant không chi cho giai đoạn sau dự án (`B-S2-C1`: "none currently require authors to guarantee the continuing functionality").
- **Kỹ thuật:** công năng phía server (truy vấn, tính toán, đăng nhập) không chuyển tĩnh được một cách tổng quát; runtime bị khai tử (Flash, Java applet, Fusion Tables) cắt hẳn đường chạy.
- **Tổ chức:** không ai "sở hữu" dự án khi PI rời đi; KDL phải tự nhận trách nhiệm đạo đức với dự án không có tiền (R2).

### g. Who pays, who maintains

- **Trả tiền (đã chứng minh):** người dùng tổ chức (TAIR subscription), nhà tài trợ tư (Wellcome, Moore cho PhET, snippet), ngân sách lab đại học (KDL), quyên góp cộng đồng (FlyBase, PhET).
- **Duy trì:** đơn vị RSE/DH lab của trường; nonprofit tách ra (Phoenix); consortium (Alliance of Genome Resources).
- **Cho công cụ đánh giá/chuyển đổi danh mục**: không tìm thấy người trả. "None found."

### h. AI: meaningful advantage or not

- **Không cần AI** cho: crawl và đóng băng site tĩnh (wget/Webrecorder), kiểm link, chạy lại SWF/applet (Ruffle, CheerpJ).
- **AI có thể hữu ích (HYPOTHESIS, `B-S2-C13`)** cho: đọc mã nguồn dự án cũ để lập danh mục chức năng phía server và đề xuất phần nào chuyển client-side được; viết lại applet nhỏ sang JS khi emulator không hỗ trợ. Chưa có benchmark nào tôi tìm thấy; một oracle khả thi là so đầu ra của phiên bản gốc (chạy trong emulator) và phiên bản chuyển đổi trên cùng input.
- Kết luận: **useful**, không load-bearing.

### i. Preservation vs restoring functionality

Bằng chứng nghiêng về **khôi phục công năng có giá trị thêm**, nhưng chỉ khi công năng là thứ được dùng:

- PhET không chấp nhận chỉ lưu bản Flash; họ chi tiền chuyển sang HTML5 và hợp tác CheerpJ để mô phỏng **chạy lại được** (R8). Đây là hành vi trả tiền cho khôi phục công năng.
- KDL có cả lựa chọn "lưu tối thiểu" (placeholder + Wayback) và "chuyển tĩnh giữ truy cập công khai". Lựa chọn thứ hai được mô tả "very cost effective" (R2).
- Với công cụ đã chết mà không ai dùng, chỉ cần lưu (Software Heritage) là đủ.

→ `restoration-adds-value` cho tài nguyên còn người dùng; `preservation-sufficient` cho đuôi dài.

### j. Resurrection theme fit

- S2 nói chung (grant hết hạn) **không** có công nghệ chết cụ thể: grant không phải công nghệ. Điểm anchor phù hợp: **2** (sản phẩm/dịch vụ còn sống nhưng suy yếu).
- **Có một mỏ neo hợp lệ ở tiểu không gian (B-S2a)**: công cụ nghiên cứu và giảng dạy chạy trên runtime **đã chính thức bị khai tử**:
  - Adobe Flash Player: hết hạn, PhET xác nhận không chạy trên trình duyệt hiện đại từ 01/01/2021 (R8; trang EOL của Adobe trả 403, nên ngày là "PhET officially stated");
  - Google Fusion Tables: ngừng, dữ liệu xóa vĩnh viễn sau 03/03/2020 (R10, trang chính thức của Google);
  - Java applet: PhET vẫn còn mô phỏng Java chỉ chạy qua CheerpJ (R8).
- Ở B-S2a, công nghệ chết là **nguyên nhân trực tiếp** khiến công cụ ngừng chạy, nên không phải kéo giãn theme. Anchor **3** (công nghệ đã hoàn tất khai tử làm mỏ neo cho việc khôi phục công năng), có thể **4** nếu demo xoay quanh một applet/SWF nghiên cứu thật. Độ tin cậy M.
- Rủi ro: phần "Flash/Java" đã có đối thủ mạnh (Ruffle, CheerpJ, Flashpoint). Khoảng trống phải là công cụ **nghiên cứu/giảng dạy** mà emulator chưa chạy được, chưa được đo.

### k. Verdict for this space

**Narrow** sang **B-S2a**: công cụ nghiên cứu/giảng dạy bị chết vì runtime bị khai tử (Flash, Java applet, Fusion Tables), đối tượng là lab RSE/DH và dự án giáo dục đang mang "nợ di sản".

Bằng chứng quyết định:

- Demand đã chứng minh có ở đầu lớn (TAIR, FlyBase, GBC), nhưng đầu lớn cần **tiền**, không cần công cụ mới;
- hành vi trả tiền cho **khôi phục công năng** có ở PhET (R8) và KDL (R2);
- theme chỉ qua cổng khi có runtime bị khai tử.

Falsifier: lấy 20 dự án Flash/Java applet học thuật trong danh sách công khai (PhET legacy, KDL, Endings); nếu ≥ 80% đã chạy được bằng Ruffle/CheerpJ hoặc đã được viết lại, khoảng trống không tồn tại.

---

## 3. T2 — Small-platform shutdown window

### a. Problem and root causes

```text
Hệ quả: nội dung, quan hệ và tài sản của cộng đồng mất khi nền tảng đóng
│
├─ A. Kinh tế đơn vị nhỏ không bù chi phí
│   └─ Cohost: 30.000 MAU, 2.630 subscriber, thâm hụt 17.000 USD (03/2024)   [B-T2-C1]
├─ B. Quyết định chiến lược của công ty mẹ (không phải thiếu tiền)
│   ├─ Glitch (thuộc Fastly) dừng hosting 08/07/2025                          [B-T2-C3]
│   ├─ Yahoo!ブログ đóng 15/12/2019                                          [B-T2-C4]
│   └─ Xiami (Alibaba) đóng 02/2021; thua trong cạnh tranh bản quyền          [B-T2-C5]
└─ C. Export không đủ để tái lập cộng đồng
    └─ đồ thị xã hội, bình luận, quan hệ không chuyển được (Task B B-O2)
```

**Phát hiện quan trọng (INFERENCE, `B-T2-C7`):** ở các ca **lớn** (Yahoo!ブログ, Xiami), chính đối thủ hoặc nền tảng nhận đã làm công cụ chuyển: Ameba, livedoor, Seesaa, sau đó Hatena nhận blog Yahoo (R14); NetEase Cloud Music và QQ Music nhận playlist Xiami (snippet R15). Ở ca **nhỏ** (Cohost), không ai làm importer; chỉ có ArchiveTeam lưu bản đọc (R13). Nghĩa là thị trường tự giải quyết ca lớn; ca nhỏ không có ai có động cơ.

**Khi nào bảo tồn KHÔNG đáng làm:** khi nội dung đã có nơi khác (cross-post); khi người dùng chủ động muốn xóa (quyền được quên); khi nền tảng chủ yếu chứa nội dung bản quyền bên thứ ba (Xiami: nhạc có bản quyền, chỉ playlist là của người dùng).

### b. Stakeholders and target users

| Actor | Job-to-be-done | Hành vi hiện tại | Sẵn sàng đóng góp/trả | Chứng minh / giả định | Bằng chứng |
|---|---|---|---|---|---|
| Nhà vận hành nền tảng nhỏ sắp đóng | Đóng có trách nhiệm với chi phí thấp | Cohost: read-only, ưu tiên phát triển export; hoãn tắt cho ArchiveTeam theo yêu cầu nhà tài trợ | Không có tiền tại thời điểm đóng | Hành vi: **chứng minh**; trả tiền: **không có** | R12, R13 |
| Nhà vận hành thuộc công ty lớn (Glitch/Fastly, Yahoo) | Đóng mà không mất uy tín | Tự xây export, redirect URL, hướng dẫn di trú | Có, nội bộ | **Chứng minh** | R11, R14 |
| Người dùng/creator | Mang nội dung đi | Tải export, di cư | Thời gian, không tiền | **Chứng minh** (thời gian) | R11, R14 |
| Tình nguyện viên lưu trữ (ArchiveTeam) | Lưu bản đọc công khai | Crawl khẩn cấp; viết lại item type để lấy "long tail" | Giờ tình nguyện | **Chứng minh** | R13 |
| Nền tảng nhận (đối thủ) | Thu hút người dùng | Viết importer | Có, vì lợi ích thương mại | **Chứng minh** ở ca lớn | R14, R15 |
| Cơ quan quản lý EU | Chống khóa nhà cung cấp | Data Act Ch. VI áp dụng từ 12/09/2025 cho SaaS | — | Chỉ snippet | R16 |

### c. Documented cases by region

- **NA:** Cohost (2024–2025): thông báo 09/2024, read-only 01/10/2024, ArchiveTeam ghi "Saved!" và chủ ý lấy cả "long tail" (R12, R13). Glitch (2025): dừng hosting 08/07/2025, tải mã tới hết 2025, redirect tới ít nhất hết 2026 (R11).
- **Asia:** Yahoo!ブログ (Nhật, 2019): công cụ chuyển chính thức ra 03/06/2019, nền tảng nhận ban đầu là Ameba, livedoor, Seesaa, bổ sung Hatena (R14). Xiami (Trung Quốc, 2021): một tháng để chuyển playlist sang đối thủ (R15 trực tiếp, chi tiết chuyển chỉ snippet). Cả hai đều là **dịch vụ của tập đoàn lớn**, không phải "nền tảng nhỏ". Không tìm thấy ca nền tảng nhỏ ở châu Á trong các truy vấn đã chạy (`B-T2-C9`, UNKNOWN).
- **EU:** chỉ có bằng chứng quy định (Data Act, snippet từ các hãng luật, R16). **Không tìm thấy** ca nền tảng nhỏ châu Âu đóng cửa có tài liệu chuyển giao, với các truy vấn đã chạy. Ca Hyves/StudiVZ không được kiểm tra.
- **Other:** Mxit (Nam Phi) nêu ở Task B; không mở lại.

### d. Demand and consequences of inaction

- **Demand đã chứng minh**: giờ tình nguyện của ArchiveTeam; nhà tài trợ Cohost yêu cầu hoãn tắt để lưu trữ (R13); công ty lớn tự chi tiền làm export và redirect (R11, R14).
- **Demand giả định**: nhà vận hành nhỏ trả tiền cho một "bộ công cụ đóng cửa". Không có bằng chứng; Cohost đóng vì hết tiền (`B-T2-C8`, HYPOTHESIS).
- **Hệ quả nếu không làm**: mất bản đọc công khai (ArchiveTeam thường đã phủ) và mất quan hệ cộng đồng (không ai phủ). Quan hệ cộng đồng là phần Task B cho là khó bảo tồn nhất về bản chất.

### e. Existing solutions and limits

| Phương án | Làm được | Giới hạn |
|---|---|---|
| **ArchiveTeam + Wayback** (R13) | Lưu bản đọc ở quy mô lớn, kể cả nhanh | Read-only; cần thời gian (Cohost phải hoãn tắt); không chuyển tài khoản |
| **Export + redirect do nhà vận hành làm** (Glitch, R11) | Mã, URL sống tiếp | Cần ngân sách của công ty mẹ |
| **Importer của nền tảng nhận** (Yahoo→Hatena..., R14) | Di trú một nhấp | Chỉ xảy ra khi có động cơ thương mại (ca lớn) |
| **DTI / Data Transfer Project** (R17, snippet) | Chuẩn chuyển dữ liệu giữa nền tảng lớn | Không thấy nội dung về nền tảng nhỏ đóng cửa |
| **EU Data Act Ch. VI** (R16, snippet) | Quyền chuyển đổi, export máy đọc được cho SaaS | Nhằm nhà cung cấp còn sống; áp vào nhà cung cấp phá sản: CHƯA RÕ |
| Mastodon account migration (Task B) | Di chuyển follower trong fediverse | Chỉ trong hệ ActivityPub |

**Khoảng trống:** chuyển **cộng đồng** (quan hệ, bình luận) của nền tảng nhỏ không có importer. Tôi không tìm thấy công cụ chung lấp khoảng trống này; nhưng cũng không tìm thấy ai trả tiền cho nó.

### f. Barriers

- **Pháp lý:** dữ liệu cá nhân (GDPR) khi chuyển hàng loạt; nội dung bản quyền (Xiami). Trung bình.
- **Tài chính:** nhà vận hành nhỏ đóng **vì** hết tiền; thời điểm cần công cụ là lúc không có ngân sách.
- **Kỹ thuật:** mỗi nền tảng có schema riêng; export thường phẳng (Task B B-O2).
- **Tổ chức:** cửa sổ thời gian ngắn (Cohost: ~3 tháng; Xiami: 1 tháng); không có bên kế nhiệm mặc định.

### g. Who pays, who maintains

- Ca lớn: công ty mẹ (Glitch/Fastly, Yahoo) và nền tảng nhận. **Đã chứng minh.**
- Ca nhỏ: tình nguyện viên (ArchiveTeam), nhà tài trợ còn lại của nền tảng. **Không ai trả cho công cụ.** "None found."

### h. AI: meaningful advantage or not

- **Unnecessary** cho crawl và export. Suy schema của export không tài liệu là việc AI có thể giúp, nhưng parser viết tay cho một nền tảng cụ thể là baseline mạnh và rẻ (giữ nguyên nhận định B Task B).
- Không tìm thấy bằng chứng mới thay đổi kết luận này.

### i. Preservation vs restoring functionality

Bản đọc (preservation) đã được ArchiveTeam phủ tốt ở các ca nổi tiếng. Giá trị thêm nằm ở chuyển **cộng đồng còn sống** sang nơi mới, tức là di trú, không phải khôi phục một chức năng đã chết. Với Glitch, phần "chức năng" (app chạy được) được giữ bằng export mã và redirect do chính nhà vận hành làm. → `unclear`.

### j. Resurrection theme fit

- T2 theo định nghĩa là "**trước** khi đóng": ngăn cái chết, không đem công nghệ chết trở lại. Đây là lý do chính khiến theme yếu.
- Nếu đảo sang "sau khi đóng" (dựng lại Cohost từ bản ArchiveTeam thành một archive duyệt được), công nghệ chết là cụ thể (Cohost, đã tắt 2025) và theme có thể đạt 3–4. Nhưng đó là **không gian khác** (gần A-P4/S1 của các vòng trước), không phải T2. Tôi không kéo giãn T2 để chứa nó.
- Anchor cho T2 như đã định nghĩa: **2**, độ tin cậy M (`B-T2-C10`, INFERENCE).

### k. Verdict for this space

**Drop** dưới dạng đã định nghĩa. Bằng chứng quyết định:

1. ca lớn đã được thị trường giải quyết (Yahoo, Xiami, Glitch);
2. ca nhỏ không có người trả tiền, vì nhà vận hành đóng chính vì hết tiền (Cohost);
3. bản đọc đã được ArchiveTeam phủ;
4. AI không cần;
5. theme ≤ 2 vì bản chất là phòng ngừa.

Điều kiện để mở lại: tìm thấy một nhà vận hành nhỏ hoặc quỹ đã **trả tiền** cho việc chuyển giao cộng đồng.

---

## 4. T3 — Disappearing journals

### a. Problem and root causes

```text
Hệ quả: bài báo có DOI/được trích dẫn không còn truy cập; chuỗi trích dẫn đứt
│
├─ A. Tạp chí nhỏ không tham gia lưu trữ dài hạn
│   ├─ chỉ 0,96% thành viên Crossref lưu >75% nội dung ở ≥3 archive      [B-T3-C2]
│   └─ JASPER: ~100 biên tập viên được mời → >40 đơn → 32 được chọn      [B-T3-C5]
├─ B. Thiếu nguồn lực và hiểu biết ("lack of resources and understanding") [B-T3-C5]
├─ C. Phần mềm xuất bản đã hết vòng đời
│   ├─ OJS 2.x: "Not supported", EOL 2021                                  [B-T3-C3]
│   └─ PKP PN (miễn phí) yêu cầu OJS ≥ 3.1.2 (snippet)                      [B-T3-C4]
└─ D. Tạp chí ngừng xuất bản khi biên tập viên rời đi (Laakso: tạp chí nhỏ, SSH, do học giả tự làm) [B-T3-C1]
```

**Khi nào bảo tồn KHÔNG đáng làm:**

- Tạp chí săn mồi (predatory): Shelomi phản biện rằng nhiều tạp chí biến mất trong mẫu Laakso có thể là predatory (R25 snippet). Nếu đúng, một phần "mất mát" không đáng cứu.
- Bài đã có bản green OA trong kho lưu trữ tổ chức: Eve tự nhận không kiểm kho tổ chức (R19), nên "không xác nhận được bảo tồn" ≠ "đã mất". Xác nhận `C-G-C1` của Task B.

### b. Stakeholders and target users

| Actor | Job-to-be-done | Hành vi hiện tại | Sẵn sàng đóng góp/trả | Chứng minh / giả định | Bằng chứng |
|---|---|---|---|---|---|
| Biên tập viên tạp chí nhỏ, do học giả tự làm | Xuất bản; đảm bảo bài không mất | Nhiều người không đăng ký lưu trữ; một số tự liên hệ JASPER | Thấp; JASPER miễn phí | Hành vi: **chứng minh** (tỷ lệ tham gia thấp) | R19, R22 |
| Mạng lưu trữ (CLOCKSS, Portico, PKP PN, IA) | Lưu trữ | Cung cấp miễn phí cho tạp chí nhỏ qua JASPER/PKP PN | Tự gánh; JASPER kêu gọi tài trợ | **Chứng minh** | R22 |
| DOAJ, Crossref | Chuẩn chất lượng | Crossref yêu cầu "best efforts" lưu trữ (snippet R20) | — | Chính sách | R20 |
| Thư viện/nhóm quốc gia (Indonesia) | Cứu bài của tạp chí ngừng | Dự án thu >6.900 bài LIS Indonesia lên Zenodo (snippet) | Giờ công | Chứng minh (snippet) | R23 |
| Tác giả | Bài còn được tìm thấy | Tự lưu green OA | — | Giả định | — |
| Nhà tài trợ | Bảo vệ kết quả đã tài trợ | JASPER cần "sustainable funding" | Chưa rõ | Giả định | R22 |

### c. Documented cases by region

Laakso et al. (R18, bảng 4) phân bố 174 tạp chí OA biến mất 2000–2019 theo vùng:

| Vùng | Số tạp chí biến mất |
|---|---|
| North America | 57 |
| Europe & Central Asia | 52 |
| South Asia | 23 |
| East Asia & Pacific | 18 |
| Latin America & Caribbean | 17 |
| Middle East & North Africa | 6 |

- **NA, EU, Asia:** có số liệu trong cùng một nghiên cứu (`B-T3-C1`, VERIFIED scoped). Rücker phản biện rằng mẫu chỉ gồm tạp chí đã biến mất, nên không so được rủi ro giữa vùng; nhóm tác giả nói một số tạp chí thực ra vẫn online (R25 snippet).
- **Asia (Indonesia):** dự án lưu bài LIS từ tạp chí Indonesia đã ngừng (snippet R23, `B-T3-C6` INFERENCE). DOAJ ghi rằng số liệu của DOAJ Ambassador cho Indonesia cho thấy nhu cầu cấp bách (R22, không có số trong đoạn đã đọc).
- **Toàn cầu:** Eve 2024 với 7,4 triệu DOI (R19 trực tiếp qua blog tác giả; bản JLSC bị chặn).

### d. Demand and consequences of inaction

- **Demand đã chứng minh:** các mạng lưu trữ và DOAJ chi nguồn lực cho JASPER; "more and more journals contact JASPER directly, asking if they can be preserved" (R22).
- **Ngược chiều:** chuyển đổi thấp (khoảng 100 lời mời → 32 tạp chí), cho thấy tạp chí nhỏ không xem đây là ưu tiên kể cả khi miễn phí (`B-T3-C7`, INFERENCE). Nút thắt là **tham gia**, không phải thiếu công nghệ. Xác nhận nhận định B-O3 của Task B.
- **Hệ quả:** ~28% bài có DOI không xác nhận được bảo tồn (R19). Không suy ra được tỷ lệ đã mất.

### e. Existing solutions and limits

| Phương án | Làm được | Giới hạn |
|---|---|---|
| **PKP PN** (LOCKSS) | Lưu miễn phí cho tạp chí OJS | Yêu cầu OJS ≥ 3.1.2 (snippet R24); loại tạp chí kẹt ở OJS 2.x |
| **Project JASPER** (DOAJ, CLOCKSS, IA, Keepers, PKP) | Lưu miễn phí cho tạp chí trong DOAJ | Cần tiêu chí DOAJ; phụ thuộc tài trợ ("next up ... sustainable funding") |
| **CLOCKSS / Portico** | Dark archive cho nhà xuất bản | Có phí; tạp chí nhỏ ít tham gia |
| **Internet Archive Scholar / Wayback** | Bắt bản chụp, kể cả tạp chí đã chết | Không đầy đủ; không có metadata chuẩn cho từng bài (không kiểm tra trực tiếp trong phiên này) |
| **Keepers Registry** | Cho biết ai đang lưu gì | Chỉ tra cứu |

Gap được khẳng định phải vượt qua cả năm phương án này. Tôi **không** tìm thấy gap công nghệ ở việc lưu tạp chí **còn sống**. Gap có thể có ở hai chỗ: (1) tạp chí kẹt trên OJS 2.x không vào được PKP PN; (2) tạp chí **đã chết** chỉ còn trong Wayback, cần dựng lại thành bản ghi theo bài. Cả hai đều chưa được đo.

### f. Barriers

- **Pháp lý:** thấp với tạp chí OA giấy phép CC; trung bình với tạp chí không ghi giấy phép (không rõ ai giữ quyền khi biên tập viên biến mất).
- **Tài chính:** dịch vụ đã miễn phí cho nhóm nhỏ; vấn đề là tài trợ cho bên lưu trữ (JASPER).
- **Kỹ thuật:** nâng cấp OJS 2 → 3 là việc thật với tạp chí không có kỹ thuật viên (PKP có hướng dẫn nâng cấp; snippet R24).
- **Tổ chức:** biên tập viên tình nguyện, không có người kế nhiệm; nhận thức thấp ("lack of understanding", R22).

### g. Who pays, who maintains

- **Hiện tại:** CLOCKSS, IA, DOAJ, PKP tự gánh JASPER; thư viện thành viên trả phí CLOCKSS/Portico. Đã chứng minh với hạ tầng; **không** thấy tạp chí nhỏ trả.
- Cho công cụ mới: "none found".

### h. AI: meaningful advantage or not

- **Unnecessary** cho việc đăng ký lưu trữ: đó là vấn đề tham gia.
- **Có thể useful (HYPOTHESIS, `B-T3-C8`)** khi dựng lại tạp chí đã chết từ bản chụp Wayback: trích metadata bài (tiêu đề, tác giả, số, trang) từ HTML/PDF không đồng nhất. GROBID và công cụ trích metadata cổ điển là baseline mạnh; chưa thấy đo lường so sánh.

### i. Preservation vs restoring functionality

Với tạp chí, "công năng" cốt lõi là bài **tìm được và trích dẫn được** (DOI resolve, metadata đúng). Preservation dạng dark archive (CLOCKSS) giữ bài nhưng chỉ mở khi có trigger event. Giá trị thêm của khôi phục: biến bản chụp Wayback của tạp chí đã chết thành bản ghi có thể tìm, gắn lại vào DOI/trích dẫn. Bằng chứng nhu cầu cho việc này: dự án Indonesia (snippet). → `unclear`, nghiêng về preservation-sufficient với tạp chí còn sống.

### j. Resurrection theme fit

- T3 nói chung: **1**. Tạp chí không phải công nghệ; giữ kết luận Task B.
- Mỏ neo ứng viên: **OJS 2.x**, được PKP chính thức ghi "Not supported", EOL 2021 (R21, VERIFIED scoped). Đây là công nghệ cụ thể, đã hoàn tất khai tử.
- **Nhưng**: OJS 2 không phải **nguyên nhân chính** khiến tạp chí biến mất (Laakso và JASPER nêu nguồn lực và nhận thức). OJS 2 là rào cản phụ: chặn đường vào PKP PN. Dùng nó làm trung tâm là kéo giãn nhẹ. Tôi cho tiểu không gian B-T3a ("tạp chí kẹt trên OJS 2.x") anchor **2–3**, độ tin cậy **L**, vì chưa biết còn bao nhiêu tạp chí trên OJS 2.x (`B-T3-C10`, UNKNOWN).
- "No legitimate Resurrection angle found" cho T3 nói chung.

### k. Verdict for this space

**Narrow** thành B-T3a (tạp chí kẹt trên OJS 2.x hoặc đã chết chỉ còn bản Wayback), **có điều kiện**. Nếu falsifier dưới đây thất bại → **drop**.

Bằng chứng quyết định: hạ tầng mạnh đã có và miễn phí; vấn đề chính là tham gia; theme chỉ mở được qua OJS 2.x và chưa có số liệu quy mô.

Falsifier: đếm số tạp chí đang trên OJS 2.x (PKP công bố thống kê cài đặt OJS theo phiên bản, hoặc quét footer "Open Journal Systems 2.x"). Nếu < vài trăm tạp chí đang hoạt động, hoặc phần lớn đã có bản lưu ở Keepers Registry, thì drop.

---

## 5. T4 — Heritage archive transfer

### a. Problem and root causes

```text
Hệ quả: kho di sản số của cộng đồng (bản địa, ngôn ngữ) không còn truy cập,
        hoặc bị chuyển đi mà mất quy tắc truy cập văn hóa
│
├─ A. Tài trợ dự án có kỳ hạn; hết dự án thì phần mềm lỗi thời   [B-T4-C4]
├─ B. Nền tảng nền bị khai tử
│   ├─ Mukurtu 3 chạy trên Drupal 7; Drupal 7 hết hỗ trợ         [B-T4-C1, B-T4-C2]
│   └─ không nâng cấp tại chỗ: phải dựng site Mukurtu 4 mới và migrate
├─ C. Cơ quan chủ quản đổi
│   └─ ELDP/ELAR chuyển từ SOAS London sang BBAW Berlin (2021)   [B-T4-C3]
└─ D. Nguyên nhân KHÔNG phải nguồn lực
    └─ đàn áp chính trị (Apple Daily, Hồng Kông), cắt tài trợ chính trị (RFA) [B-T4-C6, B-T4-C7]
```

**Khi nào bảo tồn KHÔNG đáng làm (hoặc không được phép):**

- Khi cộng đồng chủ thể không đồng ý chuyển hoặc công khai: cultural protocols tồn tại để **hạn chế** truy cập. Bảo tồn trái ý cộng đồng là vi phạm, không phải giá trị.
- Khi bản sao đầy đủ đã có ở archive lớn (ELAR, PARADISEC) và cộng đồng không cần bản riêng.

### b. Stakeholders and target users

| Actor | Job-to-be-done | Hành vi hiện tại | Sẵn sàng đóng góp/trả | Chứng minh / giả định | Bằng chứng |
|---|---|---|---|---|---|
| Cộng đồng bản địa vận hành site Mukurtu 3 | Giữ kho với quy tắc truy cập văn hóa | Đang phải migrate sang Mukurtu 4; site tùy biến cần hỗ trợ riêng | Thường dựa vào grant | Hành vi migrate: **chứng minh** (có tài liệu và quy trình); số site: **chưa rõ** | R26 |
| Nhóm Mukurtu (WSU) | Duy trì phần mềm | Ký hợp đồng HeroDevs để vá bảo mật Drupal 7 cho Mukurtu 3 ~1 năm sau khi ra M4 | Có (chi tiền thật cho hỗ trợ hậu EOL) | **Chứng minh** | R26 |
| Nhà tài trợ (Mellon, IMLS, NEH, Arcadia) | Bảo tồn di sản | Grant nhiều đợt cho Mukurtu; 21 triệu EUR/10 năm cho ELDP/ELAR | Có | **Chứng minh** (Arcadia R29); Mellon số tiền chỉ snippet | R29, R31 |
| Archive ngôn ngữ (ELAR, PARADISEC) | Nhận và lưu bộ sưu tập | Đổi cơ quan chủ quản; tiếp nhận bộ sưu tập | — | **Chứng minh** (ELAR) | R29 |
| Nhà nghiên cứu đã làm dự án di sản (2002–2007) | Dự án tiếp tục sống | Dự án bị phần mềm lỗi thời, thiếu tiền | Thấp | **Chứng minh** (Strathman) | R30 |
| Archive diaspora/truyền thông (RFA Việt, Hàn) | Cứu bộ sưu tập khi bị cắt tài trợ | Chuyển sang thư viện đại học (U-M) | — | Snippet | R32 |

### c. Documented cases by region

- **NA:** Mukurtu (WSU, Mỹ), hợp tác với các bộ tộc vùng Plateau (snippet R31); dự án di sản bản địa 2002–2007 ở Mỹ, Canada (First Nations), Úc được Strathman 2019 khảo sát (R30). RFA Korean Service collection chuyển về University of Michigan; bộ sưu tập RFA tiếng Việt bị đe dọa sau khi RFA bị cắt tài trợ 03/2025 (snippet R32).
- **EU:** ELDP/ELAR chuyển từ SOAS (London) sang BBAW (Berlin) năm 2021 với grant Arcadia 21 triệu EUR/10 năm; ELDP đã cấp hơn 500 grant tài liệu hóa ngôn ngữ toàn cầu (R29).
- **Asia:** collection.news (Hồng Kông) lưu nội dung Apple Daily sau khi bị buộc đóng 06/2021 (snippet). Nguyên nhân là chính trị, **không phải thiếu nguồn lực**. Không tìm thấy site Mukurtu hoặc archive có cultural protocols ở châu Á (truy vấn: "Indigenous community digital archive Mukurtu Asia Pacific..."; `B-T4-C10`, UNKNOWN).
- **Other (Oceania):** Mukurtu bắt nguồn từ cộng đồng Warumungu, Northern Territory, Úc (snippet R31; Strathman R30 xác nhận dự án Úc). PARADISEC (Úc) không được kiểm tra lại trong phiên này.

### d. Demand and consequences of inaction

- **Demand đã chứng minh:** nhóm Mukurtu trả tiền cho HeroDevs để kéo dài vòng đời Drupal 7 (R26); Arcadia chi 21 triệu EUR để chuyển và mở rộng ELAR (R29); Mukurtu đầu tư công cụ migration và tài liệu 10 bước (R26).
- **Demand giả định:** cộng đồng muốn một công cụ **ngoài** công cụ migration chính thức. Không có bằng chứng.
- **Hệ quả nếu không làm:** site Mukurtu 3 tiếp tục chạy trên Drupal 7 không vá sau khi hợp đồng HeroDevs hết ("at their own risk", R26). Rủi ro cụ thể: lộ nội dung bị hạn chế theo cultural protocols nếu site bị tấn công. Đây là suy luận từ cơ chế, chưa có sự cố được ghi nhận (INFERENCE).

### e. Existing solutions and limits

| Phương án | Làm được | Giới hạn |
|---|---|---|
| **Mukurtu 4 migration tool** (R26) | Tự động migrate từ Mukurtu 3 "stock" | "Designed around a stock Mukurtu 3 site"; site đã sửa module Drupal 7 cần hỗ trợ riêng |
| **HeroDevs Drupal 7 extended support** (R26) | Vá bảo mật tạm thời | Có thời hạn (~1 năm sau khi ra M4); có phí |
| **Archive ngôn ngữ lớn (ELAR, PARADISEC)** | Nhận bộ sưu tập, có chính sách truy cập | Cộng đồng mất quyền kiểm soát trực tiếp so với site riêng |
| **Local Contexts TK Labels** (biết từ Task B; không mở lại) | Gắn nhãn quyền tri thức truyền thống | Nhãn, không phải cơ chế thi hành truy cập |
| **Webrecorder/Wayback** | Lưu bản công khai | **Không phù hợp**: không giữ (và không nên phá) quy tắc truy cập |

**Khoảng trống (INFERENCE):** site Mukurtu 3 tùy biến nằm ngoài phạm vi tool chính thức; việc kiểm chứng rằng **protocol semantics** (ai được xem gì) được giữ đúng sau migrate không có công cụ độc lập nào tôi tìm thấy. Đây là H4 của Task B, nay có mỏ neo thời gian cụ thể.

### f. Barriers

- **Pháp lý/đạo đức: cao.** Nội dung có hạn chế văn hóa; không thể dùng dữ liệu thật để demo công khai. Cần sự đồng ý của cộng đồng.
- **Tài chính:** phụ thuộc grant (Mellon, IMLS, Arcadia).
- **Kỹ thuật:** Drupal 7 → Drupal 11 là di trú chéo phiên bản lớn; M4 đổi mô hình media ("No more SCALD and atoms"; "Protocols are now required for all media assets"), nên ánh xạ protocol cho media cũ là điểm dễ sai (R26, INFERENCE về rủi ro).
- **Tổ chức:** người vận hành site cộng đồng thường không có kỹ sư Drupal (Strathman: maintenance issues, R30).

### g. Who pays, who maintains

- **Trả:** quỹ tư nhân và liên bang (Mellon, IMLS, NEH, Arcadia), nhóm Mukurtu (HeroDevs). **Đã chứng minh.**
- **Duy trì:** WSU Mukurtu team; archive tổ chức (BBAW cho ELAR); cộng đồng tự host.
- Cho công cụ bên thứ ba: "none found".

### h. AI: meaningful advantage or not

- **Unnecessary** cho migrate site stock: tool chính thức đã làm.
- **Rủi ro, không phải lợi thế**, nếu AI đọc nội dung bị hạn chế văn hóa. Gửi nội dung thiêng/hạn chế ra API bên ngoài có thể vi phạm protocol.
- Có thể **useful** để đọc module Drupal 7 tùy biến và đề xuất ánh xạ sang M4 (HYPOTHESIS); oracle là ma trận truy cập (user × item) trước/sau migrate. Kiểm tra ma trận này là tất định, không cần AI.

### i. Preservation vs restoring functionality

Với T4, **chức năng cốt lõi là quy tắc truy cập**. Một bản sao tĩnh công khai của kho Mukurtu sẽ **phá** giá trị chứ không giữ được. Vậy chỉ bảo tồn nội dung là **không đủ và có thể gây hại**; giá trị nằm ở giữ được một hệ thống có kiểm soát truy cập đang chạy. → `restoration-adds-value` (chính xác hơn: continuity of functionality là bắt buộc).

### j. Resurrection theme fit

- T4 nói chung: **1** (di sản không phải công nghệ chết). Giữ kết luận Task B.
- **Mỏ neo hợp lệ ở tiểu không gian B-T4a:** Mukurtu 3 / Drupal 7.
  - Drupal 7: hết hỗ trợ bảo mật (Mukurtu nói "Drupal 7 is no longer supported", R26, VERIFIED scoped; ngày 05/01/2025 chỉ snippet từ drupal.org do bị chặn, R28).
  - Mukurtu 3: được thay bằng Mukurtu 4; hỗ trợ M3 sẽ dừng ~1 năm sau khi ra M4 (R26).
  - Công nghệ chết ở đây là **nguyên nhân trực tiếp** buộc phải chuyển giao, nên không phải kéo giãn.
- Anchor **3** ("a specific technology with an officially announced or completed retirement anchors a revived workflow"), độ tin cậy **M**. Không đạt 4–5 vì giá trị chính là di trú sang nền tảng **sống** (M4), không phải đem M3 trở lại.

### k. Verdict for this space

**Narrow** sang **B-T4a**: kho di sản cộng đồng trên Mukurtu 3/Drupal 7 (đặc biệt site tùy biến), giữ đúng cultural protocols khi bắt buộc rời Drupal 7.

Bằng chứng quyết định:

- mỏ neo EOL chính thức, gây ra vấn đề trực tiếp;
- có chi tiêu thật quanh nó (HeroDevs, tool migration);
- giới hạn chính thức của tool ("stock" site) để lại khoảng trống hẹp.

Cảnh báo:

- số site M3 tùy biến chưa biết; có thể rất nhỏ;
- demo phải dùng dữ liệu tổng hợp;
- legal/ethics cao;
- đối thủ chính là chính nhóm Mukurtu, đơn vị được tài trợ và có hợp đồng hỗ trợ.

Falsifier: đếm site Mukurtu 3 công khai còn chạy (footer/generator) và hỏi nhóm Mukurtu tỷ lệ site cần hỗ trợ migrate tùy biến. Nếu tool chính thức đã phủ đa số và nhóm Mukurtu đang tự hỗ trợ phần còn lại → drop.

---

## 6. Cross-space analysis

Chỉ viết sau §2–§5.

### 6.1 Có vấn đề chung không?

**Giả thuyết ô dù của người dùng:** tri thức, chức năng và tài sản văn hóa số biến mất vì tổ chức chịu trách nhiệm không còn đủ nguồn lực.

| Không gian | "Thiếu nguồn lực" là nguyên nhân chính? | Bằng chứng |
|---|---|---|
| S2 | **Có**, nhưng gồm 2 kiểu khác nhau: hết tiền (FlyBase, TAIR) và hết người (SFAS) | R5, R7, R9 |
| T2 | **Một phần.** Cohost: có. Glitch, Yahoo!ブログ, Xiami: quyết định chiến lược của tập đoàn **có** nguồn lực | R11, R12, R14, R15 |
| T3 | **Có**, cùng với thiếu nhận thức ("lack of resources and understanding") | R22 |
| T4 | **Một phần.** Strathman, Mukurtu: có. Apple Daily, RFA: chính trị | R30, R26, R32 |

**Kết luận (`B-G-C1`, INFERENCE):** ô dù đúng ở mức **mô tả**, nhưng quá rộng để định hướng. "Thiếu nguồn lực" giải thích S2, T3 và một phần T4. Nó **không** giải thích các ca T2 lớn nhất và các ca T4 chính trị.

### 6.2 Một cơ chế chung hẹp hơn, có bằng chứng tốt hơn

**Cơ chế (`B-G-C2`, INFERENCE):** một nền tảng/runtime bên ngoài bị khai tử chính thức, và chi phí di trú đổ lên người giữ có ít nguồn lực.

| Công nghệ khai tử | Không gian | Bằng chứng |
|---|---|---|
| Adobe Flash (hết hạn 2020/2021) | S2 (PhET) | R8 |
| Google Fusion Tables (ngừng; xóa 03/2020) | S2 | R10 |
| OJS 2.x (EOL 2021) | T3 | R21 |
| Drupal 7 (hết hỗ trợ; Mukurtu 3) | T4 | R26 |

Cơ chế này có ba ưu điểm so với ô dù:

1. nó **có ngày cụ thể** và kiểm chứng được;
2. nó là nơi duy nhất cả ba không gian S2, T3, T4 có mỏ neo Resurrection **hợp lệ**;
3. nó cho thấy có người chi tiền thật để kéo dài hoặc thoát khỏi công nghệ chết (HeroDevs cho Drupal 7; PhET chuyển HTML5; CheerpJ).

**Đây là phát hiện, không phải đề xuất sản phẩm.**

### 6.3 Bằng chứng chống lại việc gộp

- **Thứ cần giữ khác nhau (`B-G-C3`, INFERENCE):**
  - S2 cần **tính toán/truy vấn**;
  - T3 cần **tính cố định và trích dẫn được** của văn bản;
  - T4 cần **quy tắc truy cập**, và với nó một bản sao công khai là **có hại**;
  - T2 cần **quan hệ cộng đồng**.

  Một "nền tảng bảo tồn chung" phải tối ưu bốn mục tiêu xung đột. Đặc biệt, mặc định công khai (T3) mâu thuẫn trực tiếp với mặc định hạn chế (T4).
- **Hạ tầng đã có ở mọi không gian (`B-G-C4`, INFERENCE):** KDL/Endings, ArchiveTeam, JASPER/PKP PN/CLOCKSS, Mukurtu/ELAR. Nút thắt lặp lại là **tham gia, tiền, nhân công di trú**, không phải thiếu công nghệ.
- **Người trả khác nhau:** S2 là trường/nhà tài trợ khoa học; T3 là mạng thư viện; T4 là quỹ văn hóa và cộng đồng; T2 không ai. Không có người mua chung.

### 6.4 Ai trả: điểm chung duy nhất có bằng chứng

**`B-G-C5`, INFERENCE:** chi tiêu đã chứng minh ở cả bốn không gian đều đi vào **dịch vụ và con người** (SLA của KDL, subscription TAIR, phí CLOCKSS, grant Arcadia, hợp đồng HeroDevs, giờ ArchiveTeam). Tôi **không** tìm thấy chi tiêu cho một **công cụ phần mềm** bảo tồn/chuyển giao do bên thứ ba bán. Kết quả này lặp lại H0 của Task B; H0 vẫn chưa bị bác bỏ theo hướng tích cực.

## 7. Challenges to the human's framing

1. **"Thiếu nguồn lực" là quá rộng.** Nó gom cắt tài trợ chính trị (FlyBase 2025, RFA), quyết định tập đoàn (Glitch, Xiami), kiệt sức tình nguyện (tạp chí học giả) và khai tử công nghệ (Drupal 7). Mỗi loại có người trả và cách xử lý khác nhau. Gom lại sẽ làm mất khả năng chọn người dùng mục tiêu.
2. **"Có giá trị" cần một tiêu chí.** KDL cho thấy nhiều PI **tự chọn** để dự án chết gọn (R2). Laakso bị phản biện rằng một phần tạp chí biến mất có thể là predatory (R25). Không phải mọi thứ biến mất đều là mất mát.
3. **Câu hỏi giả định giải pháp là "giữ lại".** Ở T4, giữ lại sai cách (công khai) là gây hại. Ở T2, cái đáng giữ (cộng đồng sống) không lưu trữ được.
4. **T2 không cùng loại với S2/T3/T4.** T2 là phòng ngừa thương mại; ba không gian kia là di sản học thuật/văn hóa có người giữ phi lợi nhuận. Đưa T2 vào cùng ô dù làm câu hỏi kém sắc.
5. **Ô dù không tự đem lại theme.** Chỉ khi thu hẹp về **công nghệ đã khai tử cụ thể** (Flash, Fusion Tables, OJS 2.x, Drupal 7) thì S2, T3, T4 mới có mỏ neo Resurrection hợp lệ. Nếu người dùng muốn giữ ô dù rộng, cổng theme sẽ tiếp tục trượt với T3/T4.

## 8. Unresolved questions

1. Còn bao nhiêu site Mukurtu 3 công khai, bao nhiêu đã tùy biến module? (B-T4a; quyết định có khoảng trống không)
2. Mukurtu 4 ra mắt chính thức ngày nào, và hợp đồng HeroDevs kết thúc khi nào? Trang Mukurtu nói "Mukurtu 4 is here" nhưng không ghi ngày trong đoạn tôi đọc.
3. Còn bao nhiêu tạp chí đang chạy OJS 2.x? PKP PN có thật sự yêu cầu ≥ 3.1.2 (mới chỉ là snippet)?
4. Bao nhiêu % công cụ nghiên cứu Flash/Java applet đã chạy được bằng Ruffle/CheerpJ?
5. Có ca nền tảng nhỏ ở EU hoặc châu Á đóng cửa với tài liệu chuyển giao cộng đồng không? (truy vấn của tôi không tìm thấy)
6. Alliance of Genome Resources có được NIH gia hạn sau 30/06/2025 không; FlyBase hiện ra sao (cuối 2026)?
7. Có ai đã từng trả tiền cho một **công cụ** (không phải dịch vụ/hosting) để chuyển giao hoặc bảo tồn trong bốn không gian này? (H0)
8. Văn bản Data Act Ch. VI có áp dụng cho nhà cung cấp phá sản hay ngừng dịch vụ không? (EUR-Lex không đọc được trong phiên)

## 9. References

Ngày truy cập của mọi ref: 2026-11-25. Điểm 0–5 theo thứ tự: Authority(20) / Technical Evidence(20) / Mechanism(20) / Context(15) / Freshness(10) / Reproducibility(10) / Bias(5). Weighted = Σ weight × score / 5. SR = Source Reliability, RR = Reference Relevance (H/M/L).

| Ref | URL | Title | Publisher | Pub date | Opened | Claims | Au | TE | Me | Co | Fr | Re | Bi | Weighted | SR | RR |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R1 | https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.3000333 | Challenges and recommendations to improve the installability and archival stability of omics computational tools | PLOS Biology (Mangul et al.) | 2019-06 | direct | B-S2-C1 | 5 | 5 | 4 | 4 | 2 | 5 | 4 | 86 | H | H |
| R2 | https://kdl.kcl.ac.uk/about/archiving-and-sustainability | Archiving and sustainability (KDL's pragmatic approach to managing 100 DH projects) | King's Digital Lab | n.d. (cập nhật sau 2021) | direct | B-S2-C2 | 4 | 3 | 5 | 5 | 4 | 3 | 3 | 80 | H | H |
| R3 | https://endings.uvic.ca/principles.html | Endings Principles for Digital Longevity | Endings Project, UVic | n.d. | direct | B-S2-C3 | 4 | 3 | 4 | 4 | 3 | 3 | 3 | 71 | H | M |
| R4 | https://globalbiodata.org/?p=5165 | Safeguarding Global Biodata Resources in a Challenging Funding Landscape | Global Biodata Coalition | 2025-06-16 | direct | B-S2-C5 | 4 | 3 | 4 | 5 | 5 | 2 | 3 | 76 | H | H |
| R5 | https://flybase.substack.com/p/flybase-nih-grant | FlyBase NIH grant | FlyBase | 2025-08-22 | direct | B-S2-C4 | 5 | 3 | 5 | 5 | 5 | 2 | 3 | 84 | H | H |
| R6 | https://www.thecrimson.com/article/2025/9/9/flybase-funding/ | Harvard Funding Cuts Endanger the Massive Fruit Fly Database | The Harvard Crimson | 2025-09-09 | direct | B-S2-C4 | 3 | 2 | 4 | 5 | 5 | 2 | 4 | 69 | M | H |
| R7 | https://pmc.ncbi.nlm.nih.gov/articles/PMC4545719/ | The Arabidopsis Information Resource: Making and Mining the 'Gold Standard' Annotated Reference Plant Genome | Genesis (via PMC), nhóm TAIR | 2015 | direct | B-S2-C6 | 4 | 3 | 4 | 4 | 2 | 3 | 2 | 68 | M | H |
| R8 | https://phet.colorado.edu/en/help-center/running-sims | Running Sims (help center) | PhET, University of Colorado Boulder | n.d. (hiện hành) | direct | B-S2-C8 | 4 | 3 | 4 | 4 | 4 | 3 | 3 | 73 | H | H |
| R9 | https://pdbj.org/info/sfas?lang=en | SFAS service notice | Protein Data Bank Japan | 2024-02-15 | direct | B-S2-C7 | 4 | 2 | 4 | 4 | 4 | 2 | 4 | 68 | H | M |
| R10 | https://support.google.com/fusiontables/answer/9185417 | FAQ: Google Fusion Tables | Google | 2018–2019 | direct | B-S2-C9 | 5 | 2 | 4 | 3 | 2 | 3 | 4 | 67 | H | M |
| R11 | https://blog.glitch.com/post/changes-are-coming-to-glitch/ | Changes are coming to Glitch | Glitch | 2025-05 | direct | B-T2-C3 | 5 | 2 | 4 | 4 | 5 | 2 | 3 | 73 | H | H |
| R12 | https://techcrunch.com/2024/09/12/cohost-the-x-rival-founded-with-an-anti-big-tech-manifesto-is-running-out-of-money-and-will-shut-down | Cohost ... is running out of money and will shut down | TechCrunch | 2024-09-12 | direct | B-T2-C1 | 3 | 3 | 4 | 4 | 4 | 2 | 4 | 68 | M | H |
| R13 | https://wiki.archiveteam.org/index.php/Cohost | Cohost | ArchiveTeam wiki | 2024–2025 | direct | B-T2-C2 | 3 | 4 | 4 | 4 | 4 | 3 | 3 | 73 | M | H |
| R14 | https://forest.watch.impress.co.jp/docs/news/1188058.html | 年内終了の"Yahoo!ブログ"が移行ツールを公開 | 窓の杜 (Impress) | 2019-06-03 | direct | B-T2-C4 | 3 | 2 | 4 | 4 | 2 | 2 | 4 | 60 | M | M |
| R15 | https://techcrunch.com/2021/01/04/alibaba-discontinues-xiami/ | Alibaba shuts down 12-year-old music streaming app Xiami | TechCrunch | 2021-01-04 | direct | B-T2-C5 | 3 | 1 | 3 | 3 | 2 | 2 | 4 | 49 | M | L |
| R16 | https://www.cooley.com/news/insight/2025/2025-09-08-paas-iaas-or-saas-be-aware-new-switching-rules-will-become-applicable-in-eu | PaaS, IaaS or SaaS? Be aware: new switching rules ... | Cooley LLP | 2025-09-08 | snippet only | B-T2-C6 | 3 | 2 | 3 | 3 | 5 | 1 | 3 | 56 | M | M |
| R17 | https://dtinit.org/blog/2025/01/28/year-3-growth | Year 3 for DTI brings growth | Data Transfer Initiative | 2025-01-28 | snippet only | T2 §e | 3 | 1 | 2 | 2 | 5 | 1 | 2 | 44 | M | L |
| R18 | https://arxiv.org/pdf/2008.11933 | Open is not forever: a study of vanished open access journals | JASIST 72(9), Laakso, Matthias, Jahn | 2021 | direct (PDF) | B-T3-C1 | 5 | 5 | 4 | 4 | 3 | 5 | 4 | 88 | H | H |
| R19 | https://blogs.lse.ac.uk/impactofsocialsciences/2024/02/13/the-digital-scholarly-record-is-at-risk | The digital scholarly record is at risk | LSE Impact Blog (M. P. Eve) | 2024-02-13 | direct | B-T3-C2 | 4 | 3 | 4 | 4 | 4 | 3 | 3 | 73 | H | H |
| R20 | https://iastatedigitalpress.com/jlsc/article/id/16288 | Digital Scholarly Journals Are Poorly Preserved: A Study of 7 Million Articles | JLSC 12(1), Eve | 2024-01-24 | snippet only (Anubis chặn) | B-T3-C2 | 5 | 4 | 4 | 4 | 4 | 4 | 3 | 83 | H | H |
| R21 | https://github.com/pkp/ojs/security | Security policy (Supported Versions table) | PKP | hiện hành | direct | B-T3-C3 | 5 | 2 | 3 | 4 | 5 | 3 | 4 | 72 | H | H |
| R22 | https://blog.doaj.org/2023/12/06/jasper-a-cross-industry-collaboration-making-a-real-difference | JASPER: a cross-industry collaboration making a real difference | DOAJ | 2023-12-06 | direct | B-T3-C5, B-T3-C7 | 4 | 3 | 4 | 4 | 3 | 2 | 2 | 68 | H | H |
| R23 | https://journals.ed.ac.uk/eor/article/download/12270/15117/44294 | (dự án lưu bài LIS Indonesia) | Edinburgh Diamond / EOR | n.d. | snippet only (PDF không trích được) | B-T3-C6 | 2 | 2 | 3 | 4 | 3 | 2 | 3 | 53 | L | M |
| R24 | https://forum.pkp.sfu.ca/t/pkp-preservation-network-support/72110 | PKP Preservation Network Support | PKP Community Forum | n.d. | snippet only | B-T3-C4 | 3 | 2 | 3 | 4 | 2 | 1 | 4 | 54 | M | H |
| R25 | https://arxiv.org/pdf/2011.01733 | Comment on 'Open is not forever' (Rücker); phản hồi Shelomi | arXiv / JASIST | 2020–2021 | snippet only | T3 §a, §c | 4 | 3 | 3 | 4 | 3 | 3 | 4 | 68 | M | M |
| R26 | https://mukurtu.org/mukurtu-4/ | Mukurtu CMS 4 (FAQ, migration, features) | Mukurtu / WSU | hiện hành (sau ra mắt M4) | direct | B-T4-C1, B-G-C5 | 5 | 3 | 5 | 5 | 5 | 3 | 3 | 86 | H | H |
| R27 | https://docs.mukurtu.org/migration/00MigrationOverview/ | Migration Overview | Mukurtu docs | n.d. | snippet only (404 khi tải) | T4 §e | 4 | 3 | 4 | 4 | 4 | 3 | 3 | 73 | H | H |
| R28 | https://www.drupal.org/about/drupal-7/d7eol | Drupal 7 End of Life | Drupal Association | 2023–2025 | snippet only (Anubis chặn) | B-T4-C2 | 5 | 2 | 3 | 3 | 4 | 2 | 4 | 65 | H | H |
| R29 | https://www.bbaw.de/presse/pressemitteilungen/pressemitteilung-new-berlin-center-for-the-documentation-of-endangered-languages | ELDP and ELAR move to Berlin with new grant from Arcadia | BBAW | 2021 | direct | B-T4-C3 | 5 | 2 | 4 | 4 | 3 | 2 | 3 | 69 | H | M |
| R30 | https://ijoc.org/index.php/ijoc/article/download/8018/2748 | Digitizing the Ancestors: Issues in Indigenous Digital Heritage Projects | Int. J. of Communication 13 (N. Strathman) | 2019 | direct (PDF) | B-T4-C4 | 4 | 3 | 4 | 5 | 2 | 3 | 4 | 73 | H | H |
| R31 | https://www.mellon.org/grant-story/mukurtu-provides-ethical-tools-for-archiving-and-preservation | Designed with Care: Mukurtu Provides Ethical Tools ... | Mellon Foundation | 2024-12-10 | direct (trang); số tiền 1,5 triệu USD chỉ snippet | B-T4-C5 | 4 | 1 | 3 | 4 | 4 | 1 | 2 | 56 | M | M |
| R32 | https://blogs.lib.umich.edu/notes-asia-library/radio-free-asia-korean-service-finds-new-home-u-m-library | Radio Free Asia Korean Service Finds a New Home at U-M Library | U-M Library | 2025 | snippet only | B-T4-C6 | 3 | 1 | 2 | 3 | 5 | 1 | 3 | 48 | M | L |
| R33 | https://blog.archive.org/2020/11/19/flash-animations-live-forever-at-the-internet-archive/ | Flash animations live forever at the Internet Archive | Internet Archive | 2020-11-19 | snippet only | S2 §e | 4 | 3 | 4 | 3 | 2 | 3 | 3 | 66 | H | M |
| R34 | https://digitalhumanities.org/dhq/vol/17/1/000668/000668.html | (Holmes & Takeda, Endings, DHQ 17.1) | DHQ | 2023 | snippet only | S2 §c | 4 | 3 | 4 | 4 | 3 | 3 | 3 | 71 | H | M |
| R35 | https://digitalhumanities.org/dhq/vol/13/1/000411/000411.html | Managing 100 Digital Humanities Projects: Digital Scholarship & Archiving in King's Digital Lab | DHQ 13.1 (Smithies et al.) | 2019 | snippet only | B-S2-C2 (xác nhận) | 4 | 3 | 4 | 4 | 2 | 3 | 3 | 69 | H | H |
| R36 | https://www.rfa.org/english/news/china/internet-disappearing-archives-05242024131340.html | Chinese researchers say internet archives are fast disappearing | Radio Free Asia | 2024-05-24 | snippet only | §7 (bối cảnh) | 2 | 1 | 2 | 3 | 4 | 1 | 2 | 41 | L | L |
| R37 | https://doaj.org/preservation/ | Digital preservation (JASPER) | DOAJ | hiện hành | snippet only | T3 §e | 4 | 1 | 3 | 3 | 4 | 1 | 2 | 53 | H | M |

### Sổ claim

| Claim | Nhãn | Nội dung tóm tắt | Refs | Mức chuỗi bằng chứng |
|---|---|---|---|---|
| B-S2-C1 | VERIFIED (scoped vào nghiên cứu) | Mangul: ~28% của 36.702 URL không truy cập được; 28% của 98 tool không cài được; không tạp chí nào yêu cầu đảm bảo tool tiếp tục chạy | R1 | nguồn gốc + dữ liệu/script công khai (cơ chế tái lập được, chưa chạy lại) |
| B-S2-C2 | VERIFIED (scoped "KDL tuyên bố") | KDL thừa hưởng gần 100 dự án năm 2015, đa số không có tiền; 6 lựa chọn; nhiều PI xin lưu gọn | R2, R35 | nguồn gốc + xác nhận độc lập (snippet DHQ) |
| B-S2-C3 | VERIFIED (scoped) | Endings 4.1: không phụ thuộc phần mềm phía server | R3 | nguồn gốc |
| B-S2-C4 | VERIFIED | FlyBase: NIH chấm dứt grant 05/2025, >2 triệu USD/năm; 8 nhân viên Harvard bị cho nghỉ; Cambridge sống nhờ quyên góp và Wellcome | R5, R6 | nguồn gốc + xác nhận độc lập |
| B-S2-C5 | VERIFIED (scoped "GBC ước tính") | 32/52 GCBR nhận tiền liên bang Mỹ, 26 phụ thuộc chính; gây quỹ khẩn cấp, phí, đóng băng cập nhật | R4 | nguồn gốc |
| B-S2-C6 | VERIFIED | TAIR chuyển sang subscription qua Phoenix sau NSF 2013; 42% lượt truy cập từ châu Á (2014) | R7 (+ snippet Wikipedia/Phoenix) | nguồn gốc (do chính nhóm TAIR viết) + xác nhận snippet |
| B-S2-C7 | VERIFIED (scoped) | PDBj SFAS tạm ngừng 02/2024 vì thiếu nhân sự IT | R9 | nguồn gốc |
| B-S2-C8 | VERIFIED (scoped "PhET tuyên bố") | Flash sims không chạy từ 01/01/2021; PhET dựa vào quyên góp để chuyển đổi; Java qua CheerpJ, không đủ tính năng | R8, R33 | nguồn gốc + snippet độc lập |
| B-S2-C9 | VERIFIED (scoped) | Google Fusion Tables ngừng; dữ liệu xóa sau 03/03/2020 | R10 | nguồn gốc |
| B-S2-C10 | INFERENCE | Tài nguyên được trích dẫn nhiều phần lớn tự sống sót (Wren 2017 qua Task B) | Task B A §11.2 | chưa mở lại |
| B-S2-C11 | INFERENCE | Demand đầu lớn đã chứng minh; đầu đuôi dài là giả định | R4, R5, R7, R1 | suy luận từ các claim trên |
| B-S2-C12 | HYPOTHESIS | Runtime bị khai tử là mỏ neo theme hợp lệ cho B-S2a (anchor 3) | R8, R10 | — |
| B-S2-C13 | HYPOTHESIS | AI hữu ích để lập danh mục công năng server-side và chuyển đổi applet; chưa có benchmark | — | — |
| B-S2-C14 | UNKNOWN | Không có nghiên cứu định lượng về suy giảm công cụ nghiên cứu ở châu Á | truy vấn ghi ở §2c | — |
| B-T2-C1 | INFERENCE | Cohost: 30.000 MAU, 2.630 subscriber, thâm hụt 17.000 USD (03/2024) | R12 | nguồn thứ cấp mở trực tiếp; nguồn gốc (bài của Cohost) không mở |
| B-T2-C2 | VERIFIED (scoped "ArchiveTeam ghi") | Cohost hoãn tắt cho ArchiveTeam theo yêu cầu nhà tài trợ; "Saved!"; phần lớn dữ liệu ở long tail | R13 (+ snippet Wikipedia) | nguồn gốc + snippet |
| B-T2-C3 | VERIFIED (scoped "Glitch tuyên bố") | Hosting dừng 08/07/2025; tải mã tới hết 2025; redirect tới ít nhất hết 2026 | R11 | nguồn gốc |
| B-T2-C4 | INFERENCE | Yahoo!ブログ đóng 15/12/2019; tool chuyển 03/06/2019 sang Ameba/livedoor/Seesaa, sau đó Hatena | R14 (+ snippet ITmedia/GIGAZINE) | báo chí mở trực tiếp + snippet |
| B-T2-C5 | INFERENCE | Xiami đóng 02/2021; đối thủ nhận playlist | R15 (chi tiết chuyển: snippet) | thứ cấp |
| B-T2-C6 | INFERENCE | Data Act Ch. VI áp dụng từ 12/09/2025 cho SaaS; export máy đọc được | R16 | snippet only |
| B-T2-C7 | INFERENCE | Ca lớn được nền tảng nhận tự làm importer; ca nhỏ không có ai | R13, R14, R15 | suy luận |
| B-T2-C8 | HYPOTHESIS | Nhà vận hành nhỏ sẽ trả cho bộ công cụ đóng cửa: không có bằng chứng | — | — |
| B-T2-C9 | UNKNOWN | Không có ca nền tảng nhỏ ở EU/châu Á có tài liệu chuyển giao | truy vấn ở §3c | — |
| B-T2-C10 | INFERENCE | Theme T2 (trước khi đóng) ≈ 2 | rubric anchors | suy luận |
| B-T3-C1 | VERIFIED (scoped vào nghiên cứu) | 174 tạp chí OA biến mất 2000–2019; phân bố theo vùng | R18 (phản biện R25) | nguồn gốc + dữ liệu công khai; có phản biện |
| B-T3-C2 | VERIFIED (scoped "Eve báo cáo") | 0,96% thành viên Crossref lưu >75% ở ≥3 archive; ~28% bài có DOI không xác nhận được bảo tồn | R19, R20 | blog của tác giả mở trực tiếp + abstract qua snippet |
| B-T3-C3 | VERIFIED (scoped "PKP tuyên bố") | OJS 2.x "Not supported", phát hành 2005, EOL 2021 | R21 (+ snippet Wikipedia) | nguồn gốc |
| B-T3-C4 | INFERENCE | PKP PN yêu cầu OJS ≥ 3.1.2 | R24 | snippet only |
| B-T3-C5 | VERIFIED (scoped "DOAJ tuyên bố") | JASPER: ~100 lời mời → >40 đơn → 32 chọn (29 CLOCKSS+IA, 3 PKP PN); "lack of resources and understanding"; cần tài trợ | R22 | nguồn gốc |
| B-T3-C6 | INFERENCE | Dự án Indonesia thu >6.900 bài LIS từ tạp chí ngừng lên Zenodo | R23 | snippet only |
| B-T3-C7 | INFERENCE | Nút thắt là tham gia, không phải công nghệ | R22, R19 | suy luận |
| B-T3-C8 | HYPOTHESIS | Dựng lại tạp chí đã chết từ Wayback thành bản ghi theo bài có giá trị; AI có thể giúp trích metadata | — | — |
| B-T3-C9 | INFERENCE | OJS 2.x là mỏ neo theme yếu (2–3) vì không phải nguyên nhân chính | R21, R18, R22 | suy luận |
| B-T3-C10 | UNKNOWN | Số tạp chí còn chạy OJS 2.x | — | — |
| B-T4-C1 | VERIFIED (scoped "Mukurtu tuyên bố") | M3 trên Drupal 7; D7 không còn hỗ trợ; hợp đồng HeroDevs ~1 năm sau M4; tool migrate cho site stock; M4 bắt buộc protocol cho mọi media | R26 | nguồn gốc |
| B-T4-C2 | INFERENCE | Drupal 7 hết hỗ trợ bảo mật 05/01/2025 | R28 (+ R26 xác nhận "no longer supported") | ngày: snippet only |
| B-T4-C3 | VERIFIED | ELDP/ELAR chuyển từ SOAS sang BBAW 2021 với grant Arcadia | R29 (+ snippet Wikipedia) | nguồn gốc + snippet độc lập |
| B-T4-C4 | VERIFIED (scoped vào nghiên cứu) | Dự án di sản bản địa 2002–2007 gặp phần mềm lỗi thời, thiếu tiền, khó bảo trì | R30 | nguồn gốc học thuật |
| B-T4-C5 | INFERENCE | Mellon cấp 1,5 triệu USD cho Mukurtu (lần thứ tư) | R31 | số tiền: snippet only |
| B-T4-C6 | INFERENCE | Bộ sưu tập RFA tiếng Việt bị đe dọa sau 03/2025; RFA Korean chuyển về U-M | R32 | snippet only |
| B-T4-C7 | INFERENCE | collection.news lưu Apple Daily: nguyên nhân chính trị, không phải nguồn lực | snippet (không có ref riêng; xem §5c) | snippet only |
| B-T4-C8 | HYPOTHESIS | Migrate M3 tùy biến → M4 làm mất ngữ nghĩa protocol | R26 | — |
| B-T4-C9 | INFERENCE | Mukurtu 3/Drupal 7 là mỏ neo theme hợp lệ, anchor 3 | R26, R28 | suy luận |
| B-T4-C10 | UNKNOWN | Không có archive có cultural protocols ở châu Á trong kết quả | truy vấn ở §5c | — |
| B-G-C1 | INFERENCE | Ô dù "thiếu nguồn lực" đúng mô tả, quá rộng để định hướng | §6.1 | suy luận |
| B-G-C2 | INFERENCE | Cơ chế chung hẹp: công nghệ khai tử chính thức đẩy chi phí di trú sang người giữ ít nguồn lực | R8, R10, R21, R26 | suy luận từ 4 claim VERIFIED scoped |
| B-G-C3 | INFERENCE | Thứ cần giữ khác nhau và xung đột (công khai vs hạn chế) | §6.3 | suy luận |
| B-G-C4 | INFERENCE | Hạ tầng đã có ở mọi không gian; nút thắt là tham gia/tiền/nhân công | §2e–§5e | suy luận |
| B-G-C5 | INFERENCE | Chi tiêu đã chứng minh đi vào dịch vụ/con người, không vào công cụ của bên thứ ba (H0 Task B chưa bị bác bỏ) | R2, R7, R22, R26, R29 | suy luận |

**Đếm nhãn:** VERIFIED 18 (trong đó 15 scoped vào "nguồn X tuyên bố/báo cáo"), INFERENCE 22, HYPOTHESIS 5, UNKNOWN 4. Tổng 49.

**Quan hệ với claim Task B:**

- Xác nhận `C-G-C1` (28% ≠ đã mất) qua R19.
- Xác nhận B-O3 (T3 là vấn đề tham gia) qua R22.
- Mở rộng H4 (T4) bằng mỏ neo Mukurtu 3/Drupal 7 (R26).
- Xác nhận `B-O2-C3` (ArchiveTeam cần nhà vận hành hợp tác) qua R13: Cohost hoãn tắt theo yêu cầu nhà tài trợ.
- Không kiểm lại Wren 2017 (A §11.2) và giữ ở INFERENCE.
