# Sổ giả thuyết — không phải dự án đã được xác thực

Mỗi mã là một ý tưởng khác nhau, được tạo sau khi xem người dùng và công nghệ lịch sử. “30 giây” chỉ là cảnh demo dự kiến. Tất cả vẫn cần xác nhận với người dùng và kiểm thử kỹ thuật.

## Chu kỳ 1 — truyền thông

| Mã | Công nghệ; người dùng; vấn đề hiện tại | Trải nghiệm chính, lý do Resurrection, demo 30 giây | Bất định kỹ thuật; đối thủ mạnh nhất; phản biện | Trạng thái |
|---|---|---|---|---|
| C01 | BBS; nhóm khu phố; thông báo lạc giữa mạng xã hội | Bảng tin địa phương theo thời hạn, người quản trị; đăng rồi người khác tìm theo chủ đề | Xác minh địa phương/chống spam; [Nextdoor](https://nextdoor.com/); nhu cầu và khác biệt chưa chứng minh | NEEDS EVIDENCE |
| C02 | FidoNet; nhóm mất mạng; muốn trao đổi bất đồng bộ | Chuyển tiếp thông báo giữa điện thoại khi gặp nhau; hai máy đồng bộ rồi máy thứ ba nhận | Đồng bộ, an toàn; [Briar](https://briarproject.org/quick-start/) đã làm chuyển tiếp diễn đàn | REJECTED |
| C03 | Minitel; người dùng điện thoại cơ bản; cần dịch vụ công ít dữ liệu | Giao diện một màn hình đánh số để tìm dịch vụ; nhập mã thấy thông tin | Phải có nguồn dữ liệu cập nhật; web nhẹ/USSD đã tồn tại, chưa xác nhận người dùng | NEEDS EVIDENCE |
| C04 | Pager; nhân viên trực; cần báo động gọn | Hộp thông báo chỉ có tín hiệu và hành động xác nhận; giả lập ca trực | An toàn báo động, tích hợp tổ chức; pager vẫn được dùng trong y tế, không đủ yếu tố “dead” | REJECTED |
| C05 | Fax; người cao tuổi; truy cập dịch vụ số qua giấy | Gửi yêu cầu giấy, nhận phản hồi giấy; một vòng trao đổi | Tích hợp fax và nhận dạng; [Faxi](https://devpost.com/software/faxi-16iecy) thắng chính hạng mục này | REJECTED |
| C06 | TTY; người khó nghe/nói; nhắn chữ trong cuộc gọi | Cầu nối TTY sang chat/RTT, xem trao đổi đồng thời | Tương thích nhà mạng; [FCC RTT](https://docs.fcc.gov/public/attachments/DOC-342624A1.pdf) và các dịch vụ relay đã giải bài toán cốt lõi | REJECTED |

## Chu kỳ 2 — media và lưu trữ cá nhân

| Mã | Công nghệ; người dùng; vấn đề hiện tại | Trải nghiệm chính, lý do Resurrection, demo 30 giây | Bất định kỹ thuật; đối thủ mạnh nhất; phản biện | Trạng thái |
|---|---|---|---|---|
| C07 | VHS/MiniDV; gia đình đã số hóa; thiếu ngữ cảnh trên file dài | “Tape map”: liên kết ảnh nhãn băng, người kể và mốc thời gian vào bản số hóa; tìm một đoạn và thấy nguồn gốc băng | Cần file mẫu có quyền dùng, xác minh metadata; [Legacybox](https://help.legacybox.com/en-US/how-do-you-digitize-tapes-what-is-the-quality-476997) số hóa, [Tropy](https://tropy-app.com/) chú giải; khoảng trống giữa hai bước chưa xác nhận | NEEDS EVIDENCE |
| C08 | Cassette; nhà lưu trữ cộng đồng; lời kể cũ khó tìm theo chủ đề | Gắn thời gian, tên người, nơi và giấy phép vào file cassette đã số hóa; mở đoạn lời kể trên bản đồ | Chất lượng nhận giọng Việt cũ, quyền chia sẻ; [OHMS](https://www2.archivists.org/sites/all/files/OralHistoryMetadataSynchronizer2.pdf), [StoryCorps](https://storycorps.org/storycorps-app-bib/) đã xử lý nhiều phần | NEEDS EVIDENCE |
| C09 | Đĩa mềm; gia đình có disk image; không biết tệp nào đáng giữ | Xem tệp và giải thích định dạng, xuất gói kèm provenance; kéo image vào và mở một tài liệu | Đọc định dạng cũ; [FloppoScope](https://github.com/0ldStaph/FloppoScope) đã mở nhiều filesystem trên browser, [BitCurator](https://bitcurator.net/bitcurator/) phục vụ lưu trữ | NEEDS EVIDENCE |
| C10 | Cassette language lab; giáo viên ngôn ngữ; muốn học nghe-nói theo lượt | Bài tập nghe, dừng, ghi lại và so sánh; demo một lượt học | Thiết kế sư phạm; [Sanako Connect](https://sanako.com/connect) có đúng chức năng cốt lõi | REJECTED |
| C11 | Voicemail; người giữ giọng thân nhân; khó xuất lời nhắn | Một nút xuất, nghe, lưu lời nhắn; demo từ bản ghi mẫu | API nền tảng; [iMazing](https://imazing.com/iphone-call-history-voicemail) đã xuất voicemail, [Remento](https://www.remento.co/) giữ giọng | REJECTED |
| C12 | CD-R/DVD-R; gia đình có đĩa cũ; không biết lỗi đọc | Quét lỗi và báo ưu tiên sao lưu; demo ảnh đĩa bị lỗi | Cần ổ đọc và dữ liệu lỗi; [dvdisaster](https://github.com/speed47/dvdisaster) đã kiểm tra/sửa bằng ECC, công cụ thường cần chuẩn bị từ trước | REJECTED |

## Chu kỳ 3 — cộng đồng số và học tập sáng tạo

| Mã | Công nghệ; người dùng; vấn đề hiện tại | Trải nghiệm chính, lý do Resurrection, demo 30 giây | Bất định kỹ thuật; đối thủ mạnh nhất; phản biện | Trạng thái |
|---|---|---|---|---|
| C13 | Yahoo! 360; blogger Việt giữ file xuất 2009/2013; blog cũ khó đọc và thiếu bình luận | Nhập **file người dùng sở hữu**, khôi phục bài-bình luận-dòng thời gian ở chế độ riêng tư; mở một bài và các hồi đáp | Cần mẫu export thật, quyền và định dạng; [WordPress importer](https://wordpress.org/documentation/article/importing-content/) và [Webrecorder](https://webrecorder.net/archivewebpage/) có phần tương tự; dữ liệu 2026 có thể hiếm | NEEDS EVIDENCE |
| C14 | GeoCities; người muốn trang cá nhân sáng tạo; mạng xã hội bó buộc | Trang cá nhân tự vẽ với “neighborhood”; demo tạo trang | [Neocities](https://neocities.org/about) đã phục hồi tinh thần và hosting; khác biệt chỉ trang trí | REJECTED |
| C15 | Web cũ; chủ trang đang hoạt động sợ mất website | Ghi lại bản web và xem offline; demo lưu rồi phát lại | [ArchiveWeb.page](https://webrecorder.net/archivewebpage/) thực hiện cốt lõi, có WARC/WACZ | REJECTED |
| C16 | HyperCard; chủ stack cũ; không mở trên máy mới | Đổi stack sang HTML có liên kết/script; demo stack cũ chạy browser | [hc2html](https://github.com/stachon/hc2html) đã làm gần đúng toàn bộ; nguy cơ bản quyền dữ liệu | REJECTED |
| C17 | HyperCard; giáo viên; muốn bài học tương tác tự tạo | Biên tập thẻ, nút, nhánh; học sinh đi qua một bài | [Twine](https://twinery.org/?page=Home) và [H5P](https://h5p.org/getting-started-v2) đã có trải nghiệm chính; nhu cầu chưa riêng | REJECTED |
| C18 | BASIC type-in; giáo viên lập trình; học sinh bấm Run quá nhanh, không hiểu lỗi | Tài liệu mã gõ tay có lỗi cố ý, tự chạy và so sánh quá trình sửa; demo học sinh sửa một dòng | Cần thử kết quả học tập; [PICO-8 Edu](https://www.lexaloffle.com/bbs/?pid=109887) đã hỗ trợ học code và chia sẻ, khác biệt sư phạm chưa chứng minh | NEEDS EVIDENCE |
| C19 | Logo turtle; trẻ học hình học; muốn nhìn chuyển động vật lý | Điều khiển rùa thật vẽ trên giấy; demo một hình | Phần cứng/chi phí; [Scratch](https://openlearning.mit.edu/news/10-sparks-lit-flame-scratch) và biến thể Logo vẫn hoạt động; “resurrection” yếu | REJECTED |

## Chu kỳ 4 — thư viện, dữ liệu thiết bị cũ

| Mã | Công nghệ; người dùng; vấn đề hiện tại | Trải nghiệm chính, lý do Resurrection, demo 30 giây | Bất định kỹ thuật; đối thủ mạnh nhất; phản biện | Trạng thái |
|---|---|---|---|---|
| C20 | Card catalog; thủ thư/người nghiên cứu; thẻ cũ có tài liệu chưa nằm trong online catalog | Chụp thẻ, giữ ảnh gốc và vị trí ngăn, tạo chỉ mục tìm kiếm; nhập tên sách thấy thẻ gốc | OCR chữ/tiếng Việt và nguồn thẻ; [open-source OCR workflow](https://static.tdwg.org/conferences/2024/posters/jerve-169.pdf), [Omeka](https://omeka.org/s/explore/) đã làm nhiều phần; cần đối tác thư viện | NEEDS EVIDENCE |
| C21 | Card catalog; nhóm di sản; muốn gắn quyền truy cập theo cộng đồng | Thẻ số có quyền xem theo nhóm; demo hai người thấy dữ liệu khác nhau | [Mukurtu](https://docs.mukurtu.org/communities-cultural-protocols-categories/) đã có cultural protocols; công nghệ lịch sử không là cốt lõi | REJECTED |
| C22 | Palm HotSync; chủ Palm cũ; muốn sao lưu danh bạ | Nối thiết bị, xuất vCard; demo một liên hệ | [pilot-link](https://github.com/desrod/pilot-link/blob/main/README.md) đã xuất vCard/backup; cần máy Palm thật | REJECTED |
| C23 | PalmPilot; người muốn bớt phân tâm; nhiều app gây mệt | App lịch/ghi chú kiểu Palm một chạm; demo hoàn thành lịch | Nhu cầu mơ hồ; mọi smartphone có app tối giản, Palm chỉ làm trang trí | REJECTED |
| C24 | Microfiche; cơ quan lưu trữ; bản phim khó tìm | Scan/OCR fiche, tìm và phóng to một trang | Thiết bị đắt/chuyên dụng; [ViewScan](https://www.iiri.com/viewscan4-microfilm-scanner) có OCR, [đấu thầu 2026](https://webfiles.nycourts.gov/public/2026-05/oca-dgcp-072-microfiche-digitization-system-equipment-software-installation-and-support.pdf) đòi scanner chuyên biệt | REJECTED |
| C25 | Card catalog; thư viện nhỏ; ảnh thẻ đã có nhưng OCR sai | Người tình nguyện sửa bản chép cạnh ảnh, giữ lịch sử sửa; demo xác nhận một thẻ | [LOC By the People](https://labs.loc.gov/work/experiments/crowd/) đã có mô hình tương tự; cần chứng minh quy trình riêng ở thư viện nhỏ | NEEDS EVIDENCE |

## Chu kỳ 5 — dịch vụ số Đông Á

| Mã | Công nghệ; người dùng; vấn đề hiện tại | Trải nghiệm chính, lý do Resurrection, demo 30 giây | Bất định kỹ thuật; đối thủ mạnh nhất; phản biện | Trạng thái |
|---|---|---|---|---|
| C26 | i-mode; người dùng feature phone; thiếu dịch vụ nhẹ | Cổng tin một nút, ít dữ liệu; demo duyệt mục bằng phím | [KaiOS](https://consumer.kaiostech.com/platform) và [BlueKai 2025](https://devpost.com/software/bluekai-bluesky-on-a-flip-phone) đã chứng minh đúng kiểu ứng dụng | REJECTED |
| C27 | i-mode; nhà sử học web Nhật; trang cHTML cũ không chạy | Trình đọc gói lưu trữ cHTML và hiển thị giao diện máy cũ; demo trang mẫu offline | Chưa tìm được bộ dữ liệu được phép dùng/nhu cầu; [Webrecorder](https://webrecorder.net/) đã replay web chung | NEEDS EVIDENCE |
| C28 | Cyworld; cựu người dùng; muốn minihompy trở lại | Tạo mini-homepage và danh sách bạn; demo kết bạn | [Cyworld](https://www.cyworld.co.kr/) tự công bố kế hoạch phục hồi; thương hiệu/dữ liệu không có quyền | REJECTED |
| C29 | Cyworld; người cần lấy ảnh cũ | Công cụ đăng nhập và xuất ảnh; demo tải một album | Không có API/quyền dữ liệu; bên sở hữu [đang lên kế hoạch khôi phục](https://mbiz.heraldcorp.com/article/10917926) | REJECTED |

## Chu kỳ 6 — văn bản Việt mã hóa cũ

| Mã | Công nghệ; người dùng; vấn đề hiện tại | Trải nghiệm chính, lý do Resurrection, demo 30 giây | Bất định kỹ thuật; đối thủ mạnh nhất; phản biện | Trạng thái |
|---|---|---|---|---|
| C30 | TCVN3/VNI; người có đoạn chữ lỗi dấu | Dán chữ, tự nhận mã, chuyển Unicode; demo một câu | [UniKey Toolkit](https://unikey.edu.vn/cach-chuyen-ma-font-chu-bang-unikey-toolkit/) và [UniTextKit](https://unitextkit.top/en/vietnamese-encoding-converter/) đã có | REJECTED |
| C31 | TCVN3/VNI; văn thư có nhiều file cũ | Chuyển hàng loạt Word/Excel/HTML, giữ dấu; demo 10 file | [UnicodeConverter](https://vietunicode.sourceforge.net/howto/unicodeconversion.html) đã xử lý các dạng file và mã này | REJECTED |
| C32 | Mã Việt cũ trong file scan/PDF; nhà lưu trữ muốn text sạch | Nhập file, trích chữ Unicode và xuất Markdown; demo PDF cũ | [viparse](https://github.com/TrizenX/viparse) đã công bố đúng luồng, cần kiểm thử độc lập nếu muốn tranh luận chất lượng | REJECTED |
| C33 | Font chữ Việt cũ; nghệ sĩ muốn giao diện hoài cổ | App dựng lại chữ VNI/ABC như cũ; demo màn hình retro | Chỉ thẩm mỹ, không chứng minh vấn đề hay Resurrection cốt lõi; công cụ font/converter đã có | REJECTED |

## Chu kỳ 7 — tiếp cận nội dung âm thanh và hình ảnh cũ

| Mã | Công nghệ; người dùng; vấn đề hiện tại | Trải nghiệm chính, lý do Resurrection, demo 30 giây | Bất định kỹ thuật; đối thủ mạnh nhất; phản biện | Trạng thái |
|---|---|---|---|---|
| C34 | Sách nói cassette; người khiếm thị; muốn nghe lại sách cũ | Máy nghe web có điều hướng chương/mốc; demo nhảy tới chương | [BARD](https://www.loc.gov/nls/how-to-enroll/sign-up-for-bard-and-bard-mobile/) và máy phát số [DA2](https://www.loc.gov/nls/services-and-resources/equipment-for-nls-materials/da2-getting-started/) đã đáp ứng điều hướng; không có băng/giấy phép | REJECTED |
| C35 | Sách nói cassette; thư viện nhỏ; muốn đồng bộ âm thanh với văn bản | Nhập audio và text, đánh dấu từng đoạn; demo nhấp câu để nghe | [DAISY Tobi](https://daisy.org/activities/software/tobi/) đã nhập audio ngoài và đồng bộ text theo chuẩn; khác biệt không rõ | REJECTED |
| C36 | Phụ đề Line 21 trên VHS; nhà lưu trữ; muốn lấy lại chữ | Đọc bản video đã capture, xuất phụ đề WebVTT; demo bật phụ đề | [CCExtractor](https://ccextractor.org/public/general/whatsccextractor/?idx=wiki) đã trích; phần cứng có thể không giữ dữ liệu Line 21 | REJECTED |
| C37 | Máy nghe sách nói cassette; người lớn tuổi khiếm thị; cần nút vật lý dễ bấm | Bàn phím dạng băng cassette cho sách số; demo bấm tìm chương | [NLS DA2](https://www.loc.gov/nls/services-and-resources/equipment-for-nls-materials/da2-getting-started/) có nút vật lý; phần cứng tốn công, chưa có người dùng xác nhận | REJECTED |

## Chu kỳ 8 — kiến thức và trình chiếu trong giáo dục

| Mã | Công nghệ; người dùng; vấn đề hiện tại | Trải nghiệm chính, lý do Resurrection, demo 30 giây | Bất định kỹ thuật; đối thủ mạnh nhất; phản biện | Trạng thái |
|---|---|---|---|---|
| C38 | Encarta CD-ROM; học sinh ít Internet; cần bách khoa offline | Gói bài viết hữu hạn, bản đồ và liên kết chạy offline; demo tìm chủ đề không mạng | [Kiwix](https://kiwix.org/en/) đã phân phối kho tri thức offline; nội dung Encarta còn bản quyền; chỉ giao diện cũ không đủ | REJECTED |
| C39 | LaserDisc bài học tương tác; bảo tàng; muốn phát lại hành trình phi tuyến | Chọn điểm trên màn hình để xem cảnh video cũ; demo nhảy cảnh | [CHM](https://computerhistory.org/blog/quicktime-and-the-rise-of-multimedia/) đã tái dựng hệ thật; cần đĩa/player/quyền video; web video phổ biến | REJECTED |
| C40 | Khay slide 35mm; nhà lưu trữ; sợ mất thứ tự thuyết trình | Chụp khay, scan ảnh, lưu vị trí và ghi chú; demo mở slide số theo thứ tự vật lý | [Tropy](https://docs.tropy.org/) đã quản ảnh và metadata hộp/bộ sưu tập; chưa có khay mẫu hay vấn đề người dùng | REJECTED |
| C41 | Overhead projector và tấm trong suốt; giáo viên; muốn viết từng lớp khi dạy | Lớp trong suốt số, viết rồi bật/tắt; demo giải một hình | [OpenBoard](https://www.openboard.ch/en) có bảng tương tác; overhead còn dùng ở ngách; khác biệt chỉ mô phỏng thao tác | REJECTED |
