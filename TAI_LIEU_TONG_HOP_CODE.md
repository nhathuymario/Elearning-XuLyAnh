# Tài liệu tổng hợp chi tiết code bài thực hành chương 1 và chương 2

Tài liệu này dùng để tham khảo khi soạn báo cáo Word. Nội dung bám theo hai notebook:

- `CHUONG_1/Bai_thuc_hanh_chuong_1.ipynb`
- `CHUONG_2/PHAN_1/Bai_thuc_hanh_chuong_2.ipynb`

## Chương 1. Các thao tác cơ bản với ảnh

### Câu 1. Cài đặt OpenCV và Pillow

Mục tiêu là chuẩn bị các thư viện cần thiết để đọc, xử lý, hiển thị và lưu ảnh.

Các thư viện sử dụng:

- `opencv-python`: xử lý ảnh chính, đọc/ghi ảnh, đổi màu, resize, vẽ hình.
- `pillow`: đọc/ghi ảnh theo phong cách PIL, hỗ trợ lưu ảnh với nhiều định dạng.
- `numpy`: thao tác ma trận ảnh.
- `matplotlib`: hiển thị ảnh trong notebook.

Lệnh cài đặt:

```python
!pip install -r requirements.txt
```

Kiểm tra thư viện:

```python
import cv2
from PIL import Image

print(cv2.__version__)
print(Image.__version__)
```

### Câu 2. Đọc, hiển thị và lưu ảnh

Ảnh trong OpenCV được đọc theo thứ tự kênh màu BGR, còn Matplotlib hiển thị ảnh theo RGB. Vì vậy cần đổi BGR sang RGB trước khi hiển thị.

Code chính:

```python
image_bgr = cv2.imread(IMAGE_PATH)
image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)

plt.imshow(image_rgb)
plt.axis('off')
plt.show()

cv2.imwrite('outputs_chapter_1/cau_2_anh_luu_lai.png', image_bgr)
Image.fromarray(image_rgb).save('outputs_chapter_1/cau_2_anh_luu_lai.jpg')
```

Kết quả:

- Ảnh gốc được hiển thị trong notebook.
- Ảnh được lưu lại dưới định dạng PNG và JPG.

### Câu 3. Chuyển đổi không gian màu

Các không gian màu được dùng:

- Grayscale: ảnh xám, mỗi pixel chỉ có một giá trị cường độ sáng.
- HSV: gồm Hue, Saturation, Value, thường dùng trong tách màu.
- LAB: gồm Lightness và hai kênh màu, thường dùng trong xử lý màu nâng cao.

Code chính:

```python
gray = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2GRAY)
hsv = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2HSV)
lab = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2LAB)
```

Kết quả được lưu:

- `cau_3_grayscale.png`
- `cau_3_hsv.png`
- `cau_3_lab.png`

### Câu 4. Cắt xén và thay đổi kích thước

Cắt ảnh dùng slicing của NumPy:

```python
cropped = image_bgr[y1:y2, x1:x2]
```

Resize theo tỷ lệ:

```python
resized_by_scale = cv2.resize(image_bgr, None, fx=0.5, fy=0.5)
```

Resize theo kích thước cố định:

```python
resized_fixed = cv2.resize(image_bgr, (320, 240))
```

Kết quả:

- Ảnh cắt vùng trung tâm.
- Ảnh giảm kích thước 50%.
- Ảnh resize về `320x240`.

### Câu 5. Vẽ hình cơ bản và thêm văn bản

OpenCV cung cấp các hàm vẽ trực tiếp lên ảnh:

```python
cv2.line(drawn, (30, 30), (width - 30, 30), (0, 0, 255), 5)
cv2.rectangle(drawn, (50, 80), (250, 220), (255, 0, 0), 4)
cv2.circle(drawn, (width - 150, 160), 70, (0, 255, 0), 4)
cv2.putText(drawn, 'Chapter 1', (50, height - 45), cv2.FONT_HERSHEY_SIMPLEX, 1.3, (255, 255, 255), 3)
```

Lưu ý: màu trong OpenCV là BGR, không phải RGB. Ví dụ `(0, 0, 255)` là màu đỏ.

## Chương 2. Toán tử điểm ảnh, lọc ảnh và phát hiện cạnh

### I. Toán tử điểm ảnh

Toán tử điểm ảnh xử lý từng pixel độc lập. Giá trị pixel đầu ra chỉ phụ thuộc vào pixel tương ứng ở ảnh đầu vào.

### Câu I.1. Thay đổi độ sáng

Công thức:

```text
g(x, y) = f(x, y) + beta
```

Trong đó:

- `f(x, y)` là pixel đầu vào.
- `g(x, y)` là pixel đầu ra.
- `beta` là giá trị cộng thêm hoặc trừ đi.

