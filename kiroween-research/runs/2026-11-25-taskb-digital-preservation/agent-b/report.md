# Task B Round 1 — Agent B

## Metadata

| Trường | Giá trị |
|---|---|
| Model | `claude-sonnet-5-5` (quan sát được từ môi trường runtime của chính phiên này; khớp với cấu hình mission §3) |
| Effort | Medium theo cấu hình mission; **không quan sát được** trực tiếp từ launch args |
| Bắt đầu (UTC) | 2026-11-25 12:27 (lệnh `date -u` đầu tiên trả về 12:28:13) |
| Kết thúc (UTC) | 2026-11-25 12:36 |
| Số lượt WebSearch | 20 (mode `standard`, không dùng `extended`) |
| Nguồn mở trực tiếp (curl, HTTP 200, đã đọc nội dung) | 24 (R1–R24) |
| Nguồn chỉ có snippet | 7 (R25–R31) |
| Thất bại | (1) JLSC — bài gốc của Eve (2024) bị Anubis proof‑of‑work chặn → dùng bài LSE do chính tác giả viết (R7). (2) EUR‑Lex và legislation.gov.uk trả 202/challenge → Điều 6 Directive (EU) 2019/790 chỉ là snippet/kiến thức nền (R27). (3) merlin.obs.coe.int 403. (4) asiae.co.kr các bài 2021/2025 timeout (bài 2026 mở được). (5) softwareheritage.org timeout → không dùng số liệu SWH. (6) blog.archive.org về Hachette 404 → phán quyết chỉ có snippet (R25). (7) Trang EC ECI tin tức chỉ có 1 đoạn; nội dung phản hồi lấy từ API presscorner của EC (R2). |
| Công cụ | WebSearch (snippet), `curl` + trích xuất văn bản (mở trực tiếp). Không subagent, không cài gói, không đọc thư mục agent khác. |

Quy ước nhãn (áp dụng nghiêm theo brief §3):
- **ĐÃ XÁC MINH (VERIFIED)**: (a) khẳng định "nguồn X báo cáo Y" khi tôi đã mở trực tiếp nguồn gốc X; hoặc (b) khẳng định về thế giới khi có nguồn gốc mở trực tiếp **và** ít nhất một xác nhận độc lập cũng được mở trực tiếp.
- **SUY LUẬN (INFERENCE)**: có bằng chứng ủng hộ nhưng chỉ một nguồn, hoặc xác nhận độc lập chỉ là snippet, hoặc là diễn giải của tôi.
- **GIẢ THUYẾT (HYPOTHESIS)**: cần thử nghiệm; chưa có bằng chứng hành vi.
- **CHƯA RÕ (UNKNOWN)**: thiếu bằng chứng.

## 1. Method

**Phương pháp đã chọn và lý do**

1. **Cây vấn đề / root-cause analysis** (§2): mission giả định "suy giảm người dùng" là nguyên nhân. Cây vấn đề cho phép tách nguyên nhân gốc (chi phí vận hành, phụ thuộc server, IP/luật, nền tảng độc quyền theo nhà mạng, kiểm duyệt) khỏi triệu chứng.
2. **Stakeholder analysis + Jobs‑to‑be‑Done** (§3): mission yêu cầu phân biệt nhu cầu *được chứng minh* với nhu cầu *giả định*. JTBD buộc mỗi nhóm phải có "việc cần làm" cụ thể và hành vi quan sát được (chữ ký, tiền quyên góp, giờ tình nguyện, di cư).
3. **Alternative / gap analysis** (§5): không được tuyên bố khoảng trống thị trường khi chưa xét giải pháp hiện có; mỗi không gian cơ hội ghi rõ đối thủ mạnh nhất.
4. **Sustainability analysis** (§6): ai hưởng lợi / ai trả / ai bảo trì — vì các trường hợp thất bại (Cyworld, Cohost) thất bại đúng ở điểm này.
5. **Hypothesis validation** (§10): mỗi không gian có "thí nghiệm nhỏ nhất có thể bác bỏ".
6. **Red-team** (theo tinh thần skill `idea-red-team`, không tải toàn bộ skill): §11 thách thức chính giả thuyết của mission.

**Không làm**: không phỏng vấn người dùng (không có); không thiết kế ứng dụng hay chọn sản phẩm; không đọc báo cáo của agent khác hoặc Phase 1/2; không chấm điểm so với ứng viên Phase 2. Không tải các skill dự án dài (user-problem-validation, historical-technology-discovery) vì time box 60 phút — áp dụng nguyên tắc của chúng trực tiếp. Không lặp lại các chủ đề đã khám phá (thiết bị cloud bị brick, link rot/read‑later, Q&A suy giảm, Discord, InfoPath, Flash, Jamboard, Google Reader, Yahoo Pipes, DMOZ, media gia đình, gia phả Hán Nôm). Pew 2024 (link rot) chỉ được dùng làm bối cảnh chung, không làm không gian cơ hội.

**Góc nhìn mới so với các chủ đề đã khám phá**: tôi tập trung vào (a) **phần mềm phụ thuộc server không phải thiết bị** (game live‑service), (b) **khoảnh khắc đóng cửa** của nền tảng cộng đồng nhỏ/vừa và vai trò của nhà vận hành, (c) **hồ sơ tri thức học thuật** biến mất, (d) **nền tảng di động/web khu vực** ở châu Á/châu Phi, (e) **AI như công cụ tái dựng mã nguồn có oracle kiểm chứng**.

## 2. Root causes

### 2.1 Cây vấn đề

```
VẤN ĐỀ TRUNG TÂM: Giá trị do người dùng/cộng đồng tạo ra trên một nền tảng số
                  trở nên không truy cập được khi nền tảng ngừng hoạt động
│
├─ Nguyên nhân gốc A — Kinh tế vận hành
│   ├─ Chi phí chạy hạ tầng tăng theo tuổi nền tảng + lạm dụng (Glitch: "millions of users running
│   │   tens of millions of apps") [B-G-C3]
│   ├─ Doanh thu không bù chi phí ở quy mô ngách (Cohost: 30.000 MAU, 2.630 người trả phí,
│   │   thâm hụt 17.000 USD/tháng) [B-G-C4]
│   └─ Mô hình vòng đời ngắn cố ý (game gacha Nhật: >70% ngừng trước năm thứ 3) [B-G-C5]
│
├─ Nguyên nhân gốc B — Kiến trúc phụ thuộc server/DRM
│   ├─ Phần mềm chỉ chạy khi server nhà phát hành còn sống (EC thừa nhận: "Modern video games
│   │   often rely on publishers' servers to function") [B-O1-C2]
│   └─ Nền tảng riêng theo nhà mạng + mã hoá (i-mode DoJa / EZweb BREW / SoftBank MIDP;
│       CPRM trên thẻ SD) [B-O4-C1]
│
├─ Nguyên nhân gốc C — Pháp lý/IP
│   ├─ Không ai được phép phân phối lại (US DMCA §1201: thư viện không được cấp quyền truy cập
│   │   từ xa cho game) [B-G-C8]
│   └─ IP bị chuyển tay nhiều lần, tranh chấp domain (Cyworld: 5 lần đổi chủ) [B-O2-C5]
│
├─ Nguyên nhân gốc D — Không ai chịu trách nhiệm lưu trữ
│   └─ "No consensus over who should be responsible for archiving scholarship" — ~28% bài báo có
│       DOI không thấy trong archive lớn [B-O3-C1]
│
├─ Nguyên nhân gốc E — Kiểm duyệt / chính sách nhà nước (khu vực cụ thể)
│   └─ Internet Trung Quốc thời kỳ đầu: tác giả quy cho siết quản lý + tự kiểm duyệt + chuyển
│       sang mobile [B-O4-C4]
│
└─ Triệu chứng (thường bị nhầm là nguyên nhân)
    ├─ Suy giảm người dùng (Mxit: còn 1,2 triệu đến 7/2015 do WhatsApp/Facebook) [B-G-C6]
    └─ Thông báo đóng cửa ngắn hạn → người dùng/archivist chạy đua
```

### 2.2 Suy giảm người dùng: nguyên nhân hay triệu chứng?

