# Phần II: Bài tập thực hành Canny

Tài liệu này bám đúng từng chấm tròn của đề bài và notebook
`II_BAI_TAP_THUC_HANH_CANNY.ipynb`.

## Câu II.1. Thực hiện Canny bằng các thư viện

### Ý 1: OpenCV

- Dùng `cv2.Canny()` trên ảnh xám 8-bit.
- Nên làm mượt Gaussian trước khi chạy.
- Phù hợp xử lý nhanh, camera, video và triển khai thực tế.
- Kết quả thử nghiệm: tỷ lệ pixel cạnh khoảng `3.88%`.

### Ý 2: Scikit-image

- Dùng `skimage.feature.canny()` trên ảnh float trong khoảng `0-1`.
- Có thể điều chỉnh trực tiếp `sigma`.
- Phù hợp thử nghiệm, nghiên cứu và phân tích tham số.
- Kết quả cấu hình thử nghiệm: tỷ lệ pixel cạnh khoảng `7.11%`.

Không dùng trực tiếp cùng giá trị ngưỡng cho hai thư viện vì thang ảnh khác nhau.

## Câu II.2. Thay đổi tham số và quan sát kết quả

### Ý 1: Thay đổi `sigma`, ngưỡng thấp và ngưỡng cao

- `sigma` nhỏ giữ chi tiết nhưng dễ nhiễu.
- `sigma` lớn giảm nhiễu nhưng có thể mất cạnh nhỏ.
- Ngưỡng thấp giữ cạnh yếu nhưng dễ có cạnh giả.
- Ngưỡng cao giữ cạnh mạnh nhưng có thể làm đứt cạnh.

### Ý 2: So sánh với giá trị mặc định

- Mặc định Scikit-image cho khoảng `11.93%` pixel cạnh.
- Cấu hình cân bằng cho khoảng `7.11%` pixel cạnh.
- OpenCV chọn ngưỡng tự động từ trung vị ảnh cho khoảng `10.58%` pixel cạnh.

Giá trị mặc định phù hợp để bắt đầu thử nghiệm, không phải cấu hình tối ưu cho
mọi ảnh.

## Câu II.3. Áp dụng cho các loại ảnh khác nhau

### Ý 1: Thử nghiệm và phương án xử lý

| Loại ảnh | Vấn đề | Phương án phù hợp |
|---|---|---|
| Ảnh nhiễu, ban đêm, ISO cao | Nhiều cạnh giả | Median hoặc bilateral, tăng ngưỡng |
| Mưa | Hạt và vệt mưa tạo cạnh giả | Median/Gaussian, dùng ROI, tăng ngưỡng |
| Sương mù, trời âm u | Tương phản thấp | CLAHE rồi chọn lại ngưỡng theo tỷ lệ cạnh |
| Nắng gắt, bóng đổ | Chênh sáng lớn | CLAHE cục bộ, ngưỡng tự động hoặc theo vùng |
| Ảnh nhiều chi tiết | Quá nhiều cạnh nhỏ | Gaussian mạnh hơn, tăng `sigma` và ngưỡng |
| Ban ngày, ảnh rõ | Ít nhiễu | Gaussian nhẹ, ngưỡng trung bình |

### Ý 2: Đánh giá và kết luận

- Ảnh nhiễu chạy trực tiếp: khoảng `32.27%` pixel cạnh.
- Sau Median + Canny: còn khoảng `2.22%`, giảm mạnh cạnh giả.
- Ảnh nhiều chi tiết chạy trực tiếp: khoảng `16.86%`.
- Sau Gaussian + Canny: còn khoảng `1.61%`.
- CLAHE giúp tìm lại nhiều cạnh trong ảnh tương phản thấp, nhưng cũng có thể
  khuếch đại nhiễu nên phải điều chỉnh ngưỡng sau đó.
- Với ảnh tương phản thấp trong bài, CLAHE kết hợp ngưỡng `110-220` cho tỷ lệ
  cạnh khoảng `7.72%`, phù hợp hơn cấu hình `55-130` tạo quá nhiều cạnh.

Không tồn tại một bộ tham số phù hợp cho mọi ảnh.

### Khoảng tỷ lệ cạnh tham khảo

Với ảnh dùng trong bài này:

- Khoảng `2-8%`: thường phù hợp để giữ các cạnh chính.
- Khoảng `8-15%`: giữ nhiều chi tiết, cần xem mục tiêu bài toán.
- Trên `15%`: thường có quá nhiều cạnh nhỏ hoặc cạnh giả.

Đây là khoảng thực nghiệm cho ảnh của bài, không phải tiêu chuẩn cố định.

## Câu II.4. Kết hợp Canny với kỹ thuật khác

### Ý 1: Kết hợp phân đoạn

Quy trình:

1. Canny lấy đường biên.
2. Morphology close nối đoạn cạnh.
3. Dilate làm cạnh rõ hơn.
4. Tìm contour khép kín.
5. Tô vùng contour để tạo kết quả phân đoạn.

Phù hợp khi vật thể có biên rõ, khép kín và tách biệt với nền.

### Ý 2: Kết hợp nhận dạng hình dạng

Quy trình:

1. Lọc contour theo diện tích.
2. Dùng `approxPolyDP` để xấp xỉ đa giác.
3. Kết hợp số đỉnh, tỷ lệ khung bao và độ tròn.
4. Gán nhãn tam giác, hình chữ nhật, hình vuông, hình tròn hoặc đối tượng khác.

Phù hợp với biển báo, linh kiện và hình học cơ bản trong điều kiện ánh sáng
ổn định, camera ít rung và vật thể không bị che khuất.

## Kết quả đã lưu

```text
outputs_chapter_2_part_2/
├── II_1_so_sanh_hai_thu_vien.png
├── II_2_so_sanh_tham_so.png
├── II_2_so_sanh_mac_dinh.png
├── II_3_anh_nhieu_so_sanh.png
├── II_3_anh_tuong_phan_thap_so_sanh.png
├── II_3_anh_nhieu_chi_tiet_so_sanh.png
├── II_4_phan_doan.png
└── II_4_nhan_dang.png
```
