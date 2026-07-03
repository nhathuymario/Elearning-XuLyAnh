from __future__ import annotations

import argparse
from datetime import datetime
from pathlib import Path
from typing import Iterable

import cv2
import numpy as np
import torch
import torch.nn.functional as F
from facenet_pytorch import InceptionResnetV1, MTCNN, fixed_image_standardization


IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".bmp", ".webp"}
BASE_DIR = Path(__file__).resolve().parents[1]
DEFAULT_REFERENCE_DIR = BASE_DIR / "reference_faces"
DEFAULT_OUTPUT_DIR = BASE_DIR / "outputs"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Nhan dien khuon mat thoi gian thuc bang FaceNet va MTCNN."
    )
    parser.add_argument("--camera", type=int, default=0, help="Index webcam, mac dinh la 0.")
    parser.add_argument(
        "--threshold",
        type=float,
        default=0.7,
        help="Nguong cosine similarity. > threshold la Matched, nguoc lai la Unknown.",
    )
    parser.add_argument(
        "--reference-dir",
        type=Path,
        default=DEFAULT_REFERENCE_DIR,
        help="Thu muc chua anh khuon mat tham chieu.",
    )
    parser.add_argument(
        "--capture-reference",
        action="store_true",
        help="Mo webcam de chup anh tham chieu. Nhan s de luu, q de thoat.",
    )
    parser.add_argument(
        "--name",
        default="reference",
        help="Tien to ten file khi chup anh tham chieu.",
    )
    parser.add_argument(
        "--save-output",
        action="store_true",
        help="Nhan p trong luc nhan dien de luu frame ket qua vao outputs.",
    )
    return parser.parse_args()


def select_device() -> torch.device:
    return torch.device("cuda:0" if torch.cuda.is_available() else "cpu")


def load_models(device: torch.device) -> tuple[MTCNN, InceptionResnetV1]:
    detector = MTCNN(keep_all=True, device=device)
    recognizer = InceptionResnetV1(pretrained="vggface2").eval().to(device)
    return detector, recognizer


def list_images(folder: Path) -> list[Path]:
    if not folder.exists():
        return []
    return sorted(
        path
        for path in folder.iterdir()
        if path.is_file() and path.suffix.lower() in IMAGE_EXTENSIONS
    )


def bgr_to_rgb(frame_bgr: np.ndarray) -> np.ndarray:
    return cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2RGB)


def clip_box(box: Iterable[float], width: int, height: int, margin: int = 20) -> tuple[int, int, int, int]:
    x1, y1, x2, y2 = [int(round(value)) for value in box]
    x1 = max(0, x1 - margin)
    y1 = max(0, y1 - margin)
    x2 = min(width, x2 + margin)
    y2 = min(height, y2 + margin)
    return x1, y1, x2, y2


def crop_face(image_rgb: np.ndarray, box: Iterable[float], margin: int = 20) -> np.ndarray | None:
    height, width = image_rgb.shape[:2]
    x1, y1, x2, y2 = clip_box(box, width, height, margin=margin)
    if x2 <= x1 or y2 <= y1:
        return None
    return image_rgb[y1:y2, x1:x2]


def face_to_tensor(face_rgb: np.ndarray, device: torch.device) -> torch.Tensor:
    face_resized = cv2.resize(face_rgb, (160, 160), interpolation=cv2.INTER_AREA)
    tensor = torch.from_numpy(face_resized).permute(2, 0, 1).float()
    tensor = fixed_image_standardization(tensor)
    return tensor.unsqueeze(0).to(device)


@torch.no_grad()
def get_embedding(face_rgb: np.ndarray, recognizer: InceptionResnetV1, device: torch.device) -> torch.Tensor:
    face_tensor = face_to_tensor(face_rgb, device)
    embedding = recognizer(face_tensor)
    return F.normalize(embedding, p=2, dim=1)


def cosine_similarity(embedding_a: torch.Tensor, embedding_b: torch.Tensor) -> float:
    return float(F.cosine_similarity(embedding_a, embedding_b).item())


def detect_largest_face(detector: MTCNN, image_rgb: np.ndarray) -> np.ndarray | None:
    boxes, probabilities = detector.detect(image_rgb)
    if boxes is None or probabilities is None:
        return None
    valid_indices = [idx for idx, prob in enumerate(probabilities) if prob is not None and prob >= 0.90]
    if not valid_indices:
        return None
    largest_idx = max(
        valid_indices,
        key=lambda idx: (boxes[idx][2] - boxes[idx][0]) * (boxes[idx][3] - boxes[idx][1]),
    )
    return boxes[largest_idx]