- **SUY LUẬN [B-G-C1]**: Trong các trường hợp đã xem, suy giảm người dùng thường là *triệu chứng trung gian* của một nguyên nhân khác (dịch chuyển công nghệ: feature phone → smartphone với Mxit và i-mode; cạnh tranh nền tảng lớn với Cohost/Cyworld), còn *nguyên nhân trực tiếp* của việc đóng cửa là chi phí vận hành vượt doanh thu (Cohost, Glitch) hoặc quyết định danh mục sản phẩm (game live‑service). Bằng chứng: R14 (Cohost), R11 (Glitch), R19 (Mxit), R24 (gacha). Phản chứng: Glitch có "millions of users" nhưng vẫn đóng hosting — suy giảm người dùng **không** phải điều kiện cần.
- **SUY LUẬN [B-G-C2]**: Với game live‑service, đóng cửa xảy ra *dù cộng đồng còn hoạt động*: City of Heroes đóng 2012, cộng đồng vẫn tự chạy server và quyên góp hằng tháng nhiều năm sau (R10). Đây là bằng chứng rằng "nền tảng không thể tồn tại *về mặt thương mại*" ≠ "giá trị đã hết".

### 2.3 Thất bại thương mại vs lỗi thời thực sự

| Loại | Dấu hiệu | Ví dụ | Hệ quả cho bảo tồn |
|---|---|---|---|
| Thất bại thương mại, giá trị còn | Cộng đồng còn hoạt động, có hành vi trả tiền/tình nguyện sau đóng cửa | City of Heroes (R10), Cohost → di cư sang Mastodon/Bluesky (R14), Cyworld (người dùng "didn't delete the app and just kept waiting", R17) | Có lý do kinh tế cho *tiếp nối* (continuity), không chỉ lưu trữ tĩnh |
| Lỗi thời thực sự (nền tảng kỹ thuật chết) | Phần cứng/mạng không còn; giá trị chủ yếu là lịch sử | Keitai i-mode (dừng 2021, R8), Mxit (R19) | Chỉ có giá trị **heritage/nghiên cứu**; không có lý do phục hồi dịch vụ |
| Ngắn hạn cố ý | Vòng đời dự kiến ngắn | Gacha Nhật (R24) | Phần lớn **không đáng** bảo tồn toàn bộ; chọn lọc |

### 2.4 Khi nào bảo tồn KHÔNG chính đáng

- **SUY LUẬN [B-G-C7]**: (1) Khi nội dung chủ yếu là dữ liệu cá nhân riêng tư không có sự đồng ý (tin nhắn riêng Mxit/Skype) — nghĩa vụ xoá có thể nặng hơn giá trị lưu trữ. (2) Khi chi phí tái dựng > giá trị cho bất kỳ nhóm nào đã thể hiện bằng hành vi (đa số trong ~2.200 game gacha không có cộng đồng hồi sinh nào được ghi nhận — **CHƯA RÕ** về tỷ lệ, tôi không tìm thấy số liệu). (3) Khi nguồn biến mất là tạp chí săn mồi (predatory): Shelomi (R31, snippet) phản biện rằng một phần tạp chí "biến mất" của Laakso et al. có thể là predatory — bảo tồn chúng không phục vụ hồ sơ học thuật. (4) Khi nội dung bị gỡ do pháp luật hợp lệ ở nơi lưu trữ.

## 3. Stakeholders and demand

| Stakeholder | Tác nhân cụ thể | Job‑to‑be‑done | Hành vi hiện tại | Sẵn sàng đóng góp | Sẵn sàng trả tiền | Demonstrated / hypothetical | Bằng chứng |
|---|---|---|---|---|---|---|---|
| Người chơi game (cá nhân) | 1,29 triệu công dân EU ký ECI "Stop Destroying Videogames" | "Giữ được game tôi đã mua sau khi server tắt" | Ký kiến nghị; dùng private server | **Cao** (chữ ký, vận động) | Đã mua game; chưa rõ trả thêm | **Demonstrated** (chính trị/công dân) | R1, R2 [B-O1-C1] |
| Cộng đồng game hồi sinh | Homecoming (City of Heroes) | "Tiếp tục chơi và phát triển game đã chết" | Tự chạy server ~5 năm trước khi có license; "funded every month by the playerbase" | **Rất cao** (tiền + giờ dev) | Quyên góp; không phí bắt buộc | **Demonstrated** | R10 [B-O1-C4] |
| Cộng đồng bảo tồn kỹ thuật (Asia) | Kahvibreak / Keitai Wiki (keitai) | "Cứu game feature phone trước khi phần cứng chết" | Brute‑force khoá CPRM bằng GPU 20 ngày; viết ktdumper; desolder eMMC | **Rất cao** (kỹ năng phần cứng hiếm) | Quyên góp nhỏ (link donation cho Kraze) | **Demonstrated** (giờ tình nguyện) | R8 [B-O4-C2] |
| Archivist tình nguyện | ArchiveTeam (Cohost, Glitch) | "Chụp lại nền tảng trước ngày tắt" | Chạy warrior, ArchiveBot; cần nhà vận hành hợp tác | **Cao** | Không trả; Internet Archive lưu | **Demonstrated** | R12, R13 [B-O2-C3] |
| Nhà vận hành nền tảng (nhỏ) | Cohost (Anti Software Software Club), Glitch (Fastly) | "Đóng cửa có trách nhiệm với chi phí tối thiểu" | Xây export, redirect, giữ server thêm để ArchiveTeam xong | Trung bình — giới hạn bởi tiền | Không có tiền (Cohost: nhân viên không lương) | **Demonstrated** (hành vi đóng cửa) | R11, R12, R14 [B-O2-C1, C2] |
| Nhà phát hành game | ESA (vận động hành lang US); NCSoft | "Bảo vệ thị trường re‑release, tránh trách nhiệm pháp lý" | Phản đối miễn trừ truy cập từ xa; NCSoft cấp license miễn phí 1 lần | Thấp; ngoại lệ | — | Demonstrated (phản đối) | R4, R10 [B-G-C8] |
| Thư viện / tổ chức di sản | VGHF, Software Preservation Network, Yale (EaaSI) | "Cho nhà nghiên cứu truy cập phần mềm cũ hợp pháp" | Nghiên cứu, kiến nghị §1201; emulation | Cao | Ngân sách tài trợ: Yale nhận 3,5 triệu USD Mellon/Sloan | **Demonstrated** (ngân sách) | R3, R4, R22 [B-G-C9] |
| Nhà nghiên cứu / học giả | Tác giả bài báo OA; thư viện | "Trích dẫn còn kiểm chứng được" | Dựa vào CLOCKSS/LOCKSS/Portico/IA (tôi không mở các trang này) | Trung bình | Thư viện trả phí thành viên archive (**CHƯA RÕ**, không mở nguồn) | Mixed | R5, R7 [B-O3-C1, C2] |
| Người dùng mạng xã hội cũ (Asia) | Người dùng Cyworld (Hàn Quốc) | "Lấy lại ảnh gia đình/tuổi trẻ" | Chờ nhiều năm; ~4 triệu truy cập "Memory Search" trong 11 giờ (2021, snippet) | Chưa rõ | Đã từng trả Dotori; 2026 chưa rõ | Demonstrated (2021) / hypothetical (2026) | R17, R26 [B-O2-C4] |
| Nhà phát triển phần mềm | Người dùng Glitch ("tens of millions of apps") | "Di chuyển app/code sang nơi khác" | Dùng script export, redirect | — | Đã trả Glitch Pro; chưa rõ trả cho migration | Mixed | R11 |
| Nhà lập pháp/quản lý | European Commission | "Cân bằng IP và quyền người tiêu dùng" | Từ chối nghĩa vụ pháp lý; khởi động code of conduct "end of life" | — | — | Demonstrated (văn bản chính thức) | R2 [B-O1-C3] |

**Kết luận về nhu cầu**: Nhu cầu *được chứng minh* mạnh nhất nằm ở **game live‑service** (chữ ký quy mô triệu + cộng đồng tự tài trợ server) và **cộng đồng bảo tồn kỹ thuật tình nguyện** (giờ công rất lớn). Nhu cầu của **người dùng cá nhân mạng xã hội đã chết** có bằng chứng (Cyworld 2021) nhưng không chuyển hoá được thành doanh thu bền vững. **Không có bằng chứng** nào trong phiên này về việc cá nhân sẵn sàng **trả tiền** cho một công cụ bảo tồn mới — đây là giả định chưa kiểm chứng lớn nhất [B-G-C10, UNKNOWN].

## 4. Preservation dimensions

