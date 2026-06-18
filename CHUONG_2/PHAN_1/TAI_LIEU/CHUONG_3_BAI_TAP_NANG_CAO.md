# Phần III: Bài tập nâng cao

## Câu III.1. Phát hiện cạnh Sobel và Prewitt

### Sobel

Quy trình:

1. Sử dụng ảnh xám.
2. Tính gradient theo hướng `x`.
3. Tính gradient theo hướng `y`.
4. Kết hợp hai gradient.
5. Chuyển kết quả về ảnh 8-bit.
6. Lưu ảnh cạnh Sobel.

### Prewitt

Quy trình:

1. Tạo kernel Prewitt theo hướng `x`.
2. Tạo kernel Prewitt theo hướng `y`.
3. Áp dụng hai kernel bằng `cv2.filter2D()`.
4. Kết hợp kết quả của hai hướng.
5. Lưu ảnh cạnh Prewitt.

## Câu III.2. Tự thiết kế kernel

### Kernel Emboss

Mục tiêu:

- Tạo hiệu ứng nổi khối cho ảnh.

Kernel dự kiến:

```python
emboss_kernel = np.array([
    [-2, -1, 0],
    [-1, 1, 1],
    [0, 1, 2]
])
```

### Kernel Laplacian

Mục tiêu:

- Phát hiện vùng có sự thay đổi cường độ sáng mạnh.

Kernel dự kiến:

```python
laplacian_kernel = np.array([
    [0, -1, 0],
    [-1, 4, -1],
    [0, -1, 0]
])
```

Quy trình chung:

1. Khai báo ma trận kernel.
2. Áp dụng bằng `cv2.filter2D()`.
3. Chuyển kết quả về định dạng phù hợp để hiển thị.
4. Lưu ảnh.
5. Giải thích tác dụng của các hệ số trong kernel.

## Câu III.3. So sánh các loại lọc

Áp dụng các bộ lọc sau trên cùng một ảnh:

- Mean filter.
- Gaussian filter.
- Median filter.
- Bilateral filter.
- Sharpen filter.

Bảng tiêu chí so sánh:

| Bộ lọc | Khả năng làm mờ | Giảm nhiễu | Giữ biên |
|---|---|---|---|
| Mean | Cao | Trung bình | Kém |
| Gaussian | Tự nhiên | Tốt | Trung bình |
| Median | Trung bình | Tốt với nhiễu muối tiêu | Tốt |
| Bilateral | Trung bình | Tốt | Rất tốt |
| Sharpen | Không làm mờ | Có thể tăng nhiễu | Làm biên rõ |

Cách thực hiện:

1. Áp dụng tất cả bộ lọc trên cùng ảnh đầu vào.
2. Hiển thị kết quả trong cùng một bảng ảnh.
3. Quan sát độ mờ, mức giảm nhiễu và khả năng giữ biên.
4. Viết nhận xét cho từng bộ lọc.

## Câu III.4. Áp dụng lọc phi tuyến

### Median filter

Mục tiêu:

- Loại bỏ nhiễu muối tiêu.

Cách thực hiện:

1. Chọn kernel `5x5`.
2. Áp dụng `cv2.medianBlur()`.
3. So sánh ảnh trước và sau khi lọc.

### Bilateral filter

Mục tiêu:

- Làm mượt ảnh nhưng vẫn giữ đường biên.

Cách thực hiện:

1. Chọn đường kính vùng lân cận.
2. Chọn `sigmaColor`.
3. Chọn `sigmaSpace`.
4. Áp dụng `cv2.bilateralFilter()`.
5. So sánh với Median và Gaussian.

Nhận xét dự kiến:

- Median phù hợp với nhiễu muối tiêu.
- Bilateral giữ biên tốt hơn các bộ lọc làm mờ thông thường.
- Bilateral thường mất nhiều thời gian xử lý hơn.

## 5. Lưu và kiểm tra kết quả

Các công việc cần thực hiện:

1. Lưu từng ảnh bằng `cv2.imwrite()`.
2. Đặt tên file theo số thứ tự của câu.
3. Kiểm tra thư mục `outputs_chapter_2`.
4. Kiểm tra ảnh có đúng màu và đúng nội dung không.
5. Chạy lại notebook từ đầu bằng `Restart Kernel and Run All`.
6. Đảm bảo tất cả cell chạy đúng thứ tự và không có lỗi.

Danh sách kết quả dự kiến:

```text
outputs_chapter_2/
├── I_1_tang_do_sang.png
├── I_1_giam_do_sang.png
├── I_2_tang_tuong_phan.png
├── I_2_giam_tuong_phan.png
├── I_3_am_ban.png
├── I_4_cat_nguong.png
├── II_1_loc_trung_binh.png
├── II_2_loc_gaussian.png
├── II_3_lam_sac_net.png
├── III_1_sobel.png
├── III_1_prewitt.png
├── III_2_kernel_emboss.png
├── III_2_kernel_laplacian.png
├── III_4_median_filter.png
└── III_4_bilateral_filter.png
```

## 6. Hoàn thiện báo cáo

Bố cục báo cáo đề xuất:

1. Tên bài thực hành.
2. Mục tiêu.
3. Công cụ và thư viện sử dụng.
4. Dữ liệu đầu vào.
5. Toán tử điểm ảnh.
6. Lọc tuyến tính.
7. Phát hiện cạnh.
8. Kernel tùy chỉnh.
9. So sánh các bộ lọc.
10. Lọc phi tuyến.
11. Nhận xét tổng hợp.
12. Kết luận.

Với mỗi câu, trình bày:

```text
Mục tiêu
→ Input
→ Nguyên lý hoặc công thức
→ Code
→ Hình ảnh kết quả
→ Nhận xét
```
## 7. Kết luận dự kiến

Bài thực hành giúp hiểu cách thay đổi trực tiếp giá trị pixel, sử dụng
kernel để lọc ảnh, giảm nhiễu, làm sắc nét và phát hiện cạnh. Qua việc
so sánh các phương pháp, có thể lựa chọn bộ lọc phù hợp với từng loại
ảnh và mục tiêu xử lý khác nhau.
