# Lý thuyết Chương 3 - Phần 1

## 1. Quy trình phát hiện và đối sánh

Một hệ thống đối sánh đặc trưng cục bộ thường có bốn bước:

1. **Phát hiện** điểm quan tâm (góc, vùng kết cấu, blob).
2. **Mô tả** vùng lân cận bằng một vector hoặc chuỗi bit.
3. **Đối sánh** các descriptor bằng một độ đo khoảng cách.
4. **Kiểm chứng hình học** và loại ngoại lai, thường bằng RANSAC.

Detector trả lời “điểm đáng chú ý nằm ở đâu?”, descriptor trả lời “vùng quanh điểm đó trông như thế nào?”. Không nên đánh đồng hai vai trò.

## 2. Gradient và tính bất biến

Với ảnh xám `I(x, y)`, gradient gồm hai đạo hàm `Gx`, `Gy`:

```text
độ lớn  M = sqrt(Gx² + Gy²)
hướng   θ = atan2(Gy, Gx)
```

Sobel, Prewitt và Scharr là các cách xấp xỉ đạo hàm. Histogram hướng gradient giúp descriptor ít nhạy với dịch chuyển nhỏ; gán hướng chính giúp chống phép quay. Scale-space giúp chống thay đổi tỷ lệ.

## 3. SIFT, SURF và ORB

| Thuật toán | Detector / descriptor | Khoảng cách | Điểm mạnh | Hạn chế |
|---|---|---|---|---|
| SIFT | DoG / histogram gradient 128 chiều | L2 | Phân biệt tốt, bền với xoay và tỷ lệ | Tính toán nặng hơn |
| SURF | Hessian xấp xỉ / đáp ứng Haar | L2 | Nhanh hơn thiết kế SIFT cổ điển | Không sẵn trong OpenCV chuẩn |
| ORB | FAST có hướng / rotated BRIEF | Hamming | Rất nhanh, descriptor nhị phân | Kém bền hơn khi đổi góc nhìn lớn |

Không dùng Hamming cho descriptor float của SIFT, và không dùng L2 như lựa chọn mặc định cho descriptor bit của ORB.

## 4. Đối sánh và loại ngoại lai

- **Brute Force:** so từng descriptor với tất cả descriptor còn lại.
- **k-NN + ratio test:** giữ cặp tốt nhất khi khoảng cách gần nhất đủ nhỏ so với khoảng cách gần nhì; giúp bỏ match mơ hồ.
- **Cross-check:** hai chiều phải cùng chọn nhau.
- **RANSAC:** ước lượng homography/affine từ nhiều mẫu nhỏ và giữ các inlier phù hợp mô hình.

Nhiều match chưa chắc tốt. Tỷ lệ inlier sau RANSAC có ý nghĩa hơn số match thô.

## 5. Đối sánh cục bộ và băm toàn ảnh

SIFT/ORB mô tả nhiều vùng cục bộ, phù hợp khi cần tìm vị trí tương ứng hoặc ước lượng hình học. Wavelet Hash tạo **một chữ ký toàn cục** cho cả ảnh, phù hợp tìm ảnh gần trùng, biến thể nén/sáng/nhiễu nhẹ. Wavelet Hash không thay thế SIFT/ORB khi ảnh bị che khuất nhiều hoặc cần xác định homography.

## 6. Wavelet Hash

Biến đổi wavelet 2D tách ảnh thành:

- `LL`: cấu trúc tần số thấp, hình dáng tổng quát.
- `LH`, `HL`, `HH`: chi tiết theo các hướng và tần số cao.

Quy trình dùng trong bài:

1. Chuyển xám, resize và chuẩn hóa.
2. Phân rã DWT nhiều mức.
3. Lấy ma trận `LL` ở mức cuối.
4. Resize về `hash_size × hash_size`.
5. So từng hệ số với median để nhận bit 0/1.

Median bền hơn mốc 0 trong nhiều ảnh và cho mã băm cân bằng hơn. Chỉ dùng `LL` giúp hash ít nhạy với nhiễu; đổi lại có thể bỏ mất khác biệt nhỏ quan trọng.

## 7. Hamming và ngưỡng quyết định

Với hai hash cùng độ dài `N`, khoảng cách Hamming là số bit khác nhau. Khoảng cách càng nhỏ thì hai ảnh càng giống. Quy tắc phân lớp:

```text
distance <= threshold  → tương tự
distance > threshold   → không tương tự
```

Ngưỡng phải được chọn trên tập validation rồi mới báo cáo trên test. Chọn ngưỡng trực tiếp trên test tạo ra đánh giá lạc quan.

## 8. Chỉ số đánh giá

- Accuracy = `(TP + TN) / tổng số cặp`.
- Sensitivity/Recall = `TP / (TP + FN)`.
- Specificity = `TN / (TN + FP)`.
- Precision = `TP / (TP + FP)`.
- ROC quét mọi ngưỡng, biểu diễn `TPR` theo `FPR = 1 - specificity`.
- AUC gần 1 là tốt; gần 0.5 tương đương xếp hạng ngẫu nhiên.

Accuracy một mình có thể gây hiểu nhầm khi hai lớp mất cân bằng, vì vậy bài thực hành báo cáo đủ bốn chỉ số và ROC-AUC.

## 9. Hiệu chỉnh một số diễn đạt trong slide

- SIFT tìm cực trị trong **Difference of Gaussians scale-space**, không đơn giản là điểm có gradient lớn nhất.
- Descriptor SIFT là histogram hướng gradient; Hessian chủ yếu phục vụ detector của SURF, không phải toàn bộ descriptor như một ma trận Hessian thô.
- ORB là sự kết hợp và cải tiến FAST + BRIEF, không phải “phiên bản SIFT” theo nghĩa thuật toán kế thừa trực tiếp.
- “Độ đặc biệt” trong slide tương ứng thuật ngữ chuẩn **độ đặc hiệu (specificity)**.
