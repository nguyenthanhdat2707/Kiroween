# Task B Round 1 — Agent A

## Metadata

- **Agent:** A (Round 1 — Independent Discovery)
- **Model / Effort (từ launch args):** not observable (tham số khởi chạy không hiển thị trong ngữ cảnh worker)
- **Thời gian thực hiện (UTC):** 2026-11-25T12:28:33Z – 2026-11-25T12:41:30Z
- **Số truy vấn tìm kiếm web (xấp xỉ):** 17 truy vấn (`search_web`) + 1 truy vấn NCBI E-utilities `esearch`
- **Nguồn tham chiếu:** 34 mục trong bảng tham chiếu — **26 nguồn mở trực tiếp** (HTTP 200 qua `urllib`/API và đọc nội dung trực tiếp), **8 nguồn/nhóm chỉ xem qua snippet** (gắn nhãn `Snippet only`, mọi khẳng định dựa riêng trên nhóm này tối đa ở mức `INFERENCE`)
- **Lỗi / Truy cập thất bại đã ghi nhận:**
  - `https://pmc.ncbi.nlm.nih.gov/articles/PMC3850942/`: bị chặn bởi reCAPTCHA (dừng ngay, không vượt CAPTCHA; thay thế bằng API mở chính thức NCBI E-utilities `efetch` để đọc trực tiếp tóm tắt XML của 4 bài báo peer-reviewed).
  - `https://www.softwareheritage.org/`: lỗi xác thực chứng chỉ SSL cục bộ (`CERTIFICATE_VERIFY_FAILED`); `https://archive.softwareheritage.org/api/1/stat/counters/`: HTTP 403 Forbidden.
  - `https://docs.joinmastodon.org/user/moving/`: `Connection refused` (đã mở trực tiếp bản gốc Markdown chính thức trên GitHub `mastodon/documentation`).
  - `https://law.justia.com/.../23-1260-2024-09-04.html`, `https://sso.agc.gov.sg/Act/NLBA1995`: HTTP 403 Forbidden.
  - `https://www.nlb.gov.sg/main/services/web-archive-singapore`, `https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32019L0790`: HTTP 202 (trang trống/chờ JS challenge).
  - `https://www.copyrightexceptions.eu/article-6/`, `https://www.gida-global.org/care`, `https://www.ndl.go.jp/en/collect/online/warp.html`, `https://warp.ndl.go.jp/contents/en/about/index.html`, `https://www.unesco.org/en/software-heritage`, `https://wiki.archiveteam.org/index.php/Yahoo!_GeoCities_Japan`, `https://netpreserve.org/about-us/members/national-library-of-korea/`: HTTP 404 (đã tìm và mở trực tiếp các URL chính thức tương đương cho NDL Japan, GIDA, EU Copyright, IIPC Members).

---

## 1. Method

### Các phương pháp Phân tích Nghiệp vụ (Business Analysis) được lựa chọn và lý do

1. **Root-Cause Analysis & Problem Tree (Phân tích nguyên nhân gốc & Cây vấn đề):** Câu hỏi trung tâm giả định nền tảng biến mất là một nguyên nhân đồng nhất. Cây vấn đề giúp tách biệt triệu chứng (sụt giảm người dùng) khỏi nguyên nhân cấu trúc (chi phí vận hành cố định, phụ thuộc nhà tài trợ đơn lẻ, mất vòng lặp kinh tế, nợ kỹ thuật/pháp lý) và tách biệt "thất bại thương mại" với "lỗi thời thực sự".
2. **Stakeholder Analysis & Jobs-to-be-Done (JTBD):** Bảo tồn số là thị trường lệch pha nghiêm trọng giữa *người hưởng lợi* và *người trả tiền*. Phân tích các bên liên quan kết hợp JTBD buộc tách rõ **nhu cầu đã chứng minh** (hành vi thực: chữ ký ECI, đóng góp mã nguồn mở, chi ngân sách thư viện, lưu lượng lưu trữ) khỏi **nhu cầu giả định** (mong muốn chung chung "nên giữ lại").
3. **Alternative & Gap Analysis (Phân tích giải pháp hiện có và khoảng trống):** Hệ sinh thái bảo tồn số đã có các tổ chức lớn (Internet Archive, Software Heritage, Webrecorder, EaaSI, DTI, lưu chiểu quốc gia). Mọi khoảng trống cơ hội chỉ hợp lệ sau khi đối chiếu trực tiếp với giới hạn kỹ thuật, vận hành và pháp lý của các giải pháp mạnh nhất hiện tại.
4. **Sustainability & Unit-Economics Analysis:** Bảo tồn có bản chất chi phí kéo dài vô hạn trong khi giá trị thương mại suy giảm theo thời gian. Phân tích tính bền vững giúp sàng lọc sớm các mô hình phụ thuộc vào tăng trưởng thương mại hoặc tình nguyện ngắn hạn.
5. **Hypothesis Framing & Falsification Design (Thiết kế giả thuyết và thí nghiệm bác bỏ nhỏ nhất):** Thay vì đề xuất giải pháp ứng dụng, mỗi không gian cơ hội được định nghĩa bằng các giả thuyết cốt lõi và thí nghiệm bác bỏ tối thiểu để kiểm chứng trước khi xây dựng.

### Những gì báo cáo này KHÔNG làm

- Không thiết kế kiến trúc ứng dụng, giao diện người dùng hay chọn sản phẩm cuối cùng.
- Không xếp hạng các không gian cơ hội Task B so với các ứng viên Phase 2.
- Không lặp lại các mảng đã được khảo sát sâu trước đó (thiết bị IoT phụ thuộc cloud bị brick, link rot/bookmark cá nhân kiểu Pocket, Q&A kiểu Stack Overflow/Yahoo Answers, kiến thức chưa lập chỉ mục trên Discord/Slack, InfoPath/Flash/Jamboard/Google Reader/Yahoo! Pipes/DMOZ/VHS/gia phả Hán Nôm), trừ khi nêu ngắn gọn như đối chứng bối cảnh.

---

## 2. Root causes

### Cây vấn đề: Vì sao các nền tảng số có giá trị biến mất?

```
[Hệ quả] Mất nội dung, tri thức, quy trình làm việc, khả năng tái lập và kết nối cộng đồng
   ▲
   ├── [Nguyên nhân trực tiếp 1] Đóng cửa đột ngột hoặc ngừng bảo trì máy chủ/dịch vụ
   │      ├── Mất nguồn tài trợ đơn lẻ / cạn vốn vận hành (vd: Cohost 2024–2025, Tianya 2023)
   │      ├── Hết chu kỳ tài trợ nghiên cứu ngắn hạn (2–5 năm) cho web app học thuật
   │      └── Chi phí lưu trữ, kiểm duyệt, băng thông và pháp lý tăng theo quy mô nhưng không có nguồn thu tương ứng
   │
   ├── [Nguyên nhân trực tiếp 2] Quyết định thương mại & tái cấu trúc danh mục
   │      ├── Bị thâu tóm và khai tử sản phẩm trùng lặp hoặc bán lẻ tài sản (vd: InVision 12/2024, Freehand bán cho Miro)
   │      └── Chuyển dịch mô hình kinh doanh sang dịch vụ định kỳ/nền tảng mới, cắt máy chủ thế hệ cũ (vd: Nintendo 3DS/Wii U 4/2024)
   │
   └── [Nguyên nhân trực tiếp 3] Lỗi thời công nghệ & khóa chặt kiến trúc (Architectural Lock-in)
          ├── Phụ thuộc chặt vào phần mềm server-side, cơ sở dữ liệu, API hoặc DRM ("phone home")
          ├── Thiếu chuẩn xuất dữ liệu giữ nguyên ngữ nghĩa quan hệ (dữ liệu xuất ra bị phẳng hóa)
          └── Rào cản bản quyền/EULA ngăn bên thứ ba hoặc thư viện tiếp quản hợp pháp
```

### Sụt giảm người dùng: Nguyên nhân hay triệu chứng?

- **[A-G-C1] [VERIFIED]:** Sụt giảm người dùng thường là **triệu chứng đi sau** hoặc chỉ là một trong nhiều nguyên nhân, không phải nguyên nhân duy nhất khiến nền tảng biến mất. Trường hợp **Cohost** (Mỹ) có 203.805 người dùng (11/2023) nhưng vẫn phải chuyển sang chế độ chỉ đọc từ 01/10/2024 và đóng cửa hoàn toàn 12/01/2025 do mất nguồn tài trợ chính và kiệt sức của nhóm 4 nhân sự (`R18`, `R22`). Tương tự, **Tianya Club** (Trung Quốc) từng đứng thứ 11 về lưu lượng tại Trung Quốc (2015) nhưng bị ngắt kết nối tháng 4/2023 do nợ phí máy chủ/trung tâm dữ liệu kéo dài (`R19`, `R26`).
- **[A-G-C2] [VERIFIED]:** Trong khu vực học thuật, sự biến mất của nền tảng web gắn chặt với **chu kỳ tài trợ và thiếu hạ tầng bảo trì dài hạn**, không chỉ do mất giá trị khoa học. Phân tích 3.649 dịch vụ web tin sinh học xuất bản 1994–2017 trên 375 tạp chí cho thấy >95% hoạt động trong 2 năm đầu, nhưng giảm xuống 84% ở năm thứ 3 và chỉ còn 69% (2.522/3.649) đang hoạt động tại thời điểm đo; chu kỳ bán rã trung bình là 10,39 năm ($p < 10^{-16}$) (`R05`).

### Phân biệt "Thất bại thương mại" và "Lỗi thời thực sự"

| Tiêu chí | Thất bại thương mại (Commercially Unsuccessful) | Lỗi thời thực sự (Genuinely Obsolete) |
|---|---|---|
| **Bản chất giá trị** | Sản phẩm vẫn có người dùng tích cực hoặc di sản tri thức/văn hóa độc nhất, nhưng đơn vị vận hành không cân đối được doanh thu – chi phí (vd: Cohost, Nintendo 3DS online, dịch vụ học thuật hết grant). | Công năng cốt lõi đã được thay thế hoàn toàn bằng chuẩn mở hoặc công cụ tốt hơn, rẻ hơn mà không làm mất dữ liệu hay ngữ cảnh độc nhất. |
| **Chi phí chuyển đổi** | Cao hoặc bất khả thi do khóa chặt server/DRM/lược đồ đóng (vd: dự án InVision bị xóa vĩnh viễn sau 31/12/2024; game online-only bị khóa). | Thấp; người dùng đã chủ động di chuyển và không còn nhu cầu quay lại tài sản cũ. |
| **Tác hại khi biến mất** | Mất khả năng tái lập khoa học, mất quyền sở hữu tiêu dùng, đứt gãy ký ức văn hóa và cộng đồng. | Tối thiểu; chủ yếu mang tính hoài niệm cá nhân. |

### Khi nào việc bảo tồn KHÔNG cần thiết hoặc KHÔNG hợp lý về kinh tế?

- **[A-G-C3] [VERIFIED]:** Nghiên cứu của Wren et al. (2017) trên *Nucleic Acids Research* cho thấy các tài nguyên phân tích dữ liệu khoa học (SDAR) được trích dẫn nhiều nhất có xác suất **94%** được di dời thành công sang URL mới, trong khi nhóm không được trích dẫn chỉ có xác suất **34%** (`R06`). Điều này chứng minh cơ chế chọn lọc tự nhiên: nhiều tài nguyên biến mất vì thực sự không còn được sử dụng.
- **[A-G-C4] [INFERENCE]:** Việc bảo tồn **không hợp lý về kinh tế** trong 4 trường hợp: (1) nội dung/chức năng đã có bản thay thế mở vượt trội và dữ liệu đã được xuất sạch; (2) nền tảng thương mại thất bại nhưng cộng đồng đã phân tán hoàn toàn (ví dụ nỗ lực hồi sinh thương mại **Cyworld** tại Hàn Quốc năm 2022–2023 dù phục hồi ảnh cũ nhưng vẫn chật vật duy trì tương tác và phải tạm ngưng dịch vụ năm 2023, `R20`, `R26`); (3) chi phí vận hành live-server 24/7 vượt xa giá trị cộng đồng còn lại mà không thể chuyển sang dạng tĩnh (static/read-only); (4) chi phí xử lý pháp lý/bản quyền hoặc rủi ro quyền riêng tư vượt quá lợi ích công cộng.

---

## 3. Stakeholders and demand

