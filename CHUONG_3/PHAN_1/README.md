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

## Nội dung đã hoàn thành

- Biến đổi wavelet 2D và trực quan các dải LL, LH, HL, HH.
- Tạo Wavelet Hash độ dài cố định và tính khoảng cách Hamming.
- Tạo cặp ảnh tương tự/không tương tự có nhãn.
- Tự chọn ngưỡng trên tập validation, không chọn bằng tập test.
- Tính accuracy, sensitivity (recall), specificity và precision.
- Vẽ ROC, tính AUC và ma trận nhầm lẫn.
- So sánh `haar`, `db2`, `db4`, `sym4`.
- Tìm kiếm ảnh tương tự theo top-k.

## Môi trường

```powershell
pip install -r requirements.txt
jupyter lab CHUONG_3/PHAN_1/BAI_THUC_HANH_4_WAVELET_HASH.ipynb
```

Lưu ý: SURF thường không có trong bản OpenCV chuẩn; bài này dùng PyWavelets đúng yêu cầu thực hành và không phụ thuộc SURF.
