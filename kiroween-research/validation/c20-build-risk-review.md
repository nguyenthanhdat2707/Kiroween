# Build Risk Review — C20: thẻ mục lục chưa tra cứu online

**Mode:** Pre-build | **Ngày:** 22/11/2026 | **Skill:** `foundation-build-risk-review`.

## Verdict

**Don't build yet.** C20 có vấn đề thật ở các kho chuyên biệt, nhưng không khớp tiêu chí hiện tại của người dùng (cá nhân/gia đình Mỹ–Âu, nhiều người trực tiếp gặp vấn đề) và hướng OCR/AI đang được các thư viện lớn tự triển khai. Nếu đổi mục tiêu sang công cụ cho thư viện, phải có đối tác và một quy trình chưa được các dự án hiện tại giải tốt. [Luật chấm](https://kiroween.devpost.com/rules) đòi một nhóm người dùng thật và tác động đáng tin, không đặt ngưỡng số người dùng tối thiểu; đây là **tiêu chí chiến lược của người dùng**, không phải yêu cầu loại trừ của cuộc thi.

## Biggest risk

- **R1 demand:** Giả định rằng số lượng lớn thẻ chưa lên mạng đồng nghĩa với lượng lớn người dùng cá nhân gặp vấn đề thường xuyên. Hiện chỉ có bằng chứng về **số tài liệu và nỗ lực cấp tổ chức**, chưa có số lượt tìm kiếm thất bại hoặc người muốn dùng công cụ C20.
- **R2 positioning:** [Berlin](https://lab.sbb.berlin/retrokonversion-katalogkarten-mittels-vision-language-models/?lang=en), [ba thư viện Thụy Điển](https://zenodo.org/records/16037875), [Photothek Florence](https://dhlab.khi.fi.it/blog-digitizing-the-phototheks-card-index/) đều đang theo hướng OCR/AI + cấu trúc metadata + đưa dữ liệu vào catalog; “chụp thẻ, OCR, tìm kiếm” không khác biệt đủ.
- **R3 distribution:** Chưa có thư viện đồng ý chia ảnh thẻ, truy vấn thực, quyền công bố hoặc tích hợp catalog; thiếu các thứ đó, demo khó chứng minh tác động thật.

## Demand level

N/a: ý tưởng trước khi xây.

## Evidence ledger

| Tín hiệu | Độ mạnh | Nó chứng minh được gì? |
|---|---|---|
| [Cambridge](https://www.libraries.cam.ac.uk/collections-and-archives/special-collections/accessing-special-collections/how-find-special) nói một số tài liệu chỉ tìm được bằng tủ thẻ; [Columbia](https://library.columbia.edu/collections/search/search-archives.html) khuyên tra cả catalog online và tủ thẻ | Medium | Vấn đề tìm kiếm tồn tại tại các kho thật; không đo tần suất hoặc tổng số người gặp |
| [Berlin State Library](https://lab.sbb.berlin/retrokonversion-katalogkarten-mittels-vision-language-models/?lang=en) pilot cho khoảng 200.000 thẻ; [LIBER 2025](https://zenodo.org/records/16037875) mô tả ba thư viện Thụy Điển đang làm AI conversion | Strong cho nhu cầu tổ chức; medium cho sản phẩm mới | Các tổ chức thực sự bỏ công giải vấn đề, đồng thời đã có giải pháp nội bộ sát C20; không chứng minh họ sẽ dùng sản phẩm bên ngoài |
| [Photothek Florence](https://dhlab.khi.fi.it/blog-digitizing-the-phototheks-card-index/) có 553.262 thẻ, thí điểm scan/AI/đánh giá | Strong cho quy mô tồn kho; tín hiệu ngược về novelty | Quy mô vật liệu đáng kể, nhưng không phải quy mô người dùng; quy trình đối thủ sâu hơn OCR đơn giản |
| Không có thư viện đối tác, bộ ảnh thẻ được phép, hay truy vấn thất bại do người dùng cung cấp | Weak | Chưa có tín hiệu hành vi trực tiếp cho giải pháp C20 của nhóm |

## Validation plan (không cần xây app)

1. Tìm **một** thư viện/kho chưa hoàn tất chuyển thẻ và xin 20 ảnh thẻ được phép dùng, cùng 5 truy vấn thật từng không ra kết quả trong catalog online. Nếu không có đối tác hoặc dữ liệu có quyền, không chọn C20 cho bài thi.
2. Hỏi nhân viên kho: họ đang dùng OCR/VLM/nhập tay nào; một lượt xử lý mất bao lâu; lỗi nào khiến thẻ không được xuất bản. So kết quả mẫu với quy trình đang dùng. Chỉ đi tiếp nếu nhóm chỉ ra một bước quan trọng làm tốt hơn hoặc ít tốn công hơn **và** đơn vị đó muốn thử kết quả.
3. Nếu đổi sang thị trường tổ chức, đánh giá lại theo [5 tiêu chí cuộc thi](https://kiroween.devpost.com/rules), đặc biệt Impact và Innovation. Không lấy số thẻ làm đại diện cho số người dùng.

## Routing

→ `discover-competitive-analysis` nếu có đối tác thật: so quy trình của kho đó với Berlin/Sweden/Photothek và công cụ hiện có. Nếu không có đối tác, giữ **Don't build yet**.

## Nguồn và giới hạn

Nguồn gốc truy cập 22/11/2026: [Cambridge](https://www.libraries.cam.ac.uk/collections-and-archives/special-collections/accessing-special-collections/how-find-special), [Columbia](https://library.columbia.edu/collections/search/search-archives.html), [Berlin](https://lab.sbb.berlin/retrokonversion-katalogkarten-mittels-vision-language-models/?lang=en), [LIBER 2025](https://zenodo.org/records/16037875), [Photothek Florence](https://dhlab.khi.fi.it/blog-digitizing-the-phototheks-card-index/), [Devpost rules](https://kiroween.devpost.com/rules). Các số trên là khối lượng tư liệu/tồn kho hoặc dự án, không phải người dùng. Chưa kiểm tra chất lượng thực tế của các workflow AI hoặc khả năng mua sản phẩm của từng thư viện.