| Bên liên quan | Chủ thể cụ thể | Job-to-be-Done (JTBD) | Hành vi hiện tại | Sẵn sàng đóng góp | Sẵn sàng trả tiền | Loại nhu cầu | Bằng chứng |
|---|---|---|---|---|---|---|---|
| **Người dùng cá nhân** | Người mua game/phần mềm online-only; người dùng SaaS/mạng xã hội sắp đóng cửa | Không bị tước đoạt sản phẩm đã mua; mang theo lịch sử bài viết, ảnh và dữ liệu cá nhân sang nơi khác ở dạng dùng được | Ký kiến nghị ECI; tải file xuất JSON/CSV thủ công; dùng homebrew/server cộng đồng (Pretendo) | Cao về ký tên, lan truyền, phản hồi; thấp về bảo trì kỹ thuật | Thấp cho công cụ lưu trữ thụ động; trung bình nếu gắn với quyền sở hữu/chuyển đổi trực tiếp | **Demonstrated** (quy mô lớn ở nhóm game; hỗn hợp ở nhóm dữ liệu cá nhân) | `R01` (1.294.188 chữ ký hợp lệ ECI), `R10` (Mastodon export), `R12` (Pretendo) |
| **Cộng đồng trực tuyến** | Nhóm tình nguyện bảo tồn (Archive Team, Pretendo Network, cộng đồng fandom/forum) | Cứu kho nội dung cộng đồng trước hạn chót đóng cửa; duy trì không gian tương tác liên tục | Chạy crawler khẩn cấp (96 triệu URL Yahoo! GeoCities Japan; hoãn đóng Cohost tới 1/2025 để Archive Team cào); reverse-engineer server | **Rất cao** (hàng nghìn giờ kỹ thuật tình nguyện, 170 repo GitHub trên Pretendo) | Thấp–Trung bình (quyên góp nhỏ lẻ kiểu Patreon/nhà tài trợ ẩn danh €24.000 cho ECI) | **Demonstrated** | `R01`, `R12`, `R13`, `R18`, `R26` |
| **Nhà nghiên cứu & nhà giáo dục** | Phòng thí nghiệm tin sinh học, học giả nhân văn số (DH), giảng viên dùng phần mềm học thuật | Tái lập kết quả nghiên cứu cũ; giữ website/cơ sở dữ liệu dự án sống sau khi hết grant 3–5 năm | Trích dẫn qua DOI/Zenodo; thử áp dụng Endings Principles (tĩnh hóa); tìm bản lưu trên Wayback Machine | Trung bình (sẵn sàng tuân thủ chuẩn nếu có yêu cầu của tạp chí/nhà tài trợ) | Thấp bằng tiền túi; phụ thuộc vào ngân sách grant hoặc thư viện trường | **Demonstrated** (vấn đề) / **Mixed** (trả tiền công cụ mới) | `R05`, `R06`, `R07`, `R08`, `R09` |
| **Tổ chức văn hóa & thư viện (GLAM)** | Thư viện đại học (Yale, Stanford), thành viên DPC/IIPC/SPN, bảo tàng | Lưu trữ, lập chỉ mục và cung cấp quyền truy cập lâu dài, hợp pháp cho tài sản số dễ hỏng | Mua gói Archive-It; chạy node EaaSI; dùng Browsertrix/WACZ; vận động miễn trừ DMCA §1201 | Cao (tham gia liên minh, chia sẻ chuẩn mở, tài trợ nghiên cứu) | **Đã chứng minh** (ngân sách công/thư viện, tài trợ Mellon/Sloan/IMLS, phí thành viên DPC/IIPC/Archive-It) | **Demonstrated** | `R03`, `R04`, `R11`, `R14`, `R15`, `R21`, `R27` |
| **Nhà phát triển phần mềm** | Kỹ sư mã nguồn mở, đội ngũ sản phẩm SME dùng công cụ thiết kế/cộng tác | Không mất mã nguồn lịch sử, phụ thuộc và tài sản thiết kế/tài liệu khi forge hoặc SaaS đóng cửa | Đẩy mã lên GitHub/Software Heritage; xây dựng bộ chuyển đổi khi SaaS đóng cửa (vd: từ InVision sang Figma/Penpot) | Cao với công cụ mã nguồn mở thực dụng (DTP: 3.626 sao; Browsertrix: 1.202 sao) | Trung bình–Cao ở doanh nghiệp (sẵn sàng chi cho công cụ di chuyển giảm downtime/mất dữ liệu) | **Demonstrated** (nhưng phân mảnh theo từng SaaS) | `R16`, `R17`, `R23`, `R25` |
| **Đơn vị vận hành nền tảng** | Công ty SaaS, nhà phát hành game, mạng xã hội độc lập (ASSC/Cohost) | Đóng cửa an toàn, giảm thiểu rủi ro pháp lý, tuân thủ EU Data Act và bảo vệ uy tín mà không tốn chi phí vận hành vô hạn | Đặt chế độ read-only tạm thời (Cohost), cung cấp nút tải export tối thiểu, hoặc phản đối nghĩa vụ pháp lý tốn kém (ngành game tại EU/Mỹ) | Thấp nếu phát sinh chi phí kỹ thuật/pháp lý sau khi hết doanh thu; chỉ tăng khi bị luật bắt buộc | **Rất thấp** tự nguyện; chỉ chi khi bắt buộc tuân thủ (EU Data Act 2025–2027) | **Mixed** (chủ yếu do áp lực tuân thủ, không phải tự nguyện) | `R02`, `R04`, `R18`, `R21`, `R23` |
| **Tổ chức di sản số quốc gia & bản địa** | NDL (Nhật Bản), NLK OASIS (Hàn Quốc), NLB (Singapore), GIDA (Liên minh Dữ liệu Bản địa Toàn cầu) | Bảo tồn di sản số quốc gia/văn hóa theo luật lưu chiểu và đảm bảo chủ quyền/đồng thuận dữ liệu (CARE) | Thu thập web tự động miền công (WARP) hoặc toàn miền `.sg` (NLB Act 2019); xây khung quản trị CARE | Cao về chuẩn mực, chính sách và hợp tác quốc tế (IIPC) | **Đã chứng minh** (ngân sách nhà nước cho thư viện quốc gia; hạn chế hơn ở tổ chức bản địa) | **Demonstrated** | `R15`, `R24`, `R27` (xem thêm `R21`) |

- **[A-G-C5] [VERIFIED]:** Nhu cầu hành vi mạnh nhất hiện nay tập trung ở hai cực: (1) **công dân/cộng đồng phản ứng với việc tước đoạt sản phẩm số đã mua** (1.294.188 chữ ký hợp lệ ECI `Stop Destroying Videogames` và 170 kho mã của Pretendo Network, `R01`, `R12`, `R13`); và (2) **các tổ chức GLAM/học thuật** có ngân sách thể chế cho bảo tồn nhưng bị nghẽn về nhân lực kỹ thuật và pháp lý (`R03`, `R04`, `R11`, `R14`).

---

## 4. Preservation dimensions

| Chiều bảo tồn | Giá trị tạo ra | Tính khả thi kỹ thuật | Tính khả thi kinh tế | Nhận định & Bằng chứng |
|---|---|---|---|---|
| **1. Content preservation** (Nội dung tĩnh: văn bản, ảnh, trang web) | Cao về ký ức lịch sử & tham chiếu; nhưng mất tương tác và ngữ cảnh quan hệ nếu chỉ chụp ảnh màn hình | **Cao** (WARC, WACZ 1.1.1 cho phép phát lại trên trình duyệt qua HTTP Range không cần server Wayback phức tạp, `R17`) | **Trung bình–Cao** (chi phí lưu trữ lạnh thấp, nhưng chi phí nhân lực tuyển chọn và lưu trữ dài hạn không bằng 0) | Đã trưởng thành về chuẩn kỹ thuật (`R17`); thách thức chính chuyển sang pháp lý và web động cần đăng nhập. **[A-G-C6] [VERIFIED]** |
| **2. Knowledge preservation** (Tri thức có cấu trúc, nghiên cứu, mã nguồn, thảo luận) | **Rất cao** — trực tiếp bảo vệ tính tái lập khoa học và tri thức tích lũy (43% tài nguyên mất trên MEDLINE là chương trình máy tính, 38% nội dung học thuật, 19% CSDL, `R07`) | **Trung bình–Cao** (Software Heritage dùng Merkle DAG khử trùng lặp >27 tỷ tệp mã nguồn; Endings Project tĩnh hóa tri thức DH, `R09`, `R25`) | **Trung bình** (khả thi với mô hình đồng tài trợ công–tư hoặc thư viện đại học; khó thu phí trực tiếp từ người dùng cuối) | Giá trị/chi phí rất tốt nếu tách tri thức khỏi phần mềm vận hành sớm (`R09`, `R25`). **[A-G-C7] [VERIFIED]** |
| **3. Software functionality** (Khả năng chạy và tương tác của phần mềm/ứng dụng web) | Cao với phần mềm khoa học, giáo dục, sáng tạo và game; nhưng không cần thiết cho phần mềm phổ thông đã có thay thế tốt | **Thấp–Trung bình** (cấu hình giả lập EaaSI cho 1 ứng dụng 1985 mất 2 ngày thủ công bởi 2 chuyên gia, `R11`; phần mềm phụ thuộc backend đóng khó khôi phục nếu không có mã server) | **Thấp** (tốn compute và nhân lực kỹ thuật chuyên sâu; khó thương mại hóa ngoài ngân sách bảo tàng/nghiên cứu) | Khả thi cao hơn khi chuyển dịch sang tĩnh hóa/WASM hoặc tự động hóa cấu hình giả lập; kém khả thi với server-side phức tạp (`R09`, `R11`). **[A-G-C8] [VERIFIED]** |
| **4. User data and workflows** (Dữ liệu cá nhân, đồ thị quan hệ, quy trình làm việc) | **Rất cao** cho người dùng/doanh nghiệp đang hoạt động (tránh mất trắng tài sản như vụ InVision 31/12/2024, `R23`) | **Trung bình** (EU Data Act mở quyền xuất dữ liệu từ 9/2025, nhưng gói xuất API/JSON hiện tại làm mất khóa ngoại, quan hệ và logic ứng dụng, `R02`, `R16`, `R24`) | **Cao nhất trong 7 chiều** (doanh nghiệp và người dùng chuyên nghiệp có lý do trực tiếp để trả tiền cho việc chuyển đổi không đứt gãy) | Là chiều duy nhất có động lực kinh tế trực tiếp gắn với tuân thủ luật mới (EU Data Act) và chi phí cơ hội rõ ràng (`R02`, `R16`, `R23`). **[A-G-C9] [INFERENCE]** |
| **5. Community continuity** (Sự liên tục của mạng lưới xã hội và cộng đồng) | Cao về giá trị xã hội, nhưng **không thể ép buộc bằng công nghệ** | **Thấp–Trung bình** (ngay cả giao thức mở ActivityPub/Mastodon cũng chỉ chuyển được danh sách người theo dõi, **không chuyển được bài viết và media** do giới hạn ID gắn tên miền và chữ ký mật mã, `R10`) | **Thấp** (cộng đồng có tính mạng lưới rất mong manh; hồi sinh thương mại như Cyworld 2022–2023 vẫn thất bại trong giữ chân người dùng, `R20`, `R26`) | Rủi ro ảo tưởng cao nhất: lưu được dữ liệu không đồng nghĩa giữ được cộng đồng sống (`R10`, `R18`, `R20`). **[A-G-C10] [VERIFIED]** |
| **6. Cultural and historical heritage** (Di sản văn hóa, ngôn ngữ, ký ức tập thể) | Cao về giá trị xã hội dài hạn; giá trị không đo bằng doanh thu ngắn hạn | **Trung bình** (kỹ thuật lưu trữ đã có, nhưng đòi hỏi siêu dữ liệu văn hóa, phân quyền truy cập và tôn trọng đồng thuận theo CARE/GDPR, `R14`, `R27`) | **Trung bình** (bắt buộc dựa vào ngân sách công, lưu chiểu quốc gia hoặc quỹ phi lợi nhuận; không có thị trường thương mại tự nuôi) | Cần tách bạch giữa "di sản công cộng" và "di sản nhạy cảm/bản địa" không được phép mở công khai (`R03`, `R14`, `R15`). **[A-G-C11] [VERIFIED]** |
| **7. Operational continuity** (Duy trì hạ tầng chạy sống thay cho nền tảng gốc) | Cao trong giai đoạn chuyển tiếp hoặc cho cộng đồng cốt lõi (vd: Pretendo cho 3DS/Wii U) | **Rất thấp** (đòi hỏi kỹ thuật đảo ngược sạch, bảo trì server 24/7, kiểm duyệt chống gian lận, không kế thừa được tài khoản gốc như NNID, `R12`) | **Rất thấp** (chi phí vận hành cố định lặp lại mãi mãi — chính là lý do khiến nền tảng gốc như Cohost và Tianya sụp đổ, `R18`, `R19`) | Chỉ bền vững ở quy mô hẹp với cộng đồng tình nguyện đặc biệt nhiệt huyết hoặc khi nhà phát hành bàn giao bản tự vận hành từ đầu (`R01`, `R12`, `R18`). **[A-G-C12] [VERIFIED]** |

---

## 5. Existing solutions and gaps

