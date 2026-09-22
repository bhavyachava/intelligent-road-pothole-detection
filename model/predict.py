"""
YOLO11 inference script for pothole detection.

The trained model is used to detect road-surface damage
in input images or video frames.
"""

from ultralytics import YOLO


MODEL_PATH = "runs/pothole_detection/yolo11n_rdd2022/weights/best.pt"
SOURCE = "sample_road.jpg"


def detect_potholes():
    model = YOLO(MODEL_PATH)

    results = model.predict(
        source=SOURCE,
        imgsz=640,
        conf=0.25,
        save=True,
        show_labels=True,
        show_conf=True,
    )

    return results


if __name__ == "__main__":
    detect_potholes()
