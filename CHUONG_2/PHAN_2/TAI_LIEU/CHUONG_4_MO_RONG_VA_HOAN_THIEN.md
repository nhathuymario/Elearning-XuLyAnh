# Phần III: Các câu hỏi mở rộng

## 1. Mục tiêu

Chương này mở rộng Canny cho ảnh màu và video, đánh giá chất lượng
cạnh, đề xuất cách cải thiện và kiểm tra toàn bộ kết quả.

## Câu III.1. Đánh giá chất lượng cạnh

Nếu có ảnh cạnh chuẩn:

- Precision.
- Recall.
- F1-score.

Nếu không có ảnh chuẩn:

- Độ mảnh của cạnh.
- Độ liên tục.
- Số cạnh giả.
- Khả năng giữ cạnh quan trọng.

## Câu III.2. Cải thiện hiệu suất và kết quả

- Dùng Gaussian filter trước Canny.
- Dùng Median filter cho nhiễu muối tiêu.
- Dùng Bilateral filter khi cần giữ biên.
- Chọn ngưỡng tự động từ histogram hoặc Otsu.
- Chỉ xử lý vùng ROI.
- Resize ảnh trước khi xử lý.
- Xử lý cách frame khi dùng video.

## Câu III.3. Canny trên ảnh màu

Canny thường được áp dụng trên ảnh xám. Có thể phát hiện cạnh trên từng
kênh màu rồi kết hợp:

```python
b, g, r = cv2.split(image_bgr)

edge_b = cv2.Canny(b, 80, 160)
edge_g = cv2.Canny(g, 80, 160)
edge_r = cv2.Canny(r, 80, 160)

color_edges = cv2.bitwise_or(
    cv2.bitwise_or(edge_b, edge_g),
    edge_r
)
```

Nhận xét:

- Xử lý từng kênh có thể giữ cạnh màu mà ảnh xám bỏ qua.
- Kết quả có thể chứa nhiều cạnh và nhiễu hơn.

## Câu III.4. Canny trên video

Quy trình:

1. Đọc từng frame.
2. Chuyển frame sang ảnh xám.
3. Làm mượt bằng Gaussian.
4. Chạy Canny.
5. Hiển thị hoặc lưu kết quả.

```python
cap = cv2.VideoCapture('input.mp4')

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray_frame = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2GRAY
    )
    gray_frame = cv2.GaussianBlur(
        gray_frame,
        (5, 5),
        1.4
    )
    edges = cv2.Canny(gray_frame, 80, 160)

cap.release()
cv2.destroyAllWindows()
```

## 5. Danh sách kết quả tổng hợp

```text
outputs_chapter_2_part_2/
├── I_1_gaussian_blur.png
├── I_1_gradient_magnitude.png
├── I_1_canny_final.png
├── I_2_canny_nhay.png
├── I_2_canny_can_bang.png
├── I_2_canny_it_canh.png
├── II_1_canny_opencv.png
├── II_1_canny_skimage.png
├── II_2_so_sanh_tham_so.png
├── II_3_anh_nhieu.png
├── II_3_anh_tuong_phan_thap.png
├── II_3_anh_nhieu_chi_tiet.png
├── II_4_contours.png
├── II_4_nhan_dang_hinh_dang.png
└── III_3_canny_color_channels.png
```

Lưu ý: Phần II đã có đầy đủ ảnh kết quả. Các ảnh Phần I trong danh sách vẫn
cần bổ sung; Câu III.3 đã có kết quả ảnh màu và Câu III.4 về video chưa chạy
thực tế.

## 6. Kiểm tra cuối cùng

1. Kiểm tra tất cả ảnh kết quả đã được lưu.
2. So sánh OpenCV với Scikit-image.
3. So sánh các cấu hình tham số.
4. Kiểm tra contour và nhãn hình dạng.
5. Chạy notebook bằng `Restart Kernel and Run All`.
6. Đảm bảo tất cả cell chạy đúng thứ tự và không có lỗi.

## 7. Checklist phần III

- [ ] Thử Canny trên từng kênh màu.
- [ ] Trình bày cách áp dụng Canny cho video.
- [ ] Đánh giá chất lượng cạnh.
- [ ] Đề xuất phương pháp cải thiện.
- [ ] Lưu đầy đủ kết quả.
- [ ] Viết nhận xét tổng hợp.
- [ ] Viết kết luận.
- [ ] Chạy toàn bộ notebook không có lỗi.

## 8. Kết luận dự kiến

Canny tạo cạnh rõ và mảnh nhờ kết hợp giảm nhiễu, tính gradient, làm
mảnh cạnh, double threshold và hysteresis. Chất lượng kết quả phụ thuộc
nhiều vào sigma và hai giá trị ngưỡng. Khi được tiền xử lý và chọn tham
số phù hợp, Canny có thể hỗ trợ tốt cho tìm contour, phân đoạn và nhận
dạng hình dạng.
