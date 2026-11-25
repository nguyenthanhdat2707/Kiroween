# Phase 2B Debate — Agent C

## Metadata

- Run: `2026-11-25-phase2-candidate-evaluation`; một vòng tranh luận Phase 2B, ngày 25/11/2026. Bắt đầu ghi nhận UTC: `2026-11-25T11:36:09Z`; kết thúc được ghi trong `scratch/debate-validation.json`.
- Agent C; model quan sát từ launch args ở 2A: `gpt-6.1-sol`, effort `high`; không giả định tên model mới khi chưa có launch mới.
- Đã đọc AGENTS.md, brief và rubric; đã đọc evaluation/scores 2A của A, B, C. Quyền đọc A/B do dispatch 2B cấp; không sửa chúng, không liên hệ agent khác, không chạy sản phẩm hay mã cộng đồng. Không commit/push.
- Giữ nguyên trọng số `20/15/15/15/10/10/10/5`. Đây là đánh giá problem space theo anchor, không dự đoán kết quả giám khảo và không lập Top 3.
- Kiểm tra web 2B: 0 search query, 3 URL mở trực tiếp thành công: C·R25, C·R32 và D-C01. Hai nguồn đầu đã có trong 2A; **1 reference mới đối với hồ sơ C, 0 URL mới so với hợp nguồn 2A của A/B/C**. D-C01 do B2-R26 gợi ra, không phải phát hiện độc lập của C; đóng góp mới là kiểm toàn văn thay cho snippet. Không lỗi truy cập mới; không dùng snippet mới làm bằng chứng.
- Ký hiệu tránh đụng ID: `A2:P2-Rxx` là ref 2A của A; `B2:B2-Rxx` là ref 2A của B; `C2:Rxx` là ref 2A của C; `P1:…-Cx` là claim Phase 1 theo corrections-overlay. Nguồn C2 được mở trực tiếp ở 2A; chỉ C2:R25/R32 mở lại ở 2B. Đọc báo cáo A/B không đồng nghĩa tự mở tất cả URL của họ. Nhãn VERIFIED chỉ cho nội dung được xác nhận; đánh giá/gap/khả năng chuyển sang ứng viên là INFERENCE, mô hình chưa thử là HYPOTHESIS, thiếu chứng cứ là UNKNOWN.
- Hai thay đổi điểm: A-P7 demand 4→3; C-P4 theme 3→2. C-P4 chuyển gate PASS→FAIL; A-P7 tiếp tục FAIL. 62 ô điểm khác giữ nguyên. Việc bổ sung nguồn/confidence được ghi riêng, không tính là thay đổi điểm.

## 1. Challenges to Agent A

Mỗi dòng dưới đây nêu điểm của A, điểm C sau tranh luận và lập luận có thể bị bác bỏ. Khi A chỉ chấm theo phạm vi có điều kiện, tôi chỉ rõ điều kiện chưa được xác nhận; không biến điều kiện ấy thành tuyên bố A đã có phần cứng.

