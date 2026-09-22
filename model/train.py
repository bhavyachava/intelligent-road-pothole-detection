"""
YOLO11 training script for the Intelligent Road Pothole Detection
and Alert System.

Dataset: RDD2022
Model: YOLO11n
"""

from ultralytics import YOLO


DATASET_CONFIG = "../dataset/data.yaml"
MODEL_NAME = "yolo11n.pt"

EPOCHS = 30
IMAGE_SIZE = 640
BATCH_SIZE = 16


def train_model():
    model = YOLO(MODEL_NAME)

    model.train(
        data=DATASET_CONFIG,
        epochs=EPOCHS,
        imgsz=IMAGE_SIZE,
        batch=BATCH_SIZE,
        device=0,
        project="runs/pothole_detection",
        name="yolo11n_rdd2022",
    )


if __name__ == "__main__":
    train_model()