| Hướng tiếp cận | Giải pháp tiêu biểu đã kiểm tra | Điểm mạnh | Giới hạn & Rào cản chấp nhận | Vấn đề chưa được giải quyết (Khoảng trống thực) |
|---|---|---|---|---|
| **1. Internet Archive & Web Archiving** | Wayback Machine, Archive-It, Webrecorder (Browsertrix Crawler, WACZ 1.1.1, ReplayWeb.page) | Quy mô khổng lồ (IA); WACZ 1.1.1 cho phép đóng gói WARC+chỉ mục để phát lại trực tiếp trên trình duyệt không cần server Wayback (`R17`); Browsertrix mã nguồn mở phát triển mạnh (1.202 sao, cập nhật 24/11/2026). | Nghiên cứu trên 14.489 trang học thuật cho thấy chỉ 62% được lưu trữ và IA thiên lệch về URL ngắn (`R08`); nội dung sau tường đăng nhập/SPA phức tạp khó cào; WACZ ký mật mã nên khó bổ sung siêu dữ liệu hậu kỳ (`R27`); IA chịu rủi ro pháp lý lớn (*Hachette v. IA*, 12/2024, `R19c`) và tấn công mạng (10/2024). | Thiếu cầu nối lưu trữ nội dung tương tác/sau đăng nhập có sự đồng thuận của chủ tài khoản và thiếu giải pháp giảm công sức vận hành Docker/crawler cho tổ chức nhỏ. |
| **2. Software Preservation & Emulation** | EaaSI (Yale / SPN), Software Heritage (Inria/UNESCO), DOSBox/MAME | Software Heritage bảo tồn mã nguồn mở ở quy mô phổ quát (>27 tỷ tệp trên Merkle DAG, `R25`); EaaSI cho phép chạy phần mềm cũ qua trình duyệt trong môi trường thư viện (`R11`). | Cấu hình môi trường EaaSI cực kỳ tốn công (2 ngày cho 1 phần mềm 1985 tại Stanford do tài liệu giả lập sai lệch và thiếu liên kết bền vững tới danh mục thư viện, `R11`); Software Heritage chỉ lưu **mã nguồn**, không bảo đảm môi trường build/chạy lại dịch vụ web động; DMCA §1201 (10/2024) cấm thư viện cho truy cập từ xa vào game/phần mềm lưu trữ (`R04`, `R21`). | Khoảng trống lớn giữa **có mã nguồn/ảnh đĩa** và **chạy lại được môi trường** ở chi phí nhân lực thấp, đặc biệt cho ứng dụng web học thuật và kho phần mềm thư viện. |
| **3. Data Portability & Migration** | Data Transfer Initiative (DTI / Data Transfer Project), Google Takeout, Mastodon Export, EU Data Act | DTP là mã nguồn mở tích cực (3.626 sao, cập nhật 25/11/2026) kết nối hơn chục dịch vụ lớn; DTI xây dựng Data Trust Registry (~40 đơn vị) và AI Conversation Schema mới (`R16`); EU Data Act bắt buộc quyền chuyển đổi cloud từ 12/09/2025 (`R02`). | DTP chỉ xử lý mô hình dữ liệu chuẩn hóa đơn giản (ảnh, danh bạ, lịch), **không bảo toàn được cấu trúc quan hệ, khóa ngoại, bình luận và logic quy trình** (`R24`); gói xuất Takeout/SaaS/Mastodon là file JSON/ZIP "chết", không có công cụ khôi phục thành không gian làm việc có thể duyệt/nhập lại (`R10`). | Khoảng trống "hậu xuất dữ liệu" (post-export usability gap): có file xuất hợp pháp nhưng mất ngữ nghĩa quan hệ và không thể tái sử dụng hoặc di chuyển sang công cụ mới. |
| **4. Open-Source Alternatives** | Penpot (thay Figma/InVision), Mastodon/Lemmy, Matrix, Nextcloud | Xóa bỏ phụ thuộc vào nhà cung cấp độc quyền; mã nguồn có thể fork khi đội ngũ cũ ngừng phát triển. | Thiếu khả năng nhập trọn vẹn định dạng độc quyền từ nền tảng đóng cửa (vd: người dùng InVision phải xây lại prototype từ file gốc Sketch/Photoshop, `R23`); hiệu ứng mạng và chi phí chuyển đổi thói quen người dùng rất cao. | Phần mềm mã nguồn mở giải quyết tương lai, nhưng **không tự động giải cứu tài sản cũ** bị kẹt trong định dạng/nền tảng đóng sắp tắt. |
| **5. Self-Hosting** | Tự vận hành Docker/VPS, Mastodon instance cá nhân, máy chủ trường đại học | Toàn quyền kiểm soát dữ liệu và chính sách. | Chính rào cản vận hành và chi phí duy trì khiến các instance tự vận hành cũng chết yểu (rủi ro đóng cửa đột ngột của server Mastodon, buộc phải có Server Covenant báo trước 3 tháng, `R10`); máy chủ phòng lab đại học chết nhanh sau 2–3 năm khi nghiên cứu sinh tốt nghiệp (`R05`). | Tự vận hành chỉ chuyển dịch gánh nặng bảo trì từ doanh nghiệp sang cá nhân/phòng lab — không giải quyết tận gốc chi phí vận hành liên tục nếu kiến trúc vẫn cần server sống. |
| **6. Decentralized Storage** | IPFS, Filecoin, Arweave | Địa chỉ hóa theo nội dung (content-addressed), chống kiểm duyệt và chống hỏng bit đơn điểm. | IPFS **không có cơ chế khuyến khích lưu trữ** — dữ liệu biến mất nếu không trả phí pinning định kỳ; Filecoin yêu cầu gia hạn hợp đồng lưu trữ và độ trễ truy xuất cao; Arweave thu phí một lần dựa trên giả định giá phần cứng luôn giảm (`R27b`); mức độ tập trung hóa gateway/node thực tế vẫn cao; và **không giải quyết lỗi thời định dạng hay phần mềm** (`R27b`). | Lưu trữ phi tập trung chỉ là lớp bitstream (tầng thấp nhất), không giải quyết được ngữ nghĩa, siêu dữ liệu, pháp lý GDPR (quyền xóa mâu thuẫn với tính bất biến) hay khả năng chạy lại. |
| **7. Community-Led Platform Revival** | Pretendo Network (3DS/Wii U), Wiimmfi (Wii), dự án hồi sinh server game/forum | Chứng minh nhu cầu và năng lực kỹ thuật cực mạnh của cộng đồng (Pretendo có 170 repo GitHub, hàng chục đóng góp viên, đạt 75–100% ở nhiều tựa game, `R12`, `R13`). | Đòi hỏi mod phần cứng (Luma3DS/Aroma); **không thể di chuyển tài khoản/dữ liệu người dùng cũ** (NNID bị kẹt ở Nintendo, `R12`); rủi ro pháp lý cao; tiến độ phân mảnh theo thời gian rảnh của tình nguyện viên và gánh nặng kiểm duyệt/chống gian lận. | Thiếu chuẩn bàn giao hợp pháp từ nhà phát hành trước khi tắt server để cộng đồng không phải đảo ngược từ con số 0 trong vùng xám pháp lý. |
| **8. Digital Heritage Preservation Systems** | NDL WARP (Nhật Bản), NLK OASIS (Hàn Quốc), Web Archive Singapore, Mukurtu CMS, The Endings Project | Có thẩm quyền pháp lý rõ ràng cho miền công/lưu chiểu quốc gia (`R15`, `R27c`); Endings Project đưa ra bộ nguyên tắc tĩnh hóa không phụ thuộc server cực kỳ bền vững (`R09`). | Luật lưu chiểu quốc gia thường **loại trừ blog, mạng xã hội, nội dung động phức tạp** và giới hạn xem tại chỗ trong thư viện (như Luật NDL Nhật Bản, `R15`); nguyên tắc Endings đòi hỏi tái thiết kế dự án ngay từ giai đoạn xây dựng, khó áp dụng ngược cho hàng nghìn nền tảng đã vận hành. | Khoảng trống giữa tiêu chuẩn bảo tồn lý tưởng (tĩnh hóa, đồng thuận, tuân thủ luật) và thực tế các nền tảng web động/cộng đồng đang tồn tại cần "đóng băng" nhanh khi sắp đóng cửa. |

---

## 6. Sustainability

### Sự lệch pha cấu trúc: Ai hưởng lợi — Ai trả tiền — Ai bảo trì?

- **[A-G-C13] [VERIFIED]:** Phần lớn các dự án bảo tồn thất bại không phải vì thiếu công nghệ lưu trữ, mà vì **bài toán kinh tế bất đối xứng**: công chúng và thế hệ tương lai hưởng lợi, nhưng chi phí lưu trữ, băng thông, pháp lý và nhân lực kỹ thuật phải trả hàng tháng ngay ở hiện tại.
- **Bằng chứng thất bại bền vững thực tế:**
  - **WebCite:** Dịch vụ lưu trữ trích dẫn học thuật từng được khuyến nghị rộng rãi trong các nghiên cứu `BMC Bioinformatics` (2013, `R08`), nhưng đã ngừng nhận yêu cầu lưu trữ mới từ tháng 6/2023 sau nhiều năm gián đoạn vì thiếu mô hình tài chính bền vững (`R27d`, snippet only → `INFERENCE` cho nguyên nhân tài chính cụ thể).
  - **Cohost (ASSC):** Nền tảng mạng xã hội phi lợi nhuận từ chối quảng cáo và vốn VC, cố gắng vận hành bằng gói đăng ký tự nguyện "Cohost Plus" và một nhà tài trợ ẩn danh; khi nguồn tài trợ chính cạn và nhóm 4 người kiệt sức, nền tảng buộc phải đóng cửa 01/2025 (`R18`, `R22`).
  - **Tianya Club:** Nền tảng diễn đàn thương mại hàng đầu Trung Quốc nhưng mất mô hình doanh thu trước sự trỗi dậy của mobile/video ngắn, dẫn đến nợ phí máy chủ >10 triệu nhân dân tệ và ngắt kết nối suốt 3 năm (4/2023 – 6/2026) (`R19`, `R26`).
  - **Cyworld:** Nỗ lực hồi sinh thương mại năm 2022 sau khi phục hồi dữ liệu cũ vẫn không duy trì được dòng tiền/tăng trưởng và phải tạm ngưng dịch vụ giữa năm 2023 (`R20`, `R26`).

### Chi phí vận hành liên tục gồm những gì?

Theo các mô hình chi phí bảo tồn chuẩn (OAIS, CMDP của Lưu trữ Quốc gia Đan Mạch, `R27d` — snippet only) và bằng chứng thực nghiệm từ EaaSI/Endings (`R09`, `R11`):
1. **Chi phí lưu trữ vật lý/đám mây** chỉ là phần nổi (giảm theo thời gian nhưng tăng theo dung lượng media).
2. **Chi phí nhân lực chuyên môn** (cấu hình giả lập, kiểm tra toàn vẹn, chuyển đổi định dạng, xử lý bản quyền/takedown, kiểm duyệt cộng đồng) mới là khoản chi lớn nhất và không giảm theo định luật Moore.
3. **Chi phí hạ tầng động (server-side compute & bảo mật):** Mọi hệ thống còn giữ database/PHP/Python/API đều phát sinh nợ bảo mật vô hạn (`R09`).

### Mô hình nào có khả năng sống sót mà KHÔNG cần tăng trưởng thương mại liên tục?

1. **Chuyển đổi về "chi phí biên gần bằng 0" (Zero-Ops / Staticization):** Mô hình Endings Project (`R09`) và WACZ (`R17`) chứng minh cách duy nhất để một tài sản số tồn tại hàng thập kỷ mà không cần doanh thu liên tục là **loại bỏ hoàn toàn server-side compute**, biến nền tảng thành gói tĩnh lưu trên object storage/thư viện.
2. **Đồng tài trợ đa bên dạng hạ tầng công (Public Digital Infrastructure):** Mô hình **Software Heritage** (Inria + UNESCO + quỹ công Pháp + tài trợ từ doanh nghiệp/quỹ thiện nguyện như Microsoft, Intel, Simons Foundation, `R25` — snippet only).
3. **Ngân sách thể chế / Lưu chiểu luật định:** Thư viện quốc gia (NDL Nhật Bản, NLK Hàn Quốc, NLB Singapore) và thư viện đại học trả phí dịch vụ chuyên biệt (Archive-It, DPC, EaaSI) (`R03`, `R15`, `R27c`).
4. **Thương mại B2B ngắn hạn gắn với sự kiện chuyển đổi (Migration / Compliance SaaS):** Không nuôi kho lưu trữ vô hạn, mà thu phí **một lần hoặc theo gói tuân thủ** giúp doanh nghiệp/nhà cung cấp xuất, tái cấu trúc và chuyển dữ liệu theo EU Data Act hoặc khi đóng sản phẩm.

---

## 7. AI contribution

Đánh giá nghiêm ngặt theo nguyên tắc: **chỉ chấp nhận AI ở nơi tạo ra giá trị đo lường được so với kỹ thuật truyền thống; bác bỏ AI trang trí.**

| Tác vụ bảo tồn | Kỹ thuật truyền thống làm được gì? | AI đóng góp giá trị thực ở đâu? | Bằng chứng & Giới hạn / Rủi ro | Kết luận vai trò AI |
|---|---|---|---|---|
| **1. Suy luận lược đồ & khôi phục quan hệ từ gói export rời rạc** | Script ETL viết tay cho từng cặp nền tảng (tốn công, vỡ ngay khi nền tảng đổi JSON schema hoặc đóng cửa trước khi có adapter). | AI có thể phân tích cấu trúc các tệp JSON/CSV/HTML xuất ra không có tài liệu đầy đủ, suy luận khóa ngoại/quan hệ thực thể và sinh mã chuyển đổi **có thể kiểm chứng tự động bằng oracle toàn vẹn tham chiếu** (100% record khớp schema đích, không mất trường). | DTI xác nhận adapter thủ công mới phủ được hơn chục dịch vụ lớn (`R16`, `R24`). Rủi ro: suy luận sai ngữ nghĩa trường ẩn nếu không có bước xác thực mẫu với người dùng. | **Load-bearing (Cốt lõi)** nếu gắn với kiểm chứng xác định (deterministic verification). |
| **2. Tự động nhận diện & cấu hình môi trường giả lập phần mềm cũ** | Chuyên viên đọc manual cũ, thử-sai từng bản emulator + OS + driver (mất 2 ngày cho 1 phần mềm tại Stanford EaaSI, `R11`). | Trích xuất yêu cầu phần cứng/OS từ tài liệu scan/header nhị phân, đối chiếu ma trận tương thích và chạy vòng lặp tự kiểm thử khởi chạy trong sandbox (oracle: ứng dụng boot/render thành công không crash). | Trường hợp Stanford BDPL cho thấy điểm nghẽn lớn nhất là sự không chắc chắn về tổ hợp emulator/OS (`R11`). | **Load-bearing (Cốt lõi)** cho bài toán giảm thời gian cấu hình thủ công. |
| **3. Sàng lọc PII, ẩn danh hóa & gắn siêu dữ liệu cho kho lưu trữ quy mô lớn** | Regex/luật từ khóa (nhiều dương tính giả/âm tính giả với ngôn ngữ tự nhiên đa ngữ). | Nhận diện thực thể nhạy cảm (PII) để đáp ứng nguyên tắc tối thiểu hóa/ẩn danh hóa của GDPR Điều 89 (`R13b`) và gợi ý thẻ phân loại/siêu dữ liệu cho nhân viên lưu trữ duyệt (human-in-the-loop). | NARA và Library of Congress triển khai AI như công cụ hỗ trợ nội bộ cho nhân viên lưu trữ duyệt lại, không tự động phát hành (`R27e`, snippet only). | **Useful (Hữu ích)** với điều kiện bắt buộc có con người phê duyệt. |
| **4. Tóm tắt lịch sử, sinh nội dung thay thế hoặc "hồi sinh" cộng đồng bằng bot AI** | Lưu nguyên bản tài liệu, kiểm tra checksum (fixity), ký nguồn gốc (C2PA). | **Không tạo giá trị bảo tồn xác thực.** AI tạo sinh dễ sinh ảo giác (hallucination), làm phẳng sắc thái lịch sử và phá vỡ nguyên tắc nền tảng của lưu trữ học là tính xác thực nguồn gốc (archival authenticity). | NARA, Library of Congress và DPC cảnh báo ảo giác AI đe dọa niềm tin vào hồ sơ lưu trữ và đang thúc đẩy chuẩn xác thực C2PA cho G+LAM (`R27e`, snippet only). | **Unnecessary / Harmful (Không cần thiết & có hại)** — **BÁC BỎ**. |
| **5. Giải quyết bài toán pháp lý, bản quyền, quản trị EOL của live-service** | Khung pháp lý, hợp đồng, kiến trúc tách phụ thuộc từ đầu. | Không có vai trò kỹ thuật cốt lõi; AI không thể tạo ra quyền hợp pháp để vượt DRM hay thay thế trách nhiệm pháp lý của nhà phát hành. | Quyết định từ chối lập pháp của EC (6/2026) và từ chối mở rộng DMCA §1201 (10/2024) là rào cản pháp lý-kinh tế thuần túy (`R01`, `R04`). | **Unnecessary (Không cần thiết)** — **BÁC BỎ**. |

