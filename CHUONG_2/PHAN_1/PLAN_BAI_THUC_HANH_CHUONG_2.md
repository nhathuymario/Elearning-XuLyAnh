# Plan thực hiện bài thực hành Chương 2

## 1. Mục tiêu

Bài thực hành được chia thành ba phần chính:

1. Toán tử điểm ảnh.
2. Lọc tuyến tính.
3. Bài tập nâng cao: phát hiện cạnh, thiết kế kernel và lọc phi tuyến.

Mỗi câu nên được trình bày theo cấu trúc:

- Mục tiêu.
- Input.
- Công thức hoặc nguyên lý.
- Code thực hiện.
- Output.
- Nhận xét kết quả.

## 2. Chuẩn bị môi trường

Cài đặt các thư viện cần thiết:

```bash
pip install -r requirements.txt
```

Import thư viện:

```python
from pathlib import Path

import cv2
import matplotlib.pyplot as plt
import numpy as np
```

Kết quả cần đạt:

- Python nhận được các thư viện.
- Notebook có thể chạy mà không gặp lỗi import.

## 3. Chuẩn bị dữ liệu đầu vào

Các công việc cần thực hiện:

1. Chọn một ảnh làm dữ liệu đầu vào.
2. Tạo thư mục lưu kết quả `outputs_chapter_2`.
3. Đọc ảnh bằng OpenCV.
4. Kiểm tra ảnh có được đọc thành công hay không.
5. Chuyển ảnh sang các định dạng cần sử dụng.
6. Viết hàm hiển thị nhiều ảnh để thuận tiện so sánh.

Các biến ảnh chính:

- `image_bgr`: ảnh BGR dùng để xử lý bằng OpenCV.
- `image_rgb`: ảnh RGB dùng để hiển thị bằng Matplotlib.
- `gray`: ảnh xám dùng cho cắt ngưỡng và phát hiện cạnh.

Code dự kiến:

```python
IMAGE_PATH = 'image/anh_chuong_2.jpg'
OUTPUT_DIR = Path('outputs_chapter_2')
OUTPUT_DIR.mkdir(exist_ok=True)

image_bgr = cv2.imread(IMAGE_PATH)
if image_bgr is None:
    raise FileNotFoundError(IMAGE_PATH)

image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2GRAY)
```

Kết quả cần kiểm tra:

- Ảnh được đọc đúng đường dẫn.
- Ảnh hiển thị đúng màu.
- Thư mục kết quả được tạo thành công.

## 4. Phần I: Toán tử điểm ảnh

### Câu I.1. Thay đổi độ sáng

Mục tiêu:

- Tạo ảnh sáng hơn.
- Tạo ảnh tối hơn.

Công thức:

```text
g(x, y) = f(x, y) + beta
```

Cách thực hiện:

1. Giữ `alpha = 1`.
2. Dùng `beta > 0` để tăng sáng.
3. Dùng `beta < 0` để giảm sáng.
4. Hiển thị ảnh gốc, ảnh sáng và ảnh tối cạnh nhau.
5. Lưu hai ảnh kết quả.

### Câu I.2. Thay đổi độ tương phản

Mục tiêu:

- Tạo ảnh có độ tương phản cao.
- Tạo ảnh có độ tương phản thấp.

Công thức:

```text
g(x, y) = alpha * f(x, y)
```

Cách thực hiện:

1. Dùng `alpha > 1` để tăng tương phản.
2. Dùng `0 < alpha < 1` để giảm tương phản.
3. So sánh vùng sáng và vùng tối của các ảnh.
4. Lưu ảnh kết quả.

### Câu I.3. Biến đổi âm bản

Mục tiêu:

- Đảo ngược giá trị sáng tối và màu sắc của ảnh.

Công thức:

```text
g(x, y) = 255 - f(x, y)
```

Cách thực hiện:

1. Lấy `255` trừ từng pixel.
2. Hiển thị ảnh gốc và ảnh âm bản.
3. Lưu ảnh âm bản.

### Câu I.4. Cắt ngưỡng

Mục tiêu:

- Chuyển ảnh xám thành ảnh nhị phân.

Quy tắc:

```text
g(x, y) = 255 nếu f(x, y) >= T
g(x, y) = 0 nếu f(x, y) < T
```

Cách thực hiện:

1. Sử dụng ảnh xám.
2. Chọn ngưỡng ban đầu `T = 128`.
3. Áp dụng `cv2.threshold()`.
4. Hiển thị ảnh gốc, ảnh xám và ảnh nhị phân.
5. Nhận xét vùng nào trở thành màu trắng hoặc màu đen.

