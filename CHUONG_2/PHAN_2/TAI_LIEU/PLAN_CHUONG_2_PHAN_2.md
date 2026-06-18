# Plan bài thực hành Chương 2 - Phần 2

## 1. Nội dung chính

Phần này tập trung vào thuật toán Canny Edge Detector:

1. Tìm hiểu các bước của thuật toán Canny.
2. Phân tích ảnh hưởng của các tham số.
3. Thực hiện Canny bằng OpenCV và Scikit-image.
4. Thử nghiệm trên nhiều loại ảnh.
5. Kết hợp Canny với contour và nhận dạng hình dạng.
6. Trả lời các câu hỏi mở rộng.

Mỗi phần nên trình bày:

- Mục tiêu.
- Nguyên lý.
- Tham số.
- Code thực hiện.
- Hình ảnh kết quả.
- Nhận xét.

### Bố cục dùng khi thuyết trình

| Phần | Nội dung |
|---|---|
| I | Lý thuyết, các bước, tham số, ưu nhược điểm và ứng dụng |
| II | OpenCV/Scikit-image, thay đổi tham số, nhiều loại ảnh, contour |
| III | Đánh giá, cải thiện, ảnh màu và video |

Các mục đánh số bên dưới là kế hoạch nội dung chi tiết. Khi làm slide hoặc
trình bày, gom chúng về đúng ba phần I-II-III theo bảng trên.

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

## 3. Lý thuyết thuật toán Canny

Canny Edge Detector gồm các bước chính:

1. Làm mượt ảnh bằng Gaussian filter.
2. Tính gradient theo hướng `x` và `y`.
3. Tính độ lớn và hướng gradient.
4. Làm mảnh cạnh bằng Non-maximum suppression.
5. Phân loại cạnh bằng double threshold.
6. Nối cạnh bằng hysteresis.

Code minh họa gần đúng:

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

## 4. Phân tích các tham số

Các tham số quan trọng:

- `sigma`: mức làm mượt Gaussian.
- `threshold_low`: ngưỡng thấp để xác định cạnh yếu.
- `threshold_high`: ngưỡng cao để xác định cạnh mạnh.

Thử các cấu hình OpenCV:

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

- Ngưỡng thấp tạo nhiều cạnh nhưng dễ xuất hiện cạnh giả.
- Ngưỡng cao chỉ giữ cạnh mạnh nhưng có thể làm đứt cạnh.
- Hai ngưỡng cần có khoảng cách hợp lý để hysteresis hoạt động tốt.

## 5. Ưu điểm, nhược điểm và ứng dụng

Ưu điểm:

- Cạnh thu được mảnh và rõ.
- Có bước giảm nhiễu.
- Có khả năng nối cạnh yếu với cạnh mạnh.
- Ổn định hơn Sobel hoặc Prewitt trong nhiều trường hợp.

Nhược điểm:

- Phụ thuộc vào sigma và hai giá trị ngưỡng.
- Xử lý chậm hơn các toán tử gradient đơn giản.
- Ảnh nhiều nhiễu vẫn cần tiền xử lý phù hợp.

Ứng dụng:

- Phát hiện vật thể.
- Tìm contour.
- Kiểm tra lỗi sản phẩm.
- Phân đoạn ảnh.
- Nhận dạng hình dạng.
- Phân tích ảnh y tế.

## 6. Thực hiện Canny bằng OpenCV

Code dự kiến:

```python
opencv_edges = cv2.Canny(
    gray,
    threshold1=80,
    threshold2=160
)
```

Kết quả cần kiểm tra:

- Cạnh chính của vật thể được giữ lại.
- Nhiễu nền không tạo quá nhiều cạnh giả.
- Đường cạnh không bị đứt quá nhiều.

## 7. Thực hiện Canny bằng Scikit-image

Code dự kiến:

```python
gray_float = rgb2gray(image_rgb)

skimage_edges_bool = feature.canny(
    gray_float,
    sigma=1.4,
    low_threshold=0.10,
    high_threshold=0.25
)

skimage_edges = img_as_ubyte(skimage_edges_bool)
```

Điểm cần lưu ý:

- OpenCV thường xử lý ảnh 8-bit trong khoảng `0-255`.
- Scikit-image thường xử lý ảnh float trong khoảng `0-1`.
- Không sử dụng trực tiếp cùng một giá trị ngưỡng cho hai thư viện.

## 8. Thay đổi tham số và so sánh

Các cấu hình thử nghiệm:

```python
configs = [
    (0.8, 0.05, 0.15),
    (1.4, 0.10, 0.25),
    (2.2, 0.10, 0.25),
    (1.4, 0.18, 0.35)
]

for sigma, low, high in configs:
    edges_bool = feature.canny(
        gray_float,
        sigma=sigma,
        low_threshold=low,
        high_threshold=high
    )
```

Tiêu chí so sánh:

- Số lượng cạnh được phát hiện.
- Mức độ liên tục của cạnh.
- Số cạnh giả.
- Khả năng giữ chi tiết nhỏ.
- Mức độ làm mượt ảnh.

## 9. Áp dụng trên nhiều loại ảnh

Các trường hợp cần thử:

1. Ảnh gốc.
2. Ảnh có nhiều nhiễu.
3. Ảnh có độ tương phản thấp.
4. Ảnh có nhiều chi tiết.

Quy trình chung:

```python
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(img_gray, 80, 160)
```

Nhận xét dự kiến:

- Ảnh nhiễu tạo nhiều cạnh giả.
- Ảnh tương phản thấp dễ mất cạnh yếu.
- Ảnh nhiều chi tiết cần ngưỡng cao hơn hoặc làm mượt mạnh hơn.
- Không có một bộ tham số phù hợp cho mọi ảnh.

## 10. Kết hợp Canny với contour

Quy trình:

1. Phát hiện cạnh bằng Canny.
2. Dùng morphology close để nối cạnh.
3. Dùng dilate để làm cạnh rõ hơn.
4. Tìm contour.
5. Loại bỏ contour có diện tích quá nhỏ.

Code dự kiến:

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

contours, _ = cv2.findContours(
    dilated_edges,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)
```

## 11. Nhận dạng hình dạng cơ bản

Xấp xỉ contour:

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

Khi đánh giá cần kết hợp thêm:

- Diện tích contour.
- Tỷ lệ chiều rộng và chiều cao.
- Độ tròn của contour.
- Chất lượng đường cạnh.

## 12. Canny trên ảnh màu

Canny thường được áp dụng trên ảnh xám. Có thể thử phát hiện cạnh trên
từng kênh màu rồi kết hợp:

```python
b, g, r = cv2.split(image_bgr)

edge_b = cv2.Canny(b, 80, 160)
edge_g = cv2.Canny(g, 80, 160)
edge_r = cv2.Canny(r, 80, 160)

color_edges = cv2.bitwise_or(
    cv2.bitwise_or(edge_b, edge_g),
    edge_r
)
```

Nhận xét:

- Xử lý từng kênh có thể giữ cạnh màu mà ảnh xám bỏ qua.
- Kết quả cũng có thể chứa nhiều cạnh và nhiễu hơn.

## 13. Canny trên video

Quy trình:

1. Đọc từng frame.
2. Chuyển frame sang ảnh xám.
3. Làm mượt bằng Gaussian.
4. Chạy Canny.
5. Hiển thị hoặc lưu kết quả.

Code dự kiến:

```python
cap = cv2.VideoCapture('input.mp4')

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray_frame = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2GRAY
    )
    gray_frame = cv2.GaussianBlur(
        gray_frame,
        (5, 5),
        1.4
    )
    edges = cv2.Canny(gray_frame, 80, 160)

cap.release()
cv2.destroyAllWindows()
```

## 14. Đánh giá và cải thiện kết quả

Nếu có ảnh cạnh chuẩn:

- Precision.
- Recall.
- F1-score.

Nếu không có ảnh chuẩn:

- Độ mảnh của cạnh.
- Độ liên tục.
- Số cạnh giả.
- Khả năng giữ cạnh quan trọng.

Các cách cải thiện:

- Gaussian filter trước Canny.
- Median filter cho nhiễu muối tiêu.
- Bilateral filter khi cần giữ biên.
- Chọn ngưỡng tự động từ histogram hoặc Otsu.
- Chỉ xử lý vùng ROI.
- Resize ảnh trước khi xử lý.
- Xử lý cách frame khi dùng video.

## 15. Lưu và kiểm tra kết quả

Danh sách kết quả dự kiến:

```text
outputs_chapter_2_part_2/
├── I_1_gaussian_blur.png
├── I_1_gradient_magnitude.png
├── I_1_canny_final.png
├── I_2_canny_nhay.png
├── I_2_canny_can_bang.png
├── I_2_canny_it_canh.png
├── II_1_canny_opencv.png
├── II_1_canny_skimage.png
├── II_2_so_sanh_tham_so.png
├── II_3_anh_nhieu.png
├── II_3_anh_tuong_phan_thap.png
├── II_3_anh_nhieu_chi_tiet.png
├── II_4_contours.png
├── II_4_nhan_dang_hinh_dang.png
└── III_3_canny_color_channels.png
```

Các bước kiểm tra:

1. Kiểm tra tất cả ảnh kết quả đã được lưu.
2. So sánh OpenCV với Scikit-image.
3. So sánh các cấu hình tham số.
4. Kiểm tra contour và nhãn hình dạng.
5. Chạy lại notebook bằng `Restart Kernel and Run All`.

## 16. Checklist hoàn thành

- [ ] Cài đặt đầy đủ thư viện.
- [ ] Đọc được ảnh đầu vào.
- [ ] Minh họa bước Gaussian.
- [ ] Minh họa gradient.
- [ ] Thực hiện Canny bằng OpenCV.
- [ ] Thực hiện Canny bằng Scikit-image.
- [ ] Thử nhiều bộ tham số.
- [ ] Thử trên ảnh nhiễu.
- [ ] Thử trên ảnh tương phản thấp.
- [ ] Thử trên ảnh nhiều chi tiết.
- [ ] Kết hợp Canny với morphology.
- [ ] Tìm contour.
- [ ] Nhận dạng hình dạng cơ bản.
- [ ] Thử Canny trên từng kênh màu.
- [ ] Trình bày cách xử lý video.
- [ ] Lưu đầy đủ kết quả.
- [ ] Viết nhận xét và kết luận.
- [ ] Chạy toàn bộ notebook không có lỗi.

## 17. Kết luận dự kiến

Canny tạo cạnh rõ và mảnh nhờ kết hợp giảm nhiễu, tính gradient, làm
mảnh cạnh, double threshold và hysteresis. Chất lượng kết quả phụ thuộc
nhiều vào sigma và hai giá trị ngưỡng. Khi được tiền xử lý và chọn tham
số phù hợp, Canny có thể hỗ trợ tốt cho tìm contour, phân đoạn và nhận
dạng hình dạng.