Code:

```python
brighter = cv2.convertScaleAbs(image_bgr, alpha=1.0, beta=50)
darker = cv2.convertScaleAbs(image_bgr, alpha=1.0, beta=-50)
```

`convertScaleAbs` tự xử lý việc giới hạn giá trị pixel về khoảng `0-255`.

### Câu I.2. Thay đổi độ tương phản

Công thức:

```text
g(x, y) = alpha * f(x, y)
```

Trong đó:

- `alpha > 1`: tăng tương phản.
- `0 < alpha < 1`: giảm tương phản.

Code:

```python
high_contrast = cv2.convertScaleAbs(image_bgr, alpha=1.6, beta=0)
low_contrast = cv2.convertScaleAbs(image_bgr, alpha=0.6, beta=0)
```

### Câu I.3. Biến đổi âm bản

Với ảnh 8-bit, pixel có giá trị từ 0 đến 255. Ảnh âm bản được tính:

```text
g(x, y) = 255 - f(x, y)
```

Code:

```python
negative = 255 - image_bgr
```

Kết quả là vùng sáng chuyển thành tối và vùng tối chuyển thành sáng.

### Câu I.4. Cắt ngưỡng

Công thức:

```text
g(x, y) = 255 nếu f(x, y) >= T
g(x, y) = 0 nếu f(x, y) < T
```

Code:

```python
ret, binary = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)
```

Ứng dụng: tách vật thể khỏi nền, tạo ảnh nhị phân, tiền xử lý cho nhận dạng.

### II. Lọc tuyến tính

Lọc tuyến tính dùng kernel trượt qua ảnh. Pixel đầu ra là tổng có trọng số của các pixel lân cận.

### Câu II.1. Lọc trung bình

Lọc trung bình thay pixel bằng giá trị trung bình trong vùng lân cận.

Code:

```python
mean_blur = cv2.blur(image_bgr, (5, 5))
```

Ưu điểm: đơn giản, làm mượt ảnh nhanh.

Nhược điểm: dễ làm mờ biên và mất chi tiết.

### Câu II.2. Lọc Gaussian

Lọc Gaussian dùng kernel có trọng số lớn ở tâm và nhỏ dần ra ngoài.

Code:

```python
gaussian_blur = cv2.GaussianBlur(image_bgr, (5, 5), sigmaX=1.2)
```

Ưu điểm: làm mượt tự nhiên hơn lọc trung bình.

Ứng dụng: giảm nhiễu trước khi phát hiện cạnh.

### Câu II.3. Làm sắc nét

Kernel làm sắc nét:

```python
sharpen_kernel = np.array([
    [0, -1, 0],
    [-1, 5, -1],
    [0, -1, 0]
], dtype=np.float32)
```

Code:

```python
sharpened = cv2.filter2D(image_bgr, ddepth=-1, kernel=sharpen_kernel)
```

Ý nghĩa: tăng sự khác biệt giữa pixel trung tâm và các pixel xung quanh, làm cạnh rõ hơn.

### III. Bài tập nâng cao

### Câu III.1. Phát hiện cạnh Sobel và Prewitt

Sobel và Prewitt đều tính gradient theo hai hướng x và y. Cạnh thường nằm ở nơi cường độ sáng thay đổi mạnh.

Sobel:

```python
sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
sobel_edges = cv2.convertScaleAbs(cv2.magnitude(sobel_x, sobel_y))
```

Prewitt:

```python
prewitt_x_kernel = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]], dtype=np.float32)
prewitt_y_kernel = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]], dtype=np.float32)
prewitt_x = cv2.filter2D(gray, cv2.CV_32F, prewitt_x_kernel)
prewitt_y = cv2.filter2D(gray, cv2.CV_32F, prewitt_y_kernel)
prewitt_edges = cv2.convertScaleAbs(cv2.magnitude(prewitt_x, prewitt_y))
```

Nhận xét: Sobel có trọng số trung tâm lớn hơn nên thường giảm nhiễu tốt hơn Prewitt một chút.

### Câu III.2. Tự thiết kế kernel

Emboss kernel:

```python
emboss_kernel = np.array([
    [-2, -1, 0],
    [-1, 1, 1],
    [0, 1, 2]
], dtype=np.float32)
```

Laplacian kernel:

```python
laplacian_kernel = np.array([
    [0, -1, 0],
    [-1, 4, -1],
    [0, -1, 0]
], dtype=np.float32)
```

Áp dụng:

```python
emboss = cv2.filter2D(image_bgr, -1, emboss_kernel)
custom_edge = cv2.filter2D(gray, cv2.CV_32F, laplacian_kernel)
custom_edge = cv2.convertScaleAbs(custom_edge)
```

