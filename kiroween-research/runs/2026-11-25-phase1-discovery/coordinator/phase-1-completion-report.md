# Báo cáo hoàn tất Phase 1 — Independent Discovery

- Run: `2026-11-25-phase1-discovery` · Orca run `run_d6dac92308e5` · Coordinator: Claude Code (`claude-sonnet-5-5`)
- Ngày: 25/11/2026. Báo cáo này **không gộp, không xếp hạng, không chọn ý tưởng** (theo chỉ dẫn Phase 1 §7).
- Trạng thái: **Phase 1 HOÀN TẤT — dừng tại Exit Gate, chờ phê duyệt.**

## 1. Tham số thực thi thực tế

Tham số model và effort được kiểm từ `/proc/<pid>/cmdline` của tiến trình đang chạy. Không lấy từ lời tự khai của agent.

| Agent | Tiến trình thực tế | Bắt đầu → báo xong (UTC) | Dispatch | Kết quả Orca |
|---|---|---|---|---|
| A | `agy --settings ~/.config/orca/agy-api.json --model gemini-4-neon-high` (qua `agy-api.sh`) | 08:02 → ~08:22 | ctx_72ffe508bed3 | succeeded |
| B | `claude --dangerously-skip-permissions --model claude-sonnet-5-5 --effort high` (qua `claude-pro.sh`) | 08:02 → ~08:12 | ctx_ebd802ca515e | succeeded |
| C | `codex --dangerously-bypass-approvals-and-sandbox -m gpt-6.1-sol -c model_reasoning_effort=high` | 08:02 → ~08:12 | ctx_c26d22fcc8a6 | succeeded |

- Không có lỗi launch nào ở Phase 1. Cả ba `worker-start` trả exit 0. Cả ba báo `worker_done` với outcome succeeded.
- **Cả ba agent chạy không sandbox và không cần phê duyệt.** Cách ly workspace chỉ dựa vào chỉ dẫn trong prompt, không phải cơ chế bảo mật thực thi.

## 2. Kiểm tra cấu trúc deliverable

| Kiểm tra | A | B | C |
|---|---|---|---|
| `discovery.md` tồn tại | ✅ 94,6 KB | ✅ 49,7 KB | ✅ 42,7 KB |
| Đủ 12 heading bắt buộc, đúng thứ tự | ✅ | ✅ | ✅ |
| Số problem space (mục tiêu 4–8) | 7 | 6 | 4 (cận dưới) |
| Problem space mới / xem lại (yêu cầu ≥ 50% mới) | 6 mới / 1 xem lại | 5 mới / 1 xem lại một phần | 4 mới |
| Claim có ID | 28 | 38 | 32 |
| Reference được chấm rubric | 45 | 22 (+14 snippet không chấm) | 27 (+3 không mở được) |
| Viết tiếng Việt | ✅ | ✅ | ✅ |
| Nhãn claim | Cả nhãn Anh và Việt | Nhãn Việt (tương đương 1–1 theo brief) | Nhãn Việt |
| Mục 8 (Challenged assumptions A1–A5) | ✅ | ✅ | ✅ |
| Không xếp hạng / chọn ý tưởng | ✅ | ✅ | ✅ |

## 3. Vi phạm chỉ dẫn và cách ly

| Kiểm tra | Kết quả | Mức chứng cứ |
|---|---|---|
| Ghi ra ngoài `agent-<x>/` | Không phát hiện. Mọi tệp đổi sau launch ngoài thư mục agent đều do Coordinator viết trước launch. | ĐÃ XÁC MINH (`find -newer`) |
| Đọc thư mục agent khác hoặc `_preflight` | Không phát hiện trong transcript. Lần nhắc `_preflight` duy nhất là chính dòng cấm trong spec của A. | SUY LUẬN: transcript Orca có thể không đầy đủ, nên không chứng minh tuyệt đối |
| Sửa `progress/`, `ideas/`; commit/push | Không | ĐÃ XÁC MINH |
| Chạy mã cộng đồng hoặc cài gói | Không phát hiện. A tự viết script Python kiểm nguồn trong `agent-a/scratch/`, được brief cho phép. | SUY LUẬN |
| **Metadata tự khai sai** | **B** ghi effort "thấp–trung bình, brief không quy định" và giờ bắt đầu ~07:55. Thực tế là `--effort high` và 08:02. **C** ghi model/effort "CHƯA RÕ". **A** khai đúng. | ĐÃ XÁC MINH. Coordinator ghi đè bằng tham số thực ở §1 |

## 4. Kiểm tra claim và reference

### 4.1 URL tồn tại

Có 118 URL duy nhất được kiểm bằng curl:

- 105 trả HTTP 200/202 (gồm 10 URL GitHub chỉ timeout ở lượt song song và đạt 200 khi kiểm lại tuần tự);
- 9 trả 403, do site thật chặn bot;
- 1 không phân giải sau hai lần thử: URL knowledgebase.vcu.edu do C trích.

**Không phát hiện URL bịa.**

### 4.2 Số học rubric

94/94 dòng reference có điểm weighted khớp công thức Σ(trọng số × điểm/5), sai lệch ±1.

### 4.3 Hiệu chuẩn điểm giữa các agent khác nhau rõ

| Agent | Median weighted | Min | Số ref đạt 100 | Source Reliability: High / Medium / Low |
|---|---|---|---|---|
| A | 94 | 74 | 3 | 35 / 10 / 0 |
| B | 77 | 58 | 0 | 10 / 11 / 1 |
| C | 86 | 58 | 0 | 18 / 9 / 0 |