| Chiều | Giá trị tạo ra | Khả thi kỹ thuật | Khả thi kinh tế | Bằng chứng | Đánh giá |
|---|---|---|---|---|---|
| **Content** (nội dung công khai) | Trung bình–cao; hồ sơ lịch sử | Cao cho web tĩnh; thấp cho SPA/API (Cohost cần TRPC batching tắt, R12) | Có tổ chức lớn (IA ~23–33 triệu USD chi/năm, R20) | R12, R18, R20 | Đã có người làm tốt; khoảng trống ở **trang động** và **cửa sổ đóng cửa** |
| **Knowledge** (tri thức có cấu trúc, học thuật) | Cao (trích dẫn, khoa học) | Cao (văn bản/PDF) | Trung bình — có CLOCKSS/Portico nhưng phủ không đều | R5, R7 | ~28% DOI không thấy trong archive lớn [B-O3-C1] |
| **Software functionality** | Cao cho heritage & nghiên cứu; cao cho người chơi | **Khó**: server logic không có, DRM, nền tảng riêng | Thấp; pháp lý chặn phân phối | R3, R4, R8, R10 | Giá trị lớn nhất, rủi ro pháp lý cao nhất |
| **User data & workflows** | Cao cho từng cá nhân (ảnh, code) | Cao *nếu* nhà vận hành xuất dữ liệu | Thấp phía nhà vận hành sắp chết (không tiền) | R11, R14, R17, R21 | Luật (GDPR Art 20) có, nhưng sau khi công ty biến mất thì vô hiệu [B-O2-C6, INFERENCE] |
| **Community continuity** | Cao — cộng đồng là nơi giá trị tái tạo | Trung bình (di cư sang Mastodon/Bluesky) | Phụ thuộc tình nguyện | R10, R14 | Khó bảo tồn; mất *mạng lưới quan hệ* khi di cư (**SUY LUẬN**) |
| **Cultural & historical heritage** | Cao nhưng khuếch tán | Trung bình | Phụ thuộc tài trợ/nhà nước | R3, R8, R9, R22 | Có ngân sách tổ chức nhưng nhỏ |
| **Operational continuity** (dịch vụ tiếp tục chạy) | Rất cao cho cộng đồng còn sống | Thấp — cần mã server/IP | Chỉ có khi IP holder cho phép (NCSoft: license không phí, có quyền buộc đóng) | R10, R2 | Ngoại lệ hiếm; EC chọn code of conduct tự nguyện |

**SUY LUẬN [B-G-C11]**: Chiều có *giá trị lớn nhất nhưng ít được phục vụ nhất* là **software functionality + operational continuity** cho phần mềm phụ thuộc server; chiều *khả thi nhất* là **content/knowledge**, nhưng ở đó đối thủ (IA, ArchiveTeam, CLOCKSS) mạnh nhất.

## 5. Existing solutions and gaps

| Phương án | Điểm mạnh | Giới hạn | Rào cản áp dụng | Vấn đề chưa giải | Nguồn |
|---|---|---|---|---|---|
| **Internet Archive / web archiving** | Quy mô lớn; chi phí thấp nhờ hạ tầng tự sở hữu; Wayback Machine | Thua kiện Hachette (2024) về controlled digital lending (snippet R25); thâm hụt 2023 (−9,0 triệu USD) và 2025 (−4,1 triệu USD) theo Form 990 | Trang động/SPA; backlog nhập liệu (Cohost: các file cuối đẩy lên 2025‑06‑15, R12) | Phần mềm có server không thể "crawl" | R12, R20, R25 |
| **ArchiveTeam (khẩn cấp)** | Phản ứng nhanh khi có thông báo đóng cửa | Phụ thuộc hợp tác của nhà vận hành (Cohost phải tắt batching, cung cấp danh sách user, R12); chỉ dữ liệu công khai | Tình nguyện, công cụ kỹ thuật cao | Dữ liệu riêng tư và chức năng không được lưu | R12, R13 |
| **Software preservation & emulation** (EaaSI, VGHF, DoJa SDK, SquirrelJME, Melange) | Chạy lại phần mềm gốc | Truy cập chỉ tại chỗ ở US (§1201); keitai: "no comprehensive emulator", mỗi nhà mạng một nền tảng (R8) | Pháp lý; phần cứng hiếm | Logic phía server không bao giờ có trong bản dump client | R4, R8, R22 |
| **Data portability** (GDPR Art 20, DTI/Data Transfer Project) | Có cơ sở pháp lý (EU); công cụ Apple/Google cho ảnh, playlist (R23) | Phục vụ di chuyển giữa *nền tảng lớn còn sống*; không bao phủ nền tảng nhỏ phá sản | Nhà vận hành sắp chết không có ngân sách | Chuyển *ngữ cảnh cộng đồng* (follow, thread) không được | R21, R23 |
| **Open-source alternatives / self-hosting** (Mastodon, Bluesky làm nơi di cư) | Tránh phụ thuộc một công ty | Không mang theo dữ liệu cũ; người dùng Cohost tự tìm nhau bằng hashtag (R14) | Kỹ năng, chi phí tự host | Mất đồ thị xã hội | R14 |
| **Decentralized storage** | Về lý thuyết tránh điểm chết đơn lẻ | **Không tìm được bằng chứng** về một nền tảng bị cứu nhờ lưu trữ phi tập trung trong phiên này; Cyworld 2026 do công ty blockchain mua lại nhưng vẫn chưa khôi phục được ảnh (R17) | — | **CHƯA RÕ** | R17 |
| **Community-led revival** (Homecoming, private servers) | Bằng chứng hành vi mạnh nhất; có tiền lệ license chính thức | License không phí nhưng NCSoft giữ quyền buộc đóng; không mở mã nguồn; không áp dụng cho server khác (R10) | Cần mã server rò rỉ hoặc tái dựng từ đầu; rủi ro pháp lý | Không nhân rộng được nếu không có IP holder hợp tác | R10 |
| **Digital heritage systems** (CLOCKSS, LOCKSS, Portico, PKP PN) | Chuẩn cho học thuật | <1% trong 204 publisher đưa phần lớn nội dung vào nhiều archive (snippet, từ tóm tắt Eve) | Publisher nhỏ không tham gia | ~28% DOI không thấy trong archive lớn (R7) | R5, R7 |
| **Quy định / code of conduct** | EC cam kết code of conduct "end of life" cho game (R2) | Không bắt buộc; EC nói IP cản nghĩa vụ pháp lý | Ngành phải tự nguyện | Tiêu chuẩn kỹ thuật "end-of-life" là gì — chưa có | R2 |

**Khoảng trống được khẳng định (đã nêu rõ đối thủ đã kiểm tra)**:
- **SUY LUẬN [B-G-C12]**: Không có phương án nào trong bảng trên giải quyết *chức năng phía server* của phần mềm đã ngừng (game live‑service, app động) — web archive chỉ lưu client/HTML, emulation chỉ chạy client, portability chỉ chuyển dữ liệu, community revival cần mã server hoặc tái dựng thủ công. Đối thủ đã kiểm tra: IA, ArchiveTeam, EaaSI, VGHF, DTI, Homecoming. Chưa kiểm tra: các dự án server emulator thương mại (ví dụ dịch vụ "end-of-life kit" của nhà cung cấp middleware) — **CHƯA RÕ** liệu đã tồn tại.

## 6. Sustainability

| Câu hỏi | Bằng chứng | Nhãn |
|---|---|---|
| Ai hưởng lợi? | Người chơi, nhà nghiên cứu, cộng đồng, công chúng (heritage) — khuếch tán | SUY LUẬN |
| Ai trả tiền? | Quỹ tư nhân (Mellon/Sloan → Yale EaaSI 3,5 triệu USD, R22); quyên góp người dùng (Homecoming, R10; IA); không ai trả cho nhà vận hành sắp chết (Cohost, R14) | ĐÃ XÁC MINH (theo nguồn) |
| Ai bảo trì? | Tình nguyện viên kỹ năng cao (Kahvibreak, ArchiveTeam); tổ chức phi lợi nhuận (IA, VGHF) | ĐÃ XÁC MINH (theo nguồn) |
| Chi phí liên tục | IA: chi 32,7 triệu USD (2023), 23,5 triệu (2024), 27,8 triệu (2025) theo Form 990 qua ProPublica (R20). Cohost: thâm hụt 17.000 USD/tháng chỉ để vận hành mạng xã hội 30k MAU (R14) | ĐÃ XÁC MINH (theo nguồn) |
| Thất bại | **Cyworld**: 5 lần đổi chủ; 2024 dừng vì "insufficient funding for data restoration" (R17) → khôi phục *dữ liệu* tốn kém hơn *lưu* dữ liệu. **Cohost**: mô hình thuê bao không đủ. **Mxit**: chuyển IP sang tổ chức công ích (Reach Trust, R19) nhưng dịch vụ vẫn đóng | ĐÃ XÁC MINH (theo nguồn) |