| Candidate | Criterion | Điểm A | Điểm C 2B | Phản biện và bằng chứng |
|---|---|---:|---:|---|
| B-P1 | innovation | 4 | 2 | A đề xuất workbench cộng đồng thay vì nghiên cứu đơn lẻ: đây là khác biệt sản phẩm có thể có, nhưng chưa có model đuôi dài hay so sánh chứng minh workbench lấp gap. Phương pháp closed-loop đã được P1:B-P1-C5/C6 và C2:R32 mô tả; Wemo/Nest có lựa chọn C2:R29/R33. **INFERENCE:** điểm 4 đang ghi nhận lợi ích giả định “tháng xuống giờ/ngày” trước khi đo. Tôi không gọi ứng viên là clone; cho 2 vì đóng gói quy trình có thể có ích nhưng gap còn yếu hơn mức 3. C2:R32 được mở lại trực tiếp; R29/R33 trực tiếp ở 2A. |
| B-P1 | feasibility | 3 (H) | 1 (L) | A thu hẹp sang LAN/API mở và ghi “có sẵn trong tay” như điều kiện. Hồ sơ chưa xác nhận điều kiện đó. P1:B-P1-C6 và C2:R32 không cung cấp cho đội một thiết bị cùng oracle; mã pywemo không thay được đối chứng phần cứng. Theo anchor 1, phụ thuộc hardware chưa có trong tay là đủ để giữ 1; **UNKNOWN** inventory, không phải VERIFIED đội không sở hữu thiết bị. Một model thật và replay được trong 48 giờ có thể đưa lên 3. Chấm 3 có điều kiện nên tách khỏi điểm hiện tại. |
| A-P7 | demand | 2 | 3 | A đúng khi bác 4 của tôi: survey về trust không phải hành vi đóng góp cho commons mới. Nhưng 2 thấp hơn anchor 3 nếu thừa nhận survey hiện tại C2:R22/R23 và ca MRE C2:R07 là bằng chứng vấn đề kiểm chứng. Cũng không suy từ ít câu hỏi rằng người dùng “hài lòng” với AI: đó là nguyên nhân **INFERENCE**, không được API chứng minh. Không có willingness-to-contribute là lý do không cho 4/5, chưa đủ phủ nhận vấn đề ở mức 3. |
| A-P7 | innovation | 3 | 1 | Context7 mạnh về docs phiên bản nhưng chưa phải đối thủ gần nhất. C2:R25, mở lại trực tiếp, là Stack Overflow for Agents: chia sẻ tri thức sau phiên agent, TIL/Playbooks, verification và quyền duyệt trước công bố. **INFERENCE:** core job đã có đối thủ trực tiếp. Test tái lập có thể là gap, nhưng chưa kiểm chứng nó vượt nền tảng ấy; không thể chấm 3 chỉ vì Context7 không lưu lỗi chéo thư viện. Không khẳng định SOFA đã có sandbox test fail→pass. |
| A-P2 | sustainability | 2 | 4 | A dùng cạnh tranh với OS/DAP và khó thu tiền từ cá nhân để kéo về 2. Rubric cho phép comparable paid solutions và maintained solutions, không đòi proof mua sản phẩm mới. C2:R13 là bài phỏng vấn khách hàng Schneider Electric ngày 02/04/2026, mở trực tiếp ở 2A, mô tả rollout/đội adoption thực tế. **INFERENCE:** có nguồn lực duy trì loại giải pháp hướng dẫn UI, cao hơn mô hình chưa được xác nhận (3). Không cho 5 vì khác payer user-side, quyền truy cập và chi phí bảo trì từng app chưa rõ. |
| C-P4 | sustainability | 2 (H) | 4 (M) | Deadline gần và procurement khó là phản chứng hợp lệ, nhưng không chứng minh loại giải pháp này thiếu người tài trợ. C2:R42 là quyết định ngân sách cụ thể; D-C01 mở trực tiếp bổ sung funding routes trong mẫu hội đồng. **INFERENCE:** chi tiêu tương đương có thật nên 2 quá thấp. Chưa có giá tracker, hợp đồng cho startup hay cơ sở kéo dài thị trường sau deadline; đó là lý do trừ về 4, không phải chấm 5. Không đánh đồng phê duyệt với đã trả tiền. |
| C-P4 | theme | 3 (L) | 2 (M) | Đồng ý PSTN có thông báo nghỉ chính thức. Nhưng tôi rút lại lập luận trước đây rằng vậy là đủ cho 3. P1:C-P4-C6 chỉ đề xuất phiếu xác nhận; P1:C-P4-C7/C8 thừa nhận chưa chứng minh yếu tố hồi sinh và điểm nghẽn. B chỉ ra đúng vế còn thiếu: workflow/capability nào của công nghệ cũ được hồi sinh? Lịch nghỉ chỉ đáp ứng nửa anchor. Đây là thay đổi vì lý lẽ của B, không cần người dùng sửa E3. |
| C-P4 | demand | 3 (H) | 4 (H) | A có lý rằng regulator action đơn thuần khớp 3. Nhưng C2:R42 và D-C01 còn là hành vi cấp ngân sách/chuyển nhà cung cấp của đúng nhóm council. **INFERENCE:** đủ strong secondary behavioural evidence để 4; không chứng minh họ muốn tracker mới và không được lên 5. D-C01 cũng có phản chứng tiến độ tốt, nên không suy tất cả council đang mắc kẹt. |

