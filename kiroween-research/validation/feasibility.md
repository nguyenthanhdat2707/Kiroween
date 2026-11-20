# Khả thi và kế hoạch kiểm chứng nhỏ nhất

Đây là bước **nghiên cứu**, chưa triển khai dự án. Nhóm 1–3 sinh viên, ngân sách thấp, demo <3 phút. Hạng mục 2026 yêu cầu app chạy được và nếu dùng phần cứng ít phổ biến có thể phải cấp quyền tiếp cận thiết bị cho giám khảo [Rules](https://kiroween.devpost.com/rules).

| Mã | Giả định lớn; bất định kỹ thuật | Dữ liệu/phần cứng, demo nhỏ nhất | Tiếp tục nếu… / Loại nếu… |
|---|---|---|---|
| C20 | Thư viện nhỏ có thẻ chưa số hóa và cần tra cứu; OCR ảnh thẻ | 20 ảnh thẻ được cấp quyền; demo tìm tên → ảnh thẻ, bản chép được sửa, vị trí ngăn | Thủ thư chỉ ra ca tìm thất bại thực và xác nhận tiết kiệm công; loại nếu catalog hiện có đủ hoặc workflow OCR đang dùng làm được. |
| C07 | Gia đình đã chuyển băng vẫn thiếu ngữ cảnh; canh mốc thời gian/nhãn băng | 1 video đã chuyển + ảnh hộp có quyền; demo nhấp nhãn → đoạn đúng | 3/5 gia đình kể tình huống tìm đoạn khó và thích quy trình; loại nếu album hiện tại đáp ứng. |
| C13 | Cựu blogger còn file xuất và muốn đọc lại bình luận; parser HTML/zip có nhiều biến thể | Ít nhất 2 file xuất thật của chủ sở hữu; demo nhập → bài/bình luận riêng tư | Chủ dữ liệu xác nhận giá trị và parser giữ nội dung đúng; loại nếu không lấy được file hoặc WordPress import đủ. |
| C09 | Người không chuyên có disk image và muốn hiểu nội dung; chuyển định dạng | 2 disk image được phép dùng; demo từ image → danh sách → mở 1 tệp và provenance | Người dùng không làm được với FloppoScope/BitCurator nhưng làm được với luồng mới; loại nếu chỉ là explorer khác. |
| C18 | Gõ/sửa chương trình cũ giúp học hơn IDE hiện hành; đo kết quả học | 1 listing BASIC được phép dùng; demo lỗi gõ → suy luận → sửa → chạy | Giáo viên chỉ ra mục tiêu học và thử nhỏ cho hiệu quả; loại nếu PICO-8/giấy bài tập đạt như nhau. |

Với C08/C01/C03/C25, điều tra thêm người dùng trước khi cân nhắc demo. C08 cần audio/giấy phép; C01 cần nhóm khu phố thực; C03 cần dữ liệu dịch vụ công; C25 cần một thư viện có backlog OCR chưa giải quyết.