def build_reference_embedding(
    reference_dir: Path,
    detector: MTCNN,
    recognizer: InceptionResnetV1,
    device: torch.device,
) -> torch.Tensor:
    image_paths = list_images(reference_dir)
    if not image_paths:
        raise FileNotFoundError(
            f"Khong co anh tham chieu trong {reference_dir}. "
            "Hay chay voi --capture-reference hoac chep anh vao thu muc nay."
        )

    embeddings: list[torch.Tensor] = []
    for image_path in image_paths:
        frame_bgr = cv2.imread(str(image_path))
        if frame_bgr is None:
            print(f"[WARN] Khong doc duoc anh: {image_path}")
            continue

        image_rgb = bgr_to_rgb(frame_bgr)
        box = detect_largest_face(detector, image_rgb)
        if box is None:
            print(f"[WARN] Khong tim thay khuon mat ro trong: {image_path.name}")
            continue

        face_rgb = crop_face(image_rgb, box)
        if face_rgb is None:
            continue
        embeddings.append(get_embedding(face_rgb, recognizer, device))

    if not embeddings:
        raise RuntimeError("Khong tao duoc embedding tham chieu tu cac anh hien co.")

    mean_embedding = torch.mean(torch.cat(embeddings, dim=0), dim=0, keepdim=True)
    return F.normalize(mean_embedding, p=2, dim=1)


def open_camera(camera_index: int) -> cv2.VideoCapture:
    capture = cv2.VideoCapture(camera_index)
    if not capture.isOpened():
        raise RuntimeError(f"Khong mo duoc webcam index {camera_index}.")
    return capture


def capture_reference_images(args: argparse.Namespace) -> None:
    args.reference_dir.mkdir(parents=True, exist_ok=True)
    capture = open_camera(args.camera)
    print("[INFO] Nhan 's' de luu anh tham chieu, 'q' de thoat.")

    try:
        while True:
            ok, frame_bgr = capture.read()
            if not ok:
                print("[WARN] Khong doc duoc frame tu webcam.")
                break

            preview = frame_bgr.copy()
            cv2.putText(
                preview,
                "Press s: save reference | q: quit",
                (20, 35),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.75,
                (0, 255, 255),
                2,
            )
            cv2.imshow("Capture reference face", preview)

            key = cv2.waitKey(1) & 0xFF
            if key == ord("s"):
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                output_path = args.reference_dir / f"{args.name}_{timestamp}.jpg"
                cv2.imwrite(str(output_path), frame_bgr)
                print(f"[OK] Da luu: {output_path}")
            elif key == ord("q"):
                break
    finally:
        capture.release()
        cv2.destroyAllWindows()


def draw_result(
    frame_bgr: np.ndarray,
    box: Iterable[float],
    label: str,
    similarity: float,
    color: tuple[int, int, int],
) -> None:
    height, width = frame_bgr.shape[:2]
    x1, y1, x2, y2 = clip_box(box, width, height, margin=0)
    cv2.rectangle(frame_bgr, (x1, y1), (x2, y2), color, 2)
    text = f"{label} {similarity:.2f}"
    cv2.putText(
        frame_bgr,
        text,
        (x1, max(25, y1 - 10)),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.75,
        color,
        2,
    )


def run_realtime_recognition(args: argparse.Namespace) -> None:
    device = select_device()
    print(f"[INFO] Device: {device}")
    detector, recognizer = load_models(device)
    reference_embedding = build_reference_embedding(args.reference_dir, detector, recognizer, device)

    capture = open_camera(args.camera)
    DEFAULT_OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    print("[INFO] Nhan 'q' de thoat. Neu bat --save-output, nhan 'p' de luu frame.")

    try:
        while True:
            ok, frame_bgr = capture.read()
            if not ok:
                print("[WARN] Khong doc duoc frame tu webcam.")
                break

            frame_rgb = bgr_to_rgb(frame_bgr)
            boxes, probabilities = detector.detect(frame_rgb)

            if boxes is not None and probabilities is not None:
                for box, probability in zip(boxes, probabilities):
                    if probability is None or probability < 0.90:
                        continue

                    face_rgb = crop_face(frame_rgb, box)
                    if face_rgb is None:
                        continue

                    embedding = get_embedding(face_rgb, recognizer, device)
                    similarity = cosine_similarity(embedding, reference_embedding)
                    is_matched = similarity > args.threshold
                    label = "Matched" if is_matched else "Unknown"
                    color = (0, 220, 0) if is_matched else (0, 0, 255)
                    draw_result(frame_bgr, box, label, similarity, color)

            cv2.putText(
                frame_bgr,
                f"Threshold: {args.threshold:.2f}",
                (20, 35),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.75,
                (255, 255, 0),
                2,
            )
            cv2.imshow("FaceNet + MTCNN realtime recognition", frame_bgr)

            key = cv2.waitKey(1) & 0xFF
            if key == ord("p") and args.save_output:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                output_path = DEFAULT_OUTPUT_DIR / f"recognition_{timestamp}.jpg"
                cv2.imwrite(str(output_path), frame_bgr)
                print(f"[OK] Da luu: {output_path}")
            elif key == ord("q"):
                break
    finally:
        capture.release()
        cv2.destroyAllWindows()


def main() -> None:
    args = parse_args()
    if args.capture_reference:
        capture_reference_images(args)
    else:
        run_realtime_recognition(args)


if __name__ == "__main__":
    main()
