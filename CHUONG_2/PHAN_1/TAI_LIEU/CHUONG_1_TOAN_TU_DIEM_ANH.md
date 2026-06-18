# Phần I: Toán tử điểm ảnh

## 1. Mục tiêu

Phần này tập trung vào:

1. Chuẩn bị môi trường xử lý ảnh.
2. Chuẩn bị dữ liệu đầu vào.
3. Thực hiện các toán tử điểm ảnh.

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

## 4. Các câu thực hành

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
