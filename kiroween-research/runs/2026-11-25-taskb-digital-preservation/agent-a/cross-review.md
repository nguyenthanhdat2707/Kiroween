# Task B Round 2 — Agent A

## Metadata

- **Agent:** A (Round 2 — Cross-Review)
- **Model / Effort (từ launch args):** not observable (tham số khởi chạy không hiển thị trong ngữ cảnh worker)
- **Thời gian thực hiện (UTC):** 2026-11-25T12:43:37Z – 2026-11-25T12:51:00Z
- **Tài liệu đã đọc:** `agent-b/report.md`, `agent-b/opportunities.json`, `agent-c/report.md`, `agent-c/opportunities.json`, cùng bản đóng băng Round 1 của `agent-a/`.
- **Nguồn mới mở trực tiếp trong Round 2:** 7 URL sơ cấp/học thuật mới (`R28`–`R34`, đều HTTP 200 qua `urllib`), 0 nguồn snippet-only mới, **0 lỗi truy cập** trong Round 2.
- **Tóm tắt kết quả phản biện & tự kiểm toán:**
  - Số phản biện có căn cứ gửi tới Agent B: **6** (`B-O1-C4`, `B-O2-C1`/`B-G-C4`, `B-O2-C5`, `B-G-C8`, `B-O5-C1`/`B-O5`, `B-O2`/`B-O3` bỏ sót đối thủ & luật).
  - Số phản biện có căn cứ gửi tới Agent C: **5** (`C-O2`/`C-G-C19` thiếu phản hồi EC 16/06/2026, thiếu EU Data Act, thiếu bằng chứng châu Á, `C-O2-C3` thiếu bằng chứng nhu cầu maintainer, `C-G-C11` nguồn EaaSI 2019 cũ).
  - Tự kiểm toán nhãn `VERIFIED` của chính Agent A (Round 1): **27** claim `VERIFIED` → **3 giữ `VERIFIED`**, **23 hạ xuống `INFERENCE`**, **1 hạ xuống `HYPOTHESIS`** (tổng **24 nhãn thay đổi**).
  - Cập nhật 5 không gian cơ hội của Agent A: **0 kept nguyên vẹn**, **4 revised** (`A-O1`, `A-O2` đề xuất gộp `B-O2`, `A-O3`, `A-O4` đề xuất gộp `B-O1` & `C-O2`), **1 withdrawn** (`A-O5`, trượt cổng theme và bị Mukurtu/PARADISEC phủ phần lớn).

---

## 1. Challenges to Agent B

### 1.1 Lạm phát nhãn `VERIFIED` ở các claim chịu lực (load-bearing claims)

Agent B tự ghi nhận 15/20 claim `VERIFIED` chỉ là *"nguồn X báo cáo Y"* chưa có xác nhận độc lập (`agent-b/report.md` dòng 359). Tuy nhiên, theo `brief.md` §3, **`VERIFIED` đòi hỏi nguồn sơ cấp mở trực tiếp + xác nhận độc lập mở trực tiếp (hoặc kiểm tra tái lập được)**, và **không bao giờ chấp nhận snippet làm xác nhận cho `VERIFIED`**. Nhiều claim chịu lực của Agent B vi phạm tiêu chuẩn này ngay cả ở tiêu chí nguồn sơ cấp:

1. **`B-O1-C4` (Homecoming tự tài trợ, NCSoft cấp license không phí):** Agent B gắn `ĐÃ XÁC MINH` dựa trên **một bài báo game thứ cấp** (`MassivelyOP`, `B-R10`, Source Reliability `M`) + snippet (PC Gamer, GameSpot). Báo chí thứ cấp + snippet chỉ đạt tối đa **`INFERENCE`**, không phải `VERIFIED`.
2. **`B-O2-C1` & `B-G-C4` (Cohost 30k MAU, 2.630 subscriber, thâm hụt 17.000 USD/tháng):** Agent B gắn `ĐÃ XÁC MINH` chỉ dựa trên **một bài TechCrunch** (`B-R14`) trích lại bài đăng của nhân viên Cohost, không mở trực tiếp bài gốc của ASSC và không có nguồn độc lập thứ hai mở trực tiếp → phải hạ xuống **`INFERENCE`**.
3. **`B-O2-C5` (Cyworld dừng 2024 vì thiếu tiền khôi phục dữ liệu, 5 đời chủ):** Dựa trên một bài báo duy nhất (`Asia Economy`, `B-R17`) + snippet timeout (`B-R30`) → phải hạ xuống **`INFERENCE`**.
4. **`B-G-C8` (U.S. Copyright Office từ chối miễn trừ truy cập từ xa cho game năm 2024):** Agent B gắn `ĐÃ XÁC MINH` dựa trên tuyên bố của **một bên vận động có lợi ích liên quan** (Video Game History Foundation, `B-R4`, chính Agent B chấm Bias = `2/5`) + snippet (`B-R29`), mà không mở văn bản chính thức của Copyright Office (trong khi Agent C đã mở trực tiếp `Register's Recommendation PDF`, `C-R31`). Dù kết luận có khả năng đúng, ở trạng thái nguồn của Agent B thì chỉ là **`INFERENCE`**.
5. **`B-O5-C1` & điểm `ai: 5/M` cho `B-O5` (LLM matching decompilation khớp 74% trên 60 hàm):** Tôi đã mở trực tiếp cả hai nguồn của Agent B là blog `gambiconf.substack.com` (`R32`) và bài báo `DecompileBench` trên arXiv (`R31`, `arXiv:2505.11340`). Kết quả xác nhận:
   - `R32` chỉ là **một bài blog cá nhân đơn lẻ** (chính Agent B chấm Source Reliability = `L`), mẫu nhỏ (`n=60`), và **không nêu số liệu baseline chỉ-công-cụ (`m2c` + `decomp-permuter`) trong văn bản** — nên không thể biết LLM đóng góp thêm bao nhiêu phần trăm so với công cụ cổ điển.
   - Trong khi đó, `DecompileBench` (`R31`, đánh giá trên 23.400 hàm từ 130 chương trình thực) cho thấy các phương pháp LLM tuy dễ đọc hơn nhưng **kém hơn 52,2% về tính đúng chức năng** khi không có oracle.
   - **Phản biện:** Dùng một bài blog đơn lẻ thiếu baseline để chấm `ai: 5 (M)` (mức cao nhất trên rubric, đòi hỏi *"mechanism is evidenced (paper, benchmark, documented method)"*) là **đánh giá quá cao**. Với oracle khớp byte (`compiler + objdiff`), vai trò AI ở `B-O5` là *tiềm năng đáng kiểm chứng*, tối đa `ai: 3–4 (L)` cho đến khi có benchmark độc lập so với `m2c + decomp-permuter`.

