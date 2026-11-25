# Chỗ trùng giữa các ứng viên trong shortlist

Mô tả chỗ trùng, không gộp và không chọn. Việc gộp hay tách thuộc Phase 2 và cần phê duyệt.

## O1 · A-P1 và C-P1: theo dõi và tổng hợp nhiều nguồn

| | A-P1 | C-P1 |
|---|---|---|
| Công nghệ mỏ neo | Yahoo! Pipes (2007–2015) | Google Reader (2005–2013) |
| Người dùng | Nhà nghiên cứu, nhà báo, người theo dõi nguồn chuyên biệt | Người theo dõi tin chuyên ngành, nhóm nghiên cứu nhỏ |
| Việc cốt lõi | **Lắp ráp** đường ống: lấy nguồn không có RSS, lọc ngữ nghĩa | **Đọc**: không đọc lặp cùng sự kiện, thấy phần mới |
| Vai trò AI theo agent | Trích xuất tự sửa khi trang đổi cấu trúc; lọc ngữ nghĩa | Nhận diện phần **thay đổi** giữa các bản tin, vượt rule/hash (`C-P1-C7`) |
| Đối thủ chung | Feedly (A: Leo AI; C: AI dedup `C·R04`) | Feedly, Inoreader (`C·R05`) |

- **Trùng:** cùng nhóm người dùng, cùng đối thủ chính (Feedly).
- **Khác:** A nhắm đầu vào (lấy và lọc nguồn); C nhắm đầu ra (trình bày điều mới). Hai hướng có thể là hai tầng của cùng một luồng, nhưng đó là SUY LUẬN của Coordinator.
- **Chi tiết chưa kiểm:** A nói tính năng AI của Feedly bị khóa ở bản miễn phí; C không nêu giá. Coordinator chưa kiểm bảng giá Feedly.

## O2 · B-P1 và B-P4: cùng cơ chế suy giao thức bằng AI từ trace

| | B-P1 | B-P4 |
|---|---|---|
| Đối tượng | Chủ thiết bị tiêu dùng bị brick | Phòng thí nghiệm có thiết bị khoa học |
| Oracle (phần mềm gốc còn chạy để so hành vi) | Có trước ngày tắt; AirPort Utility vẫn chạy trên OS cũ | Có: PC cũ vẫn chạy phần mềm gốc |
| Bằng chứng cơ chế | `B·R01` (HotNets '26) trực tiếp | `B-P4-C4`: GIẢ THUYẾT chuyển giao từ `B·R01` |

- **Phụ thuộc chung:** cả hai dựa vào một nguồn cơ chế duy nhất (`B·R01`). Bài này tự ghi là chưa chứng minh tổng quát hóa và đã tiêu tốn "billions of model tokens". Nếu phương pháp không tái lập được trong khung thời gian hackathon, cả hai space bị ảnh hưởng cùng lúc.
- B-P2 (ngoài shortlist) cũng dựa vào cơ chế này.

## O3 · A-P4 và hai space ngoài shortlist (A-P6, B-P6): phát hiện link rot "mềm"

- A-P4 đề xuất AI nhận diện trang vẫn trả HTTP 200 nhưng đã thành trang đỗ hoặc spam. A-P6 và B-P6 đề xuất cùng cơ chế cho danh mục và webring.
- Cả ba dùng cùng nghiên cứu Pew về link rot (`A·R21` = `B·R20`).
- Coordinator ghi nhận để Phase 2 không nghiên cứu cùng cơ chế ba lần.

## O4 · A-P7 và A-P3 (ngoài shortlist): tri thức kỹ thuật công khai bị dời vào kênh riêng

- A-P7: lời giải lỗi biên nằm trong chat AI riêng. A-P3: tri thức hỗ trợ nằm trong Discord/Slack.
- Cùng vấn đề gốc là tri thức không còn công khai và tìm kiếm được, nhưng khác nguồn dữ liệu và khác đối thủ.

## Không trùng đáng kể

- **A-P2** (coachmark bám trạng thái UI) không trùng với ứng viên nào khác trong shortlist.
- **C-P4** (telecare) không trùng với ứng viên nào khác. Đây cũng là space duy nhất trong shortlist mà agent đề xuất tự ghi **AI không bắt buộc** (`C-P4-C7`).