## 5. Phần II: Lọc tuyến tính

### Câu II.1. Lọc trung bình

Mục tiêu:

- Làm mượt ảnh.
- Giảm nhiễu nhẹ.

Cách thực hiện:

1. Chọn kernel `3x3` hoặc `5x5`.
2. Áp dụng `cv2.blur()`.
3. Hiển thị ảnh trước và sau khi lọc.
4. Nhận xét mức độ mất chi tiết và mờ biên.

### Câu II.2. Lọc Gaussian

Mục tiêu:

- Làm mượt ảnh tự nhiên hơn lọc trung bình.
- Giảm nhiễu trước khi phát hiện cạnh.

Cách thực hiện:

1. Chọn kernel có kích thước lẻ.
2. Chọn giá trị sigma.
3. Áp dụng `cv2.GaussianBlur()`.
4. So sánh với lọc trung bình.

### Câu II.3. Làm sắc nét

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

## 6. Phần III: Bài tập nâng cao

### Câu III.1. Phát hiện cạnh Sobel và Prewitt

#### Sobel

Quy trình:

1. Sử dụng ảnh xám.
2. Tính gradient theo hướng `x`.
3. Tính gradient theo hướng `y`.
4. Kết hợp hai gradient.
5. Chuyển kết quả về ảnh 8-bit.
6. Lưu ảnh cạnh Sobel.

#### Prewitt

Quy trình:

1. Tạo kernel Prewitt theo hướng `x`.
2. Tạo kernel Prewitt theo hướng `y`.
3. Áp dụng hai kernel bằng `cv2.filter2D()`.
4. Kết hợp kết quả của hai hướng.
5. Lưu ảnh cạnh Prewitt.

#### So sánh Sobel và Prewitt

Tiêu chí đánh giá:

- Độ rõ của cạnh.
- Số lượng cạnh được phát hiện.
- Khả năng chống nhiễu.
- Khả năng giữ các chi tiết nhỏ.

Nhận xét dự kiến:

- Sobel thường giảm nhiễu tốt hơn một chút vì có trọng số lớn hơn ở hàng hoặc cột trung tâm.
- Prewitt có kernel đơn giản nhưng có thể nhạy với nhiễu hơn.

### Câu III.2. Tự thiết kế kernel

#### Kernel Emboss

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

#### Kernel Laplacian

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

### Câu III.3. So sánh các loại lọc

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

### Câu III.4. Áp dụng lọc phi tuyến

#### Median filter

Mục tiêu:

- Loại bỏ nhiễu muối tiêu.

Cách thực hiện:

1. Chọn kernel `5x5`.
2. Áp dụng `cv2.medianBlur()`.
3. So sánh ảnh trước và sau khi lọc.

#### Bilateral filter

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

## 7. Lưu và kiểm tra kết quả

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

## 8. Hoàn thiện báo cáo

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

## 9. Checklist hoàn thành

- [ ] Cài đặt đầy đủ thư viện.
- [ ] Đọc và hiển thị đúng ảnh đầu vào.
- [ ] Hoàn thành thay đổi độ sáng.
- [ ] Hoàn thành thay đổi độ tương phản.
- [ ] Hoàn thành biến đổi âm bản.
- [ ] Hoàn thành cắt ngưỡng.
- [ ] Hoàn thành lọc trung bình.
- [ ] Hoàn thành lọc Gaussian.
- [ ] Hoàn thành làm sắc nét.
- [ ] Hoàn thành phát hiện cạnh Sobel.
- [ ] Hoàn thành phát hiện cạnh Prewitt.
- [ ] Hoàn thành kernel Emboss.
- [ ] Hoàn thành kernel Laplacian.
- [ ] Hoàn thành bảng so sánh các bộ lọc.
- [ ] Hoàn thành lọc Median và Bilateral.
- [ ] Lưu đầy đủ ảnh đầu ra.
- [ ] Chạy lại toàn bộ notebook không có lỗi.
- [ ] Viết nhận xét và kết luận.

## 10. Kết luận dự kiến

Bài thực hành giúp hiểu cách thay đổi trực tiếp giá trị pixel, sử dụng
kernel để lọc ảnh, giảm nhiễu, làm sắc nét và phát hiện cạnh. Qua việc
so sánh các phương pháp, có thể lựa chọn bộ lọc phù hợp với từng loại
ảnh và mục tiêu xử lý khác nhau.