### 1.2 Bỏ sót khung pháp lý & công cụ hiện có trọng yếu trong `B-O2` và `B-O3`

6. **`B-O2` bỏ sót hoàn toàn EU Data Act (Regulation (EU) 2023/2854):** Agent B chỉ xét GDPR Điều 20 (`B-R21`) và kết luận luật vô hiệu khi công ty nhỏ giải thể (`B-O2-C6`). Tuy nhiên, **EU Data Act** đã chính thức có hiệu lực áp dụng từ **12/09/2025** (và cấm hoàn toàn phí chuyển đổi từ **12/01/2027**, đã mở trực tiếp tại `A-R02` `https://digital-strategy.ec.europa.eu/en/policies/data-act`), tạo nghĩa vụ chuyển đổi cloud/SaaS trong 30 ngày cho mọi nhà cung cấp phục vụ thị trường EU. Ngoài ra, trong `§5`, Agent B bỏ sót hoàn toàn **Webrecorder/WACZ 1.1.1** (`A-R17`) và **Software Heritage** (timeout), và ở `B-O3` thừa nhận **chưa mở trang chính thức nào** của CLOCKSS/LOCKSS/Portico/PKP PN/IA Scholar nhưng vẫn chấm điểm `innovation: 1` và `sustainability: 3`.

---

## 2. Challenges to Agent C

Kỷ luật gắn nhãn của Agent C (6/42 `VERIFIED`, tách bạch nguồn đơn lẻ thành `INFERENCE`, không suy diễn từ snippet) là **chuẩn mực nhất trong ba agent**. Tuy nhiên, báo cáo của Agent C có **5 điểm yếu thực chất về bằng chứng và phạm vi**:

1. **`C-O2` & `C-G-C19` bỏ sót sự kiện pháp lý quan trọng nhất năm 2026 về ECI:** Agent C chỉ dừng ở thời điểm nộp đơn **26/01/2026** (`C-R15`, `C-R16`) và viết *"không suy ra initiative đã thành luật"*. Thực tế, ngày **16/06/2026**, Ủy ban châu Âu đã ban hành **phản hồi chính thức `IP/26/1369` / `C(2026)4110`** (tôi đã mở trực tiếp cả API Đăng bộ ECI `A-R01` lẫn API Presscorner EC `R28`), nêu rõ: *"The Commission considers that at this stage it cannot propose a legal obligation to keep video games playable after they stop being provided commercially. This is due, also, to existing intellectual property rights"* và cam kết đối thoại xây dựng chuẩn ngành cuối năm 2026. Việc bỏ sót phán quyết này khiến phân tích `why now` và rủi ro pháp lý của `C-O2` bị thiếu thông tin cốt lõi.
2. **Bỏ sót hoàn toàn EU Data Act (Reg. 2023/2854) và mảng di chuyển dữ liệu SaaS:** Agent C chỉ trích snippet GDPR Điều 20 (`C-R32`) mà không khảo sát **EU Data Act** (có hiệu lực 12/09/2025, `A-R02`) hay **Data Transfer Initiative (DTI)** (`A-R16`). Do đó, Agent C bỏ qua hoàn toàn không gian có đòn bẩy pháp lý–kinh tế B2B rõ nhất hiện nay (`A-O2`).
3. **Bỏ sót bằng chứng sơ cấp khu vực Châu Á:** Trong `§9`, Agent C chỉ có duy nhất thông báo đóng cửa của Nintendo Nhật (`C-R10`) cho toàn bộ Châu Á và ghi nhận thiếu bằng chứng châu Á cho `C-O1` và `C-O3`. Thực tế có bằng chứng sơ cấp trực tiếp rất phong phú: **Luật Lưu chiểu điện tử NDL Nhật Bản & WARP** (hiệu lực 2010/2013/2023, `A-R15`), **Thư viện Quốc gia Hàn Quốc OASIS** (`A-R15b`), **Cyworld** (`B-R17`, `A-R20`), **Tianya Club** (`A-R19`), và hệ sinh thái **keitai Nhật** (`B-R8`).
4. **`C-O2-C3` (bàn giao maintainer cho đội revival như Pretendo) thiếu bằng chứng nhu cầu và bỏ lỡ thông tin trang chủ Pretendo:** Do bị 403 khi mở `pretendo.network`, Agent C phải dựa vào snippet `C-R11`/`C-R12`. Bản mở trực tiếp `pretendo.network` (`A-R12`) và GitHub API (`A-R13`) cho thấy Pretendo đã có cấu trúc nhóm lõi 12 người, 170 kho mã nguồn mở, danh sách đóng góp viên rõ ràng và tiến độ công khai theo từng tựa game. Không có bằng chứng nào cho thấy bài toán "maintainer succession" là nút thắt thực sự mà Pretendo cần một công cụ mới (chính Agent C cũng chấm `innovation: 1/M`, `feasibility: 1/L`, `sustainability: 1/L`).
5. **`C-G-C11` dùng nguồn EaaSI năm 2019 quá cũ để đánh giá giới hạn giả lập:** Agent C chỉ dựa vào bài cập nhật phát triển EaaSI tháng 3/2019 (`C-R29`), bỏ qua bằng chứng vận hành thực tế mạnh hơn như nghiên cứu tình huống Stanford BDPL (`A-R11`, 2021 — mất 2 ngày cấu hình thủ công cho 1 phần mềm 1985) và gói tài trợ 3,5 triệu USD của Mellon/Sloan cho Yale (`B-R22`).