Một bất đồng bổ sung ảnh hưởng ứng viên có tổng cao: **A-P4 innovation A=2, C=1**. C2:R19/R20/R16 (mở trực tiếp 2A) cho thấy Obsidian Web Clipper lưu local không cần Docker, SingleFile lưu HTML và wallabag có hosting/export full text. Đối lập “SaaS đắt hoặc tự dựng Docker” của P1 không còn bao phủ lựa chọn mạnh nhất. Tôi giữ 1 cho core lưu đọc/bảo toàn cá nhân; phải đo khả năng đọc lại asset hoặc provenance vượt các lựa chọn ấy mới nâng. Đây là INFERENCE về overlap, không tuyên bố mọi cạnh của link rot đã được giải.

## 2. Challenges to Agent B

| Candidate | Criterion | Điểm B | Điểm C 2B | Phản biện và bằng chứng |
|---|---|---:|---:|---|
| B-P1 | innovation | 3 (M) | 2 (M) | Lập luận tốt nhất của B là nghiên cứu chưa thành quy trình dùng lại cho long tail. Tôi công nhận gap có thể tồn tại, nhưng B·R01/C2:R32 đã đặt chính bài toán recovery/coverage/oracle; chưa chỉ ra tác vụ hoặc đầu ra workbench mới còn thiếu sau HA/NLE. Đóng gói nghiên cứu không tự thành khác biệt mức 3. Cần một model chưa được hỗ trợ và một comparison cụ thể. Điểm 2 là **INFERENCE** thận trọng, không phải xác nhận không có gap. |
| B-P1 | feasibility | 2 (M) | 1 (L) | B nhận diện đúng hai rủi ro phần cứng/phương pháp; tôi áp dụng trực tiếp vế “hardware not in hand” của anchor 1. C2:R32 được mở lại: ước lượng 4–5 ngày là retrospective ở điều kiện tác giả, không phải thời gian onboarding đội mới. Chưa biết inventory nên không nói bất khả thi/0. Nếu có thiết bị/oracle và một phép thử ngắn, tôi sẽ bỏ 1; hiện nay 2 vẫn cấp một phần khả thi chưa được chứng minh. |
| A-P7 | demand | 2 (M) | 3 (M) | Nhận phản biện của B rằng C2:R22/R23 chưa đo lỗi biên hay ý định xuất log: vì vậy sửa 4→3. Tuy nhiên các tài liệu đó là survey hiện tại về trust/provenance; C2:R07 là chi phí MRE quan sát được. Có vấn đề đáng tin ở mức 3 dù chưa có cầu cho nền tảng mới. B2-R39 chỉ snippet về doanh thu không chứng minh nỗi đau đã hết hoặc cộng đồng công khai không cần kiểm chứng. |
| A-P7 | innovation | 3 (L) | 1 (H) | B ghi rõ chưa quét kỹ agent memory và dựa B2-R40 snippet. C2:R25 mở trực tiếp cung cấp đối thủ gần hơn AI Assist/MCP tìm kiếm. Khoảng trống được nêu là fix→tri thức chia sẻ; SOFA đã phục vụ việc ấy. Chưa thấy cơ chế thực thi lockfile/test trong bài giới thiệu không đủ xác nhận khoảng trống end-to-end; phải thử cùng lỗi. Vì vậy giữ 1, đồng thời không biến giới thiệu vendor thành benchmark hiệu quả. |
| A-P2 | sustainability | 3 (M) | 4 (M) | B2-R30/R32 được B ghi là snippet; mức 3 của B phù hợp trần snippet. Tôi không nâng bằng các snippet đó. C2:R13 là nguồn tôi đã mở, có khách hàng/rollout/đội vận hành được nêu tên. Nó bổ sung hành động duy trì thực tế mà lý do “mô hình B2B có thật nhưng user-side chưa rõ” của B chưa cho trọng lượng đủ. 4 là comparable solution có bằng chứng cộng rủi ro chuyển phân khúc; không phải PMF của extension. |
| C-P4 | sustainability | 3 (M) | 4 (M) | B2-R28 về commissioning ở 2A chỉ snippet. Nay D-C01 (cùng URL B2-R26, mở toàn văn trực tiếp) và C2:R42 cho thấy ngân sách/hành động cụ thể, vượt “plausible model, not verified” của 3. Cửa sổ UK ngắn vẫn giữ trần 4; không lấy chuyển mạng tại Mỹ/Nhật làm doanh thu mở rộng đã xác minh. |