**Mô hình khả thi (SUY LUẬN [B-G-C13])**:
1. **Cộng đồng + license không phí từ IP holder** (Homecoming) — bền vững chỉ khi cộng đồng đủ lớn và IP holder đồng ý.
2. **Tổ chức tài trợ/phi lợi nhuận** (IA, VGHF, Yale) — bền nhưng IA có năm thâm hụt và rủi ro pháp lý.
3. **Nghĩa vụ phía nhà vận hành *trước* khi đóng cửa** (code of conduct EC; export + redirect như Glitch) — rẻ nhất vì làm khi hệ thống còn chạy; nhưng phụ thuộc tự nguyện.
4. **Thương mại**: GIẢ THUYẾT — nhà phát hành có thể trả cho "end-of-life compliance" nếu code of conduct EC trở thành áp lực thị trường. Chưa có bằng chứng chi tiêu.

**Không phải nền tảng nào cũng đáng sống**: >70% game gacha Nhật đóng trước năm thứ 3 (R24); bảo tồn tất cả vừa không khả thi vừa không có ai yêu cầu.

## 7. AI contribution

| Vị trí | AI làm gì | So với kỹ thuật truyền thống | Đo được? | Đánh giá |
|---|---|---|---|---|
| **Matching decompilation** (tái tạo mã C khớp byte với binary gốc) | LLM thử viết C cho hàm mà m2c + decomp-permuter không khớp | Pipeline LLM + công cụ khớp 74% trên 60 hàm từ 2 dự án decomp game thật; 88% hàm có kết quả giống nhau qua các lần chạy (R15). Baseline chỉ‑công‑cụ: **CHƯA RÕ** (bài nói có đo nhưng số liệu không có trong văn bản trích được, có thể nằm trong biểu đồ) | **Có oracle**: compiler + objdiff khớp byte → kiểm chứng tuyệt đối | **Load‑bearing tiềm năng** [B-O5-C1, SUY LUẬN — một tác giả, blog, n=60] |
| **Decompile thông thường** | LLM tạo mã dễ đọc | DecompileBench: LLM vượt decompiler thương mại về độ dễ hiểu nhưng **thấp hơn 52,2%** về tính đúng chức năng (R16) | Có benchmark | Phản chứng quan trọng: không có oracle thì LLM kém tin cậy [B-O5-C2] |
| **Mô tả metadata/tìm kiếm trong archive lớn** | Gắn nhãn, tóm tắt | Có thể thay bằng tìm kiếm toàn văn | Khó đo | Hữu ích, không thiết yếu — không có bằng chứng trong phiên này |
| **Tái dựng server game từ traffic** | Suy diễn giao thức | Reverse engineering thủ công (đã được khám phá ở chủ đề thiết bị cloud — không lặp lại) | Có oracle (client chạy được) | GIẢ THUYẾT |
| **Chatbot "hỏi archive"** | Hội thoại trên nội dung cũ | Tìm kiếm thường | Không có oracle | **Không cần thiết** — trang trí |

**Kết luận**: AI chỉ thực sự load‑bearing khi có **oracle kiểm chứng cơ học** (byte‑match, client chạy được). Ở các chiều content/knowledge, AI hầu như không cần thiết; vấn đề ở đó là tổ chức, pháp lý và chi phí, không phải trí tuệ.

## 8. Legal and ethical constraints

| Vấn đề | Khu vực | Nội dung | Nhãn / nguồn |
|---|---|---|---|
| Truy cập từ xa phần mềm/game đã bảo tồn | US | Copyright Office (10/2024) từ chối miễn trừ §1201 cho thư viện cung cấp truy cập game từ xa; ESA tuyên bố "would never support remote game access for research purposes under any conditions" | ĐÃ XÁC MINH theo VGHF (R4); xác nhận độc lập chỉ snippet (R29) |
| Cho mượn số hoá | US | Hachette v. Internet Archive (2d Cir., 4/9/2024): CDL của IA với 127 sách có ebook thương mại **không** là fair use | SUY LUẬN (snippet R25) |
| Nghĩa vụ giữ game chơi được | EU | EC: "cannot propose a legal obligation to keep video games playable… due, also, to existing intellectual property rights"; nhưng Directive 2019/770 (digital content) cho quyền hoàn tiền tương xứng; sẽ làm code of conduct | ĐÃ XÁC MINH (R2, văn bản EC) |
| Ngoại lệ bảo tồn di sản | EU | Điều 6 Directive (EU) 2019/790 cho phép tổ chức di sản văn hoá tạo bản sao để bảo tồn tác phẩm thuộc bộ sưu tập — **sao chép để bảo tồn ≠ quyền phân phối lại công khai** | SUY LUẬN (R27, không mở được văn bản gốc) |
| Chuyển dữ liệu cá nhân | EU | GDPR Art 20: quyền nhận dữ liệu ở định dạng máy đọc được và chuyển trực tiếp "where technically feasible" | ĐÃ XÁC MINH văn bản (R21) |
| License cộng đồng | Toàn cầu (US‑Korea) | NCSoft cấp license cho Homecoming nhưng giữ quyền buộc đóng; không mở mã; không áp dụng server khác | ĐÃ XÁC MINH theo MassivelyOP (R10); xác nhận độc lập snippet (PC Gamer, GameSpot) |
| Dump phần cứng & phá mã hoá | Nhật/US | Keitai: brute‑force khoá CPRM; ở US phá TPM là vấn đề §1201 ngay cả khi game không còn bán | SUY LUẬN [B-O4-C3] |
| Kiểm duyệt | Trung Quốc | Nội dung bị xoá có thể do chủ đích nhà nước; tái phân phối có thể vi phạm luật địa phương | SUY LUẬN (R9) |
| Quyền riêng tư & đồng ý | Mọi nơi | "Công khai" (public post Cohost) ≠ được phép phân phối lại; tin nhắn riêng (Mxit, Cyworld) không thể lưu trữ công khai | SUY LUẬN [B-G-C14] |

**Phân biệt quan trọng**: *Công khai truy cập được* (Cohost post, i-mode store page) ≠ *được phép sao chép/phân phối lại*. Ngoại lệ bảo tồn (EU Art 6, US §108/§1201 on‑premises) cho phép **giữ** nhưng thường **không** cho phép **chia sẻ rộng**. Đây là nút thắt pháp lý của chiều software và heritage.

## 9. International evidence

| Khu vực | Trường hợp cụ thể | Bằng chứng |
|---|---|---|
| **Bắc Mỹ** | City of Heroes (NCSoft/US studio, đóng 2012 → Homecoming 2024); Glitch (US, 2025); Cohost (US, 2024); VGHF 87% game US trước 2010 không còn bán; Pew: 38% trang web 2013 không còn (2023) | R3, R10, R11, R14, R18 |
| **Châu Âu** | ECI "Stop Destroying Videogames": 1,29 triệu chữ ký hợp lệ, đạt ngưỡng ở 24 quốc gia thành viên; phản hồi EC 16/6/2026 | R1, R2 |
| **Châu Á** | Nhật: keitai i-mode/EZweb/SoftBank — "thousands of keitai games" bị xoá khi dịch vụ đóng (R8); >70% trong ~2.200 game live‑service Nhật ngừng trước năm 3 (R24). Hàn Quốc: Cyworld — dữ liệu ảnh vẫn chưa khôi phục sau nhiều đời chủ (R17). Trung Quốc: He Jiayan — internet tiếng Trung thời kỳ đầu gần như biến mất (theo tìm kiếm của tác giả, không phải đo lường hệ thống; R9) | R8, R9, R17, R24 |
| **Khác (châu Phi)** | Mxit (Nam Phi): giảm còn 1,2 triệu người dùng (7/2015), chuyển IP cho Reach Trust (R19) | R19 |
| **Toàn cầu (học thuật)** | 174 tạp chí OA biến mất 2000–2019 "spanning all major research disciplines and geographic regions" (R5) | R5, R7 |

**Không tìm được bằng chứng**: Việt Nam — truy vấn "Zing Me shutdown Vietnam social network closes users data 2024" không xác nhận Zing Me đã đóng hay cách xử lý dữ liệu. Mỹ Latinh — truy vấn Orkut Brazil không trả kết quả liên quan. Phi tập trung — không tìm được trường hợp cứu nền tảng nhờ lưu trữ phi tập trung.

**Rào cản liên văn hoá (SUY LUẬN [B-G-C15])**: (1) Ngôn ngữ — keitai và Cyworld chủ yếu tài liệu tiếng Nhật/Hàn; cộng đồng bảo tồn nhỏ và tập trung trên Discord. (2) Pháp lý khác nhau — EU có code of conduct tiềm năng; US bị §1201 cản; Trung Quốc có kiểm duyệt. (3) Hiện tượng *gốc* (server dependency, nền tảng sắp chết không có ngân sách đóng cửa) là **xuyên văn hoá**: đã thấy ở 4 khu vực.

