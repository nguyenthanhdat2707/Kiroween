# BMad Brainstorming: từ hành vi phần mềm cũ tới năng lực cho agent

**Sổ ý tưởng cụ thể:** [5 hướng sản phẩm/kỹ thuật đã ghi riêng ngày 25/11](../ideas/behavioral-resurrection-ideas-2026-11-25.md). Tài liệu này giữ chứng cứ và câu hỏi nghiên cứu; sổ ý tưởng giữ đầu ra và rủi ro của từng hướng.

Ngày truy cập nguồn: **24/11/2026 (Việt Nam)**. Đây là ghi chép **vòng mở ý tưởng**, chưa phải thiết kế hay quyết định xây. Đầu vào là bản đánh giá người dùng gửi trong `Pasted text.txt` cùng phản hồi tiếp theo: cần hồi sinh **năng lực tổng quát hóa trên dữ liệu mới**, không chỉ replay. Phiên dùng phép **Assumption Reversal** và **TRIZ Contradiction** của BMad ở vai Creative Partner. Bản cài dự án hiện **không có** `_bmad/scripts/memlog.py`, nên không thể tạo memlog chuẩn của skill; ghi tạm các phát hiện nghiên cứu trong tài liệu này và tiến độ dự án, không nhận đây là artifact hoàn tất của BMad.

## Điều kiện người dùng đặt — quyết định đã rõ

1. **Generalization:** xử lý được đầu vào chưa từng quan sát.
2. **Independence:** chạy khi hệ thống gốc bị tắt.
3. **Verifiability:** mỗi quy tắc có bằng chứng.
4. **Uncertainty:** từ chối hành vi ngoài phần đã biết.

**Câu hỏi mở của người dùng:** thay vì hồi sinh hình thái phần mềm, có thể rút tri thức nghiệp vụ từ phần mềm lỗi thời và biến nó thành năng lực mà AI agent hiện đại gọi được một cách đáng tin cậy không? Đây là **GIẢ THUYẾT**, chưa chọn Web Forms hay một công nghệ cụ thể.

**Ranh giới người dùng đã sửa:** hồi sinh một *năng lực* nghĩa là xử lý được đơn hàng mới theo quy tắc đã kiểm; phát lại 10 thao tác cũ chỉ là replay. Ví dụ hệ thống đơn hàng là minh họa tiêu chuẩn, **không phải hệ thống mẫu đã tìm được**.

## Các hướng đầu vào còn giữ để brainstorm

| Hướng từ bản đánh giá người dùng | Câu hỏi riêng cần trả lời |
|---|---|
| **Behavioral Archaeology** | Có khám phá được quy tắc ẩn bằng cách chủ động hỏi/chạy hệ thống cũ không? |
| **Behavioral Resurrection Engine** | Có tạo được một năng lực chạy độc lập với đầu vào mới không? Đây là hướng người dùng muốn phản biện sâu, **chưa chọn xây**. |
| **Behavioral Time Machine** | Có phân biệt quy tắc nào thay đổi qua các phiên bản không? |
| **Digital Fossil Runtime** | Có giữ được môi trường cũ đủ lâu để khám phá và kiểm chứng không? |

Giữ bốn hướng như các **lăng kính**, không coi chúng là bốn ứng viên đã qua kiểm chứng. Không khóa phạm vi vào CodeProject hoặc Web Forms: chúng là nguồn/ca từng được xem xét, không phải yêu cầu mới của người dùng.

## Đối chứng mới: ý tưởng chung đã có người làm

