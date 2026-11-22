# Khuyến nghị nghiên cứu

**Thứ tự mới theo tiêu chí cá nhân/gia đình Mỹ–Âu:** xem [xếp hạng lại 22/11/2026](rerank-2026-11-22.md). Bảng bên dưới giữ lại lịch sử xếp hạng theo tiêu chí cũ; không dùng nó làm ưu tiên hiện tại.

**NO IDEA HAS PASSED THE REQUIRED EVIDENCE THRESHOLD.**

**Cập nhật 22/11/2026:** Người dùng ưu tiên vấn đề phổ biến, nhiều người gặp. [Kiểm tra mức phổ biến C20](../validation/c20-prevalence.md) xác nhận nhiều kho chuyên biệt vẫn dùng thẻ, nhưng chưa có số liệu hiện hành cho số thư viện hoặc lượt người dùng bị ảnh hưởng. Vì vậy bảng dưới là xếp hạng theo tiêu chí nghiên cứu cũ; **C20 không còn là ưu tiên số 1 theo tiêu chí mới** nếu không có bằng chứng thêm. Không có ý tưởng nào được nâng hạng.

Sau 8 chu kỳ, 32 hồ sơ công nghệ và 41 giả thuyết: 31 bị loại, 10 còn **NEEDS EVIDENCE**, 0 PROMISING/STRONG. Ba chu kỳ 6–8 liên tiếp không cho cơ hội mới đủ tin cậy, nên dừng quét rộng theo tiêu chí nhiệm vụ. **Chưa khuyến nghị xây dự án.**

| Vai trò so sánh, có điều kiện | Hướng tạm dẫn đầu | Cổng còn thiếu |
|---|---|---|
| Mạnh nhất tổng thể | **C20 — thẻ mục lục** | [LOC](https://guides.loc.gov/american-women-general-collections/catalogs) xác nhận thẻ chưa lên catalog tại kho của họ; cần thư viện mục tiêu, ảnh được phép và so OCR/Omeka. |
| Sáng tạo nhất | **C13 — Yahoo! Blog** | Cứu cấu trúc bài/bình luận từ file xuất cá nhân có thể đặc thù; cần file thật và đối chứng importer. |
| Ý nghĩa nhất | **C07 — bản đồ băng** | Có tiềm năng giữ bối cảnh ký ức gia đình; cần gia đình xác nhận file số hóa hiện tại không đủ. |
| Khả thi nhất | **C18 — bài học BASIC** | Ít dữ liệu/phần cứng, demo ngắn; cần chứng minh cải thiện học tập và vai trò thực của BASIC. |
| Khác biệt cạnh tranh tiềm năng nhất | **C13 — Yahoo! Blog** | Chỉ đúng nếu parser cứu được quan hệ/bình luận mà importer/archive hiện có không cứu. |

## Kiểm chứng nhỏ nhất cho từng hướng

| Mã | Giả định và kỹ thuật; đối chứng | Dữ liệu/demo | Đi tiếp khi…; loại khi… |
|---|---|---|---|
| **C20** | Thư viện có thẻ chưa tra cứu được; OCR ảnh; so [OCR thẻ](https://static.tdwg.org/conferences/2024/posters/jerve-169.pdf)/[Omeka](https://omeka.org/s/explore/). | 20 ảnh thẻ có quyền; tìm tên → ảnh, bản chép, ngăn. | Thủ thư chỉ ca bỏ sót thật và luồng mới tiết kiệm công; loại nếu catalog/công cụ hiện tại đủ. |
| **C07** | Gia đình cần ngữ cảnh băng; khớp nhãn/timeline; so album số/[Tropy](https://tropy-app.com/). | 1 video số hóa + ảnh hộp có quyền; bấm nhãn → đoạn. | 3/5 gia đình nêu ca tìm đoạn khó và ưu tiên luồng này; loại nếu đặt tên/album giải xong. |
| **C13** | Chủ blog còn export; parser nhiều format; so [WordPress import](https://wordpress.org/documentation/article/importing-content/). | 2 export do chủ sở hữu cho phép; nhập riêng tư → bài/bình luận. | Khôi phục đúng và chủ dữ liệu xác nhận giá trị; loại nếu không có file hoặc import đủ. |
| **C09** | Người không chuyên có disk image; đọc filesystem/định dạng; so [FloppoScope](https://github.com/0ldStaph/FloppoScope). | 2 image hợp pháp; mở tệp và provenance. | Người dùng làm được việc chưa làm được với đối thủ; loại nếu chỉ khác giao diện. |
| **C18** | Giáo viên cần luyện debugging; đo hiểu lỗi; so [PICO-8 Edu](https://www.lexaloffle.com/bbs/?pid=109887)/bài giấy. | 1 listing BASIC có quyền; học sinh sửa lỗi và giải thích. | Thử nhỏ cho thấy hiểu lỗi tốt hơn; loại nếu ngang đối chứng/BASIC chỉ trang trí. |

Phỏng vấn và thử đối thủ là nghiên cứu, chưa phải triển khai sản phẩm. Khi có chứng cứ mới, cập nhật [trạng thái](../progress/current-state.md) và ghi lý do nâng/loại. Nếu các cổng thất bại, giữ kết luận không có đề xuất thay vì cứu bằng tính năng.