Hệ quả là **không thể so điểm reference giữa các agent** nếu chưa hiệu chuẩn lại. A có xu hướng chấm rộng tay.

### 4.4 Kiểm tra mẫu claim then chốt (Coordinator tự kiểm)

| Claim | Kết luận của Coordinator |
|---|---|
| A-P5-C1: InfoPath 2013 và InfoPath Forms Services (SharePoint Online) hết hỗ trợ 14/07/2026 | **Khớp.** Microsoft SharePoint blog, Message Center MC616550 và danh sách Microsoft end-of-support 2026. Riêng phần "xóa khỏi SharePoint SE bằng PU 13/07/2027" chưa được Coordinator kiểm. |
| A-P7-C1: Stack Overflow chỉ 843 câu hỏi tháng 10/2026 | **Chưa tự kiểm lại được.** Stack Exchange API chặn rate-limit IP của Coordinator. Nhất quán về độ lớn với nguồn thứ hai A trích (maccus.fr: 969 câu hỏi tháng 9). |
| A-P7-C2: Developer Survey 2026 ">30.000 người" | **Mâu thuẫn chưa giải.** Cùng claim dẫn n=16.985 từ chu kỳ 18. Có thể là tổng người trả lời so với n của một câu hỏi, nhưng A không làm rõ. |
| B-P1: bài HotNets '26 "You Bought It, They Bricked It" | **Khớp.** PDF tồn tại. Hội nghị 16–17/11/2026. Có mô tả AI hỗ trợ reverse engineering giao thức AirPort. |
| B-P1-C2: Apple bỏ AirPort Utility khỏi App Store với iOS 27 | **Khớp.** Bài MacRumors 22/06/2026 tồn tại, tiêu đề đúng. |
| C-P4-C2: Ofcom phạt Virgin Media £23,8 triệu ngày 01/12/2025 vì migration telecare | **Khớp.** Trang Ofcom và nhiều báo độc lập. |

### 4.5 Nhãn ĐÃ XÁC MINH chỉ dựa trên một nguồn

Brief yêu cầu nguồn chính cộng xác nhận độc lập, hoặc kiểm tra tái lập được.

- **B:** 8 claim ĐÃ XÁC MINH chỉ dẫn một reference: B-P1-C5, B-P2-C4, B-P3-C1, B-P4-C2, B-P5-C1, B-P6-C1, B-P6-C2, B-P6-C3. B ghi minh bạch loại chứng cứ.
  - Một số có thể chấp nhận vì là văn bản luật hoặc dữ liệu tái lập được (B-P2-C4, B-P6-C2).
  - Một số **nhãn hơi cao**, vì xác nhận độc lập chỉ là snippet (B-P3-C1, B-P5-C1, B-P6-C3) hoặc không có (B-P4-C2, B-P6-C1).
- **A:** A-P3-C1 (Google Groups dừng Usenet 22/02/2024) chỉ dẫn nguồn chính thức của Google. Có thể chấp nhận.
- **C:** không phát hiện trường hợp nào bằng kiểm tra tự động.
- Kiểm tra này dùng heuristic. Định dạng báo cáo khác nhau nên có thể bỏ sót.

## 5. Problem spaces đã nộp (liệt kê, không xếp hạng)

- **A:** Yahoo Pipes (A-P1) · Apple Guide (A-P2) · Usenet/diễn đàn mở so với chat khép kín (A-P3) · Del.icio.us/Pocket và link rot (A-P4) · InfoPath EOL (A-P5) · DMOZ/Webrings (A-P6) · Stack Overflow (A-P7, xem lại)
- **B:** thiết bị bị brick khi tắt cloud (B-P1) · game online bị tắt server (B-P2) · gia phả Hán Nôm (B-P3) · thiết bị khoa học khóa vào OS EOL (B-P4) · định vị không phụ thuộc GNSS (B-P5) · webring/blogroll (B-P6, xem lại một phần)
- **C:** Google Reader/RSS (C-P1) · Flash/SWF (C-P2) · Jamboard (C-P3) · telecare khi rút PSTN tại Anh (C-P4)

Quan sát thuần mô tả, không phải đánh giá: có vùng chủ đề trùng độc lập giữa các agent. Webring/danh mục do người tuyển chọn xuất hiện ở A-P6 và B-P6. Tổng hợp/đọc feed xuất hiện ở A-P1 và C-P1. Việc xử lý chỗ trùng thuộc Phase Cross Review/Synthesis.

## 6. Hạn chế đã biết

- Không agent nào có phỏng vấn hay quan sát người dùng. Mọi nhu cầu hiện tại dựa trên nguồn công khai.
- Tổng cộng ~23 lượt truy cập nguồn thất bại được ghi (A 10, B 10, C 3).
- B và C hoàn tất trong ~10 phút với effort high. Độ sâu kiểm chứng của B và C thấp hơn A, nếu đo bằng số reference.

## 7. Quyết định cần người dùng phê duyệt

1. Phê duyệt kết thúc Phase 1, hoặc yêu cầu agent sửa:
   - B: hạ nhãn các claim ở §4.5 và sửa metadata;
   - A: làm rõ mâu thuẫn A-P7-C2;
   - C: bổ sung model/effort và URL VCU.
2. Hiệu chuẩn lại điểm reference trước khi dùng cho Cross Review hoặc không.
3. Có cập nhật `progress/` theo AGENTS.md cho chu kỳ này hay không. Coordinator chưa sửa, vì Phase 1 cấm gộp.
4. Phase tiếp theo (Deep Research / Cross Review): chưa khởi động.