---

## 3. Overlooked alternatives and counterevidence

### 3.1 Phân tích hội tụ độc lập giữa 3 Agent (Convergence Map)

| Nhóm hội tụ | Các không gian | Giống nhau ở đâu? | Khác nhau ở đâu? | Bằng chứng của ai mạnh hơn? |
|---|---|---|---|---|
| **1. Game live-service / End-of-Life** | `A-O4`, `B-O1`, `C-O2` | Đều xoay quanh đóng cửa server phụ thuộc nhà phát hành, ECI 1,29 triệu chữ ký, và cộng đồng tự vận hành server. | `A-O4` & `B-O1` tập trung vào **khung EOL/chuyển giao trước khi tắt** gắn với code of conduct EC 2026; `C-O2` thu hẹp vào **bàn giao maintainer** cho đội revival như Pretendo. | **A + B mạnh hơn C** ở bối cảnh pháp lý 2026 (cùng mở trực tiếp phản hồi EC 16/06/2026 `A-R01`, `B-R2`/`R28`); **B** có bằng chứng độc đáo về Homecoming (`B-R10`) & gacha Nhật (`B-R24`); **C** có bằng chứng tốt nhất về Nintendo/Capcom (`C-R08..10`) và kỷ luật chấm điểm nghiêm khắc nhất. |
| **2. Hồ sơ học thuật / tạp chí nhỏ vs web app học thuật** | `B-O3`, `C-O1` (và `A-O1` liền kề) | Đều dựa trên sự biến mất của tri thức khoa học công bố trực tuyến. | **`B-O3` & `C-O1` là cùng một không gian** (tạp chí OA nhỏ & lưu trữ bài báo/DOI). **`A-O1` KHÁC BẢN CHẤT:** nhắm vào **ứng dụng web tương tác / web server tin sinh học / dự án DH** (43% tài nguyên mất trên MEDLINE là chương trình máy tính, `A-R07`), thứ mà JASPER/PKP PN/CLOCKSS không bảo tồn được. | Với tạp chí nhỏ: **C mạnh hơn B rất nhiều** (mở trực tiếp PDF Eve `C-R02`, PKP PN `C-R03`, TDL `C-R04`, JASPER `C-R05`, ISSN Plan `C-R07`, chứng minh đối thủ đã phủ rất sâu). Với web app học thuật: **chỉ A có bằng chứng peer-reviewed trực tiếp** (`A-R05..09`). |
| **3. Cửa sổ đóng cửa nền tảng & dữ liệu người dùng** | `A-O2`, `B-O2` | Cùng giải quyết mất mát dữ liệu/quy trình khi nền tảng cộng tác hoặc cộng đồng đóng cửa (Cohost, Mastodon, SaaS). | `B-O2` đứng từ phía **nhà vận hành sắp chết** (Cohost thâm hụt $17k/tháng, Glitch đóng hosting 7/2025 `R29`); `A-O2` đứng từ phía **người dùng/SME hậu xuất dữ liệu** gắn với EU Data Act (`A-R02`), Mastodon export (`A-R10`) và DTI (`A-R16`). | **B mạnh hơn ở bằng chứng thực tế đóng cửa** (mở trực tiếp blog Glitch `R29`, ArchiveTeam Cohost `B-R12`, Cyworld `B-R17`); **A mạnh hơn ở đòn bẩy pháp lý & kỹ thuật hậu xuất** (EU Data Act 9/2025, Mastodon official docs, DTI). Nên **đề xuất gộp** theo hướng hậu xuất + chuẩn đóng cửa. |
| **4. Di sản cộng đồng, đồng thuận & chủ quyền dữ liệu** | `A-O5`, `C-O3` (và `B-O4` liền kề) | `A-O5` và `C-O3` cùng chỉ ra "sao chép công khai ≠ bảo tồn hợp pháp/đạo đức" và lấy Mukurtu làm đối thủ chính. | `A-O5` rộng hơn (gồm cả NDL WARP Nhật & GDPR Điều 89); `C-O3` sắc nét hơn khi thu hẹp vào **mất ngữ nghĩa quyền khi di chuyển Mukurtu 3→4** và ca thực địa Ranongga/PARADISEC. `B-O4` khác hẳn (di sản phần cứng/nền tảng khu vực chết như keitai i-mode, Mxit). | **C mạnh hơn A về bằng chứng công cụ hiện có** (mở trực tiếp Mukurtu migration `R34`, Local Contexts `C-R19`, PARADISEC offline HTML 2026 `C-R21`); **A mạnh hơn về bằng chứng pháp lý Châu Á/EU** (NDL Nhật `A-R15`, GDPR Art. 89 `A-R13b`). Cả hai đều xác nhận **trượt cổng Resurrection (`theme < 3`)**. |
| **5. Phần mềm bị bỏ rơi: giả lập môi trường vs tái dựng mã nguồn** | `A-O3`, `B-O5` | Cùng thuộc chiều `software` + `heritage`, giải cứu phần mềm cũ không còn chạy được. | **Hai bài toán kỹ thuật hoàn toàn khác nhau:** `A-O3` là tự động cấu hình môi trường giả lập (EaaSI) cho thư viện chạy binary gốc; `B-O5` là dịch ngược khớp byte (matching decompilation) để tái tạo mã nguồn C cho cộng đồng decomp. | Cả hai đều dựa trên bằng chứng hẹp (`A-O3`: 1 case study Stanford `A-R11`; `B-O5`: 1 blog n=60 `R32` + DecompileBench phản chứng `R31`). Không nên gộp. |

