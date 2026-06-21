# Hướng dẫn Bài thực hành 4 - Wavelet Hash

## Mục tiêu

Hoàn thành bài này, người học có thể tạo chữ ký wavelet, so sánh ảnh bằng Hamming, chọn ngưỡng hợp lệ, đánh giá bằng các chỉ số phân lớp/ROC và xây dựng tìm kiếm top-k.

## Thiết kế thí nghiệm

Notebook đọc trực tiếp hai thư mục. `image/tuong_tu/` cần ít nhất 3 ảnh của cùng một đối tượng hoặc cảnh; `image/khong_tuong_tu/` cần ít nhất 1 ảnh khác đối tượng hoặc cảnh. Mọi cặp trong nhóm tương tự mang nhãn `1`; mỗi ảnh tương tự ghép với ảnh không tương tự mang nhãn `0`.

Để tránh rò rỉ dữ liệu:

- tập validation dùng chọn threshold;
- tập test chỉ dùng báo cáo kết quả cuối;
- seed ngẫu nhiên được cố định để tái lập.

## Sáu phần trong notebook

1. Chuẩn bị dữ liệu ảnh tương tự và không tương tự.
2. Trích xuất ma trận Wavelet cho từng ảnh và trực quan LL, LH, HL, HH.
3. Lượng tử hóa hệ số Wavelet và tạo mã băm 64 bit.
4. Tạo cặp có nhãn và tính khoảng cách Hamming.
5. Chọn ngưỡng trên validation; đánh giá test bằng Accuracy, Sensitivity, Specificity, Precision, confusion matrix và ROC/AUC.
6. Khảo sát và so sánh `haar`, `db2`, `db4`, `sym4` trên cùng validation/test.

Notebook chỉ giữ đúng sáu phần của đề. Hàm phục vụ bước nào nằm ngay trong bước đó; mỗi bước đều có **Input**, **Output**, chú thích mã và **Nhận xét**.

## Vì sao không dùng khung mã nguyên trạng trong slide?

Khung slide nối mọi hệ số chi tiết sau `wavedec2` rồi lấy phần dư `% 2`. Cách đó có ba vấn đề: mã rất dài, phép `% 2` trên số thực âm không phải lượng tử hóa cảm nhận hợp lý, và kích thước phụ thuộc ảnh/mức phân rã. Bản thực hành tạo đúng `hash_size²` bit từ `LL` và threshold median.

## Cách đọc kết quả

- Histogram hai lớp tách xa: hash phân biệt tốt.
- FN cao: threshold quá chặt hoặc biến đổi ảnh quá mạnh.
- FP cao: threshold quá rộng hoặc các ảnh khác lớp có bố cục tổng thể giống nhau.
- AUC đo chất lượng xếp hạng trên mọi threshold; không phụ thuộc một ngưỡng duy nhất.

## Bài tập nâng cao

1. Thêm JPEG compression, crop và perspective transform; đo độ bền.
2. Khảo sát `level = 1..3`, `hash_size = 8, 16` và các wavelet khác.
3. So sánh Wavelet Hash với average hash, pHash và ORB.
4. Thay tìm kiếm tuần tự bằng cấu trúc chỉ mục nhị phân cho tập dữ liệu lớn.
