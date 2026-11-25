# Discovery Report — Agent A

## Metadata

- **Run ID:** `2026-11-25-phase1-discovery` (Kiroween 2026 — Phase 1: Independent Discovery)
- **Agent:** Research Agent A
- **Model:** Gemini 4 Neon (High) (`effort: high`)
- **Start Time (UTC):** `2026-11-25T08:02:21Z`
- **End Time (UTC):** `2026-11-25T08:22:30Z`
- **Tools Used:** `read_file`, `search_web`, `run_command` (Python 3 `urllib` để giải mã redirect URL, kiểm chứng HTTP status/tiêu đề/ngày đăng/trích đoạn nội dung gốc, và truy vấn trực tiếp Stack Exchange Public API v2.3), `write_file`
- **Searches & Verification Run:** ~22 truy vấn `search_web` độc lập; 4 tập lệnh kiểm chứng tự động (tổng cộng ~58 lượt HTTP fetch kiểm chứng URL gốc + 7 lượt gọi trực tiếp `api.stackexchange.com/2.3/questions`)
- **Failures / Access Blocks (10 lượt truy cập không đọc được nội dung trực tiếp):**
  1. `venturebeat.com` (Yahoo Pipes): `HTTP 429 Too Many Requests`
  2. `eclecticlight.co` (Apple Guide): `HTTP 403 Forbidden`
  3. `bleepingcomputer.com` (Google Groups Usenet): `HTTP 403 Forbidden`
  4. `support.discord.com` (Server Web Pages — 2 URL): `HTTP 403 Forbidden` (chỉ trích dẫn thông tin đã được đối chiếu qua nguồn thứ cấp mở `serverfront.app` và ghi rõ giới hạn kiểm chứng)
  5. `support.mozilla.org` (Pocket KB — 3 URL): `Client Challenge` (cơ chế chống bot; không vượt rào, thay bằng bài công bố chính thức trên `blog.mozilla.org` và kiểm chứng chéo qua `niemanlab.org`)
  6. `techcommunity.microsoft.com` (InfoPath blog — 2 URL): `HTTP 403 Forbidden` (thay bằng tài liệu chính thức `learn.microsoft.com` + blog kỹ sư SharePoint `stefan-gossner.com` + thông báo IT Đại học `its.wsu.edu`)
  7. `walkme.com` (thông cáo SAP mua lại): `HTTP 403 Forbidden` (thay bằng thông cáo báo chí chính thức từ `news.sap.com`)
  8. `scribehow.com`: SSL handshake timeout (không đưa làm nguồn xác minh trực tiếp; hạn chế của Scribe chỉ ghi nhận ở mức cần kiểm chứng trực tiếp)
  9. `stackoverflow.com/help/ai-policy` và 2 trang `meta.stackoverflow.com`: `HTTP 403 Forbidden`
  10. `search.marginalia.nu/about/`: `HTTP 404 Not Found` (đã xác minh qua tên miền chính hiện hành `https://marginalia-search.com/`)

---

## 1. Research methodology

Báo cáo này thực hiện **khám phá độc lập (Independent Discovery)** các không gian vấn đề (*problem spaces*) và cơ hội hồi sinh (*revival opportunities*) phù hợp với hạng mục **Resurrection** của Kiroween 2026 (*"Bring your favorite dead technology back to life. Reimagine obsolete tech with today's innovations or solving tomorrow's problems"* [R01]), tuân thủ đồng thời hai kỹ năng chuẩn của dự án (`historical-technology-discovery` và `user-problem-validation`) cùng nguyên tắc phản biện giả định nền (A1–A5):

1. **Rà soát nền cũ để tránh trùng lặp và phản biện thay vì mở rộng mù quáng:** Đọc `AGENTS.md`, `brief.md`, `progress/current-state.md`, `ideas/all-candidates.md` (41 giả thuyết C01–C41) và `ideas/rejected.md` (31 ý tưởng bị loại). Mục tiêu đặt ra là tìm tối thiểu 50% không gian vấn đề **hoàn toàn mới** (báo cáo này đạt **6/7 không gian mới = 85,7%**), và chỉ mở lại **1 không gian cũ** (`A-P7`) khi có **dữ liệu sơ cấp mới năm 2026 có thể tái lập** làm lung lay trực tiếp lý do đánh giá của các chu kỳ 16–21.
2. **Truy nguyên lịch sử → cơ chế suy giảm → giá trị mất đi → nỗi đau hiện tại:** Với mỗi không gian vấn đề, tách bạch rõ: (a) nguyên nhân suy giảm đã được chủ sở hữu công bố chính thức so với suy đoán bên ngoài; (b) công nghệ đã ngừng hoàn toàn (*discontinued*) so với công nghệ còn tồn tại ở ngách (*niche/active*); (c) giá trị thực sự bị mất khi chuyển sang công nghệ thay thế, thay vì hoài niệm giao diện.
3. **Kiểm chứng khẳng định theo chuỗi 4 bậc và gán nhãn tường minh:** Mọi khẳng định trọng yếu (`A-Px-Cy`) được đối chiếu theo chuỗi `Claim → Primary evidence → Independent confirmation → Reproduction/mechanism check` và gán nhãn **VERIFIED (ĐÃ XÁC MINH)**, **INFERENCE (SUY LUẬN)**, **HYPOTHESIS (GIẢ THUYẾT)**, hoặc **UNKNOWN (CHƯA RÕ)**. Tuyệt đối không suy diễn quy mô thị trường từ độ phổ biến lịch sử hay phàn nàn trên diễn đàn, và không dùng URL trung gian chưa kiểm chứng.
4. **Tìm đối thủ mạnh nhất và bằng chứng phản biện trước khi nói về cơ hội hồi sinh:** Với từng không gian, chủ động tìm đối thủ thương mại/mã nguồn mở mạnh nhất năm 2025–2026, bóc tách hạn chế cụ thể có kiểm chứng, chỉ rõ phần **AI đóng vai trò trụ cột (load-bearing)** so với **trang trí (decorative)**, và thiết kế phép thử nhỏ nhất để bác bỏ nhu cầu. Không xếp hạng, không chấm điểm thắng giải, và không chọn ý tưởng để triển khai ở Pha 1.

---

## 2. Discovered problem spaces

| ID | Problem space (Không gian vấn đề) | Who is affected (Đối tượng chịu tác động) | Technology / Workflow (Công nghệ / Quy trình lịch sử) | New vs Revisited |
|---|---|---|---|---|
| **A-P1** | Tuyến đường tổng hợp và lọc dữ liệu web minh bạch do người dùng cuối lập trình trực quan | Nhà nghiên cứu, nhà báo, người theo dõi nguồn tin chuyên biệt (chính sách, học bổng, đấu thầu, phát hành kỹ thuật) bị quá tải bởi thuật toán mạng xã hội | **Yahoo! Pipes** (2007–2015) — môi trường lập trình luồng dữ liệu trực quan (visual web mashup & RSS routing) | **New** |
| **A-P2** | Hướng dẫn thao tác phần mềm tương tác nhận biết trạng thái giao diện thực (*state-aware coachmarks*) | Người dùng phần mềm phức tạp thường xuyên đổi giao diện (phần mềm mã nguồn mở chuyên sâu, cổng dịch vụ công/thuế, SaaS nghiệp vụ) và người ít rành kỹ thuật | **Apple Guide / Macintosh Guide** (System 7.5, 1994–2001) — hệ trợ giúp chủ động đọc trạng thái ứng dụng (AEOM) và vẽ *coachmark* trực tiếp trên UI | **New** |
| **A-P3** | Tri thức cộng đồng mở, lập chỉ mục được và di chuyển được trước sự dịch chuyển sang không gian chat khép kín | Cộng đồng mã nguồn mở quy mô vừa/nhỏ (<1.000 thành viên), nhóm phần cứng/modding/self-hosting và người tự học bị mắc kẹt trong "hố đen tri thức" trên Discord/Slack | **Usenet / NNTP** (Google Groups ngừng hỗ trợ 22/02/2024) & **diễn đàn/mailing list lập chỉ mục công khai** (Gmane, Mailman) | **New** |
| **A-P4** | Bảo tồn dấu trang, trích dẫn nghiên cứu và kho đọc cá nhân chống *link rot* và rủi ro đóng cửa dịch vụ SaaS | Nhà nghiên cứu, sinh viên, nhà báo, lập trình viên và người đọc web có kho lưu trữ liên kết/bài đọc nhiều năm | **Del.icio.us** (2003–2017) & **Mozilla Pocket** (2007–2025, đóng cửa 08/07/2025) — đánh dấu xã hội phân loại bằng thẻ (*folksonomy*) và lưu đọc sau | **New** |
| **A-P5** | Cứu hộ biểu mẫu nghiệp vụ khai báo (*declarative forms*) và dữ liệu XML lịch sử sau hạn khai tử bắt buộc | Bộ phận vận hành, CNTT nội bộ tại trường đại học, bệnh viện, cơ quan địa phương và doanh nghiệp vừa/nhỏ phụ thuộc biểu mẫu SharePoint cũ | **Microsoft InfoPath** (2003–2026; chính thức ngừng hỗ trợ và gỡ khỏi SharePoint Online ngày 14/07/2026) | **New** |
| **A-P6** | Khám phá nguồn web đáng tin cậy có kiểm duyệt cộng đồng giữa làn sóng *SEO affiliate spam* và nội dung AI hàng loạt (*AI slop*) | Người tìm kiếm thông tin phi thương mại, đánh giá sản phẩm trung lập, tài nguyên độc lập và chuyên gia tra cứu (OSINT/nghiên cứu) | **DMOZ / Open Directory Project** (1998–2017) & **Webrings** — danh mục web do biên tập viên tình nguyện thẩm định và liên kết cộng đồng | **New** |
| **A-P7** | Kho tri thức hỏi-đáp kỹ thuật công khai và bảo tồn lời giải ca biên (*edge-case*) được con người kiểm chứng sau cú sụp đổ lưu lượng 2026 | Lập trình viên, kỹ sư hạ tầng/hệ thống và người duy trì thư viện mới hoặc lỗi hiếm nơi LLM thiếu dữ liệu huấn luyện hoặc ảo giác | **Stack Overflow & cộng đồng hỏi-đáp kỹ thuật công khai** (sụp đổ >99% lượng câu hỏi mới năm 2026) | **Revisited** *(bằng chứng sơ cấp API 2026 mới, thách thức kết luận chu kỳ 16–21 và A4)* |

---

## 3. Historical context

### A-P1 — Yahoo! Pipes (2007–2015)

- **Giai đoạn, chức năng và người dùng gốc:** Ra mắt tháng 2/2007 bởi Yahoo!, **Yahoo! Pipes** là ứng dụng web cho phép người dùng kéo-thả các khối xử lý (*modules*) để lấy nguồn RSS/Atom/JSON/HTML, trộn, lọc, đổi định dạng, sắp xếp và xuất ra một luồng RSS/JSON mới mà không cần viết mã truyền thống [R02, R03, R04]. Người dùng gốc gồm blogger, nhà báo dữ liệu, nghệ sĩ truyền thông số (*net art*), người dùng kỹ thuật không chuyên (*prosumers*) và lập trình viên muốn tạo *mashup* nhanh [R02, R04].
- **Bằng chứng sử dụng & nguyên nhân suy giảm:** Được ghi nhận rộng rãi như tiền thân của các công cụ tự động hóa web kiểu IFTTT [R02, R03]. Ngày **04/06/2015**, Yahoo! công bố trong báo cáo ưu tiên sản phẩm quý 2 (*Q2 2015 Progress Report*) việc đóng cửa Yahoo! Pipes cùng Yahoo! Maps để tập trung nguồn lực vào các mảng cốt lõi [R02, R04]. Dịch vụ ngừng cho tạo pipe mới từ **30/08/2015** và tắt hoàn toàn ngày **30/09/2015** mà không có công cụ thay thế hay đường di chuyển chính thức [R02, R03, R04]. *Tách biệt suy đoán:* Bên cạnh lý do tái cơ cấu doanh nghiệp đã công bố, giới phân tích cho rằng sự suy giảm của RSS mở, sự chuyển dịch sang API đóng và nguồn tin thuật toán trên mạng xã hội làm giảm tệp người dùng duy trì (*SUY LUẬN*).
- **Công nghệ thay thế & trạng thái hiện tại:** Đã ngừng hoàn toàn (*discontinued*). Được thay thế phân mảnh bởi IFTTT/Zapier/Make/n8n (tự động hóa SaaS/workflow), các trình đọc RSS có AI (Feedly, Inoreader) và các dòng thời gian thuật toán (X, TikTok, YouTube, LinkedIn).
- **Lợi ích từ thay thế & giá trị bị mất:** Công cụ mới ổn định hơn với API thương mại có xác thực OAuth và kết nối ứng dụng doanh nghiệp. **Giá trị mất đi:** Một không gian **minh bạch, kiểm soát được, dễ chia sẻ/nhân bản (*cloneable pipe*)** cho phép người không chuyên lập trình tự lắp ghép quy tắc lọc tin xuyên nguồn web mà không phụ thuộc hộp đen thuật toán đề xuất hay hạ tầng tự lưu trữ (*self-host*) phức tạp.

### A-P2 — Apple Guide / Macintosh Guide (1994–2001)