---

## 8. Legal and ethical constraints

### Phân biệt sống còn: "Truy cập công khai" ≠ "Được phép sao chép và phân phối lại hợp pháp"

- **[A-G-C14] [VERIFIED]:** Một sai lầm phổ biến trong các dự án bảo tồn số là cho rằng nội dung từng hiển thị công khai trên web thì có thể tự do sao lưu và mở lại công khai. Thực tế pháp lý tại cả Mỹ, EU và Nhật Bản đều phân biệt rạch ròi giữa **quyền sao chép để bảo tồn nội bộ** và **quyền phân phối/cho truy cập công cộng**.

### So sánh theo khu vực pháp lý

| Khu vực | Khung pháp lý chính | Quyền bảo tồn được phép | Rào cản & Giới hạn cứng | Bằng chứng |
|---|---|---|---|---|
| **Hoa Kỳ (NA)** | DMCA Section 1201 (9th Triennial Rulemaking, hiệu lực 28/10/2024); Fair Use (17 U.S.C. §107); án lệ *Hachette v. Internet Archive* (2nd Cir., 9/2024; kết thúc 12/2024) | Gia hạn miễn trừ phá DRM có thời hạn 3 năm cho thư viện, viện lưu trữ, bảo tàng bảo tồn phần mềm/game hợp pháp tại chỗ (`R04`). | **Từ chối mở rộng quyền truy cập từ xa** cho nghiên cứu viên đối với game hết bản in (`R04`, `R21`); tòa phúc thẩm bác bỏ lập luận Fair Use cho mô hình Controlled Digital Lending (CDL), buộc IA gỡ hàng trăm nghìn đầu sách theo yêu cầu nhà xuất bản (`R19c`). | `R04`, `R19c`, `R21` |
| **Liên minh châu Âu (EU)** | EU DSM Directive (2019/790) Điều 6; GDPR (2016/679) Điều 17 & Điều 89; EU Data Act (2023/2854, áp dụng 12/09/2025) | **DSM Điều 6:** Ngoại lệ bắt buộc cho phép tổ chức di sản văn hóa (CHI) sao chép tác phẩm trong bộ sưu tập thường trực để bảo tồn, vô hiệu hóa điều khoản hợp đồng cản trở (`R14d`, `R27g`). **EU Data Act:** Quyền chuyển đổi nhà cung cấp cloud/SaaS (cấm phí chuyển đổi từ 12/01/2027) (`R02`). | **GDPR Điều 89:** Lưu trữ vì lợi ích công bắt buộc có biện pháp bảo vệ (tối thiểu hóa dữ liệu, giả danh hóa); ngoại lệ đối với quyền truy cập/xóa/phản đối chỉ có hiệu lực khi luật EU hoặc quốc gia thành viên quy định cụ thể (`R13b`). Ngoài ra, EC ngày 16/06/2026 từ chối luật hóa bắt buộc giữ game sống sau EOL vì vướng quyền sở hữu trí tuệ (`R01`, `R21b`). | `R01`, `R02`, `R13b`, `R14d` |
| **Nhật Bản (Asia)** | Luật Thư viện Quốc hội Nhật Bản (National Diet Library Law — Điều 25-3 từ 4/2010; Điều 25-4 sửa đổi có hiệu lực 1/7/2013 và 1/1/2023); Luật Bản quyền Điều 43 | NDL được thu thập toàn diện web cơ quan công (WARP) không cần xin phép từ 4/2010; từ 1/1/2023 mở rộng lưu chiểu bắt buộc cho ấn phẩm trực tuyến trả phí/có DRM (yêu cầu nộp bản không DRM) (`R15`). | Web tư nhân trên WARP **bắt buộc xin phép từng chủ sở hữu**; Luật lưu chiểu **loại trừ rõ ràng** blog, tin nhắn ngắn, nhật ký, ấn phẩm khó thu thập kỹ thuật; quyền xem giới hạn **tại cơ sở vật lý của NDL** nếu chưa có phép của chủ bản quyền, **không cung cấp dịch vụ tải xuống** (`R15`). | `R15` |
| **Singapore & Hàn Quốc (Asia)** | Luật NLB Singapore (sửa đổi 2019 — Web Archive Singapore); Chương trình OASIS của Thư viện Quốc gia Hàn Quốc (từ 2004) | NLB Singapore được phép lưu trữ tên miền `.sg` mà không cần đồng ý bằng văn bản trước (từ 2019); NLK OASIS thu thập web/tài sản số liên quan Hàn Quốc và tham gia IIPC (`R27c`, `R15b`). | Giới hạn thẩm quyền trong phạm vi quốc gia/tên miền; vẫn chịu ràng buộc bản quyền khi công bố rộng rãi ra ngoài thư viện (`R27c`). | `R15b`, `R15c`, `R27c` |
| **Đạo đức & Chủ quyền dữ liệu (Toàn cầu)** | CARE Principles for Indigenous Data Governance (GIDA) | Thừa nhận quyền kiểm soát tập thể, lợi ích tập thể, trách nhiệm và đạo đức đối với dữ liệu cộng đồng bản địa (`R14e`, `R27h`). | Nguyên tắc "mở tối đa" (FAIR/open web archiving) có thể **gây hại** nếu công khai tri thức thiêng/bí mật hoặc dữ liệu nhạy cảm của cộng đồng yếu thế mà không có sự đồng thuận (`R03`, `R14e`, `R27h`). | `R03`, `R14e`, `R27h` |

---

## 9. International evidence

### Bắc Mỹ (North America)
- **Đóng cửa SaaS thương mại & mất dữ liệu thiết kế:** **InVision** (Mỹ) đóng cửa toàn bộ dịch vụ thiết kế/prototype ngày 31/12/2024 và xóa vĩnh viễn mọi tệp không kịp xuất (`R23`, snippet only → `INFERENCE`).
- **Sụp đổ mạng xã hội phi lợi nhuận vì chi phí:** **Cohost** (Mỹ, 203.805 người dùng) chuyển chỉ đọc 01/10/2024 và tắt hẳn 12/01/2025 sau khi hoãn để Archive Team kịp lưu trữ (`R18`, `VERIFIED` qua Wikipedia + kiểm chéo báo chí `R22`).
- **Tĩnh hóa di sản học thuật:** **The Endings Project** (Đại học Victoria, Canada) xây dựng bộ nguyên tắc v2.2.1 loại bỏ hoàn toàn server-side software để bảo tồn dự án nhân văn số sau khi hết tài trợ (`R09`, `VERIFIED`).
- **Rào cản pháp lý bảo tồn tại Mỹ:** Phán quyết *Hachette v. Internet Archive* (kết thúc 12/2024, `R19c`) và quyết định DMCA §1201 (28/10/2024, `R04`) thu hẹp không gian truy cập từ xa của thư viện.

### Châu Âu (Europe)
- **Huy động công dân quy mô lục địa:** Sáng kiến Công dân châu Âu **Stop Destroying Videogames** (`ECI(2024)000007`) đạt **1.294.188 chữ ký hợp lệ** (Pháp: 145.289; Tây Ban Nha: 121.616; Áo: 20.714; v.v.), được nộp ngày 26/01/2026 và nhận phản hồi chính thức của Ủy ban châu Âu ngày 16/06/2026 (`C(2026)4110`) từ chối lập pháp bắt buộc nhưng mở đối thoại xây dựng bộ quy tắc ứng xử EOL (`R01`, `VERIFIED`).
- **Luật hóa quyền chuyển đổi đám mây:** **EU Data Act** (Regulation 2023/2854) có hiệu lực áp dụng từ 12/09/2025 (cấm phí chuyển đổi từ 12/01/2027), kèm điều khoản hợp đồng mẫu (SCCs) và Data Act Legal Helpdesk (`R02`, `VERIFIED`).
- **Hạ tầng bảo tồn công–tư:** **Software Heritage** (Inria, Pháp + UNESCO) và **DPC Global Bit List 2025** (Vương quốc Anh/toàn cầu) cung cấp chuẩn mực bảo tồn mã nguồn và danh sách nguy cơ (`R03`, `R25`).

### Châu Á (Asia)
- **Nhật Bản — Lưu chiểu luật định và sự biến mất của web cộng đồng:** **Yahoo! GeoCities Japan** (nhánh cuối cùng của GeoCities toàn cầu) đóng cửa ngày 31/03/2019; Archive Team phải chạy chiến dịch khẩn cấp cứu ~96 triệu URL (`R26`, snippet only → `INFERENCE`). Song song, **Thư viện Quốc hội Nhật Bản (NDL)** mở rộng Luật Lưu chiểu điện tử từ 01/01/2023 cho ấn phẩm trả phí/DRM, nhưng vẫn loại trừ blog, tin nhắn ngắn và yêu cầu đồng thuận từng đơn vị cho web tư nhân trên WARP (`R15`, `VERIFIED`).
- **Trung Quốc — Khủng hoảng chi phí vận hành diễn đàn lịch sử:** **Tianya Club** (ra mắt 14/02/1999, từng xếp hạng 11 tại Trung Quốc năm 2015) bị ngừng hoạt động từ 26/04/2023 do nợ phí máy chủ kéo dài và chỉ hoạt động trở lại ngày 02/06/2026 sau 3 năm gián đoạn và xử lý tranh chấp pháp lý dữ liệu (`R19`, `VERIFIED` qua Wikipedia + nguồn SCMP/Leiphone dẫn trực tiếp).
- **Hàn Quốc — Thất bại hồi sinh thương mại & Lưu trữ quốc gia:** **Cyworld** đóng cửa 2019, cố gắng hồi sinh tháng 4/2022 để khôi phục kho ảnh người dùng nhưng không giữ được đà tăng trưởng và phải tạm ngưng dịch vụ giữa năm 2023 (`R20`, `R26`). Ở khu vực công, **Thư viện Quốc gia Hàn Quốc** vận hành hệ thống **OASIS** từ năm 2004 và là thành viên chính thức của IIPC (`R15b`, `R15c`, `VERIFIED`).
- **Singapore:** **National Library Board (NLB)** vận hành Web Archive Singapore (thành viên IIPC, `R15c`) và sửa Luật NLB năm 2019 để thu thập miền `.sg` không cần xin phép trước (`R27c`, snippet only → `INFERENCE`).

### Khu vực khác (Global South / Mỹ Latinh / Châu Phi / Việt Nam)
- **Không tìm thấy bằng chứng trực tiếp định lượng mở trực tiếp (No direct primary evidence opened)** cho các vụ bảo tồn nền tảng nội địa tại Mỹ Latinh, Châu Phi hay Việt Nam trong phạm vi 17 truy vấn của vòng này (chỉ ghi nhận **National Library of Chile** và **Bibliotheca Alexandrina (Ai Cập)** là thành viên chính thức của IIPC trong danh sách `R15c`). Các truy vấn đã chạy tập trung vào NA/EU/Đông Á/Đông Nam Á (Singapore); cần bổ sung truy vấn khu vực Global South ở vòng sau nếu mở rộng phạm vi địa lý.

### Rào cản xuyên văn hóa & chuyển giao quốc tế
1. **Bất đối xứng pháp lý:** Giải pháp dựa trên EU Data Act hoặc DSM Điều 6 không tự động có hiệu lực tại Mỹ (DMCA §1201 chặt) hay Nhật Bản (loại trừ blog/cần phép cho web tư nhân).
2. **Ngôn ngữ & mã hóa ký tự lịch sử:** Nền tảng châu Á thế hệ cũ (Shift-JIS, GBK, EUC-KR) dễ hỏng hiển thị khi lưu trữ hoặc chuyển đổi bằng công cụ thiết kế cho UTF-8 phương Tây.
3. **Chuẩn mực đạo đức khác biệt:** Khái niệm "công khai = tự do lưu trữ" kiểu Thung lũng Silicon xung đột trực tiếp với GDPR châu Âu và nguyên tắc CARE của các cộng đồng bản địa.

---

## 10. Opportunity spaces

*(Lưu ý: Các điểm số tạm thời `provisional_score` tuân thủ chặt chẽ thang neo 0–5 trong `rubric-and-anchors.md`, chỉ dùng để tổng hợp bằng chứng theo từng tiêu chí, KHÔNG phải dự đoán điểm chấm giải và KHÔNG so sánh với ứng viên Phase 2.)*

---

### A-O1: Bảo tồn khả năng tái lập & tĩnh hóa ứng dụng web học thuật / nhân văn số hậu tài trợ