### 3.2 Kiểm định tuyên bố của Agent B về Willingness to Pay (`B-G-C10`)

Agent B khẳng định **không tìm thấy bằng chứng ai sẵn sàng trả tiền cho một công cụ bảo tồn mới** (`B-G-C10`). Kiểm định trực tiếp trên toàn bộ các không gian của cả 3 agent:

- **Xác nhận ĐÚNG đối với người dùng cá nhân (B2C) và nhà vận hành sắp phá sản:**
  - Người chơi game ký ECI (1,29 triệu chữ ký) và quyên góp tự nguyện (Homecoming), **không** chứng minh họ mua công cụ bảo tồn (`A-O4`, `B-O1`, `C-O2`).
  - Nhà vận hành nền tảng sắp đóng (Cohost thâm hụt $17k/tháng, nhân viên không lương, `B-R14`) **không còn tiền** để mua công cụ đóng cửa (`B-O2`).
  - Ngay cả **Internet Archive** — tổ chức bảo tồn lớn nhất thế giới — cũng ghi nhận thâm hụt theo IRS Form 990 trên ProPublica (`R33`, mở trực tiếp): năm tài chính kết thúc 2023 và 2025 đều chi vượt thu, cho thấy kinh tế lưu trữ phi lợi nhuận cực kỳ mong manh.
  - Phục hồi di sản tiêu dùng thương mại (**Cyworld**) thất bại lặp lại vì thiếu vốn khôi phục dữ liệu (`B-R17`).
- **Phản chứng MỘT PHẦN (nhưng chưa đủ để chứng minh WTP cho công cụ mới):**
  - Có bằng chứng **chi tiêu thể chế/grant thực tế** cho hạ tầng bảo tồn: Yale EaaSI nhận 3,5 triệu USD từ Mellon/Sloan (`B-R22`), BBAW có 21 triệu EUR/10 năm cho chương trình ELDP (`C-R24`), PARADISEC công bố mức dự trù AUD 20/tệp video trong grant (`C-R23`), và **JASPER** (`R30`, mở trực tiếp) miễn phí cho tạp chí nhỏ nhưng được DOAJ/CLOCKSS/PKP tài trợ.
  - Có **động lực tuân thủ B2B mới** từ **EU Data Act** (`A-R02`, cấm phí chuyển đổi cloud từ 12/01/2027) — đây là trường hợp duy nhất có giả thuyết doanh thu B2B hợp lý (`A-O2`), **nhưng** hiện vẫn chưa có bằng chứng hợp đồng/chi tiêu thực tế cho một công cụ tái tạo gói export mới.
- **Kết luận:** Tuyên bố `B-G-C10` đứng vững ở mức *"chưa có bằng chứng WTP trực tiếp cho bất kỳ công cụ bảo tồn mới nào trên cả 13 không gian của 3 agent"*. Mọi điểm `sustainability` của các không gian phụ thuộc vào sản phẩm mới phải phản ánh sự thật này.

### 3.3 Kiểm định vai trò AI (`load-bearing` vs kỹ thuật truyền thống)

Kiểm tra riêng mọi không gian được gắn `ai_role: "load-bearing"` trong Round 1 (Agent C không gắn không gian nào là `load-bearing`):

1. **`A-O2` (Agent A Round 1 gắn `load-bearing`):** **Không đứng vững.** Với các định dạng xuất có đặc tả rõ như Mastodon Activity Streams 2.0 (`A-R10`), Cohost JSON, hay Glitch git export (`R29`), **kỹ thuật truyền thống (parser xác định + ánh xạ lược đồ tường minh)** làm tốt hơn, chính xác 100% và rẻ hơn AI. AI chỉ *hữu ích* (`useful`) khi gặp gói export SaaS đuôi dài không có tài liệu lược đồ, và chưa có benchmark chứng minh lợi thế ròng sau khi tính công kiểm duyệt. → **Hạ xuống `useful`.**
2. **`A-O3` (Agent A Round 1 gắn `load-bearing`):** **Không đứng vững.** Nhận diện định dạng nhị phân/header đĩa (tương tự PRONOM/DROID) + ma trận tương thích hệ điều hành/emulator có cấu trúc + kiểm thử khởi chạy tự động trong sandbox đều làm được bằng **kỹ thuật phần mềm truyền thống**. AI chỉ *hữu ích* (`useful`) ở khâu trích xuất yêu cầu hệ thống từ file manual scan cũ có ngôn ngữ tự nhiên lộn xộn. → **Hạ xuống `useful`.**
3. **`B-O5` (Agent B Round 1 gắn `load-bearing`, `ai: 5/M`):** **Chưa đủ bằng chứng để kết luận `load-bearing`.** Về mặt cơ chế, matching decompilation có oracle tuyệt đối (biên dịch khớp từng byte qua `objdiff`), nên AI *có tiềm năng* giải các hàm khó mà `m2c`/`decomp-permuter` bỏ sót. Tuy nhiên, như đã kiểm chứng trực tiếp tại `R32` (`gambiconf.substack.com`), tác giả không công bố tỷ lệ khớp của baseline chỉ-công-cụ trong văn bản, còn `DecompileBench` (`R31`) chứng minh LLM kém 52,2% về độ đúng chức năng khi thiếu oracle. Cần giữ thái độ hoài nghi cho tới khi có thí nghiệm đo phần tăng ròng (delta) của LLM so với công cụ cổ điển.

---

## 4. Self-audit of my VERIFIED labels