- **Giai đoạn, chức năng và người dùng gốc:** Ra mắt năm **1994** trong **System 7.5** (tồn tại qua Mac OS 8–9), **Apple Guide** (tên hướng người dùng: *Macintosh Guide*) là hệ trợ giúp tương tác cấp hệ điều hành đi kèm *Balloon Help* [R09, R10, R11]. Điểm cốt lõi không phải tài liệu tĩnh mà là khả năng đọc trạng thái thực tế của ứng dụng đang chạy thông qua **AppleEvent Object Model (AEOM)**, kiểm tra ngữ cảnh (*context checks*), vẽ dấu chỉ trực tiếp bằng nét đỏ (*coachmarks*) lên đúng nút/menu/cửa sổ ngay cả khi vị trí thay đổi, và tự điều chỉnh bước nếu người dùng thao tác khác dự kiến [R09, R10, R11].
- **Bằng chứng sử dụng & nguyên nhân suy giảm:** Được Apple tích hợp sẵn trong System 7.5 và khuyến khích qua sách kỹ thuật chính thức *Apple Guide Complete* (1995) cùng các công cụ bên thứ ba như Anarchie (ghi nhận đương thời trên *TidBITS*, 19/09/1994 và 12/12/1994) [R09, R10]. Tuy nhiên, Apple Guide **không được đưa lên Mac OS X (2001)** mà bị thay bằng hệ trợ giúp HTML tĩnh (*Apple Help Viewer*) [R11]. *Nguyên nhân kỹ thuật được ghi nhận:* Chi phí viết kịch bản, gắn móc kiểm tra trạng thái vào giao diện và bảo trì mỗi khi UI thay đổi quá lớn đối với lập trình viên bên thứ ba, khiến tỷ lệ áp dụng ngoài Apple thấp [R10, R11].
- **Công nghệ thay thế & trạng thái hiện tại:** Đã ngừng hoàn toàn (*discontinued*). Được thay bằng tài liệu web tĩnh, video YouTube, công cụ chụp bước tĩnh (Scribe/Tango), nền tảng hướng dẫn doanh nghiệp (*Digital Adoption Platforms* như WalkMe/Pendo), framework gợi ý nhẹ do nhà phát triển tự viết (Apple TipKit) và gần đây là chatbot AI.
- **Lợi ích từ thay thế & giá trị bị mất:** Tài liệu HTML và video rẻ hơn nhiều để xuất bản và tìm qua Google. **Giá trị mất đi:** Cơ chế hướng dẫn **chủ động kiểm tra trạng thái màn hình thực** và chỉ đúng phần tử đang hiển thị của phiên bản phần mềm người dùng đang mở, thay vì buộc người dùng tự đối chiếu giữa hướng dẫn lỗi thời (hoặc lời giải AI tự suy đoán) với giao diện thật.

### A-P3 — Usenet / NNTP & Diễn đàn/Mailing List công khai lập chỉ mục (1980–2024)

- **Giai đoạn, chức năng và người dùng gốc:** **Usenet** (giao thức NNTP) và các cổng lưu trữ danh sách thư/diễn đàn web công khai (như **Gmane** ra mắt 2002 [R14b], Mailman/Pipermail, phpBB) từng là xương sống trao đổi kỹ thuật, hỗ trợ phần mềm mã nguồn mở và cộng đồng chuyên đề từ thập niên 1980–2000. Đặc tính kiến trúc là **giao thức mở, phân luồng theo chủ đề (*threaded*), có URL/Message-ID ổn định và được công cụ tìm kiếm lập chỉ mục công khai**.
- **Bằng chứng suy giảm & mốc lịch sử:** Cổng lưu trữ mail-sang-news **Gmane** gặp gián đoạn nghiêm trọng và mất chức năng giao diện web truyền thống từ 2016 trở đi [R14b]. Gần đây nhất, ngày **22/02/2024**, Google chính thức chấm dứt hỗ trợ Usenet trên **Google Groups** (ngừng đăng bài, đăng ký, xem bài mới và tắt máy chủ NNTP/peering), chỉ giữ kho đọc trước 22/02/2024 [R14]. *Nguyên nhân đã công bố:* Google nêu rõ hoạt động văn bản hợp lệ trên Usenet đã sụt giảm mạnh trong khi spam tràn lan, và người dùng đã chuyển sang diễn đàn web hiện đại và mạng xã hội [R14]. Song song đó, hàng loạt cộng đồng kỹ thuật và sở thích chuyển hẳn sang chat thời gian thực (**Discord**, **Slack**).
- **Công nghệ thay thế & trạng thái hiện tại:** Usenet văn bản đại chúng suy tàn mạnh (cổng web lớn nhất là Google Groups đã đóng cửa chiều tương tác mới [R14]); giao thức NNTP còn tồn tại ở ngách hẹp. Công nghệ thay thế chủ đạo là Discord, Slack, GitHub Discussions và Discourse [R15].
- **Lợi ích từ thay thế & giá trị bị mất:** Chat thời gian thực giảm ma sát gia nhập, phản hồi nhanh, hỗ trợ thoại/ảnh/bot tốt trên di động. **Giá trị mất đi:** **Tính công khai lập chỉ mục được, cấu trúc vấn đề-lời giải bền vững và quyền sở hữu/di chuyển kho lưu trữ cộng đồng** — tri thức giải quyết sự cố bị chôn vùi trong dòng chat khép kín sau cánh cửa mời vào máy chủ (*walled garden*).

### A-P4 — Del.icio.us (2003–2017) & Mozilla Pocket (2007–2025)

- **Giai đoạn, chức năng và người dùng gốc:** **Del.icio.us** (ra mắt 2003) tiên phong mô hình đánh dấu xã hội (*social bookmarking*) cho phép lưu URL kèm từ khóa tự do (*folksonomy*) và khám phá liên kết do cộng đồng cùng gắn thẻ [R18]. **Pocket** (tiền thân Read It Later, ra mắt 2007, Mozilla mua lại năm 2017) cho phép người đọc lưu bài web để đọc ngoại tuyến, đánh dấu đoạn trích và giữ bản đọc sạch [R19, R20].
- **Bằng chứng sử dụng & nguyên nhân suy giảm:** Del.icio.us qua nhiều lần đổi chủ (Yahoo!, AVOS, Delicious Media) trước khi **Pinboard** mua lại ngày **01/06/2017** và chuyển sang chế độ **chỉ đọc (*read-only*) từ 15/06/2017**, tắt hoàn toàn tính năng lưu mới và API [R18]. Gần đây hơn, ngày **22/05/2025**, Mozilla công bố chính thức đóng cửa **Pocket** vào ngày **08/07/2025** (cùng Fakespot) để tập trung nguồn lực vào trình duyệt Firefox, viện dẫn sự thay đổi trong thói quen sử dụng web của người dùng [R19, R20]; cửa sổ xuất dữ liệu CSV kết thúc cuối năm 2025 và toàn bộ dữ liệu người dùng bị xóa vĩnh viễn sau đó [R20].
- **Công nghệ thay thế & trạng thái hiện tại:** Cả hai dịch vụ đều đã ngừng hoạt động tương tác (*discontinued*). Thay thế hiện tại gồm dấu trang trình duyệt, ứng dụng quản lý bookmark đám mây (Raindrop.io, Instapaper, Pinboard), công cụ ghi chú (Notion/Obsidian Web Clipper), và công cụ tự lưu trữ (*self-hosted*) như Karakeep (Hoarder) và ArchiveBox [R22, R23, R24].
- **Lợi ích từ thay thế & giá trị bị mất:** Trình duyệt và app ghi chú tích hợp sâu hơn với quy trình cá nhân. **Giá trị mất đi:** Hai tầng giá trị cùng đứt gãy: (1) một **kho lưu trữ bài đọc/liên kết bền vững thuộc quyền kiểm soát người dùng** không chết theo công ty SaaS hay biến mất vì *link rot* [R21]; (2) khả năng **chia sẻ và khám phá tập hợp tài liệu có phân loại ngữ nghĩa** giữa những người cùng nghiên cứu một chủ đề (điều mất hẳn khi bookmark chỉ nằm kín trong trình duyệt cá nhân).

### A-P5 — Microsoft InfoPath (2003–2026)

- **Giai đoạn, chức năng và người dùng gốc:** Ra mắt năm 2003 trong bộ Microsoft Office và đạt bản cuối **InfoPath 2013**, Microsoft InfoPath kết hợp với **InfoPath Forms Services** trên SharePoint cho phép nhân viên nghiệp vụ (không cần lập trình viên chuyên nghiệp) thiết kế biểu mẫu XML khai báo (`.xsn`), gắn quy tắc kiểm tra hợp lệ bằng XPath, bảng lặp (*repeating tables*), quy trình phê duyệt và lưu bản ghi đã nộp dưới dạng tệp XML chuẩn hóa [R25, R26].
- **Bằng chứng sử dụng & mốc khai tử chính thức:** InfoPath từng là công cụ biểu mẫu nội bộ chủ lực suốt hơn hai thập kỷ tại các tổ chức dùng Microsoft 365/SharePoint (trường đại học, cơ quan hành chính, y tế, doanh nghiệp). Theo bảng vòng đời chính thức của Microsoft Learn, **InfoPath 2013 chấm dứt hỗ trợ mở rộng (*Extended End Date*) ngày 14/07/2026 (giờ PT; 15/07/2026 UTC)** [R25]. Cùng ngày **14/07/2026**, Microsoft chính thức ngừng hỗ trợ **InfoPath Forms Services** trên SharePoint Server Subscription Edition [R26] và loại bỏ hoàn toàn dịch vụ này khỏi **SharePoint Online** (khẳng định độc lập qua thông báo ngừng vận hành thực tế của IT Đại học bang Washington ngày 06/07/2026 [R28]). Ngày **10/11/2026**, kỹ sư cấp cao mảng SharePoint của Microsoft (Stefan Goßner) xác nhận thêm: bản cập nhật **July 13, 2027 PU** sẽ **xóa vĩnh viễn** InfoPath Forms Services khỏi SharePoint Server Subscription Edition tại chỗ (*on-premises*) [R27]. *Nguyên nhân đã công bố:* Microsoft đã tuyên bố ngừng phát triển InfoPath từ 2014 để chuyển hướng sang nền tảng low-code đám mây **Power Platform / Power Apps** [R26, R28].
- **Công nghệ thay thế & trạng thái hiện tại:** Đã ngừng hỗ trợ hoàn toàn (*end-of-life* trên đám mây 07/2026; đang đếm ngược xóa mã trên máy chủ tại chỗ 07/2027). Công nghệ thay thế chính thức là Microsoft Power Apps, Power Automate, Microsoft Forms và các phần mềm bên thứ ba (Plumsail, NITRO Studio, Nintex).
- **Lợi ích từ thay thế & giá trị bị mất:** Power Apps hỗ trợ di động tốt hơn và kết nối nhiều dịch vụ đám mây hiện đại. **Giá trị mất đi:** Mô hình **biểu mẫu tự chứa bằng tệp chuẩn mở (`.xsn`/`.xml`) không phát sinh phí bản quyền phụ theo từng người dùng**, dễ in ấn/lưu hồ sơ pháp lý nguyên trạng, và có thể được nhân viên phòng ban tự chỉnh sửa mà không cần kiến trúc lại bằng Power Fx hay mua gói Power Apps Premium [R29].

### A-P6 — DMOZ / Open Directory Project (1998–2017) & Webrings

- **Giai đoạn, chức năng và người dùng gốc:** Ra mắt ngày **05/06/1998** (ban đầu tên GnuHoo/NewHoo, sau do Netscape/AOL sở hữu), **DMOZ (Open Directory Project)** là danh mục web do khoảng 90.000 biên tập viên tình nguyện xây dựng theo cây phân loại chủ đề ở 90 ngôn ngữ, cung cấp dữ liệu mở theo giấy phép Open Directory License/CC-BY từng nuôi sống kết quả danh mục và đoạn mô tả của nhiều công cụ tìm kiếm (kể cả Google thời kỳ đầu) [R30, R31]. Song song là các **Webrings** (từ 1994) nối các trang cá nhân/chuyên đề cùng mối quan tâm thành vòng tròn duyệt thủ công.
- **Bằng chứng sử dụng & nguyên nhân suy giảm:** DMOZ chính thức **đóng cửa ngày 17/03/2017** (ngừng biên tập từ 14/03/2017) theo quyết định của chủ sở hữu AOL [R30, R31]. *Nguyên nhân suy giảm:* Sự vượt trội về quy mô và tốc độ của công cụ tìm kiếm thuật toán (PageRank và hệ thống thu thập tự động), cộng với áp lực spam SEO gửi bài hàng loạt, kiệt sức của tình nguyện viên và việc AOL không còn đầu tư bảo trì hạ tầng [R31] (*phần nguyên nhân nội bộ kiệt sức tình nguyện viên là SUY LUẬN từ các ghi chép cộng đồng, trong khi mốc đóng cửa của AOL là ĐÃ XÁC MINH*).
- **Công nghệ thay thế & trạng thái hiện tại:** DMOZ đã đóng hoàn toàn (*discontinued*); cộng đồng biên tập viên lập dự án kế thừa **Curlie** (`curlie.org`) năm 2017 vẫn đang duy trì ở quy mô ngách [R30]. Công cụ thay thế đại chúng là công cụ tìm kiếm thuật toán (Google, Bing), tìm kiếm trả phí (Kagi), tìm kiếm web phi thương mại (Marginalia), các danh sách Awesome Lists trên GitHub và câu trả lời tổng hợp bằng AI.
- **Lợi ích từ thay thế & giá trị bị mất:** Tìm kiếm toàn văn theo thuật toán bao phủ hàng tỷ trang tức thời. **Giá trị mất đi:** **Lớp lọc thẩm định nguồn gốc con người (*human-vetted provenance*)** tách bạch rõ nguồn chuyên môn độc lập khỏi các trang tối ưu hóa công cụ tìm kiếm vì hoa hồng tiếp thị liên kết (*affiliate SEO*) và nội dung sinh tự động hàng loạt.

### A-P7 — Kho hỏi-đáp kỹ thuật công khai / Stack Overflow (2008–2026) *(Revisited)*

