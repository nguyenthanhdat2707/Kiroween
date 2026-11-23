# Living Legacy Lab: thu hẹp tới một hành vi cũ có thể kiểm chứng

**Bối cảnh nền tảng cập nhật 24/11/2026:** xem [nghiên cứu CodeProject đóng cửa và bốn ngách hồi sinh](../discovery/codeproject-collapse-and-revival-2026-11-24.md). Tài liệu này giữ phạm vi thiết kế phép thử hành vi Web Forms; nguyên nhân công ty đóng đã được tách khỏi giả thuyết cạnh tranh/AI trong nghiên cứu mới.

Ngày truy cập nguồn: **23/11/2026 (Việt Nam)**. Nghiên cứu ý tưởng, không triển khai. Kế thừa [chu kỳ 23](dead-communities-rubric-2026-11-23.md); nhãn **ĐÃ XÁC MINH / SUY LUẬN / GIẢ THUYẾT / CHƯA RÕ** áp dụng cho kết luận chính.

## Hiệu chỉnh quan trọng

Đề xuất trước là “bài CodeProject + mã + phiên bản + log”. **SUY LUẬN:** đây còn là *khuôn dữ liệu*, chưa phải ngách sản phẩm. [Microsoft GitHub Copilot upgrade](https://learn.microsoft.com/en-us/dotnet/core/porting/github-copilot-upgrade/dotnet-overview) công bố hỗ trợ cả WinForms và ASP.NET Web Forms; [nó còn có kỹ năng chuyển Web Forms sang Blazor](https://learn.microsoft.com/en-us/dotnet/core/porting/github-copilot-app-modernization/scenarios-and-skills). [Playwright](https://playwright.dev/docs/codegen) đã ghi lại tương tác và [Trace Viewer](https://playwright.dev/docs/trace-viewer) đã lưu ảnh/DOM/network; không thể gọi “record và so UI” là mới. Điểm tiềm năng **39/50** chu kỳ 23 chỉ là kịch bản thuận lợi, **không còn là ước lượng đáng dùng cho bản chung**.

Ngách phải chỉ ra một lỗi có thể xảy ra **dù build xanh và giao diện ban đầu đúng**, rồi biến điều kiện ngầm trong bài hướng dẫn cũ thành phép kiểm không thể bị agent sửa theo ý mình. Trước khi có phép so đối thủ, khác biệt **CHƯA RÕ**.

## So ba lát cắt

| Lát cắt | Tác vụ người dùng | Bằng chứng / đối thủ | Phán đoán |
|---|---|---|---|
| **A. ASP.NET Web Forms: state sau postback và control tạo động** | Nhóm đang sửa/chuyển một trang cũ cần giữ hành vi qua 2–3 tương tác, kể cả dữ liệu đã chọn, validation, dynamic controls. | [Microsoft về dynamic controls/ViewState](https://learn.microsoft.com/en-us/previous-versions/aspnet/hbdfdyh7%28v%3Dvs.100%29), [page lifecycle](https://learn.microsoft.com/en-us/previous-versions/aspnet/ms178472%28v%3Dvs.100%29); [Copilot upgrade Web Forms → Blazor](https://learn.microsoft.com/en-us/dotnet/core/porting/github-copilot-app-modernization/scenarios-and-skills); [Playwright codegen](https://playwright.dev/docs/codegen). | **Ưu tiên phép thử.** Hành vi nhiều bước có điều kiện kỹ thuật thật, tác vụ chẩn đoán rõ. Cần chứng minh tiết kiệm công/tìm lỗi hơn dùng Playwright + Copilot hiện tại. Web Forms **vẫn được hỗ trợ**, nên Resurrection phải gắn với phiên bản/tài liệu cũ cụ thể, không gọi cả Web Forms là đã chết. |
| **B. WinForms control từ bài CodeProject** | Kiểm tra ví dụ control cũ có còn đúng khi retarget .NET và khi UI đổi font/hiển thị. | [Eric Woodruff tự lưu bài Masked Label và link code](https://ewoodruff.us/CodeProject/MaskedLabelControl.html); [Microsoft đã hướng dẫn agent nâng cấp WinForms và kiểm tra layout/font](https://learn.microsoft.com/en-us/dotnet/desktop/winforms/migration/how-to-upgrade-winforms). | **Dự phòng.** Mẫu cụ thể có thật, nhưng cần Windows desktop/UI automation và đối thủ nâng cấp mạnh. Bản WinForms chung yếu hơn A. |
| **C. Silverlight tutorial/app** | Cứu ví dụ plugin cũ để chạy trong browser mới. | [Microsoft xác nhận Silverlight hết hỗ trợ 2021](https://learn.microsoft.com/en-us/lifecycle/faq/developer-tools); [OpenSilver](https://opensilver.net/migration-service/) đã cung cấp đường chạy/migrate sang browser/WASM. | **Không chọn hiện tại.** Resurrection rất rõ nhưng đối thủ trực diện và thiếu môi trường chạy bản gốc để kiểm chứng hành vi trong thời gian ngắn. |

## Ngách khuyến nghị thử: chứng minh hành vi sau postback của một control Web Forms cũ

**Người dùng — GIẢ THUYẾT:** một người phải bảo trì hoặc chuyển một trang Web Forms sang Blazor nhưng không có test cho tương tác nhiều bước. Họ tìm thấy bài hướng dẫn cũ về control và tin rằng “mã compile + ảnh ban đầu đúng” là đủ. [Tài liệu Microsoft](https://learn.microsoft.com/en-us/previous-versions/aspnet/hbdfdyh7%28v%3Dvs.100%29) giải thích dynamic control có thể được tái tạo ở thời điểm khác với quá trình khôi phục ViewState; [bài của một người trực tiếp thử nghiệm](https://blog.thomasbandt.de/39/2250/de/blog/blog/aspnet-dropdownlist-und-optgroups.html) nói một cách làm trên CodeProject thiếu hoặc lỗi ViewState trong biểu mẫu phức tạp. Đây là **ví dụ định tính**, không phải tỷ lệ lỗi phổ biến.

**Một đầu ra duy nhất:** *hợp đồng hành vi có chứng cứ*, gồm: URL/tác giả của bài cũ (chỉ liên kết, không tái đăng), mã/commit đầu vào có quyền, framework/browser cụ thể, chuỗi hành động, giá trị mong đợi do con người duyệt, kết quả chạy, log và trạng thái **đã kiểm / không đạt / chưa rõ**. Tuyên bố có thể kiểm: “Sau khi chọn B, thêm control động, bấm Submit, mục B vẫn được chọn và validation không mất.” Hợp đồng sống cùng app, chạy lại trên bản chuyển đổi.

**Luồng MVP đề xuất — GIẢ THUYẾT thiết kế:**

1. Người dùng chọn đúng một bài hướng dẫn hoặc repo có quyền và một trang Web Forms **đang chạy**. Không nhận toàn bộ CodeProject hay toàn bộ ứng dụng doanh nghiệp.
2. AI gợi ý 2–3 giả định cần kiểm từ bài và mã: phiên bản ASP.NET, thứ tự tạo control, điều kiện postback, vùng state. Người dùng chấp nhận/sửa kỳ vọng trước khi kiểm thử; AI không tự xác nhận kỳ vọng của chính nó.
3. Ghi một luồng trong browser cũ: tải trang → chọn/nhập → gây postback hoặc tạo control → submit → đọc giá trị hiển thị, thông báo validation và network/DOM trace. Lưu hash/phiên bản môi trường; không coi screenshot đơn lẻ là bằng chứng hành vi.
4. Chạy cùng hợp đồng trên bản mới, so **giá trị có ý nghĩa với người dùng** thay vì so byte của `__VIEWSTATE`, session ID, thời gian hoặc bố cục ngẫu nhiên. Trả lời “mất lựa chọn sau postback ở bước 3”, kèm hai trace. Nếu không chạy được bản cũ, trả **chưa rõ**.
5. Xuất một test có thể chạy lại và một thẻ chứng cứ gắn nguồn, không tự đăng lại bài gốc hay đề xuất sửa code nếu chưa cần.

**Biên sản phẩm:** Đây là công cụ *đặc tả và chứng minh hành vi khi chuyển công nghệ*, không phải một AI migration agent. Kết quả phải hữu ích ngay cả khi người dùng tự nâng cấp bằng Copilot/Visual Studio. [Microsoft](https://learn.microsoft.com/en-us/dotnet/architecture/blazor-for-web-forms-developers/migration) xác nhận Web Forms có state/session khác Blazor; [Playwright](https://playwright.dev/docs/codegen) có thể ghi test và assertion nhưng không tự biết *điều kiện trong bài cũ* nào quan trọng. Việc app của ta làm tốt hơn combo Copilot + Playwright **chưa được chứng minh**.

## Dữ liệu mẫu, quyền và câu chuyện Kiroween

- **ĐÃ XÁC MINH:** [eShopModernizing](https://github.com/dotnet-architecture/eShopModernizing) của .NET Foundation có ví dụ Web Forms và [MIT license](https://github.com/dotnet-architecture/eShopModernizing/blob/main/LICENSE). Đây là bộ thử **quyền rõ**; vẫn phải xem tệp bên trong và điều kiện chạy trước khi chọn ca. [eShopOnBlazor](https://github.com/dotnet-architecture/eshoponblazor) là đối chứng migration có giấy phép MIT, không tự giả định hai repo có hành vi tương đương.
- **ĐÃ XÁC MINH:** [Eric Woodruff](https://ewoodruff.us/CodeProject.aspx) tự host nhiều bài CodeProject ASP.NET 1.1/2.0, nhưng [CPOL](https://spdx.org/licenses/CPOL-1.02.html) không tự cho tái đăng bài. Có thể trích liên kết và metadata; muốn đưa toàn văn, ảnh, code vào demo/repo phải kiểm từng license hoặc có tác giả đồng ý.
- **SUY LUẬN về vòng 1 Kiroween:** “Web Forms” nói chung chưa chết; [Microsoft còn ghi nó được hỗ trợ trong nhiều năm](https://learn.microsoft.com/en-us/dotnet/architecture/blazor-for-web-forms-developers/migration). Resurrection phải là *ví dụ/hành vi của phiên bản cũ hoặc kho tri thức CodeProject ngừng truy cập*, được đổi thành hợp đồng kiểm thử hôm nay. Nếu demo chỉ là regression tester cho Web Forms hiện còn sống, chủ đề Resurrection **yếu**; hạng mục khác có thể phù hợp hơn nhưng cần đối chiếu luật trước khi chọn.

## Vì sao ngách này có thể mạnh, và điều gì có thể giết nó

| Rubric | Điểm sáng nếu demo thật | Điểm mất nếu không có chứng cứ |
|---|---|---|
| Impact | Một người bảo trì nhìn thấy lỗi mà build xanh bỏ sót; tránh sai hành vi sau migration. | Chưa biết số người trả công để kiểm một trang; một bug minh họa tự tạo không chứng minh tác vụ thực. |
| Kiro Implementation | Specs/steering định nghĩa trạng thái và nguồn; Kiro hỗ trợ xây bộ tạo hợp đồng, hooks kiểm trạng thái “đã kiểm” chỉ khi có trace; mô tả thí nghiệm trong bài nộp. | Chỉ nói “dùng AI/Kiro” không tạo điểm. Điểm này phụ thuộc quá trình phát triển thực tế. |
| Design | Một claim card, một luồng 3 bước, một diff quan sát được; không bắt người xem đọc cả codebase. | Nếu thành bảng log kỹ thuật dài, khó dùng. |
| Innovation | Nối bài hướng dẫn lỗi thời, điều kiện ngầm và test hai phiên bản; phân biệt thiếu chứng cứ. | Copilot + Playwright + test tự viết có thể làm gần hết; nếu không tốt hơn, Innovation thấp. |
| Presentation | Demo “build pass → postback làm mất state → test báo lỗi ở bước 3 → sửa và pass” rất dễ hiểu. | Nếu không chạy được app cũ hoặc không có sự khác biệt có thật, video chỉ là mô phỏng. |

**Hiệu chỉnh 39/50:** bản tổng quát không xứng 39/50. Ngách này chỉ có thể ở vùng **khoảng 36–38/50 có điều kiện** nếu chứng minh được ca lỗi thật, trace thật, quyền dữ liệu và lợi ích hơn baseline. Đây là đánh giá chủ quan phục vụ quyết định, không phải điểm hiện tại hay dự báo giải. Nếu chỉ trích xuất bài + chạy test thông thường, nên hạ Innovation và dừng.

## Phép thử quyết định trước khi thiết kế app

1. **Dữ liệu và môi trường:** chọn một trang Web Forms MIT từ [eShopModernizing](https://github.com/dotnet-architecture/eShopModernizing) hoặc một ca tác giả cho phép; xác nhận chạy được. Cần Windows/IIS hoặc môi trường phù hợp cho bản cũ; **CHƯA RÕ** người làm dự án có sẵn không.
2. **Hành vi:** dựng 3 kịch bản có state/postback, cố ý chọn ít nhất một điều kiện dễ bị bỏ sót; baseline kết quả phải được chạy và lưu, không do AI suy đoán. Nếu sample không có bug thật, benchmark có thể dùng một nhánh thay đổi có chủ đích, ghi rõ đó là *thí nghiệm*, không gọi lỗi sản phẩm.
3. **Đối chứng:** người thử dùng Copilot upgrade + Playwright codegen/trace để tìm và mô tả cùng sai khác. Đo thời gian đến phát hiện đúng, số bước con người, và tình huống AI tự tin sai. Không đo mỗi số test được tạo.
4. **Cổng tiếp tục:** ít nhất một sai khác hành vi thực được tìm rõ hơn hoặc nhanh hơn baseline, một developer Web Forms nói họ sẽ dùng hợp đồng này cho ca riêng, và demo có dữ liệu được phép. Nếu không có ba điều này, Living Legacy Lab **NEEDS EVIDENCE** và không đưa vào build chính.
