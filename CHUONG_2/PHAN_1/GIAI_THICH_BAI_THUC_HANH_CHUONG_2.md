# Giải thích bài thực hành chương 2

File này giải thích các đoạn code trong `Bai_thuc_hanh_chuong_2.ipynb`.

## 1. Chuẩn bị thư viện và ảnh đầu vào

```python
from pathlib import Path

import cv2
import matplotlib.pyplot as plt
import numpy as np
```

Ý nghĩa:

- `Path`: dùng để tạo và quản lý đường dẫn thư mục, file.
- `cv2`: thư viện OpenCV, dùng để đọc, xử lý và lưu ảnh.
- `matplotlib.pyplot`: dùng để hiển thị ảnh trong notebook.
- `numpy`: dùng để tạo và xử lý ma trận, đặc biệt là các kernel lọc ảnh.

```python
IMAGE_PATH = 'image/anh_chuong_2.jpg'
OUTPUT_DIR = Path('outputs_chapter_2')
OUTPUT_DIR.mkdir(exist_ok=True)
```

Ý nghĩa:

- `IMAGE_PATH`: đường dẫn đến ảnh đầu vào.
- `OUTPUT_DIR`: thư mục lưu các ảnh kết quả sau khi xử lý.
- `mkdir(exist_ok=True)`: tạo thư mục nếu chưa tồn tại. Nếu thư mục đã có rồi thì không báo lỗi.

```python
image_bgr = cv2.imread(IMAGE_PATH)
if image_bgr is None:
    raise FileNotFoundError(IMAGE_PATH)
image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2GRAY)
```

Ý nghĩa:

- `cv2.imread(...)`: đọc ảnh từ file.
- `image_bgr`: ảnh gốc theo hệ màu BGR của OpenCV.
- `if image_bgr is None`: kiểm tra xem ảnh có đọc được không.
- `cv2.COLOR_BGR2RGB`: chuyển ảnh từ BGR sang RGB để hiển thị đúng màu bằng Matplotlib.
- `cv2.COLOR_BGR2GRAY`: chuyển ảnh màu sang ảnh xám.

```python
def show_images(items, cols=None):
    cols = cols or len(items)
    rows = (len(items) + cols - 1) // cols
    fig, axes = plt.subplots(rows, cols, figsize=(4 * cols, 4 * rows), squeeze=False)
    for ax, (title, img) in zip(axes.ravel(), items):
        ax.imshow(img, cmap='gray' if img.ndim == 2 else None)
        ax.set_title(title)
        ax.axis('off')
    for ax in axes.ravel()[len(items):]:
        ax.axis('off')
    plt.tight_layout()
    plt.show()
```

Ý nghĩa:

- Hàm `show_images` dùng để hiển thị một hoặc nhiều ảnh cạnh nhau.
- `items`: danh sách gồm tiêu đề và ảnh, ví dụ `('Ảnh gốc', image_rgb)`.
- `cols`: số cột khi hiển thị ảnh.
- `plt.subplots(...)`: tạo khung hiển thị nhiều ảnh.
- `ax.imshow(...)`: hiển thị ảnh.
- Nếu ảnh là ảnh xám, tức `img.ndim == 2`, thì dùng `cmap='gray'`.
- `ax.axis('off')`: tắt trục tọa độ để ảnh nhìn gọn hơn.
- `plt.tight_layout()`: tự căn chỉnh bố cục.

## 2. Câu I.1. Thay đổi độ sáng

```python
brighter = cv2.convertScaleAbs(image_bgr, alpha=1, beta=50)
darker = cv2.convertScaleAbs(image_bgr, alpha=1, beta=-50)
```

Ý nghĩa:

- Đoạn code này tạo ra 2 ảnh mới từ ảnh gốc: một ảnh sáng hơn và một ảnh tối hơn.
- `cv2.convertScaleAbs(...)` biến đổi giá trị pixel theo công thức:

```python
new_pixel = alpha * pixel + beta
```

- `alpha=1`: giữ nguyên độ tương phản.
- `beta=50`: cộng thêm 50 vào mỗi pixel, làm ảnh sáng hơn.
- `beta=-50`: trừ 50 khỏi mỗi pixel, làm ảnh tối hơn.
- Giá trị pixel sau xử lý vẫn được đưa về khoảng hợp lệ `0` đến `255`.