**Điểm B thuyết phục tôi:** C-P4 theme 2. Tôi từng gộp “PSTN có ngày nghỉ” và “giữ liên tục telecare” thành một sự hồi sinh. B tách đúng hai điều kiện của anchor 3. P1:C-P4-C6 chưa chỉ ra phiếu bàn giao là workflow của PSTN đã mất đi, cũng chưa cho thấy công cụ khôi phục khả năng gọi báo động. Tài liệu retirement không lấp được chỗ trống này. Tôi sửa về 2 theo hồ sơ hiện có; không thêm firmware, adapter hay sản phẩm mới để cứu theme. Lập luận này không phủ nhận nhu cầu xã hội hoặc ngân sách cho telecare.

**A-P4 innovation B=2 so với C=1:** cùng phản biện về lựa chọn local ở mục 1; các URL C2:R19/R20/R16 là chứng cứ trực tiếp, không chỉ tìm kiếm. Nếu B chỉ cho một điểm vì khả năng đóng gói thuận tiện, khác biệt 1/2 còn là phán đoán mức độ, không phải bất đồng về việc đối thủ tồn tại.

## 3. Revisions to my own scores

| candidate | criterion | 2A score | revised score | reason | triggered by A/B/C/own |
|---|---|---:|---:|---|---|
| A-P7 | demand | 4 | 3 | A và B đúng rằng trust/attribution chung cộng một MRE không phải strong behavioural evidence cho target edge-case commons. Theo anchor 3, credible current problem evidence đủ cho 3, chưa đủ 4. B là trigger chính; phản biện A và tự đối chiếu anchor củng cố. | B |
| C-P4 | theme | 3 | 2 | B chỉ ra thiếu vế “revived workflow or capability”. PSTN retirement đã rõ, nhưng phiếu bàn giao là quản lý migration và chưa được nối bằng chứng tới một năng lực cũ được hồi sinh. Sửa lỗi áp dụng anchor của chính tôi; không sửa rubric hay candidate. | B |

Không có thay đổi điểm khác. C-P4 theme confidence H→M: lịch retirement chắc, còn phân loại sản phẩm là INFERENCE; độ chắc của ngày nghỉ không truyền sang độ chắc của theme. Thêm D-C01 vào evidence C-P4 demand/sustainability; đây là bổ sung nguồn, không phải thay điểm. `changes` trong JSON chỉ ghi hai thay đổi điểm trên.

| Candidate | Weighted total 2A | Weighted total 2B | Theme 2B | Gate 2B |
|---|---:|---:|---:|---|
| A-P1 | 65.0 | 65.0 | 5 | PASS |
| A-P2 | 71.0 | 71.0 | 5 | PASS |
| A-P4 | 71.0 | 71.0 | 4 | PASS |
| A-P7 | 59.0 | 55.0 | 2 | FAIL |
| B-P1 | 64.0 | 64.0 | 4 | PASS |
| B-P4 | 56.0 | 56.0 | 3 | PASS |
| C-P1 | 67.0 | 67.0 | 4 | PASS |
| C-P4 | 60.0 | 57.0 | 2 | FAIL |

Các tổng là bảng đối chiếu, không xếp hạng. Demand giảm 1 gây −4.0 cho A-P7; theme giảm 1 gây −3.0 cho C-P4.

## 4. Judgments I keep despite disagreement

**B-P1 innovation 2 — phản biện mạnh nhất:** công cụ cộng đồng có giá trị sản phẩm dù phương pháp đã công bố. Tôi giữ 2 vì A/B chưa chỉ ra model chưa được hỗ trợ và gap workbench được kiểm tra; không trừ điểm chỉ vì dùng lại nghiên cứu. Đo được giảm công so với HA/pywemo hoặc tái tạo paper trên một model mới sẽ đủ lý do lên 3. **INFERENCE**, confidence M.

