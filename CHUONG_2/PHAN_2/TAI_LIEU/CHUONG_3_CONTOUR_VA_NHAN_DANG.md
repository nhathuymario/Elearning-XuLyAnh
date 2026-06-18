# Phần II - Câu II.4: Kết hợp Canny với các kỹ thuật khác

## 1. Mục tiêu Câu II.4

Kết hợp Canny với các phép toán hình thái học để tìm contour và nhận
dạng các hình dạng cơ bản.

## 2. Quy trình xử lý

1. Phát hiện cạnh bằng Canny.
2. Dùng morphology close để nối cạnh.
3. Dùng dilate để làm cạnh rõ hơn.
4. Tìm contour.
5. Loại bỏ contour có diện tích quá nhỏ.
6. Xấp xỉ contour và xác định hình dạng.

## 3. Kết hợp Canny với morphology

```python
edges = cv2.Canny(gray, 80, 160)

kernel = np.ones((3, 3), dtype=np.uint8)
closed_edges = cv2.morphologyEx(
    edges,
    cv2.MORPH_CLOSE,
    kernel,
    iterations=2
)

dilated_edges = cv2.dilate(
    closed_edges,
    kernel,
    iterations=1
)
```

Kết quả cần kiểm tra:

- Các đoạn cạnh gần nhau được nối lại.
- Cạnh đủ rõ để tạo contour khép kín.
- Không làm dính quá nhiều vật thể riêng biệt.

## 4. Tìm contour

```python
contours, _ = cv2.findContours(
    dilated_edges,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)
```

Nên lọc contour theo diện tích:

```python
valid_contours = [
    contour
    for contour in contours
    if cv2.contourArea(contour) >= 100
]
```

## 5. Xấp xỉ contour

```python
perimeter = cv2.arcLength(contour, True)
approx = cv2.approxPolyDP(
    contour,
    0.03 * perimeter,
    True
)

vertices = len(approx)
```

Quy tắc nhận dạng dự kiến:

- `3` đỉnh: tam giác.
- `4` đỉnh: tứ giác hoặc hình chữ nhật.
- Trên `6` đỉnh: có thể là hình tròn hoặc đường cong.

## 6. Các tiêu chí bổ sung

Không nên chỉ dựa vào số đỉnh. Cần kết hợp:

- Diện tích contour.
- Tỷ lệ chiều rộng và chiều cao.
- Độ tròn của contour.
- Chu vi.
- Chất lượng và độ khép kín của đường cạnh.

Độ tròn có thể tính bằng:

```text
circularity = 4 * pi * area / perimeter^2
```

## 7. Kết quả cần lưu

```text
outputs_chapter_2_part_2/
├── II_4_canny_edges.png
├── II_4_closed_edges.png
├── II_4_contours.png
└── II_4_nhan_dang_hinh_dang.png
```

## 8. Checklist Câu II.4

- [ ] Phát hiện cạnh bằng Canny.
- [ ] Nối cạnh bằng morphology close.
- [ ] Làm rõ cạnh bằng dilate.
- [ ] Tìm contour.
- [ ] Lọc contour nhỏ.
- [ ] Xấp xỉ contour.
- [ ] Nhận dạng tam giác.
- [ ] Nhận dạng tứ giác.
- [ ] Nhận dạng hình tròn hoặc đường cong.
- [ ] Vẽ contour và nhãn lên ảnh kết quả.