Áp dụng nghiêm ngặt `brief.md` §3: **`VERIFIED` chỉ hợp lệ khi có (a) nguồn sơ cấp mở trực tiếp + xác nhận độc lập mở trực tiếp, HOẶC (b) kiểm tra tái lập được trực tiếp.** Mọi claim chỉ dựa trên 1 nguồn sơ cấp duy nhất, hoặc dựa trên Wikipedia/báo thứ cấp, hoặc trộn lẫn với snippet, hoặc mang tính suy diễn tổng hợp đều phải hạ nhãn.

| Claim | Round 1 label | Revised label | Reason |
|---|---|---|---|
| `A-G-C1` | VERIFIED | **INFERENCE** | Dựa trên nguồn thứ cấp Wikipedia (`R18`, `R19`) + snippet (`R22`, `R26`); chưa mở bài gốc ASSC/Tianya cùng xác nhận độc lập. |
| `A-G-C2` | VERIFIED | **INFERENCE** | Chỉ dựa trên **1** bài báo peer-reviewed mở trực tiếp (`R05`, PMID 29228189); thiếu xác nhận độc lập thứ hai cho riêng con số 69% / 10,39 năm. |
| `A-G-C3` | VERIFIED | **INFERENCE** | Chỉ dựa trên **1** bài báo (`R06`, Wren 2017, PMID 28334982); phần kết luận "cơ chế chọn lọc tự nhiên" là diễn giải. |
| `A-G-C5` | VERIFIED | **VERIFIED** | Giữ nguyên: 1.294.188 chữ ký ECI mở trực tiếp từ Đăng bộ EC (`R01`) + xác nhận trực tiếp từ API Presscorner EC (`R28`) và Heise (Agent C `R16`); Pretendo 170 repo kiểm tra tái lập trực tiếp qua GitHub API (`R13`) + trang chủ (`R12`). |
| `A-G-C6` | VERIFIED | **INFERENCE** | Chỉ dựa trên 1 đặc tả WACZ 1.1.1 (`R17`); nhận định "đã trưởng thành, thách thức chuyển sang pháp lý" là tổng hợp suy luận. |
| `A-G-C7` | VERIFIED | **INFERENCE** | Trộn lẫn nguồn mở trực tiếp (`R07`, `R09`) với nguồn **snippet-only** Software Heritage (`R25` lỗi SSL). |
| `A-G-C8` | VERIFIED | **INFERENCE** | Dựa trên 1 case study Stanford (`R11`) + 1 bộ nguyên tắc Endings (`R09`); khái quát hóa sang toàn chiều `software` là suy luận. |
| `A-G-C10` | VERIFIED | **INFERENCE** | Phần Mastodon dựa trên 1 nguồn gốc (`R10`); phần Cyworld dựa trên Wikipedia (`R20`) + snippet (`R26`). |
| `A-G-C11` | VERIFIED | **INFERENCE** | Nhận định mang tính chuẩn tắc/tổng hợp từ 1 trang GIDA (`R14e`), 1 trang NDL (`R15`) và DPC (`R03`). |
| `A-G-C12` | VERIFIED | **INFERENCE** | Tổng hợp từ Pretendo (`R12`) và Wikipedia Cohost/Tianya (`R18`, `R19`); kết luận "chỉ bền vững ở quy mô hẹp" là suy luận. |
| `A-G-C13` | VERIFIED | **HYPOTHESIS** | Tuyên bố tổng quát *"Phần lớn các dự án bảo tồn thất bại vì bài toán kinh tế bất đối xứng"* là khái quát hóa từ 4 trường hợp lẻ (Cohost, Tianya, Cyworld, WebCite snippet), chưa có nghiên cứu định lượng tổng thể. |
| `A-G-C14` | VERIFIED | **INFERENCE** | So sánh xuyên 3 khu vực pháp lý gồm một phần dữ liệu từ snippet (`R21` remote access, `R27g` DSM Art. 6); cần hạ xuống `INFERENCE`. |
| `A-O1-C1` | VERIFIED | **INFERENCE** | Số liệu 69% và chu kỳ bán rã 10,39 năm đến từ **1** nghiên cứu đơn lẻ (`R05`, PMID 29228189), chưa có tái kiểm độc lập. |
| `A-O1-C2` | VERIFIED | **VERIFIED** | Giữ nguyên: hiện tượng suy thoái URL/tài nguyên học thuật được xác nhận độc lập bởi nhiều nghiên cứu peer-reviewed mở trực tiếp qua NCBI XML (`R07` Wren 2008, `R08` Hennessey & Ge 2013, cùng `R05` 2019). |
| `A-O1-C3` | VERIFIED | **INFERENCE** | Chỉ dựa trên 1 tài liệu nguyên tắc do chính Endings Project công bố (`R09`), chưa có kiểm chứng độc lập về độ bền thực nghiệm hàng thập kỷ. |
| `A-O2-C1` | VERIFIED | **INFERENCE** | Chỉ mở trực tiếp 1 trang chính thức của EC (`R02`), chưa mở bản văn quy định trên EUR-Lex (bị HTTP 202) hoặc xác nhận độc lập thứ hai. |
| `A-O2-C2` | VERIFIED | **INFERENCE** | Chỉ dựa trên 1 nguồn tài liệu gốc của Mastodon (`R10`), chưa có kiểm thử tái lập thực tế hoặc xác nhận độc lập thứ hai. |
| `A-O2-C3` | VERIFIED | **INFERENCE** | Phần DTI (`R16`) chỉ 1 nguồn và phần hạn chế lược đồ quan hệ dựa trên snippet (`R24`). |
| `A-O3-C1` | VERIFIED | **INFERENCE** | Dựa trên **1** case study duy nhất của SPN/Stanford (`R11`), chưa có xác nhận độc lập từ thư viện thứ hai. |
| `A-O3-C2` | VERIFIED | **INFERENCE** | Phần xếp hạng cụ thể *Practically Extinct* cho trò chơi bị ngừng hỗ trợ nằm ở snippet (`R27a`), không hiện nguyên văn trên trang tổng quan mở trực tiếp (`R03`). |
| `A-O3-C3` | VERIFIED | **INFERENCE** | Trang tổng quan `copyright.gov/1201/2024/` (`R04`) xác nhận có Final Rule 28/10/2024, nhưng chi tiết **từ chối mở rộng truy cập từ xa** ở Round 1 lấy từ snippet (`R21`). |
| `A-O4-C1` | VERIFIED | **INFERENCE** | Trong Round 1, số chữ ký 1.294.188 mở trực tiếp từ `R01`, nhưng nội dung **EC từ chối luật hóa và đề xuất code of conduct** lấy từ snippet (`R21b`) → Round 1 gắn nhãn quá tay. *(Ghi chú: ở Round 2 đã mở trực tiếp API Presscorner EC `R28` xác nhận nguyên văn từ chối lập pháp; tuy nhiên cả `R01` và `R28` đều thuộc cùng nguồn EC.)* |
| `A-O4-C2` | VERIFIED | **VERIFIED** | Giữ nguyên: 170 repo công khai trên GitHub (`R13`, kiểm tra tái lập trực tiếp qua API) + trang chủ Pretendo (`R12`) xác nhận cấu trúc clean-room và giới hạn không chuyển NNID. |
| `A-O4-C3` | VERIFIED | **INFERENCE** | Dựa trên hai trang Wikipedia thứ cấp (`R18`, `R19`), không phải thông báo sơ cấp của ASSC và Tianya. |
| `A-O5-C1` | VERIFIED | **INFERENCE** | Chỉ dựa trên 1 trang thông tin chính thức của NDL Nhật (`R15`), chưa đối chiếu trực tiếp văn bản luật gốc tiếng Nhật hoặc nguồn độc lập thứ hai. |
| `A-O5-C2` | VERIFIED | **INFERENCE** | Mở trực tiếp trang tổng hợp `gdpr-info.eu` (`R13b`, không phải EUR-Lex chính thức do bị bot gate), không có nguồn pháp lý thứ hai. |
| `A-O5-C3` | VERIFIED | **INFERENCE** | Kết hợp nhiều nguồn đơn lẻ (`R19c` blog IA — bên thua kiện có thiên lệch, `R14e` GIDA, `R03` DPC), chưa mở phán quyết tòa phúc thẩm gốc (Justia 403). |

