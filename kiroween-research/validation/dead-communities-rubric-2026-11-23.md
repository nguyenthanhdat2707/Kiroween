# Hai hướng Kiroween từ cộng đồng hỏi đáp đã suy tàn

Ngày nghiên cứu và truy cập nguồn: **23/11/2026 (Việt Nam)**. Đây là đánh giá **ý tưởng trước khi xây**, không phải điểm giám khảo hoặc xác nhận nhu cầu. Người dùng chấp nhận cải thiện một ngách, không yêu cầu phát minh cả nền tảng mới. Phạm vi là Kiroween 2026, ưu tiên hạng mục **Resurrection**.

## Rubric và điều kiện phải vượt trước khi chấm

[Luật Kiroween 2026](https://kiroween.devpost.com/rules) có hai giai đoạn: vòng 1 đạt/không đạt về chủ đề và việc dùng Kiro; vòng 2 chấm năm tiêu chí ngang trọng số, mỗi tiêu chí 10 điểm: **Potential Impact, Technological Implementation (cách dùng Kiro), Design, Innovation/Idea, Presentation**. Resurrection yêu cầu tái tưởng tượng công nghệ đã lỗi thời bằng đổi mới hiện tại hoặc giải bài toán tương lai. Một website đã ngừng không tự động làm mọi app dùng dữ liệu của nó thành Resurrection; đây là **SUY LUẬN về rủi ro vòng 1**, không phải diễn giải chính thức của giám khảo.

Ứng dụng cần hoạt động ổn định, được xây mới trong kỳ nộp, repo GitHub công khai và có giấy phép nguồn mở, thư mục `/.kiro` ở gốc, URL app chạy được, video công khai dưới ba phút và bài viết về cách dùng Kiro. Dữ liệu/SDK bên thứ ba cần quyền sử dụng. Hạn nộp là **04/12/2026 14:00 PST**. [Luật §1, §4, §6](https://kiroween.devpost.com/rules).

**Phương pháp chấm dưới đây:** điểm là *kịch bản tiềm năng nếu hoàn thành demo chất lượng và qua quyền dữ liệu*, không phải điểm hiện tại hay xác suất thắng. Điểm Technological Implementation chỉ đạt nếu chứng minh thực tế cách dùng Kiro có chủ đích; công nghệ AI trong sản phẩm không tự tạo điểm này. Không cộng điểm riêng cho “cũ” hay “lớn”.

## Bằng chứng mới làm thay đổi hướng từ chu kỳ 22

1. **ĐÃ XÁC MINH — nguồn CodeProject có thể truy theo tác giả:** [Eric Woodruff](https://ewoodruff.us/CodeProject.aspx) tự lưu lại các bài của mình và nối tới kho GitHub; một [bài WinForms](https://ewoodruff.us/CodeProject/MaskedLabelControl.html) ghi môi trường Visual Studio .NET, Windows Forms và mã nguồn trên GitHub. Đây là một ví dụ, chưa chứng minh cả kho 65.000 bài có thể cứu.
2. **ĐÃ XÁC MINH — quyền dữ liệu là cổng chặn:** [CPOL 1.02 do SPDX lưu](https://spdx.org/licenses/CPOL-1.02.html) phân biệt mã nguồn với bài viết; bài không được đăng lại nếu không có sự đồng ý của tác giả. Mỗi bài/code package vẫn phải kiểm giấy phép riêng. Luật Kiroween yêu cầu quyền đối với dữ liệu và tài sản bên thứ ba. Vì vậy **không đề xuất crawl rồi tái đăng toàn bộ CodeProject**.
3. **ĐÃ XÁC MINH — đối thủ nâng cấp mã đã rất mạnh:** [Microsoft GitHub Copilot upgrade](https://learn.microsoft.com/en-us/dotnet/core/porting/github-copilot-app-modernization/overview) đánh giá, lập kế hoạch, sửa, build/test .NET; [AWS Transform for .NET](https://aws.amazon.com/transform/windows/net/) cũng công bố nâng cấp và xác minh. Không xem “AI nâng cấp .NET” là khác biệt.
4. **ĐÃ XÁC MINH — tín hiệu đau chung, không phải nhu cầu CodeProject:** trong [Stack Overflow Developer Survey 2026](https://survey.stackoverflow.co/2026/technology/data), 69,3% người trả lời câu hỏi về lỗi AI chọn mã *có vẻ đúng nhưng sai*, 33,9% chọn API lỗi thời (n=13.648 cho bảng). Khảo sát không hỏi về CodeProject, khôi phục bài hay trả tiền; chỉ làm nền cho nhu cầu kiểm chứng hành vi mã.
5. **ĐÃ XÁC MINH — nguồn Yahoo Groups còn vật liệu cụ thể:** [ARRL](https://www.arrl.org/news/view/yahoo-groups-shutdown-has-ham-radio-interest-groups-seeking-to-save-content) ghi nhóm radio đã mất kho trao đổi, một thành viên lưu các nhóm theo từng mẫu máy. [Trang K5QO](https://www.k5qo.com/yahoo_groups/) còn chỉ mục nhiều nhóm/model. Có thể đọc công khai không đồng nghĩa được phép tái đăng hoặc dùng thông tin cá nhân để huấn luyện.
6. **ĐÃ XÁC MINH — đối thủ của hướng sửa thiết bị:** [Groups.io](https://groups.io/helpcenter/single/web_features.htm) cho tìm và xuất archive tùy quyền chủ nhóm; [Discourse](https://meta.discourse.org/t/migrate-a-mailing-list-to-discourse-mbox-listserv-google-groups-etc/79773) nhập mbox và [Ask AI](https://meta.discourse.org/t/search-better-in-your-community-with-ask-ai/411346) tìm ngữ nghĩa; [iFixit](https://www.ifixit.com/Device/Ham_Radio) có hỏi đáp radio và FixBot. Chỉ “import/search/chat với archive” không đủ khác biệt. Trang ham-radio iFixit hiện hiển thị 1 guide; đây chỉ là một danh mục, không suy thành toàn bộ thị trường còn trống.

## Hướng A — Living Legacy Lab (CodeProject)

**Người dùng và việc cần làm — GIẢ THUYẾT:** lập trình viên giữ ứng dụng cũ gặp bài hướng dẫn có mã từ CodeProject nhưng không biết **mã dùng với phiên bản nào, có còn chạy không, và thay đổi hiện đại có giữ đúng hành vi cũ không**. Một bài của Woodruff cho thấy thông tin môi trường (Visual Studio .NET, WinForms, IIS ở các bài khác) và code thực tồn tại, nhưng chưa có phỏng vấn người bảo trì nào xác nhận họ cần sản phẩm này.

**Trải nghiệm đề xuất:** người dùng đưa URL bài do tác giả còn host hoặc tài liệu họ có quyền + repo/code có giấy phép rõ. App tạo *hồ sơ phục dựng*: (i) tác giả/nguồn/phiên bản công cụ, (ii) điều kiện build và giả định từ bài, (iii) một hoặc vài phép thử hành vi do người kiểm tra xác nhận, (iv) trạng thái **chạy được / chỉ chạy trong môi trường cũ / không chạy / chưa rõ**, kèm log. App đề xuất đường nâng cấp nhưng luôn so hành vi trước/sau; không sao chép bài viết vào repo/app nếu không có quyền. Nếu môi trường cũ không thể chạy, trạng thái phải là **chưa xác minh**, không tạo kết quả giả.

**Demo dưới 3 phút:** chọn một bài + code có quyền rõ, cho thấy tài liệu cũ mất đường truy cập gốc → hồ sơ phiên bản → chạy phép thử thật trên code hợp lệ → chỉ ra kết quả hoặc khác biệt với phiên bản mới. Một dự án rất nhỏ đủ; không cần tuyên bố cứu toàn bộ CodeProject.

**Lõi khác biệt — GIẢ THUYẾT:** biến *bài hướng dẫn + mã + điều kiện môi trường + bằng chứng hành vi* thành một đơn vị có thể kiểm tra. [Copilot upgrade](https://learn.microsoft.com/en-us/dotnet/core/porting/github-copilot-upgrade/best-practices) có build/test cho repo, nên nếu chỉ chạy test hoặc tạo patch thì ý tưởng này trùng. Khác biệt chỉ giữ được nếu đầu vào là tri thức mất nền tảng và app diễn giải/kiểm chứng **tuyên bố trong bài** tốt hơn luồng đọc bài + Copilot/agent.

**Rủi ro chính:** bản quyền bài, license code riêng, runtime cũ khó dựng, yêu cầu Windows/IIS/VS cho một số mẫu, nhiều code không có test, khó chứng minh nhu cầu trong thời gian còn lại. [Microsoft](https://learn.microsoft.com/en-us/lifecycle/faq/developer-tools) xác nhận VB6 IDE và Silverlight đã hết hỗ trợ, nhưng không suy mọi .NET Framework/WinForms đã chết; chọn đúng runtime/công nghệ cũ cho câu chuyện Resurrection.

**Cổng đi tiếp:** tìm 3 bài từ tác giả tự host hoặc có phép dùng, 2 repo/code package có quyền và môi trường chạy được; 1 tác vụ so sánh mà người bảo trì thực sự cần; demo cho thấy app tìm đúng điều kiện/bất tương thích hoặc kiểm thử đúng hơn luồng bài gốc + Copilot/agent. Nếu không đạt, hạ hướng; không chỉ bọc AI bằng giao diện cổ.

## Hướng B — Radio Casebook (Yahoo Groups)

**Người dùng và việc cần làm — GIẢ THUYẾT:** chủ thiết bị radio cũ có triệu chứng cụ thể, kho trao đổi của đúng model trên Yahoo Groups đã biến mất hoặc nằm trong bản lưu khó tra, và họ cần biết **trường hợp nào thực sự được giải, bởi ai, với biến thể máy nào**. [ARRL](https://www.arrl.org/news/view/yahoo-groups-shutdown-has-ham-radio-interest-groups-seeking-to-save-content) xác nhận tri thức theo mẫu máy có giá trị với cộng đồng ham radio; chưa có số liệu hiện nay về số ca cần công cụ này.

**Trải nghiệm đề xuất:** chủ nhóm hoặc người có quyền đưa mbox/archive; app khớp model/biến thể và triệu chứng, gom *ca sửa đã có kết quả* với link hoặc message ID nguồn, phân biệt suy đoán và người sửa xác nhận, hiển thị mâu thuẫn và chỗ thiếu chứng cứ. Người am hiểu duyệt trước khi công bố thành casebook. Một nhóm/model đủ cho demo; tránh gợi ý thao tác điện nguy hiểm khi thiếu điều kiện an toàn.

**Demo dưới 3 phút:** nhập một archive có quyền của một model → hỏi một triệu chứng có nhiều thread → xem ca đã giải với liên kết từng thông điệp và chỗ các thành viên bất đồng → người duyệt chọn kết luận/đánh dấu chưa rõ. Không cần chạy trên phần cứng để chấm ứng dụng, nhưng tuyên bố “giúp sửa được máy” phải có thử trên thiết bị/người dùng thật.

**Lõi khác biệt — GIẢ THUYẾT:** từ thư điện tử rời rạc sang *bằng chứng ca sửa theo model và kết quả*, thay vì chỉ nhập dữ liệu/tìm kiếm/tóm tắt. [Groups.io](https://groups.io/helpcenter/single/web_features.htm), [Discourse Ask AI](https://meta.discourse.org/t/search-better-in-your-community-with-ask-ai/411346) và [iFixit FixBot](https://www.ifixit.com/Info/Terms_of_Use) là đối chứng bắt buộc. Nếu kết quả chỉ là câu trả lời AI có trích dẫn, không đủ khác biệt.

**Rủi ro chính:** quyền và riêng tư người viết email; archive thiếu tệp đính kèm; tóm tắt sai biến thể máy gây chỉ dẫn sai; khó có chuyên gia duyệt trước hạn; nhiều nhóm đã chuyển sang Groups.io. Cần chọn nhóm có quyền rõ, không xuất công khai dữ liệu nhạy cảm.

**Cổng đi tiếp:** 1 archive/model được phép xử lý, tối thiểu 10 ca hỏi đáp có kết quả kiểm được, 1 người am hiểu xác nhận 5 ca; so thời gian tìm câu trả lời đúng và tỷ lệ tự tin sai với tìm kiếm archive/Groups.io, Discourse Ask AI, iFixit. Nếu không có chủ dữ liệu/người kiểm, không gọi là ứng viên mạnh.

## Chấm rubric có điều kiện (không phải điểm hiện tại)

| Hướng | Impact /10 | Kiro /10 | Design /10 | Innovation /10 | Presentation /10 | Tổng tiềm năng /50 | Mức chứng cứ hiện tại |
|---|---:|---:|---:|---:|---:|---:|---|
| **A Living Legacy Lab** | 7 | 8 | 8 | 7 | 9 | **39** | **NEEDS EVIDENCE:** có nguồn/đối thủ rõ, chưa có quyền mẫu cụ thể và phép thử người dùng. |
| **B Radio Casebook** | 7 | 7 | 8 | 8 | 8 | **38** | **NEEDS EVIDENCE:** có archive công khai và vấn đề mất kho, chưa có quyền xử lý/người thẩm định. |

**Lý do từng cột:** Impact 7 vì có người dùng và vấn đề có thật ở mức tín hiệu nhưng chưa đo nhu cầu dùng app. Kiro 7–8 là **trần có điều kiện** nếu quá trình xây dùng spec, steering, hooks/agent và thử nghiệm có log; ý tưởng tự nó không được điểm Kiro. Design 8 vì có một vòng thao tác rõ, nếu UI thực sự mạch lạc. Innovation A 7 vì đối thủ nâng cấp code rất mạnh; B 8 vì cấu trúc ca sửa theo model/kết quả có thể khác search, chưa đối chứng. Presentation A 9 vì có cảnh trước/sau kiểm chứng mã rõ; B 8 vì cần dữ liệu thật và có thể khó giải thích trong 3 phút. Nếu dữ liệu/kiểm thử không qua, các điểm tiềm năng này **không áp dụng**.

## Các hướng đã thử nhưng không đưa vào shortlist

- **Clone CodeProject hoặc tổng hợp toàn bộ bài:** CPOL hạn chế tái đăng bài; rủi ro quyền và phạm vi cao, làm yếu thiết kế/dự thi. **Loại bản rộng**.
- **Agent nâng cấp .NET từ mọi bài cũ:** Microsoft/AWS đã làm phần quan trọng; thiếu đường khác biệt, khó đạt Innovation. **Loại bản chung**.
- **Chuyển Yahoo Groups sang forum mới hoặc chat với archive:** Groups.io/Discourse đã nhập và tìm AI. **Loại bản chung**.
- **Yahoo Answers tổng quát:** quy mô cũ lớn nhưng không có ngách người dùng/tác vụ/dữ liệu có quyền rõ. **Không ưu tiên**.
- **DaniWeb trợ lý hỏi đáp:** site vẫn sống; người vận hành đang có mô hình nối người hỏi với người trả lời; câu chuyện Resurrection yếu. **Không ưu tiên hạng mục này**.

## Phán đoán hiện tại

**SUY LUẬN:** A hợp hướng kỹ thuật Stack Overflow/CodeProject người dùng đang theo, và demo có thể rõ nhất nếu có code hợp lệ. B hợp câu chuyện “cứu tri thức từ một nền tảng đã chết” hơn, nhưng cần quyền archive và chuyên gia radio, khó bảo đảm trước hạn. **Chưa có hướng nào đạt mức STRONG CANDIDATE** vì cả hai thiếu thử người dùng và phép đối chứng. Trật tự hợp lý là thử cổng dữ liệu/quyền trước, rồi mới chọn build. Không đưa điểm dự đoán thành bằng chứng thị trường hay dự báo thắng giải.

**Hiệu chỉnh sau chu kỳ 24:** [phân tích ngách](living-legacy-lab-niche-2026-11-23.md) phát hiện Microsoft đã công bố hỗ trợ nâng cấp cả Web Forms/WinForms và Playwright đã ghi interaction/trace. Do đó **39/50 không dùng cho Living Legacy Lab dạng chung**. Chỉ ngách kiểm chứng hành vi nhiều bước sau postback, có bài/nguồn cũ và baseline thật, còn tiềm năng có điều kiện khoảng 36–38/50; vẫn **NEEDS EVIDENCE**, không phải điểm hiện tại.