```python
cv2.imwrite(str(OUTPUT_DIR / 'I_1_tang_do_sang.png'), brighter)
cv2.imwrite(str(OUTPUT_DIR / 'I_1_giam_do_sang.png'), darker)
```

Ý nghĩa:

- Lưu ảnh tăng độ sáng vào file `I_1_tang_do_sang.png`.
- Lưu ảnh giảm độ sáng vào file `I_1_giam_do_sang.png`.

```python
show_images([
    ('Gốc', image_rgb),
    ('Tăng độ sáng', cv2.cvtColor(brighter, cv2.COLOR_BGR2RGB)),
    ('Giảm độ sáng', cv2.cvtColor(darker, cv2.COLOR_BGR2RGB)),
])
```

Ý nghĩa:

- Hiển thị 3 ảnh để so sánh: ảnh gốc, ảnh tăng sáng và ảnh giảm sáng.
- Vì ảnh OpenCV đang ở dạng BGR nên cần đổi sang RGB trước khi hiển thị.

## 3. Câu I.2. Thay đổi độ tương phản

```python
high_contrast = cv2.convertScaleAbs(image_bgr, alpha=1.6)
low_contrast = cv2.convertScaleAbs(image_bgr, alpha=0.6)
```

Ý nghĩa:

- Đoạn code này thay đổi độ tương phản của ảnh.
- `alpha` là hệ số nhân với giá trị pixel.
- `alpha=1.6`: tăng độ tương phản, vùng sáng sáng hơn và vùng tối tối hơn.
- `alpha=0.6`: giảm độ tương phản, ảnh nhìn nhạt hơn và ít chênh lệch sáng tối hơn.

```python
cv2.imwrite(str(OUTPUT_DIR / 'I_2_tang_tuong_phan.png'), high_contrast)
cv2.imwrite(str(OUTPUT_DIR / 'I_2_giam_tuong_phan.png'), low_contrast)
```

Ý nghĩa:

- Lưu ảnh tăng tương phản.
- Lưu ảnh giảm tương phản.

```python
show_images([
    ('Gốc', image_rgb),
    ('Tăng tương phản', cv2.cvtColor(high_contrast, cv2.COLOR_BGR2RGB)),
    ('Giảm tương phản', cv2.cvtColor(low_contrast, cv2.COLOR_BGR2RGB)),
])
```

Ý nghĩa:

- Hiển thị ảnh gốc và 2 ảnh sau khi thay đổi độ tương phản để so sánh trực quan.

## 4. Câu I.3. Biến đổi âm bản

```python
negative = 255 - image_bgr
```

Ý nghĩa:

- Tạo ảnh âm bản từ ảnh gốc.
- Với ảnh 8-bit, mỗi pixel có giá trị từ `0` đến `255`.
- Công thức âm bản:

```python
new_pixel = 255 - old_pixel
```

- Pixel càng sáng sẽ thành càng tối.
- Pixel càng tối sẽ thành càng sáng.

```python
cv2.imwrite(str(OUTPUT_DIR / 'I_3_am_ban.png'), negative)
```

Ý nghĩa:

- Lưu ảnh âm bản vào thư mục kết quả.

```python
show_images([('Ảnh âm bản', cv2.cvtColor(negative, cv2.COLOR_BGR2RGB))])
```

Ý nghĩa:

- Chuyển ảnh từ BGR sang RGB rồi hiển thị ảnh âm bản.

## 5. Câu I.4. Cắt ngưỡng

```python
_, binary = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)
```

Ý nghĩa:

- Đoạn code này chuyển ảnh xám thành ảnh nhị phân.
- Ảnh nhị phân chỉ có 2 giá trị chính: `0` và `255`.
- `gray`: ảnh xám đầu vào.
- `128`: giá trị ngưỡng.
- `255`: giá trị gán cho pixel nếu pixel lớn hơn ngưỡng.
- `cv2.THRESH_BINARY`: kiểu cắt ngưỡng nhị phân.

Quy tắc:

