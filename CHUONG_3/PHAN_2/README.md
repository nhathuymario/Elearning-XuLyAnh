# Chương 3 - Phần 2: Nhận diện khuôn mặt thời gian thực với FaceNet & MTCNN

Thư mục này chứa bài thực hành nhận diện khuôn mặt thời gian thực từ webcam bằng:

- OpenCV: truy cập webcam, đọc từng frame, hiển thị kết quả.
- MTCNN: phát hiện khuôn mặt trong từng frame.
- FaceNet/InceptionResnetV1: trích xuất vector đặc trưng khuôn mặt.
- Cosine similarity: so sánh khuôn mặt hiện tại với khuôn mặt tham chiếu.

Điều kiện hiển thị:

- `similarity > 0.7`: hiển thị `Matched`.
- `similarity <= 0.7`: hiển thị `Unknown`.

## Cấu trúc file

```text
CHUONG_3/PHAN_2/
├── BAI_THUC_HANH_CHUONG_3_PHAN_2_FACENET_MTCNN.ipynb
├── README.md
├── reference_faces/                 # Chứa ảnh khuôn mặt mẫu
├── outputs/                         # Lưu ảnh kết quả nếu bật --save-output
├── src/
│   └── realtime_facenet_mtcnn.py    # Script chạy webcam trực tiếp
└── TAI_LIEU/
    └── HUONG_DAN_THUC_HANH_FACENET_MTCNN.md
```

## Cách chạy nhanh

1. Cài thư viện:

```powershell
pip install -r requirements.txt
```

2. Chụp ảnh khuôn mặt tham chiếu nếu thư mục `reference_faces/` chưa có ảnh:

```powershell
python CHUONG_3/PHAN_2/src/realtime_facenet_mtcnn.py --capture-reference --name sinh_vien
```

Không gõ `script --capture-reference`; `script` chỉ là cách gọi chung, còn file cần chạy là `src/realtime_facenet_mtcnn.py`.

Nhấn `s` để lưu ảnh, nhấn `q` để thoát.

3. Chạy nhận diện thời gian thực:

```powershell
python CHUONG_3/PHAN_2/src/realtime_facenet_mtcnn.py
```

Nhấn `q` để thoát webcam.

4. Mở notebook để học theo từng cell:

```powershell
jupyter lab CHUONG_3/PHAN_2/BAI_THUC_HANH_CHUONG_3_PHAN_2_FACENET_MTCNN.ipynb
```

## Ghi chú

Lần chạy đầu tiên, `facenet-pytorch` có thể tải trọng số pretrained cho FaceNet/InceptionResnetV1. Nếu máy không có GPU, chương trình tự chạy bằng CPU nhưng tốc độ có thể chậm hơn.

Nếu gặp lỗi `ModuleNotFoundError: No module named 'torch'`, hãy cài thư viện vào đúng môi trường Python đang chạy:

```powershell
python -m pip install -r requirements.txt
```

Nếu đang dùng Python 3.13 trở lên và `facenet-pytorch` bị lỗi khi kéo dependency cũ, dùng bộ lệnh đã kiểm thử dưới đây:

```powershell
python -m pip install torch torchvision tqdm
python -m pip install facenet-pytorch --no-deps
```

Trong notebook, nên chạy cell **1.1. Cài đặt thư viện nếu thiếu** trước cell import. Cell này đã tự chọn cách cài phù hợp với phiên bản Python của kernel.