- **Giai đoạn, chức năng và người dùng gốc:** **Stack Overflow** (ra mắt 2008) là kho hỏi-đáp lập trình công khai theo mô hình bầu chọn, chuẩn hóa một câu hỏi tái lập tối thiểu với các lời giải xếp hạng theo cộng đồng, đạt đỉnh lịch sử **207.169 câu hỏi mới trong một tháng vào tháng 03/2014** [R38, R39]. (Các chu kỳ nghiên cứu 16–25 của dự án trước đây đã khảo sát Stack Overflow và CodeProject.)
- **Bằng chứng mới năm 2026 & nguyên nhân suy giảm:** Khác với nhận định ở chu kỳ 16–21 rằng *"Stack Overflow còn hoạt động, nên yếu tố Resurrection chưa chặt"*, dữ liệu trực tiếp truy xuất từ **Stack Exchange Public API v2.3** ngày 25/11/2026 [R38] và phân tích độc lập tháng 10/2026 [R39] chứng minh khối lượng câu hỏi mới hàng tháng đã **sụp đổ >99%** xuống dưới ngưỡng 1.000 câu hỏi/tháng (thấp hơn cả tháng đầu vận hành đầy đủ năm 2008): từ **207.169** (03/2014) và **123.257** (03/2022) xuống **44.704** (03/2024), **15.074** (03/2025), **2.981** (03/2026), **940** (09/2026) và **843** (10/2026) [R38]. *Nguyên nhân:* Hai động lực chồng lấn — suy giảm dài hạn từ sau 2014 gắn với ma sát kiểm duyệt/đóng bài khắt khe, và cú rơi thẳng đứng sau khi ChatGPT/coding agent ra đời cuối 2022 khi lập trình viên chuyển sang hỏi AI trực tiếp trong IDE thay vì đăng công khai [R39, R40].
- **Công nghệ thay thế & trạng thái hiện tại:** Tên miền `stackoverflow.com` vẫn tồn tại để đọc kho lưu trữ lịch sử và bán giấy phép dữ liệu, nhưng **cơ chế sản sinh tri thức công khai mới từ cộng đồng đã gần như chết lâm sàng** (<30 câu hỏi không bị xóa mỗi ngày trên toàn cầu vào tháng 10/2026 [R38]). Công nghệ thay thế là coding agent/LLM trong IDE, tài liệu chính thức, GitHub Issues/Discussions và Discord.
- **Lợi ích từ thay thế & giá trị bị mất:** AI giải đáp tức thì câu hỏi cú pháp/mẫu chuẩn theo đúng ngữ cảnh repo riêng mà không sợ bị đóng bài. **Giá trị mất đi:** **Vòng phản hồi công khai tạo tri thức mới cho các lỗi biên (*edge-case*), thư viện phiên bản mới và xung đột hệ thống thực tế** — khi câu hỏi mới biến mất, cả con người lẫn chính mô hình AI tương lai mất đi nguồn xác nhận thực nghiệm từ cộng đồng đối với công nghệ hậu-2025.

---

## 4. Evidence of contemporary relevance

*(Mỗi khẳng định tuân theo chuỗi: `Claim → Primary evidence → Independent confirmation → Reproduction/mechanism check` và ghi rõ bậc đạt được.)*

### A-P1 — Yahoo! Pipes / Tuyến lọc thông tin minh bạch

- **A-P1-C1:** Yahoo! Pipes là công nghệ đã khai tử hoàn toàn từ ngày 30/09/2015 (chỉ đọc từ 30/08/2015) mà không có công cụ kế thừa chính thức từ Yahoo!.
  - *Chuỗi kiểm chứng:* Đạt bậc **Independent confirmation** (bài báo đương thời ngày 04/06/2015 [R02], hồ sơ lưu trữ bảo tàng nghệ thuật số ZKM [R03], tổng hợp lịch sử [R04]).
  - *Nhãn:* **VERIFIED (ĐÃ XÁC MINH)**.
- **A-P1-C2:** Quá tải thông tin và lệ thuộc vào luồng đề xuất thuật toán trên mạng xã hội/video là hiện tượng quy mô toàn cầu và gia tăng trong năm 2025–2026: lần đầu tiên trong lịch sử báo cáo Reuters Institute Digital News Report (2026), mạng xã hội và nền tảng video vượt cả truyền hình lẫn trang tin/ứng dụng báo chí về mức phổ biến tiếp cận tin tức; đồng thời khảo sát Pew Research Center (tháng 12/2025, công bố 02/2026) ghi nhận **52% người trưởng thành Mỹ cảm thấy kiệt sức vì tin tức (*worn out*)** và **48% cho rằng phần lớn tin họ bắt gặp không liên quan đến cuộc sống** dù **80%** vẫn coi việc nắm thông tin là trách nhiệm công dân.
  - *Chuỗi kiểm chứng:* Đạt bậc **Independent confirmation** (hai khảo sát độc lập quy mô lớn năm 2026: Reuters Institute [R05] và Pew Research Center [R06]).
  - *Nhãn:* **VERIFIED (ĐÃ XÁC MINH)**.
- **A-P1-C3:** Sự lệ thuộc vào nền tảng thuật toán làm suy giảm quyền kiểm soát nguồn tin của nhóm người dùng chuyên môn (nhà báo, nhà nghiên cứu, người theo dõi phát hành/chính sách), tạo ra nhu cầu thực tế cho quy trình lọc và tổng hợp đa nguồn minh bạch không qua thuật toán mạng xã hội.
  - *Chuỗi kiểm chứng:* Đạt bậc **Primary evidence → Reasoning** (suy luận từ dữ liệu mệt mỏi tin tức [R05, R06] kết hợp sự tồn tại và phát triển tích cực của các kho mã nguồn mở tạo RSS như RSSHub/RSS-Bridge và hệ thống tự động hóa như n8n/Huginn [R07, R08]).
  - *Nhãn:* **INFERENCE (SUY LUẬN)**.
- **A-P1-C4:** Người dùng không chuyên lập trình sẵn sàng tự lắp ghép một đường ống lọc trực quan (*visual pipe*) nếu AI đảm nhận phần bóc tách trang web không có RSS và lọc theo ngữ nghĩa.
  - *Chuỗi kiểm chứng:* Chưa có kiểm chứng hành vi trực tiếp trên nhóm người dùng mục tiêu năm 2026.
  - *Nhãn:* **HYPOTHESIS (GIẢ THUYẾT)**.

### A-P2 — Apple Guide / Hướng dẫn giao diện nhận biết trạng thái

- **A-P2-C1:** Apple Guide (ra mắt System 7.5, 1994) từng cung cấp hướng dẫn từng bước nhận biết trạng thái ứng dụng trực tiếp qua AEOM và *coachmarks*, nhưng đã bị loại bỏ từ Mac OS X (2001) và không còn tồn tại trong hệ điều hành hiện đại; chi phí viết kịch bản thủ công cho nhà phát triển được ghi nhận ngay từ năm 1994 là rào cản lớn.
  - *Chuỗi kiểm chứng:* Đạt bậc **Independent confirmation** (ghi nhận đương thời trên *TidBITS* tháng 09 & 12/1994 [R09, R10], tổng hợp kỹ thuật [R11]).
  - *Nhãn:* **VERIFIED (ĐÃ XÁC MINH)**.
- **A-P2-C2:** Nhu cầu hướng dẫn thao tác ngay trong ứng dụng (*in-app digital adoption*) trên phần mềm hiện đại có giá trị kinh tế rất lớn ở phân khúc doanh nghiệp — minh chứng bằng thương vụ **SAP thỏa thuận mua lại WalkMe** ngày 05/06/2024 (nền tảng hướng dẫn thao tác trên phần mềm doanh nghiệp) và việc Apple phải giới thiệu framework **TipKit** cho lập trình viên hiển thị gợi ý theo điều kiện ngữ cảnh.
  - *Chuỗi kiểm chứng:* Đạt bậc **Independent confirmation** (thông cáo báo chí chính thức của SAP [R12] và tài liệu lập trình chính thức của Apple Developer [R13]).
  - *Nhãn:* **VERIFIED (ĐÃ XÁC MINH)**.
- **A-P2-C3:** Khoảng trống hiện tại nằm ở phía **người dùng cuối và phần mềm không tích hợp DAP**: WalkMe/TipKit đòi hỏi *chính nhà phát triển hoặc doanh nghiệp mua gói trả phí lớn* nhúng mã vào ứng dụng, nên người dùng cá nhân/tổ chức nhỏ thao tác trên phần mềm nguồn mở phức tạp (Blender, GIMP, OBS) hoặc cổng công/thuế vẫn không có *coachmark* nhận biết trạng thái thực.
  - *Chuỗi kiểm chứng:* Đạt bậc **Primary evidence → Reasoning** (rút ra từ kiến trúc yêu cầu tích hợp phía nhà phát triển của Apple TipKit [R13] và định vị doanh nghiệp của SAP/WalkMe [R12]).
  - *Nhãn:* **INFERENCE (SUY LUẬN)**.
- **A-P2-C4:** Người dùng gặp khó với phần mềm phức tạp sẽ chuộng lớp phủ *coachmark* kiểm chứng trạng thái UI thực hơn là hỏi chatbot/chia sẻ màn hình AI thông thường (như Copilot Vision/Gemini Live) khi các công cụ đó đã sẵn có vào cuối 2026.
  - *Chuỗi kiểm chứng:* Chưa có phép thử đối chứng định lượng giữa *coachmark* bám DOM/Accessibility Tree và AI screen-sharing năm 2026.
  - *Nhãn:* **HYPOTHESIS (GIẢ THUYẾT)**.

### A-P3 — Usenet / Diễn đàn công khai vs Không gian chat khép kín

- **A-P3-C1:** Google Groups đã chấm dứt hoàn toàn chức năng đăng bài, đăng ký và xem nội dung mới trên Usenet (cũng như máy chủ NNTP/peering) từ ngày **22/02/2024**, khép lại cổng web công khai lớn nhất còn lại của giao thức Usenet.
  - *Chuỗi kiểm chứng:* Đạt bậc **Primary evidence** (tài liệu hỗ trợ chính thức của Google Groups [R14]).
  - *Nhãn:* **VERIFIED (ĐÃ XÁC MINH)**.
- **A-P3-C2:** Vấn đề tri thức bị khóa trong máy chủ Discord là nỗi đau thật được cộng đồng đầu tư công cụ giải quyết (ví dụ dự án mã nguồn mở **Answer Overflow** biến luồng hỗ trợ Discord thành trang web lập chỉ mục được [R16]) và buộc chính Discord cuối năm 2026 phải tung ra tính năng **Server Web Pages** [R17].
  - *Chuỗi kiểm chứng:* Đạt bậc **Independent confirmation** (kho mã nguồn mở Answer Overflow trên GitHub [R16] và bài phân tích độc lập ngày 05/11/2026 về việc Answer Overflow thu hẹp sau động thái của Discord [R17]).
  - *Nhãn:* **VERIFIED (ĐÃ XÁC MINH)**.
- **A-P3-C3:** Ngay cả khi Discord ra mắt Server Web Pages (từ giữa tháng 12/2026), giải pháp chính chủ vẫn loại trừ toàn bộ máy chủ dưới 1.000 thành viên hoặc chưa bật Discoverable, **không xuất bản bất kỳ luồng lịch sử nào trước giữa tháng 12/2026**, và khóa nội dung trên tên miền `discord.com` (không cho dùng tên miền riêng hay dữ liệu Search Console) — dẫn tới khoảng trống tiếp diễn cho các cộng đồng vừa/nhỏ và kho tri thức lịch sử.
  - *Chuỗi kiểm chứng:* Đạt bậc **Secondary/independent reporting** (bảng đối chiếu chi tiết trên Serverfront ngày 05/11/2026 [R17]; lưu ý trang hỗ trợ gốc `support.discord.com` trả HTTP 403 nên chưa kiểm chứng trực tiếp bằng HTTP GET).
  - *Nhãn:* **INFERENCE (SUY LUẬN)** *(cần xác minh lại trực tiếp trên trang hỗ trợ Discord từ trình duyệt người dùng để nâng lên VERIFIED)*.
- **A-P3-C4:** Quản trị viên các cộng đồng mã nguồn mở/sở thích quy mô nhỏ (<1.000 thành viên) trên Discord hoặc Slack sẵn sàng triển khai công cụ trích xuất & chuẩn hóa dòng chat hỗn tạp thành kho hỏi-đáp tĩnh/mở thuộc quyền sở hữu cộng đồng.
  - *Chuỗi kiểm chứng:* Chưa khảo sát trực tiếp quản trị viên cộng đồng <1.000 thành viên năm 2026.
  - *Nhãn:* **HYPOTHESIS (GIẢ THUYẾT)**.

### A-P4 — Del.icio.us & Mozilla Pocket / Bảo tồn tri thức web chống *link rot*

- **A-P4-C1:** Hai nền tảng lưu trữ liên kết/bài đọc có tầm ảnh hưởng lịch sử đều đã chấm dứt hoạt động: **Del.icio.us** bị Pinboard chuyển sang chỉ đọc và tắt API từ **15/06/2017** [R18], còn **Mozilla Pocket** chính thức bị đóng cửa ngày **08/07/2025** kèm lộ trình xóa dữ liệu người dùng [R19, R20].
  - *Chuỗi kiểm chứng:* Đạt bậc **Independent confirmation** (thông báo chính thức của Pinboard [R18], blog chính thức của Mozilla ngày 22/05/2025 [R19], và bài tường thuật của Nieman Journalism Lab ngày 22/05/2025 [R20]).
  - *Nhãn:* **VERIFIED (ĐÃ XÁC MINH)**.
