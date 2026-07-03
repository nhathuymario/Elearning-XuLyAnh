# Hướng dẫn bài thực hành - FaceNet & MTCNN trên Webcam

## Mục tiêu

Sau bài thực hành, người học có thể:

1. Mở webcam và đọc frame bằng OpenCV.
2. Dùng MTCNN để phát hiện vị trí khuôn mặt.
3. Dùng FaceNet/InceptionResnetV1 để trích xuất embedding 512 chiều.
4. So sánh embedding bằng cosine similarity.
5. Hiển thị `Matched` hoặc `Unknown` theo ngưỡng `0.7`.

## Quy trình xử lý

```text
Webcam frame
    ↓
OpenCV đọc ảnh BGR
    ↓
Đổi BGR sang RGB
    ↓
MTCNN phát hiện khuôn mặt
    ↓
Cắt và resize khuôn mặt về 160x160
    ↓
FaceNet trích xuất embedding
    ↓
Cosine similarity với embedding tham chiếu
    ↓
Hiển thị Matched hoặc Unknown
```

## Chuẩn bị ảnh tham chiếu

Cách 1: Chép ảnh có khuôn mặt rõ vào:

```text
CHUONG_3/PHAN_2/reference_faces/
```

Cách 2: Chụp trực tiếp bằng webcam:

```powershell
python CHUONG_3/PHAN_2/src/realtime_facenet_mtcnn.py --capture-reference --name sinh_vien
```

Khi cửa sổ webcam mở:

- Nhấn `s` để lưu ảnh tham chiếu.
- Nhấn `q` để thoát.

Nên dùng 2 đến 5 ảnh cùng một người, khác góc mặt hoặc ánh sáng nhẹ, để embedding trung bình ổn định hơn.

## Chạy nhận diện

```powershell
python CHUONG_3/PHAN_2/src/realtime_facenet_mtcnn.py
```

Mặc định:

- Camera index: `0`.
- Ngưỡng similarity: `0.7`.
- Thư mục ảnh tham chiếu: `CHUONG_3/PHAN_2/reference_faces`.

Có thể thay đổi ngưỡng:

```powershell
python CHUONG_3/PHAN_2/src/realtime_facenet_mtcnn.py --threshold 0.75
```

## Cách đọc kết quả

- `Matched 0.82`: khuôn mặt hiện tại giống ảnh tham chiếu vì similarity lớn hơn `0.7`.
- `Unknown 0.45`: khuôn mặt hiện tại không đủ giống ảnh tham chiếu.
- Không có khung: MTCNN chưa phát hiện được khuôn mặt, thường do mặt quá xa, thiếu sáng hoặc bị che.

## Lỗi thường gặp

1. Không mở được webcam:
   - Kiểm tra camera có đang bị ứng dụng khác dùng không.
   - Thử `--camera 1` nếu máy có nhiều camera.

2. Lần đầu chạy lâu:
   - Model pretrained có thể đang được tải về.

3. Nhận diện sai:
   - Thêm ảnh tham chiếu rõ hơn.
   - Điều chỉnh ngưỡng `--threshold`.
   - Đảm bảo khuôn mặt nhìn tương đối thẳng và đủ sáng.

4. Máy yếu, webcam bị giật:
   - Chạy CPU sẽ chậm hơn GPU.
   - Giảm độ phân giải webcam trong script nếu cần.
