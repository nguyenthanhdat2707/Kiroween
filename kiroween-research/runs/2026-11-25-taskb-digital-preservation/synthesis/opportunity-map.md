# Bản đồ cơ hội — Task B

Nguồn:

- [`opportunities-revised.json`](../agent-a/opportunities-revised.json) của từng agent;
- §10 trong `report.md`, §5 trong `cross-review.md`;
- bảng bằng chứng rubric: [`data/rubric-evidence-table.md`](data/rubric-evidence-table.md).

**Không xếp hạng.** Các cụm **không** được so với ứng viên Phase 2 (B-P1, A-P4, vị trí thứ 3). Điểm "tạm thời" là tóm tắt bằng chứng do agent tự chấm theo anchor Phase 2, không phải điểm tổng hợp. Điểm của A có xu hướng rộng tay (Phase 1.5: +8; Task B: international 5H ở hầu hết cơ hội).

## 1. Các cụm sau phản biện chéo

13 cơ hội ban đầu (A 5, B 5, C 3) gom thành 7 mục:

- 5 cụm có đề xuất gộp từ chính các agent;
- 2 cơ hội đứng riêng.

Đã rút: A-O5 (gộp vào C-O3) và B-O3 (gộp vào C-O1).

| Cụm | Thành viên | Ai đề xuất gộp | Dải điểm `theme` tạm thời | Rủi ro cổng chủ đề (≥3) |
|---|---|---|---|---|
| **T1 · Kết thúc vòng đời game live-service** | A-O4, B-O1, C-O2 | **Cả ba** | 4 / 4 / 5 | Thấp |
| **T2 · Cửa sổ đóng cửa của nền tảng nhỏ/SaaS** | A-O2, B-O2 | A | 3 / 3 | Trung bình |
| **T3 · Hồ sơ học thuật của tạp chí nhỏ** | C-O1 (gộp B-O3); A-O1 liền kề | B, C | 1 (C-O1); A-O1: 3 | **Cao**: tự C chấm 1 |
| **T4 · Chuyển giao kho di sản giữ quyền/ngữ cảnh** | C-O3 (gộp A-O5) | A, B | 1 | **Cao**: A rút A-O5 vì trượt cổng; C chấm 1 |
| **T5 · Tái dựng hoặc chạy lại phần mềm bị bỏ rơi** | B-O5, A-O3 | (không ai đề xuất gộp; Coordinator nhóm theo chiều "software") | 3 / 5 | Thấp–trung bình |
| **S1 · Di sản nền tảng vùng đã chết** (keitai Nhật, web Trung Quốc thời đầu, Mxit) | B-O4 | — | 5 | Thấp |
| **S2 · Tĩnh hóa web app học thuật sau grant** | A-O1 | — (A giữ độc lập) | 3 | Trung bình |

## 2. Từng cụm: bằng chứng mạnh nhất, phản chứng mạnh nhất, bất đồng

### T1 · Kết thúc vòng đời game live-service

- **Ba cách đặt vấn đề khác nhau** (đã được ghi nhận, không gộp nội dung):
  - A: quản trị kết thúc và bàn giao cho cộng đồng **phía nhà phát hành**;
  - B: **thu trace trước khi server tắt**;
  - C: **kế nhiệm maintainer** của đội hồi sinh.
- **Bằng chứng mạnh nhất:**
  - 1.294.188 chữ ký ECI đã xác nhận;
  - phản hồi EC ngày 16/06/2026: **từ chối nghĩa vụ pháp lý** giữ game chơi được, nhưng **cam kết code of conduct** cho end-of-life. B mở trực tiếp; A-O4-C1 được B xác nhận;
  - Homecoming (license NCSoft, quyên góp hằng tháng) và Pretendo (170 repo).
- **Phản chứng mạnh nhất:**
  - IP và DMCA §1201; nhà phát hành (ESA) phản đối;
  - AI: unnecessary theo A và C;
  - feasibility tạm thời 1–3; sustainability 1–3.
- **Bất đồng còn lại:** nút thắt chính là pháp lý (A, sustainability 1) hay thiếu chuẩn kỹ thuật end-of-life (B, sustainability 3). Có studio nào tự nguyện cam kết sau phản hồi EC không: CHƯA RÕ.

### T2 · Cửa sổ đóng cửa của nền tảng nhỏ/SaaS

- **Bằng chứng mạnh nhất:**
  - Cohost (thâm hụt ~17.000 USD/tháng) và Glitch: ArchiveTeam cần nhà vận hành hợp tác (`B-O2-C3`);
  - EU Data Act 09/2025 (A).
- **Phản chứng mạnh nhất:**
  - AI unnecessary theo B; A tự hạ xuống "useful";
  - đã có trình xem archive Mastodon và DTI/DTP;
  - không tìm thấy WTP của nhà vận hành.