- **A-P4-C2:** Hiện tượng mục rữa liên kết (*link rot*) đang trực tiếp phá hủy kho tài liệu tham khảo trên web hiện đại: nghiên cứu định lượng của **Pew Research Center** (17/05/2024) cho thấy **38% trang web tồn tại năm 2013 đã không còn truy cập được sau một thập kỷ** (so với 8% của năm 2023), **23% trang báo chí** và **21% trang chính phủ** chứa ít nhất một liên kết hỏng, và **54% trang Wikipedia** có ít nhất một liên kết trích dẫn hỏng trong mục References.
  - *Chuỗi kiểm chứng:* Đạt bậc **Primary evidence + Reproducible methodology** (báo cáo nghiên cứu định lượng của Pew Research Center Data Labs [R21]).
  - *Nhãn:* **VERIFIED (ĐÃ XÁC MINH)**.
- **A-P4-C3:** Người dùng phổ thông (không biết vận hành Docker/VPS) hiện mắc kẹt giữa hai cực rủi ro: dùng dịch vụ đám mây trả phí (như Raindrop.io Pro, nơi tài liệu chính thức xác nhận **bản lưu trữ web bị xóa vĩnh viễn sau khoảng 1 tháng kể từ khi hết hạn gói Pro** [R22]) hoặc dùng công cụ tự lưu trữ mạnh (Karakeep, ArchiveBox [R23, R24]) nhưng đòi hỏi kỹ năng quản trị máy chủ.
  - *Chuỗi kiểm chứng:* Đạt bậc **Primary evidence → Reasoning** (xác minh trực tiếp chính sách xóa bản lưu của Raindrop.io [R22] và kiến trúc self-hosted của Karakeep/ArchiveBox [R23, R24]).
  - *Nhãn:* **INFERENCE (SUY LUẬN)**.
- **A-P4-C4:** Người dùng từng mất dữ liệu hoặc bị buộc di dời khỏi Pocket năm 2025 sẽ áp dụng giải pháp lưu trữ ưu tiên cục bộ (*local-first*), tự phát hiện *soft-404 / domain hijack* và tái tạo chia sẻ theo chủ đề kiểu *folksonomy* của Del.icio.us.
  - *Chuỗi kiểm chứng:* Chưa phỏng vấn nhóm cựu người dùng Pocket sau đợt đóng cửa 2025.
  - *Nhãn:* **HYPOTHESIS (GIẢ THUYẾT)**.

### A-P5 — Microsoft InfoPath / Cứu hộ biểu mẫu nghiệp vụ & hồ sơ XML hậu-EOL

- **A-P5-C1:** **Microsoft InfoPath 2013** và **InfoPath Forms Services** đã chính thức hết hạn hỗ trợ vào ngày **14/07/2026** (giờ PT); biểu mẫu InfoPath trên SharePoint Online đã ngừng hoạt động từ mốc này, và bản cập nhật **13/07/2027 PU** sẽ xóa vĩnh viễn tính năng này khỏi SharePoint Server Subscription Edition.
  - *Chuỗi kiểm chứng:* Đạt bậc **Independent confirmation** (Microsoft Learn Lifecycle [R25], tài liệu deprecated SharePoint Server SE [R26], thông báo kỹ sư Microsoft Stefan Goßner ngày 10/11/2026 [R27], và thông báo thực tế từ IT Đại học bang Washington ngày 06/07/2026 [R28]).
  - *Nhãn:* **VERIFIED (ĐÃ XÁC MINH)**.
- **A-P5-C2:** Phương án thay thế chính thức Microsoft khuyến nghị (**Power Apps**) đòi hỏi chi phí bản quyền đáng kể đối với ứng dụng dùng trình kết nối nâng cao/Dataverse (**Power Apps Premium: 20 USD/người dùng/tháng** trả theo năm, hoặc 12 USD/người dùng/tháng với tối thiểu 2.000 ghế) [R29], đồng thời Microsoft không cung cấp công cụ chuyển đổi tự động từ `.xsn` sang Power Apps.
  - *Chuỗi kiểm chứng:* Đạt bậc **Primary evidence** (bảng giá chính thức Microsoft Power Apps [R29]; phần không có công cụ chuyển đổi tự động được nhiều nguồn tư vấn di dời xác nhận nhưng chưa tìm thấy một trang Learn duy nhất tuyên bố phủ định tuyệt đối, nên chỉ ghi nhận phạm vi giá đã xác minh và khuyến nghị tự xây lại của Microsoft [R26, R28]).
  - *Nhãn:* **VERIFIED (ĐÃ XÁC MINH)** *(phần giá Power Apps & khuyến nghị chuyển sang Power Apps)* / **INFERENCE (SUY LUẬN)** *(mức độ phổ biến của chi phí cản trở ở SMB/trường học)*.
- **A-P5-C3:** Vào cuối năm 2026 (4 tháng sau hạn SharePoint Online và 8 tháng trước hạn xóa mã tại chỗ tháng 07/2027), một bộ phận tổ chức vẫn còn tồn đọng kho tệp mẫu `.xsn` và hàng nghìn bản ghi `.xml` đã nộp trước đây cần đọc, kiểm toán quy tắc nghiệp vụ hoặc chuyển sang biểu mẫu web nhẹ không khóa nền tảng (*vendor lock-in*).
  - *Chuỗi kiểm chứng:* Đạt bậc **Primary evidence → Reasoning** (từ lịch xóa vĩnh viễn tháng 07/2027 [R27] và thông báo vận hành đại học sát hạn tháng 07/2026 [R28]).
  - *Nhãn:* **INFERENCE (SUY LUẬN)**.
- **A-P5-C4:** Tỷ lệ tổ chức quy mô vừa/nhỏ hiện vẫn còn tệp `.xsn`/`.xml` chưa kịp di dời vào tháng 11/2026 và sẵn sàng dùng một công cụ mã nguồn mở đọc/chuyển đổi trực tiếp thay vì thuê đối tác Microsoft là bao nhiêu?
  - *Chuỗi kiểm chứng:* Thiếu số liệu thống kê công khai về số tổ chức còn tồn đọng InfoPath tại thời điểm tháng 11/2026.
  - *Nhãn:* **UNKNOWN (CHƯA RÕ)**.

### A-P6 — DMOZ & Webrings / Khám phá web có kiểm duyệt giữa *SEO spam* và *AI slop*

- **A-P6-C1:** DMOZ (Open Directory Project, thành lập 05/06/1998) đã chính thức đóng cửa ngày **17/03/2017**; dự án tình nguyện kế thừa **Curlie** tiếp nối danh mục mở nhưng không lấy lại được vị thế điểm khởi đầu tìm kiếm đại chúng.
  - *Chuỗi kiểm chứng:* Đạt bậc **Independent confirmation** (trang giới thiệu chính thức của Curlie [R30] và hồ sơ DMOZ [R31]).
  - *Nhãn:* **VERIFIED (ĐÃ XÁC MINH)**.
- **A-P6-C2:** Chất lượng kết quả tìm kiếm thương mại bị bào mòn có hệ thống bởi *affiliate SEO spam*: nghiên cứu dọc 1 năm công bố tại **ECIR 2024** (Bevendorff et al., Đại học Leipzig & Bauhaus-Universität Weimar, DOI `10.1007/978-3-031-56063-7_4`) trên Google, Bing và DuckDuckGo chỉ ra các trang xếp hạng cao ngày càng nghiêng về nội dung tối ưu hóa tiếp thị liên kết chất lượng văn bản thấp, và các đợt cập nhật thuật toán chỉ mang lại cải thiện tạm thời.
  - *Chuỗi kiểm chứng:* Đạt bậc **Primary evidence + Reproducible code/data** (kho mã nguồn & dữ liệu công khai của nhóm Webis tại ECIR 2024 [R32] và bài tóm lược độc lập từ Open Search Foundation [R33]).
  - *Nhãn:* **VERIFIED (ĐÃ XÁC MINH)**.
- **A-P6-C3:** Làn sóng nội dung có sự tham gia của AI tràn ngập web mới xuất bản: nghiên cứu của **Ahrefs** (19/05/2025) trên **900.000 trang web tiếng Anh mới tạo** (1 trang/tên miền, thu thập tháng 04/2025) ước tính **74,2%** có chứa nội dung AI (2,5% thuần AI, 71,7% pha trộn, chỉ 25,8% thuần người viết) [R34]. *Lưu ý phương pháp:* Con số này phụ thuộc độ chính xác của bộ phát hiện nội bộ `bot_or_not` của Ahrefs và chính Ahrefs trong nghiên cứu tiếp theo (07/07/2025, 600.000 trang [R35]) cho thấy nội dung AI không tự động thống trị tuyệt đối mọi thứ hạng Google, nên cần tách biệt tỷ lệ xuất bản với tỷ lệ xếp hạng.
  - *Chuỗi kiểm chứng:* Đạt bậc **Primary industry study** (hai nghiên cứu gốc của Ahrefs [R34, R35]).
  - *Nhãn:* **VERIFIED (ĐÃ XÁC MINH)** *(về kết quả đo của Ahrefs trên mẫu 900k trang)* / **INFERENCE (SUY LUẬN)** *(tác động thực tế đến cảm nhận người tìm kiếm ngoài nhóm truy vấn đánh giá sản phẩm)*.
- **A-P6-C4:** Một mô hình danh mục/vòng liên kết cộng đồng có AI hỗ trợ kiểm tra liên kết chết, phát hiện trang bị mua lại làm trang rác (*domain hijacking/slop drift*) có thể giảm đủ gánh nặng bảo trì để biên tập viên tình nguyện duy trì chất lượng lâu dài mà không lặp lại sự suy kiệt của DMOZ.
  - *Chuỗi kiểm chứng:* Chưa kiểm nghiệm cơ chế vận hành cộng đồng thực tế.
  - *Nhãn:* **HYPOTHESIS (GIẢ THUYẾT)**.

### A-P7 — Kho hỏi-đáp kỹ thuật công khai / Stack Overflow *(Revisited)*

- **A-P7-C1:** Lượng câu hỏi mới hằng tháng trên Stack Overflow đã giảm hơn **99,5% so với đỉnh tháng 03/2014** và hơn **99,3% so với tháng 03/2022 (trước ChatGPT)**: kiểm chứng tái lập trực tiếp qua **Stack Exchange Public API v2.3** ngày 25/11/2026 cho kết quả số câu hỏi không bị xóa lần lượt là **207.169** (03/2014), **123.257** (03/2022), **44.704** (03/2024), **15.074** (03/2025), **2.981** (03/2026), **940** (09/2026) và **843** (10/2026).
  - *Chuỗi kiểm chứng:* Đạt bậc **Reproduction / mechanism check** (truy vấn trực tiếp API công khai `api.stackexchange.com/2.3/questions` ngày 25/11/2026 [R38], khớp xu hướng với báo cáo độc lập ngày 31/10/2026 ghi nhận 969 câu hỏi tháng 09/2026 trước các lượt xóa/đóng sau đó [R39]).
  - *Nhãn:* **VERIFIED (ĐÃ XÁC MINH)**.
- **A-P7-C2:** Khảo sát Stack Overflow Developer Survey 2026 (>30.000 kỹ sư từ 169 quốc gia [R40]; kết hợp số liệu trực tiếp đã ghi nhận ở chu kỳ 18 trên cùng khảo sát 2026, n=16.985) cho thấy sự dịch chuyển vai trò: người dùng giảm mạnh việc hỏi câu cơ bản nhưng vẫn cần điểm kiểm chứng khi lời giải AI không chắc chắn.
  - *Chuỗi kiểm chứng:* Đạt bậc **Primary evidence** (trang công bố Stack Overflow Developer Survey 2026 [R40] và đối chiếu ngữ cảnh nội bộ `current-state.md` chu kỳ 18).
  - *Nhãn:* **VERIFIED (ĐÃ XÁC MINH)** *(về quy mô khảo sát và xu hướng giảm hỏi/tăng nhu cầu kiểm chứng)* / **INFERENCE (SUY LUẬN)** *(mức độ sẵn sàng dùng công cụ ngoài IDE để kiểm chứng)*.
- **A-P7-C3:** Khi lượng câu hỏi-đáp công khai mới tụt xuống dưới 1.000/tháng trên toàn cầu [R38], một "hố trống tri thức hậu-2025" xuất hiện đối với các lỗi biên thực nghiệm (phiên bản SDK mới, tương tác giữa hai thư viện mới, lỗi hạ tầng cụ thể) mà trước đây cộng đồng Stack Overflow biến từ sự cố cá nhân thành tài sản công khai có chứng cứ.
  - *Chuỗi kiểm chứng:* Đạt bậc **Primary evidence → Reasoning** (suy luận trực tiếp từ sụp đổ nguồn cung câu hỏi mới [R38, R39]).
  - *Nhãn:* **INFERENCE (SUY LUẬN)**.
- **A-P7-C4:** Lập trình viên năm 2026 có sẵn sàng đóng góp hoặc chia sẻ ẩn danh các "ca sửa lỗi đã kiểm chứng bằng log/test thực" từ phiên làm việc với AI/IDE sang một kho cộng đồng mở (thay vì giữ kín trong chat AI cá nhân) hay không?
  - *Chuỗi kiểm chứng:* Chưa có dữ liệu định lượng về động cơ đóng góp (*incentive*) khi không còn hệ điểm reputation kiểu cũ.
  - *Nhãn:* **UNKNOWN (CHƯA RÕ)**.

---

## 5. Existing alternatives