**Tổng kết tự kiểm toán:** Từ 30 claim Round 1 (`27 VERIFIED`, `3 INFERENCE`), sau khi áp chuẩn chặt `brief.md` §3 còn **`3 VERIFIED`, `26 INFERENCE`, `1 HYPOTHESIS`, `0 UNKNOWN`** (**24/27 nhãn `VERIFIED` bị hạ**). Bài học rõ ràng: ở Round 1 tôi đã nhầm lẫn giữa *"đã mở trực tiếp 1 nguồn sơ cấp"* với *"đã xác minh độc lập"*.

---

## 5. Revisions to my opportunities

1. **`A-O1` (Post-Grant Academic & Digital Humanities Web-App Staticization) → `revised` (KHÔNG gộp với `B-O3`/`C-O1`):**
   - **Lý do giữ tách biệt:** Bằng chứng của Agent C về JASPER/PKP PN/ISSN (`C-R03..07`, tôi đã kiểm chứng trực tiếp `R30` `doaj.org/preservation/`) khẳng định mảng lưu trữ bài báo/tạp chí nhỏ (`B-O3`, `C-O1`) đã có hạ tầng mạnh và trượt cổng Resurrection (`theme: 1`). Ngược lại, `A-O1` tập trung vào **ứng dụng web tương tác / web server học thuật**, nơi JASPER/CLOCKSS không thể lưu được tính năng.
   - **Thay đổi điểm số:** Hạ `demand` `4 (H) → 3 (M)` và `sustainability` `4 (M) → 3 (L)` (kích hoạt bởi phản biện `B-G-C10` của Agent B và `C-G-C23` của Agent C: chưa có bằng chứng WTP trực tiếp cho công cụ tĩnh hóa mới).
2. **`A-O2` (Post-Shutdown SaaS & Federated Export Semantic Rehydration) → `revised`, đề xuất gộp `merge_with: ["B-O2"]`:**
   - **Lý do gộp & điều chỉnh:** `B-O2` (Agent B) bổ sung bằng chứng sơ cấp cực mạnh từ vụ đóng cửa **Glitch** (`R29`, 08/07/2025) và thâm hụt Cohost (`B-R14`), chứng minh nhà vận hành sắp chết *không có tiền* và thường chỉ kịp xuất tệp thô/redirect. Gộp `A-O2` + `B-O2` cho phép định vị đúng điểm đòn bẩy: xử lý **khoảng trống hậu xuất dữ liệu** (khi người dùng/SME đã có tệp export hợp pháp nhờ EU Data Act hoặc nút export trước khi đóng cửa).
   - **Thay đổi điểm số & AI:** Hạ `ai_role` từ `"load-bearing"` → `"useful"`, `ai` `4 (M) → 3 (L)` (kích hoạt bởi kiểm định đối trọng kỹ thuật truyền thống của Coordinator & `C-G-C22`); hạ `demand` `4 (M) → 3 (M)` và `sustainability` `4 (M) → 3 (L)` (kích hoạt bởi `B-G-C10`: chưa có bằng chứng WTP thực tế dù EU Data Act là đòn bẩy hứa hẹn).