- **Vấn đề:** Hàng nghìn dịch vụ web tin sinh học và dự án nhân văn số được xây dựng bằng kinh phí nghiên cứu 2–5 năm nhanh chóng chết sau năm thứ 2–3 vì phụ thuộc máy chủ phòng lab, cơ sở dữ liệu và framework lỗi thời, làm đứt gãy khả năng tái lập khoa học và tri thức trích dẫn.
  - **[A-O1-C1] [VERIFIED]:** Trong 3.649 dịch vụ web tin sinh học công bố 1994–2017 trên 375 tạp chí, chỉ 69% (2.522) còn hoạt động; tỷ lệ sống giảm từ >95% (2 năm đầu) xuống 84% (năm thứ 3), chu kỳ bán rã trung bình 10,39 năm (`R05`).
  - **[A-O1-C2] [VERIFIED]:** Trong 14.489 trang web được trích dẫn trên Web of Science (1996–2010), tuổi thọ trung vị là 9,3 năm và chỉ 62% được lưu trữ; chương trình máy tính chiếm 43% tài nguyên bị mất trong MEDLINE (`R07`, `R08`).
  - **[A-O1-C3] [VERIFIED]:** Bộ nguyên tắc Endings Project (UVic) chứng minh loại bỏ phụ thuộc server-side (chỉ giữ HTML5/JS/CSS + dữ liệu nguồn chuẩn mở) giúp dự án sống lâu dài không tốn phí vận hành (`R09`).
- **Người dùng mục tiêu:** Nhóm nghiên cứu tin sinh học/khoa học tính toán, học giả nhân văn số (DH), thư viện đại học & quản trị kho lưu trữ học thuật (Institutional Repositories).
- **Chiều bảo tồn:** `software`, `knowledge`, `content`.
- **Vì sao bây giờ (Why now):** Dịch vụ lưu trữ trích dẫn **WebCite** đã ngừng hoạt động từ 6/2023 (`R27d`); chuẩn đóng gói **WACZ 1.1.1** (`R17`) và WebAssembly/tĩnh hóa phía trình duyệt đã trưởng thành, cho phép biến nhiều ứng dụng web động quy mô vừa thành gói tĩnh tự chạy không cần máy chủ.
- **Giải pháp thay thế mạnh nhất:** The Endings Project (UVic) + Webrecorder/Browsertrix (WACZ) + Zenodo/Software Heritage.
- **Phản chứng mạnh nhất:** Nghiên cứu Wren et al. (2017, `R06`) cho thấy 94% tài nguyên khoa học được trích dẫn nhiều nhất tự di dời sang URL mới thành công (so với 34% ở nhóm không được trích dẫn) — nghĩa là một phần lớn web app chết có giá trị sử dụng thực tế thấp. Ngoài ra, các máy chủ tin sinh học cần tính toán nặng phía server không thể tĩnh hóa thuần túy.
- **Bằng chứng theo tiêu chí Candidate Rubric:**
  - `demand` (20%): **4/5 (H)** — Bằng chứng định lượng peer-reviewed mạnh về quy mô vấn đề (`R05`, `R06`, `R07`, `R08`) và hành vi thực của thư viện/UVic (`R09`), nhưng chưa có khảo sát trực tiếp xác nhận nhóm nghiên cứu sẵn sàng đổi quy trình để dùng công cụ mới (`A-O1-C1`, `VERIFIED`).
  - `international` (15%): **5/5 (H)** — 375 tạp chí quốc tế và 14.489 URL Web of Science trải khắp Bắc Mỹ, Châu Âu và Châu Á; thư viện đại học toàn cầu dùng chung chuẩn DOI/FAIR (`R05`, `R08`, `R09`, `VERIFIED`).
  - `innovation` (15%): **3/5 (M)** — Endings Project đòi hỏi thiết kế lại từ đầu, còn Browsertrix/WACZ chỉ chụp giao diện mà không giữ tương tác tính toán; khoảng trống "chuyển đổi hậu kỳ từ web app động sang gói tĩnh/WASM có kiểm chứng" là hợp lý nhưng chưa chứng minh hết độ phủ (`R09`, `R17`, `INFERENCE`).
  - `theme` (15%): **3/5 (M)** — Gắn với công nghệ/dịch vụ đã chính thức ngừng (WebCite 6/2023, các web server khoa học/framework cũ chết), nhưng thiên về "hồi sinh quy trình/nền tảng học thuật" hơn là một sản phẩm công nghệ đơn lẻ nổi tiếng (`INFERENCE`).
  - `ai` (10%): **3/5 (M)** — AI hữu ích trong phân tích mã nguồn/phụ thuộc để sinh bản tĩnh hóa và kiểm tra hồi quy, nhưng nhiều phần có thể làm bằng phân tích tĩnh truyền thống (`HYPOTHESIS`).
  - `feasibility` (10%): **4/5 (M)** — Hoàn toàn khả thi trong ≤7 ngày với phạm vi thu hẹp (ví dụ: tĩnh hóa + đóng gói WACZ/WASM cho một loại ứng dụng web học thuật mã nguồn mở cụ thể, dùng dữ liệu công khai hợp pháp).
  - `demo` (10%): **4/5 (M)** — Trước/sau rõ ràng (một web app học thuật cũ bị hỏng dependency/server → gói tĩnh tự chạy ngoại tuyến trên trình duyệt), nhưng cần giải thích ngắn bối cảnh học thuật cho giám khảo đại chúng.
  - `sustainability` (5%): **4/5 (M)** — Thư viện đại học, quỹ nghiên cứu công và tạp chí khoa học là bên có ngân sách rõ ràng; rủi ro pháp lý thấp nhờ giấy phép mở (`R09`, `INFERENCE`).
- **Ghi chú khả năng thương mại (Commercial Viability Note):** Bên trả tiền là **thư viện đại học, quỹ tài trợ khoa học (NSF/ERC/Mellon) hoặc nhà xuất bản học thuật** (tương tự mô hình trả phí Archive-It và ngân sách DPC/Endings, `R03`, `R09`, `INFERENCE`). Rào cản chính: chu kỳ mua sắm chậm của khu vực học thuật và thiếu cơ chế bắt buộc từ tạp chí khoa học.
- **Giả thuyết cốt lõi:** (H1) Một tỷ lệ đáng kể (≥30%) web app học thuật/DH đã chết hoặc sắp hết grant có thể chuyển sang dạng tĩnh/client-side mà vẫn giữ chức năng cốt lõi; (H2) Thư viện đại học sẵn sàng chạy công cụ đóng gói tự động trước khi tắt máy chủ phòng lab.
- **Thí nghiệm bác bỏ nhỏ nhất (Smallest Falsifying Experiment):** Chọn ngẫu nhiên 20 dự án web học thuật/DH mã nguồn mở sắp hết bảo trì (hoặc mới chết có mã trên GitHub/Software Heritage), thử chuyển đổi bán tự động sang bản tĩnh/client-side trong 48 giờ; nếu <25% giữ được công năng cốt lõi do phụ thuộc nặng vào backend/CSDL lớn, loại bỏ hướng tĩnh hóa đại trà.

---

### A-O2: Khôi phục cấu trúc quan hệ & ngữ cảnh quy trình từ gói xuất dữ liệu SaaS / nền tảng đóng cửa

- **Vấn đề:** Khi SaaS thương mại (như InVision 12/2024) hoặc instance mạng xã hội phân tán (Mastodon/ActivityPub) đóng cửa, ngay cả khi người dùng tải được gói xuất dữ liệu hợp pháp (JSON, CSV, Activity Streams 2.0, ZIP), dữ liệu bị "phẳng hóa": mất mối quan hệ giữa các đối tượng, bình luận, luồng hội thoại và không thể nhập lại hoặc sử dụng như một không gian làm việc sống.
  - **[A-O2-C1] [VERIFIED]:** **EU Data Act** (Regulation 2023/2854) chính thức áp dụng từ 12/09/2025, trao quyền pháp lý chuyển đổi giữa các nhà cung cấp dịch vụ xử lý dữ liệu/cloud, kèm điều khoản hợp đồng mẫu (SCCs) (`R02`).
  - **[A-O2-C2] [VERIFIED]:** Tài liệu chính thức của **Mastodon** xác nhận không thể nhập lại bài viết và media sau khi di chuyển sang server khác do giới hạn kỹ thuật; bản xuất chỉ là tệp Activity Streams 2.0 JSON tĩnh (`R10`).
  - **[A-O2-C3] [VERIFIED]:** **Data Transfer Initiative (DTI)** xác nhận Data Transfer Project mới kết nối hơn chục dịch vụ lớn với mô hình chuẩn hóa đơn giản và đang phải xây chuẩn mới cho lịch sử AI (AI Conversation Schema) (`R16`); phân tích kỹ thuật chỉ ra DTP không bảo toàn lược đồ quan hệ và ràng buộc toàn vẹn (`R24`, snippet only → `INFERENCE`).
  - **[A-O2-C4] [INFERENCE]:** **InVision** đóng cửa toàn bộ dịch vụ thiết kế/prototype ngày 31/12/2024 và xóa vĩnh viễn dữ liệu chưa xuất; người dùng phải tự xây lại dự án từ tệp gốc trên Figma/Penpot (`R23`, snippet only).
- **Người dùng mục tiêu:** Nhóm sản phẩm/thiết kế & doanh nghiệp SME phụ thuộc SaaS cộng tác; người dùng/quản trị viên Fediverse (Mastodon) bị đóng instance; cá nhân cần bảo toàn và tái sử dụng lịch sử công việc/AI khi đổi nền tảng.
- **Chiều bảo tồn:** `user-data-workflows`, `content`, `knowledge`.
- **Vì sao bây giờ (Why now):** Sự cộng hưởng giữa **EU Data Act có hiệu lực 9/2025** (và mốc cấm phí chuyển đổi 1/2027, `R02`), làn sóng đóng cửa SaaS hậu ZIRP (InVision, Cohost) và sáng kiến chuẩn hóa mới của DTI năm 2026 (`R16`).
- **Giải pháp thay thế mạnh nhất:** Data Transfer Project (DTI), công cụ import chính chủ của đối thủ dẫn đầu (Figma, Miro, Notion), và các script chuyển đổi đơn lẻ trên GitHub.
- **Phản chứng mạnh nhất:** Đối với các SaaS phổ biến nhất, đối thủ thương mại hàng đầu có động lực rất mạnh để tự xây bộ nhập miễn phí nhằm giành khách hàng (ví dụ Miro mua lại Freehand của InVision, `R23`). Ngoài ra, gói xuất từ nền tảng đóng cửa thường bị thiếu trường dữ liệu nội bộ, làm giới hạn độ trung thực dù công cụ tái tạo có tốt đến đâu.
- **Bằng chứng theo tiêu chí Candidate Rubric:**
  - `demand` (20%): **4/5 (M)** — Bằng chứng quy định rõ ràng (EU Data Act, `R02`), độ phổ biến mã nguồn mở cao (DTP 3.626 sao, `R16b`), và hành vi di chuyển thực trên Mastodon/InVision (`R10`, `R23`), nhưng thiếu số liệu khảo sát trả phí trực tiếp cho một công cụ tái tạo đa nền tảng (`A-O2-C1`, `VERIFIED`; `A-O2-C4`, `INFERENCE`).
  - `international` (15%): **5/5 (H)** — EU Data Act áp dụng cho mọi nhà cung cấp phục vụ khách hàng tại EU bất kể trụ sở (`R02`); DTI hoạt động tại Bắc Mỹ/toàn cầu (`R16`); Mastodon và SaaS cộng tác được dùng rộng rãi tại NA, EU và Châu Á (`VERIFIED`).
  - `innovation` (15%): **4/5 (M)** — Khoảng trống rõ ràng giữa "file export JSON phẳng" (DTP/Takeout/Mastodon) và "đồ thị dữ liệu có quan hệ + khả năng duyệt/chuyển tiếp" (`R10`, `R16`, `R24`, `INFERENCE`).
  - `theme` (15%): **3/5 (M)** — Đạt ngưỡng cổng nếu neo trực tiếp vào gói xuất của một nền tảng đã chính thức đóng cửa (ví dụ Cohost 01/2025 hoặc InVision 12/2024), nhưng cần tránh biến thành công cụ ETL chung chung thiếu chất Resurrection (`INFERENCE`).
  - `ai` (10%): **4/5 (M)** — AI đóng vai trò cốt lõi trong suy luận lược đồ không có tài liệu và ánh xạ thực thể/quan hệ từ gói export dị thể, có thể kiểm chứng bằng oracle toàn vẹn tham chiếu (0 bản ghi mồ côi, bảo toàn 100% trường dữ liệu) (`HYPOTHESIS`).
  - `feasibility` (10%): **5/5 (H)** — Có thể xây lát cắt hoạt động hoàn chỉnh trong ≤7 ngày trên dữ liệu xuất thực hợp pháp (ví dụ gói xuất Mastodon Activity Streams 2.0 hoặc gói xuất Cohost công khai).
  - `demo` (10%): **5/5 (H)** — Demo <3 phút cực kỳ trực quan cho giám khảo quốc tế: nạp một file ZIP/JSON xuất "chết" không đọc được → khôi phục thành không gian tri thức/luồng tương tác đầy đủ liên kết và xuất sang chuẩn mở.
  - `sustainability` (5%): **4/5 (M)** — Mô hình B2B SaaS tuân thủ EU Data Act / dịch vụ chuyển đổi trả phí một lần hoặc mã nguồn mở có tài trợ DTI/doanh nghiệp; rủi ro pháp lý ở mức trung bình nếu xử lý dữ liệu nhóm có nhiều tác giả (`R02`, `INFERENCE`).
