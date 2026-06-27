# Log chat - Bài thực hành Wavelet Hash

Tài liệu này ghi lại các câu hỏi, quyết định chỉnh sửa và giải thích chính trong quá trình hoàn thiện notebook `BAI_THUC_HANH_4_WAVELET_HASH.ipynb`.

### 1. Giải thích `LL shape = (69, 69)`

**Câu hỏi:** `LL shape = (69, 69)` nghĩa là gì?

**Trả lời ngắn:** `LL` là ma trận xấp xỉ sau biến đổi Wavelet. Shape `(69, 69)` nghĩa là ma trận có 69 hàng và 69 cột.

**Ý chính:**

- `LL` giữ thông tin tổng quát của ảnh.
- Số đầu là chiều cao, số sau là chiều rộng.
- Nếu ảnh bị phân rã 1 mức, kích thước thường giảm khoảng một nửa theo mỗi chiều.

### 2. Hàm dùng để so sánh ảnh tương đồng

**Câu hỏi:** Notebook dùng hàm gì để so sánh ảnh tương đồng?

**Trả lời ngắn:** dùng `hamming_distance(hash1, hash2)`.

**Ý chính:**

- Mỗi ảnh được đổi thành Wavelet Hash 64 bit.
- Hai ảnh được so sánh bằng số bit khác nhau.
- Hamming càng nhỏ thì ảnh càng giống.

### 3. Vì sao chỉ dùng `LL` nhưng vẫn tách `LH`, `HL`, `HH`

**Câu hỏi:** Tại sao chỉ dùng ma trận `LL` mà lại tách thêm các ma trận khác?

**Trả lời ngắn:** `LH`, `HL`, `HH` được tách để minh họa Wavelet hoạt động như thế nào; khi tạo hash thì chỉ dùng `LL` vì ổn định hơn.

**Ý chính:**

- `LL`: thông tin tổng quát, ít nhạy với nhiễu.
- `LH`, `HL`, `HH`: chi tiết cạnh, texture, nhiễu.
- Dùng `LL` giúp hash ổn định hơn khi ảnh bị nén, resize hoặc thay đổi sáng nhẹ.

### 4. Vì sao chọn `level=2`

**Câu hỏi:** Tại sao `wavelet_matrices` lại dùng `level=2`?

**Trả lời ngắn:** `level=2` phân rã ảnh hai lần, lấy đặc trưng tổng quát hơn `level=1`.

**Ý chính:**

- `level=1`: còn nhiều chi tiết nhỏ.
- `level=2`: tổng quát hơn, ổn định hơn cho hash.
- Level quá cao có thể làm mất nhiều thông tin.

### 5. Thêm ví dụ level 1 để so sánh với level 2

**Yêu cầu:** Notebook đang phân rã level 2, thêm trích xuất level 1 làm ví dụ về sự khác nhau.

**Đã chỉnh:**

- Cell minh họa phần 2 hiển thị cả `level 1` và `level 2`.
- Mỗi ảnh minh họa có 2 hàng:
  - hàng 1: `Ảnh xám`, `LL1`, `LH1`, `HL1`, `HH1`;
  - hàng 2: `Ảnh xám`, `LL2`, `LH2`, `HL2`, `HH2`.
- In thêm shape của `LL level 1` và `LL level 2`.

### 6. Tối ưu phần 1 và phần 2

**Yêu cầu:** Check và tối ưu lại phần 1, 2 vì bị dư hàm và lặp đổi ảnh RGB/xám.

**Đã chỉnh:**

- Phần 1 tạo sẵn:
  - `images`: ảnh màu RGB/RGBA để hiển thị;
  - `gray_images`: ảnh xám `256x256` để xử lý Wavelet.
- Bỏ hàm `extract_wavelet_matrices()` vì không cần thiết.
- Phần 2 dùng lại `gray_images`.
- Tạo `wavelet_matrices` chứa kết quả `level1` và `level2`.
- Cell minh họa dùng lại `wavelet_matrices`, không phân rã lại trong lúc vẽ.

### 7. Sửa lỗi font tiếng Việt

**Vấn đề:** Một số dòng bị lỗi font như `?? tr?ch xu?t Wavelet`.

**Đã chỉnh:**

- Ghi lại các cell phần 1 và phần 2 bằng Unicode chuẩn.
- Kiểm tra không còn chuỗi lỗi kiểu `??`, `tr?ch`, `xu?t`.
- Kiểm tra cú pháp toàn bộ code cell thành công.

### 8. Giải thích `raise ValueError`

**Câu hỏi:** `raise ValueError("Ảnh phải có dạng HxW, HxWx3 hoặc HxWx4")` nghĩa là gì?

**Trả lời ngắn:** nếu ảnh không đúng dạng dữ liệu mà hàm xử lý được thì báo lỗi.

**Ý chính:**

- `HxW`: ảnh xám.
- `HxWx3`: ảnh RGB.
- `HxWx4`: ảnh RGBA.
- Các dạng khác không được xử lý để tránh lỗi âm thầm.

### 9. Biến `image` lấy từ đâu

**Câu hỏi:** `image` trong hàm phía dưới lấy ở đâu?

**Trả lời ngắn:** lấy từ dictionary `images`.

**Luồng dữ liệu:**

```text
file ảnh trong thư mục
        ↓
read_rgb(path)
        ↓
images["anh1.jpg"]
        ↓
to_gray(image, 256)
        ↓
gray_images["anh1.jpg"]
```

### 10. `LL` là lọc ảnh hay chỉ thu nhỏ?

**Câu hỏi:** `LL` có lọc nhiều của ảnh không hay chỉ trích xuất thu nhỏ?

**Trả lời ngắn:** `LL` không chỉ là thu nhỏ; nó là ảnh đã được lọc tần số thấp rồi mới giảm kích thước.

**Ý chính:**

- `LL` giữ vùng sáng/tối lớn, bố cục và hình dáng tổng quát.
- `LL` giảm bớt cạnh sắc, texture nhỏ và nhiễu.
- Wavelet `LL` khác resize thường vì có bước lọc low-pass trước khi downsample.

## Quy ước cập nhật log

Khi tiếp tục chỉnh notebook, nên ghi thêm vào file này:

1. Ngày chỉnh sửa.
2. Câu hỏi hoặc vấn đề gặp phải.
3. Quyết định chỉnh code.
4. Lý do chọn cách đó.
5. Kết quả kiểm tra nếu có.