3. **`A-O3` (Automated Environment Discovery & Configuration for Institutional Software Emulation) → `revised` (KHÔNG gộp với `B-O5`):**
   - **Lý do:** Khác biệt hoàn toàn về tác vụ và người dùng với `B-O5` (chạy binary trong EaaSI vs dịch ngược mã nguồn C).
   - **Thay đổi điểm số & AI:** Hạ `ai_role` từ `"load-bearing"` → `"useful"`, `ai` `4 (M) → 3 (L)` (do PRONOM/DROID + ma trận tương thích + kiểm thử sandbox tự động giải quyết phần lớn công việc bằng kỹ thuật truyền thống; kích hoạt bởi tự kiểm định & `C-G-C22`); hạ độ tin cậy `sustainability` từ `3 (M) → 3 (L)` (kích hoạt bởi `B-G-C10`, dù Yale EaaSI có grant 3,5 triệu USD `B-R22`).
4. **`A-O4` (End-of-Life Sunset & Community Handover Governance for Live-Service Platforms) → `revised`, đề xuất gộp `merge_with: ["B-O1", "C-O2"]`:**
   - **Lý do gộp & điều chỉnh:** Ba không gian hội tụ trên cùng một vấn đề gốc (dịch vụ game/trực tuyến phụ thuộc server). Giữ nguyên đánh giá khắt khe `ai_role: "unnecessary"` (`1/H`) và `sustainability: 1 (H)` (được củng cố trực tiếp bởi văn bản EC `R28` `IP/26/1369` khẳng định IP cản nghĩa vụ pháp lý).
   - **Thay đổi điểm số:** Hạ `demand` từ `5 (H) → 4 (H)` (kích hoạt bởi `C-G-C19` của Agent C và `B-O1` của Agent B: 1,29 triệu chữ ký ECI là bằng chứng vận động chính sách, không phải bằng chứng nhu cầu mua/dùng một công cụ mới).
5. **`A-O5` (Consent-Aware & Sovereign Community Digital Heritage Preservation) → `withdrawn` (đề xuất chuyển các phát hiện pháp lý/đạo đức sang tầng ràng buộc chung; liên kết hồ sơ với `C-O3`):**
   - **Lý do rút lui:** Cả Agent A (`theme: 2/M`) lẫn Agent C (`C-O3`: `theme: 1/M`) đều xác nhận không gian này **trượt cổng Resurrection** vì không có công nghệ chết cụ thể làm trung tâm. Hơn nữa, bằng chứng trực tiếp tôi vừa kiểm chứng từ `Mukurtu 3→4 Migration` (`R34`) cùng `PARADISEC offline collections 2026` (`C-R21`) và `Local Contexts` (`C-R19`) cho thấy hệ sinh thái chuyên biệt đã phủ phần lớn bài toán cốt lõi. Rút lui khỏi danh sách cơ hội ứng viên, giữ lại các quy tắc GDPR Điều 89 / NDL Nhật / CARE làm **ràng buộc đạo đức–pháp lý bắt buộc** cho mọi hướng khác.

---

## 6. Positions I keep despite challenge

1. **Giữ tách biệt `A-O1` (web app học thuật) khỏi `B-O3`/`C-O1` (tạp chí học thuật nhỏ):**
   - *Phản biện mạnh nhất:* Cả Agent B (`B-O3`) và Agent C (`C-O1`) đều kết luận khu vực học thuật đã có hạ tầng bảo tồn mạnh (JASPER, PKP PN, CLOCKSS, Keepers Registry) và trượt cổng Resurrection (`theme: 1`).
   - *Lý do giữ lập trường:* Hạ tầng JASPER (`R30`) và PKP PN (`C-R03`) bảo tồn **văn bản tĩnh (PDF/XML/metadata tạp chí)**, **không** bảo tồn được các **ứng dụng web động/web server phân tích** (chiếm 43% tài nguyên mất trên MEDLINE, `A-R07`, và 31% web server tin sinh học đã chết, `A-R05`). Do đó `A-O1` không bị các đối thủ tạp chí vô hiệu hóa và vẫn có neo công nghệ cụ thể (web server/framework học thuật chết, WebCite đóng cửa).
2. **Giữ đòn bẩy EU Data Act (Reg. 2023/2854) là điểm khác biệt chiến lược của `A-O2` so với `B-O2`:**
   - *Phản biện mạnh nhất:* Agent B (`B-O2`) lập luận đúng rằng nhà vận hành nền tảng nhỏ sắp chết (như Cohost) hết tiền và đã tự xuất dữ liệu cơ bản, còn Glitch cũng tự cấp nút export/redirect (`R29`), nên khoảng trống có thể rất hẹp.
   - *Lý do giữ lập trường:* Cả Agent B và Agent C đều bỏ sót **EU Data Act** (có hiệu lực 12/09/2025, cấm phí chuyển đổi 12/01/2027, `A-R02`). Đạo luật này dịch chuyển bài toán từ *"cứu nền tảng nhỏ phá sản không có tiền"* sang *"giải mã và tái cấu trúc dữ liệu xuất hợp pháp ở quy mô SME/cloud"*, nơi có người hưởng lợi còn đang hoạt động và có lý do tài chính để trả tiền cho việc chuyển đổi không đứt gãy — dù WTP cho công cụ mới vẫn cần kiểm chứng thực nghiệm.
3. **Giữ quan điểm phản đối AI trong `A-O4`/`B-O1` và bác bỏ điểm `ai: 5` của `B-O5`:**
   - *Phản biện mạnh nhất:* Agent B cho rằng AI hữu ích ở `B-O1` (`ai: 2`) và load-bearing ở `B-O5` (`ai: 5/M`) nhờ oracle khớp byte.
   - *Lý do giữ lập trường:* Ở `A-O4`/`B-O1`, nút thắt là sở hữu trí tuệ (`R28` EC `IP/26/1369`) chứ không phải trí tuệ nhân tạo. Ở `B-O5`, việc `R32` thiếu baseline chỉ-công-cụ trên tập `n=60` và `R31` (`DecompileBench`) chỉ ra mức tụt 52,2% độ đúng chức năng khiến mức điểm `5` chưa được biện minh.

---

## 7. Remaining disagreements

