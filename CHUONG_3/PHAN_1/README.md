# Chương 3 - Phần 1: Phát hiện đặc trưng và đối sánh ảnh

Thư mục này chuyển phần lý thuyết trong slide thành một bài thực hành hoàn chỉnh về **Wavelet Hash**, đúng yêu cầu cuối tài liệu.

## Thứ tự học và chạy

1. Đọc `TAI_LIEU/LY_THUYET_PHAT_HIEN_DAC_TRUNG_VA_DOI_SANH.md`.
2. Đọc `TAI_LIEU/HUONG_DAN_THUC_HANH_WAVELET_HASH.md`.
3. Chép ít nhất 3 ảnh cùng đối tượng/cảnh vào `image/tuong_tu/`.
4. Chép ít nhất 1 ảnh khác đối tượng/cảnh vào `image/khong_tuong_tu/`.
5. Mở và chọn **Run All** cho `BAI_THUC_HANH_4_WAVELET_HASH.ipynb`.
6. Đọc giải thích Input/Output, console và hình ngay dưới từng mục; biểu đồ cũng được lưu ở `outputs/`.

Notebook tự đọc hai thư mục ảnh, tự tạo cặp và gán nhãn. Toàn bộ hàm Wavelet Hash được đặt ngay trong notebook nên không cần file Python riêng và không cần sửa đường dẫn trong mã.

## Sáu phần của bài thực hành

1. Chuẩn bị dữ liệu ảnh tương tự và không tương tự.
2. Trích xuất, hiển thị các ma trận Wavelet LL, LH, HL, HH.
3. Lượng tử hóa hệ số Wavelet và tạo mã băm 64 bit.
4. So sánh mã băm bằng khoảng cách Hamming.
5. Đánh giá Accuracy, Sensitivity, Specificity, Precision và ROC/AUC.
6. So sánh hiệu suất các họ Wavelet `haar`, `db2`, `db4`, `sym4`.

Notebook chỉ có đúng sáu phần trên. Hàm xử lý thuộc phần nào được đặt và chú thích ngay trong phần đó.

## Môi trường

```powershell
pip install -r requirements.txt
jupyter lab CHUONG_3/PHAN_1/BAI_THUC_HANH_4_WAVELET_HASH.ipynb
```

Lưu ý: SURF thường không có trong bản OpenCV chuẩn; bài này dùng PyWavelets đúng yêu cầu thực hành và không phụ thuộc SURF.
