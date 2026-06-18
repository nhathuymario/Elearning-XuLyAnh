# Plan bài thực hành Chương 1

## 1. Nội dung chính

Chương 1 tập trung vào các thao tác cơ bản với ảnh:

1. Cài đặt thư viện xử lý ảnh.
2. Đọc, hiển thị và lưu ảnh.
3. Chuyển đổi không gian màu.
4. Cắt xén và thay đổi kích thước ảnh.
5. Vẽ hình cơ bản và thêm văn bản.

Mỗi câu nên trình bày theo cấu trúc:

- Mục tiêu.
- Dữ liệu đầu vào.
- Nguyên lý hoặc hàm sử dụng.
- Code thực hiện.
- Hình ảnh kết quả.
- Nhận xét.

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
from PIL import Image
```

Kết quả cần đạt:

- Import được OpenCV, Pillow, NumPy và Matplotlib.
- Notebook chạy không có lỗi thư viện.

## 3. Chuẩn bị ảnh đầu vào

Các bước thực hiện:

1. Chọn ảnh `image/sample_chapter_1.jpg`.
2. Tạo thư mục `outputs_chapter_1`.
3. Đọc ảnh bằng OpenCV.
4. Kiểm tra ảnh có tồn tại hay không.
5. Chuyển ảnh từ BGR sang RGB để hiển thị.

Code dự kiến:

```python
IMAGE_PATH = 'image/sample_chapter_1.jpg'
OUTPUT_DIR = Path('outputs_chapter_1')
OUTPUT_DIR.mkdir(exist_ok=True)

image_bgr = cv2.imread(IMAGE_PATH)
if image_bgr is None:
    raise FileNotFoundError(IMAGE_PATH)

image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)
```

## 4. Đọc, hiển thị và lưu ảnh

Mục tiêu:

- Đọc ảnh bằng OpenCV.
- Hiển thị ảnh đúng màu bằng Matplotlib.
- Lưu ảnh bằng OpenCV và Pillow.

Các bước thực hiện:

1. Đọc ảnh bằng `cv2.imread()`.
2. Chuyển BGR sang RGB bằng `cv2.cvtColor()`.
3. Hiển thị ảnh bằng `plt.imshow()`.
4. Lưu ảnh PNG bằng `cv2.imwrite()`.
5. Lưu ảnh JPG bằng Pillow.

Code dự kiến:

```python
plt.imshow(image_rgb)
plt.axis('off')
plt.show()

cv2.imwrite(
    str(OUTPUT_DIR / 'cau_2_anh_luu_lai.png'),
    image_bgr
)

Image.fromarray(image_rgb).save(
    OUTPUT_DIR / 'cau_2_anh_luu_lai.jpg'
)
```

Kết quả cần kiểm tra:

- Ảnh hiển thị không bị sai màu.
- File PNG và JPG được tạo thành công.

## 5. Chuyển đổi không gian màu

Mục tiêu:

- Chuyển ảnh sang Grayscale.
- Chuyển ảnh sang HSV.
- Chuyển ảnh sang LAB.

Code dự kiến:

```python
gray = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2GRAY)
hsv = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2HSV)
lab = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2LAB)
```

Kết quả cần lưu:

```text
outputs_chapter_1/
├── cau_3_grayscale.png
├── cau_3_hsv.png
└── cau_3_lab.png
```

Nhận xét cần viết:

- Grayscale chỉ giữ thông tin cường độ sáng.
- HSV thuận tiện khi cần phân tích hoặc tách màu.
- LAB tách độ sáng khỏi thông tin màu.

## 6. Cắt xén ảnh

Mục tiêu:

- Lấy một vùng quan tâm trong ảnh.
- Hiểu cách ảnh được biểu diễn bằng mảng NumPy.

Code dự kiến:

```python
height, width = image_bgr.shape[:2]

x1 = width // 4
x2 = width * 3 // 4
y1 = height // 4
y2 = height * 3 // 4