| Bất đồng còn tồn tại | Các bên liên quan | Bằng chứng cụ thể cần có để phân giải |
|---|---|---|
| **1. AI trong matching decompilation (`B-O5`) có thực sự `load-bearing` vượt công cụ cổ điển?** | Agent B (`ai: 5/M`) vs Agent A (tối đa `3–4/L`, chưa chứng minh delta) | Chạy lại benchmark độc lập trên ≥30 hàm của một dự án decomp khác, báo cáo rõ tỷ lệ khớp của **(a) `m2c + decomp-permuter` thuần** vs **(b) kết hợp LLM**; chỉ gọi là `load-bearing` nếu delta ≥ +15 điểm phần trăm. |
| **2. EU Data Act (9/2025) có thực sự tạo ra WTP cho công cụ tái tạo gói export (`A-O2`) hay chỉ do đối thủ lớn tự xây importer?** | Agent A (`A-O2` giữ cơ hội B2B tiềm năng) vs Agent B (`B-G-C10` chưa có WTP) & Agent C (`C-G-C23`) | Kiểm tra thực nghiệm 5 gói export thực tế (Mastodon, Cohost, Glitch, 2 SaaS vừa đóng hoặc tuân thủ Data Act) + khảo sát 10 nhóm sản phẩm SME về chi phí chuyển đổi thực tế khi đối thủ đích không có importer miễn phí. |
| **3. Liệu các game live-service đóng cửa có thực sự bị chặn chủ yếu bởi pháp lý hay thiếu chuẩn kỹ thuật EOL?** | Agent A (`sustainability: 1`, rào cản IP áp đảo) vs Agent B (`sustainability: 3`, kỳ vọng code of conduct EC 2026) | Lấy mẫu 20 game live-service đóng cửa 2024–2026 (thí nghiệm của chính `B-O1`) + theo dõi văn bản dự thảo đầu tiên của EC về bộ quy tắc ứng xử EOL cuối năm 2026 để xem có điều khoản kỹ thuật hay chỉ minh bạch thời hạn. |
| **4. Tỷ lệ thực tế web app học thuật có thể tĩnh hóa không mất công năng (`A-O1`)?** | Agent A (`A-O1` giữ độc lập) vs nhận định chung của B/C về học thuật | Chạy thí nghiệm bác bỏ của `A-O1` trên 20 web app tin sinh học/DH mã nguồn mở sắp hết bảo trì: đo tỷ lệ (%) chuyển sang static/WASM giữ nguyên công năng cốt lõi. |

---

## 8. New references

*(Chỉ liệt kê các nguồn mới được Agent A mở trực tiếp trong Round 2 để kiểm chứng chéo các luận điểm của Agent B và Agent C. Thang điểm giống Round 1: `A/T/M/C/F/R/B`, trọng số `20/20/20/15/10/10/5`, quy đổi thang `0.00–5.00`.)*

| Ref ID | URL | Title | Publisher | Pub Date | Accessed | Opened Directly / Snippet | Claims / Sections | A/T/M/C/F/R/B | Weighted | Source Reliability | Reference Relevance |
|---|---|---|---|---|---|---|---|---|---|---|---|
| R28 | https://ec.europa.eu/commission/presscorner/api/documents?reference=IP/26/1369&language=en | Commission will engage with industry following European Citizens' Initiative on the disabling of videogames by publishers (`IP/26/1369`) | European Commission (Presscorner API) | 2026-06-16 | 2026-11-25 | Opened directly | §2.1, §3.1, §4 (`A-O4-C1`), §5 (`A-O4`) | 5/4/5/5/5/5/5 | 4.80 | High | High |
| R29 | https://blog.glitch.com/post/changes-are-coming-to-glitch/ | Important changes are coming to Glitch (hosting shutdown July 8, 2025; export & redirects through 2026) | Glitch (Fastly) | 2025-05-22 | 2026-11-25 | Opened directly | §3.1, §3.3, §5 (`A-O2`), §6 | 5/4/5/5/4/5/4 | 4.65 | High | High |
| R30 | https://doaj.org/preservation/ | JASPER preservation service (free preservation via CLOCKSS/LOCKSS, PKP PN, Internet Archive; eligibility criteria) | DOAJ | 2026 (live) | 2026-11-25 | Opened directly | §1.2, §3.1, §3.2, §5 (`A-O1`), §6 | 5/4/5/5/4/5/4 | 4.65 | High | High |
| R31 | https://arxiv.org/abs/2505.11340 | DecompileBench: A Comprehensive Benchmark for Evaluating Decompilers in Real-World Scenarios (23,400 functions, 130 programs) | arXiv / ACL Findings 2025 | 2025-05 | 2026-11-25 | Opened directly (abstract) | §1.1 (`B-O5`), §3.3, §6 | 5/5/5/4/4/5/5 | 4.75 | High | High |
| R32 | https://gambiconf.substack.com/p/can-llms-really-do-matching-decompilation | Can LLMs Really Do Matching Decompilation? I Tested 60 Functions to Find Out | Substack (Macabeus) | 2026-03-10 | 2026-11-25 | Opened directly | §1.1 (`B-O5-C1`), §3.3, §6 | 2/4/4/5/5/4/3 | 3.80 | Low | High |
| R33 | https://projects.propublica.org/nonprofits/organizations/943242767 | Internet Archive — Nonprofit Explorer (IRS Form 990) | ProPublica | 2026 (live) | 2026-11-25 | Opened directly | §3.2 (WTP / sustainability) | 5/4/4/4/5/5/5 | 4.45 | High | Medium-High |
| R34 | https://docs.mukurtu.org/migration/PM02Activities/ | Mukurtu 3 Pre-Migration Activities (custom fields, media & cultural protocols) | Mukurtu Official User Manual | 2026 (live) | 2026-11-25 | Opened directly | §3.1, §5 (`A-O5` withdrawn) | 5/5/5/5/4/4/4 | 4.75 | High | High |
