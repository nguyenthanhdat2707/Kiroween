# Giả thuyết và kế hoạch kiểm chứng — Task B

Mỗi phép thử lấy từ falsifier trong `opportunities-revised.json` và §7 `cross-review.md` của agent đề xuất. Coordinator chỉ gom lại, ước lượng công sức và ghi điều kiện bác bỏ.

**Chưa phép thử nào được chạy.** Còn khoảng 9 ngày đến 04/12/2026 14:00 PT. Cột "Công sức" là ước lượng của Coordinator (SUY LUẬN).

## H0 · Giả thuyết xuyên suốt: có người trả tiền cho **công cụ** bảo tồn

| | |
|---|---|
| Trạng thái | **Chưa có bằng chứng** (B, C). Chỉ thấy trả tiền cho nội dung và phí lưu trữ. |
| Phép thử | Tìm ít nhất một giao dịch, gói thầu hay hợp đồng mua **công cụ** (không phải grant số hóa, không phải quyên góp hosting) trong từng cụm |
| Bác bỏ nếu | Không tìm thấy ở cụm nào. Khi đó mọi cơ hội phải dựa trên mô hình tổ chức, grant hoặc cộng đồng, và `sustainability` ≤ 3 |
| Công sức | ~0,5 ngày, nghiên cứu nguồn công khai |

## Theo cụm

| Mã | Giả thuyết | Phép thử nhỏ nhất | Bác bỏ nếu | Người đề xuất | Công sức |
|---|---|---|---|---|---|
| H1a (T1) | Nút thắt end-of-life game là **thiếu chuẩn kỹ thuật**, không chỉ IP | Lấy mẫu 20 game live-service đóng cửa 2024–2026; phân loại rào cản (IP, kỹ thuật, kinh tế) theo nguồn công khai | Đa số bị chặn bởi IP hoặc đã có bản offline | A, B | 1–2 ngày |
| H1b (T1) | Đội hồi sinh gặp vấn đề **kế nhiệm maintainer** | Đối chiếu lịch sử commit và người duy trì của Pretendo và Homecoming | Không có sự cố kế nhiệm nào được ghi nhận | B, C | 0,5 ngày |
| H1c (T1) | Có studio tự nguyện cam kết end-of-life sau phản hồi EC | Theo dõi dự thảo code of conduct của EC; tìm cam kết công khai | Không có studio nào | B, C | Phụ thuộc lịch EC; có thể quá hạn thi |
| H2 (T2) | Export của nền tảng nhỏ **mất ngữ nghĩa** mà parser thường không khôi phục | 3–5 gói export thật (Mastodon AS2.0, Cohost, Glitch, một SaaS không tài liệu). So parser viết tay với AI suy schema trên mẫu gán nhãn tay | Parser viết tay đạt tương đương, hoặc tổn thất không đáng kể | A, B | 1–2 ngày; cần dữ liệu có quyền dùng |
| H3 (T3) | Bàn giao tạp chí nhỏ **mất tính đầy đủ** (supplement, phiên bản), không chỉ thiếu tham gia | Manifest trước/sau trên tạp chí đã chuyển PKP PN hoặc JASPER | Bản lưu đầy đủ; vấn đề chỉ là tham gia | C | 1 ngày |
| H4 (T4) | Chuyển kho di sản **mất ngữ nghĩa quyền** (roles, protocols) mà công cụ chính thức không giữ | Một ca chuyển Mukurtu thật có custom protocols và ground truth | Công cụ chính thức giữ đủ; nút thắt là governance | C | Cần đối tác; khó trong 9 ngày |
| H5 (T5) | LLM tạo **cải thiện đo được** so với `m2c` + `decomp-permuter` trong giải mã khớp byte | Tái lập benchmark trên ≥30 hàm của một dự án decomp khác; ablation cùng ngân sách; báo cáo token và giờ chuyên gia | Không có cải thiện có ý nghĩa | A, B, C | 1–2 ngày; cần GPU/API budget |
| H6 (T5) | Quét môi trường tất định **không đủ**; AI cấu hình giúp đáng kể | 15 phần mềm cũ; so quét emulator × OS × kiểm tra boot với cấu hình do AI đề xuất; oracle là chạy hết một kịch bản | Quét tất định đạt tương đương | B | 1–2 ngày |
| H7 (S1) | Có đường pháp lý và cộng đồng sẵn sàng cho bảo tồn keitai | Hỏi Kahvibreak; tra quy định CPRM và quyền IP tại Nhật | Không có đường hợp pháp để công khai demo | B | Cần liên hệ cộng đồng |
| H8 (S2) | Đa số web app học thuật hết bảo trì **tĩnh hóa được** mà giữ công năng | 20 web app tin sinh học/DH mã nguồn mở; đo tỷ lệ chuyển sang static/WASM giữ công năng cốt lõi | Tỷ lệ thấp, hoặc đã có công cụ làm việc này | A | 2 ngày |

## Điều kiện để bất kỳ cụm nào đi tiếp

1. Qua cổng `theme` ≥ 3 theo anchor Phase 2. T3 và T4 hiện trượt theo chính agent chấm.
2. Có ít nhất một bằng chứng hành vi về nhu cầu cho **đúng** người dùng mục tiêu.
3. Có dữ liệu hoặc artifact được phép dùng cho demo công khai.
4. Nếu đề xuất AI: phải có baseline thông thường và phép đo cải thiện.
