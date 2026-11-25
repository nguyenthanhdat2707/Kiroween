# Lớp hiệu chỉnh: nhãn claim và metadata

Báo cáo gốc của agent **không bị sửa**. Bảng dưới đề xuất nhãn hiệu chỉnh và giữ nhãn gốc bên cạnh. Khi Phase 2 trích dẫn một claim có trong bảng này, cần dùng nhãn hiệu chỉnh và ghi cả nhãn gốc.

Quy tắc áp dụng theo brief Phase 1 §5.1: ĐÃ XÁC MINH cần nguồn chính cộng xác nhận độc lập, hoặc phép kiểm tái lập được. Claim có phần dữ kiện đạt chuẩn và phần diễn giải không đạt được **tách đôi**, không hạ toàn bộ.

## 1. Nhãn claim trong shortlist

| Claim | Nhãn gốc | Nhãn hiệu chỉnh | Lý do |
|---|---|---|---|
| A-P1-C2 | VERIFIED | **Tách:** VERIFIED cho hai số liệu (Reuters: 54% so với 51%, lần đầu; Pew: 52% "worn out") / **INFERENCE** cho "quá tải thông tin … gia tăng 2025–2026" và việc áp vào nhóm người theo dõi chuyên môn | Nguồn đo kênh tiếp cận và mệt mỏi tin tức ở Mỹ, không đo quá tải của nhóm người dùng mục tiêu |
| A-P2-C2 | VERIFIED | **Tách:** VERIFIED cho thương vụ SAP–WalkMe (05/06/2024) và sự tồn tại của TipKit / **INFERENCE** cho "giá trị kinh tế rất lớn" và "Apple phải giới thiệu TipKit" | Thương vụ là dữ kiện; quy mô giá trị và động cơ của Apple là diễn giải |
| A-P7-C2 | VERIFIED / INFERENCE | Giữ. **Sửa trình bày:** 30.903 người trả lời toàn khảo sát; n=16.985 cho câu hỏi về việc dùng Stack Overflow | Hai con số khác mẫu, không mâu thuẫn |
| B-P4-C1 | ĐÃ XÁC MINH | **Tách:** ĐÃ XÁC MINH cho việc lab giữ PC chạy OS EOL để điều khiển thiết bị (Nature 2021 + UW–Madison 2024) / **SUY LUẬN** cho chi phí 10.000 USD và các chi tiết XP/eBay như mô tả hiện tại | Con số chỉ có một nguồn, năm 2021 |
| B-P4-C2 | ĐÃ XÁC MINH | Giữ, **thu hẹp phạm vi:** "Khoa Hóa UW–Madison mô tả …" | Một nguồn chính thức về thực hành của chính khoa đó; không đại diện cho các lab khác |
| B-P1-C5 | ĐÃ XÁC MINH (về việc bài báo báo cáo) | Giữ. Ghi rõ kết quả **chưa tái lập độc lập** | B đã tự giới hạn phạm vi đúng |

Claim trong shortlist được giữ nguyên nhãn sau khi kiểm (xem `claim-verification.md`):

- A-P1-C1, A-P4-C1 (phần Pocket), A-P4-C2, A-P7-C1 (đã tái lập qua API);
- B-P1-C1, B-P1-C2;
- C-P1-C1, C-P4-C1 (qua nguồn chính phủ thay thế), C-P4-C2.

Claim có nhãn gốc **thận trọng hơn** mức nguồn cho phép: B-P1-C4, C-P4-C3. Coordinator **không nâng** nhãn. Tăng nhãn không thuộc yêu cầu và để Phase 2 quyết.

Chưa kiểm, giữ nhãn gốc kèm cờ "chưa kiểm": C-P4-C4 (nguồn 403), phần Del.icio.us của A-P4-C1.

## 2. Nhãn claim ngoài shortlist (mang từ Phase 1, chưa kiểm lại)

| Claim | Nhãn gốc | Đề xuất | Căn cứ |
|---|---|---|---|
| B-P3-C1 | ĐÃ XÁC MINH | SUY LUẬN | Một nguồn chính; xác nhận độc lập chỉ là snippet |
| B-P5-C1 | ĐÃ XÁC MINH | SUY LUẬN | Như trên |
| B-P6-C3 | ĐÃ XÁC MINH (Kagi) | Giữ cho Kagi; các webring khác vẫn SUY LUẬN như B ghi | B đã tự tách |
| B-P6-C1 | ĐÃ XÁC MINH | Cần kiểm | Một nguồn, chưa có xác nhận độc lập |

## 3. Metadata thực thi

Tham số lấy từ `/proc/<pid>/cmdline` của tiến trình worker trong Phase 1.

| Agent | Agent tự khai | Thực tế |
|---|---|---|
| A | Gemini 4 Neon (High), effort high; 08:02:21Z → 08:22:30Z | Khớp: `agy --model gemini-4-neon-high` (effort nằm trong hậu tố model), qua `agy-api.sh` |
| B | `claude-sonnet-5-5`; effort "thấp–trung bình, brief không quy định"; bắt đầu "~07:55 UTC (ước lượng)" | `claude --model claude-sonnet-5-5 --effort high`; tiến trình bắt đầu **08:02:16Z**; tệp ghi xong 08:11Z |
| C | Model "CHƯA RÕ", effort "CHƯA RÕ" | `codex -m gpt-6.1-sol -c model_reasoning_effort=high`; tiến trình bắt đầu 08:02:16Z |

Cả ba worker chạy **không sandbox**:

- Claude: `--dangerously-skip-permissions`;
- Codex: `--dangerously-bypass-approvals-and-sandbox`;
- agy: `toolPermission = always-proceed`.

## 4. Thay đổi tệp không do agent

- `agent-c/discovery.md` bị sửa lúc 15:47 (UTC+7), sau khi C báo xong. Kích thước tăng từ 42.669 lên 53.676 byte, số dòng và mọi mã claim/URL không đổi. Nếu gộp các chuỗi khoảng trắng, kích thước còn 42.691 byte.
- `human/phase-1-decision-brief.md` cũng bị đệm khoảng trắng trong bảng, vào lúc 16:31.
- SUY LUẬN: đây là định dạng lại bảng chỉ bằng khoảng trắng, nhiều khả năng do Obsidian. Không có thay đổi nội dung.