## 10. Opportunity spaces

> Đây là *không gian vấn đề*, không phải sản phẩm. Điểm rubric tạm thời ở `opportunities.json` là tóm tắt bằng chứng theo anchors Phase 2.

### B-O1 — Hậu kỳ (end-of-life) của phần mềm phụ thuộc server: game live‑service

- **Vấn đề**: Khi nhà phát hành tắt server, game đã mua trở nên không chơi được; cộng đồng mất nơi gặp gỡ. EC xác nhận cơ chế này và từ chối nghĩa vụ pháp lý, chuyển sang code of conduct tự nguyện (R2).
- **Người dùng mục tiêu**: Người chơi đã mua game; cộng đồng hồi sinh (Homecoming); nhà phát hành cần tuân thủ code of conduct EC; thư viện game (VGHF).
- **Chiều**: software, operational, community, heritage.
- **Vì sao bây giờ**: EC cam kết khởi động trao đổi với ngành về code of conduct "end of life" và báo cáo về Directive digital content **trước cuối 2026** (R2) — có cửa sổ định nghĩa "end-of-life tốt" trông như thế nào.
- **Phương án thay thế mạnh nhất**: Server emulator do cộng đồng tự làm (Homecoming) + bản vá offline do nhà phát hành tự nguyện.
- **Phản chứng mạnh nhất**: EC nói rõ IP cản nghĩa vụ; ESA phản đối mọi truy cập từ xa (R4); license Homecoming là "near unprecedented" — không nhân rộng.
- **Claims**: B-O1-C1 (1,29 triệu chữ ký hợp lệ, 24 quốc gia — ĐÃ XÁC MINH: R1 + R2 cùng nguồn EC, chính thức; snippet độc lập heise R28), B-O1-C2 (EC thừa nhận game phụ thuộc server — ĐÃ XÁC MINH theo R2), B-O1-C3 (EC từ chối nghĩa vụ, chọn code of conduct — ĐÃ XÁC MINH theo R2), B-O1-C4 (Homecoming tự tài trợ, license không phí, NCSoft giữ quyền đóng — ĐÃ XÁC MINH theo R10; độc lập snippet), B-O1-C5 (>70% game live‑service Nhật dừng trước năm 3 — SUY LUẬN: một nhà nghiên cứu độc lập qua AUTOMATON, R24), B-O1-C6 (tồn tại khoảng trống về "chuẩn kỹ thuật end-of-life" — GIẢ THUYẾT).
- **Bằng chứng theo rubric**: demand 4 (hành vi công dân quy mô triệu + cộng đồng trả tiền; chưa có bằng chứng người dùng muốn *giải pháp mới*); international 4 (EU, NA, Asia trực tiếp, nhưng rào cản pháp lý lớn); innovation 3 (khoảng trống hợp lý, đối thủ cộng đồng phủ một phần); theme 4 (game cụ thể đã chết làm neo); ai 2; feasibility 3; demo 4; sustainability 3.
- **Giả thuyết then chốt**: H1 — Một phần đáng kể game đóng cửa có thể chạy lại ở chế độ offline/tự host nếu nhà phát hành phát hành artefact tối thiểu (binary server hoặc spec giao thức). H2 — Nhà phát hành sẽ chấp nhận một chuẩn "end-of-life" tự nguyện nếu chi phí thấp.
- **Thí nghiệm nhỏ nhất có thể bác bỏ**: Lấy 20 game live‑service đóng 2024–2026 (EU/NA/JP); đếm bao nhiêu đã có (a) bản offline chính thức, (b) server cộng đồng hoạt động. Nếu ≥ 50% đã có lối thoát → khoảng trống nhỏ. Nếu < 10% có cộng đồng hồi sinh dù có cộng đồng lớn → rào cản là pháp lý, không phải kỹ thuật → không gian không giải được bằng công cụ.

### B-O2 — "Cửa sổ đóng cửa" của nền tảng cộng đồng nhỏ/vừa

- **Vấn đề**: Nền tảng nhỏ chết vì hết tiền; chính việc *đóng cửa có trách nhiệm* (export, redirect, cho archivist truy cập) cũng tốn tiền và thời gian kỹ sư mà họ không còn. Cohost: nhân viên không lương; ArchiveTeam cần Cohost tắt TRPC batching và cung cấp danh sách user (R12, R14). Glitch: export đến cuối 2025, redirect đến cuối 2026 (R11).
- **Người dùng mục tiêu**: Nhà vận hành nền tảng nhỏ đang đóng cửa; người dùng của họ; ArchiveTeam.
- **Chiều**: user-data-workflows, community, content.
- **Vì sao bây giờ**: Làn sóng nền tảng "thay thế X" thất bại (Cohost, T2, Post — R14); chi phí hosting và lạm dụng tăng (R11).
- **Phương án thay thế mạnh nhất**: ArchiveTeam + Internet Archive (nội dung công khai) + export tự xây của nhà vận hành + GDPR Art 20.
- **Phản chứng mạnh nhất**: Cohost và Glitch *đã* tự làm export và redirect; ArchiveTeam *đã* lưu Cohost. Khoảng trống có thể chỉ là "làm sớm hơn", không phải công cụ mới. Cyworld cho thấy khôi phục sau khi chết tốn kém đến mức 2 lần thất bại (R17).
- **Claims**: B-O2-C1 (Cohost 30k MAU, 2.630 subscriber, thâm hụt 17k USD — ĐÃ XÁC MINH theo TechCrunch R14 trích bài staff), B-O2-C2 (Glitch đóng hosting 8/7/2025 vì chi phí + lạm dụng — ĐÃ XÁC MINH: R11 gốc + R13 ArchiveTeam độc lập), B-O2-C3 (ArchiveTeam phụ thuộc hợp tác của nhà vận hành — ĐÃ XÁC MINH theo R12), B-O2-C4 (Cyworld 2021 ~4 triệu truy cập trong 11 giờ — SUY LUẬN, snippet R26), B-O2-C5 (Cyworld dừng 2024 vì thiếu tiền khôi phục dữ liệu, 5 đời chủ — ĐÃ XÁC MINH theo R17), B-O2-C6 (GDPR Art 20 không hiệu lực thực tế khi controller đã giải thể — SUY LUẬN).
- **Bằng chứng theo rubric**: demand 3; international 3 (NA, Asia/Korea, Africa); innovation 2; theme 3; ai 1; feasibility 4; demo 3; sustainability 2.
- **Giả thuyết**: H3 — Phần lớn mất mát xảy ra vì nhà vận hành nhỏ không biết/không có công cụ đóng cửa chuẩn, không phải vì không muốn.
- **Thí nghiệm bác bỏ**: Đọc trang ArchiveTeam "Deathwatch" và 20 thông báo đóng cửa 2024–2026; đếm tỷ lệ có export + redirect + thời gian báo trước ≥ 90 ngày. Nếu ≥ 70% đã có → giả thuyết sai.

### B-O3 — Hồ sơ tri thức học thuật không được lưu trữ (tạp chí nhỏ, OA)

- **Vấn đề**: ~28% bài báo có DOI không có trong archive lớn (Eve, 7,4 triệu DOI, R7); 174 tạp chí OA biến mất 2000–2019 (R5).
- **Người dùng mục tiêu**: Biên tập viên tạp chí nhỏ, thư viện đại học, nhà nghiên cứu trích dẫn.
- **Chiều**: knowledge, content, heritage.
- **Phương án thay thế mạnh nhất**: CLOCKSS / LOCKSS / Portico / PKP Preservation Network / Internet Archive Scholar (tôi **không** mở trang chính thức của các dịch vụ này trong phiên — hạn chế).
- **Phản chứng mạnh nhất**: Shelomi (R31, snippet): một phần tạp chí biến mất là predatory; Laakso et al. tự ghi nhận một số tạp chí thực ra vẫn online. Hạ tầng chuyên ngành đã tồn tại — vấn đề là tham gia, không phải công nghệ.
- **Claims**: B-O3-C1 (~28% DOI không thấy trong archive lớn — ĐÃ XÁC MINH theo R7 do chính tác giả viết; bài JLSC gốc bị chặn), B-O3-C2 (174 tạp chí OA biến mất — ĐÃ XÁC MINH theo R5; phiên bản sau báo 192, snippet), B-O3-C3 (không có đồng thuận ai chịu trách nhiệm lưu trữ — ĐÃ XÁC MINH theo R7).
- **Bằng chứng theo rubric**: demand 3; international 4; innovation 1; theme 1 (không có công nghệ cụ thể đã chết); ai 1; feasibility 3; demo 2; sustainability 3.
- **Nhận định**: Vấn đề thật và toàn cầu nhưng **trượt cổng theme** (≤ 2) và đối thủ chuyên ngành mạnh. Ghi lại để không bỏ sót, không khuyến nghị theo đuổi trong Kiroween.
- **Thí nghiệm bác bỏ**: Kiểm tra 50 DOI ngẫu nhiên "không được lưu" trong dataset Eve: bao nhiêu vẫn truy cập được và có trong IA Scholar? Nếu ≥ 80% truy cập được → mức độ cấp bách bị thổi phồng.