- **Bất đồng còn lại:** Data Act có tạo WTP cho công cụ tái dựng gói export không (A), hay chỉ làm các nền tảng lớn tự xây importer (B, C).

### T3 · Hồ sơ học thuật của tạp chí nhỏ

- **Bằng chứng mạnh nhất:**
  - Laakso: 174 tạp chí OA biến mất giai đoạn 2000–2019;
  - Eve: 27,64% DOI không xác nhận được bảo tồn (`C-G-C1`: hai mẫu và định nghĩa khác nhau, không suy ra tỷ lệ đã mất).
- **Phản chứng mạnh nhất:**
  - hạ tầng đã có (PKP PN miễn phí, CLOCKSS, Portico); vấn đề là **tham gia**;
  - **theme 1**, vì tạp chí không phải "dead technology";
  - AI unnecessary.
- **Bất đồng còn lại:** là vấn đề tham gia thuần túy (B-O3), hay còn tổn thất tính đầy đủ khi bàn giao (C-O1).

### T4 · Chuyển giao kho di sản giữ quyền và ngữ cảnh

- **Bằng chứng mạnh nhất:**
  - Mukurtu có roles và cultural protocols;
  - ELDP/ELAR đổi đơn vị chủ trì; PARADISEC có bản offline;
  - Kulu Language Institute (Ranongga).
- **Phản chứng mạnh nhất:**
  - **theme 1**: A rút A-O5 vì trượt cổng;
  - nút thắt có thể là nhân sự và governance, không phải công cụ (C, cross-review);
  - legal high.
- **Bất đồng còn lại:** cần thêm tooling hay chủ yếu cần governance.

### T5 · Tái dựng hoặc chạy lại phần mềm bị bỏ rơi

- **Bằng chứng mạnh nhất:**
  - B-O5: benchmark giải mã có hỗ trợ LLM (nguồn B; chưa tái lập độc lập);
  - A-O3: A ghi demand "demonstrated" ở tổ chức;
  - US Copyright Office, khuyến nghị §1201 (`A-O3-C3`, B xác nhận).
- **Phản chứng mạnh nhất:**
  - **baseline `m2c` + `decomp-permuter`** (A, C);
  - EaaSI và quét tất định cho A-O3;
  - demand B-O5 **hypothetical**, chỉ có bằng chứng ở NA.
- **Bất đồng còn lại:** AI có tạo cải thiện đo được so với công cụ cổ điển không (B so với A/C).

### S1 · Di sản nền tảng vùng đã chết (B-O4)

- **Bằng chứng mạnh nhất:**
  - Kahvibreak / Keitai Wiki: brute-force CPRM, ktdumper, desolder eMMC. Đây là bằng chứng hành vi mạnh **ở châu Á**.
  - "No comprehensive emulator", mỗi nhà mạng một nền tảng (i-mode DoJa, EZweb BREW, SoftBank MIDP).
- **Phản chứng mạnh nhất:**
  - legal high (DRM, CPRM);
  - feasibility 2;
  - người dùng chủ yếu là cộng đồng bảo tồn kỹ năng cao, không phải đại chúng.
- **Giới hạn bằng chứng:** không tìm thấy bằng chứng cho Việt Nam (B, Round 1).

### S2 · Tĩnh hóa web app học thuật sau grant (A-O1)

- **Bằng chứng mạnh nhất:** A ghi demand "demonstrated" và bằng chứng ở NA, EU, châu Á. Nhãn đã bị A hạ phần lớn ở Round 2.
- **Phản chứng mạnh nhất:** Wren 2017 (A §11.2): tài nguyên được trích dẫn nhiều phần lớn tự sống sót. B yêu cầu bằng chứng 2025–2026 rằng nhóm nghiên cứu hoặc thư viện **hành động**.
- **Bất đồng còn lại:** tỷ lệ web app tĩnh hóa được mà không mất công năng là bao nhiêu (thí nghiệm bác bỏ của A).

## 3. Quan hệ với ứng viên Phase 2 (mô tả, không xếp hạng)

| Cụm Task B | Liên quan Phase 2 | Ghi chú |
|---|---|---|
| T1 (game) | B-P1 (thiết bị bị brick) | Cùng cơ chế "server tắt thì sản phẩm đã mua chết"; T1 có bằng chứng chính sách EU mạnh hơn, B-P1 có cơ chế AI (HotNets '26) rõ hơn |
| T2 (cửa sổ đóng cửa) | A-P4 (link rot, Pocket) | Cùng vùng "nội dung người dùng khi dịch vụ đóng" |
| T5, S1 | — | Không có tương đương trong Phase 2 |

Gộp hay so với Phase 2 là quyết định của anh/chị (Exit Gate).
