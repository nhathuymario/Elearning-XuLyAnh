# Phần II: Lọc tuyến tính

## 1. Mục tiêu

Thực hiện và so sánh các kỹ thuật lọc tuyến tính:

1. Lọc trung bình.
2. Lọc Gaussian.
3. Làm sắc nét.

## Câu II.1. Lọc trung bình

Mục tiêu:

- Làm mượt ảnh.
- Giảm nhiễu nhẹ.

Cách thực hiện:

1. Chọn kernel `3x3` hoặc `5x5`.
2. Áp dụng `cv2.blur()`.
3. Hiển thị ảnh trước và sau khi lọc.
4. Nhận xét mức độ mất chi tiết và mờ biên.

## Câu II.2. Lọc Gaussian

Mục tiêu:

- Làm mượt ảnh tự nhiên hơn lọc trung bình.
- Giảm nhiễu trước khi phát hiện cạnh.

Cách thực hiện:

1. Chọn kernel có kích thước lẻ.
2. Chọn giá trị sigma.
3. Áp dụng `cv2.GaussianBlur()`.
4. So sánh với lọc trung bình.

## Câu II.3. Làm sắc nét

Mục tiêu:

- Làm rõ cạnh và chi tiết trong ảnh.

Kernel dự kiến:

```python
sharpen_kernel = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
])
```

Cách thực hiện:

1. Khai báo kernel làm sắc nét.
2. Áp dụng kernel bằng `cv2.filter2D()`.
3. Hiển thị ảnh gốc và ảnh kết quả.
4. Kiểm tra ảnh có bị tăng nhiễu hoặc quá sắc hay không.
