# Plan thực hành Canny Edge Detector — Phần II

Tài liệu này mô tả kế hoạch thực hiện theo đúng trình tự của notebook
`II_BAI_TAP_THUC_HANH_CANNY.ipynb`.

## 1. Mục tiêu

Sau khi hoàn thành phần thực hành, người học có thể:

1. Thực hiện phát hiện biên Canny bằng OpenCV và Scikit-image.
2. Giải thích ảnh hưởng của `sigma`, ngưỡng thấp và ngưỡng cao.
3. Điều chỉnh Canny cho ảnh tương phản thấp và ảnh có nhiều chi tiết.
4. Kết hợp Canny với Hough Circle để nhận dạng vùng có dạng hình tròn.
5. Hiển thị, thống kê và nhận xét kết quả của từng thử nghiệm.

Mỗi nội dung thực hành được trình bày theo cấu trúc:

```text
Mục tiêu → Ảnh đầu vào → Các bước thực hiện → Kết quả cần đạt → Nhận xét
```

## 2. Chuẩn bị môi trường và dữ liệu

### 2.1. Thư viện sử dụng

- `cv2`: đọc ảnh, chuyển ảnh xám, Gaussian Blur, Canny và Hough Circle.
- `numpy`: xử lý ma trận và thống kê số pixel cạnh.
- `matplotlib`: hiển thị ảnh và kết quả so sánh.
- `scipy.ndimage`: hỗ trợ các phép xử lý ảnh khi cần.
- `skimage.feature.canny`: thực hiện Canny bằng Scikit-image.

Các bước thực hiện:

1. Import đầy đủ thư viện.
2. Bật chế độ hiển thị biểu đồ trong notebook bằng `%matplotlib inline`.
3. Cấu hình kích thước hình, cỡ chữ và độ phân giải hiển thị.
4. In phiên bản OpenCV để kiểm tra môi trường.

### 2.2. Hàm tiện ích

Xây dựng hai hàm dùng chung:

- `show_images(images, titles, rows, figsize)`: hiển thị nhiều ảnh trong cùng một lưới.
- `print_edge_stats(name, edges)`: đếm số pixel cạnh và tính tỷ lệ trên toàn ảnh.

Kết quả cần đạt:

- Ảnh xám được hiển thị với colormap `gray`.
- Ảnh màu BGR được chuyển sang RGB trước khi hiển thị bằng Matplotlib.
- Các ô dư trong lưới ảnh được ẩn.

### 2.3. Dữ liệu đầu vào

| Nội dung      | Đường dẫn ảnh        | Vai trò                               |
| ------------- | -------------------- | ------------------------------------- |
| Ảnh đồi núi   | `image/chuong2.jpg`  | Ảnh chuẩn cho mục 2.1 và 2.2          |
| Ảnh sương mù  | `image/suongmu.jpg`  | Thử nghiệm ảnh tương phản thấp        |
| Ảnh cao tốc   | `image/caotoc.jpg`   | Thử nghiệm ảnh nhiều chi tiết         |
| Ảnh vòng xoay | `image/vongxoay.jpg` | Nhận dạng hình tròn bằng Hough Circle |

Với ảnh đồi núi:

1. Đọc ảnh màu bằng `cv2.imread()`.
2. Chuyển ảnh BGR sang ảnh xám.
3. Chuẩn hóa ảnh xám từ `[0, 255]` về ảnh `float` trong `[0, 1]`.
4. Hiển thị ảnh màu và ảnh xám.
5. Kiểm tra kích thước và kiểu dữ liệu của ảnh.

## 3. Thực hiện Canny bằng các thư viện

### 3.1. Canny với OpenCV

Mục tiêu:

- Phát hiện biên trên ảnh đồi núi bằng `cv2.Canny()`.
- Quan sát tác dụng của bước làm mượt trước khi phát hiện biên.

Các bước thực hiện:

1. Làm mượt ảnh xám bằng Gaussian Blur với kernel `(5, 5)` và `sigmaX=1.4`.
2. Chạy `cv2.Canny()` với `threshold1=50`, `threshold2=150`.
3. Hiển thị ảnh gốc, ảnh sau Gaussian Blur và ảnh biên.
4. In số lượng và tỷ lệ pixel cạnh.

Kết quả cần đạt:

- Các đường biên chính của ảnh được phát hiện.
- Nhiễu nhỏ được hạn chế nhờ Gaussian Blur.
- Kết quả Canny có kiểu ảnh nhị phân 8-bit trong khoảng `[0, 255]`.

### 3.2. Canny với Scikit-image

Mục tiêu:

- Thực hiện cùng bài toán bằng `skimage.feature.canny()`.
- Nhận biết sự khác nhau về thang dữ liệu giữa hai thư viện.

Các bước thực hiện:

