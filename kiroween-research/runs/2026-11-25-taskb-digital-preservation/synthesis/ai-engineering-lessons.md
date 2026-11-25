# Bài học AI Engineering — Task B (và các phase trước)

Mỗi điểm được gắn một trong hai nhãn:

- **[đo được]**: có số liệu trong [`../coordinator/execution-log.md`](../coordinator/execution-log.md) hoặc trong log của Phase 1, 1.5, 2;
- **[suy luận]**: diễn giải, chưa được kiểm định.

## 1. Cross-review có đổi kết luận nghiên cứu không?

**Có, rõ ràng. [đo được]**

- **Nhãn bằng chứng.** A hạ 24/27 nhãn VERIFIED, B hạ 12/20, C hạ 1/6. Tỷ lệ VERIFIED của A giảm từ 90% xuống khoảng 10%.
- **Vai trò AI.** Ba cơ hội "AI load-bearing" giảm còn một (B-O5), và cơ hội này cũng chỉ ở mức giả thuyết.
- **Phạm vi.** 2 cơ hội bị rút, 3 đề xuất gộp. Cụm game được **cả ba agent** đề xuất gộp.
- **Phương án bị bỏ sót được bổ sung:** phản hồi EC 16/06/2026, EU Data Act, WACZ, trình xem archive Mastodon, baseline `m2c` + `decomp-permuter`.
- **[suy luận]** Phần lớn thay đổi nằm ở **mức độ chắc chắn** và **khoảng trống so với đối thủ**, không nằm ở việc phát hiện vấn đề mới. Phản biện chéo hiệu quả nhất khi kiểm nhãn và tìm phương án thay thế.

## 2. Bất đồng giữa evaluator theo model

**[đo được]** Kỷ luật nhãn khác nhau rõ rệt giữa các model, và hướng lệch ổn định qua các phase:

- Phase 1.5: A +8, B −5, C ≈ 0 so với người chấm tham chiếu.
- Task B Round 1: A gắn VERIFIED 90% claim, B 49%, C 14%.

**[suy luận]** Muốn so điểm hoặc nhãn giữa các agent thì cần hiệu chuẩn hoặc phản biện chéo. Gộp thẳng điểm của nhiều model mà không hiệu chuẩn sẽ thiên về model rộng tay.

## 3. Độc lập nghiên cứu và hội tụ

- **[đo được]** Round 1: không có đọc chéo (kiểm transcript, không có tham chiếu tới thư mục bị cấm).
- **[đo được]** Dù vậy, 5 vùng vấn đề được ít nhất hai agent tìm ra độc lập; game end-of-life được cả ba tìm ra.
- **[suy luận]** Hội tụ độc lập là tín hiệu mạnh hơn điểm số của từng agent. Tuy nhiên ba agent có cùng brief và danh sách "đã khám phá", nên hội tụ có thể một phần do bối cảnh chung tạo ra, không hoàn toàn độc lập.

## 4. Chuyên môn hóa agent

- Không giao vai trò. **[đo được]** Có khác biệt tự nhiên:
  - A rộng nhất (5 cơ hội, nhiều vùng) nhưng nhãn lỏng;
  - B mạnh về bằng chứng hành vi cộng đồng và châu Á (keitai);
  - C hẹp nhất (3 cơ hội) nhưng chặt nhất về pháp lý và quyền.
- **[suy luận]** Cấu hình "một model rộng, một model chặt" hữu ích nếu bước phản biện chéo được thiết kế để model chặt kiểm model rộng.

## 5. Chọn ngữ cảnh và bàn giao ngữ cảnh

- **[đo được]** Agent nhận một **danh sách** chủ đề đã khám phá, không nhận điểm hay xếp hạng.
- **[đo được]** Không cơ hội Round 1 nào trùng tên với một mục trong danh sách "đã khám phá". **[suy luận]** Chỉ T2 gần vùng của A-P4. T1 (game) gần B-P1 về cơ chế nhưng khác đối tượng. Coordinator chưa đếm có hệ thống mức trùng với sổ ý tưởng cũ.
- **[suy luận]** Chặn xếp hạng cũ đã làm đúng việc của nó là không neo vào kết quả trước.
- **[đo được]** Bàn giao giữa round qua tệp và hash cộng với follow-up dispatch trên cùng session hoạt động ổn: tệp Round 1 không đổi.

## 6. Chi phí token và thời gian

- **[đo được]** Worker (B, C):
  - đầu vào 8–10M token mỗi agent cho hai round, trong đó 95–98% là cache read;
  - đầu ra 50–86k token;
  - thời gian 13–20 phút.
- **[đo được]** Round 2 của C tốn nhiều đầu vào hơn Round 1 (6,07M so với 3,63M), vì đọc báo cáo người khác làm ngữ cảnh tích lũy tăng.
- **[đo được]** **Coordinator là bên tiêu thụ lớn nhất:** 20,9M token đầu vào trong 30 phút của Task B, vì phiên dài mang toàn bộ lịch sử các phase trước.
- **[suy luận]** Muốn giảm chi phí thì nên tách coordinator theo phase, hoặc tóm tắt lịch sử, thay vì giảm effort của worker.
- **[đo được]** Không đo được token của Antigravity (agy): log và DB hội thoại không có trường token. Đây là khoảng trống quan sát thực sự cho mọi phép so sánh chi phí có agy.

## 7. Nâng effort

- **[đo được]** Không nâng effort ở Task B. Lý do được ghi trước khi quyết định.
- **[suy luận]** Bất đồng giữa các agent thường cần **bằng chứng mới**, không cần **suy luận sâu hơn**. Nâng effort chỉ đáng khi bất đồng nằm ở phân tích trên cùng một bộ bằng chứng (ví dụ diễn giải pháp lý của một văn bản đã mở). Task B không có ca nào như vậy.
- **[đo được]** Effort cố định theo tiến trình. Muốn nâng effort cho một vấn đề cụ thể phải khởi chạy worker riêng; follow-up trên cùng session không đổi được effort.

## 8. An ninh runtime và cô lập filesystem

- **[đo được]** Orca chạy cả ba worker với full-access. Không có cờ sandbox theo lần khởi chạy.
- **[đo được]** Bubblewrap chặn được ghi ngoài thư mục, ẩn thư mục peer, và vẫn giữ web cùng socket Orca. Đã kiểm trong scratch, chưa chạy agent CLI bên trong.
- **[đo được]** Anh/chị chọn chấp nhận rủi ro có phạm vi. Kiểm tra sau chạy không thấy vi phạm ở cả bốn lần chạy worker (Phase 1, Phase 2, Task B R1, Task B R2).
- **[suy luận]** "Không thấy vi phạm" là bằng chứng về **hành vi** trong các lần chạy này, không phải bảo đảm **an ninh**. Tính năng cô lập vẫn là việc kỹ thuật chưa làm.

## 9. Kiểm chứng bằng chứng

- **[đo được]** Quy tắc "snippet không phải VERIFIED" và yêu cầu ghi "opened directly / snippet" làm tỷ lệ nguồn mở trực tiếp tăng:
  - Phase 2A, B: 12/50;
  - Task B R1, B: 24/31;
  - Task B R2, B: 11/11.
- **[suy luận]** Quy tắc rõ ràng trong output contract có tác dụng mạnh hơn yêu cầu chung chung về chất lượng.