```python
if pixel >= 128:
    pixel = 255
else:
    pixel = 0
```

```python
cv2.imwrite(str(OUTPUT_DIR / 'I_4_cat_nguong.png'), binary)
show_images([('Ảnh xám', gray), ('Ngưỡng 128', binary)])
```

Ý nghĩa:

- Lưu ảnh sau cắt ngưỡng.
- Hiển thị ảnh xám và ảnh nhị phân để so sánh.

## 6. Câu II.1. Lọc trung bình

```python
mean_blur = cv2.blur(image_bgr, (5, 5))
```

Ý nghĩa:

- Dùng bộ lọc trung bình để làm mờ ảnh.
- `(5, 5)` là kích thước kernel, tức vùng lân cận 5 hàng và 5 cột.
- Mỗi pixel mới được tính bằng trung bình cộng của các pixel xung quanh nó.

Tác dụng:

- Làm ảnh mượt hơn.
- Giảm nhiễu nhẹ.
- Có thể làm mất chi tiết và làm mờ biên.

```python
cv2.imwrite(str(OUTPUT_DIR / 'II_1_loc_trung_binh.png'), mean_blur)
show_images([('Lọc trung bình', cv2.cvtColor(mean_blur, cv2.COLOR_BGR2RGB))])
```

Ý nghĩa:

- Lưu ảnh đã lọc trung bình.
- Chuyển BGR sang RGB rồi hiển thị ảnh.

## 7. Câu II.2. Lọc Gaussian

```python
gaussian_blur = cv2.GaussianBlur(image_bgr, (5, 5), 1.2)
```

Ý nghĩa:

- Dùng bộ lọc Gaussian để làm mờ ảnh.
- `(5, 5)`: kích thước kernel.
- `1.2`: độ lệch chuẩn, điều khiển mức độ làm mờ.
- Khác với lọc trung bình, Gaussian cho pixel gần tâm trọng số lớn hơn pixel ở xa tâm.

Tác dụng:

- Làm mượt ảnh tự nhiên hơn lọc trung bình.
- Giảm nhiễu.
- Thường được dùng trước các bước phát hiện cạnh.

```python
cv2.imwrite(str(OUTPUT_DIR / 'II_2_loc_gaussian.png'), gaussian_blur)
show_images([('Lọc Gaussian', cv2.cvtColor(gaussian_blur, cv2.COLOR_BGR2RGB))])
```

Ý nghĩa:

- Lưu ảnh sau lọc Gaussian.
- Hiển thị ảnh sau khi xử lý.

## 8. Câu II.3. Làm sắc nét

```python
sharpen_kernel = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
sharpened = cv2.filter2D(image_bgr, -1, sharpen_kernel)
```

Ý nghĩa:

- Tạo kernel làm sắc nét ảnh.
- `np.array(...)`: tạo ma trận kernel.
- `cv2.filter2D(...)`: áp dụng phép lọc 2D lên ảnh.
- `-1`: ảnh đầu ra có cùng độ sâu dữ liệu với ảnh đầu vào.

Kernel:

```python
[[ 0, -1,  0],
 [-1,  5, -1],
 [ 0, -1,  0]]
```

Ý nghĩa kernel:

- Giá trị `5` ở giữa làm nổi bật pixel trung tâm.
- Các giá trị `-1` xung quanh làm tăng sự khác biệt giữa pixel trung tâm và vùng lân cận.
- Kết quả là cạnh và chi tiết trong ảnh rõ hơn.

```python
cv2.imwrite(str(OUTPUT_DIR / 'II_3_lam_sac_net.png'), sharpened)
show_images([('Làm sắc nét', cv2.cvtColor(sharpened, cv2.COLOR_BGR2RGB))])
```

Ý nghĩa:

- Lưu ảnh đã làm sắc nét.
- Hiển thị ảnh sau xử lý.

## 9. Câu III.1. Phát hiện cạnh Sobel và Prewitt

```python
sx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
sy = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
sobel = cv2.convertScaleAbs(cv2.magnitude(sx, sy))
```

Ý nghĩa:

- Sobel dùng để phát hiện cạnh trong ảnh xám.
- `sx`: đạo hàm theo trục x, phát hiện cạnh theo chiều dọc.
- `sy`: đạo hàm theo trục y, phát hiện cạnh theo chiều ngang.
- `cv2.CV_64F`: dùng kiểu số thực để tránh mất dữ liệu khi tính đạo hàm.
- `ksize=3`: kích thước kernel Sobel là 3x3.
- `cv2.magnitude(sx, sy)`: tính độ lớn gradient từ 2 hướng x và y.
- `cv2.convertScaleAbs(...)`: chuyển kết quả về dạng ảnh 8-bit để hiển thị.

```python
kx = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]], np.float32)
ky = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]], np.float32)
```

Ý nghĩa:

- Tạo 2 kernel Prewitt.
- `kx`: phát hiện thay đổi cường độ theo trục x.
- `ky`: phát hiện thay đổi cường độ theo trục y.

```python
px = cv2.filter2D(gray, cv2.CV_32F, kx)
py = cv2.filter2D(gray, cv2.CV_32F, ky)
prewitt = cv2.convertScaleAbs(cv2.magnitude(px, py))
```

Ý nghĩa:

- Áp dụng kernel Prewitt lên ảnh xám.
- `px`: kết quả lọc theo hướng x.
- `py`: kết quả lọc theo hướng y.
- `prewitt`: ảnh biên cuối cùng sau khi kết hợp 2 hướng.

```python
cv2.imwrite(str(OUTPUT_DIR / 'III_1_sobel.png'), sobel)
cv2.imwrite(str(OUTPUT_DIR / 'III_1_prewitt.png'), prewitt)
show_images([('Sobel', sobel), ('Prewitt', prewitt)])
```

Ý nghĩa:

- Lưu ảnh biên Sobel và Prewitt.
- Hiển thị 2 kết quả để so sánh.

## 10. Câu III.2. Tự thiết kế kernel

```python
emboss_kernel = np.array([[-2, -1, 0], [-1, 1, 1], [0, 1, 2]])
laplacian_kernel = np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]])
```

Ý nghĩa:

- Tạo 2 kernel tùy chỉnh.
- `emboss_kernel`: tạo hiệu ứng nổi khối.
- `laplacian_kernel`: phát hiện cạnh bằng toán tử Laplacian.

```python
emboss = cv2.filter2D(image_bgr, -1, emboss_kernel)
custom_edge = cv2.convertScaleAbs(cv2.filter2D(gray, cv2.CV_32F, laplacian_kernel))
```

Ý nghĩa:

- `emboss`: ảnh sau khi áp dụng kernel nổi khối.
- `custom_edge`: ảnh phát hiện cạnh bằng kernel Laplacian.
- Với Laplacian, ảnh được xử lý trên ảnh xám vì phát hiện cạnh chủ yếu dựa vào thay đổi cường độ sáng.

```python
cv2.imwrite(str(OUTPUT_DIR / 'III_2_kernel_emboss.png'), emboss)
cv2.imwrite(str(OUTPUT_DIR / 'III_2_kernel_laplacian.png'), custom_edge)
show_images([
    ('Emboss', cv2.cvtColor(emboss, cv2.COLOR_BGR2RGB)),
    ('Laplacian', custom_edge),
])
```

Ý nghĩa:

- Lưu ảnh emboss và ảnh cạnh Laplacian.
- Hiển thị 2 kết quả xử lý.

## 11. Câu III.3. So sánh các loại lọc

```python
mean_blur = cv2.blur(image_bgr, (5, 5))
gaussian_blur = cv2.GaussianBlur(image_bgr, (5, 5), 1.2)
median_filter = cv2.medianBlur(image_bgr, 5)
bilateral_filter = cv2.bilateralFilter(image_bgr, 9, 75, 75)
sharpened = cv2.filter2D(image_bgr, -1, sharpen_kernel)
```

Ý nghĩa:

- Áp dụng nhiều phương pháp lọc khác nhau trên cùng một ảnh để so sánh.
- `cv2.blur`: lọc trung bình, làm mờ đơn giản.
- `cv2.GaussianBlur`: lọc Gaussian, làm mờ tự nhiên hơn.
- `cv2.medianBlur`: lọc trung vị, hiệu quả với nhiễu muối tiêu.
- `cv2.bilateralFilter`: lọc song phương, làm mượt nhưng vẫn giữ biên tốt.
- `cv2.filter2D` với `sharpen_kernel`: làm sắc nét ảnh.