### B-O4 — Di sản của nền tảng khu vực đã chết (keitai Nhật, web Trung Quốc thời kỳ đầu, Mxit)

- **Vấn đề**: Nền tảng riêng theo quốc gia/nhà mạng tạo ra văn hoá số lớn (Hamatani: >80% người dùng keitai 2005–2006 dùng tính năng game — snippet), nay bị kẹt trên phần cứng lão hoá hoặc bị xoá.
- **Người dùng mục tiêu**: Cộng đồng bảo tồn (Kahvibreak, Keitai Wiki), nhà nghiên cứu lịch sử game/văn hoá số, thư viện di sản Nhật (Game Preservation Society — snippet).
- **Chiều**: heritage, software, content.
- **Vì sao bây giờ**: Phần cứng đang chết; số máy DoCoMo dump được tăng từ 2 (2022) lên >50 (2023) nhờ phương pháp debug cable (R8) — cửa sổ kỹ thuật mở ra.
- **Phương án thay thế mạnh nhất**: Kahvibreak + Keitai Wiki + DoJa 5.1 SDK emulator + SquirrelJME + Melange (BREW); G‑MODE Archives (tái phát hành thương mại).
- **Phản chứng mạnh nhất**: Cộng đồng tự làm hiệu quả; nút thắt là **phần cứng và khoá mã hoá**, không phải phần mềm; pháp lý chặn phân phối; khán giả quốc tế ngoài Nhật hạn chế.
- **Claims**: B-O4-C1 (3 nền tảng không tương thích DoJa/BREW/MIDP; không có emulator toàn diện — ĐÃ XÁC MINH theo R8; độc lập snippet Time Extension), B-O4-C2 (công sức tình nguyện cực lớn: brute-force 20 ngày GPU, desolder — ĐÃ XÁC MINH theo R8), B-O4-C3 (phá mã hoá là rủi ro pháp lý — SUY LUẬN), B-O4-C4 (internet tiếng Trung thời kỳ đầu phần lớn biến mất — SUY LUẬN: dựa trên tìm kiếm cá nhân của tác giả, R9), B-O4-C5 (Mxit chuyển IP cho Reach Trust nhưng dịch vụ vẫn đóng — ĐÃ XÁC MINH theo R19).
- **Bằng chứng theo rubric**: demand 3; international 3 (Asia mạnh, Africa, cơ chế tổng quát); innovation 2; theme 5 (i-mode là công nghệ đã chết rõ ràng); ai 3; feasibility 2; demo 4; sustainability 1.
- **Thí nghiệm bác bỏ**: Liệt kê top 100 game keitai theo Keitai Wiki; nếu ≥ 70% đã được dump và chạy được trên emulator hiện có → không còn khoảng trống phần mềm.

### B-O5 — Tái dựng mã nguồn của phần mềm bị bỏ rơi bằng AI có oracle kiểm chứng

- **Vấn đề**: Khi chỉ còn binary (game cổ, ứng dụng không còn hãng hỗ trợ), muốn port/bảo trì cần mã nguồn. Matching decompilation (mã C biên dịch ra đúng byte gốc) là kỹ thuật cộng đồng decomp dùng, nhưng tốn nhiều năm công.
- **Người dùng mục tiêu**: Cộng đồng decomp (GBA/N64), lập trình viên bảo tồn, có thể thư viện phần mềm.
- **Chiều**: software, heritage.
- **Vì sao bây giờ**: Pipeline LLM + công cụ cổ điển khớp 74% hàm benchmark (R15, 3/2026); benchmark học thuật mới (DecompileBench, ACL Findings 2025, R16).
- **Phương án thay thế mạnh nhất**: m2c + decomp-permuter + objdiff (công cụ cộng đồng), Ghidra/IDA; các dự án LLM‑decompile học thuật.
- **Phản chứng mạnh nhất**: DecompileBench: LLM kém 52,2% về tính đúng chức năng khi không có oracle (R16); kết quả 74% đến từ **một** tác giả, n=60, blog; baseline chỉ‑công‑cụ chưa rõ; mã decomp từ binary có bản quyền vẫn là tác phẩm phái sinh — phân phối có rủi ro.
- **Claims**: B-O5-C1 (74% match / 88% xác định — ĐÃ XÁC MINH là *điều nguồn báo cáo* (R15); về thực tế: SUY LUẬN, chưa có xác nhận độc lập), B-O5-C2 (DecompileBench −52,2% functionality — ĐÃ XÁC MINH theo R16), B-O5-C3 (AI giảm đáng kể thời gian decomp toàn dự án — GIẢ THUYẾT), B-O5-C4 (byte-match là oracle đủ cho kiểm chứng — SUY LUẬN, cơ chế rõ ràng nhưng không đảm bảo mã dễ đọc).
- **Bằng chứng theo rubric**: demand 2 (cộng đồng decomp có tồn tại; chưa đo); international 2; innovation 3; theme 3; ai 5 (load‑bearing với oracle đo được); feasibility 3; demo 3; sustainability 2.
- **Thí nghiệm bác bỏ**: Chạy lại benchmark công khai (nếu có mã Mizuchi/Kappa) trên 30 hàm của một dự án decomp *khác*; nếu tỷ lệ khớp thêm do LLM (so với chỉ công cụ) < 15 điểm phần trăm → AI không load‑bearing.

## 11. Challenges to the mission hypothesis

1. **"Giá trị của nền tảng" là quá rộng** (SUY LUẬN [B-G-C16]): Mission gộp 7 chiều có kinh tế học khác nhau hoàn toàn. Content/knowledge đã có hạ tầng tổ chức (IA, CLOCKSS) — vấn đề là tài trợ và tham gia. Software/operational bị chặn chủ yếu bởi **IP**, không phải kỹ thuật. Câu hỏi "có thể bảo tồn không?" có câu trả lời kỹ thuật là "thường có", nhưng câu hỏi thật là "**ai được phép** và **ai trả tiền**".
2. **Suy giảm người dùng không phải nguyên nhân chính** (§2.2): Glitch đóng khi còn hàng triệu người dùng; City of Heroes đóng khi cộng đồng còn sẵn sàng trả tiền. Tập trung vào "nền tảng suy giảm" bỏ sót trường hợp quan trọng nhất: **giá trị còn sống nhưng mô hình kinh doanh không**.
3. **Bảo tồn sau khi chết đắt hơn nhiều so với chuẩn bị trước khi chết** (SUY LUẬN [B-G-C17]): Cyworld (khôi phục thất bại vì chi phí), Cohost (ArchiveTeam cần nhà vận hành sửa API), keitai (brute-force khoá). Ngược lại, EC chọn đúng điểm đòn bẩy là *thời điểm trước khi đóng cửa*. Mission nên tách "resurrection sau khi chết" khỏi "end-of-life có kế hoạch".
4. **Không phải mọi nền tảng đều đáng sống** — >70% game live‑service Nhật đóng trong 3 năm; nhu cầu bảo tồn tập trung ở số ít nền tảng có cộng đồng mạnh.
5. **Nhu cầu trả tiền chưa được chứng minh**: mọi hành vi "demonstrated" tìm thấy là chữ ký, quyên góp, giờ tình nguyện — **không** phải mua công cụ. Điều này ảnh hưởng tiêu chí sustainability.
6. **Rủi ro chồng lấn với khung "Resurrection"**: không gian có theme fit cao nhất (keitai, game live‑service) cũng có rủi ro pháp lý cao nhất.

## 12. Unresolved questions

1. Baseline chỉ‑công‑cụ trong benchmark decomp của R15 là bao nhiêu? (CHƯA RÕ)
2. Nội dung chi tiết code of conduct "end of life" EC — đã khởi động chưa, ai tham gia? (CHƯA RÕ; R2 chỉ là cam kết)
3. Tỷ lệ game live‑service đóng cửa có lối thoát offline/cộng đồng? (CHƯA RÕ — xem thí nghiệm B-O1)
4. Có nhà cung cấp thương mại nào bán dịch vụ "end-of-life / sunsetting" cho game hoặc SaaS? (CHƯA RÕ — chưa tìm)
5. Văn bản chính xác Điều 6 Directive 2019/790 và luật tương đương ở Nhật/Hàn (CHƯA RÕ — EUR‑Lex bị chặn)
6. Tình trạng Zing Me / Yahoo 360 Plus ở Việt Nam và dữ liệu người dùng (CHƯA RÕ)
7. Phiên bản cuối của Laakso et al. (174 vs 192 tạp chí) và mức độ predatory (CHƯA RÕ)
8. Có bằng chứng người dùng cá nhân trả tiền để giữ dữ liệu từ nền tảng đang chết? (CHƯA RÕ)