### Câu III.3. So sánh các loại lọc

Các bộ lọc được so sánh:

- Lọc trung bình: làm mờ đều, đơn giản nhưng mất biên.
- Lọc Gaussian: làm mờ tự nhiên, thường dùng trước phát hiện cạnh.
- Median filter: tốt với nhiễu muối tiêu.
- Bilateral filter: làm mượt nhưng giữ biên tốt hơn.
- Sharpen filter: tăng cạnh và chi tiết.

Code:

```python
mean_blur = cv2.blur(image_bgr, (5, 5))
gaussian_blur = cv2.GaussianBlur(image_bgr, (5, 5), sigmaX=1.2)
median_filter = cv2.medianBlur(image_bgr, 5)
bilateral_filter = cv2.bilateralFilter(image_bgr, d=9, sigmaColor=75, sigmaSpace=75)
```

### Câu III.4. Lọc phi tuyến

Median filter:

```python
median_filter = cv2.medianBlur(image_bgr, 5)
```

Bilateral filter:

```python
bilateral_filter = cv2.bilateralFilter(image_bgr, d=9, sigmaColor=75, sigmaSpace=75)
```

Nhận xét:

- Median filter thay pixel bằng trung vị trong vùng lân cận, nên xử lý nhiễu đột biến tốt.
- Bilateral filter xét cả khoảng cách không gian và độ khác biệt màu, nên giữ cạnh tốt hơn các bộ lọc làm mờ thông thường.

## Cách chạy toàn bộ bài

1. Cài thư viện:

```bash
pip install -r requirements.txt
```

2. Mở Jupyter:

```bash
jupyter notebook
```

3. Chạy lần lượt hai file:

```text
CHUONG_1/Bai_thuc_hanh_chuong_1.ipynb
CHUONG_2/PHAN_1/Bai_thuc_hanh_chuong_2.ipynb
```

4. Kiểm tra kết quả trong:

```text
CHUONG_1/outputs_chapter_1/
CHUONG_2/PHAN_1/outputs_chapter_2/
```

## Chương 2 phần 2. Canny Edge Detector

### I. Lý thuyết thuật toán Canny

Canny Edge Detector là thuật toán phát hiện cạnh nhiều bước, được dùng phổ biến vì tạo cạnh mảnh, ít nhiễu và có khả năng nối các cạnh yếu liên quan đến cạnh mạnh.

Các bước chính:

1. Giảm nhiễu bằng Gaussian filter.
2. Tính gradient theo hướng x và y, thường bằng Sobel.
3. Tính độ lớn và hướng gradient.
4. Non-maximum suppression để làm mảnh cạnh.
5. Double threshold và hysteresis để giữ cạnh mạnh, nối cạnh yếu hợp lệ và loại nhiễu.

Minh họa code:

```python
blurred = cv2.GaussianBlur(gray, (5, 5), sigmaX=1.4)
grad_x = cv2.Sobel(blurred, cv2.CV_64F, 1, 0, ksize=3)
grad_y = cv2.Sobel(blurred, cv2.CV_64F, 0, 1, ksize=3)
gradient_magnitude = cv2.convertScaleAbs(cv2.magnitude(grad_x, grad_y))
canny_final = cv2.Canny(gray, threshold1=80, threshold2=160)
```

So với Sobel và Laplacian, Canny thường ổn định hơn vì có thêm bước giảm nhiễu, làm mảnh cạnh và nối cạnh bằng hysteresis.

### Tham số ảnh hưởng đến Canny

Các tham số quan trọng:

- `sigma`: điều khiển mức làm mượt Gaussian. Sigma lớn giảm nhiễu tốt hơn nhưng có thể làm mất cạnh nhỏ.
- `threshold_low`: ngưỡng thấp. Ngưỡng thấp nhỏ giữ nhiều cạnh yếu nhưng dễ giữ nhiễu.
- `threshold_high`: ngưỡng cao. Ngưỡng cao lớn chỉ giữ cạnh mạnh nhưng có thể làm đứt cạnh.

Code thay đổi ngưỡng OpenCV:

```python
edges = cv2.Canny(gray, threshold1=80, threshold2=160)
```

### Ưu điểm, nhược điểm và ứng dụng

Ưu điểm:

- Cạnh mảnh và rõ.
- Giảm nhiễu tốt hơn các toán tử đơn giản.
- Có cơ chế nối cạnh yếu với cạnh mạnh.

Nhược điểm:

- Phụ thuộc tham số.
- Chạy chậm hơn Sobel/Prewitt đơn giản.
- Ảnh quá nhiễu vẫn cần tiền xử lý.

