# Hiệu chuẩn điểm reference

Dữ liệu gốc: `data/calibration-anchor-scores.json`. Script tính: `data/calibration-anchor-scores.py`.

## 1. Vì sao không làm được hiệu chuẩn bằng cặp trùng

Yêu cầu ban đầu là hiệu chuẩn bằng các cặp claim–source giống hệt nhau giữa các agent. Trên 94 reference được chấm:

- **A và B:** trùng 1 URL (Pew, "When Online Content Disappears"), dùng cho hai claim gần nhau (`A-P4-C2`, `B-P6-C2`).
- **A và C:** trùng 1 URL (Reuters DNR 2026). C ghi nguồn này là lỗi truy cập và không chấm.
- **B và C:** không trùng URL nào.

Một cặp không đủ để hiệu chuẩn ba người chấm. Coordinator thay bằng **bộ anchor chung**: 22 cặp claim–source trong 8 space shortlist. Coordinator chấm lại cả 22 cặp bằng một rubric với định nghĩa mốc viết sẵn, rồi tính độ lệch của từng agent so với Coordinator.

## 2. Định nghĩa mốc Coordinator dùng (thang 0–5)

| Tiêu chí | 5 | 4 | 3 | 2 | 1–0 |
|---|---|---|---|---|---|
| Authority | Nguồn gốc: tài liệu chính thức, chính phủ, tác giả gốc, peer-reviewed | Tổ chức nghiên cứu lớn; workshop paper | Báo chuyên ngành đưa lại nguồn gốc | Blog có lợi ích, trang SEO | Ẩn danh, không rõ |
| Technical Evidence | Dữ liệu đo, phương pháp công bố | Dữ kiện cụ thể (ngày, giá, số) từ nguồn gốc | Dữ kiện cụ thể qua nguồn thứ cấp | Mô tả định tính | Ý kiến, không có |
| Mechanism | Cơ chế được giải thích **và** kiểm | Giải thích rõ, hoặc claim thuần dữ kiện được nêu trực tiếp | Một phần claim là diễn giải vượt nguồn | Cơ chế yếu | Sai hoặc không có |
| Context Fit | Cùng nhóm người, thời điểm, phạm vi với claim | Gần, lệch nhẹ | Khác nhóm hoặc khác quốc gia | Khác đáng kể | Không liên quan |
| Freshness | Claim "vẫn còn" có nguồn 2025–2026; claim lịch sử có nguồn cùng thời | 2024 | 2023 | 2022 | ≤ 2021 cho claim hiện tại |
| Reproducibility | Dữ liệu hoặc API công khai, tài liệu chính thức lưu trữ được | Trang công khai ổn định | Bài báo | Bị chặn hoặc paywall | Không kiểm lại được |
| Bias (cao = ít thiên lệch) | Không có lợi ích liên quan | Tổ chức mô tả chính sách của mình một cách trung tính | Vendor nói về sản phẩm của mình; tài liệu vận động | Trang marketing | Quảng bá mạnh |

## 3. Kết quả

Offset = điểm weighted của agent − điểm weighted của Coordinator, cho cùng cặp claim–source.

| Agent | Số anchor | Offset trung bình | Trung vị | Khoảng | Tiêu chí lệch nhiều nhất (trung bình điểm agent − Coordinator) |
|---|---|---|---|---|---|
| A | 9 | **+8,0** | +9 | +1 → +16 | Mechanism +0,78; Reproducibility +0,78; Context Fit +0,56 |
| B | 7 | **−5,1** | −5 | −15 → +3 | Technical Evidence −0,57; Bias −0,43 |
| C | 6 | **−0,3** | 0 | −8 → +4 | Reproducibility −0,67; Mechanism +0,50 |

### Cặp cùng nguồn (bằng chứng hiệu chuẩn trực tiếp)

| Cặp | Điểm agent | Điểm Coordinator |
|---|---|---|
| A·R21 (Pew link rot, cho `A-P4-C2`) | 98 | 95 |
| B·R20 (cùng nguồn, cho `B-P6-C2`) | 88 | 95 |

Cùng một nguồn, A và B chấm cách nhau 10 điểm. B chấm thấp hơn ở Mechanism (4 so với 5) và Context Fit (3 so với 4).

### Kiểu lệch quan sát được

- **A** chấm cao cho tài liệu vendor và blog: A·R22 Raindrop help +10, A·R39 MACCUS +16. A chấm Mechanism và Context Fit cao khi claim diễn giải vượt nguồn (A·R05, A·R06, A·R12).
- **B** chấm thấp Technical Evidence cho bài báo đưa lại nguyên văn ngày và số của nhà sản xuất. Ví dụ B·R02 MacRumors về Car Thing được B chấm 2/5 Technical Evidence, nên tổng thấp hơn Coordinator 15 điểm.
- **C** gần Coordinator nhất. C chấm Reproducibility thấp hơn cho thông cáo báo chí (C·R25: 2 so với 4).

## 4. Cách dùng

- **Không** sửa điểm trong báo cáo gốc. Bảng trên là lớp hiệu chỉnh.
- Khi so điểm reference giữa agent ở Phase 2, có thể trừ offset trung bình (A −8, B +5, C 0) như một hiệu chỉnh thô. Hiệu chỉnh này dựa trên 6–9 anchor mỗi agent và một người chấm, nên chỉ đủ cho so sánh xu hướng, không đủ cho quyết định dựa trên chênh lệch vài điểm.
- **Thiên lệch người chấm:** Coordinator chạy cùng model với Agent B (`claude-sonnet-5-5`). Offset của B có thể bị đánh giá thấp so với thực tế. Muốn hiệu chuẩn thật cần ít nhất một người chấm khác model, hoặc người dùng chấm một phần bộ anchor.