**B-P1 feasibility 1 — phản biện mạnh nhất:** Wemo hoặc Bose LAN mở có thể nhỏ hơn rất nhiều bài toán AirPort. Tôi đồng ý cơ chế thu hẹp; giữ 1 chỉ vì chưa xác nhận vật liệu/oracle của đội, không vì mọi giao thức đều khó. C2:R32 cung cấp cơ chế đã được tác giả báo cáo, không chứng minh đội thi có cùng đầu vào. **UNKNOWN** inventory, confidence L. Không chuyển điểm có điều kiện thành thực tế.

**A-P7 innovation 1 — phản biện mạnh nhất:** bản ghi có environment lockfile + test fail→pass đáng tin hơn TIL có trust score. Tôi không phủ nhận khác biệt kỹ thuật đó. Nhưng C2:R25 đã phủ core trao đổi tri thức/verification sau phiên agent; chưa có phép thử gap đủ để coi bản test là một cơ hội sản phẩm riêng ở mức 3. Giữ 1 với phạm vi core job, không nói SOFA đã làm tất cả. **INFERENCE**, confidence H cho overlap, không cho chất lượng sản phẩm vendor.

**A-P2 sustainability 4 — phản biện mạnh nhất:** doanh nghiệp thuê DAP không phải người tự cài extension; Copilot/Gemini làm biên thu phí thấp. Tôi giữ 4 vì rubric nhận comparable solutions; chi phí duy trì loại hướng dẫn này có bằng chứng hiện tại C2:R13. Kết luận chuyển payer chỉ là HYPOTHESIS nên không lên 5. Nếu so hoàn toàn vào commons cá nhân và loại tài trợ B2B, 3 có thể hợp lý hơn, nhưng đó là giả định phân khúc cần được nói rõ.

**C-P4 sustainability 4 — phản biện mạnh nhất:** ngân sách thay thiết bị/dịch vụ ARC không phải tiền mua tracker, và UK gần hết cửa sổ. Tôi giữ 4 vì C2:R42 chứng minh comparable spend: Hillingdon phê duyệt Appello 12 tháng cho 2026, 235.364 GBP. D-C01 xác nhận rộng hơn về cơ chế cấp nguồn lực, nhưng không xác minh thị trường tracker hay việc đã thanh toán. **INFERENCE** cho sustainability, confidence M. C-P4 trượt theme vẫn có thể có người tài trợ; không để gate chi phối tiêu chí khác.

**C-P4 demand 4 — phản biện mạnh nhất:** ngành đã có dịch vụ và nhiều đơn vị tự tin, nên phần thiếu có thể không phải phần mềm. Tôi giữ 4 cho hành vi ứng phó của nhóm mục tiêu, giữ innovation 2 cho gap chưa rõ; không lấy nguy cơ y tế tự nâng nhu cầu sản phẩm mới. D-C01 còn là counter-evidence chống câu chuyện “mọi nơi chưa sẵn sàng”.

**B-P1 ai 5, A/B đều 4 — phản biện mạnh nhất:** chưa tái lập độc lập, token cao, chưa generalise. Theo anchor ai 5, cơ chế có paper và oracle đo được là điều kiện; không có điều kiện chi phí thấp hay triển khai tổng quát đã xong. C2:R32 thỏa bằng chứng phương pháp ở một trường hợp theo báo cáo tác giả. Giữ 5 cho tiềm năng đóng góp kỹ thuật, không nâng độ chắc của kết quả lên VERIFIED độc lập và không nâng feasibility. Đây là INFERENCE, confidence M, không chứng nhận tái lập.

**B-P4 feasibility 1, A/B đều 2 — phản biện mạnh nhất:** có thể chọn driver SCPI và mô phỏng dụng cụ. C2:R37/R54 cho thấy framework/driver có sẵn, chưa cho đội một instrument/trace/oracle tương ứng. Một simulator tự viết kiểm tra implementation của mình không xác minh đã cứu được workflow instrument EOL. Giữ 1 (L) cho đầu vào chưa xác nhận; một capture có quyền dùng và thiết bị thật phù hợp có thể đổi điểm. Không coi mọi thiết bị phòng lab đều không nâng cấp được (C2:R39 phản chứng).

