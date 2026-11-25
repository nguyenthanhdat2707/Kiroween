# Các ý tưởng hồi sinh năng lực từ phần mềm cũ

Ghi ngày **25/11/2026 (Việt Nam)**. Đây là **sổ ý tưởng chọn lọc** từ bản đánh giá người dùng và phiên BMad tiếp theo, không phải thiết kế đã chốt hay dự án đã kiểm chứng. Nguồn đối chứng được truy cập 24/11/2026; xem [phân tích chứng cứ](../validation/behavioral-capability-for-agents-2026-11-24.md). Bốn điều kiện người dùng đặt cho mọi ý tưởng: **xử lý đầu vào mới, chạy độc lập khi hệ gốc tắt, truy được chứng cứ của từng quy tắc, từ chối khi chưa biết**. Ví dụ quản lý đơn hàng chỉ minh họa phép thử, chưa có hệ thống hay dữ liệu thực.

## 1. Behavioral Resurrection Engine — tái tạo một năng lực từ hành vi quan sát

**Nguồn ý tưởng: người dùng. Vai trò: ứng viên sản phẩm, chưa chọn xây.**

- **Việc cần giải:** tổ chức còn dùng phần mềm cũ nhưng thiếu mã nguồn hoặc mất người hiểu nó; cần giữ *một năng lực nghiệp vụ* trước khi runtime biến mất.
- **Đầu vào giả định:** hệ gốc còn gọi được trong giai đoạn khám phá, hoặc có đầu vào/đầu ra lịch sử đủ rõ; cần quyền sử dụng dữ liệu và người xác nhận quy tắc.
- **Đầu ra:** một thành phần độc lập nhận **đơn hàng mới** và cho quyết định/kết quả có giải thích; từ chối trường hợp ngoài miền chứng cứ. Phát lại 10 đơn hàng đã ghi không đạt mục tiêu.
- **Lõi kỹ thuật cần chứng minh:** chọn phép hỏi hệ cũ để phân biệt các giả thuyết quy tắc; sinh triển khai; tìm phản ví dụ; đo mức tổng quát hóa trên dữ liệu giữ lại và tỷ lệ từ chối đúng.
- **Đối chứng bắt buộc:** [ALEX](https://learnlib.de/alex/) đã học mô hình hành vi web app; [nghiên cứu black-box 2023](https://www.unin.hr/wp-content/uploads/tj_17_2023_1.pdf) đã trích quy tắc tính toán từ đầu ra lịch sử. Cần cho thấy giá trị thực vượt việc dùng các phương pháp đó với coding agent.
- **Nguy cơ loại:** nếu chỉ chạy lại kịch bản hoặc không có oracle/đầu ra thật cho đầu vào mới thì không chứng minh được năng lực đã hồi sinh. Nếu hệ gốc đã tắt trước khi có mẫu và không có dữ liệu lịch sử, không thể khẳng định đúng.

## 2. Verified Capability Capsule — biến quy tắc cũ thành công cụ agent gọi được

**Nguồn ý tưởng: người dùng đề xuất hướng trích tri thức cho agent; trợ lý đề xuất hình thức capsule. Vai trò: biến thể sản phẩm riêng hoặc đầu ra hẹp của ý tưởng 1, chưa chốt.**

- **Việc cần giải:** một agent cần dùng một quyết định nghiệp vụ đã bị khóa trong phần mềm cũ, nhưng không nên tự suy luận lại quy tắc từ văn bản mơ hồ mỗi lần chạy.
- **Đầu ra:** một hàm/công cụ nhận dữ liệu mới; kèm miền áp dụng, phiên bản quy tắc, chứng cứ cho từng nhánh, trạng thái người phụ trách đã duyệt và lý do từ chối. Agent gọi công cụ và nhận kết quả có cấu trúc; giao thức gọi (MCP/API) chỉ là cách phân phối.
- **Điểm phải tách:** **“phần mềm cũ từng làm X”** là chứng cứ lịch sử; **“agent hiện được phép làm X”** cần xác nhận nghiệp vụ. Quy tắc cũ có thể là bug hoặc chính sách hết hiệu lực. Chưa có quyết định của người dùng về trạng thái quy tắc chưa được duyệt: chỉ hiển thị, cho chạy thử, hay từ chối hoàn toàn.
- **Đối chứng bắt buộc:** [AWS Transform](https://docs.aws.amazon.com/transform/latest/userguide/transform-app-mainframe-workflow.html) đã trích quy tắc có truy vết từ source; [quy trình AWS + Codex](https://aws.amazon.com/blogs/migration-and-modernization/forward-engineering-aws-transform-generated-business-requirements-with-openai-codex/) đã dùng đặc tả đó để tạo dịch vụ mới. Tính mới không thể chỉ là “trích rule rồi cho agent gọi”.
- **Nguy cơ loại:** nếu chỉ là wrapper API cho luật người khác đã viết, không có phát hiện/kiểm chứng/từ chối đáng tin, ý tưởng không đủ khác biệt. Nếu không có người chịu trách nhiệm duyệt, agent không nên coi hành vi lịch sử là chính sách hiện tại.

## 3. Behavioral Time Machine — nhận diện quy tắc đã đổi hoặc biến mất

**Nguồn ý tưởng: người dùng. Vai trò: hướng sản phẩm khác với 1; ưu tiên sau khi có ít nhất hai phiên bản chạy được.**

- **Việc cần giải:** khi nâng cấp hoặc thay nhà cung cấp, người bảo trì cần biết *quyết định nghiệp vụ nào đã đổi*, chứ không chỉ thấy giao diện/response khác.
- **Đầu vào/đầu ra:** cùng bộ đầu vào có các trường hợp mới và biên → chạy trên hai phiên bản → tạo bản đồ `điều kiện → kết quả cũ/mới → chứng cứ → người duyệt sự thay đổi`.
- **Khác biệt cần chứng minh:** gom nhiều sai khác cụ thể thành một quy tắc có ý nghĩa cho người nghiệp vụ; không chỉ là snapshot diff. Có thể tạo bộ regression cho agent về sau.
- **Đối chứng bắt buộc:** ALEX đã [so mô hình hành vi](https://learnlib.de/alex/); công cụ test thông thường cũng so đầu ra. Chỉ đi tiếp nếu bản đồ quy tắc giúp người dùng ra quyết định nhanh/đúng hơn.
- **Nguy cơ loại:** cần hai phiên bản có thể chạy hoặc dữ liệu lịch sử tương đương; nếu chỉ còn một bản, ý tưởng không thực hiện được như mô tả.

## 4. Behavioral Archaeology — máy khám phá điều kiện ngầm

**Nguồn ý tưởng: người dùng. Vai trò: mô-đun nghiên cứu có thể dùng trong 1 hoặc 3; chưa đủ căn cứ làm sản phẩm độc lập.**

- **Năng lực:** từ nhiều giả thuyết về một quy tắc, chọn đầu vào tiếp theo có khả năng phân biệt chúng, hỏi hệ gốc, lưu kết quả và phản ví dụ. Chẳng hạn thay đúng một biến trong đơn hàng để thấy ngưỡng giảm giá phụ thuộc tổng tiền hay loại khách hàng.
- **Đầu ra:** tập điều kiện ứng viên, bằng chứng ủng hộ/bác bỏ và vùng chưa quan sát, không tự tuyên bố đã học toàn bộ hệ thống.
- **Đối chứng:** [LearnLib](https://learnlib.de/) và [ALEX](https://learnlib.de/alex/) đã thực hiện active automata learning. Giá trị mới phải đến từ việc tìm **quy tắc nghiệp vụ có ý nghĩa** hoặc kiểm soát chi phí hỏi hệ cũ, không từ tên thuật toán.
- **Nguy cơ loại:** không có quyền/tài nguyên để chạy nhiều phép hỏi; không thể đặt lại trạng thái hệ thống sạch; đầu ra bị nhiễu bởi dữ liệu, thời gian hoặc tác dụng phụ.

## 5. Digital Fossil Runtime — giữ hệ cũ làm nguồn kiểm chứng

**Nguồn ý tưởng: người dùng. Vai trò: hạ tầng hỗ trợ 1, 3, 4; chỉ làm sản phẩm riêng nếu phát hiện nhu cầu lưu runtime độc lập.**

- **Năng lực:** đóng gói bản chạy, dependency, dữ liệu thử và cách đặt lại trạng thái của một lát cắt công nghệ cũ; người nghiên cứu có thể gọi lại nó để kiểm giả thuyết.
- **Đầu ra:** một môi trường thực thi có phiên bản rõ, log chạy và khả năng reset; không đồng nghĩa đã trích được quy tắc.
- **Khác biệt cần chứng minh:** tái lập được một ca mà VM/container thường hoặc archive không làm được, và có quyền phân phối thành phần đi kèm.
- **Nguy cơ loại:** license, hệ điều hành/thiết bị cũ, bí mật dữ liệu, phụ thuộc ngoài hoặc phần mềm cần dịch vụ đã ngừng. Chỉ bọc một ứng dụng vào container là demo kỹ thuật, chưa phải hồi sinh năng lực cho người dùng.

## Cách các ý tưởng liên hệ, không phải quyết định ghép hết vào một sản phẩm

```text
Digital Fossil Runtime (nếu cần hệ gốc chạy)
             ↓
Behavioral Archaeology (tìm giả thuyết và phản ví dụ)
             ↓
Behavioral Resurrection Engine (năng lực chạy độc lập)
             ↓
Verified Capability Capsule (một cách đưa năng lực cho agent)

Behavioral Time Machine: nhánh khác để so hai phiên bản.
```

**Lọc ở thời điểm này:** ý tưởng **1 và 2** là hai giả thuyết sản phẩm cần phản biện sâu nhất; **3** phụ thuộc có hai phiên bản; **4 và 5** là kỹ thuật hỗ trợ, chưa cần dựng riêng. Không gọi bất kỳ ý tưởng nào là `PROMISING` hay cộng vào [sổ 41 giả thuyết cũ](all-candidates.md) trước khi có ca thực. Hướng CodeProject trước đó vẫn nằm ở [bốn ngách hồi sinh riêng](../discovery/codeproject-collapse-and-revival-2026-11-24.md); không lặp nội dung ấy ở đây.

**Phép thử chung trước khi chọn:** tìm một năng lực có đầu vào/đầu ra được phép dùng; giữ lại bộ dữ liệu chưa cho hệ khám phá thấy; chạy bản tái tạo khi runtime gốc tắt; yêu cầu truy vết từng quy tắc; đo đồng thời tỷ lệ trả lời đúng, tỷ lệ từ chối và số lần từ chối đúng. Cần một người biết nghiệp vụ xác nhận liệu quy tắc lịch sử còn nên áp dụng. Chưa có dữ liệu, người dùng hoặc kết quả thí nghiệm như vậy.