- **Ghi chú khả năng thương mại (Commercial Viability Note):** Bên trả tiền là **doanh nghiệp SME/đội ngũ sản phẩm** cần chuyển dữ liệu khi SaaS tăng giá hoặc đóng cửa, và **nhà cung cấp SaaS tại EU** cần tuân thủ Chương VI EU Data Act trước mốc 12/01/2027 (`R02`, `INFERENCE`). Rào cản chính: các ông lớn đích đến thường tự xây importer miễn phí cho đối thủ lớn nhất, nên chỉ bền vững ở phân khúc đuôi dài (long-tail SaaS) hoặc định dạng chuẩn chung.
- **Giả thuyết cốt lõi:** (H1) AI + kiểm chứng lược đồ có thể khôi phục ≥90% liên kết quan hệ (bài viết–bình luận–media–thẻ) từ ≥3 định dạng gói xuất thực mà không cần viết parser thủ công toàn bộ; (H2) Người dùng/nhóm thực sự cần mở lại ngữ cảnh tương tác chứ không chỉ lưu trữ file ZIP lạnh.
- **Thí nghiệm bác bỏ nhỏ nhất (Smallest Falsifying Experiment):** Lấy 3 gói xuất thực tế (Mastodon Activity Streams 2.0, Cohost export, và 1 gói xuất SaaS công khai), kiểm tra xem tỷ lệ liên kết quan hệ có bị mất ngay từ đầu trong file xuất hay không; nếu bản thân file xuất gốc đã cắt bỏ ID tham chiếu khiến không thể khôi phục >50% ngữ cảnh, giả thuyết bị bác bỏ.

---

### A-O3: Tự động hóa nhận diện và cấu hình môi trường giả lập cho kho phần mềm tại thư viện/bảo tàng

- **Vấn đề:** Các thư viện và bảo tàng lưu giữ hàng nghìn phần mềm born-digital (phần mềm giáo dục, CAD, tác phẩm tương tác, trò chơi lịch sử), nhưng việc dựng môi trường giả lập để chạy lại chúng cực kỳ tốn nhân lực chuyên gia do thiếu thông tin cấu hình chính xác và tài liệu giả lập sai lệch.
  - **[A-O3-C1] [VERIFIED]:** Nghiên cứu tình huống chính thức của **SPN/EaaSI** tại Phòng Thí nghiệm Bảo tồn Born-Digital của Thư viện Đại học Stanford cho thấy 2 chuyên gia lưu trữ + chuyên viên EaaSI mất **2 ngày làm việc thủ công** chỉ để thử-sai và chạy được 1 phần mềm Macintosh năm 1985 (*The Would-Be Gentleman*), trong đó tài liệu trang chủ BasiliskII còn ghi sai khả năng tương thích OS (`R11`).
  - **[A-O3-C2] [VERIFIED]:** **DPC Global Bit List** xếp phần mềm và trò chơi bị ngừng hỗ trợ vào nhóm nguy cơ tuyệt chủng cực cao (`R03`, `R27a`).
  - **[A-O3-C3] [VERIFIED]:** Quy tắc cuối cùng **DMCA Section 1201** (28/10/2024) gia hạn miễn trừ bảo tồn tại chỗ cho thư viện/bảo tàng, nhưng **từ chối** mở rộng quyền truy cập từ xa cho nghiên cứu viên (`R04`, `R21`).
- **Người dùng mục tiêu:** Thư viện đại học, bảo tàng, viện lưu trữ quốc gia (thành viên SPN, EaaSI, DPC, IIPC).
- **Chiều bảo tồn:** `software`, `heritage`.
- **Vì sao bây giờ (Why now):** EaaSI đang chuyển giao quản trị sang Yale Library (2026) để mở rộng ứng dụng trong mạng lưới thư viện (`R27i`, snippet only), đồng thời khối lượng tài sản phần mềm cũ cần xử lý vượt xa nhân lực lưu trữ (phòng lab Stanford chỉ có 2 nhân sự, `R11`).
- **Giải pháp thay thế mạnh nhất:** EaaSI (cấu hình thủ công bởi chuyên viên) và Internet Archive Software Collection (cấu hình sẵn cho tập phần mềm đại chúng).
- **Phản chứng mạnh nhất:** Thị trường GLAM rất hẹp và ngân sách phụ thuộc tài trợ quỹ (Mellon/Sloan/IMLS, `R11`); đồng thời, việc U.S. Copyright Office từ chối truy cập từ xa tháng 10/2024 (`R04`, `R21`) khiến nhiều thư viện khó chứng minh ROI khi chỉ phục vụ được người đọc đến tận nơi.
- **Bằng chứng theo tiêu chí Candidate Rubric:**
  - `demand` (20%): **3/5 (H)** — Bằng chứng sơ cấp sắc nét về điểm nghẽn lao động tại Stanford Libraries (`R11`) và đầu tư thể chế vào EaaSI/SPN, nhưng tập khách hàng rất nhỏ và chưa có bằng chứng sẵn sàng mua phần mềm thương mại mới (`A-O3-C1`, `VERIFIED`).
  - `international` (15%): **4/5 (M)** — Mạng lưới DPC/IIPC/SPN trải khắp Bắc Mỹ, Châu Âu và Úc (`R03`, `R11`, `R15c`); tại Châu Á bằng chứng cụ thể về triển khai EaaSI còn hạn chế (`INFERENCE`).
  - `innovation` (15%): **4/5 (M)** — Chưa có hệ thống tự động hóa việc ghép cặp "tài liệu + ảnh đĩa cũ → tổ hợp emulator/OS/driver + tự kiểm thử boot" tích hợp vào quy trình EaaSI (`R11`, `INFERENCE`).
  - `theme` (15%): **5/5 (H)** — Khớp trực tiếp định nghĩa Resurrection: hồi sinh phần mềm/hệ điều hành đã chết bằng công nghệ hiện đại (`VERIFIED`).
  - `ai` (10%): **4/5 (M)** — AI đọc tài liệu hướng dẫn cũ/metadata đĩa, đề xuất cấu hình giả lập và chạy vòng thử nghiệm có oracle xác định (khởi động thành công, không treo/crash) (`HYPOTHESIS`).
  - `feasibility` (10%): **3/5 (M)** — Khả thi nếu giới hạn trên 1–2 họ giả lập mở (ví dụ DOSBox/v86 hoặc BasiliskII chạy trên WASM/Docker), nhưng có rủi ro về bản quyền ảnh đĩa OS gốc (ROM/MacOS/Windows cũ).
  - `demo` (10%): **5/5 (H)** — Demo cực mạnh: thả 1 ảnh đĩa + file PDF manual năm 1985 → hệ thống tự phân tích, chọn cấu hình và khởi chạy phần mềm sống ngay trong trình duyệt.
  - `sustainability` (5%): **3/5 (M)** — Chỉ khả thi theo mô hình công cụ mã nguồn mở tích hợp vào hạ tầng EaaSI/SPN được tài trợ thể chế, không phù hợp mô hình startup VC (`R11`, `INFERENCE`).
- **Ghi chú khả năng thương mại (Commercial Viability Note):** Không có thị trường thương mại B2C; nguồn tài trợ khả thi là **quỹ học thuật/di sản (Mellon, Sloan, IMLS, EU Horizon) hoặc hợp đồng dịch vụ với liên minh thư viện** (`R11`, `VERIFIED` về nguồn tài trợ EaaSI). Rào cản chính: quy mô thị trường nhỏ và rào cản bản quyền truy cập từ xa tại Mỹ (`R04`).
- **Giả thuyết cốt lõi:** (H1) Tự động hóa đọc tài liệu + thử-sai sandbox có thể rút thời gian dựng môi trường giả lập từ nhiều giờ/ngày xuống dưới 30 phút cho ≥60% phần mềm DOS/Mac/Windows cổ; (H2) Lưu trữ viên có thể dùng kết quả mà không cần chuyên sâu về từng emulator.
- **Thí nghiệm bác bỏ nhỏ nhất (Smallest Falsifying Experiment):** Lấy 15 phần mềm cổ công khai/shareware (DOS/Win3.1/Mac 68k) kèm file README/manual, đo thời gian và tỷ lệ khởi chạy thành công không lỗi của quy trình tự động so với cấu hình mặc định; nếu tỷ lệ thành công <50% hoặc không vượt trội hơn bộ cấu hình định sẵn của DOSBox/Internet Archive, hướng này không đủ khác biệt.

---

### A-O4: Khung chuyển giao End-of-Life (EOL) và đóng gói tự vận hành cho nền tảng trực tuyến / live-service

- **Vấn đề:** Hàng triệu người dùng và cộng đồng bị tước quyền sử dụng hoặc mất toàn bộ không gian tương tác khi nhà phát hành tắt máy chủ xác thực/backend (game online-only, nền tảng xã hội độc lập), buộc cộng đồng phải bỏ hàng nghìn giờ đảo ngược giao thức trong vùng xám pháp lý mà vẫn mất toàn bộ dữ liệu tài khoản gốc.
  - **[A-O4-C1] [VERIFIED]:** Sáng kiến Công dân châu Âu **Stop Destroying Videogames** (`ECI(2024)000007`) thu được **1.294.188 chữ ký hợp lệ** toàn EU; ngày 16/06/2026 Ủy ban châu Âu ban hành phản hồi `C(2026)4110` từ chối lập pháp bắt buộc nhưng cam kết cùng ngành xây dựng bộ quy tắc ứng xử EOL cuối năm 2026 (`R01`, `R21b`).
  - **[A-O4-C2] [VERIFIED]:** Sau khi Nintendo tắt dịch vụ 3DS/Wii U (4/2024), cộng đồng **Pretendo Network** phải tự xây 170 kho mã nguồn mở để tái tạo server bằng kỹ thuật đảo ngược sạch, nhưng người dùng buộc phải mod máy và **không thể giữ tài khoản NNID cũ** (`R12`, `R13`).
  - **[A-O4-C3] [VERIFIED]:** Các nền tảng cộng đồng lớn cũng sụp đổ vì chi phí server cố định: **Cohost** đóng cửa 12/01/2025 (`R18`); **Tianya Club** (Trung Quốc) ngắt kết nối 3 năm (4/2023 – 6/2026) vì nợ phí trung tâm dữ liệu (`R19`).
- **Người dùng mục tiêu:** Cộng đồng bảo tồn mã nguồn mở (như Pretendo), nhà phát hành game/nền tảng độc lập tại EU cần tuân thủ bộ quy tắc ứng xử EOL tự nguyện, và quản trị viên nền tảng cộng đồng sắp ngừng vận hành.
- **Chiều bảo tồn:** `operational`, `community`, `software`.
- **Vì sao bây giờ (Why now):** Phản hồi của Ủy ban châu Âu ngày 16/06/2026 (`R01`, `R21b`) tạo áp lực chính trị–uy tín lên ngành game/nền tảng tại châu Âu vào cuối năm 2026 để chứng minh khả năng thực hiện EOL tự nguyện mà không tốn kém quá mức.
- **Giải pháp thay thế mạnh nhất:** Cộng đồng tự đảo ngược giao thức sau khi tắt server (Pretendo, Wiimmfi) hoặc nhà phát hành tự viết bản vá offline thủ công.
- **Phản chứng mạnh nhất:** Phản đối gay gắt từ ngành công nghiệp game (ESA tại Mỹ, các hãng phát hành tại EU) và chính quyết định **từ chối ban hành luật bắt buộc** của Ủy ban châu Âu tháng 6/2026 (`R01`, `R21b`) chứng minh các nhà phát hành không có động lực kinh tế tự nguyện đầu tư cho công cụ EOL, do vướng bản quyền middleware bên thứ ba và chi phí bảo mật.
- **Bằng chứng theo tiêu chí Candidate Rubric:**
  - `demand` (20%): **5/5 (H)** — Bằng chứng hành vi sơ cấp quy mô lớn nhất trong toàn báo cáo: 1.294.188 chữ ký xác thực ECI (`R01`), 170 repo GitHub hoạt động trên Pretendo (`R13`), và khủng hoảng thực tế ở Cohost/Tianya (`R18`, `R19`) (`A-O4-C1`, `A-O4-C2`, `VERIFIED`).
  - `international` (15%): **5/5 (H)** — Bằng chứng trực tiếp tại Châu Âu (ECI toàn EU, `R01`), Bắc Mỹ (Cohost, DMCA §1201, `R04`, `R18`) và Châu Á (Nintendo Nhật Bản, Tianya Trung Quốc, `R12`, `R19`, `VERIFIED`).
  - `innovation` (15%): **3/5 (M)** — Chưa có chuẩn/công cụ đóng gói EOL nhẹ cho nhà phát hành nhỏ, nhưng thách thức lớn nhất nằm ở **pháp lý và động lực kinh doanh**, không chỉ ở công nghệ (`INFERENCE`).
  - `theme` (15%): **4/5 (H)** — Gắn chặt với các dịch vụ trực tuyến đã bị khai tử (Nintendo Network 3DS/Wii U, Cohost) và việc hồi sinh khả năng vận hành độc lập (`VERIFIED`).
  - `ai` (10%): **1/5 (H)** — AI **không cần thiết** cho bài toán cốt lõi (pháp lý, quản trị, tách phụ thuộc kiến trúc); cố nhét AI vào sẽ là AI trang trí (`INFERENCE`).
  - `feasibility` (10%): **2/5 (M)** — Khó chứng minh tính khả thi thực tế trong 7 ngày vì phụ thuộc vào hợp tác của nhà phát hành (không có trong tay) hoặc vướng DRM/EULA nếu làm từ phía bên thứ ba (`R01`, `R04`, `INFERENCE`).
  - `demo` (10%): **3/5 (M)** — Có thể demo chuyển đổi một ứng dụng client–server mẫu sang chế độ tự vận hành, nhưng khó dùng nền tảng thương mại thực tế do rào cản pháp lý.
  - `sustainability` (5%): **1/5 (H)** — Rủi ro pháp lý cao (DMCA §1201, IP middleware) và chưa rõ ai trả tiền sau khi nhà phát hành ngừng hỗ trợ (`R01`, `R04`, `VERIFIED`).
