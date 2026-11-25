# Phương án hiện có và phân tích khoảng trống — Task B

Bảng chi tiết nằm ở §5 của từng báo cáo: [`A`](../agent-a/report.md), [`B`](../agent-b/report.md), [`C`](../agent-c/report.md). Phản biện bổ sung nằm ở §3 của các `cross-review.md`.

**Quy tắc:** chỉ gọi là "khoảng trống" khi đã nêu tên phương án được kiểm tra. Cả ba agent đều tuân thủ điều này ở Round 2.

## 1. Tám hướng tiếp cận

| Hướng | Mạnh ở | Không giải được | Khoảng trống còn lại (nhãn) |
|---|---|---|---|
| **Internet Archive / web archiving** (Wayback, Archive-It, Webrecorder WACZ 1.1.1) | Quy mô; WACZ phát lại trực tiếp trên trình duyệt | Nội dung sau đăng nhập, backend, tính đầy đủ; IA thua Hachette (2024); thâm hụt ngân sách 2023 và 2025 (B §5) | Bản sao có đủ để làm được công việc người dùng cần hay chưa: CHƯA RÕ (`C-G-C9`) |
| **ArchiveTeam** (khẩn cấp) | Phản ứng nhanh | **Phụ thuộc nhà vận hành hợp tác** (Cohost phải tắt batching, cấp danh sách user); chỉ dữ liệu công khai (B §5) | Bộ công cụ hoặc quy trình để nhà vận hành nhỏ hợp tác rẻ: GIẢ THUYẾT (B-O2) |
| **Bảo tồn và giả lập phần mềm** (EaaSI, Software Heritage, VGHF, MAME/DOSBox) | Chạy lại hành vi gốc | §1201 giới hạn truy cập từ xa; server backend thường không có; keitai: "no comprehensive emulator" (B §5) | Không làm lại EaaSI; chỉ xét phần phụ thuộc chưa được đáp ứng (`C-G-C11`) |
| **Di chuyển dữ liệu** (GDPR Art. 20, DTI/DTP, Takeout, export Mastodon, **EU Data Act 09/2025**) | Có cơ sở pháp lý ở EU | Phục vụ di chuyển giữa **nền tảng lớn còn sống**; mất ngữ nghĩa và quan hệ khi export | Tổn thất của chính bộ chuyển hiện có: GIẢ THUYẾT (`C-G-C15/C20`, A-O2) |
| **Mã nguồn mở thay thế** (Penpot, Mastodon, Matrix, Nextcloud) | Fork được khi đội gốc dừng | Không mang theo dữ liệu cũ; quyền với asset không đi kèm quyền với mã | Kế nhiệm maintainer: chưa đo (`C-O2-C3`) |
| **Tự host** | Toàn quyền | Chính chi phí vận hành làm instance tự host cũng chết (A §5) | Không có bằng chứng chủ cộng đồng muốn tự vận hành (`C-G-C23`) |
| **Lưu trữ phi tập trung** (IPFS, Filecoin, Arweave) | Địa chỉ theo nội dung | IPFS không có cơ chế khuyến khích lưu (A §5); **không tìm thấy nền tảng nào được cứu nhờ cách này** (B §5) | **Không phải khoảng trống chính** (cả ba agent) |
| **Hồi sinh do cộng đồng** (Homecoming, Pretendo, Wiimmfi) | Bằng chứng hành vi mạnh nhất; có tiền lệ license chính thức | License có thể bị thu hồi; không mở mã; không áp dụng cho game khác | Kế nhiệm và quy trình bàn giao: GIẢ THUYẾT (C-O2) |
| **Hệ thống di sản số** (CLOCKSS, LOCKSS, Portico, PKP PN, Mukurtu, NDL WARP, PARADISEC, ELAR) | Chuẩn cho học thuật; có thẩm quyền pháp lý cho lưu chiểu | Tạp chí nhỏ không tham gia: dưới 1% trong 204 publisher gửi phần lớn nội dung vào nhiều archive (B, **snippet**) | Mất ngữ nghĩa quyền khi chuyển kho: GIẢ THUYẾT (C-O3) |

## 2. Phương án bị bỏ sót ở Round 1 (phát hiện nhờ phản biện chéo)

| Phương án | Bị bỏ sót bởi | Phát hiện bởi | Ảnh hưởng |
|---|---|---|---|
| Phản hồi của Ủy ban châu Âu ngày 16/06/2026 (IP/26/1369) với ECI về game | C | A, B | Làm mạnh bằng chứng chính sách cho cụm game |
| EU Data Act (09/2025) | B, C | A | Cơ sở pháp lý tiềm năng cho cụm "cửa sổ đóng cửa"; WTP vẫn tranh chấp |
| Trình xem archive Mastodon | A | C | Phủ một phần A-O2 |
| Baseline giải mã có lập trình: `m2c` + `decomp-permuter` | B (B-O5 thiếu baseline) | A, C | AI ở B-O5 phải vượt baseline này mới gọi là chịu tải |
| WACZ 1.1.1 | B | A | Định dạng chuẩn cho bản lưu phát lại được |

Phản biện chéo đã thay đổi đánh giá khoảng trống ở ít nhất bốn cơ hội: A-O2, A-O3, B-O5 và C-O2.

## 3. AI so với kỹ thuật thông thường

Kết luận sau Round 2 (nguồn: §7 báo cáo và §3–4 cross-review):

| Cơ hội | AI ở Round 1 | AI sau Round 2 | Phương án thông thường cạnh tranh |
|---|---|---|---|
| A-O2 (tái dựng ngữ nghĩa gói export) | load-bearing | **useful** (A tự hạ) | Parser viết tay theo tài liệu export (B) |
| A-O3 (tìm môi trường chạy phần mềm cũ) | load-bearing | **useful** (A tự hạ) | Quét tất định emulator × OS × kiểm tra boot (B) |
| B-O5 (giải mã khớp byte) | load-bearing | **load-bearing, chỉ ở mức giả thuyết** | `m2c` + `decomp-permuter` (A, C) |
| Cụm game (A-O4, B-O1, C-O2) | unnecessary / useful | unnecessary (A, C), useful (B) | Chuẩn kỹ thuật và quy trình end-of-life, pháp lý |
| Tạp chí (C-O1, B-O3) | unnecessary | unnecessary | Plugin PKP PN, manifest diff |

**Kết luận:** sau phản biện, **không còn cơ hội nào có AI chịu tải đã được chứng minh**. Ứng viên duy nhất (B-O5) cần benchmark lặp lại có baseline mới xác định được.