Ứng dụng:

- Phát hiện vật thể.
- Kiểm tra lỗi sản phẩm.
- Tách biên trong ảnh y tế.
- Phân đoạn ảnh.
- Nhận dạng hình dạng hoặc contour.

### II.1. Thực hiện Canny bằng OpenCV và Scikit-image

OpenCV:

```python
opencv_edges = cv2.Canny(gray, threshold1=80, threshold2=160)
```

Scikit-image:

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

Nhận xét:

- OpenCV dùng ngưỡng theo thang pixel `0-255`.
- Scikit-image thường dùng ảnh float trong khoảng `0-1`, nên ngưỡng cũng đặt theo khoảng `0-1`.

### II.2. Thay đổi tham số và quan sát kết quả

Code mẫu:

```python
configs = [
    {'sigma': 0.8, 'low': 0.05, 'high': 0.15},
    {'sigma': 1.4, 'low': 0.10, 'high': 0.25},
    {'sigma': 2.2, 'low': 0.10, 'high': 0.25},
    {'sigma': 1.4, 'low': 0.18, 'high': 0.35},
]

for cfg in configs:
    edges_bool = feature.canny(
        gray_float,
        sigma=cfg['sigma'],
        low_threshold=cfg['low'],
        high_threshold=cfg['high']
    )
```

Nhận xét:

- Sigma nhỏ giữ nhiều chi tiết nhưng dễ nhiễu.
- Sigma lớn làm mượt mạnh hơn nhưng mất cạnh nhỏ.
- Ngưỡng càng cao thì số cạnh giữ lại càng ít.

### II.3. Áp dụng Canny cho nhiều loại ảnh

Các loại ảnh được thử:

- Ảnh gốc.
- Ảnh nhiễu nhiều.
- Ảnh tương phản thấp.
- Ảnh nhiều chi tiết.

Code chính:

```python
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(img_gray, 80, 160)
```

Đánh giá:

- Ảnh nhiễu nhiều tạo nhiều cạnh giả.
- Ảnh tương phản thấp có thể mất cạnh quan trọng.
- Ảnh nhiều chi tiết tạo nhiều đường biên nhỏ, cần chọn ngưỡng cao hơn hoặc tiền xử lý.

### II.4. Kết hợp Canny với phân đoạn và nhận dạng hình dạng

Quy trình:

1. Chạy Canny để lấy biên.
2. Dùng morphology close/dilate để nối cạnh.
3. Tìm contour bằng `cv2.findContours`.
4. Xấp xỉ contour bằng `cv2.approxPolyDP`.
5. Dựa vào số đỉnh để nhận dạng hình dạng cơ bản.

Code chính:

```python
edges = cv2.Canny(gray, 80, 160)
kernel = np.ones((3, 3), dtype=np.uint8)
closed_edges = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel, iterations=2)
dilated_edges = cv2.dilate(closed_edges, kernel, iterations=1)
contours, _ = cv2.findContours(dilated_edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
```

Nhận dạng hình dạng:

```python
perimeter = cv2.arcLength(contour, True)
approx = cv2.approxPolyDP(contour, 0.03 * perimeter, True)
vertices = len(approx)
```

Nếu `vertices == 3` thì có thể xem là tam giác. Nếu `vertices == 4` thì là tứ giác/hình chữ nhật. Nếu `vertices > 6` thì thường là hình tròn hoặc đường cong.

### III. Câu hỏi mở rộng

Đánh giá chất lượng cạnh:

- Nếu có nhãn chuẩn, dùng precision, recall, F1-score.
- Nếu không có nhãn, đánh giá trực quan theo độ mảnh cạnh, độ liên tục, số cạnh giả và khả năng giữ biên quan trọng.

Cải thiện hiệu suất:

- Dùng Gaussian, median hoặc bilateral filter trước Canny.
- Chọn ngưỡng tự động bằng histogram hoặc Otsu.
- Resize ảnh hoặc chỉ xử lý ROI.
- Với video, có thể xử lý cách frame hoặc dùng GPU.

Canny với ảnh màu:

```python
b, g, r = cv2.split(image_bgr)
edge_b = cv2.Canny(b, 80, 160)
edge_g = cv2.Canny(g, 80, 160)
edge_r = cv2.Canny(r, 80, 160)
color_channel_edges = cv2.bitwise_or(cv2.bitwise_or(edge_b, edge_g), edge_r)
```

Canny với video:

```python
cap = cv2.VideoCapture('input.mp4')
while True:
    ret, frame = cap.read()
    if not ret:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 1.4)
    edges = cv2.Canny(gray, 80, 160)
    cv2.imshow('edges', edges)
cap.release()
cv2.destroyAllWindows()
```
