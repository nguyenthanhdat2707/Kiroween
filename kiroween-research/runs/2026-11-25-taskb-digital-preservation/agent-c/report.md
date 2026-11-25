# Task B Round 1 — Agent C

## Metadata

- Run: `2026-11-25-taskb-digital-preservation`; Round 1, khám phá độc lập.
- Model/effort quan sát từ launch args: **not observable / not observable**. Preamble yêu cầu gpt-6.1-sol/Medium nhưng không cung cấp receipt xác nhận; không coi cấu hình mong muốn là runtime đã đo.
- Bắt đầu UTC: 2026-11-25T12:27:00Z, xấp xỉ theo lần đọc đầu; kết thúc biên soạn UTC: 2026-11-25T12:38:32Z. Khoảng 11 phút 32 giây tổng; đồng hồ UTC quan sát lần đầu 12:28:28Z, nên phần trước đó chỉ là ước lượng.
- Khoảng 27 truy vấn tìm kiếm; 34 tài liệu được sử dụng: **30 mở trực tiếp có nội dung, 4 snippet-only**. Không đếm các kết quả tìm kiếm bị bỏ qua. Mở thành công không đồng nghĩa đã kiểm chứng độc lập.
- Không phỏng vấn, khảo sát, chạy phần mềm cộng đồng, thanh toán hay kiểm tra gameplay; không có số liệu token đáng tin cậy. Không nâng reasoning effort. Chỉ ghi trong agent-c/, không đọc báo cáo agent khác hoặc báo cáo Phase 1/2.
- Lỗi truy cập: 12 lần không lấy được nội dung dự định, gồm Pretendo homepage 403 qua web (hai lần) và urllib (một lần); donation FAQ bị restricted URL; Software Heritage activity report 502; trang gốc bài Eve tại Iowa State 403 (đọc bản PDF mirror); EUR-Lex Directive 2019/790 HTML/PDF và GDPR trả trang chống bot (ba lần); một URL EDPB đoán sai trả 404 (đã tìm đúng trang); EaaSI handbook không truy cập được (dùng SPN); thao tác find trên trang WP29 timeout. Không biến những lỗi này thành bằng chứng nội dung.
- 42 claim độc nhất: **VERIFIED 6; INFERENCE 25; HYPOTHESIS 7; UNKNOWN 4**. Nhãn tiếng Việt tương ứng: ĐÃ XÁC MINH / SUY LUẬN / GIẢ THUYẾT / CHƯA RÕ. Số liệu từ một nghiên cứu được mô tả đúng giới hạn nhưng vẫn giữ INFERENCE nếu chưa có đối chứng cho chính mệnh đề đó.
- Hoàn thành hợp đồng Round 1 ở mức desk research; kiểm chứng hành vi hiện tại, pháp lý từng nước và willingness to pay còn mở. Không chọn sản phẩm hay ý tưởng hackathon cuối cùng.

## 1. Method

Dùng **problem tree** để tách nguyên nhân nền tảng đóng cửa khỏi cơ chế làm mất giá trị; **stakeholder/JTBD** để tách người hưởng lợi, người quyết định và người chi tiền; **alternative analysis** để kiểm tra liệu nhu cầu đã được giải quyết; **falsification** để ưu tiên thử nghiệm có thể loại hướng nghiên cứu. Không chạy đầy đủ mọi framework và không thiết kế ứng dụng.

Luồng nghiên cứu: nền tảng/định dạng lịch sử → người sử dụng và mục đích ban đầu → suy giảm/đổi nơi quản lý → giải pháp thay thế → phần giá trị còn thiếu → nhu cầu hiện tại → giả thuyết. Ba không gian là tạp chí học thuật nhỏ, dịch vụ trò chơi nhiều người, và quyền/ngữ cảnh trong kho di sản cộng đồng. Góc tạp chí là bàn giao trách nhiệm và tính đầy đủ của hồ sơ học thuật, không phải bookmark/link rot cá nhân; góc trò chơi là trải nghiệm tập thể và duy trì tổ chức, không phục hồi thiết bị cloud đã nghiên cứu trước.

Quy tắc: claim có ID và nhãn tại lần định nghĩa; các bảng sau dùng lại ID, không tạo chứng cứ mới. Reference rubric chấm **một nguồn đối với claim được chỉ định**, không chấm uy tín chung của tổ chức rồi áp cho mọi kết luận. VERIFIED chỉ dùng khi nguồn sơ cấp đã mở và có xác nhận độc lập, hoặc kiểm tra lặp lại được. Hai trang cùng nhà cung cấp không được tính là hai nguồn độc lập.

## 2. Root causes