### A-P1 — Yahoo! Pipes
- **Đối thủ mạnh nhất:**
  1. **n8n** [R07, R08]: Nền tảng tự động hóa trực quan *fair-code*, hỗ trợ nút AI và chạy tự lưu trữ miễn phí (bản Cloud trả phí theo lượt chạy). *Hạn chế cụ thể:* Thiết kế hướng tới tích hợp API doanh nghiệp/lập trình viên; người dùng không chuyên phải tự vận hành máy chủ (VPS/Docker) để tránh phí Cloud, và các bộ thu thập HTML vẫn dễ vỡ khi trang nguồn đổi cấu trúc.
  2. **Huginn** [R08b]: Thường được gọi là "Yahoo! Pipes mã nguồn mở". *Hạn chế cụ thể:* Cấu hình tác nhân bằng JSON thuần, giao diện kém trực quan với người dùng phổ thông, cần kỹ năng tự vận hành Ruby/Docker.
  3. **RSSHub & RSS-Bridge** [R08c, R08d]: Sinh nguồn RSS cho các trang không có RSS. *Hạn chế cụ thể:* Chỉ dừng ở bước chuyển đổi đầu vào (*bridge*), không cung cấp luồng trộn/lọc/khử trùng lặp trực quan và dễ gãy khi nền tảng mạng xã hội chặn scraper.
  4. **Feedly (Pro+ / Leo AI)** [R08e]: Trình đọc RSS tích hợp AI ưu tiên tin và lọc chủ đề. *Hạn chế cụ thể:* Bản miễn phí bị giới hạn nguồn/thư mục và khóa tính năng AI; không phải công cụ lập trình luồng dữ liệu mở có thể xuất ra nguồn RSS chuẩn cho công cụ khác nếu không kết nối thêm dịch vụ trung gian.

### A-P2 — Apple Guide
- **Đối thủ mạnh nhất:**
  1. **WalkMe (thuộc SAP)** [R12]: Nền tảng hướng dẫn thao tác doanh nghiệp (*Digital Adoption Platform*) có lớp phủ chỉ dẫn từng bước. *Hạn chế cụ thể:* Định vị hoàn toàn cho doanh nghiệp lớn với hợp đồng thường niên đắt đỏ (ước tính bên thứ ba phổ biến hàng chục nghìn USD/năm — chưa có bảng giá công khai cố định) và đòi hỏi tổ chức/nhà phát triển chủ động triển khai tích hợp.
  2. **Apple TipKit** [R13]: Framework chính chủ của Apple hiển thị mẹo theo quy tắc sự kiện. *Hạn chế cụ thể:* Chỉ do **chính nhà phát triển ứng dụng** lập trình sẵn trong SwiftUI/UIKit/AppKit; người dùng cuối không thể dùng TipKit để hướng dẫn thao tác trên phần mềm bên thứ ba hoặc phần mềm cũ.
  3. **Scribe / Tango:** Công cụ ghi màn hình tự tạo hướng dẫn từng bước. *Hạn chế cụ thể:* Đầu ra là tài liệu ảnh chụp tĩnh dễ lỗi thời ngay khi giao diện phần mềm thay đổi, không kiểm tra trạng thái thực tế của ứng dụng người dùng đang mở. *(Lưu ý: `scribehow.com` gặp lỗi SSL timeout khi kiểm chứng trực tiếp.)*
  4. **AI chia sẻ màn hình (Microsoft Copilot Vision, Google Gemini Live):** Nhìn màn hình thời gian thực và giải thích bằng giọng nói/văn bản. *Hạn chế cụ thể:* Thường mô tả bằng lời nói/chữ thay vì vẽ *coachmark* định vị chính xác vào cây phần tử UI; bị ràng buộc hệ sinh thái (Edge/Windows hoặc thiết bị/OS nhất định) và dễ phát sinh lo ngại quyền riêng tư khi gửi toàn bộ luồng video màn hình lên đám mây.

### A-P3 — Usenet / Diễn đàn công khai vs Chat khép kín
- **Đối thủ mạnh nhất:**
  1. **Discord Server Web Pages (ra mắt cuối 2026)** [R17]: Tính năng chính chủ của Discord tự tạo trang web công khai và tóm tắt kênh để Google lập chỉ mục. *Hạn chế cụ thể:* Chỉ áp dụng cho máy chủ Discoverable (**từ 1.000 thành viên trở lên**, hoạt động ít nhất 8 tuần), **không xuất bản luồng cũ trước giữa tháng 12/2026**, và chỉ lưu trên tên miền `discord.com` (không xuất khẩu mở, không tên miền riêng) [R17].
  2. **Answer Overflow** [R16, R17]: Bot mã nguồn mở từng giúp lập chỉ mục luồng hỗ trợ Discord lên web. *Hạn chế cụ thể:* **Đang trong quá trình thu hẹp (*winding down*)** sau khi Discord công bố Server Web Pages [R17].
  3. **Discourse / GitHub Discussions / Zulip** [R15]: Diễn đàn và trao đổi có cấu trúc, lập chỉ mục tốt. *Hạn chế cụ thể:* Đòi hỏi cộng đồng phải di dời khỏi nơi người dùng đang trò chuyện hàng ngày (Discord/Slack), tạo ma sát kép khiến người mới vẫn hỏi trong chat thời gian thực.

### A-P4 — Del.icio.us & Mozilla Pocket
- **Đối thủ mạnh nhất:**
  1. **Raindrop.io** [R22]: Quản lý dấu trang đám mây đẹp, đa nền tảng, có tính năng *Web archive* (trước đây gọi là *Permanent copy*). *Hạn chế cụ thể:* Tính năng lưu bản sao web chỉ có ở gói trả phí Pro, và theo tài liệu trợ giúp chính thức của Raindrop.io, **khi hết hạn đăng ký Pro, các bản lưu trữ sẽ không thể truy cập và bị xóa vĩnh viễn sau khoảng một tháng** [R22] — tái diễn đúng rủi ro phụ thuộc SaaS.
  2. **Karakeep (trước đây là Hoarder)** [R23]: Mã nguồn mở tự lưu trữ, có tự động gắn thẻ AI, tìm kiếm toàn văn và lưu bản chụp trang. *Hạn chế cụ thể:* Đòi hỏi người dùng tự triển khai và bảo trì máy chủ/Docker (hoặc dùng bản Cloud trả phí), không giải quyết mượt bài toán chia sẻ danh mục cộng đồng kiểu *folksonomy* mở của Del.icio.us.
  3. **ArchiveBox** [R24]: Lưu trữ web mã nguồn mở lưu nhiều định dạng tĩnh (HTML, PDF, WARC) hướng tệp hệ thống. *Hạn chế cụ thể:* Quy trình kỹ thuật cao, tối ưu cho lưu trữ đơn lẻ hơn là trải nghiệm đọc-tìm-chia sẻ hàng ngày của người không chuyên.

### A-P5 — Microsoft InfoPath
- **Đối thủ mạnh nhất:**
  1. **Microsoft Power Apps** [R26, R29]: Phương án thay thế chính thức của Microsoft. *Hạn chế cụ thể:* Không có công cụ chuyển đổi tự động từ tệp `.xsn`; yêu cầu xây lại toàn bộ biểu mẫu và viết logic mới bằng Power Fx; gói **Power Apps Premium có giá 20 USD/người dùng/tháng** (trả năm) [R29], tăng mạnh chi phí so với InfoPath đi kèm SharePoint; yếu về mô hình xuất tài liệu/biểu mẫu tự chứa kiểu XML.
  2. **Microsoft Forms:** Miễn phí trong Microsoft 365. *Hạn chế cụ thể:* Chỉ phù hợp khảo sát đơn giản, không hỗ trợ bảng lặp lồng nhau (*repeating tables*), quy tắc phân nhánh phức tạp hay xem lại hồ sơ XML lịch sử của InfoPath.
  3. **Bên thứ ba chuyên SharePoint (Plumsail Forms, Crow Canyon NITRO Studio, Nintex):** Giải quyết nhiều khoảng trống biểu mẫu SharePoint. *Hạn chế cụ thể:* Chi phí thuê bao định kỳ, tiếp tục khóa tổ chức vào hệ sinh thái SharePoint/nhà cung cấp thương mại thay vì giải phóng cấu trúc biểu mẫu và dữ liệu XML sang chuẩn mở.

### A-P6 — DMOZ & Webrings
- **Đối thủ mạnh nhất:**
  1. **Curlie** [R30]: Kế thừa trực tiếp DMOZ do tình nguyện viên duy trì. *Hạn chế cụ thể:* Giao diện và mô hình duyệt thủ công kiểu cũ khó chống chọi tốc độ mục rữa liên kết (38% sau 10 năm [R21]) và hiện tượng tên miền cũ bị mua lại để nhồi *affiliate/AI slop*; khả năng tìm kiếm ngữ nghĩa yếu.
  2. **Kagi Search** [R36]: Công cụ tìm kiếm trả phí cho phép người dùng tự tạo bộ lọc (*Lenses*), chặn hoặc nâng hạng tên miền. *Hạn chế cụ thể:* Rào cản thu phí hàng tháng (**5 USD/tháng giới hạn 300 truy vấn; 10 USD/tháng không giới hạn** [R36]), hạn chế tiếp cận đại chúng và chủ yếu phục vụ nhóm người dùng kỹ thuật.
  3. **Marginalia Search** [R37]: Công cụ tìm kiếm mã nguồn mở (AGPL) ưu tiên trang web phi thương mại, văn bản thuần, không dùng AI [R37]. *Hạn chế cụ thể:* Không có cơ chế kiểm định cộng đồng theo chuyên ngành hẹp và không tối ưu cho truy vấn kỹ thuật/sản phẩm cập nhật nhanh.
  4. **GitHub Awesome Lists:** Danh sách tài nguyên do cộng đồng duy trì qua Pull Request. *Hạn chế cụ thể:* Chỉ mạnh trong lĩnh vực phần mềm/kỹ thuật, thiếu kiểm tra tự động về tính sống còn/sự biến chất nội dung của liên kết theo thời gian.

### A-P7 — Kho hỏi-đáp kỹ thuật công khai / Stack Overflow *(Revisited)*
- **Đối thủ mạnh nhất:**
  1. **Coding Agents & LLM trong IDE (Cursor, GitHub Copilot, Kiro, Claude Code):** Giải quyết tức thì phần lớn câu hỏi cú pháp và gỡ lỗi thông thường theo ngữ cảnh repo. *Hạn chế cụ thể:* Tri thức sửa lỗi biên bị **tư nhân hóa hoàn toàn** trong lịch sử chat cục bộ; khi gặp lỗi mới ở thư viện vừa phát hành, hàng nghìn lập trình viên lặp lại cùng vòng thử-sai riêng lẻ và AI có nguy cơ ảo giác vì thiếu bằng chứng thực thi công khai mới.
  2. **Stack Overflow AI Assist / Stack Internal:** Bản thân Stack Overflow đang tích hợp lớp AI và sản phẩm doanh nghiệp. *Hạn chế cụ thể:* Không đảo ngược được sự sụp đổ nguồn cung câu hỏi công khai mới (843 câu hỏi/tháng vào tháng 10/2026 [R38]) và vẫn mang gánh nặng ma sát đóng bài/quy định cộng đồng cũ.
  3. **GitHub Issues & Discussions:** Nơi báo lỗi gắn trực tiếp với từng kho mã nguồn. *Hạn chế cụ thể:* Tri thức bị phân mảnh theo từng repo, khó tra cứu lỗi tương tác chéo giữa nhiều thư viện/hệ điều hành (*cross-stack bugs*), và nhiều issue dài hàng trăm bình luận không tách rõ phương án đã kiểm chứng theo phiên bản.

---

## 6. Potential revival opportunities

*(Ghi chú: Phần này phác họa cơ chế hồi sinh tiềm năng và phân định rõ vai trò AI **trụ cột — load-bearing** so với **trang trí — decorative**; KHÔNG chọn hay xếp hạng ý tưởng.)*

### A-P1 — Hồi sinh Yahoo! Pipes kiểu "Semantic Deterministic Pipes"
- **Giá trị đương đại:** Trao lại cho người không chuyên lập trình một bảng vẽ đường ống minh bạch, kiểm tra được từng bước (*inspectable*) để gom tin từ các nguồn rời rạc (web chính quyền địa phương, trang học bổng, changelog phần mềm, blog độc lập), lọc bỏ rác/trùng lặp và xuất ra RSS/Atom/bản tin riêng tư — không hộp đen thuật toán.
- **AI trụ cột (*load-bearing*):** (1) **Tự sinh và tự sửa bộ trích xuất (*self-healing extractor*)** chuyển trang HTML không có RSS thành luồng có cấu trúc khi giao diện trang nguồn thay đổi — giải quyết điểm gãy lớn nhất của Yahoo! Pipes và RSS-Bridge; (2) **Nút lọc ngữ nghĩa có kiểm chứng (*semantic predicate node*)** cho phép viết điều kiện ngôn ngữ tự nhiên (ví dụ: *"chỉ giữ thông báo đấu thầu hạ tầng mạng, bỏ thông cáo báo chí"*) nằm *bên trong* một đồ thị xử lý tất định, lưu log rõ lý do từng mục bị giữ/loại.
- **AI trang trí (*decorative — cần tránh*):** Gắn một ô chat "Hỏi về tin tức hôm nay" lên trên trình đọc RSS thông thường.
- **Khả thi lát cắt demo (~9 ngày):** Cao — có thể chạy hoàn toàn trên web/local với trình dựng đồ thị nút (visual node editor), 3–4 nguồn web/RSS thật, một nút lọc ngữ nghĩa có giải thích và đầu ra RSS/JSON sống.

