# Kế hoạch làm code - Bài thực hành Wavelet Hash

Tài liệu này ghi lại kế hoạch triển khai notebook `BAI_THUC_HANH_4_WAVELET_HASH.ipynb`. Mục tiêu là giúp người đọc hiểu vì sao code được chia như hiện tại, phần nào tạo dữ liệu, phần nào trích xuất Wavelet, phần nào tạo hash và đánh giá.

## 1. Chuẩn bị dữ liệu

**Mục tiêu:** đọc ảnh từ hai thư mục `image/tuong_tu` và `image/khong_tuong_tu`.

**Kế hoạch code:**

1. Khai báo đường dẫn dữ liệu và thư mục output.
2. Lọc các file có đuôi ảnh hợp lệ.
3. Đọc ảnh bằng OpenCV.
4. Đổi ảnh từ BGR/BGRA/Gray sang RGB/RGBA để hiển thị đúng màu bằng Matplotlib.
5. Tạo thêm `gray_images` kích thước `256x256` để dùng lại cho phần Wavelet.
6. Gán nhãn:
   - `1`: ảnh thuộc nhóm tương tự.
   - `0`: ảnh thuộc nhóm không tương tự.
7. Hiển thị ảnh để kiểm tra nhãn bằng mắt.

**Lý do tối ưu:** phần đọc ảnh và đổi ảnh xám được làm một lần ở đầu, tránh đổi RGB sang xám lặp lại ở nhiều cell phía sau.

## 2. Trích xuất ma trận Wavelet

**Mục tiêu:** phân rã ảnh xám thành các ma trận Wavelet.

**Kế hoạch code:**

1. Dùng `gray_images` đã chuẩn hóa từ phần 1.
2. Chọn wavelet mặc định là `db4`.
3. Với mỗi ảnh, tính:
   - `level1 = pywt.wavedec2(gray, wavelet="db4", level=1)`
   - `level2 = pywt.wavedec2(gray, wavelet="db4", level=2)`
4. Lưu kết quả vào `wavelet_matrices`.
5. Hiển thị trực quan level 1 và level 2 để so sánh:
   - `LL`: phần xấp xỉ, giữ hình dáng tổng quát.
   - `LH`, `HL`, `HH`: các phần chi tiết theo hướng.

**Lý do có level 1 và level 2:** level 1 giúp nhìn rõ bước phân rã đầu tiên; level 2 tổng quát hơn, phù hợp hơn để tạo hash ổn định.

## 3. Tạo Wavelet Hash

**Mục tiêu:** biến mỗi ảnh thành mã hash nhị phân 64 bit.

**Kế hoạch code:**

1. Resize ảnh đầu vào theo công thức:

```python
image_size = hash_size * (2 ** level)
```

2. Với `hash_size=8`, `level=2`, ảnh được đưa về `32x32`.
3. Phân rã Wavelet level 2.
4. Chỉ lấy ma trận `LL` vì đây là phần tần số thấp, ổn định hơn trước nhiễu và nén ảnh.
5. Resize `LL` về `8x8`.
6. Lấy median của `LL`.
7. Lượng tử hóa:
   - hệ số lớn hơn median thành bit `1`;
   - hệ số nhỏ hơn hoặc bằng median thành bit `0`.
8. Trải ma trận `8x8` thành vector 64 bit.

## 4. So sánh ảnh bằng Hamming

**Mục tiêu:** đo độ khác nhau giữa hai hash.

**Kế hoạch code:**

1. Tạo hash cho toàn bộ ảnh.
2. Tạo cặp ảnh:
   - cặp trong nhóm tương tự là nhãn `1`;
   - cặp giữa ảnh tương tự và ảnh không tương tự là nhãn `0`.
3. Tính khoảng cách Hamming:

```python
distance = np.count_nonzero(hash1 != hash2)
```

4. Khoảng cách càng nhỏ thì ảnh càng giống.

## 5. Chọn ngưỡng và đánh giá

**Mục tiêu:** chọn threshold hợp lý để phân loại tương tự/không tương tự.

**Kế hoạch code:**

1. Chia các cặp thành validation và test.
2. Quét threshold từ `0` đến `64`.
3. Trên validation, chọn threshold có balanced accuracy cao nhất.
4. Dùng threshold đã chọn để đánh giá test.
5. Báo cáo:
   - Accuracy
   - Sensitivity
   - Specificity
   - Precision
   - Confusion matrix
   - ROC/AUC

**Lý do không chọn threshold trên test:** nếu chọn trực tiếp trên test thì kết quả bị lạc quan, không phản ánh khả năng tổng quát.

## 6. So sánh các họ Wavelet

**Mục tiêu:** kiểm tra wavelet nào phù hợp hơn với bộ ảnh đang dùng.

**Kế hoạch code:**

1. Thử các họ wavelet: `haar`, `db2`, `db4`, `sym4`.
2. Với mỗi họ:
   - tạo lại hash;
   - tính Hamming;
   - chọn threshold trên validation;
   - đánh giá trên test.
3. So sánh Accuracy và AUC.

## Ghi chú tối ưu code

- Không giữ hàm nếu chỉ gọi một lần và làm luồng đọc khó hơn.
- Dữ liệu dùng nhiều lần nên lưu lại bằng biến rõ nghĩa, ví dụ `images`, `gray_images`, `wavelet_matrices`.
- Cell minh họa nên dùng lại kết quả đã tính, tránh phân rã Wavelet lại trong lúc vẽ.
- Các phần cần học nên giữ comment ngắn, đúng trọng tâm, không giải thích quá dài trong code.