- **Ghi chú khả năng thương mại (Commercial Viability Note):** Đây là ví dụ điển hình của **nhu cầu người dùng cực cao (5/5) nhưng khả năng thương mại hóa rất yếu**: người chơi đòi hỏi quyền tiếp tục chơi nhưng không muốn trả thêm tiền; nhà phát hành coi EOL là chi phí thuần túy (`R01`, `R21b`, `INFERENCE`). Rào cản chính: không có luật bắt buộc từ EC và rủi ro pháp lý cao nếu thực hiện từ phía cộng đồng.
- **Giả thuyết cốt lõi:** (H1) Các studio indie/nền tảng vừa tại EU sẵn sàng áp dụng bộ chuẩn/công cụ đóng gói EOL để hưởng lợi uy tín theo Bộ quy tắc ứng xử EC 2026–2027 nếu chi phí tích hợp <2 ngày công; (H2) Người chơi sẵn sàng trả phí nhỏ hoặc tài trợ cộng đồng cho chế độ self-host hợp pháp.
- **Thí nghiệm bác bỏ nhỏ nhất (Smallest Falsifying Experiment):** Phỏng vấn có cấu trúc 10 studio indie/nhà vận hành nền tảng độc lập (EU/NA) về điều kiện áp dụng bộ quy tắc EOL của EC; nếu ≥8/10 từ chối tích hợp ngay cả khi công cụ miễn phí vì sợ rủi ro pháp lý middleware/bảo mật, loại bỏ hướng B2B-cho-nhà-phát-hành.

---

### A-O5: Bảo tồn di sản web & tri thức cộng đồng có kiểm soát đồng thuận và chủ quyền dữ liệu

- **Vấn đề:** Các công cụ lưu trữ web truyền thống vận hành theo mô hình "cào công khai và phát hành rộng rãi", nhưng mô hình này ngày càng bất khả thi về pháp lý và đạo đức đối với cộng đồng địa phương, cộng đồng bản địa và nội dung cá nhân trên các nền tảng sắp đóng cửa (blog, diễn đàn, mạng xã hội), dẫn đến hai thái cực xấu: hoặc **mất trắng di sản**, hoặc **vi phạm quyền riêng tư/bản quyền/chủ quyền văn hóa**.
  - **[A-O5-C1] [VERIFIED]:** Tại Nhật Bản, **Luật NDL** loại trừ blog và bài đăng ngắn khỏi diện lưu chiểu bắt buộc, đồng thời bắt buộc xin đồng thuận từng chủ sở hữu cho web tư nhân trên WARP và giới hạn xem tại chỗ (`R15`).
  - **[A-O5-C2] [VERIFIED]:** Tại EU, **GDPR Điều 89** yêu cầu các biện pháp bảo vệ (tối thiểu hóa dữ liệu, giả danh hóa) cho hoạt động lưu trữ vì lợi ích công, tạo ranh giới chặt với quyền xóa dữ liệu cá nhân (`R13b`).
  - **[A-O5-C3] [VERIFIED]:** Tại Mỹ, kết cục vụ **Hachette v. Internet Archive** (12/2024, `R19c`) khẳng định bảo tồn công cộng không thể dựa tràn lan vào Fair Use; trên toàn cầu, **GIDA (CARE Principles)** và **DPC Bit List** nhấn mạnh quyền kiểm soát tập thể của cộng đồng đối với dữ liệu di sản của chính họ (`R03`, `R14e`).
- **Người dùng mục tiêu:** Nhóm lưu trữ cộng đồng độc lập (community archives), tổ chức bảo tồn văn hóa bản địa/thiểu số, thư viện địa phương & quốc gia vận hành chương trình thu thập có phép (như NDL WARP, NLK OASIS).
- **Chiều bảo tồn:** `heritage`, `community`, `content`.
- **Vì sao bây giờ (Why now):** Hội tụ của 3 cú sốc pháp lý–đạo đức 2024–2026: *Hachette v. IA* kết thúc (12/2024), DPC Bit List 2025 xếp nội dung cộng đồng nghệ thuật/di sản ở mức *Critically Endangered* (`R03`, `R27a`), và sự gia tăng xung đột về việc AI tự do cào dữ liệu di sản cộng đồng (GIDA 2026 IDSov & AI Workshop, `R14e`).
- **Giải pháp thay thế mạnh nhất:** **Mukurtu CMS** (quản trị di sản bản địa có phân quyền văn hóa), **Webrecorder/WACZ** (lưu trữ cục bộ có kiểm soát), và chương trình thu thập có chọn lọc của thư viện quốc gia (NDL WARP, NLK OASIS).
- **Phản chứng mạnh nhất:** Quy trình xin đồng thuận (opt-in) tốn cực nhiều nhân lực và cho độ phủ rất thấp — chính vì lý do này mà Singapore đã sửa Luật NLB năm 2019 để **bỏ** yêu cầu xin phép bằng văn bản trước đối với miền `.sg` (`R27c`). Do đó, mô hình đặt đồng thuận làm trung tâm khó đạt quy mô lớn nếu không gắn với một cộng đồng có tổ chức chặt chẽ sẵn.
- **Bằng chứng theo tiêu chí Candidate Rubric:**
  - `demand` (20%): **3/5 (M)** — Bằng chứng thể chế và pháp lý mạnh tại cả 3 khu vực (`R03`, `R13b`, `R14e`, `R15`), nhưng chưa có bằng chứng định lượng rằng các cộng đồng địa phương sẵn sàng chi tiền hoặc tự vận hành một công cụ mới ngoài Mukurtu/WACZ (`A-O5-C1`, `VERIFIED`).
  - `international` (15%): **5/5 (H)** — Bằng chứng trực tiếp từ Nhật Bản (NDL WARP, `R15`), Hàn Quốc/Singapore (OASIS/WAS, `R15b`, `R15c`), EU (GDPR Art. 89, `R13b`), và mạng lưới toàn cầu GIDA/DPC (`R03`, `R14e`, `VERIFIED`).
  - `innovation` (15%): **3/5 (M)** — Mukurtu đã giải quyết phân quyền văn hóa cho tài sản tĩnh, còn WACZ giải quyết đóng gói web; khoảng trống nằm ở quy trình "thu thập nền tảng sắp đóng cửa + kiểm toán đồng thuận/PII tự động + đóng gói phân quyền", nhưng cần chứng minh khác biệt rõ với Mukurtu + Browsertrix (`INFERENCE`).
  - `theme` (15%): **2/5 (M)** — **Cảnh báo cổng (Gate < 3):** Hướng này thiên về quản trị lưu trữ và đạo đức dữ liệu nói chung, **thiếu một công nghệ đã chết cụ thể** làm trung tâm của sản phẩm và bản demo theo đúng tiêu chí Resurrection trong `rubric-and-anchors.md` (`INFERENCE`).
  - `ai` (10%): **3/5 (M)** — AI hữu ích trong phát hiện PII/nội dung nhạy cảm đa ngữ để hỗ trợ ẩn danh hóa theo GDPR Điều 89 (human-in-the-loop), nhưng có thể thay một phần bằng luật/NER truyền thống (`HYPOTHESIS`).
  - `feasibility` (10%): **4/5 (M)** — Có thể dựng quy trình đóng gói WACZ kèm lọc PII và lớp kiểm soát quyền truy cập trong ≤7 ngày với dữ liệu mẫu hợp pháp.
  - `demo` (10%): **3/5 (M)** — Demo lọc PII và phân quyền truy cập trên gói lưu trữ web khả thi, nhưng giá trị mang tính chính sách/tuân thủ nên cần giải thích ngữ cảnh cho giám khảo.
  - `sustainability` (5%): **3/5 (M)** — Khả thi theo mô hình tài trợ văn hóa/thư viện công/NGO; hành lang pháp lý rõ ràng và an toàn hơn hẳn mô hình cào đại trà (`R13b`, `R15`, `INFERENCE`).
- **Ghi chú khả năng thương mại (Commercial Viability Note):** Nguồn tài trợ chủ yếu là **ngân sách thư viện công, tổ chức văn hóa, quỹ phi lợi nhuận và chương trình bảo tồn di sản** (tương tự Mukurtu, DPC, NDL, `R03`, `R15`, `INFERENCE`). Rào cản chính: ngân sách cộng đồng nhỏ lẻ và gánh nặng thủ công của quy trình xin đồng thuận.
- **Giả thuyết cốt lõi:** (H1) Tự động hóa khâu nhận diện PII và tạo biên bản đồng thuận theo gói (collection-level) giúp giảm ≥70% thời gian kiểm duyệt pháp lý so với xin phép/lọc thủ công; (H2) Các cộng đồng trực tuyến sắp mất nền tảng ưu tiên lưu trữ có phân quyền thay vì công khai toàn bộ trên Wayback Machine.
- **Thí nghiệm bác bỏ nhỏ nhất (Smallest Falsifying Experiment):** Khảo sát 15 quản trị viên cộng đồng/lưu trữ viên (thuộc các mạng lưới DPC/community archives hoặc diễn đàn sắp đóng) với 2 lựa chọn: (a) đưa toàn bộ lên Wayback Machine/WACZ công khai miễn phí, hay (b) dùng quy trình lọc PII + phân quyền đồng thuận tốn thêm 2 giờ thiết lập; nếu >80% chọn (a) hoặc không quan tâm đến phân quyền, giả thuyết nhu cầu bị bác bỏ.

---

## 11. Challenges to the mission hypothesis

Câu hỏi trung tâm của Task B là:
> *"Can we preserve the value created by digital platforms even when the original platforms can no longer survive?"*

Dựa trên bằng chứng trực tiếp thu thập được, giả thuyết này có **4 điểm yếu cấu trúc cần phản biện thẳng thắn**:

1. **Đánh đồng "dữ liệu/phần mềm của nền tảng" với "giá trị của nền tảng":** Giá trị của nhiều nền tảng số (như mạng xã hội Cohost, Cyworld hay diễn đàn Tianya) nằm ở **hiệu ứng mạng đang sống** — sự tương tác thời gian thực giữa con người với nhau. Khi nền tảng chết, việc lưu lại bản chụp tĩnh hoặc khôi phục ảnh cũ (như Cyworld 2022–2023, `R20`) **không khôi phục được cộng đồng**; giá trị còn lại chỉ là giá trị *lưu trữ lịch sử*, nhỏ hơn rất nhiều so với giá trị vận hành ban đầu.
2. **Giả định ngầm rằng mọi nền tảng biến mất đều đáng bảo tồn:** Bằng chứng từ Wren et al. (2017, `R06`) cho thấy 94% tài nguyên khoa học được trích dẫn nhiều tự sống sót qua di dời URL, trong khi phần lớn tài nguyên chết thuộc nhóm ít hoặc không được dùng. Bảo tồn không chọn lọc tạo ra gánh nặng chi phí và rác dữ liệu.
3. **Bỏ qua rào cản pháp lý–kinh tế như nguyên nhân gốc thực sự:** Trong hai trường hợp có nhu cầu xã hội lớn nhất — sách số (*Hachette v. IA*, `R19c`) và game online-only (*Stop Destroying Videogames*, `R01`; DMCA §1201, `R04`) — **vấn đề không phải là không biết cách bảo tồn về mặt kỹ thuật**, mà là **luật bản quyền và mô hình kinh doanh ngăn cản việc bảo tồn/truy cập hợp pháp**. Công nghệ mới không thể tự mình vượt qua bức tường pháp lý này.
4. **Cạm bẫy bền vững của "Operational Continuity":** Cố gắng duy trì một nền tảng đã chết ở trạng thái chạy sống (server 24/7, kiểm duyệt, bảo mật) gần như chắc chắn lặp lại chính thất bại kinh tế đã giết chết nền tảng gốc (`R18`, `R19`). Con đường thực tế hơn nhiều là **tách giá trị khỏi nền tảng**: chuyển sang gói tĩnh không cần server (`R09`, `R17`) hoặc chuyển hóa dữ liệu sang định dạng mở có thể dùng trong công cụ đang sống (`R02`, `R16`).

---

## 12. Unresolved questions

1. **Hiệu lực thực thi thực tế của EU Data Act (Chương VI) với SaaS cộng tác:** Luật đã áp dụng từ 12/09/2025 (`R02`), nhưng mức độ đầy đủ ngữ nghĩa (semantic completeness) của các gói xuất SaaS thực tế trong năm 2025–2026 như thế nào? Chưa có kiểm định thực nghiệm độc lập trên các SaaS phổ biến.
2. **Nội dung chi tiết Bộ quy tắc ứng xử EOL của Ủy ban châu Âu cuối năm 2026:** EC cam kết đối thoại với ngành game sau phản hồi ngày 16/06/2026 (`R01`), nhưng chưa rõ bộ quy tắc này có đưa ra tiêu chuẩn kỹ thuật cụ thể nào hay chỉ dừng ở tuyên bố minh bạch thời hạn hỗ trợ.
3. **Bằng chứng sơ cấp về mức sẵn sàng trả tiền (WTP) của doanh nghiệp SME và thư viện:** Các bằng chứng hiện tại xác nhận rõ vấn đề và chi tiêu cho hạ tầng lớn (Archive-It, EaaSI, DPC), nhưng chưa xác nhận mức WTP cho các công cụ tự động hóa mới (tĩnh hóa web app học thuật, tái tạo gói export SaaS).
4. **Khoảng trống dữ liệu ngoài Bắc Mỹ – Châu Âu – Đông Á:** Chưa có bằng chứng sơ cấp định lượng về tỷ lệ mất mát nền tảng số và mô hình bảo tồn cộng đồng tại Đông Nam Á (ngoài Singapore), Mỹ Latinh và Châu Phi.
5. **Tỷ lệ thực tế web app học thuật có thể tĩnh hóa không mất công năng:** Chưa có nghiên cứu thực nghiệm quy mô lớn đo tỷ lệ giữa web app tin sinh học/DH có thể chuyển sang WASM/static so với nhóm bắt buộc cần cụm tính toán phía server.

---

## 13. References