## 13. References

Thang điểm 0–5 cho: Auth (Source Authority 20%), Tech (Technical Evidence 20%), Mech (Mechanism Correctness 20%), Ctx (Context Fit 15%), Fresh (Freshness 10%), Repro (Reproducibility 10%), Bias (Commercial/Opinion Bias 5%, 5 = ít thiên lệch). Weighted = Σ(weight × score/5) × 100. **Source Reliability** (độ tin cậy của nguồn, H/M/L) tách khỏi **Reference Relevance** (mức liên quan tới claim, H/M/L). Ngày truy cập: 2026-11-25 cho tất cả.

| Ref | URL | Title | Publisher | Pub date | Accessed | Opened / snippet | Claims | Auth | Tech | Mech | Ctx | Fresh | Repro | Bias | Weighted | Src Rel | Ref Rel |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R1 | https://citizens-initiative.europa.eu/news/european-commission-replies-stop-destroying-videogames-initiative-2026-06-16_en | European Commission replies to 'Stop Destroying Videogames' initiative | European Commission, Secretariat-General | 2026-06-16 | 2026-11-25 | Opened | B-O1-C1 | 5 | 3 | 4 | 5 | 5 | 4 | 5 | 86 | H | H |
| R2 | https://ec.europa.eu/commission/presscorner/detail/en/ip_26_1369 (nội dung lấy qua API presscorner) | Commission will engage with industry following European Citizens' Initiative on the disabling of videogames by publishers | European Commission | 2026-06-16 | 2026-11-25 | Opened (API) | B-O1-C1..C3, B-G-C8 bối cảnh EU | 5 | 3 | 5 | 5 | 5 | 4 | 4 | 89 | H | H |
| R3 | https://gamehistory.org/87percent/ | 87% Missing: the Disappearance of Classic Video Games | Video Game History Foundation | 2023-07-10 | 2026-11-25 | Opened | B-G-C9, §9 | 4 | 4 | 4 | 4 | 3 | 4 | 3 | 77 | H | M |
| R4 | https://gamehistory.org/dmca-2024-statement/ | Statement on the DMCA 2024 triennial review ruling | Video Game History Foundation | 2024-10 | 2026-11-25 | Opened | B-G-C8 | 4 | 3 | 4 | 4 | 4 | 3 | 2 | 72 | M | H |
| R5 | https://arxiv.org/abs/2008.11933 | Open is not forever: a study of vanished open access journals | arXiv (Laakso, Matthias, Jahn; JASIST 2021) | 2020 (v1) | 2026-11-25 | Opened (abstract) | B-O3-C2 | 5 | 4 | 4 | 3 | 2 | 5 | 5 | 80 | H | M |
| R6 | https://iastatedigitalpress.com/jlsc/article/id/16288 | Digital Scholarly Journals Are Poorly Preserved: A Study of 7 Million Articles | JLSC (Eve) | 2024-01 | 2026-11-25 | **Failed** (Anubis) — không dùng làm bằng chứng | — | — | — | — | — | — | — | — | — | — | — |
| R7 | https://blogs.lse.ac.uk/impactofsocialsciences/2024/02/13/the-digital-scholarly-record-is-at-risk/ | The digital scholarly record is at risk | LSE Impact Blog (Eve) | 2024-02-13 | 2026-11-25 | Opened | B-O3-C1, C3 | 4 | 4 | 4 | 3 | 4 | 3 | 4 | 75 | H | M |
| R8 | https://hitsave.org/the-state-of-japanese-feature-phone-preservation-in-2023/ | The State of Japanese Feature Phone Preservation in 2023 | Hit Save | ~2024-01 | 2026-11-25 | Opened | B-O4-C1, C2; §2 | 3 | 5 | 4 | 4 | 3 | 4 | 4 | 78 | M | H |
| R9 | https://chinadigitaltimes.net/2024/06/translation-he-jiayan-on-the-accelerating-collapse-of-the-chinese-internet/ | Translation: He Jiayan on the "Accelerating Collapse" of the Chinese Internet | China Digital Times | 2024-06 | 2026-11-25 | Opened | B-O4-C4 | 3 | 2 | 2 | 3 | 4 | 3 | 3 | 54 | M | M |
| R10 | https://massivelyop.com/2024/01/04/ncsoft-has-officially-granted-a-city-of-heroes-server-license-to-the-homecoming-crew/ | NCsoft has officially granted a City of Heroes server license to the Homecoming crew | Massively Overpowered | 2024-01-04 | 2026-11-25 | Opened | B-O1-C4; §3, §6, §8 | 3 | 3 | 4 | 5 | 4 | 3 | 4 | 73 | M | H |
| R11 | https://blog.glitch.com/post/changes-are-coming-to-glitch/ | Important Changes are Coming to Glitch | Glitch (Fastly) | 2025-05-22 | 2026-11-25 | Opened | B-O2-C2; B-G-C3 | 5 | 3 | 4 | 4 | 4 | 4 | 3 | 79 | H | H |
| R12 | https://wiki.archiveteam.org/index.php/Cohost | Cohost | ArchiveTeam Wiki | 2025 | 2026-11-25 | Opened | B-O2-C3 | 3 | 5 | 5 | 5 | 4 | 4 | 5 | 88 | M | H |
| R13 | https://wiki.archiveteam.org/index.php/Glitch | Glitch | ArchiveTeam Wiki | 2025 | 2026-11-25 | Opened | B-O2-C2 (xác nhận độc lập) | 3 | 4 | 4 | 4 | 4 | 4 | 5 | 77 | M | M |
| R14 | https://techcrunch.com/2024/09/12/cohost-the-x-rival-founded-with-an-anti-big-tech-manifesto-is-running-out-of-money-and-will-shut-down/ | Cohost… is running out of money and will shut down | TechCrunch | 2024-09-12 | 2026-11-25 | Opened | B-O2-C1; B-G-C4 | 4 | 3 | 4 | 5 | 4 | 3 | 4 | 77 | H | H |
| R15 | https://gambiconf.substack.com/p/can-llms-really-do-matching-decompilation | Can LLMs Really Do Matching Decompilation? I Tested 60 Functions to Find Out | Substack (Macabeus) | 2026-03-10 | 2026-11-25 | Opened | B-O5-C1 | 2 | 4 | 4 | 4 | 5 | 4 | 3 | 73 | L | H |
| R16 | https://arxiv.org/abs/2505.11340 | DecompileBench: A Comprehensive Benchmark for Evaluating Decompilers in Real-World Scenarios | arXiv / ACL Findings 2025 | 2025-05 | 2026-11-25 | Opened (abstract) | B-O5-C2 | 5 | 5 | 4 | 3 | 4 | 5 | 5 | 88 | H | M |
| R17 | https://view.asiae.co.kr/en/article/2026081210023586075 | 'Photo Album Recovery Raises Hopes Again: Is This Cyworld's Real Comeback?' | Asia Economy | 2026-08-12 | 2026-11-25 | Opened | B-O2-C5; §6 | 3 | 2 | 3 | 4 | 5 | 2 | 4 | 62 | M | H |
| R18 | https://www.pewresearch.org/data-labs/2024/05/17/when-online-content-disappears/ | When Online Content Disappears | Pew Research Center | 2024-05-17 | 2026-11-25 | Opened | §9 bối cảnh | 5 | 5 | 4 | 2 | 4 | 5 | 5 | 85 | H | L |
| R19 | https://qz.com/africa/531667/south-africas-social-network-loses-out-to-whatsapp-and-shuts-down | South Africa's pioneering social network loses out to Whatsapp and shuts down | Quartz | 2015-10 | 2026-11-25 | Opened | B-O4-C5; B-G-C6 | 3 | 2 | 3 | 3 | 1 | 2 | 4 | 51 | M | M |
| R20 | https://projects.propublica.org/nonprofits/organizations/943242767 | Internet Archive — Nonprofit Explorer (Form 990 data) | ProPublica | cập nhật 2026 | 2026-11-25 | Opened | §5, §6 | 5 | 4 | 4 | 3 | 5 | 5 | 5 | 86 | H | M |
| R21 | https://gdpr-info.eu/art-20-gdpr/ | Art. 20 GDPR — Right to data portability | gdpr-info.eu (văn bản Regulation (EU) 2016/679) | 2016 | 2026-11-25 | Opened | B-O2-C6; §8 | 4 | 3 | 5 | 4 | 3 | 5 | 4 | 80 | M | M |
| R22 | https://web.library.yale.edu/news/2021/06/library-sandbox-lets-researchers-test-critical-software | Library sandbox lets researchers test critical software | Yale University Library | 2021-06 | 2026-11-25 | Opened | B-G-C9 | 4 | 3 | 3 | 3 | 2 | 3 | 4 | 63 | H | M |
| R23 | https://dtinit.org/blog/2025/01/28/year-3-growth | Year 3 for DTI brings growth | Data Transfer Initiative | 2025-01-28 | 2026-11-25 | Opened | §5 | 4 | 2 | 3 | 3 | 4 | 2 | 2 | 59 | M | M |
| R24 | https://automaton-media.com/en/news/more-than-70-of-gacha-and-live-service-games-in-japan-get-discontinued-before-their-third-year-gacha-game-researcher-finds/ | More than 70% of gacha and live-service games in Japan get discontinued before their third year | AUTOMATON West | 2025-11-18 | 2026-11-25 | Opened | B-O1-C5; B-G-C5 | 3 | 4 | 3 | 4 | 4 | 3 | 4 | 70 | M | H |
| R25 | https://www.govinfo.gov/content/pkg/USCOURTS-ca2-23-01260/pdf/USCOURTS-ca2-23-01260-0.pdf | Hachette Book Group v. Internet Archive (2d Cir.) | US Court of Appeals 2d Cir. | 2024-09-04 | 2026-11-25 | **Snippet only** | §8 | 5 | 2 | 3 | 3 | 4 | 3 | 5 | 68 | H | M |
| R26 | https://www.asiae.co.kr/en/article/2021080407590600922 | Cyworld 'Memory Search' Draws Crowd... 4 Million Users Access in 11 Hours | Asia Economy | 2021-08-04 | 2026-11-25 | **Snippet only** (fetch timeout) | B-O2-C4 | 3 | 2 | 2 | 4 | 2 | 1 | 3 | 49 | M | H |
| R27 | https://eur-lex.europa.eu/eli/dir/2019/790/oj/eng | Directive (EU) 2019/790 (DSM), Art. 6 | EUR-Lex | 2019 | 2026-11-25 | **Snippet / không mở được** (HTTP 202 challenge) | §8 | 5 | 2 | 3 | 4 | 3 | 3 | 5 | 69 | H | M |
| R28 | https://heise.de/-11154579 | Citizens' initiative: 1,294,188 signatures for "Stop Destroying Videogames" | heise online | 2026 | 2026-11-25 | **Snippet only** | B-O1-C1 (xác nhận độc lập) | 4 | 2 | 3 | 5 | 5 | 2 | 4 | 69 | H | H |
| R29 | https://www.copyright.gov/1201/2024/hearing-transcripts/240418-Section-1201-Public-Hearing-Class6a-6b.pdf | Section 1201 Public Hearing Class 6(a)/6(b) transcript | US Copyright Office | 2024-04-18 | 2026-11-25 | **Snippet only** | B-G-C8 (xác nhận) | 5 | 2 | 3 | 4 | 4 | 3 | 5 | 71 | H | M |
| R30 | https://www.asiae.co.kr/en/article/2025031613150559032 | Restoration Was Announced for the Second Half of This Year, But the Project Has Been Halted | Asia Economy | 2025-03-16 | 2026-11-25 | **Snippet only** (fetch timeout) | B-O2-C5 (xác nhận một phần) | 3 | 2 | 3 | 4 | 4 | 1 | 4 | 58 | M | M |
| R31 | https://arxiv.org/abs/2009.07561 | Comment on "Open is not forever: a study of vanished open access journals" (Shelomi) | arXiv | 2020 | 2026-11-25 | **Snippet only** | §2.4, B-O3 phản chứng | 3 | 2 | 3 | 3 | 2 | 2 | 3 | 52 | M | M |