1. Sử dụng ảnh xám dạng `float` trong khoảng `[0, 1]`.
2. Chạy Canny với `sigma=1.4`, `low_threshold=0.05`, `high_threshold=0.15`.
3. Hiển thị ảnh gốc và ảnh biên.
4. In số lượng và tỷ lệ pixel cạnh.

Kết quả cần đạt:

- Kết quả Scikit-image là mảng Boolean.
- Gaussian Blur được thực hiện bên trong hàm Canny thông qua `sigma`.
- Không dùng trực tiếp cùng giá trị ngưỡng của OpenCV vì hai thư viện sử dụng thang ảnh khác nhau.

### 3.3. Nội dung so sánh

| Tiêu chí         | OpenCV                              | Scikit-image                    |
| ---------------- | ----------------------------------- | ------------------------------- |
| Dữ liệu đầu vào  | Ảnh 8-bit `[0, 255]`                | Ảnh float `[0, 1]`              |
| Làm mượt         | Thực hiện trước bằng `GaussianBlur` | Điều khiển bằng tham số `sigma` |
| Kết quả          | Ảnh `uint8`                         | Mảng Boolean                    |
| Ngưỡng trong bài | `50/150`                            | `0.05/0.15`                     |

## 4. Thay đổi tham số và quan sát kết quả

### 4.1. Khảo sát ảnh hưởng của `sigma`

Mục tiêu:

- Đánh giá mức độ làm mượt ảnh trước khi phát hiện biên.

Các giá trị thử nghiệm:

```python
sigma_values = [0.5, 1.0, 1.5, 2.0, 3.0, 5.0]
```

Các bước thực hiện:

1. Giữ cố định `low_threshold=0.05` và `high_threshold=0.15`.
2. Chạy Scikit-image Canny lần lượt với từng giá trị `sigma`.
3. Đếm số pixel cạnh của mỗi kết quả.
4. Hiển thị sáu kết quả trong lưới `2 × 3`.
5. Ghi giá trị `sigma` và số pixel cạnh trên tiêu đề từng ảnh.

Nhận xét dự kiến:

- `sigma` nhỏ giữ nhiều chi tiết nhỏ nhưng có thể giữ cả nhiễu.
- `sigma` lớn làm mượt mạnh và chủ yếu giữ các đường biên lớn.
- `sigma` quá lớn có thể làm mất những cạnh quan trọng.

### 4.2. Khảo sát ngưỡng thấp và ngưỡng cao

Các cặp ngưỡng thử nghiệm:

```python
threshold_pairs = [
    (10, 50), (30, 100), (50, 150),
    (100, 200), (150, 250), (50, 100)
]
```

Các bước thực hiện:

1. Sử dụng cùng ảnh đã Gaussian Blur.
2. Chạy OpenCV Canny với từng cặp ngưỡng.
3. Tính số pixel cạnh và tỷ lệ `T_high/T_low`.
4. Hiển thị sáu kết quả trong lưới `2 × 3`.
5. So sánh mức độ nhạy, số cạnh giả và độ liên tục của cạnh.

Nhận xét dự kiến:

- Ngưỡng thấp tạo nhiều cạnh hơn nhưng dễ xuất hiện cạnh giả.
- Ngưỡng cao chỉ giữ cạnh mạnh nhưng có thể làm mất hoặc đứt cạnh yếu.
- Tỷ lệ ngưỡng `2:1` hoặc `3:1` là điểm khởi đầu phù hợp, sau đó cần điều chỉnh theo ảnh.

## 5. Canny trên các loại ảnh thực tế đặc thù

### 5.1. Ảnh sương mù, tương phản thấp

Mục tiêu:

- Khôi phục các cạnh mờ trong ảnh sương mù.
- So sánh giảm ngưỡng với tăng tương phản bằng CLAHE.

Các cấu hình thử nghiệm:

| Cấu hình          | Tiền xử lý                | `sigma` | Ngưỡng thấp/cao |
| ----------------- | ------------------------- | ------: | --------------: |
| Canny ban đầu     | Không                     |   `1.4` |     `0.05/0.15` |
| Canny ngưỡng thấp | Không                     |   `1.0` |     `0.01/0.05` |
| Canny sau CLAHE   | CLAHE `3.0`, lưới `8 × 8` |   `1.4` |     `0.05/0.15` |

Các bước thực hiện:

1. Đọc `image/suongmu.jpg` và chuyển sang ảnh xám.
2. Chuẩn hóa ảnh xám về `[0, 1]`.
3. Tăng tương phản cục bộ bằng CLAHE.
4. Chạy ba cấu hình Canny trong bảng trên.
5. Hiển thị ảnh gốc, ảnh xám, ảnh CLAHE và ba kết quả cạnh trong lưới `2 × 3`.

