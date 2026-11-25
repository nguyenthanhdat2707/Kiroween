# Phase 1.5 — Targeted Quality Gate

- Run: `2026-11-25-phase1-discovery`. Ngày: 25/11/2026.
- Người thực hiện: **chỉ Coordinator** (`claude-sonnet-5-5`). Đây là option (a), do người dùng chọn sau khi kiểm tra an toàn thực thi thất bại. Xem mục 1.
- Phạm vi: 8 problem space trong shortlist của người dùng.
- Phase 1.5 **không loại, không xếp hạng và không chọn** ứng viên. Phase 2 chưa bắt đầu.

## Tệp trong thư mục này

| Tệp | Nội dung |
|---|---|
| `human-shortlist.md` | Shortlist nguyên văn của người dùng, ghi là phán đoán của người, chưa được kiểm chứng |
| `overlaps.md` | Chỗ trùng giữa các ứng viên trong shortlist |
| `claim-verification.md` | Kiểm tra claim quyết định và giải quyết mâu thuẫn |
| `calibration.md` | Hiệu chuẩn điểm reference trên một bộ anchor chung |
| `corrections-overlay.md` | Sửa nhãn ĐÃ XÁC MINH và metadata, dưới dạng lớp phủ |
| `data/` | Điểm anchor dạng JSON và script tính offset |

Tài liệu cho người đọc: `../human/phase-1.5-decision-brief.md`. Bản Phase 1 trong `../human/phase-1-decision-brief.md` được giữ nguyên.

## Nguyên tắc bảo toàn

- **Không sửa** `../agent-{a,b,c}/discovery.md`. Mọi chỉnh sửa nằm ở `corrections-overlay.md` và trỏ về mã claim gốc.
- Phản chứng và nhãn bất định của agent được giữ nguyên. Khi Coordinator đề xuất nhãn khác, cả hai nhãn được ghi cạnh nhau.
- Nguồn tải về được lưu tạm trong scratchpad, không đưa vào thư mục dự án.

## 1. Kiểm tra an toàn thực thi trước khi dùng worker

Kết luận: **không thể thiết lập thực thi an toàn cho worker**, nên không khởi chạy worker nào.

| Bằng chứng | Mức chứng cứ |
|---|---|
| Orca `agentPermissionDefault = "full-access"`, `agentPermissionOverrides = {"antigravity": "own"}` (trong `profile-state.db`) | Confirmed |
| Phase 1 worker chạy với `--dangerously-skip-permissions` (Claude), `--dangerously-bypass-approvals-and-sandbox` (Codex), `toolPermission = always-proceed` (agy) | Confirmed (`/proc/<pid>/cmdline`) |
| `orchestration worker-start` và `agent launch` không có cờ sandbox hay permission cho từng lần khởi chạy | Confirmed (`--help`) |
| Sandbox tốt nhất khả dụng nếu siết cài đặt là Codex `workspace-write`, chỉ giới hạn ở cả workspace `Kiroqeen/`, không theo thư mục từng agent | Inferred |

Phiên Coordinator cũng chạy ở chế độ bỏ qua quyền. Khác biệt duy nhất: mọi lệnh hiển thị trực tiếp cho người dùng.

## 2. Giới hạn của Phase 1.5

- **Một người chấm.** Hiệu chuẩn dùng Coordinator làm người chấm tham chiếu, không phải đồng thuận nhiều người. Coordinator dùng cùng model với Agent B, nên có rủi ro thiên lệch về phía B.
- **Ít cặp trùng nguồn.** Chỉ có **một** cặp claim–source trùng thật giữa hai agent (Pew link rot: A·R21 và B·R20). Cặp Reuters của C nằm trong danh sách lỗi, không được chấm.
- **Kiểm có chọn lọc.** Chỉ claim quyết định của 8 space shortlist được kiểm. Các space ngoài shortlist chỉ mang theo phát hiện từ Phase 1, không kiểm lại.
- **Nguồn bị chặn.** Hai nguồn của C (Commons Library CBP-9471, Ofcom "landline going digital") trả 403 với Coordinator. Claim liên quan được đối chiếu qua nguồn chính phủ khác nếu có.