**Rà lại các ứng viên còn lại:** A-P1 giữ innovation 1 vì C2:R05 GhostPipes là revival Yahoo! Pipes bằng AI đã được trình bày ở Kiroween 2025, ngoài overlap n8n/Inoreader mà A/B cùng nhận diện; không lấy novelty framing làm innovation. A-P4 giữ demand 4 vì hành vi migration có tên ở Nhật và hoạt động hướng dẫn di chuyển ở Ottawa (C2:R17/R18), mạnh hơn chỉ một thông báo EOL nhưng không chứng minh cầu sản phẩm mới. C-P1 giữ demand 3: P1:C-P1-C2/C2:R47 và tài liệu vendor là credible problem evidence đủ anchor 3 dù chưa có đo đạc target users, nên tôi không theo B về 2; giữ innovation 2 vì C2:R10 đã có grouping đa ngữ và gap claim-level delta còn chưa benchmark. Với theme/feasibility và các ô còn lại, chứng cứ A/B không cung cấp retirement mới hay đầu vào đã xác nhận làm thay đổi anchor đang áp dụng; giữ nguyên, không lấy trung bình. Đây đều là INFERENCE, các confidence/evidence gốc còn trong JSON.

## 5. Remaining disagreements

Các mục này là việc có thể giải quyết bằng bằng chứng; không chờ user/agent trả lời trong vòng này.

| Bất đồng còn lại | Bằng chứng/phép thử sẽ giải quyết | Hệ quả điểm có thể có |
|---|---|---|
| B-P1 innovation: C2 / B3 / A4 | Chọn một model chưa có HA/NLE tích hợp phù hợp; kiểm official docs/repo hiện tại; so cùng capture và cùng task giữa baseline, quy trình paper và workbench. Công bố độ phủ, lỗi, thời gian công. | Gap hợp lý cụ thể →3; năng lực vượt baseline được đo →4–5. Chỉ wrapper →1–2. |
| B-P1 feasibility: C1 / B2 / A3 | Inventory xác nhận có hardware, app/trace/oracle còn hoạt động và quyền sử dụng; proof một lệnh/trạng thái được replay trong 48 giờ. | Có đầu vào và narrowed slice →3; truy cập được nhưng chưa thử →2; tiếp tục thiếu →1. |
| A-P7 demand: C3 / A2 / B2 | Mẫu maintainer/engineer hiện tại chia sẻ lỗi biên có thật, chi phí workarounds, đóng góp lặp lại sau bước duyệt. Phân biệt dùng AI với willingness publish. | Hành vi độc lập đủ mạnh →4–5; chỉ chứng cứ suy giảm nền tảng không nỗi đau xác minh →2. |
| A-P7 innovation: C1 / A3 / B3 | Chạy cùng bug có lockfile trên SOFA/GitHub và bản ghi được đề xuất; chứng minh thiếu thực thi tái lập, hoặc không chuyển kết quả an toàn được. Không suy absence chỉ từ trang marketing. | Gap độc lập, quan trọng →3; chỉ template/test attachment →1–2. |
| C-P4 theme: C2 / B2 / A3 | Dẫn workflow/capability lịch sử cụ thể mà PSTN từng cung cấp, đã mất trong migration, và chứng minh phiếu bàn giao phục hồi chính workflow đó; không thêm sản phẩm mới. | Nối được cả retirement và revival →3; chỉ quản lý chuyển đi →2. Không tự đổi gate bằng cách sửa E3. |
| A-P2 sustainability: C4 / B3 / A2 | Quan sát trường học/maintainer/IT sponsor duy trì hướng dẫn phía người dùng; điều khoản quyền truy cập, chi phí cập nhật và ngân sách được giao cho đúng công việc. | Comparable spend tiếp tục hỗ trợ 4; payer khác hoàn toàn và không sponsor →3 hoặc thấp hơn. |
| C-P4 sustainability: C4 / B3 / A2 | Hợp đồng hoặc ngân sách riêng cho reconciliation/handoff và nhiệm vụ còn lại sau 31/01/2027; legal scope của tracker không tự chứng nhận an toàn. | Funding trực tiếp + đường pháp lý rõ →5; chỉ one-off thay hardware và không việc còn lại →3 hoặc thấp hơn. |
| C-P4 demand C4/A3; A-P4 innovation C1/A2/B2; B-P4 feasibility C1/A2/B2 | Tương ứng: hồ sơ bàn giao gây chậm thực tế; benchmark archive local/provenance; instrument/capture có oracle thật. | Làm rõ mức độ liền kề của bằng chứng thay vì điều chỉnh cho gần trung bình. |

