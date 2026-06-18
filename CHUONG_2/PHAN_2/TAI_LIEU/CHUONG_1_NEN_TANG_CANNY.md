# Phần I: Lý thuyết thuật toán Canny

## 1. Mục tiêu

Chương này tập trung vào:

1. Chuẩn bị môi trường và ảnh đầu vào.
2. Tìm hiểu các bước của Canny Edge Detector.
3. Phân tích các tham số quan trọng.
4. Tìm hiểu ưu điểm, nhược điểm và ứng dụng.

## 2. Chuẩn bị môi trường

Cài đặt các thư viện:

```bash
pip install -r requirements.txt
```

Import thư viện:

```python
from pathlib import Path

import cv2
import matplotlib.pyplot as plt
import numpy as np
from skimage import feature, img_as_ubyte
from skimage.color import rgb2gray
```

Chuẩn bị dữ liệu:

```python
IMAGE_PATH = 'image/sample_chapter_part_2.jpg'
OUTPUT_DIR = Path('outputs_chapter_2_part_2')
OUTPUT_DIR.mkdir(exist_ok=True)

image_bgr = cv2.imread(IMAGE_PATH)
if image_bgr is None:
    raise FileNotFoundError(IMAGE_PATH)

image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2GRAY)
```

## Câu I.1. Các bước của thuật toán Canny

Canny Edge Detector gồm các bước:

1. Làm mượt ảnh bằng Gaussian filter.
2. Tính gradient theo hướng `x` và `y`.
3. Tính độ lớn và hướng gradient.
4. Làm mảnh cạnh bằng Non-maximum suppression.
5. Phân loại cạnh bằng double threshold.
6. Nối cạnh bằng hysteresis.

Code minh họa:

```python
blurred = cv2.GaussianBlur(gray, (5, 5), 1.4)

grad_x = cv2.Sobel(
    blurred, cv2.CV_64F, 1, 0, ksize=3
)
grad_y = cv2.Sobel(
    blurred, cv2.CV_64F, 0, 1, ksize=3
)

gradient = cv2.magnitude(grad_x, grad_y)
gradient_8bit = cv2.convertScaleAbs(gradient)

canny_final = cv2.Canny(gray, 80, 160)
```

Kết quả cần hiển thị:

- Ảnh xám.
- Ảnh sau Gaussian.
- Độ lớn gradient.
- Kết quả Canny cuối cùng.

## Câu I.2. Tham số quan trọng và ảnh hưởng

- `sigma`: mức làm mượt Gaussian.
- `threshold_low`: ngưỡng xác định cạnh yếu.
- `threshold_high`: ngưỡng xác định cạnh mạnh.

Các cấu hình thử nghiệm:

```python
settings = [
    ('Nhạy', 40, 100),
    ('Cân bằng', 80, 160),
    ('Ít cạnh', 130, 240)
]

for name, low, high in settings:
    edges = cv2.Canny(gray, low, high)
```

Nhận xét dự kiến:

- Ngưỡng thấp tạo nhiều cạnh nhưng dễ có cạnh giả.
- Ngưỡng cao chỉ giữ cạnh mạnh nhưng có thể làm đứt cạnh.
- Hai ngưỡng cần có khoảng cách hợp lý để hysteresis hoạt động tốt.

## Câu I.3. Ưu điểm, nhược điểm và ứng dụng

Ưu điểm:

- Cạnh thu được mảnh và rõ.
- Có bước giảm nhiễu.
- Có khả năng nối cạnh yếu với cạnh mạnh.
- Ổn định hơn Sobel hoặc Prewitt trong nhiều trường hợp.

Nhược điểm:

- Phụ thuộc vào sigma và hai giá trị ngưỡng.
- Chậm hơn các toán tử gradient đơn giản.
- Ảnh nhiều nhiễu vẫn cần tiền xử lý phù hợp.

### Ứng dụng

- Phát hiện vật thể.
- Tìm contour.
- Kiểm tra lỗi sản phẩm.
- Phân đoạn ảnh.
- Nhận dạng hình dạng.
- Phân tích ảnh y tế.

## 4. Checklist phần I

- [ ] Cài đặt đầy đủ thư viện.
- [ ] Đọc được ảnh đầu vào.
- [ ] Minh họa bước Gaussian.
- [ ] Minh họa gradient.
- [ ] Hiểu double threshold và hysteresis.
- [ ] Thử ít nhất ba cặp ngưỡng.
- [ ] Viết nhận xét về ưu và nhược điểm.