### Danh mục claim chung (B-G)

| ID | Khẳng định (tóm tắt) | Nhãn | Ref |
|---|---|---|---|
| B-G-C1 | Suy giảm người dùng thường là triệu chứng; nguyên nhân trực tiếp là chi phí/quyết định danh mục | SUY LUẬN | R11, R14, R19, R24 |
| B-G-C2 | Đóng cửa xảy ra dù cộng đồng còn hoạt động (City of Heroes) | SUY LUẬN | R10 |
| B-G-C3 | Glitch: chi phí chạy hàng triệu app + lạm dụng tăng theo tuổi nền tảng | ĐÃ XÁC MINH | R11, R13 |
| B-G-C4 | Cohost thâm hụt, 30k MAU | ĐÃ XÁC MINH (theo nguồn) | R14 |
| B-G-C5 | >70% game live‑service Nhật ngừng trước năm 3 | SUY LUẬN | R24 |
| B-G-C6 | Mxit còn 1,2 triệu người dùng 7/2015 do WhatsApp/Facebook | SUY LUẬN (snippet cho con số; Quartz mở được nhưng con số đến từ snippet) | R19 |
| B-G-C7 | Các trường hợp bảo tồn không chính đáng | SUY LUẬN | R24, R31 |
| B-G-C8 | US Copyright Office từ chối miễn trừ truy cập từ xa cho game (2024) | ĐÃ XÁC MINH (theo nguồn VGHF; xác nhận độc lập snippet) | R4, R29 |
| B-G-C9 | Có ngân sách tổ chức cho software preservation (Yale 3,5 triệu USD; VGHF nghiên cứu) | ĐÃ XÁC MINH (theo nguồn) | R3, R22 |
| B-G-C10 | Cá nhân sẵn sàng trả tiền cho công cụ bảo tồn mới | CHƯA RÕ | — |
| B-G-C11 | Software+operational có giá trị cao nhất, ít được phục vụ nhất | SUY LUẬN | tổng hợp |
| B-G-C12 | Không phương án hiện có nào bảo tồn chức năng phía server | SUY LUẬN | R2, R8, R10, R12, R22, R23 |
| B-G-C13 | Các mô hình bền vững khả thi | SUY LUẬN | R2, R10, R20, R22 |
| B-G-C14 | Công khai ≠ được phép phân phối lại; dữ liệu riêng tư không thể lưu trữ công khai | SUY LUẬN | R21, R27 |
| B-G-C15 | Hiện tượng gốc là xuyên văn hoá, rào cản ngôn ngữ/pháp lý khác nhau | SUY LUẬN | §9 |
| B-G-C16 | "Giá trị nền tảng" quá rộng; nút thắt thật là IP + tài trợ | SUY LUẬN | tổng hợp |
| B-G-C17 | Bảo tồn sau khi chết đắt hơn chuẩn bị trước khi chết | SUY LUẬN | R2, R12, R17, R8 |

### Đếm claim theo nhãn

| Nhãn | B-G | B-O1 | B-O2 | B-O3 | B-O4 | B-O5 | Tổng |
|---|---|---|---|---|---|---|---|
| ĐÃ XÁC MINH | 4 (C3, C4, C8, C9) | 4 (C1–C4) | 4 (C1, C2, C3, C5) | 3 (C1–C3) | 3 (C1, C2, C5) | 2 (C1 — chỉ "nguồn báo cáo", C2) | **20** |
| SUY LUẬN | 12 | 1 (C5) | 2 (C4, C6) | 0 | 2 (C3, C4) | 1 (C4) | **18** |
| GIẢ THUYẾT | 0 | 1 (C6) | 0 | 0 | 0 | 1 (C3) | **2** |
| CHƯA RÕ | 1 (C10) | 0 | 0 | 0 | 0 | 0 | **1** |
| **Tổng** | 17 | 6 | 6 | 3 | 5 | 4 | **41** |

Ghi chú về VERIFIED: 15/20 claim ĐÃ XÁC MINH thuộc loại (a) "nguồn X báo cáo Y" — tức đã mở trực tiếp nguồn gốc nhưng **chưa** có xác nhận độc lập mở trực tiếp. Chỉ B-O2-C2/B-G-C3 (Glitch: R11 + R13) và B-O1-C1..C3 (hai tài liệu chính thức EC + snippet heise) có xác nhận chéo mạnh hơn. Synthesis nên coi phần lớn VERIFIED ở đây là "đã kiểm chứng nội dung nguồn", không phải "đã kiểm chứng thực tế độc lập".