cropped = image_bgr[y1:y2, x1:x2]
```

Kết quả cần kiểm tra:

- Vùng cắt nằm trong kích thước ảnh.
- Ảnh kết quả là vùng trung tâm của ảnh gốc.

## 7. Thay đổi kích thước ảnh

Thực hiện theo hai cách:

### 7.1. Resize theo tỷ lệ

```python
resized_by_scale = cv2.resize(
    image_bgr,
    None,
    fx=0.5,
    fy=0.5
)
```

### 7.2. Resize theo kích thước cố định

```python
resized_fixed = cv2.resize(
    image_bgr,
    (320, 240)
)
```

Nhận xét cần viết:

- Resize theo tỷ lệ giúp giữ tỷ lệ khung hình.
- Resize về kích thước cố định có thể làm ảnh bị biến dạng.

## 8. Vẽ hình và thêm văn bản

Mục tiêu:

- Vẽ đường thẳng.
- Vẽ hình chữ nhật.
- Vẽ hình tròn.
- Thêm nội dung văn bản lên ảnh.

Code dự kiến:

```python
drawn = image_bgr.copy()
height, width = drawn.shape[:2]

cv2.line(
    drawn, (30, 30), (width - 30, 30),
    (0, 0, 255), 5
)

cv2.rectangle(
    drawn, (50, 80), (250, 220),
    (255, 0, 0), 4
)

cv2.circle(
    drawn, (width - 150, 160), 70,
    (0, 255, 0), 4
)

cv2.putText(
    drawn,
    'Chapter 1',
    (50, height - 45),
    cv2.FONT_HERSHEY_SIMPLEX,
    1.3,
    (255, 255, 255),
    3
)
```

Lưu ý:

- Màu trong OpenCV sử dụng thứ tự BGR.
- Nên tạo bản sao bằng `.copy()` để không sửa ảnh gốc.
- Tọa độ vẽ phải nằm trong kích thước ảnh.

## 9. Lưu và kiểm tra kết quả

Danh sách kết quả dự kiến:

```text
outputs_chapter_1/
├── cau_2_anh_luu_lai.png
├── cau_2_anh_luu_lai.jpg
├── cau_3_grayscale.png
├── cau_3_hsv.png
├── cau_3_lab.png
├── cau_4_anh_cat.png
├── cau_4_resize_50_percent.png
├── cau_4_resize_320x240.png
└── cau_5_ve_hinh_va_van_ban.png
```

Các bước kiểm tra:

1. Kiểm tra tất cả file đầu ra đã được tạo.
2. Mở ảnh và kiểm tra màu sắc.
3. Kiểm tra kích thước của ảnh crop và resize.
4. Kiểm tra hình vẽ và văn bản không vượt khỏi ảnh.
5. Chạy lại notebook bằng `Restart Kernel and Run All`.

## 10. Checklist hoàn thành

- [ ] Cài đặt đầy đủ thư viện.
- [ ] Đọc được ảnh đầu vào.
- [ ] Hiển thị ảnh đúng màu.
- [ ] Lưu ảnh bằng OpenCV.
- [ ] Lưu ảnh bằng Pillow.
- [ ] Tạo ảnh Grayscale.
- [ ] Tạo ảnh HSV.
- [ ] Tạo ảnh LAB.
- [ ] Cắt vùng trung tâm của ảnh.
- [ ] Resize ảnh theo tỷ lệ.
- [ ] Resize ảnh về kích thước cố định.
- [ ] Vẽ đường thẳng.
- [ ] Vẽ hình chữ nhật.
- [ ] Vẽ hình tròn.
- [ ] Thêm văn bản lên ảnh.
- [ ] Lưu đầy đủ kết quả.
- [ ] Chạy toàn bộ notebook không có lỗi.

## 11. Kết luận dự kiến

Chương 1 giúp làm quen với cách OpenCV biểu diễn và xử lý ảnh. Sau bài
thực hành, có thể đọc, hiển thị, lưu, chuyển đổi không gian màu, cắt,
thay đổi kích thước và vẽ các đối tượng cơ bản lên ảnh.
