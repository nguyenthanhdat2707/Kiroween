# CodeProject: vì sao công ty đóng, giá trị nào mất, và các ngách có thể hồi sinh

Ngày nghiên cứu và truy cập nguồn: **24/11/2026 (Việt Nam)**. Đây là nghiên cứu để chọn ý tưởng Kiroween, **không phải kế hoạch xây hoặc tuyên bố sở hữu CodeProject**. Nhãn dùng trong tài liệu: **ĐÃ XÁC MINH** = nguồn trực tiếp/quan sát kiểm được; **SUY LUẬN** = giải thích hợp lý từ chứng cứ nhưng chưa có đo lường nhân quả; **GIẢ THUYẾT** = đề xuất cần thử; **CHƯA RÕ** = chưa đủ dữ liệu. Những con số tài khoản đăng ký là tích lũy, không phải người dùng hoạt động năm 2026.

## 1. CodeProject vốn giải quyết việc gì?

**ĐÃ XÁC MINH:** CodeProject ra đời để lập trình viên chia sẻ bài hướng dẫn dài, giải thích quyết định thiết kế và đính kèm mã nguồn, thay vì chỉ đưa một câu trả lời ngắn. Bản lưu trang của hãng tháng 10/2024 ghi **65.938 bài**; [thông cáo của chính CodeProject năm 2013](https://www.prnewswire.com/news-releases/codeproject-celebrates-ten-million-members-218836081.html) ghi 10 triệu tài khoản đăng ký; [người đồng sáng lập Chris Maunder](https://chrismaunder.com/) tự ghi 16 triệu thành viên và khoảng 65.000 bài trong vòng đời. Các số không chứng minh lượng độc giả/đóng góp còn hoạt động ngay trước lúc đóng. Nguồn: [bản lưu thông báo chính thức 22/10/2024](https://web.archive.org/web/20241022172524/https://www.codeproject.com/info/Changes.aspx), [hồ sơ của Chris Maunder](https://chrismaunder.com/).

**ĐÃ XÁC MINH:** Bài viết, mã tải về, bình luận và hỏi đáp là nhiều lớp của cùng một đơn vị tri thức. Trong [bài tự mô tả lần thiết kế lại](https://github.com/ChrisMaunder/Redesigning-CodeProject), Chris coi bài viết là phần cốt lõi; ông cũng ghi nhận site từng bị phàn nàn là cũ, chật và khó tập trung vào nội dung, đồng thời đội ngũ phải cắt bớt những tính năng ít dùng để giảm công bảo trì. Đây là bằng chứng về **vấn đề trải nghiệm và chi phí bảo trì đã được nhận thấy**, không phải bằng chứng chúng gây ra phá sản năm 2024.

**Giá trị lịch sử cần phân biệt:** (a) lưu bài cũ; (b) biết chính xác mã chạy trong điều kiện nào; (c) học *vì sao* tác giả chọn cách làm; (d) đọc phần sửa lỗi/ngoại lệ do cộng đồng phát hiện. Bản lưu tĩnh có thể giữ (a) nhưng không mặc nhiên giữ (b)–(d). Đây là **SUY LUẬN sản phẩm**, chưa có phỏng vấn định lượng với người từng dùng.

## 2. Chuỗi sự kiện: “đóng công ty” khác “mất website”

| Mốc | Sự kiện và mức chứng cứ | Điều không nên suy ra |
|---|---|---|
| **2013** | **ĐÃ XÁC MINH:** CodeProject tự công bố đạt 10 triệu tài khoản đăng ký. [Thông cáo 08/08/2013](https://www.prnewswire.com/news-releases/codeproject-celebrates-ten-million-members-218836081.html). | Không phải 10 triệu người dùng hoạt động hằng tháng. |
| **10/2024** | **ĐÃ XÁC MINH:** Chris Maunder và David Cunningham thông báo **CodeProject Solutions Inc. đóng sau gần hai năm thua lỗ đáng kể**; dự định chuyển website sang chế độ chỉ đọc và ngừng đăng bài, diễn đàn, QuickAnswers. [Thông báo chính thức, bản lưu 22/10/2024](https://web.archive.org/web/20241022172524/https://www.codeproject.com/info/Changes.aspx). | Chưa có báo cáo tài chính công khai trong nghiên cứu này để tách tỷ trọng từng khoản lỗ. “Chỉ đọc” không đồng nghĩa toàn bộ bài bị xóa. |
| **11/2024** | **ĐÃ XÁC MINH:** thông báo trên chính trang đổi thành “có nhà mới”: D2 Emerge tiếp quản, hứa thiết kế lại và đưa nội dung trở lại; mời cộng đồng sang Discord trong thời gian chờ. [Thông báo 26/11/2024](https://web.archive.org/web/20241126124743/https://www.codeproject.com/info/Changes.aspx). [Đồng sáng lập D2 Emerge](https://www.linkedin.com/posts/rubinsteindavid_d2-emerge-acquires-codeproject-expanding-activity-7262171470087294976-BXnL) cũng công bố mua tài sản. | Lời hứa phục hồi không chứng minh việc di chuyển bài, mã tải về, tài khoản và thảo luận đã hoàn tất. |
| **03–11/2026** | **ĐÃ XÁC MINH ở mức nguồn cá nhân và quan sát giới hạn:** [tác giả Eric Woodruff](https://ewoodruff.us/CodeProject.aspx) và [tác giả Ring](https://groups.google.com/g/ring-lang/c/5r6-ejzuqPY/m/i3a1Ac41BQAJ) nói trang ngừng hoạt động khoảng 03/2026. Kiểm tra từ môi trường này ngày **24/11/2026**: `https://www.codeproject.com/` trả HTML chuyển tới `/lander`; `/lander` chứa mã `parking-lander` của GoDaddy. | Không kết luận mọi bản sao, file đính kèm hoặc quyền sở hữu domain đã biến mất vĩnh viễn; kết quả truy cập có thể thay đổi theo nơi/thời điểm. HTTP 200 ở trang gốc **không có nghĩa bài viết đang hoạt động**. |

**Kết luận trạng thái:** công ty vận hành cũ đã đóng là sự kiện có nguồn chính thức. Tài sản từng được mua và có kế hoạch phục hồi. Tại thời điểm kiểm tra này, domain chính không phục vụ kho bài qua đường thông thường từ môi trường nghiên cứu. “CodeProject sập” vì vậy nên được diễn đạt thành **mất vận hành cộng đồng và khả năng truy cập ổn định**, không thành “toàn bộ tri thức đã bị xóa”.

## 3. Nguyên nhân chính và các tầng nguyên nhân chưa được chứng minh

### 3.1 Nguyên nhân trực tiếp: mô hình vận hành hết tiền

**ĐÃ XÁC MINH theo chính nhóm sáng lập:** họ nêu “tech recession” tác động mạnh tới **khách hàng của CodeProject**, kéo theo gần hai năm thua lỗ, dù đã bổ sung tiền để duy trì. Đây là **lý do chính thức và mạnh nhất** cho quyết định đóng CodeProject Solutions Inc.; nguồn là [thông báo 2024](https://web.archive.org/web/20241022172524/https://www.codeproject.com/info/Changes.aspx). Không có căn cứ để nói “AI giết CodeProject”, “chất lượng bài giảm gây đóng cửa”, hoặc “Stack Overflow lấy hết người dùng” như một nguyên nhân đã được xác nhận.

**ĐÃ XÁC MINH về cơ chế kinh doanh lịch sử:** [bộ tài liệu bán hàng của DeveloperMedia năm 2017](https://developermedia.com/wp-content/uploads/2017/11/Developer-Media-Advertising-Programs-Overview-2017.pdf) chào bán quảng cáo hiển thị, newsletter, lead generation, Product Showcase và tài trợ chuyên mục trên CodeProject. **SUY LUẬN:** nếu khách hàng công nghệ giảm chi marketing, dòng tiền gắn với tiếp thị developer sẽ dễ tổn thương. Ta **chưa biết** tỷ trọng doanh thu CodeProject từ các kênh đó năm 2023–24, hợp đồng cụ thể, hay mức suy giảm traffic, nên không viết “quảng cáo giảm X%” hoặc “SEO sập” khi chưa có số.

### 3.2 Vì sao mất khả năng vận hành làm trải nghiệm tiếp tục yếu đi?

**ĐÃ XÁC MINH:** chuyển sang chỉ đọc chặn bài mới, câu hỏi và trả lời mới; D2 Emerge nói sẽ khôi phục sau thiết kế lại và chuyển cộng đồng tạm sang Discord ([thông báo 10/2024](https://web.archive.org/web/20241022172524/https://www.codeproject.com/info/Changes.aspx), [thông báo 11/2024](https://web.archive.org/web/20241126124743/https://www.codeproject.com/info/Changes.aspx)). **SUY LUẬN:** khi không thể sửa bài, xác nhận bản mới hay hỏi tiếp tác giả, kho hướng dẫn cũ dần thành tài liệu có tuổi nhưng thiếu cơ chế cập nhật. Discord có thể duy trì trò chuyện, nhưng không tự gắn sửa lỗi trở lại đúng bài và đúng phiên bản mã. Không có dữ liệu đủ để đo mức mất cộng đồng sau 2024.

### 3.3 Sức ép sản phẩm tồn tại, nhưng không thể nhận là nguyên nhân đóng cửa

- **ĐÃ XÁC MINH:** Chris từng ghi nhận thiết kế cũ chật, gây nhiễu và khó bảo trì ([repo thiết kế lại](https://github.com/ChrisMaunder/Redesigning-CodeProject)). **CHƯA RÕ:** ảnh hưởng đến giữ chân độc giả/doanh thu thời điểm đóng.
- **ĐÃ XÁC MINH:** [GitHub Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site) giúp tác giả tự xuất bản; [Copilot upgrade](https://learn.microsoft.com/en-us/dotnet/core/porting/github-copilot-app-modernization/overview) đã xử lý nhiều tác vụ nâng cấp .NET. **SUY LUẬN:** một nền tảng hướng dẫn cũ phải mang lại nhiều hơn lưu bài hoặc tạo bản vá. Đây là đối thủ của **ý tưởng hồi sinh**, không phải bằng chứng về nguyên nhân tài chính 2024.
- **CHƯA RÕ:** traffic theo năm, số người viết mới, doanh thu, nguyên nhân lần offline 2026, tình trạng đầy đủ của kho dữ liệu D2 Emerge nhận. Không khẳng định site chết do lỗi kỹ thuật cụ thể khi chưa có công bố của chủ sở hữu.

## 4. Cái gì thực sự mất và ai còn cần nó?

| Giá trị cũ | Mất mát có thể kiểm chứng | Người có thể cần hôm nay — GIẢ THUYẾT |
|---|---|---|
| Bài dài giải thích quyết định, mã kèm theo | URL gốc hiện không dẫn tới nội dung từ môi trường kiểm tra; tác giả phải [tự host lại bài của mình](https://ewoodruff.us/CodeProject.aspx). | Tác giả muốn giữ hồ sơ công trình; developer bảo trì cần hiểu ý định ban đầu. |
| Mã gắn với điều kiện môi trường | Bài cũ có thể nói Visual Studio/.NET/Windows đời trước; bản lưu không tự xác nhận mã còn chạy. | Người bảo trì hệ thống legacy cần biết *chạy được ở phiên bản nào*, không chỉ có code. |
| Bình luận, errata, lời giải bổ sung | Khi chỉ đọc/offline, không thể duy trì một bản kết luận hiện hành trên đúng trang. Mức dữ liệu bình luận còn truy xuất được **CHƯA RÕ**. | Người đọc đang tìm lỗi hoặc trường hợp biên mà bài gốc bỏ sót. |
| Ghi nhận người viết và đóng góp bảo trì | Trang gốc không còn là hồ sơ đóng góp dễ truy cập. | Tác giả/chuyên gia muốn giữ attribution; tổ chức muốn biết ai xác nhận bài. |

**Bài toán nền tảng:** hồi sinh **cơ chế bài giải thích + source + kiểm chứng + sửa sai có xuất xứ**, thay vì tạo bản sao giao diện CodeProject. Một tính năng hồi sinh nên giải đúng một tác vụ của một nhóm người, dùng dữ liệu được phép, và sinh kết quả hữu ích ngay cả khi CodeProject.com chưa trở lại.

## 5. Bốn ngách sản phẩm, từ dễ kiểm chứng đến khó

### A. Author Rescue Kit — tác giả tự phục hồi bài và dấu vết

**Người dùng:** tác giả có bài CodeProject của chính mình. **Việc cần làm:** nối bài tự lưu, repo gốc, ảnh/download còn lại và đường dẫn cũ thành một trang có xuất xứ và redirect map để người đọc vẫn tìm được. [Eric Woodruff](https://ewoodruff.us/CodeProject.aspx) là bằng chứng có **một tác giả thực sự đã tự làm việc này**; chưa biết nhiều tác giả khác muốn dùng công cụ.

**MVP:** một tác giả nhập 3 URL bài cũ và repo họ kiểm soát → kiểm quyền → tạo catalog các bản do họ cho phép đăng lại, chỉ rõ file thiếu, link hỏng, phiên bản gốc. **Khác biệt cần có:** phục hồi link và xuất xứ trên nhiều bản, không chỉ publish Markdown. **Đối chứng mạnh:** GitHub Pages và Wayback đã giải nhiều phần lưu trữ. **Rủi ro:** nhu cầu có thể chỉ là tác vụ một lần; sản phẩm dễ thành công cụ chuyển bài nhỏ, yếu ở Innovation/Presentation. **Resurrection:** khá rõ về tri thức mất đường truy cập, nhưng ít “công nghệ cũ được tái tưởng tượng” nếu chỉ là catalog.

### B. Living Legacy Lab — kiểm chứng một khẳng định/hành vi của mã cũ

**Người dùng:** developer bảo trì hoặc chuyển hệ thống cũ, gặp một bài có mã nhưng không biết điều kiện hoạt động. **Việc cần làm:** từ câu “control này giữ trạng thái sau postback” tạo một *hợp đồng hành vi* do người duyệt, chạy trên app cũ và bản sửa mới, lưu trace/log và trạng thái **đạt / sai / chưa xác minh**. [Phân tích hẹp ở chu kỳ 24](../validation/living-legacy-lab-niche-2026-11-23.md) đề xuất thử **Web Forms/ViewState/control tạo động** vì [Microsoft giải thích rủi ro vòng đời control](https://learn.microsoft.com/en-us/previous-versions/aspnet/hbdfdyh7%28v%3Dvs.100%29).

**MVP:** đúng một bài có quyền, một trang, một chuỗi 2–3 tương tác, một sai khác có bằng chứng. **Đối chứng mạnh:** [Copilot upgrade](https://learn.microsoft.com/en-us/dotnet/core/porting/github-copilot-app-modernization/overview) và [Playwright trace](https://playwright.dev/docs/trace-viewer); “AI nâng cấp .NET” hoặc “record test” không đủ khác biệt. **Điểm khác biệt cần thắng:** lấy *điều kiện ngầm trong bài cũ* và báo sai khác hành vi mà build/test sẵn có bỏ qua. **Rủi ro:** cần app cũ chạy được, thường cần Windows/IIS; người dùng và baseline chưa xác nhận. **Resurrection:** gắn với bài/phiên bản cũ, không tuyên bố Web Forms nói chung đã chết.

### C. Errata Ledger — biến sửa lỗi trong bài và thảo luận thành hồ sơ có chứng cứ

**Người dùng:** người đọc bài cũ hoặc tác giả đang sửa lại hướng dẫn. **Việc cần làm:** biết phần nào của bài gốc còn đúng, phần nào bị bình luận/sửa đổi sau đó bác bỏ, và mỗi kết luận áp dụng cho phiên bản nào. AI chỉ **đề xuất claim**, người am hiểu chốt và gắn nguồn; ghi cả tranh chấp hoặc chưa rõ. **MVP:** 3 bài có tác giả cho phép, mỗi bài 1–2 claim, link tới nguồn/commit/issue; không copy toàn văn thảo luận nếu không có quyền. **Đối chứng:** GitHub issues/wiki, comment thread hiện có, coding agent với RAG. **Điểm khác biệt cần thắng:** cấu trúc *claim → điều kiện phiên bản → chứng cứ phản ví dụ → người xác nhận*, khiến người đọc quyết định được có nên áp dụng mã. **Rủi ro:** nếu bình luận/archive thiếu hoặc không có chuyên gia, AI dễ suy diễn và ngách này thất bại. **Resurrection:** hồi sinh quá trình sửa sai cộng đồng, nhưng quyền bình luận và dữ liệu là cổng chặn.

### D. Living Article for maintainers — bài kỹ thuật mới tự gắn mã và tình trạng chạy

**Người dùng:** tác giả chuyên về hệ thống legacy muốn xuất bản hướng dẫn còn bảo trì được. **Việc cần làm:** viết một bài có repo/commit, phiên bản hỗ trợ, phép thử tái chạy và phần thay đổi; mỗi lần dependency đổi, trạng thái bài được cập nhật bằng bằng chứng. **MVP:** 1 tác giả, 1 bài họ sở hữu, 1 test chạy tự động, 1 thay đổi phiên bản dẫn tới cập nhật claim. **Đối chứng:** README + GitHub Actions + tài liệu hãng; không thể chỉ bọc chúng bằng UI. **Điểm khác biệt cần thắng:** làm việc cập nhật *phần giải thích* và công nhận công người bảo trì dễ hơn. **Rủi ro:** bài mới không cứu trực tiếp kho CodeProject; cần thuyết phục tác giả đóng góp lâu dài. **Resurrection:** định dạng bài dài có source và thảo luận được đưa vào workflow hiện đại, phù hợp chủ đề nếu trình bày lịch sử rõ.

### Hướng loại: clone CodeProject hoặc “AI migrate mọi bài .NET”

**Loại bản chung.** [CPOL 1.02](https://spdx.org/licenses/CPOL-1.02.html) cho quyền rộng hơn với mã nhưng **không tự cho đăng lại bài viết**; mỗi bài/mã có thể dùng license khác nhau. Mua/khôi phục domain và dữ liệu gốc thuộc quyền chủ sở hữu hiện tại, không nằm trong phạm vi một dự án nhỏ. [Copilot upgrade](https://learn.microsoft.com/en-us/dotnet/core/porting/github-copilot-app-modernization/overview) đã hỗ trợ Web Forms/WinForms và test; làm một agent nâng cấp chung không có lõi mới đủ rõ.

## 6. So sánh để chọn ngách đầu tiên

Các cột là **phán đoán nghiên cứu, không phải điểm giám khảo**. “Khả thi” giả định demo trước hạn Kiroween; “khác biệt” chỉ đạt nếu thắng đối chứng được ghi ở trên.

| Ngách | Quyền và đầu vào | Bằng chứng vấn đề | Khác biệt có thể bảo vệ | Khả thi demo | Quyết định |
|---|---|---|---|---|---|
| **A. Author Rescue Kit** | Dễ nhất nếu tác giả tự cấp quyền | Có một ca tác giả tự cứu bài | Yếu–trung bình; GitHub Pages/Wayback mạnh | Cao | **Dự phòng nếu không có app legacy chạy được** |
| **B. Living Legacy Lab** | Cần bài/code được phép và môi trường chạy | Rủi ro kỹ thuật có nguồn; nhu cầu trả công chưa rõ | Trung bình nếu chứng minh lỗi hành vi bị bỏ qua | Trung bình–thấp | **Ưu tiên phép thử kỹ thuật**, chưa ưu tiên xây |
| **C. Errata Ledger** | Khó vì bình luận, quyền, người xác nhận | Có vấn đề logic; dữ liệu hiện có chưa kiểm | Có thể cao nếu claim có chứng cứ thật | Thấp | **Giữ để khảo sát**, chưa làm demo chính |
| **D. Living Article** | Dễ với bài mới của tác giả | Nhu cầu bảo trì bài chưa đo | Trung bình; README+CI mạnh | Trung bình | **Thử nếu có tác giả hợp tác** |

**Lựa chọn hiện tại — SUY LUẬN:** thử **B** trước vì một phép thử thật có thể trả lời nhanh “có giá trị vượt Copilot + Playwright không?”. Nếu thiếu Windows/app cũ hoặc không có sai khác hành vi thật, chuyển sang **A** với tác giả cho phép; không cố cứu B bằng lời hứa AI. **C** có tiềm năng cộng đồng hơn nhưng cần dữ liệu và người thẩm định mà nghiên cứu hiện chưa có. Chưa ngách nào qua cổng **PROMISING**.

## 7. Điều kiện để nói “hồi sinh” một cách trung thực

1. **Quyền:** chỉ đưa bài/ảnh/code vào app hoặc repo khi tác giả/license cho phép; với CPOL, không coi quyền dùng code là quyền đăng lại bài. Chỉ liên kết hoặc mô tả metadata khi quyền nội dung chưa rõ. [CPOL 1.02](https://spdx.org/licenses/CPOL-1.02.html).
2. **Tính thật:** “đã kiểm” chỉ khi có lệnh chạy, môi trường, đầu ra và log/trace; nếu không dựng được bản cũ, ghi “chưa xác minh”.
3. **Khác biệt:** so với nguồn tác giả tự host + GitHub/Wayback + Copilot + Playwright, trên **cùng một ca**; đo thời gian tới kết luận đúng, sai sót và độ rõ của điều kiện áp dụng, không đếm số trang AI tạo ra.
4. **Người dùng:** phỏng vấn ít nhất 2–3 tác giả/người bảo trì độc lập, đưa họ một ca thật của họ và xem họ có tự quay lại dùng kết quả không. Không biến lời khen demo thành chứng cứ nhu cầu.
5. **Câu chuyện Kiroween:** [luật Resurrection](https://kiroween.devpost.com/rules) đòi tái tưởng tượng công nghệ lỗi thời bằng đổi mới hiện tại; nhắc “site cũ từng rất lớn” chưa đủ. Demo phải cho thấy chính một **bài/mã/quy trình cũ** được dùng lại để giải việc hôm nay.

**Cổng quyết định:** nếu không có dữ liệu được phép, một ca thực chạy được và lợi ích rõ hơn đối thủ, dừng hoặc đổi ngách. Không dùng điểm rubric giả định 39/50 cũ để biện hộ; [bản hiệu chỉnh chu kỳ 24](../validation/living-legacy-lab-niche-2026-11-23.md) đã hạ đánh giá Living Legacy Lab dạng chung.

## 8. Sổ nguồn và giới hạn

| Nguồn trực tiếp (truy cập 24/11/2026) | Nó chứng minh được | Nó không chứng minh được |
|---|---|---|
| [CodeProject, thông báo 10/2024 qua Wayback](https://web.archive.org/web/20241022172524/https://www.codeproject.com/info/Changes.aspx) | Công ty cũ đóng sau thua lỗ; kế hoạch chỉ đọc | Phân tích tài chính chi tiết hay nguyên nhân offline 2026 |
| [CodeProject, thông báo 11/2024 qua Wayback](https://web.archive.org/web/20241126124743/https://www.codeproject.com/info/Changes.aspx) và [D2 Emerge đồng sáng lập](https://www.linkedin.com/posts/rubinsteindavid_d2-emerge-acquires-codeproject-expanding-activity-7262171470087294976-BXnL) | Có chủ mới và kế hoạch khôi phục | Mọi tính năng/nội dung đã khôi phục |
| [DeveloperMedia sales deck 2017](https://developermedia.com/wp-content/uploads/2017/11/Developer-Media-Advertising-Programs-Overview-2017.pdf) | Các kênh tài trợ/quảng cáo từng bán | Tỷ trọng doanh thu hay mức lỗ 2023–24 |
| [Chris Maunder về thiết kế](https://github.com/ChrisMaunder/Redesigning-CodeProject), [hồ sơ cá nhân](https://chrismaunder.com/) | Mục tiêu nội dung, chi phí bảo trì đã được nêu, quy mô tự báo | Lý do tài chính cụ thể hoặc active users năm 2026 |
| [Eric Woodruff tự lưu bài](https://ewoodruff.us/CodeProject.aspx), [tác giả Ring thuật lại](https://groups.google.com/g/ring-lang/c/5r6-ejzuqPY/m/i3a1Ac41BQAJ) | Một số tác giả bị ảnh hưởng và có hành vi tự bảo tồn | Quy mô toàn thị trường hoặc mọi bài đều mất |
| [CPOL 1.02](https://spdx.org/licenses/CPOL-1.02.html), [Microsoft Copilot upgrade](https://learn.microsoft.com/en-us/dotnet/core/porting/github-copilot-app-modernization/overview), [Playwright trace](https://playwright.dev/docs/trace-viewer) | Ràng buộc tái đăng và baseline cạnh tranh | Ý tưởng B đã vượt đối thủ trong thử nghiệm |

**Giới hạn nghiên cứu:** chưa liên hệ D2 Emerge, chưa có số doanh thu/traffic theo năm, chưa xác minh độ đầy đủ archive, chưa chạy mẫu legacy, chưa khảo sát tác giả/người bảo trì. Kết quả kiểm tra domain chỉ phản ánh truy cập từ môi trường nghiên cứu ngày 24/11/2026.