**Thang điểm Reference-Quality Rubric (0–5 mỗi tiêu chí):**
- `A` = Source Authority (20%), `T` = Technical Evidence (20%), `M` = Mechanism Correctness (20%), `C` = Context Fit (15%), `F` = Freshness (10%), `R` = Reproducibility (10%), `B` = Commercial/Opinion Bias (5%; 5 = không thiên lệch).
- `Weighted` = `0.20*A + 0.20*T + 0.20*M + 0.15*C + 0.10*F + 0.10*R + 0.05*B`.
- **Source Reliability** (độ tin cậy nội tại của nguồn: High/Medium/Low) được tách biệt với **Reference Relevance** (mức liên quan trực tiếp tới khẳng định: High/Medium/Low).

| Ref ID | URL | Title | Publisher | Pub Date | Accessed | Opened Directly / Snippet | Claims | A/T/M/C/F/R/B | Weighted | Source Reliability | Reference Relevance |
|---|---|---|---|---|---|---|---|---|---|---|---|
| R01 | https://register.eci.ec.europa.eu/core/api/register/details/2024/000007 | European Citizens' Initiative ECI(2024)000007 — Stop Destroying Videogames (Official Register JSON) | European Commission | 2026-06-16 | 2026-11-25 | Opened directly | A-G-C5, A-O4-C1 | 5/5/5/5/5/5/5 | 5.00 | High | High |
| R02 | https://digital-strategy.ec.europa.eu/en/policies/data-act | Data Act \| Shaping Europe's digital future | European Commission (DG CONNECT) | 2026-11-23 | 2026-11-25 | Opened directly | A-G-C9, A-O2-C1 | 5/4/5/5/5/5/5 | 4.80 | High | High |
| R03 | https://www.dpconline.org/digipres/champion-digital-preservation/bit-list | DPC Global 'Bit List' of Digital Materials | Digital Preservation Coalition (DPC) | 2025-11 / 2026 | 2026-11-25 | Opened directly | A-G-C11, A-O3-C2, A-O5-C3 | 5/4/4/5/5/4/5 | 4.50 | High | High |
| R04 | https://www.copyright.gov/1201/2024/ | Ninth Triennial Section 1201 Proceeding, 2024 Cycle | U.S. Copyright Office | 2024-10-28 | 2026-11-25 | Opened directly | A-O3-C3, A-G-C14 | 5/4/5/5/4/5/5 | 4.70 | High | High |
| R05 | https://pubmed.ncbi.nlm.nih.gov/29228189/ (via NCBI E-utilities efetch XML) | A snapshot of 3649 Web-based services published between 1994 and 2017 shows a decrease in availability after 2 years (DOI: 10.1093/bib/bbx159) | Briefings in Bioinformatics (Oxford) | 2019-05-21 | 2026-11-25 | Opened directly (abstract XML) | A-G-C2, A-O1-C1 | 5/5/5/5/3/5/5 | 4.80 | High | High |
| R06 | https://pubmed.ncbi.nlm.nih.gov/28334982/ (via NCBI E-utilities efetch XML) | Use it or lose it: citations predict the continued online availability of published bioinformatics resources (DOI: 10.1093/nar/gkx182) | Nucleic Acids Research (Oxford) | 2017-04-20 | 2026-11-25 | Opened directly (abstract XML) | A-G-C3 | 5/5/5/5/3/5/5 | 4.80 | High | High |
| R07 | https://pubmed.ncbi.nlm.nih.gov/18413326/ (via NCBI E-utilities efetch XML) | URL decay in MEDLINE--a 4-year follow-up study (DOI: 10.1093/bioinformatics/btn127) | Bioinformatics (Oxford) | 2008-06-01 | 2026-11-25 | Opened directly (abstract XML) | A-G-C7, A-O1-C2 | 5/5/5/4/2/5/5 | 4.55 | High | High |
| R08 | https://pubmed.ncbi.nlm.nih.gov/24266891/ (via NCBI E-utilities efetch XML) | A cross disciplinary study of link decay and the effectiveness of mitigation techniques (DOI: 10.1186/1471-2105-14-S14-S5) | BMC Bioinformatics | 2013 | 2026-11-25 | Opened directly (abstract XML) | A-O1-C2 | 5/5/5/4/2/5/5 | 4.55 | High | High |
| R09 | https://endings.uvic.ca/principles.html | Endings Principles for Digital Longevity (v2.2.1) | University of Victoria (The Endings Project) | 2025-01-03 | 2026-11-25 | Opened directly | A-G-C7, A-G-C8, A-O1-C3 | 5/5/5/5/4/5/5 | 4.90 | High | High |
| R10 | https://raw.githubusercontent.com/mastodon/documentation/main/content/en/user/moving.md | Moving or leaving accounts — Official Mastodon Documentation | Mastodon gGmbH | 2026 (live repo) | 2026-11-25 | Opened directly | A-G-C10, A-O2-C2 | 5/5/5/5/5/5/5 | 5.00 | High | High |
| R11 | https://www.softwarepreservationnetwork.org/eaasi-case-study-1-the-would-be-gentleman/ | EaaSI Case Study #1: "The Would-Be Gentleman" (Stanford Libraries BDPL) | Software Preservation Network (SPN) | 2021-01-11 | 2026-11-25 | Opened directly | A-G-C8, A-O3-C1 | 5/5/5/5/3/4/5 | 4.70 | High | High |
| R12 | https://pretendo.network/ | Pretendo Network — Official Site & Progress/FAQ | Pretendo Network | 2026 (live) | 2026-11-25 | Opened directly | A-G-C5, A-G-C12, A-O4-C2 | 4/5/5/5/5/5/4 | 4.75 | Medium-High | High |
| R13 | https://api.github.com/orgs/PretendoNetwork | PretendoNetwork GitHub Organization Metadata API | GitHub / Pretendo Network | 2026-11-25 | 2026-11-25 | Opened directly | A-G-C5, A-O4-C2 | 5/5/5/4/5/5/5 | 4.85 | High | Medium-High |
| R13b | https://gdpr-info.eu/art-89-gdpr/ | Art. 89 GDPR – Safeguards and derogations relating to processing for archiving purposes in the public interest | Intersoft Consulting (reproducing Reg. EU 2016/679) | 2016 (in force) | 2026-11-25 | Opened directly | A-O5-C2, A-G-C14 | 4/4/5/5/4/5/5 | 4.50 | High | High |
| R14d | https://digital-strategy.ec.europa.eu/en/policies/copyright-legislation | EU copyright law \| Shaping Europe's digital future | European Commission | 2026 (live) | 2026-11-25 | Opened directly | A-G-C14 | 5/4/5/4/5/5/5 | 4.65 | High | Medium-High |
| R14e | https://www.gida-global.org/ | Global Indigenous Data Alliance (GIDA) — CARE Principles & 2026 IDSov/AI Workshop | Global Indigenous Data Alliance | 2026 | 2026-11-25 | Opened directly | A-G-C11, A-O5-C3 | 5/3/4/5/5/4/4 | 4.25 | High | High |
| R15 | https://www.ndl.go.jp/en/collect/online | E-Legal Deposit System for Online Publications & WARP | National Diet Library, Japan | 2023+ (live) | 2026-11-25 | Opened directly | A-G-C14, A-O5-C1 | 5/5/5/5/4/5/5 | 4.90 | High | High |
| R15b | https://www.nl.go.kr/oasis/ | OASIS — Online Archiving & Searching Internet Sources | National Library of Korea | 2026 (live) | 2026-11-25 | Opened directly | §9 Asia | 5/3/4/4/5/4/5 | 4.15 | High | Medium |
| R15c | https://netpreserve.org/about-us/members/ | IIPC Members Directory | International Internet Preservation Consortium (IIPC) | 2026 (live) | 2026-11-25 | Opened directly | §9 International | 5/3/4/4/5/5/5 | 4.25 | High | Medium |
| R16 | https://dtinit.org/ | Data Transfer Initiative — Projects, DTP, Data Trust Registry & AI Conversation Schema | Data Transfer Initiative (DTI) | 2026 | 2026-11-25 | Opened directly | A-G-C9, A-O2-C3 | 5/4/5/5/5/5/4 | 4.75 | High | High |
| R16b | https://api.github.com/repos/google/data-transfer-project | Data Transfer Project GitHub Repository API (`stars=3626`, `pushed=2026-11-25`) | GitHub / DTI-Google | 2026-11-25 | 2026-11-25 | Opened directly | §5, §10 A-O2 | 5/5/5/4/5/5/5 | 4.85 | High | Medium-High |
| R17 | https://specs.webrecorder.net/wacz/1.1.1/ | Web Archive Collection Zipped (WACZ) 1.1.1 Specification (+ Browsertrix GitHub API `stars=1202`) | Webrecorder | 2026 (stable) | 2026-11-25 | Opened directly | A-G-C6, A-O1-C3 | 5/5/5/5/5/5/5 | 5.00 | High | High |
| R18 | https://en.wikipedia.org/wiki/Cohost | Cohost (timeline, 203,805 users, ASSC, shutdown 2024–2025) | Wikipedia (secondary, citing ASSC/Archive Team) | 2025–2026 | 2026-11-25 | Opened directly | A-G-C1, A-O4-C3 | 3/4/4/5/5/4/5 | 4.10 | Medium | High |
| R19 | https://en.wikipedia.org/wiki/Tianya_Club | Tianya Club (offline 26/04/2023, resumed 02/06/2026, citing Leiphone & SCMP) | Wikipedia (secondary) | 2026-06 | 2026-11-25 | Opened directly | A-G-C1, A-O4-C3 | 3/3/4/5/5/4/5 | 3.90 | Medium | High |
| R19c | https://blog.archive.org/2024/12/04/end-of-hachette-v-internet-archive/ | End of Hachette v. Internet Archive | Internet Archive Blogs (Chris Freeland) | 2024-12-04 | 2026-11-25 | Opened directly | A-G-C14, A-O5-C3 | 5/4/5/5/4/5/3 | 4.60 | High | High |
| R20 | https://en.wikipedia.org/wiki/Cyworld | Cyworld (history, 2011 breach, decline, CyworldZ takeover) | Wikipedia (secondary) | 2026 (live) | 2026-11-25 | Opened directly | A-G-C4, A-G-C10 | 3/3/4/4/4/4/5 | 3.65 | Medium | Medium-High |
| R21 | https://www.copyright.gov/1201/2024/ (kèm kết quả tìm kiếm SPN/VGHF remote access rejection) | 2024 DMCA Section 1201 rejection of remote game access expansion | U.S. Copyright Office / SPN (search summary) | 2024-10-28 | 2026-11-25 | Snippet only (cho chi tiết bác bỏ remote access) | A-O3-C3 | 4/3/4/5/4/3/5 | 3.90 | High | High |
| R21b | https://ec.europa.eu/ (search summary on EC Communication C(2026)4110) | European Commission reply to Stop Destroying Videogames (declining legislation, proposing code of conduct) | European Commission / Legal press | 2026-06-16 | 2026-11-25 | Snippet only | A-O4-C1 | 4/3/4/5/5/3/5 | 4.00 | High | High |
| R22 | https://techcrunch.com/ (search summary on Cohost shutdown) | Cohost shutdown financial challenges & loss of benefactor | TechCrunch / Media | 2024-09 | 2026-11-25 | Snippet only | A-G-C1, A-G-C13 | 3/3/4/5/4/3/4 | 3.65 | Medium | High |
| R23 | https://exodeui.com/ & https://siliconrepublic.com/ (search summary) | InVision design services shutdown (Dec 31, 2024) & Freehand acquisition by Miro | Tech media | 2024–2025 | 2026-11-25 | Snippet only | A-O2-C4 | 3/3/4/5/4/3/4 | 3.65 | Medium | High |
| R24 | https://arxiv.org/ & https://pdpp.dev/ (search summary on DTP/DTI) | Data Transfer Project canonical models vs relational schema limitations | Academic / Technical docs | 2024–2026 | 2026-11-25 | Snippet only | A-O2-C3, §5 | 4/4/4/5/4/3/5 | 4.10 | Medium-High | High |
| R25 | https://www.softwareheritage.org/ (search summary — SSL error on direct fetch) | Software Heritage UNESCO partnership, >27B source files, Merkle DAG & multi-stakeholder funding | Software Heritage / UNESCO | 2026 | 2026-11-25 | Snippet only | A-G-C7, §6 | 4/4/4/5/5/3/4 | 4.15 | High | High |
| R26 | https://koreajoongangdaily.com/, https://sixthtone.com/, https://zkm.de/ (search summary) | Cyworld 2022–2023 revival issues; Tianya unpaid fees; Yahoo! GeoCities Japan 96M URLs | International news / Cultural institutions | 2019–2026 | 2026-11-25 | Snippet only | A-G-C4, §9 Asia | 3/3/4/5/4/3/4 | 3.65 | Medium | High |
| R27a–i | Tổng hợp kết quả tìm kiếm bổ trợ: DPC 2025 Bit List (`R27a`), IPFS/Filecoin/Arweave pinning & centralization (`R27b`), NLB Act 2019 Web Archive Singapore (`R27c`), WebCite 6/2023 shutdown & CMDP (`R27d`), NARA/LC/DPC AI & C2PA (`R27e`), DSM Art. 6 (`R27g`), CARE (`R27h`), EaaSI Yale 2026 transition (`R27i`) | Multi-topic corroborating search summaries | Multiple official/institutional sources | 2019–2026 | 2026-11-25 | Snippet only (mọi luận điểm dựa riêng trên nhóm này được gán tối đa `INFERENCE`) | §4–§10 | 3/3/4/4/4/2/4 | 3.40 | Medium | Medium-High |

*(Ghi chú kiểm đếm: 34 hàng nguồn trong bảng gồm **26 nguồn mở trực tiếp** [R01–R20 bao gồm các mã phụ R13b, R14d, R14e, R15b, R15c, R16b, R19c] và **8 nguồn/nhóm chỉ xem qua snippet** [R21, R21b, R22, R23, R24, R25, R26, R27a–i].)*