Đã xử lý tất cả spreads bắt buộc. Có bất đồng vẫn giữ; không coi chúng là lỗi thực thi hoặc lý do phải đồng thuận.

## 6. Rubric challenges

Không đổi trọng số, anchor hay công thức. Ba điểm cần Coordinator lưu ý cho lần hiệu chỉnh sau (không dùng làm ngoại lệ ở bảng điểm này):

1. Demand 3 nói không cần bằng chứng muốn giải pháp mới; 4 được phép dùng secondary behavioural evidence. Thiếu định nghĩa rõ mức độ gần của hành vi target problem với hành vi mua/đóng góp sản phẩm mới, nên A-P7 và C-P4 dễ bị áp hai tiêu chuẩn. Tôi sửa A-P7 về 3 vì hành vi được đo quá rộng; giữ C-P4 4 vì council đang thực sự huy động nguồn lực cho đúng công việc chuyển đổi.
2. Sustainability cho phép comparable paid products/institutional budgets ở 5 nhưng không chỉ rõ comparable đến đâu. Nếu đòi revenue của ứng viên chưa xây, gần như không candidate nào đạt; nếu chỉ cần ngành có ngân sách, lại quá dễ. Tôi dùng 4 khi có comparable spend cụ thể nhưng payer/product transfer và legal path còn thiếu.
3. Feasibility 1 phụ thuộc hardware “not in hand”, trong khi brief không có inventory đội. Điều này làm so sánh hardware/software lệch theo thông tin đầu vào. Tôi tuân anchor 1 với confidence L, giữ rõ UNKNOWN và báo điểm có điều kiện riêng. Theme 3 cũng có hai vế độc lập: thông báo nghỉ và revival; sự mơ hồ ở “revived capability” không cho phép bỏ vế thứ hai. Thay đổi C-P4 là sửa cách áp dụng, không phải phản đối hay sửa gate.

## 7. New references

Chỉ nguồn **mới trong hồ sơ C** ở 2B; không chép lại 55 refs 2A. C2:R25/R32 được mở lại nhưng không đếm mới. Chất lượng nguồn dùng trọng số A/T/M/C/F/R/B = 20/20/20/15/10/10/5; weighted = `4A+4T+4M+3C+2F+2R+B`. Chất lượng nguồn không cộng vào candidate score.

| Ref ID | URL | Title | Publisher | Pub date | Accessed | Claims | 7 scores A/T/M/C/F/R/B | Weighted /100 | Source Reliability | Reference Relevance |
|---|---|---|---|---|---|---|---|---:|---|---|
| D-C01 (mới với C; từ B2-R26) | [Nguồn](https://www.local.gov.uk/publications/digital-switchover-insights-partners-care-and-health-pch-digital-switchover-survey) | Digital switchover: insights from the Partners in Care and Health (PCH) digital switchover survey | Local Government Association / PCH; commissioned by DHSC | 2026-03-26; snapshot khảo sát May 2025 | 2026-11-25, mở trực tiếp toàn văn thành công | Nội dung nguồn: 55/63 council có funding approach; 4/63 chưa xác nhận ARC status. Mẫu 66 phản hồi, gồm 63 council adult social care (~41% upper-tier), không đại diện toàn ngành. Nhiều council tự tin/đã tiến bộ, là phản chứng cho nhu cầu phổ quát. VERIFIED về nội dung báo cáo; INFERENCE về nhu cầu còn lại và sustainability của tracker, không xác nhận hiệu quả hay willingness-to-buy. | 5/4/3/5/4/4/4 | 83 | High | High cho response/funding; Medium cho tracker riêng |

Không dùng số liệu D-C01 như một phép kiểm độc lập cho tỷ lệ alarm analog của DHSC: population, thời điểm và mẫu khác nhau. Publication 2026 không biến snapshot May 2025 thành tình trạng đo tháng 11/2026. Không có nguồn mới bị lỗi hoặc claim dựa duy nhất vào snippet được dùng để giữ/nâng điểm trên 3.