```python
filters = [
    ('Gốc', image_bgr), ('Trung bình', mean_blur), ('Gaussian', gaussian_blur),
    ('Median', median_filter), ('Bilateral', bilateral_filter), ('Sắc nét', sharpened),
]
```

Ý nghĩa:

- Tạo danh sách các ảnh cần hiển thị.
- Mỗi phần tử gồm tên ảnh và dữ liệu ảnh tương ứng.

```python
show_images([(name, cv2.cvtColor(img, cv2.COLOR_BGR2RGB)) for name, img in filters], cols=3)
```

Ý nghĩa:

- Chuyển toàn bộ ảnh từ BGR sang RGB.
- Hiển thị các ảnh thành bảng 3 cột để dễ so sánh.

Nhận xét:

- Lọc trung bình làm ảnh mờ nhanh nhưng dễ mất chi tiết.
- Lọc Gaussian mượt hơn và tự nhiên hơn.
- Lọc median tốt khi ảnh có nhiễu dạng chấm đen trắng.
- Lọc bilateral giữ biên tốt hơn các bộ lọc làm mờ thông thường.
- Làm sắc nét giúp chi tiết rõ hơn nhưng nếu dùng quá mạnh có thể làm ảnh gắt.

## 12. Câu III.4. Áp dụng lọc phi tuyến

```python
median_filter = cv2.medianBlur(image_bgr, 5)
bilateral_filter = cv2.bilateralFilter(image_bgr, 9, 75, 75)
```

Ý nghĩa:

- Áp dụng 2 bộ lọc phi tuyến: median và bilateral.
- Lọc phi tuyến không tính pixel mới bằng tổng có trọng số đơn giản như lọc tuyến tính.

### Median filter

```python
median_filter = cv2.medianBlur(image_bgr, 5)
```

Ý nghĩa:

- Mỗi pixel được thay bằng giá trị trung vị trong vùng lân cận.
- `5`: kích thước kernel là 5x5.
- Rất hiệu quả để khử nhiễu muối tiêu.

### Bilateral filter

```python
bilateral_filter = cv2.bilateralFilter(image_bgr, 9, 75, 75)
```

Ý nghĩa:

- Làm mượt ảnh nhưng vẫn cố gắng giữ lại cạnh.
- `9`: đường kính vùng lân cận.
- `75`: mức độ xét chênh lệch màu.
- `75`: mức độ xét khoảng cách không gian.

```python
cv2.imwrite(str(OUTPUT_DIR / 'III_4_median_filter.png'), median_filter)
cv2.imwrite(str(OUTPUT_DIR / 'III_4_bilateral_filter.png'), bilateral_filter)
show_images([
    ('Median', cv2.cvtColor(median_filter, cv2.COLOR_BGR2RGB)),
    ('Bilateral', cv2.cvtColor(bilateral_filter, cv2.COLOR_BGR2RGB)),
])
```

Ý nghĩa:

- Lưu ảnh sau lọc median.
- Lưu ảnh sau lọc bilateral.
- Hiển thị 2 ảnh kết quả để so sánh.

## Tổng kết chương 2

Trong bài thực hành chương 2, các thao tác chính gồm:

- Thay đổi độ sáng bằng cách cộng hoặc trừ giá trị pixel.
- Thay đổi độ tương phản bằng cách nhân giá trị pixel với hệ số `alpha`.
- Tạo ảnh âm bản bằng công thức `255 - pixel`.
- Cắt ngưỡng để tạo ảnh nhị phân.
- Làm mờ ảnh bằng lọc trung bình và Gaussian.
- Làm sắc nét ảnh bằng kernel tùy chỉnh.
- Phát hiện cạnh bằng Sobel, Prewitt và Laplacian.
- So sánh các bộ lọc tuyến tính và phi tuyến.

Các ảnh kết quả được lưu trong thư mục `outputs_chapter_2`.