Nhận xét dự kiến:

- Ảnh tương phản thấp làm mất nhiều cạnh yếu.
- Giảm ngưỡng giúp bắt thêm cạnh nhưng cũng có thể tăng nhiễu.
- CLAHE làm rõ chi tiết cục bộ trước khi phát hiện cạnh và thường cho kết quả dễ quan sát hơn.

### 5.2. Ảnh cao tốc có nhiều chi tiết

Mục tiêu:

- Quan sát khả năng loại bớt chi tiết nhỏ bằng cách thay đổi `sigma`.

Các giá trị thử nghiệm:

```python
sigmas = [0.5, 1.5, 3.0]
```

Các bước thực hiện:

1. Đọc `image/caotoc.jpg` và chuyển sang ảnh xám dạng float.
2. Giữ ngưỡng ở `0.04/0.12`.
3. Chạy Canny với ba giá trị `sigma`.
4. Hiển thị ảnh gốc và ba ảnh biên trên cùng một hàng.
5. Ghi số pixel cạnh ở tiêu đề để hỗ trợ so sánh.

Nhận xét dự kiến:

- `sigma=0.5` giữ nhiều xe, vạch đường và chi tiết nhỏ.
- Khi tăng `sigma`, các chi tiết nhỏ giảm dần.
- `sigma=3.0` ưu tiên các đường biên lớn như lề và cấu trúc chính của đường.

## 6. Kết hợp Canny với Hough Circle

### 6.1. Mục tiêu

- Dùng Canny để minh họa đường biên trên ảnh vòng xoay.
- Dùng `cv2.HoughCircles()` để phát hiện vùng có dạng hình tròn.
- Vẽ tâm, bán kính và nhãn lên ảnh kết quả.

### 6.2. Các bước thực hiện

1. Đọc `image/vongxoay.jpg` và chuyển sang ảnh xám.
2. Làm mượt bằng Gaussian Blur với kernel `(9, 9)` và `sigma=2`.
3. Phát hiện hình tròn bằng Hough Gradient với các tham số:

```python
dp = 1.2
minDist = 100
param1 = 150
param2 = 40
minRadius = 200
maxRadius = 280
```

4. Kiểm tra kết quả khác `None` trước khi xử lý để tránh lỗi.
5. Làm tròn tọa độ và bán kính, sau đó vẽ đường tròn, tâm và nhãn `Vong Xoay`.
6. Chạy Canny với ngưỡng `50/150` để hiển thị ảnh biên tham khảo.
7. Hiển thị ảnh gốc, ảnh Canny và ảnh đã đánh dấu hình tròn.
8. In số hình tròn phát hiện được.

### 6.3. Kết quả cần đạt

- Vùng vòng xoay được khoanh đúng vị trí và kích thước tương đối.
- Tâm hình tròn được đánh dấu rõ ràng.
- Số hình tròn phát hiện được hiển thị trên tiêu đề và trong kết quả in.

Lưu ý: trong `HoughCircles`, `param1` là ngưỡng cao của bộ phát hiện Canny nội bộ, còn `param2` là ngưỡng bộ tích lũy dùng để chấp nhận một hình tròn.

## 7. Tiêu chí đánh giá kết quả

| Tiêu chí            | Nội dung quan sát                                                       |
| ------------------- | ----------------------------------------------------------------------- |
| Số pixel cạnh       | Cạnh quá nhiều có thể cho thấy ngưỡng thấp hoặc ảnh còn nhiễu           |
| Độ liên tục         | Các đường biên chính có liền mạch hay bị đứt đoạn                       |
| Cạnh giả            | Nền hoặc nhiễu có tạo ra nhiều cạnh không cần thiết hay không           |
| Mức giữ chi tiết    | Các chi tiết quan trọng còn xuất hiện sau khi tăng `sigma` hay không    |
| Khả năng thích nghi | Tham số có phù hợp với độ tương phản và mức chi tiết của từng ảnh không |
| Nhận dạng hình tròn | Vị trí tâm và bán kính có bám đúng vòng xoay hay không                  |

## 9. Kết luận dự kiến

Canny không có một bộ tham số tối ưu cho mọi ảnh. `sigma` quyết định mức làm mượt và lượng chi tiết được giữ lại, trong khi ngưỡng thấp và ngưỡng cao quyết định độ nhạy của quá trình phát hiện biên. Với ảnh tương phản thấp, cần giảm ngưỡng hoặc tăng tương phản bằng CLAHE; với ảnh nhiều chi tiết, có thể tăng `sigma` để ưu tiên các cấu trúc lớn. Khi kết hợp với Hough Circle, kết quả Canny và bước làm mượt hỗ trợ việc nhận dạng các đối tượng hình tròn trong ảnh thực tế.
