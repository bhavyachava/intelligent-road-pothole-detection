"""
Pothole detection module.

Provides a reusable function for running YOLO-based
pothole detection on an image.
"""

from ultralytics import YOLO


class PotholeDetector:
    def __init__(self, model_path):
        self.model = YOLO(model_path)

    def detect(self, image_path, confidence=0.25):
        results = self.model.predict(
            source=image_path,
            imgsz=640,
            conf=confidence,
            save=True,
        )

        return results


if __name__ == "__main__":
    MODEL_PATH = "../model/best.pt"
    IMAGE_PATH = "sample_road.jpg"

    detector = PotholeDetector(MODEL_PATH)
    results = detector.detect(IMAGE_PATH)

    print("Pothole detection completed.")
    print(f"Detections generated: {len(results)}")