### A-P2 — Hồi sinh Apple Guide thành "User-Side State-Aware Coachmarks"
- **Giá trị đương đại:** Một trợ lý hướng dẫn phía người dùng (*browser extension* cho web app/cổng dịch vụ công, hoặc công cụ desktop đọc Accessibility Tree) hướng dẫn từng bước trực tiếp trên giao diện sống: chỉ đánh dấu bước kế tiếp khi xác nhận trạng thái UI hiện tại khớp điều kiện, vẽ *coachmark* trực tiếp quanh phần tử thật, không phụ thuộc nhà phát triển nhúng WalkMe/TipKit.
- **AI trụ cột (*load-bearing*):** Apple Guide chết vì chi phí viết tay kịch bản kiểm tra trạng thái quá đắt. AI đa phương thức kết hợp DOM/Accessibility Tree có thể **biên dịch tài liệu hướng dẫn tĩnh hoặc mục tiêu người dùng thành chuỗi bước gắn neo phần tử UI sống**, tự thích nghi khi tên nút/vị trí menu đổi giữa các phiên bản và từ chối hướng dẫn nếu phần tử thực sự không tồn tại (chống ảo giác).
- **AI trang trí (*decorative — cần tránh*):** Thanh bên chatbot trả lời văn bản *"Bước 1: vào Settings → Bước 2: bấm Advanced"* mà không đọc trạng thái trang thực tế.
- **Khả thi lát cắt demo (~9 ngày):** Trung bình–Cao nếu giới hạn lát cắt trên trình duyệt (Chrome/Web Extension đọc DOM sống trên 2–3 ứng dụng web phức tạp công khai); khó hơn nếu làm ở cấp OS đa nền tảng.

### A-P3 — Hồi sinh tinh thần Usenet/NNTP thành "Open Knowledge Harvester" cho cộng đồng chat nhỏ
- **Giá trị đương đại:** Phục hồi quyền sở hữu tri thức công khai, lập chỉ mục được và di chuyển được (xuất kho tĩnh HTML + RSS/Atom + chuẩn mở) cho các cộng đồng dưới 1.000 thành viên trên Discord/Slack/Matrix — nhóm bị Discord Server Web Pages bỏ rơi — cũng như kho lịch sử trước tháng 12/2026 [R17].
- **AI trụ cột (*load-bearing*):** Dòng chat thời gian thực có nhiều cuộc hội thoại đan xen, ảnh chụp lỗi rời rạc và câu chốt lời giải không có ranh giới rõ ràng — điều bot dựa trên quy tắc cố định không thể gom sạch. AI đóng vai trò **tách luồng hội thoại đan xen (*thread disentanglement*)**, hợp nhất thành cặp *Vấn đề → Môi trường → Lời giải đã xác nhận*, che mờ dữ liệu cá nhân (*PII redaction*) và yêu cầu người điều hành duyệt 1 chạm trước khi xuất bản.
- **AI trang trí (*decorative — cần tránh*):** Chỉ chạy tóm tắt kênh chat chung chung kiểu *"Hôm nay mọi người thảo luận về lỗi cài đặt"* (điều Discord đã tự làm cho máy chủ lớn).
- **Khả thi lát cắt demo (~9 ngày):** Cao — có thể trình diễn trọn vẹn trên một bộ dữ liệu xuất chat công khai có giấy phép hợp lệ (hoặc máy chủ thử nghiệm), xuất ra trang tri thức tĩnh tìm kiếm được + RSS/archive chuẩn mở.

### A-P4 — Hồi sinh Del.icio.us + Pocket thành "Local-First Rot-Proof Collective Library"
- **Giá trị đương đại:** Kết hợp bản lưu bất biến cục bộ (*local-first* bằng tệp chuẩn mở không mất khi ngừng trả phí SaaS như Raindrop Pro [R22] hay khi công ty đóng cửa như Pocket [R19]) với khả năng xuất/chia sẻ bộ sưu tập theo thẻ (*folksonomy*) gọn nhẹ không cần quản trị Docker như ArchiveBox/Karakeep.
- **AI trụ cột (*load-bearing*):** (1) **Phát hiện mục rữa ngữ nghĩa (*semantic link-rot & hijack detection*)** — nhận diện trang vẫn trả HTTP 200 nhưng thực chất đã thành trang đỗ tên miền, tường trả phí hoặc trang spam mua lại tên miền cũ (điều kiểm tra HTTP status đơn thuần bỏ sót); (2) **Tự động chuẩn hóa *folksonomy* và truy xuất theo khẳng định/trích dẫn** từ bản chụp cục bộ đã lưu, giảm gánh nặng gắn thẻ thủ công từng làm người dùng bỏ Del.icio.us.
- **AI trang trí (*decorative — cần tránh*):** Tóm tắt bài viết 3 gạch đầu dòng đơn thuần (đã phổ biến khắp các trình duyệt/extension).
- **Khả thi lát cắt demo (~9 ngày):** Cao — ứng dụng cục bộ/trình duyệt nhập tệp xuất Pocket CSV/HTML bookmarks, chụp bản lưu cục bộ, kiểm tra *semantic rot* và dựng đồ thị thẻ có thể xuất ra gói tĩnh chia sẻ được.

### A-P5 — Hồi sinh InfoPath thành "Open Legacy Form Archaeologist & Runner"
- **Giá trị đương đại:** Công cụ phân tích tệp mẫu `.xsn` (bản chất là gói CAB chứa `manifest.xsf`, lược đồ XSD, giao diện XSLT và quy tắc XPath) cùng các bản ghi `.xml` lịch sử sau hạn khai tử 14/07/2026 [R25, R27], giúp tổ chức vừa **xem/in/kiểm toán dữ liệu XML cũ ngoại tuyến** vừa **chuyển biểu mẫu sang chuẩn web mở** (JSON Schema/HTML Form) không lệ thuộc gói Power Apps Premium 20 USD/người dùng/tháng [R29].
- **AI trụ cột (*load-bearing*):** Phần khó nhất của di dời InfoPath không phải vẽ lại ô nhập liệu mà là giải mã hàng chục quy tắc điều kiện XPath lồng nhau, kết nối dữ liệu phụ và bảng lặp thiếu tài liệu. AI (kết hợp bộ phân tích cú pháp XML/XSLT tất định) **giải thích quy tắc nghiệp vụ ẩn bằng ngôn ngữ dễ kiểm duyệt, sinh bộ kiểm thử đối chiếu hành vi biểu mẫu cũ-mới, và đánh dấu rõ phần phụ thuộc SOAP/SharePoint cần con người quyết định**.
- **AI trang trí (*decorative — cần tránh*):** "Tạo biểu mẫu mới từ prompt văn bản" (không giải quyết kho `.xsn`/`.xml` lịch sử).
- **Khả thi lát cắt demo (~9 ngày):** Cao nếu dùng mẫu `.xsn`/`.xml` tự tạo hoặc mã nguồn mở hợp pháp; giá trị trình diễn rất rõ về mặt kỹ thuật (kéo tệp `.xsn` chết vào → tách quy tắc + chạy biểu mẫu web sống + hiển thị hồ sơ `.xml` cũ).

### A-P6 — Hồi sinh DMOZ & Webrings thành "Provenance-Audited Topic Guilds"
- **Giá trị đương đại:** Khôi phục khám phá web phi thương mại theo chuyên ngành hẹp dưới dạng các vòng liên kết/danh mục nhỏ có kiểm chứng nguồn gốc con người, giúp người dùng tránh vòng xoáy *affiliate SEO spam* [R32] và làn sóng trang web sinh AI hàng loạt [R34] mà không phải trả phí tìm kiếm hàng tháng như Kagi [R36].
- **AI trụ cột (*load-bearing*):** DMOZ sụp đổ một phần vì chi phí bảo trì thủ công khi web phình to và biến đổi liên tục. AI đóng vai trò **trợ lý kiểm toán định kỳ cho nhóm biên tập nhỏ**: tự động quét phát hiện trang trong danh mục đổi chủ, chèn dày đặc liên kết tiếp thị liên kết, chuyển sang xuất bản nội dung tự động hàng loạt, hoặc chết liên kết — giữ quyết định duyệt/loại ở con người nhưng giảm 80–90% lao động kiểm tra lặp lại (*GIẢ THUYẾT về tỷ lệ giảm công*).
- **AI trang trí (*decorative — cần tránh*):** Dùng LLM tự sinh danh sách "Top 10 website hay nhất về chủ đề X" (phản tác dụng vì mất hoàn toàn giá trị kiểm định con người).
- **Khả thi lát cắt demo (~9 ngày):** Trung bình–Cao về mặt công cụ kiểm toán & xuất danh mục/webring tĩnh; rủi ro nằm ở việc không chứng minh được cộng đồng biên tập thực trong 9 ngày.

### A-P7 — Hồi sinh tinh thần Stack Overflow thành "Verified Edge-Case Field Notes" *(Revisited)*
- **Giá trị đương đại:** Không cố xây lại diễn đàn hỏi-đáp chung (vốn đã bị coding agent thay thế cho 90%+ câu hỏi thường [R38, R40]), mà hồi sinh chức năng **biến một lần gỡ lỗi biên thành công thành chứng cứ kỹ thuật công khai có khả năng tái lập** (gắn chặt phiên bản thư viện/OS, tối thiểu hóa log tái hiện, và kết quả kiểm chứng thực tế) — phục vụ đồng thời lập trình viên và công cụ AI tra cứu nguồn có bằng chứng.
- **AI trụ cột (*load-bearing*):** Lý do lập trình viên ngại đăng Stack Overflow trước đây là tốn công gọt giũa *Minimal Reproducible Example* và sợ bị kiểm duyệt đóng bài [R39]. AI làm việc trực tiếp từ dấu vết sửa lỗi cục bộ (*diff*, phiên bản lockfile, log lỗi trước/sau) để **tự động ẩn danh bí mật/mã riêng tư, cô lập đúng điều kiện kích hoạt lỗi và sinh bản ghi *field note* có thể kiểm thử tự động**, hạ chi phí đóng góp về gần bằng 0.
- **AI trang trí (*decorative — cần tránh*):** Một trang Q&A mới có bot AI tự trả lời câu hỏi thay con người (trùng lặp với ChatGPT/Stack Overflow AI Assist).
- **Khả thi lát cắt demo (~9 ngày):** Cao — có thể demo luồng từ một phiên sửa lỗi thật (kèm `package.json`/lockfile + test fail → pass) tự động đóng gói thành hồ sơ lỗi biên đã ẩn danh, kiểm tra độ khớp phiên bản và xuất bản công khai/MCP cho cả người lẫn agent tra cứu.

---

## 7. Counterevidence and limitations

### Bằng chứng phản biện & phép thử bác bỏ nhỏ nhất theo từng không gian

1. **A-P1 (Yahoo! Pipes):**
   - *Bằng chứng phản biện mạnh nhất:* **n8n** [R07], **RSSHub** [R08c] và **Feedly Leo** [R08e] đã tồn tại trưởng thành. Ngoài ra, khảo sát Pew 2026 [R06] chứng minh sự mệt mỏi tin tức, *không* chứng minh đa số người mệt mỏi tin tức muốn tự lắp ráp đường ống dữ liệu (nhiều người chọn tránh tin hoặc xem video ngắn hơn là tự cấu hình bộ lọc).
   - *Phép thử bác bỏ nhỏ nhất:* Mời 5 nhà nghiên cứu/nhà báo đang theo dõi ≥5 nguồn web không có RSS thử dựng 1 luồng theo dõi trong 15 phút; nếu họ vẫn quay về kiểm tra thủ công hoặc thấy Feedly/Google Alerts đã đủ, giả thuyết nhu cầu bị bác bỏ.

2. **A-P2 (Apple Guide):**
   - *Bằng chứng phản biện mạnh nhất:* **Copilot Vision** và **Gemini Live** (2025–2026) đang phổ cập nhanh khả năng nhìn màn hình và chỉ dẫn bằng giọng nói mà không cần cài tiện ích riêng; với phần mềm phổ thông, video ngắn 60 giây trên YouTube/TikTok thường đủ nhanh. Đồng thời, đọc DOM/Accessibility Tree trên ứng dụng phức tạp (như canvas WebGL của Blender/Figma) vẫn gặp giới hạn kỹ thuật cứng.
   - *Phép thử bác bỏ nhỏ nhất:* Quan sát 5 người dùng thực hiện cùng 1 tác vụ nhiều bước trên một cổng web/phần mềm vừa đổi giao diện (như cài đặt quyền riêng tư/thuế hoặc OBS) dùng chatbot/Copilot Vision so với lớp phủ *coachmark* bám DOM; nếu tỷ lệ hoàn thành và thời gian không cải thiện rõ rệt, giá trị *coachmark* không vượt nổi AI chia sẻ màn hình.

3. **A-P3 (Usenet / Cộng đồng chat khép kín):**
   - *Bằng chứng phản biện mạnh nhất:* Chính **Discord đã ra mắt Server Web Pages** (thông báo 10/2026, mở rộng 11–12/2026 [R17]) khiến dự án dẫn đầu **Answer Overflow phải thu hẹp hoạt động** [R17]. Ngoài ra, quyền riêng tư là rào cản nhạy cảm: nhiều thành viên Discord cố tình chọn chat vì *không muốn* lời nói của mình xuất hiện trên Google.
   - *Phép thử bác bỏ nhỏ nhất:* Hỏi trực tiếp 5 quản trị viên máy chủ Discord kỹ thuật/sở thích quy mô 100–900 thành viên xem họ có thực sự muốn xuất bản lịch sử hỗ trợ lên web công khai không, hay chính cộng đồng phản đối vì lo ngại quyền riêng tư/ít lợi ích.