**C-G-C1 — INFERENCE.** Mất hồ sơ học thuật là hiện tượng quan sát được: Laakso và cộng sự tìm 174 tạp chí OA biến mất trong giai đoạn 2000–2019; Eve nghiên cứu 7.438.037 DOI và không xác nhận được bảo tồn cho 27,64% mẫu. Hai mẫu và định nghĩa khác nhau: không suy ra 27,64% bài đã mất, cũng không suy ra tỷ lệ hiện tại năm 2026. [R01](https://arxiv.org/abs/2008.11933), [R02](https://microblogging.infodocs.eu/wp-content/uploads/2024/01/jlsc-16288-eve.pdf).

**C-G-C2 — INFERENCE.** Cây nguyên nhân được đề xuất từ R01/R02/R08/R30:

```text
Nguyên nhân nền: ngân sách/tài trợ hữu hạn; chủ thể đổi ưu tiên;
                kiến thức vận hành tập trung; phần mềm/hạ tầng già đi
       ↓
Nền tảng không còn được vận hành hoặc được chuyển giao
       ↓ nếu thiếu bàn giao, quyền, bản sao đủ và khả năng đọc/chạy
Mất truy cập / mất ngữ cảnh / mất chức năng / mất quan hệ cộng đồng
       ↓
Không kiểm tra được nghiên cứu; không sử dụng tài sản đã mua;
không tiếp cận được ký ức cộng đồng
```

Suy giảm adoption có thể là nguyên nhân doanh thu giảm; cũng có thể là triệu chứng của dịch vụ khó dùng hoặc công nghệ đã bị thay thế. Nintendo nêu vòng đời và sử dụng giảm cho eShop; nguồn đó **không chứng minh** đây là nguyên nhân duy nhất của mọi dịch vụ online bị đóng. Không có dữ liệu đủ để phân bổ tỷ trọng nguyên nhân giữa chi phí, cạnh tranh và quản trị. [R08](https://en-americas-support.nintendo.com/app/answers/detail/a_id/57847), [R30](https://www.unesco.org/en/legal-affairs/charter-preservation-digital-heritage).

**C-G-C3 — INFERENCE.** Thất bại thương mại không chứng minh giá trị sử dụng bằng không. Chức năng chơi local còn sống sau khi online ngừng; chương trình ELDP đổi nơi chủ trì thay vì biến mất. Ngược lại, giữ nguyên hệ điều hành/phần mềm cũ có thể chỉ là một phương tiện đọc tài liệu: không nhất thiết phải duy trì toàn bộ tổ chức cũ. [R09](https://www.capcom-support.com/hc/en-us/articles/11752429426204-Discontinuation-of-Online-Services-for-Nintendo-3DS-and-Wii-U-Software), [R25](https://www.soas.ac.uk/about/news/soas-marks-eldp-move-new-base-berlin), [R29](https://www.softwarepreservationnetwork.org/eaasi-software-development-update/).

**C-G-C4 — INFERENCE.** Không nên bảo tồn toàn bộ nền tảng nếu bản thay thế giữ được công việc cần làm, nội dung chỉ là bản trùng, không có người quản lý hợp pháp, hoặc chi phí vận hành vượt giá trị sử dụng và giá trị chứng cứ dự kiến. Đây là tiêu chí ra quyết định, không phải kết quả đo ROI. UNESCO yêu cầu tuyển chọn theo giá trị dài hạn; không đặt nghĩa vụ giữ mọi thứ. Đôi khi nên giữ bằng chứng có kiểm soát thay vì mở lại cộng đồng độc hại hoặc tài liệu nhạy cảm. [R30](https://www.unesco.org/en/legal-affairs/charter-preservation-digital-heritage), [R22](https://www.paradisec.org.au/blog/2024/02/using-raspberry-pi-in-ranongga/).

## 3. Stakeholders and demand

| Stakeholder cụ thể | JTBD | Hành vi hiện có | Đóng góp | Trả tiền/tài trợ | Loại bằng chứng |
|---|---|---|---|---|---|
| Biên tập viên OJS trong Texas Digital Library; thư viện chủ trì | Bài đã công bố còn đọc được khi tạp chí ngừng | Có quy trình bật plugin, kiểm tra status, nhờ helpdesk | Cấu hình, quyền ký terms | PKP PN miễn phí cho tạp chí; ngân sách cho một công cụ mới chưa biết | Demonstrated ở mức quy trình vận hành; C-G-C5, C-G-C8 |
| Tác giả, giảng viên, người đọc tạp chí nhỏ | Truy xuất và kiểm tra công trình gốc | Nghiên cứu đã đo mất/thiếu hồ sơ | Chưa đo mức thời gian họ bỏ ra | Chưa thấy giao dịch của cá nhân | Mixed; C-G-C1; không dùng mất mát làm bằng chứng mua |
| Người sở hữu Wii U/3DS và nhóm phát triển Pretendo | Tiếp tục chơi cùng nhau | Có dự án server, thư viện transport và hướng dẫn contribution | Có repository, quy tắc DCO; không đo giờ tình nguyện | Donation FAQ nói hỗ trợ hosting và một vị trí dev; chỉ đọc snippet, chưa có số thu | Mixed; C-G-C18, C-G-C19; C-O2-C2 |
| Công dân EU ký Stop Destroying Videogames | Giữ khả năng dùng trò chơi sau chấm dứt dịch vụ | 1.294.188 chữ ký đã xác nhận | Đóng góp hành vi vận động | Chữ ký không phải willingness to pay | Demonstrated cho nhu cầu chính sách; C-G-C19 |
| Kulu Language Institute, Ranongga | Đưa ghi âm về người nói và người học | Mang kho ghi âm đi chia sẻ; thử Raspberry Pi và hỗ trợ từng người | Thời gian giáo viên, người nghiên cứu, người tổ chức | Grant tài trợ số hóa; không có bằng chứng hộ gia đình mua thuê bao | Demonstrated địa phương; C-G-C17 |
| BBAW, SOAS, ELDP/ELAR; PARADISEC | Giữ kho và trách nhiệm qua kỳ tài trợ/chủ trì | Chuyển đơn vị chủ trì; nhiều vòng grant | Nhân sự chuyên môn và governance | Có grant công bố; không phải doanh thu cho nhà cung cấp mới | Demonstrated loại chi tiêu, C-G-C12/C-G-C13 |
| Người giữ cultural protocols trong Mukurtu; cộng đồng nguồn | Quyền truy cập và ngữ cảnh không bị mất khi di chuyển | Có roles, protocols, hướng dẫn pre-migration | Cần quyết định quyền của cộng đồng | Chưa biết ngân sách cho kiểm tra chuyển giao riêng | Mixed; C-G-C14/C-G-C15 |
| Nhà vận hành nền tảng thương mại sắp đóng | Giảm nghĩa vụ kéo dài và xử lý bàn giao | Có thông báo chấm dứt, có chức năng offline còn lại | Mức sẵn sàng cung cấp mã/server chưa biết | Không có bằng chứng họ trả tiền cho bên bảo tồn | Hypothetical cho dịch vụ bàn giao; C-G-C23 |
| Notre Dame, University of Virginia, Yale và SPN | Đọc được tài liệu phụ thuộc phần mềm cũ | Tham gia EaaSI nodes | Chia sẻ môi trường và kinh nghiệm | Chưa đọc ngân sách hiện tại | Demonstrated tham gia lịch sử, không đo adoption 2026; C-G-C11 |

**C-G-C5 — VERIFIED.** PKP PN dùng LOCKSS để bảo tồn nội dung OJS và có đường phục hồi sau trigger event; TDL mô tả quy trình triển khai, điều kiện và kiểm tra status độc lập với tài liệu PKP. Điều này xác nhận một lựa chọn vận hành có thật, không chứng minh mọi tạp chí bật plugin đều đã nộp đủ dữ liệu. [R03](https://github.com/pkp/pkp-docs/blob/main/pkp-pn/en/index.md), [R04](https://texasdigitallibrary.atlassian.net/wiki/spaces/OAJ/pages/1762295809).

**C-G-C8 — INFERENCE.** Infra Finder, bản cập nhật 19-09-2025, ghi 1.763 tạp chí và hai tạp chí đã trigger. Đây là thông tin hồ sơ về hành vi bảo tồn, chưa kiểm đếm độc lập và không coi là tổng hiện tại. [R06](https://infrafinder.investinopen.org/solutions/pkp-preservation-network).

## 4. Preservation dimensions

Các đánh giá giá trị/khả thi trong bảng là SUY LUẬN từ các claim chỉ định; không phải benchmark hay cost estimate.

| Chiều | Giá trị cần giữ | Thực tế kỹ thuật | Thực tế kinh tế | Cơ sở |
|---|---|---|---|---|
| Content | Bài, ảnh, âm thanh nguyên gốc | Cao hơn với file và metadata xuất được; crawl có thể thiếu | Có mô hình dùng chung; tuyển chọn vẫn cần | C-G-C1/C-G-C5/C-G-C9 |
| Knowledge | Quan hệ giữa file, tác giả, bối cảnh, quy tắc sử dụng | Cần metadata và kiểm tra ngữ nghĩa; giữ byte chưa đủ | Lao động chuyên môn có thể là rào cản chính | C-G-C14/C-G-C15/C-G-C17 |
| Software functionality | Chạy lại chương trình và tương tác | Emulation giữ môi trường cũ; server ngoài máy là ranh giới khác | Môi trường chia sẻ giảm lặp việc; vẫn cần bảo trì | C-G-C11/C-O2-C2 |
| User data and workflows | Quyền, trình tự công việc, trạng thái và quan hệ | Có export/migration nhưng custom fields và quyền cần kiểm tra | Không có dữ liệu chi phí hoàn tất một lần chuyển | C-G-C6/C-G-C15/C-G-C20 |
| Community | Có người thật cùng tham gia, điều phối, moderation | Không thể suy ra cộng đồng sống từ database hay server chạy | Người quản lý phải tiếp tục đóng góp; chưa đo retention | C-G-C19/C-G-C23; C-O2-C3 |
| Heritage | Tiếp cận chứng cứ văn hóa và ngôn ngữ | Kho có quyền kiểm soát, cơ chế offline đã có | Grant và chủ trì tổ chức có tiền lệ; không tự duy trì vô hạn | C-G-C12/C-G-C13/C-G-C16/C-G-C17 |
| Operational | Hoàn thành dịch vụ cũ sau khi nhà vận hành rời đi | Khó nhất khi phụ thuộc account, server và bản quyền không chuyển | Chi phí định kỳ gồm nhân sự, an ninh, hạ tầng và governance | C-G-C10/C-G-C18/C-G-C21/C-G-C23 |

## 5. Existing solutions and gaps

**C-G-C6 — INFERENCE.** PKP nói rõ bảo tồn của PN không thay backup OJS để khôi phục site. Phân biệt này giới hạn cả luận điểm “đã có archive là đủ” lẫn luận điểm “cần tạo một archive mới”. [R03](https://github.com/pkp/pkp-docs/blob/main/pkp-pn/en/index.md).

**C-G-C7 — INFERENCE.** JASPER đã phối hợp PKP PN, CLOCKSS và Internet Archive theo ba đường: OJS, upload và crawl. Có điều kiện về DOAJ, giấy phép và tài chính; không thể tuyên bố tạp chí nhỏ thiếu mọi phương án miễn phí. [R05](https://doaj.org/preservation/).

**C-G-C9 — INFERENCE.** Wayback FAQ nêu giới hạn với nội dung không crawl được và JavaScript còn phụ thuộc server nguồn. Bản lưu web không đảm bảo dịch vụ phía server hoặc toàn bộ site được phục hồi. [R27](https://help.archive.org/help/using-the-wayback-machine/).

**C-G-C10 — INFERENCE.** IPFS cần pin để tránh garbage collection trên node. Suy ra định danh phân tán không tự tạo ngân sách, người giữ bản sao hoặc cam kết cung cấp lâu dài; đây là giới hạn của “đưa lên decentralized storage”, không phải kết luận mọi giải pháp decentralized đều thất bại. Chưa chạy thử node. [R26](https://docs.ipfs.tech/how-to/pin-files/).

**C-G-C11 — INFERENCE.** EaaSI đã có nodes tổ chức và chia sẻ môi trường emulation; tài liệu phát triển mô tả môi trường có version và emulator tương ứng. Đó là đối thủ mạnh cho việc làm phần mềm cũ đọc được tài liệu. Nguồn kỹ thuật năm 2019 chỉ chứng minh cơ chế đã tồn tại, chưa chứng minh vận hành/giá hiện tại hay phục hồi được backend thương mại. [R28](https://www.softwarepreservationnetwork.org/emulation-as-a-service-infrastructure/participants/), [R29](https://www.softwarepreservationnetwork.org/eaasi-software-development-update/).

| Cách tiếp cận | Điểm mạnh | Giới hạn/rào cản | Khoảng trống có thể kiểm tra, chưa xác nhận |
|---|---|---|---|
| Internet Archive/web archiving | Giữ dấu vết và file công khai, không cần nhà cung cấp sống | Crawl, auth, backend, completeness | Bản sao có đủ thành phần để thực hiện JTBD? C-G-C9 |
| Software preservation/emulation | Giữ hành vi chương trình cũ, chia sẻ môi trường | Licensing, image, kiến thức máy cũ; backend không mặc nhiên có | Tránh làm lại EaaSI; chỉ xét dependency chưa được đáp ứng. C-G-C11 |
| Portability/migration | Chuyển cho người quản lý mới thay vì nuôi nền tảng cũ | Schema, custom fields và semantics quyền | Kiểm tra tổn thất của chính bộ chuyển có sẵn. C-G-C15/C-G-C20 |
| Open source | Mã và contribution của Pretendo hiện hữu | Quyền với asset và dữ liệu không đi kèm quyền với mã | Maintainer succession, chưa đo nhu cầu riêng. C-O2-C2/C-O2-C3 |
| Self-hosting | Chủ thể mới có thể quản lý môi trường | Chuyển việc cập nhật/an ninh/on-call cho chủ thể đó | Chưa có bằng chứng chủ cộng đồng muốn tự vận hành. C-G-C11/C-G-C23 |
| Decentralized storage | Không buộc một địa chỉ phục vụ duy nhất | Vẫn cần pin và vận hành; không giữ quyền hoặc workflow | Không coi storage là khoảng trống chính. C-G-C10 |
| Community-led revival | Có mã và người đóng góp thật | Chưa kiểm tra gameplay, số active users, moderation hay finances | Không xây bản sao Pretendo; kiểm tra nhu cầu nhóm bảo trì. C-O2-C2 |
| Digital heritage systems | Mukurtu giữ protocols; PARADISEC có offline; ELAR có chuyển chủ trì | Tùy biến, người có thẩm quyền, mạng/thiết bị | Chỉ xét mất semantics trong chuyển giao có thật. C-G-C12/C-G-C14–17 |
| Scholarly preservation networks | PKP PN/JASPER và Keepers Registry đã tổ chức bảo tồn/giám sát | Eligibility, coverage, dữ liệu status không luôn ở article level | Không tuyên bố “chưa có dashboard”: ISSN đã công bố kế hoạch timeline. C-O1-C2 |

## 6. Sustainability

**C-G-C12 — VERIFIED.** SOAS và BBAW đều xác nhận ELDP đổi cơ sở sang Berlin và archive liên quan được duy trì/chuyển theo. Hai đơn vị là bên đi và bên nhận, xác nhận độc lập ở mức tổ chức; đây là continuity có quản trị, không phải bằng chứng archive từng chết rồi hồi sinh. [R24](https://www.bbaw.de/files-bbaw/presse/pressemitteilungen/pressemitteilungen-2021/PM-18_Dokumentation_bedrohter_Sprachen_englisch/BBAW_PM_ELDP_engl.pdf), [R25](https://www.soas.ac.uk/about/news/soas-marks-eldp-move-new-base-berlin).

**C-G-C13 — INFERENCE.** BBAW công bố €21 triệu cho chương trình 10 năm, không phải toàn bộ tiền cho phần mềm archive; PARADISEC liệt kê grant nhiều kỳ và đề nghị dự trù phí archiving trong grant, có ví dụ AUD20/file video. Đó là bằng chứng có nguồn tài trợ/giá công bố cho loại công việc này; chưa có hóa đơn hoặc chi phí dài hạn trên mỗi collection. [R20](https://www.paradisec.org.au/about-us/funding/), [R23](https://www.paradisec.org.au/deposit/costing-a-deposit/), R24.

Khung chi phí đề xuất để kiểm tra, thuộc C-G-C2/C-G-C4: tổng chi phí gồm tiếp nhận/kiểm quyền, metadata, lưu nhiều bản và fixity, chuyển định dạng, thiết bị/egress, nhân sự hỗ trợ, an ninh/moderation, và lần bàn giao tiếp theo. Không chỉ là GB/tháng. Không có dữ liệu để đưa con số tổng hoặc ROI.

| Mô hình | Ai hưởng lợi / ai trả / ai giữ | Điều kiện sống được | Failure mode |
|---|---|---|---|
| Consortium thư viện | Tác giả/người đọc; các tổ chức cùng tài trợ; nhân viên kho vận hành | Sứ mệnh dài hạn, quyền trigger rõ | Hết kinh phí hoặc không nộp đủ; C-G-C5–8 |
| Grant + tổ chức nhận trách nhiệm | Cộng đồng/người nghiên cứu; quỹ/đại học; archive và cộng đồng quản lý | Có chủ thể kế nhiệm và chi phí sau grant | Chỉ tài trợ digitization, bỏ phí stewardship; C-G-C12/C-G-C13 |
| Donation + tình nguyện | Người chơi; donor; đội server | Tập người đóng góp ổn định và giới hạn hỗ trợ | Burnout, thiếu moderation, pháp lý; C-O2-C2/C-O2-C6 |
| Dịch vụ thương mại chuyển giao một lần | Operator/thư viện có thể trả; archive nhận | Hợp đồng cho artefact được quyền chuyển và tiêu chí nghiệm thu | Người hưởng lợi không có ngân sách, vendor không hợp tác; C-G-C23 |

Không có bằng chứng một doanh nghiệp “bảo tồn mọi nền tảng” tự trang trải được. Cũng chưa có bằng chứng nonprofit hoặc OSS tự động tránh được thất bại vận hành (C-G-C4/C-G-C10/C-G-C23).

## 7. AI contribution

**C-G-C22 — HYPOTHESIS.** AI có thể giảm thời gian tìm lỗi metadata, mô tả mapping schema hoặc gợi ý trường cần review; chưa tìm được benchmark trực tiếp cho ba công việc trong báo cáo. Không có cơ sở chấm AI load-bearing. Các thí nghiệm dưới đây là đề xuất, chưa chạy.

| Công việc | Baseline thường | Vai trò AI có thể đo | Oracle và điều kiện bác bỏ |
|---|---|---|---|
| Kiểm đầy đủ hồ sơ tạp chí | Manifest + checksum + DOI/ISSN reconciliation | Gợi ý ghép tên/trường khi metadata nhiễu | Nhãn thủ công trên mẫu; precision/recall và phút review, tính cả sửa lỗi AI |
| Hỗ trợ maintainer server cũ | Protocol specification, log parser, golden traces, test deterministic | Gợi ý tài liệu/định vị khác biệt | Kết quả session và regression oracle; bỏ AI nếu không giảm giờ hoặc đưa sai semantics |
| Chuyển cultural metadata | Explicit mapping + role/access matrix + người có thẩm quyền | Đánh dấu trường có nguy cơ mất nghĩa | Reviewer cộng đồng xác nhận; đo false negative quyền truy cập, không để AI tự cấp quyền |

AI không cần cho lưu byte, hashing, pinning, nén, bản sao, xuất schema biết trước hoặc thực thi access control. Sinh transcript/summary chỉ có thể là lớp dẫn xuất có provenance; không thay file nguồn hay xác nhận quyền cộng đồng. Giữ nguyên nội dung gốc và đo lao động review là điều kiện thí nghiệm C-G-C22.

## 8. Legal and ethical constraints

**C-G-C14 — INFERENCE.** Mukurtu yêu cầu cultural protocols cho media ở v4; Local Contexts cho cộng đồng tùy chỉnh và phê duyệt Labels, đồng thời xuất được text/icon. Các cơ chế đó cho thấy một file public có thể vẫn cần bối cảnh và quy tắc sử dụng; không suy ra Label là giấy phép copyright hay công cụ kỹ thuật chặn mọi sao chép. [R18](https://docs.mukurtu.org/media/ManageMediaAccessWithProtocols/), [R19](https://localcontexts.org/support/working-with-labels/).

**C-G-C15 — INFERENCE.** Tài liệu migration Mukurtu 3→4 nêu custom content/fields ngoài stock không được công cụ bao phủ, có hình không chuyển và media chưa test live. Đây là giới hạn do nhà phát triển công bố, không phải lỗi đã tự tái hiện. [R17](https://docs.mukurtu.org/migration/PM02Activities/).

**C-G-C20 — INFERENCE.** Snippet văn bản GDPR Art.20 cho thấy portability có điều kiện về consent/contract và xử lý tự động; không thể coi là quyền lấy toàn bộ mã, asset hoặc dữ liệu của người khác. EUR-Lex trực tiếp bị bot gate, nên không nâng VERIFIED. Với Directive 2019/790 Art.6, chỉ thấy snippet quy định sao chép bảo tồn cho cultural heritage institutions đối với tài sản trong permanent collections; chưa xác nhận bản luật quốc gia triển khai hoặc quyền phân phối. [R32](https://eur-lex.europa.eu/eli/reg/2016/679), [R33](https://regelex.com/legislation/32019L0790/art_6?as=adopted&on=2026-11-10).

**C-G-C21 — INFERENCE.** Hồ sơ khuyến nghị Copyright Office tháng 10-2024 phân biệt computer programs và videogames, có giới hạn mục đích, chủ thể và premises. Đây không phải giấy phép tổng quát mở server công cộng. Chưa kiểm final rule hiện hành 2026 nên phạm vi exemption áp cho từng trường hợp vẫn CHƯA RÕ; không được dùng nghiên cứu này để phê chuẩn dịch vụ revival. [R31](https://www.copyright.gov/1201/2024/2024_Section_1201_Registers_Recommendation.pdf).

| Phạm vi | Ràng buộc cần phân biệt | Trạng thái cho quyết định |
|---|---|---|
| Hoa Kỳ | Quyền sao chép, circumvention và cung cấp cho người dùng là các câu hỏi riêng; tên/trademark và asset không được cấp theo license của server | Chỉ có hồ sơ 2024 và DCO dự án; không xác nhận quyền vận hành công cộng. C-G-C21, R13/R14 |
| EU/EEA | Portability không tương đương sao chép cả cộng đồng; exception bảo tồn tổ chức không mặc nhiên cho redistributing công khai | Chưa kiểm bản triển khai quốc gia/ngoại lệ mới; C-G-C20 |
| Australia/Solomon Islands | Quyết định của chủ thể văn hóa và rủi ro công bố thông tin tổ tiên/đất phải được xem xét bên cạnh copyright | Có ca thực địa, không có khảo cứu luật địa phương; C-G-C17 |
| Nhật Bản và châu Á khác | Thông báo kết thúc dịch vụ xác nhận mất tính năng, không cấp quyền phục hồi hay tái phát hành | Luật và giấy phép cho từng artefact chưa nghiên cứu; C-G-C23, R10 |
| Xuyên biên giới | Chủ thể dữ liệu, người giữ quyền, cộng đồng và đơn vị nhận archive có thể khác nhau | Cần consent/access basis và chủ thể xử lý yêu cầu rút/xóa trước chuyển; đề xuất theo C-G-C14/C-G-C20 |

Rủi ro cụ thể cần test: private messages và social graph không phải chỉ thuộc người xuất; giấy phép OSS của code không cấp quyền dataset/game assets; quyền sở hữu carrier không đồng nghĩa quyền tái phát hành nội dung. PKP terms yêu cầu người ký có thẩm quyền và thông tin license chính xác (R04). Cách xử lý đề xuất là giới hạn collection có quyền rõ và access matrix được người có thẩm quyền ký, không tự suy quyền từ khả năng crawl (C-G-C14/C-G-C20/C-G-C21).

## 9. International evidence

**C-G-C16 — INFERENCE.** PARADISEC công bố năm 2026 cách tạo bộ sưu tập HTML ngoại tuyến đi cùng RO-Crates. Đây là phản chứng trực tiếp cho ý tưởng rằng catalog phụ thuộc duy nhất vào dịch vụ online; chưa chạy công cụ để kiểm tính hoàn chỉnh. [R21](https://www.paradisec.org.au/blog/2026/03/offline-static-collections/).

**C-G-C17 — INFERENCE.** Debra McDougall ghi việc Kulu Language Institute chia sẻ ghi âm tại Ranongga, gặp điện thoại/mạng/navigation khó dùng và cân nhắc ghi âm về genealogy/đất có thể gây tranh chấp. Đây là hành vi sử dụng thực do người tham gia thuật lại, chưa có đối chứng độc lập và không đại diện mọi cộng đồng. [R22](https://www.paradisec.org.au/blog/2024/02/using-raspberry-pi-in-ranongga/).

**C-G-C18 — VERIFIED.** Nintendo xác nhận online Wii U/3DS kết thúc 08-04-2024 theo giờ Bắc Mỹ; Capcom xác nhận hậu quả với game của họ, phân biệt online/local và DLC. Thông báo Nhật ghi 09-04-2024 09:00 JST, phù hợp khác múi giờ. [R08](https://en-americas-support.nintendo.com/app/answers/detail/a_id/57847), [R09](https://www.capcom-support.com/hc/en-us/articles/11752429426204-Discontinuation-of-Online-Services-for-Nintendo-3DS-and-Wii-U-Software), [R10](https://support.nintendo.com/jp/information/2023/1004.html).

**C-G-C19 — VERIFIED.** EC công bố 1.294.188 statements of support đã xác nhận cho Stop Destroying Videogames vào 26-01-2026; Heise xác nhận cùng số. Đây là bằng chứng nhu cầu chính sách xuyên EU, không phải số khách hàng của revival service; không suy ra initiative đã thành luật. [R15](https://citizens-initiative.europa.eu/news/14th-valid-initiative-stop-destroying-videogames-submitted-commission-examination-2026-01-26_en), [R16](https://www.heise.de/en/news/Citizens-initiative-1-294-188-signatures-for-Stop-Destroying-Videogames-11154579.html).

| Vùng | Ca trực tiếp và actor | Giới hạn chuyển giao kết luận |
|---|---|---|
| North America | TDL/PKP; Nintendo America/Capcom; Notre Dame/UVA/Yale trong EaaSI | Có hạ tầng tổ chức; không chứng minh cộng đồng nhỏ tự trả được; R03/R04/R08/R09/R28 |
| Europe | ELDP/ELAR, SOAS→BBAW; EC và công dân ký ECI; ISSN tại Paris | Có chuyển chủ trì/tài trợ; quyền và mô hình tài chính không tự áp cho nước khác; R07/R15/R24/R25 |
| Asia | Nintendo Nhật xác nhận shutdown cùng nền tảng | Chưa có bằng chứng trực tiếp người chơi Nhật trả tiền/di cư; thông báo vendor không đủ để chấm demand địa phương cao; R10 |
| Other | PARADISEC Australia và Kulu Language Institute, Solomon Islands | Đây là Oceania, không gộp nhầm vào Asia; thiết bị, ngôn ngữ và quyền cộng đồng khác nhau; R20–24 |

Chưa tìm được trong lượt này ca cộng đồng/tài trợ châu Á độc lập cho C-O3; các truy vấn đã dùng gồm `site.paradisec.org.au funding archive endangered languages collections`, `site.mukurtu.org cultural protocols export migration Mukurtu 4`, `site.paradisec.org.au Ranongga Raspberry Pi`. Chưa có bằng chứng trực tiếp châu Phi/Mỹ Latin cho ba không gian; ISSN chỉ mô tả chênh lệch coverage vùng, không phải hành vi người dùng ở một tổ chức được phỏng vấn. Không dùng các khoảng trống tìm kiếm này để nói vấn đề không tồn tại.

## 10. Opportunity spaces

Đây là ba không gian vấn đề để kiểm tra, không phải ba đề xuất xây ứng dụng. Điểm 0–5 theo anchors Phase 2 chỉ tóm tắt chứng cứ; không cộng tổng, không so Phase 2, không dự đoán chấm giải. H/M/L là độ tin cậy; nguồn liên kết qua các claim và bảng References.

### C-O1 — Tính đầy đủ và trách nhiệm bàn giao của hồ sơ tạp chí nhỏ

**C-O1-C1 — INFERENCE.** Nhu cầu cần khảo sát là bảo toàn hồ sơ có thể kiểm tra được khi tạp chí/người chủ trì ngừng, gồm những thành phần mà bản archive không chứng minh đã nhận đủ. Target: library publishing staff và biên tập viên tạp chí nhỏ, không phải mọi người có bookmark. Mất tạp chí trong R01 và hạn chế article-level observation trong R02 là động cơ; chưa có mẫu tạp chí sắp đóng hiện tại. Dimensions: content, knowledge, user-data-workflows, operational.

**C-O1-C2 — INFERENCE.** Strongest alternative là **JASPER + PKP PN + Keepers Registry**. JASPER đã ghép đường nộp; ISSN 2025–2029 đã đề xuất công cụ chronological archival status và hướng tới issue/volume. Phản chứng mạnh nhất: nhu cầu cốt lõi có thể được giải bằng dịch vụ hiện có và hỗ trợ cấu hình; “dashboard bảo tồn” chưa phải khác biệt được chứng minh. R05/R07.

**C-O1-C3 — HYPOTHESIS.** Phần chưa được đáp ứng có thể là chuyển giao có nghiệm thu cho supplementary files, thay đổi metadata và trạng thái bài, thay vì một nơi lưu PDF mới. Không có bằng chứng rằng mọi PKP deposit đều thiếu các loại này; cần kiểm collection thật. Why now: ISSN đang đầu tư giám sát và hạ tầng đang có, nên kiểm khoảng trống thực tế trước khi thêm lớp mới. R02/R03/R07.

**C-O1-C4 — UNKNOWN.** Người sẽ chi tiền cho phần việc bổ sung chưa được xác định. Commercial viability: thư viện/consortium có thể tài trợ công việc stewardship; comparable ở đây là preservation service miễn phí và đóng góp tổ chức, không có bằng chứng hợp đồng thương mại cho khoảng trống này. Rào cản chính là người hưởng lợi không có ngân sách độc lập.

**C-O1-C5 — HYPOTHESIS.** AI có thể giúp ghép metadata nhiễu; rules/manifest là baseline mạnh. AI role useful, không load-bearing; legal risk medium do license và file phụ có thông tin cá nhân. Không để AI tự quyết file nào được công bố.

**C-O1-C6 — INFERENCE.** Chưa có một công nghệ chết cụ thể làm trung tâm, nên theme chỉ 1. Việc có tạp chí biến mất không làm mọi công cụ quản trị archive trở thành Resurrection. Artefact/mapping nhỏ có thể kiểm trong tuần, nhưng partner và dữ liệu đúng quyền chưa có, nên feasibility 3/L.

| Tiêu chí | Điểm/confidence | Evidence và nhãn |
|---|---|---|
| demand | 3/M | R01/R02/R04/R06; C-O1-C1 INFERENCE, không có yêu cầu mua mới |
| international | 3/M | R03/R04 NA, R07 EU; chưa có actor châu Á trực tiếp; C-O1-C1 INFERENCE |
| innovation | 1/M | C-O1-C2 INFERENCE: đối thủ đã làm preservation/routing/status |
| theme | 1/M | C-O1-C6 INFERENCE: thiếu dead-tech anchor |
| ai | 3/L | C-O1-C5 HYPOTHESIS; kỹ thuật reconciliation có ích, AI chưa đo |
| feasibility | 3/L | C-O1-C6 INFERENCE: cần giới hạn và artefact hợp pháp |
| demo | 3/L | C-O1-C3 HYPOTHESIS: kiểm before/after đầy đủ cần giải thích chuyên môn |
| sustainability | 3/L | C-O1-C4 UNKNOWN; loại tài trợ có tiền lệ, đường ngân sách riêng chưa rõ |

**Thử nghiệm bác bỏ nhỏ nhất:** với sự cho phép, chọn 3 tạp chí nhỏ có kế hoạch đóng/chuyển, lấy manifest và hồ sơ quyền; yêu cầu staff thử JASPER/PKP/Keepers với hỗ trợ sẵn có. Dừng hướng khác biệt mới nếu tất cả công việc bàn giao quan trọng đã hoàn tất trong một ngày mỗi tạp chí và không có sai lệch cần người nhận xử lý. Đo số artefact thiếu/không đọc được, thời gian và người chịu trách nhiệm; không dùng survey “có thích ý tưởng không”. Ngưỡng là thiết kế thí nghiệm C-O1-C3, chưa phải dữ liệu.

### C-O2 — Khả năng tiếp tục của đội revival trò chơi sau khi vendor và maintainer rời đi

**C-O2-C1 — VERIFIED.** Online Wii U/3DS đã dừng, trong khi một phần local vẫn hoạt động; Nintendo và Capcom xác nhận. Giá trị lịch sử là chơi cùng nhau/rank/content distribution, nên emulation máy cá nhân không tự thay toàn bộ trải nghiệm. R08/R09/R10. Target: đội duy trì server cộng đồng, nhóm người chơi tổ chức lịch chơi; dimensions software, community, operational, user-data-workflows.

**C-O2-C2 — INFERENCE.** Strongest alternative **Pretendo**, cùng nex-go và tài liệu contribution đã mở trực tiếp, chứng minh có nền móng kỹ thuật đáng kể. Homepage và donation FAQ chỉ snippet: có claims về clean-room, các game hỗ trợ, user account không thể tự chuyển, donations trả hosting/dev. Không dùng progress percentages hay thu nhập chưa xác nhận để tính market size. Phản chứng mạnh: những người có kỹ năng và nhu cầu đã tổ chức revival, làm server tổng quát khác có thể chỉ lặp công sức. R11/R12/R13/R14.

**C-O2-C3 — HYPOTHESIS.** Nhu cầu còn lại có thể là khả năng bàn giao vận hành cho maintainer kế tiếp mà không mất runbook, tương thích, moderation và lịch chơi; chưa có bằng chứng đội Pretendo muốn một giải pháp riêng. Why now dựa trên closure đã xác nhận và vận động ECI 2026, không suy ra người ký ECI cần công cụ kỹ thuật này. R13/R14/R15.

**C-O2-C4 — UNKNOWN.** Donation là tín hiệu hỗ trợ dự án theo snippet, không xác nhận doanh thu, mức đủ bù phí hoặc willingness to pay cho maintainer succession. Commercial viability: donor/hiệp hội người chơi có thể tài trợ; barrier là quy mô nhỏ, chi phí moderation và IP. Chưa có comparable audited spending.

**C-O2-C5 — HYPOTHESIS.** AI có thể giảm thời gian đọc log và tạo draft runbook, nhưng test traces deterministic và review maintainer là chuẩn. AI useful, không cần cho runtime. Không làm generic chatbot hoặc tái tạo dữ liệu người dùng bằng suy đoán.

**C-O2-C6 — INFERENCE.** Legal risk high và feasibility 1/L ở phạm vi continuity thật: chưa có console, trace, quyền hoặc nhóm đối tác trong tay. Một demo mô phỏng không chứng minh phục hồi game đã chết. Theme 5 vì Nintendo Network chết là trung tâm rõ ràng; điều này không bù rủi ro pháp lý và khác biệt thấp. R08/R09/R13/R14/R31.

| Tiêu chí | Điểm/confidence | Evidence và nhãn |
|---|---|---|
| demand | 3/M | C-O2-C1 VERIFIED, C-O2-C2 INFERENCE, ECI C-G-C19 VERIFIED; thiếu direct maintainer requests |
| international | 3/M | NA/Asia shutdown và EU hành vi chính sách; barriers pháp lý lớn, không đạt 5; R08–10/R15 |
| innovation | 1/M | C-O2-C2 INFERENCE: Pretendo đã đáp ứng revival core |
| theme | 5/H | C-O2-C1 VERIFIED: nền tảng cụ thể đã chấm dứt |
| ai | 3/L | C-O2-C5 HYPOTHESIS; có kỹ thuật protocol nhưng lợi ích AI chưa đo |
| feasibility | 1/L | C-O2-C6 INFERENCE: thiếu artefact, đối tác, quyền |
| demo | 3/L | C-O2-C3 HYPOTHESIS: continuity không rõ bằng gameplay, chưa có artefact demo |
| sustainability | 1/L | C-O2-C4 UNKNOWN/C-O2-C6 INFERENCE: donor chưa xác nhận và legal grey zone |

**Thử nghiệm bác bỏ nhỏ nhất:** đề nghị hai đội revival tự chọn một incident/bàn giao lịch sử; maintainer mới thử hoàn thành bằng runbook, repo và công cụ hiện có, ghi lỗi/quãng thời gian. Loại khoảng trống nếu không có lỗi quan trọng chưa được giải hoặc cả hai đội không coi bàn giao là việc đáng bỏ thời gian. Trước test chạy thực phải có quyền với artefact; không yêu cầu game/SDK bị leak. Đây là thí nghiệm nhu cầu C-O2-C3, không kế hoạch thiết kế server.

### C-O3 — Giữ ngữ nghĩa quyền và ngữ cảnh khi kho di sản đổi chủ hoặc nền tảng

**C-O3-C1 — INFERENCE.** Công việc cần giữ là người đúng quyền vẫn tìm/đọc/hiểu được collection sau chuyển đổi. Mukurtu migration có giới hạn cụ thể; Ranongga cho thấy nội dung có thể nhạy cảm về đất/genealogy. Target: archive staff, cultural protocol stewards và tổ chức giáo dục ngôn ngữ như Kulu. Dimensions knowledge, heritage, user-data-workflows, content. R17/R18/R22.

**C-O3-C2 — INFERENCE.** Strongest alternative **Mukurtu migration + Local Contexts + PARADISEC offline collections**. Phản chứng mạnh nhất: protocols, chuyển phiên bản, export labels và delivery ngoại tuyến đã tồn tại; ELDP/ELAR còn có tiền lệ chuyển tổ chức. Một “archive văn hóa mới” khó có lý do tồn tại chỉ nhờ AI hoặc đa ngôn ngữ. R17/R19/R21/R24/R25.

**C-O3-C3 — HYPOTHESIS.** Khoảng trống hẹp có thể là xác nhận semantics quyền/custom metadata vẫn giữ qua một lần chuyển cụ thể; không giả định tất cả migration làm lộ dữ liệu. Why now: tài liệu Mukurtu 4 và PARADISEC 2026 làm phương án thay thế kiểm được; nhu cầu phải được chứng minh ở collection đang chuyển, không dựa vào nguy cơ mất ngôn ngữ nói chung.

**C-O3-C4 — UNKNOWN.** Ai trả cho công việc xác nhận riêng chưa rõ. Commercial viability: đại học, quỹ di sản hoặc archive nhận có thể đưa vào grant; grant và bảng giá R20/R23/R24 chứng minh loại chi tiêu có thật, không chứng minh một startup có thể bán cross-platform assurance. Barrier: procurement, quyền cộng đồng, khối lượng nhỏ và lao động chuyên môn.

**C-O3-C5 — HYPOTHESIS.** AI useful cho gắn cờ mapping rủi ro và so mô tả; approval và access enforcement phải dựa trên quy tắc/người có thẩm quyền. Legal risk high do consent/cultural harm có thể không khôi phục được sau công bố. Không dùng summary AI thay tri thức gốc.

**C-O3-C6 — INFERENCE.** Theme 1: không có nền tảng cụ thể đã chết được chứng minh trong ca này; cơ quan văn hóa cũ ngừng hoạt động không tự là dead technology. Feasibility 3/L chỉ cho phép kiểm collection đã có quyền và mapping giới hạn; chưa có partner hoặc collection của họ trong tay. Tính cấp bách xã hội không tự nâng điểm Resurrection.

| Tiêu chí | Điểm/confidence | Evidence và nhãn |
|---|---|---|
| demand | 3/M | C-O3-C1 INFERENCE; R22 có hành vi thực nhưng không phải mua dịch vụ kiểm chuyển |
| international | 3/M | R24/R25 EU, R22 Oceania; chưa có demand Asia hoặc xác nhận địa lý người dùng Mukurtu cụ thể; C-O3-C1/C-O3-C2 INFERENCE |
| innovation | 3/L | C-O3-C3 HYPOTHESIS: custom semantics có thể hở, tool chính đã bao phủ nhiều phần |
| theme | 1/M | C-O3-C6 INFERENCE: thiếu anchor công nghệ chết |
| ai | 3/L | C-O3-C5 HYPOTHESIS: hỗ trợ review có baseline rules mạnh |
| feasibility | 3/L | C-O3-C6 INFERENCE: narrow scope và consent cần có |
| demo | 3/L | C-O3-C3 HYPOTHESIS: cần minh họa ai thấy gì, giải thích ngữ cảnh văn hóa |
| sustainability | 3/L | C-O3-C4 UNKNOWN; loại funding có tiền lệ C-G-C13 INFERENCE, nhu cầu riêng chưa đo |

**Thử nghiệm bác bỏ nhỏ nhất:** một archive đồng ý cung cấp 30 record đã được phép dùng, gồm record hạn chế và custom fields; so quy tắc quyền trước/sau bằng mapping chính thức, nhờ hai người có thẩm quyền đánh giá. Loại hướng nếu công cụ hiện có giữ đầy đủ mọi điều kiện quan trọng và không có lao động review đáng kể; dừng ngay test nếu không thống nhất người có quyền duyệt. Không cần xây app để thực hiện phép kiểm nhu cầu này.

## 11. Challenges to the mission hypothesis

1. “Nền tảng không sống được” chưa có nghĩa “giá trị phải sống dưới dạng nền tảng”: chuyển chủ trì hoặc collection offline có thể đủ, C-G-C12/C-G-C16.
2. “Bảo tồn” bao gồm jobs rất khác nhau: giữ chứng cứ, đọc lại file, duy trì multiplayer, duy trì người tham gia. Một phương án chung dễ lấy thành công ở content để hứa quá mức ở community, C-G-C9/C-G-C11/C-G-C23.
3. Nhu cầu xã hội và thị trường cho người cung cấp mới là hai mệnh đề khác nhau. ECI, grant và tình nguyện không xác nhận một dòng doanh thu mới, C-G-C13/C-G-C19 và C-O1/2/3-C4.
4. Cứu một nền tảng bằng việc tạo một nền tảng phụ thuộc khác có thể tái tạo điểm chết ban đầu. Phải kiểm được bàn giao tiếp theo, C-G-C2/C-G-C10/C-O2-C3.
5. Quyền được quên, quyền cộng đồng và giới hạn tái phát hành có thể làm một “thành công sao chép” thành thất bại bảo tồn có trách nhiệm, C-G-C14/C-G-C17/C-G-C20/C-G-C21.
6. Chưa có bằng chứng AI là phần bắt buộc. Không thêm AI để cứu khoảng trống bị đối thủ bao phủ hoặc để bù thiếu dead-tech anchor, C-G-C22/C-O1-C6/C-O3-C6.

**C-G-C24 — VERIFIED.** Kiroween live rules đã mở và đối chiếu với snapshot coordinator: phải có working software application dùng Kiro, Resurrection gắn công nghệ chết, deadline 04-12-2026 14:00 PST. Đây là kiểm tra lặp lại nội dung văn bản, không phải tư vấn eligibility hay dự đoán giải. Rubric nghiên cứu 8 tiêu chí khác rubric official 5 tiêu chí; không dùng điểm potential để tuyên bố sản phẩm đủ điều kiện. [R34](https://kiroween.devpost.com/rules).

## 12. Unresolved questions

**C-G-C23 — UNKNOWN.** Chưa biết chi phí vận hành đầy đủ, willingness to pay, willingness to maintain, tỷ lệ retention cộng đồng, hoặc quyền chuyển asset cho một ca đóng nền tảng cụ thể. Không suy các biến này từ lượng tài liệu tìm được.

Ưu tiên kiểm tra tiếp theo, không phải hành động đã thực hiện:

- Với C-O1: chọn tạp chí thật đang chuyển/đóng và kiểm đầy đủ bằng công cụ hiện có. Xác nhận mọi artifact quan trọng trước khi gán novelty.
- Với C-O2: tìm nhu cầu maintainer độc lập với tiếng nói vận động người chơi; kiểm tài chính/khả năng bàn giao và quyền trước gameplay.
- Với C-O3: có người giữ thẩm quyền cộng đồng và ca migration thật, xác nhận có lỗi semantics mà công cụ hiện có chưa giải được.
- Mở final rules/exemption hiện hành và bản triển khai quốc gia cần thiết; không vận hành dịch vụ dựa trên C-G-C20/C-G-C21.
- Lấp bằng chứng châu Á cho hành vi cộng đồng và funding; không gọi Oceania là Asia.

AI Engineering lessons quan sát được: brief + anchors + rules đủ để giữ độc lập mà không xem thứ hạng cũ; sơ cấp bị bot block buộc hạ nhãn thay vì suy snippet thành fact; nguồn cạnh tranh hiện tại có thể làm giảm novelty rõ rệt. Chưa có kết quả cross-review, chưa đo evaluator disagreement, token usage hoặc hiệu quả effort escalation. Prompt-only isolation là quy tắc tự tuân thủ của worker; không thể dùng việc tôi không thấy peer folders làm bằng chứng OS đã chặn truy cập. Không cập nhật progress chung vì brief mới giới hạn mọi ghi vào agent-c/.

Quyết định cần human/coordinator approval ở vòng sau: tiếp cận người thật/collection hạn chế, điều kiện dùng dữ liệu và cấp quyền, chi phí thử nghiệm hoặc bất kỳ triển khai nào. Không có quyết định cần duyệt để kết thúc desk research này; không chọn finalist.

## 13. References

Tất cả truy cập **2026-11-25 UTC**. `direct` = đã mở và đọc nội dung; `snippet` = chỉ kết quả tìm kiếm dù đã thử mở thất bại. Scores theo thứ tự **A/T/M/C/F/R/B** = Authority/Technical evidence/Mechanism/Context/Freshness/Reproducibility/low Bias, mỗi tiêu chí 0–5; weighted = tổng trọng số 20/20/20/15/10/10/5, quy đổi 100. SR = Source Reliability 0–5; RR = Reference Relevance 0–5 với **claim cụ thể** ở cột claims. SR cao không nâng cấp một claim snippet. Các điểm là đánh giá của researcher, không phải số liệu nguồn.

| Ref ID | URL | Title | Publisher | Pub date | Accessed | Mode | Claims chính | 7 scores | Weighted | SR | RR |
|---|---|---|---|---|---|---|---|---|---:|---:|---:|
| R01 | https://arxiv.org/abs/2008.11933 | Open is not forever | Laakso/Matthias/Jahn, arXiv; published version | 2021-02-22 revision | 2026-11-25 | direct | C-G-C1; C-O1-C1 | 5/4/4/5/2/4/5 | 84 | 4.5 | 5 |
| R02 | https://microblogging.infodocs.eu/wp-content/uploads/2024/01/jlsc-16288-eve.pdf | Digital Scholarly Journals Are Poorly Preserved | Martin Paul Eve/JLSC, PDF mirror | 2024-01 | 2026-11-25 | direct | C-G-C1; C-O1-C1/C3 | 5/5/4/5/3/4/4 | 89 | 4.5 | 5 |
| R03 | https://github.com/pkp/pkp-docs/blob/main/pkp-pn/en/index.md | PKP Preservation Network | PKP official docs source | n.d., current branch | 2026-11-25 | direct | C-G-C5/C6; C-O1-C2 | 5/4/5/5/4/4/4 | 91 | 4.5 | 5 |
| R04 | https://texasdigitallibrary.atlassian.net/wiki/spaces/OAJ/pages/1762295809 | PKP Preservation Network | Texas Digital Library | 2024-01-11 | 2026-11-25 | direct | C-G-C5; C-O1-C1 | 5/4/5/5/3/4/5 | 90 | 4.5 | 5 |
| R05 | https://doaj.org/preservation/ | JASPER preservation service | DOAJ | n.d. | 2026-11-25 | direct | C-G-C7; C-O1-C2 | 5/4/5/5/4/4/4 | 91 | 4.5 | 5 |
| R06 | https://infrafinder.investinopen.org/solutions/pkp-preservation-network | PKP Preservation Network | Invest in Open Infrastructure; provider profile | updated 2025-09-19 | 2026-11-25 | direct | C-G-C8 | 4/3/4/5/4/3/4 | 77 | 3.5 | 5 |
| R07 | https://www.issn.org/wp-content/uploads/2025/01/PLAN-2025-%E2%80%93-2029-ISSN-INTERNATIONAL-CENTRE_compressed-2.pdf | Action Plan 2025–2029, pp.10–11 | ISSN International Centre | 2025-01 | 2026-11-25 | direct | C-O1-C2/C3 | 5/3/4/5/4/4/4 | 83 | 4.5 | 5 |
| R08 | https://en-americas-support.nintendo.com/app/answers/detail/a_id/57847 | Wii U & Nintendo 3DS eShop Discontinuation Q&A | Nintendo | n.d., updated after 2024-04 | 2026-11-25 | direct | C-G-C2/C18; C-O2-C1 | 5/4/5/5/4/5/3 | 92 | 4.5 | 5 |
| R09 | https://www.capcom-support.com/hc/en-us/articles/11752429426204-Discontinuation-of-Online-Services-for-Nintendo-3DS-and-Wii-U-Software | Discontinuation of Online Services | Capcom | updated 2026-07-22 | 2026-11-25 | direct | C-G-C3/C18; C-O2-C1 | 5/4/5/5/5/5/4 | 95 | 4.5 | 5 |
| R10 | https://support.nintendo.com/jp/information/2023/1004.html | ニンテンドー3DS…オンラインプレイサービス終了 | Nintendo Japan | 2023-10-04; updated 2024-04-09 | 2026-11-25 | direct | C-G-C18; C-O2-C1 | 5/4/5/5/3/5/3 | 90 | 4.5 | 5 |
| R11 | https://pretendo.network/ | Pretendo Network homepage/FAQ | Pretendo | n.d. | 2026-11-25 | snippet; direct 403 | C-O2-C2 | 4/2/3/5/3/1/3 | 62 | 3 | 5 |
| R12 | https://forum.pretendo.network/t/donation-subscription-faq/4955 | Donation Subscription FAQ | Pretendo forum contributor, quotes server guide | 2024-08-28 | 2026-11-25 | snippet; restricted | C-O2-C2/C4 | 3/1/3/5/2/1/3 | 52 | 2.5 | 4 |
| R13 | https://github.com/PretendoNetwork/.github/blob/master/.github/CONTRIBUTING.md | How to contribute | Pretendo official repository | n.d., current branch | 2026-11-25 | direct | C-O2-C2/C3/C6 | 4/4/4/5/4/4/4 | 83 | 4 | 5 |
| R14 | https://github.com/PretendoNetwork/nex-go | Barebones PRUDP/NEX server library | Pretendo official repository | n.d., current branch | 2026-11-25 | direct | C-O2-C2/C6 | 4/5/5/5/4/5/4 | 93 | 4 | 5 |
| R15 | https://citizens-initiative.europa.eu/news/14th-valid-initiative-stop-destroying-videogames-submitted-commission-examination-2026-01-26_en | 14th valid initiative submitted | European Commission | 2026-01-26 | 2026-11-25 | direct | C-G-C19; C-O2-C3 | 5/4/5/4/5/5/5 | 93 | 5 | 4 |
| R16 | https://www.heise.de/en/news/Citizens-initiative-1-294-188-signatures-for-Stop-Destroying-Videogames-11154579.html | Citizens' initiative: 1,294,188 signatures | Heise, Daniel Herbig | 2026-01-26 | 2026-11-25 | direct | C-G-C19 | 4/3/4/5/5/4/4 | 81 | 4 | 5 |
| R17 | https://docs.mukurtu.org/migration/PM02Activities/ | Mukurtu 3 Pre-Migration Activities | Mukurtu official manual | n.d. | 2026-11-25 | direct | C-G-C15; C-O3-C1/C2 | 5/5/5/5/4/4/4 | 95 | 4.5 | 5 |
| R18 | https://docs.mukurtu.org/media/ManageMediaAccessWithProtocols/ | Manage Media Access with Cultural Protocols | Mukurtu official manual | n.d. | 2026-11-25 | direct | C-G-C14; C-O3-C1 | 5/4/5/5/4/4/4 | 91 | 4.5 | 5 |
| R19 | https://localcontexts.org/support/working-with-labels/ | Working with Labels in the Hub | Local Contexts | n.d. | 2026-11-25 | direct | C-G-C14; C-O3-C2 | 5/4/5/5/4/4/4 | 91 | 4.5 | 5 |
| R20 | https://www.paradisec.org.au/about-us/funding/ | Funding | PARADISEC | n.d., includes 2024–2028 grants | 2026-11-25 | direct | C-G-C13; C-O3-C4 | 5/3/4/5/4/3/4 | 81 | 4 | 5 |
| R21 | https://www.paradisec.org.au/blog/2026/03/offline-static-collections/ | Offline static collections | PARADISEC, Nick Thieberger | 2026-03-02; displays update 2026-08-26 | 2026-11-25 | direct | C-G-C16; C-O3-C2 | 5/4/5/5/5/4/4 | 93 | 4 | 5 |
| R22 | https://www.paradisec.org.au/blog/2024/02/using-raspberry-pi-in-ranongga/ | Using Raspberry Pi in Ranongga | PARADISEC, guest Debra McDougall | 2024-02-13 | 2026-11-25 | direct | C-G-C17; C-O3-C1 | 4/4/5/5/3/3/4 | 83 | 4 | 5 |
| R23 | https://www.paradisec.org.au/deposit/costing-a-deposit/ | Costing a deposit | PARADISEC | n.d.; historical policy from 2014 mentioned | 2026-11-25 | direct | C-G-C13; C-O3-C4 | 5/3/4/5/2/3/4 | 77 | 4 | 5 |
| R24 | https://www.bbaw.de/files-bbaw/presse/pressemitteilungen/pressemitteilungen-2021/PM-18_Dokumentation_bedrohter_Sprachen_englisch/BBAW_PM_ELDP_engl.pdf | New Berlin Center for Documentation of Endangered Languages | BBAW | 2021-07-19 | 2026-11-25 | direct | C-G-C12/C13; C-O3-C2 | 5/3/5/5/2/4/4 | 83 | 4.5 | 5 |
| R25 | https://www.soas.ac.uk/about/news/soas-marks-eldp-move-new-base-berlin | SOAS marks ELDP move to new base in Berlin | SOAS | 2021-07-01/02 displayed | 2026-11-25 | direct | C-G-C12; C-O3-C2 | 5/3/5/5/2/4/4 | 83 | 4.5 | 5 |
| R26 | https://docs.ipfs.tech/how-to/pin-files/ | Pin files | IPFS official docs | n.d. | 2026-11-25 | direct | C-G-C10 | 5/5/5/5/4/5/4 | 97 | 4.5 | 5 |
| R27 | https://help.archive.org/help/using-the-wayback-machine/ | Using the Wayback Machine | Internet Archive | n.d. | 2026-11-25 | direct | C-G-C9 | 5/4/5/5/3/4/4 | 89 | 4.5 | 5 |
| R28 | https://www.softwarepreservationnetwork.org/emulation-as-a-service-infrastructure/participants/ | EaaSI Participants | Software Preservation Network | n.d., early-service wording | 2026-11-25 | direct | C-G-C11 | 5/3/4/5/1/3/4 | 75 | 4 | 4 |
| R29 | https://www.softwarepreservationnetwork.org/eaasi-software-development-update/ | EaaSI Software Development Update | SPN, Klaus Rechert | 2019-03-29 | 2026-11-25 | direct | C-G-C11 | 5/5/5/5/1/4/4 | 89 | 4 | 5 |
| R30 | https://www.unesco.org/en/legal-affairs/charter-preservation-digital-heritage | Charter on Preservation of Digital Heritage, Arts.3/5/7 | UNESCO | 2003-10-15 | 2026-11-25 | direct | C-G-C2/C4 | 5/2/4/5/1/4/5 | 74 | 5 | 4 |
| R31 | https://www.copyright.gov/1201/2024/2024_Section_1201_Registers_Recommendation.pdf | Ninth Triennial Proceeding Recommendation, pp.163–195, Appendix | US Copyright Office | 2024-10-18 | 2026-11-25 | direct | C-G-C21; C-O2-C6 | 5/5/5/4/3/5/5 | 93 | 5 | 3 |
| R32 | https://eur-lex.europa.eu/eli/reg/2016/679 | GDPR Article 20 | EU Official Journal | 2016; current status not checked | 2026-11-25 | snippet; direct bot gate | C-G-C20 | 5/2/3/5/2/1/5 | 66 | 5 | 4 |
| R33 | https://regelex.com/legislation/32019L0790/art_6?as=adopted&on=2026-11-10 | Directive 2019/790 Article 6 transcription | Regelex; EUR-Lex origin blocked | 2019 text, secondary page date 2026-11-10 | 2026-11-25 | snippet | C-G-C20 | 3/2/3/5/2/1/3 | 56 | 2.5 | 4 |
| R34 | https://kiroween.devpost.com/rules | Kiroween 2026 Official Rules | AWS/Devpost | updated 2026-11-16 | 2026-11-25 | direct + local snapshot comparison | C-G-C24 | 5/4/5/5/5/5/4 | 95 | 5 | 5 |

Lưu ý chất lượng: R06 là hồ sơ provider, R11/R12 snippet không thể xác nhận finances/gameplay; R15/R16 đối chứng số chữ ký nhưng không tạo bằng chứng mua hàng; R24/R25 có lợi ích truyền thông và không chứng minh toàn bộ migration kỹ thuật đã hoàn tất; R31 là recommendation lịch sử, không final legal clearance. Các claim quan trọng cho thứ hạng cơ hội vẫn có uncertainty được giữ nguyên thay vì cưỡng ép đồng thuận.