- **ĐÃ XÁC MINH về phần khám phá/mô phỏng:** [ALEX](https://learnlib.de/alex/) học mô hình hành vi web app từ các test input được định nghĩa; [LearnLib](https://learnlib.de/) cung cấp thuật toán học automata. [Hoverfly](https://docs.hoverfly.io/en/latest/) và [WireMock](https://wiremock.org/docs/stateful-behaviour/) mô phỏng phụ thuộc API có trạng thái; chúng không tự chứng minh đã hồi sinh trọn ứng dụng. [Kiro Correctness](https://kiro.dev/docs/specs/correctness/) sinh property-based tests từ đặc tả đã có; nó không tự xác lập ý định nghiệp vụ của phần mềm mất nguồn. Các công cụ này là đối chứng cho khâu kỹ thuật, không phải bằng chứng nhu cầu người dùng.

- **ĐÃ XÁC MINH:** [AWS Transform for mainframe](https://aws.amazon.com/transform/faq/) công bố phân tích COBOL/PL/I, trích quy tắc nghiệp vụ, tạo tài liệu/yêu cầu và hiện đại hóa có người duyệt. [Hướng dẫn traceability](https://docs.aws.amazon.com/transform/latest/userguide/transform-app-mainframe-workflow.html) nối yêu cầu, rule và dòng mã gốc. [Bài AWS/OpenAI](https://aws.amazon.com/blogs/migration-and-modernization/forward-engineering-aws-transform-generated-business-requirements-with-openai-codex/) đã mô tả cả vòng từ trích rule đến agent tạo service mới, kiểm thử và phê duyệt của chuyên gia. Vì vậy “trích rule từ mã cũ rồi dùng agent” **không phải khoảng trống trắng**.
- **ĐÃ XÁC MINH:** [IBM watsonx Code Assistant for Z](https://www.ibm.com/docs/en/watsonx/watsonx-code-assistant-4z/2.x?topic=started-getting-web-ui) có bước nhận diện business rules với người dùng và AI. Cần đối chiếu khả năng thực trên ca cụ thể trước khi gọi đây là đối thủ hoàn toàn tương đương.
- **ĐÃ XÁC MINH:** [nghiên cứu Albassam 2023](https://www.unin.hr/wp-content/uploads/tj_17_2023_1.pdf) mô tả trích quy tắc tính toán từ đầu ra lịch sử, không cần hiểu source, rồi kiểm với test từ đầu ra đó. Ca là một thành phần tính lương trong hệ thống COBOL. Kết quả còn những trường hợp không trích được rule; paper không chứng minh mọi quy tắc tổng quát hóa hay agent runtime được an toàn.
- **ĐÃ XÁC MINH:** [bài kinh nghiệm của Thoughtworks trên Martin Fowler](https://martinfowler.com/articles/black-box-to-blueprint.html) mô tả thử phục dựng đặc tả khi thiếu source, kết hợp nhiều nguồn chứng cứ và duyệt với người dùng; nhóm tác giả nói chưa kiểm được khả năng mở rộng lên toàn hệ thống. Đây là ca thực về công việc khó, không phải chứng minh sản phẩm của ta có thị trường.

## Phép đảo giả định đầu tiên

**Giả định cũ:** nếu khám phá đúng hành vi phần mềm cũ, ta đã thu được quy tắc nên dùng. **Đảo lại:** hệ thống cũ có thể chứa bug, ngoại lệ xử lý tay, chính sách đã hết hiệu lực hoặc quy tắc phụ thuộc dữ liệu/đơn vị tổ chức. “Hệ thống từng làm X” là bằng chứng **mô tả**; “agent hôm nay được phép làm X” là quyết định **chuẩn tắc** cần chủ nghiệp vụ duyệt. Một agent dùng nhầm hai lớp có thể tổng quát hóa rất tốt một quy tắc **không còn đúng**. Đây là **SUY LUẬN kỹ thuật**, cần ca thực để đánh giá tần suất và mức độ.

**Mầm ý tưởng để phản biện, chưa chốt:** một *verified capability capsule* gồm (a) hàm/quy trình độc lập nhận dữ liệu mới, (b) miền đầu vào và điều kiện áp dụng, (c) bằng chứng quan sát/source/đầu ra lịch sử cho từng rule, (d) phiên bản và người phê duyệt ý định nghiệp vụ hiện tại, (e) tự từ chối khi thiếu bằng chứng, (f) giao diện mà agent gọi được. Giao thức gọi là phương tiện phân phối, không phải khác biệt; khác biệt phải nằm ở cách **kiểm và chặn quyết định ngoài miền đã chứng minh**. Không tuyên bố capsule đã làm được trước một thí nghiệm.

**Quyết định chưa có:** khi một quy tắc cũ có bằng chứng từng được chạy nhưng chưa rõ còn đúng, agent được phép làm gì? Đây là câu hỏi mở quan trọng nhất của phiên BMad; chưa ghi câu trả lời thay người dùng.

## Mâu thuẫn kỹ thuật cần giải, không thể giải bằng tên gọi

| Mâu thuẫn | Hệ quả phải thử |
|---|---|
| Tổng quát hóa trên đầu vào mới **vs.** chỉ có hữu hạn ví dụ cũ | Cần thử trên tập dữ liệu giữ lại và biên miền; không thể chứng minh mọi đầu vào từ hữu hạn quan sát. |
| Hệ thống gốc tắt hẳn **vs.** cần oracle để kiểm hành vi mới | Phải thu đủ bằng chứng trước khi tắt, hoặc dùng đầu ra lịch sử/chuyên gia làm oracle yếu hơn; không gọi thiếu oracle là “đã xác minh”. |
| Agent được dùng rule tự động **vs.** rule cũ có thể lỗi thời | Tách “phục dựng hành vi đã từng có” khỏi “được duyệt để sử dụng hiện nay”; trạng thái duyệt thuộc chủ nghiệp vụ. |
| Tính khả dụng rộng **vs.** từ chối khi chưa chắc | Phải đo coverage/abstention cùng độ chính xác; từ chối mọi thứ thì an toàn nhưng vô dụng. |

## Điểm mở cho vòng tiếp theo

**Chưa chọn ngách hay build.** Sau khi làm rõ quyền dùng quy tắc cũ, tìm một năng lực có dữ liệu đầu vào/đầu ra hợp pháp, nhiều trường hợp mới để thử, một người biết nghiệp vụ xác nhận, và đường dùng của agent cụ thể. So trực tiếp với AWS Transform/IBM nếu có source, và với paper black-box/đặc tả thủ công nếu không có source. Ca demo cần cho thấy quy tắc cũ chạy trên đầu vào mới, làm việc khi runtime gốc tắt, trace của từng kết luận, và ít nhất một lần từ chối đúng. Nếu không có dữ liệu giữ lại hoặc chuyên gia xác nhận ý định hiện tại, chưa thể nâng hạng ý tưởng.