4. **A-P4 (Del.icio.us & Mozilla Pocket):**
   - *Bằng chứng phản biện mạnh nhất:* Sự thất bại thương mại của cả Del.icio.us (bán giá 35.000 USD năm 2017 [R18]) lẫn Pocket (Mozilla đóng cửa 2025 vì thay đổi thói quen dùng web [R19]) là **bằng chứng trực tiếp rằng đa số người dùng đại chúng không sẵn sàng trả tiền hoặc duy trì thói quen quản lý bookmark/read-later độc lập**. Với nhóm kỹ thuật sẵn sàng lưu trữ nghiêm túc, **Karakeep** [R23] và **ArchiveBox** [R24] đã miễn phí và mạnh.
   - *Phép thử bác bỏ nhỏ nhất:* Lấy tệp xuất bookmark/Pocket CSV thật từ 5 người dùng (chứa ≥100 liên kết trên 2 năm), đo tỷ lệ liên kết hỏng/*soft-404* mà họ thực sự *cần truy cập lại* trong 30 ngày; nếu phần lớn liên kết cũ không bao giờ được mở lại ("nghĩa địa bookmark"), nhu cầu thực tế sẽ rất hẹp.

5. **A-P5 (Microsoft InfoPath):**
   - *Bằng chứng phản biện mạnh nhất:* Microsoft đã thông báo ngừng phát triển InfoPath hơn một thập kỷ trước hạn 14/07/2026 [R25]; nhiều doanh nghiệp lớn đã di dời xong sang Power Apps hoặc giải pháp thương mại (Plumsail/Nintex). Thêm vào đó, trong khuôn khổ hackathon 9 ngày, rất khó tiếp cận bộ tệp `.xsn`/`.xml` nội bộ thật từ tổ chức vì chứa dữ liệu nghiệp vụ nhạy cảm, và phân khúc khách hàng là B2B/IT nội bộ có chu kỳ chấp nhận phần mềm chậm.
   - *Phép thử bác bỏ nhỏ nhất:* Khảo sát 5 quản trị viên SharePoint/IT tổ chức vừa-nhỏ xem họ còn bao nhiêu biểu mẫu InfoPath tồn đọng (đặc biệt trên SharePoint Server SE trước hạn xóa tháng 07/2027 [R27]) và liệu quy định bảo mật có cho phép họ chạy công cụ bên thứ ba/AI trên tệp `.xsn`/`.xml` nội bộ hay không.

6. **A-P6 (DMOZ & Webrings):**
   - *Bằng chứng phản biện mạnh nhất:* Chính nghiên cứu của **Ahrefs (07/07/2025, 600.000 trang)** [R35] cho thấy tỷ lệ trang AI trong nhóm xếp hạng cao trên Google không đơn giản là "AI chiếm trọn mọi tìm kiếm", và người dùng ngày càng dùng AI search (Perplexity/ChatGPT Search) hoặc Kagi/Reddit để lọc thay vì duyệt danh mục phân cấp. Thêm nữa, mọi danh mục cộng đồng đều đối mặt bài toán khởi động lạnh (*cold-start*) và động cơ duy trì biên tập viên tình nguyện — điều phần mềm không tự giải quyết được.
   - *Phép thử bác bỏ nhỏ nhất:* So sánh 20 truy vấn tìm nguồn học tập/sản phẩm trung lập giữa tìm kiếm thường, Kagi/Marginalia và một danh mục nhỏ có kiểm định; đo xem người dùng có thực sự quay lại dùng danh mục sau lần thử đầu tiên không.

7. **A-P7 (Stack Overflow / Tri thức lỗi biên — Revisited):**
   - *Bằng chứng phản biện mạnh nhất:* **Sụp đổ lượng câu hỏi trên Stack Overflow [R38] cũng đồng thời là bằng chứng mạnh rằng coding agent đã giải quyết đủ tốt phần lớn nhu cầu hàng ngày của lập trình viên.** Không có gì đảm bảo lập trình viên muốn chia sẻ log sửa lỗi từ công việc (vốn vướng NDA/bảo mật công ty) để nuôi một kho công cộng mới; ngoài ra, công cụ AI ngày càng đọc thẳng mã nguồn thư viện và GitHub Issues qua MCP/web search.
   - *Phép thử bác bỏ nhỏ nhất:* Thử ghi nhận 10 lỗi biên thực tế của 5 lập trình viên với các thư viện phát hành năm 2026: đếm xem bao nhiêu lỗi khiến coding agent hiện tại thất bại lặp lại và liệu bản ghi lỗi biên đã ẩn danh có giúp agent/người khác giải ngay lần đầu hay không.

### Hạn chế phương pháp chung của báo cáo Pha 1
- Toàn bộ bằng chứng nhu cầu hiện tại trong Pha 1 đến từ nguồn công khai, khảo sát quy mô lớn và kiểm chứng API trực tiếp; **chưa thực hiện phỏng vấn người dùng thực hay thử nghiệm nguyên mẫu**.
- Một số trang tài liệu (như `support.discord.com`, `support.mozilla.org`, `techcommunity.microsoft.com`, `meta.stackoverflow.com`) chặn truy cập tự động bằng HTTP 403 hoặc cơ chế chống bot; các điểm dữ liệu liên quan đã được thay bằng nguồn gốc mở khác hoặc đánh dấu rõ mức độ suy luận.

---

## 8. Challenged assumptions

| Giả định cũ | Phán quyết (Verdict) | Bằng chứng & lập luận phản biện |
|---|---|---|
| **A1:** Người dùng mục tiêu phải là cá nhân hoặc gia đình tại Mỹ–Âu với vấn đề phổ biến đại chúng. | **BÁC BỎ (CHALLENGED — quá hẹp và không có trong luật thi)** | Luật chính thức Kiroween 2026 [R01] chỉ yêu cầu *Potential Impact*: *"solving a real problem for a real audience … Would someone actually use this?"* — hoàn toàn **không giới hạn** ở cá nhân/gia đình Mỹ–Âu. Việc tự bó vào hộ gia đình Mỹ–Âu đã vô tình bỏ qua các nỗi đau cấp bách có thời hạn rõ ràng ở tổ chức/giáo dục/nhóm chuyên môn như hạn khai tử InfoPath 2026–2027 (`A-P5`), cộng đồng mã nguồn mở bị bỏ rơi bởi Discord Server Web Pages (`A-P3`), hay nhà báo/nhà nghiên cứu toàn cầu đối mặt quá tải thuật toán (`A-P1`). |
| **A2:** Yếu tố Resurrection bắt buộc phải là một *công nghệ vật lý/phần mềm đã chết* (thay vì quy trình, tập quán xã hội hay cấu trúc cộng đồng). | **ĐIỀU CHỈNH (NUANCED — tách rõ phần "mỏ neo" và phần "giá trị lõi")** | Giá trị hiện đại nằm chủ yếu ở **quy trình và cấu trúc đã mất** (lọc dữ liệu minh bạch `A-P1`, hướng dẫn bám trạng thái UI `A-P2`, tri thức cộng đồng mở lập chỉ mục được `A-P3`, thẩm định nguồn gốc con người `A-P6`), không nằm ở hoài niệm phần cứng cũ. Tuy nhiên, vì Vòng 1 Kiroween chấm Đạt/Không đạt theo chủ đề *"Bring your favorite dead technology back to life"* [R01], mỗi không gian vẫn cần **neo vào một công nghệ/nền tảng cụ thể đã chết hoặc suy tàn có kiểm chứng** (Yahoo! Pipes, Apple Guide, Usenet/Google Groups, Del.icio.us/Pocket, InfoPath, DMOZ) để vừa qua cổng chủ đề vừa giữ giá trị thực. |
| **A3:** Có đối thủ đã bao phủ một phần vấn đề là đủ để loại bỏ ý tưởng. | **BÁC BỎ (CHALLENGED — sai lầm về cấu trúc cạnh tranh)** | Bằng chứng thực tế cho thấy ở hầu hết không gian sống động, đối thủ mạnh nhất đều tồn tại **lỗ hổng cấu trúc có kiểm chứng**: Raindrop.io xóa bản lưu web sau ~1 tháng hết Pro [R22]; Power Apps tính phí 20 USD/người dùng/tháng và không chuyển đổi tự động `.xsn` [R29]; WalkMe thuộc SAP có giá hợp đồng doanh nghiệp và đòi tích hợp từ chủ app [R12]; Discord Server Web Pages loại toàn bộ máy chủ <1.000 thành viên và lịch sử trước 12/2026 [R17]. Việc có đối thủ lớn là dấu hiệu **có nhu cầu thật**, không phải lý do loại tự động nếu xác định được phân đoạn bị bỏ quên rõ ràng. |
| **A4:** Các vấn đề hướng tới lập trình viên (Stack Overflow, mã cũ, cộng đồng kỹ thuật) là lựa chọn kém phù hợp. | **BÁC BỎ MỘT PHẦN (CHALLENGED WITH CAVEAT)** | Hai lý do chính: (1) Kiểm chứng tái lập qua Stack Exchange API ngày 25/11/2026 chứng minh lượng câu hỏi mới trên Stack Overflow đã giảm **99,59%** so với đỉnh (còn 843 câu hỏi tháng 10/2026 [R38]) — phủ nhận nhận định cũ ở chu kỳ 16–21 rằng nền tảng này "chưa đủ chết"; (2) Cuộc thi do AWS/Kiro tổ chức với hội đồng giám khảo công nghệ [R01], nên các vấn đề kỹ thuật/prosumer (`A-P3`, `A-P5`, `A-P7`) dễ tạo cảm nhận *"Would someone actually use this?"* hơn hẳn bài toán gia đình chưa có bằng chứng. *Cảnh báo đi kèm:* Bài toán cho lập trình viên đối mặt rào cản khác biệt rất cao trước chính coding agent hiện đại, nên phải chứng minh rõ giá trị mà agent riêng lẻ không làm được. |
| **A5:** Kết quả lặp lại "0 PROMISING" sau 26 chu kỳ có nghĩa là không gian ý tưởng đã cạn kiệt. | **BÁC BỎ (CHALLENGED — lỗi do bộ lọc chồng chéo quá chặt)** | Rà soát `ideas/all-candidates.md` và `ideas/rejected.md` cho thấy kết quả 0/41 PROMISING xuất phát từ **bộ lọc giao hội (conjunctive over-filtering)**: đòi hỏi đồng thời (i) công nghệ cổ/chết rõ ràng, (ii) người dùng cá nhân/gia đình Mỹ–Âu đại chúng, (iii) không trùng chức năng với bất kỳ công cụ nào hiện có, và (iv) phải có bằng chứng phỏng vấn sơ cấp trước khi chọn hướng. Hầu hết ý tưởng bị loại ở chu kỳ 1–8 (như C09, C13, C20, C30–C41) vốn xuất phát từ "nhìn đồ cổ rồi tìm việc cho nó" thay vì nhìn **các đứt gãy công nghệ vừa xảy ra năm 2024–2026** (Google Groups bỏ Usenet 2024, Pocket đóng cửa 2025, InfoPath khai tử 07/2026, Stack Overflow sụp đổ 2026). Không gian tìm kiếm hoàn toàn chưa cạn kiệt. |

---

## 9. Unresolved questions

1. **Quyền riêng tư và đồng thuận dữ liệu cộng đồng (`A-P3`, `A-P7`):** Với `A-P3`, tỷ lệ thành viên trong các máy chủ Discord <1.000 thành viên chấp thuận xuất bản ẩn danh luồng hỗ trợ ra web công khai là bao nhiêu? Với `A-P7`, cơ chế nào đảm bảo việc chia sẻ *field note* sửa lỗi từ repo công việc không rò rỉ bí mật kinh doanh/NDA?
2. **Độ sâu tồn đọng InfoPath thực tế cuối 2026 (`A-P5`):** Bao nhiêu phần trăm tổ chức chạy SharePoint Server Subscription Edition vẫn còn phụ thuộc InfoPath trước hạn xóa mã 13/07/2027, và có sẵn kho tệp `.xsn`/`.xml` mẫu công khai có giấy phép mở đủ phức tạp để kiểm thử hay không?
3. **Ngưỡng vượt trội trước AI đa phương thức sẵn có (`A-P2`):** Trong tác vụ thực tế trên giao diện web/desktop phức tạp, lớp phủ *coachmark* bám DOM/Accessibility Tree giảm tỷ lệ sai thao tác bao nhiêu so với việc người dùng mở trực tiếp Copilot Vision hoặc Gemini Live?
4. **Hành vi thực tế sau "mệt mỏi tin tức" và "đóng cửa Pocket" (`A-P1`, `A-P4`):** Trong nhóm 52% người trưởng thành Mỹ báo cáo mệt mỏi tin tức [R06] hoặc nhóm từng xuất CSV từ Pocket năm 2025, tỷ lệ thực sự muốn *công cụ tự chủ động lọc/lưu trữ* là bao nhiêu so với nhóm chỉ đơn giản giảm đọc hoặc chuyển sang trình duyệt mặc định?
5. **Động lực duy trì dài hạn của cộng đồng biên tập (`A-P6`):** Nếu AI gánh phần kiểm toán *link rot* và *slop drift*, động cơ nào khiến con người tiếp tục tuyển chọn và xác thực nguồn mới thay vì bỏ dở như lịch sử nhiều chuyên mục DMOZ?
6. **Khớp nối tính năng Kiro theo tiêu chí 20% Technological Implementation [R01]:** Trong 7 không gian trên, không gian nào tận dụng rõ nhất các năng lực đặc thù của Kiro (spec-driven development, agent hooks, steering, MCP, property-based testing) mà không gượng ép? *(Câu hỏi dành cho giai đoạn đánh giá/thu hẹp tiếp theo, không quyết định ở Pha 1.)*

---

## 10. Evaluated references

*Quy ước điểm 7 tiêu chí (0–5): `A` = Source Authority (20%), `T` = Technical Evidence (20%), `M` = Mechanism Correctness (20%), `C` = Context Fit (15%), `F` = Freshness (10%), `R` = Reproducibility (10%), `B` = Commercial/Opinion Bias (5%, điểm càng cao càng ít thiên vị).*  
*Công thức Weighted Score (0–100) = `4×A + 4×T + 4×M + 3×C + 2×F + 2×R + 1×B`.*  
*Tất cả URL dưới đây đã được truy cập và kiểm chứng trực tiếp ngày `2026-11-25` (HTTP 200 hoặc snapshot cục bộ đối chiếu từ nguồn chính thức).*

| Ref ID | URL | Title | Publisher | Pub Date | Accessed | Claims Supported | Scores (A/T/M/C/F/R/B) | Weighted | Source Reliability | Reference Relevance |
|---|---|---|---|---|---|---|---|---|---|---|
| R01 | https://kiroween.devpost.com/rules | Kiroween 2026 Official Rules (snapshot: `sources/kiroween-official-rules-2026-11-25.txt`) | AWS / Devpost | 2026-11-16 | 2026-11-25 | Scope, A1–A5 | 5/5/5/5/5/5/5 | 100 | High | High |
| R02 | https://uk.pcmag.com/web-sites/42482/yahoo-shutting-down-maps-and-pipes | Yahoo Shutting Down Maps and Pipes | PCMag UK | 2015-06-04 | 2026-11-25 | A-P1-C1 | 4/3/4/5/5/5/4 | 83 | High | High |
| R03 | https://extinction.zkm.de/events/yahoo-pipes-shutdown | Yahoo Pipes shut down — Net Art Extinction Timeline | ZKM Center for Art and Media | N/A | 2026-11-25 | A-P1-C1 | 4/3/4/4/4/5/5 | 79 | High | High |
| R04 | https://en.wikipedia.org/wiki/Yahoo_Pipes | Yahoo Pipes | Wikipedia | N/A (updated) | 2026-11-25 | A-P1-C1 | 3/3/4/5/4/5/4 | 77 | Medium | High |
| R05 | https://reutersinstitute.politics.ox.ac.uk/digital-news-report/2026/dnr-executive-summary | Overview and key findings of the 2026 Digital News Report | Reuters Institute (Oxford) | 2026-06-16 | 2026-11-25 | A-P1-C2, A-P1-C3 | 5/5/4/4/5/5/5 | 93 | High | High |
| R06 | https://www.pewresearch.org/journalism/2026/02/11/americans-complicated-relationship-with-news/ | Americans’ Complicated Relationship With News | Pew Research Center | 2026-02-11 | 2026-11-25 | A-P1-C2, A-P1-C3 | 5/5/4/4/5/5/5 | 93 | High | High |
| R07 | https://github.com/n8n-io/n8n | n8n — Fair-code workflow automation platform | n8n GmbH (GitHub) | Active 2026 | 2026-11-25 | A-P1-C3, Alt A-P1 | 5/5/5/4/5/5/3 | 95 | High | High |
| R08 | https://n8n.io/pricing/ | n8n Plans and Pricing | n8n GmbH | 2026 | 2026-11-25 | Alt A-P1 | 5/4/4/4/5/5/2 | 86 | High | High |
| R08b | https://github.com/huginn/huginn | Huginn — Create agents that monitor and act on your behalf | Huginn Contributors (GitHub) | Active 2026 | 2026-11-25 | A-P1-C3, Alt A-P1 | 5/5/5/5/4/5/4 | 97 | High | High |
| R08c | https://github.com/DIYgod/RSSHub | RSSHub — Everything is RSSible | DIYgod / RSSHub (GitHub) | Active 2026 | 2026-11-25 | A-P1-C3, Alt A-P1 | 5/5/5/4/5/5/4 | 96 | High | High |
| R08d | https://github.com/RSS-Bridge/rss-bridge | RSS-Bridge — The RSS feed for websites missing it | RSS-Bridge Contributors (GitHub) | Active 2026 | 2026-11-25 | A-P1-C3, Alt A-P1 | 5/5/5/4/5/5/5 | 97 | High | High |
| R08e | https://feedly.com/i/pro | Stay ahead of the curve with Feedly AI | Feedly | 2026 | 2026-11-25 | Alt A-P1 | 5/3/4/4/5/5/2 | 82 | Medium | High |
| R09 | https://tidbits.com/1994/09/19/anarchie-apple-guide/ | Anarchie & Apple Guide (TidBITS-244) | TidBITS | 1994-09-19 | 2026-11-25 | A-P2-C1 | 4/4/4/5/5/5/4 | 87 | High | High |
| R10 | https://tidbits.com/1994/12/12/os-directions-marconi-copland-and-gershwin/ | OS Directions: Marconi, Copland, and Gershwin (TidBITS-251) | TidBITS | 1994-12-12 | 2026-11-25 | A-P2-C1 | 4/3/4/4/5/5/4 | 80 | High | Medium |
| R11 | https://en.wikipedia.org/wiki/Macintosh_Guide | Macintosh Guide | Wikipedia | N/A (updated) | 2026-11-25 | A-P2-C1 | 3/3/4/5/4/5/4 | 77 | Medium | High |
| R12 | https://news.sap.com/2024/06/sap-enters-agreement-to-acquire-walkme/ | SAP Enters into Agreement to Acquire WalkMe | SAP News Center | 2024-06-05 | 2026-11-25 | A-P2-C2, A-P2-C3 | 5/4/4/4/4/5/2 | 84 | High | High |
| R13 | https://developer.apple.com/documentation/TipKit | TipKit — Apple Developer Documentation | Apple Inc. | Active 2026 | 2026-11-25 | A-P2-C2, A-P2-C3 | 5/5/5/4/5/5/4 | 96 | High | High |
| R14 | https://support.google.com/groups/answer/11036538 | Google Groups ending support for Usenet | Google LLC | 2024 | 2026-11-25 | A-P3-C1 | 5/5/5/5/5/5/4 | 99 | High | High |
| R14b | https://en.wikipedia.org/wiki/Gmane | Gmane | Wikipedia | N/A (updated) | 2026-11-25 | A-P3 History | 3/3/4/4/4/5/4 | 74 | Medium | Medium |
| R15 | https://www.discourse.org/ | Discourse — One platform. Any community. | Civilized Discourse Construction Kit | 2026 | 2026-11-25 | Alt A-P3 | 5/3/4/4/5/5/2 | 82 | Medium | Medium |
| R16 | https://github.com/AnswerOverflow/AnswerOverflow | AnswerOverflow — Powering Discord content discovery | AnswerOverflow (GitHub) | Active 2026 | 2026-11-25 | A-P3-C2, Alt A-P3 | 5/5/5/5/5/5/3 | 98 | High | High |
| R17 | https://www.serverfront.app/blog/answer-overflow-is-winding-down | Answer Overflow is winding down. Here are your three options. | Serverfront | 2026-11-05 | 2026-11-25 | A-P3-C2, A-P3-C3, Alt A-P3 | 3/4/4/5/5/4/2 | 79 | Medium | High |
| R18 | https://blog.pinboard.in/2017/06/pinboard_acquires_delicious/ | Pinboard Acquires Delicious | Pinboard Blog (Maciej Cegłowski) | 2017-06-01 | 2026-11-25 | A-P4-C1 | 5/5/5/5/5/5/4 | 99 | High | High |
| R19 | https://blog.mozilla.org/en/mozilla/building-whats-next/ | Investing in what moves the internet forward | Mozilla Blog | 2025-05-22 | 2026-11-25 | A-P4-C1 | 5/5/5/5/5/5/3 | 98 | High | High |
| R20 | https://www.niemanlab.org/2025/05/mozilla-shuts-down-pocket/ | Mozilla is shutting down Pocket, its read-it-later app | Nieman Journalism Lab | 2025-05-22 | 2026-11-25 | A-P4-C1 | 4/4/4/5/5/5/4 | 87 | High | High |
| R21 | https://www.pewresearch.org/data-labs/2024/05/17/when-online-content-disappears/ | When Online Content Disappears (Link Rot and Digital Decay) | Pew Research Center | 2024-05-17 | 2026-11-25 | A-P4-C2, A-P6 Alt | 5/5/5/5/4/5/5 | 98 | High | High |
| R22 | https://help.raindrop.io/web-archive | Web archive — Raindrop.io Help | Raindrop.io | 2026 | 2026-11-25 | A-P4-C3, Alt A-P4 | 5/5/5/5/5/5/4 | 99 | High | High |
| R23 | https://github.com/karakeep-app/karakeep | Karakeep (formerly Hoarder) — Self-hostable bookmark-everything app | Karakeep Contributors (GitHub) | Active 2026 | 2026-11-25 | A-P4-C3, Alt A-P4 | 5/5/5/5/5/5/4 | 99 | High | High |
| R24 | https://github.com/ArchiveBox/ArchiveBox | ArchiveBox — Open source self-hosted web archiving | ArchiveBox Contributors (GitHub) | Active 2026 | 2026-11-25 | A-P4-C3, Alt A-P4 | 5/5/5/5/5/5/4 | 99 | High | High |
| R25 | https://learn.microsoft.com/en-us/lifecycle/products/infopath-2013 | InfoPath 2013 — Microsoft Lifecycle | Microsoft Learn | 2026 | 2026-11-25 | A-P5-C1 | 5/5/5/5/5/5/5 | 100 | High | High |
| R26 | https://learn.microsoft.com/en-us/sharepoint/what-s-new/what-s-deprecated-or-removed-from-sharepoint-server-subscription-edition | What's deprecated or removed from SharePoint Server Subscription Edition? | Microsoft Learn | 2026 | 2026-11-25 | A-P5-C1, A-P5-C2 | 5/5/5/5/5/5/4 | 99 | High | High |
| R27 | https://blog.stefan-gossner.com/2026/11/10/important-sharepoint-2010-workflows-and-infopath-forms-services-will-be-removed-with-july-2027-cu/ | Important: SharePoint 2010 Workflows and InfoPath Forms Services will be removed with July 2027 CU | Stefan Goßner (Microsoft SharePoint Escalation Engineer) | 2026-11-10 | 2026-11-25 | A-P5-C1, A-P5-C3 | 5/5/5/5/5/5/4 | 99 | High | High |
| R28 | https://its.wsu.edu/2026/07/06/infopath-forms-in-sharepoint-online-retire-7-14/ | InfoPath Forms in SharePoint Online Retire 7/14 | Washington State University ITS | 2026-07-06 | 2026-11-25 | A-P5-C1, A-P5-C3 | 5/4/5/5/5/5/5 | 96 | High | High |
| R29 | https://www.microsoft.com/en-us/power-platform/products/power-apps/pricing | Power Apps Licensing and Pricing | Microsoft | 2026 | 2026-11-25 | A-P5-C2, Alt A-P5 | 5/5/5/5/5/5/3 | 98 | High | High |
| R30 | https://curlie.org/docs/en/about.html | About Curlie | Curlie (Open Directory Project successor) | N/A (live) | 2026-11-25 | A-P6-C1, Alt A-P6 | 5/3/4/5/4/5/4 | 85 | High | High |
| R31 | https://en.wikipedia.org/wiki/DMOZ | DMOZ | Wikipedia | N/A (updated) | 2026-11-25 | A-P6-C1 | 3/3/4/5/4/5/4 | 77 | Medium | High |
| R32 | https://github.com/webis-de/ecir24-seo-spam-in-search-engines | Is Google Getting Worse? A Longitudinal Investigation of SEO Spam in Search Engines (ECIR 2024 code & data) | Webis Group (Leipzig Univ. / Bauhaus-Univ. Weimar) | 2024-03 | 2026-11-25 | A-P6-C2 | 5/5/5/5/4/5/5 | 98 | High | High |
| R33 | https://opensearchfoundation.org/is-google-search-getting-worse-new-long-term-study-by-the-webis-research-group/ | Is Google search getting worse? New long-term study by the Webis research group | Open Search Foundation | 2024-05-09 | 2026-11-25 | A-P6-C2 | 4/4/4/5/4/5/4 | 85 | High | High |
| R34 | https://ahrefs.com/blog/what-percentage-of-new-content-is-ai-generated/ | 74% of New Webpages Include AI Content (Study of 900k Pages) | Ahrefs | 2025-05-19 | 2026-11-25 | A-P6-C3 | 4/4/4/4/5/3/3 | 79 | Medium | High |
| R35 | https://ahrefs.com/blog/ai-generated-content-does-not-hurt-your-google-rankings/ | AI-Generated Content Does Not Hurt Your Google Rankings (600,000 Pages Analyzed) | Ahrefs | 2025-07-07 | 2026-11-25 | A-P6-C3, Counterevidence A-P6 | 4/4/4/4/5/3/3 | 79 | Medium | High |
| R36 | https://kagi.com/pricing | Kagi Search Pricing and Plans | Kagi Inc. | 2026 | 2026-11-25 | Alt A-P6 | 5/5/4/5/5/5/3 | 94 | High | High |
| R37 | https://marginalia-search.com/ | Marginalia Search | Marginalia (Viktor Löfgren) | 2026 | 2026-11-25 | Alt A-P6 | 5/4/4/4/5/5/5 | 89 | High | High |
| R38 | https://api.stackexchange.com/2.3/questions?site=stackoverflow&fromdate=1790812800&todate=1793491200&filter=total | Stack Exchange Public API v2.3 — Monthly Question Count Verification (2014-03 đến 2026-10) | Stack Exchange Inc. | Live API (2026-11-25) | 2026-11-25 | A-P7-C1, A-P7-C3, A4 | 5/5/5/5/5/5/5 | 100 | High | High |
| R39 | https://maccus.fr/en/stack-overflow-questions-chatgpt/ | Stack Overflow got 969 questions in September, 99% fewer than when ChatGPT launched | MACCUS (Marc Winer) | 2026-10-31 | 2026-11-25 | A-P7-C1 | 3/4/4/5/5/5/3 | 82 | Medium | High |
| R40 | https://survey.stackoverflow.co/2026 | Stack Overflow Developer Survey 2026 | Stack Overflow | 2026 | 2026-11-25 | A-P7-C2 | 5/5/4/5/5/5/3 | 94 | High | High |
