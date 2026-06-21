# Hướng dẫn Bài thực hành 4 - Wavelet Hash

## Mục tiêu

Hoàn thành bài này, người học có thể tạo chữ ký wavelet, so sánh ảnh bằng Hamming, chọn ngưỡng hợp lệ, đánh giá bằng các chỉ số phân lớp/ROC và xây dựng tìm kiếm top-k.

## Thiết kế thí nghiệm

Notebook đọc trực tiếp hai thư mục. `image/tuong_tu/` cần ít nhất 3 ảnh của cùng một đối tượng hoặc cảnh; `image/khong_tuong_tu/` cần ít nhất 1 ảnh khác đối tượng hoặc cảnh. Mọi cặp trong nhóm tương tự mang nhãn `1`; mỗi ảnh tương tự ghép với ảnh không tương tự mang nhãn `0`.

Để tránh rò rỉ dữ liệu:

- tập validation dùng chọn threshold;
- tập test chỉ dùng báo cáo kết quả cuối;
- seed ngẫu nhiên được cố định để tái lập.

## Các phần trong notebook

1. Kiểm tra môi trường và tạo thư mục.
2. Đọc và hiển thị hai nhóm ảnh do người học tự thêm.
3. Trực quan phân rã wavelet.
4. Tạo hash và kiểm tra độ dài.
5. Tạo cặp có nhãn, tính Hamming.
6. Chọn ngưỡng tốt nhất trên validation bằng balanced accuracy.
7. Đánh giá test: confusion matrix, accuracy, sensitivity, specificity, precision.
8. Vẽ ROC và tính AUC.
9. So sánh nhiều họ wavelet.
10. Truy vấn tìm top-k ảnh gần nhất.

Mỗi mục trong notebook có ba phần: **Input**, **Output** và **Nhận xét**. Toàn bộ hàm xử lý nằm trong notebook, không cần import `wavelet_hash.py`.

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
