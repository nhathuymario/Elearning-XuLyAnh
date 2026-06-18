# Đánh giá nội dung thuyết trình Canny

## Kết luận nhanh

Nội dung hiện tại đã đủ khung kiến thức và đủ code để thuyết trình một bài Canny hoàn chỉnh:

- Có nguyên lý và các bước của thuật toán.
- Có phân tích `sigma`, ngưỡng thấp và ngưỡng cao.
- Có so sánh OpenCV với Scikit-image.
- Có thử nghiệm trên nhiều điều kiện ảnh.
- Có kết hợp contour, nhận dạng hình dạng, ảnh màu và video.

Phần II đã có đầy đủ ảnh minh chứng cho so sánh thư viện, tham số, loại ảnh,
phân đoạn và nhận dạng hình dạng. Phần I vẫn cần bổ sung ảnh minh họa từng
bước Canny; phần III về video vẫn là hướng mở rộng chưa chạy thực tế.

## Bố cục đề xuất

### I. Lý thuyết

1. Bài toán phát hiện cạnh và vai trò của Canny.
2. Sáu bước: Gaussian, gradient, hướng gradient, non-maximum suppression, double threshold, hysteresis.
3. Ý nghĩa của `sigma`, `threshold_low`, `threshold_high`.
4. Ưu điểm, nhược điểm và ứng dụng.

Điểm cần nhấn mạnh: phần code hiện chỉ minh họa Gaussian, Sobel và kết quả Canny cuối; chưa tự cài đặt non-maximum suppression và hysteresis. Khi trình bày nên nói rõ đây là minh họa gần đúng, còn `cv2.Canny` thực hiện quy trình hoàn chỉnh.

### II. Bài tập thực hành

1. So sánh OpenCV và Scikit-image.
2. Thay đổi tham số và giải thích sự thay đổi của cạnh.
3. Thử ảnh nhiễu, tương phản thấp và nhiều chi tiết.
4. Kết hợp morphology, contour và nhận dạng hình dạng.

Notebook đã bổ sung tỷ lệ pixel cạnh và số thành phần liên thông để hỗ trợ
đánh giá. Khi thuyết trình cần giải thích đây là chỉ số hỗ trợ, không thay thế
Precision, Recall và F1 khi có ảnh biên chuẩn.

### III. Câu hỏi mở rộng

1. Đánh giá bằng Precision, Recall, F1 khi có ảnh biên chuẩn.
2. Cải thiện tốc độ bằng resize, ROI, xử lý cách frame hoặc GPU.
3. Canny trên từng kênh màu.
4. Canny trên video.

Phần video hiện mới có code mẫu, chưa có video đầu vào và kết quả thực chạy. Khi thuyết trình cần ghi rõ đây là hướng mở rộng.

## Các phần còn thiếu nên bổ sung

- Lưu ảnh cho minh họa Gaussian, gradient và ba bộ ngưỡng.
- Chuẩn bị một video đầu vào nếu muốn trình diễn Canny trên video.
- Chuẩn bị ảnh biên chuẩn nếu muốn tính Precision, Recall và F1.
- Có một slide kết luận: không tồn tại một bộ tham số tốt cho mọi ảnh.

## Câu kết luận có thể dùng

Canny cho cạnh mảnh và ổn định nhờ kết hợp giảm nhiễu, gradient, làm mảnh cạnh và hysteresis. Chất lượng kết quả phụ thuộc mạnh vào mức làm mượt và hai ngưỡng, vì vậy tham số phải được chọn theo đặc điểm nhiễu, độ tương phản và mục tiêu của từng ảnh.
