"""
Dataset preprocessing utilities for the
Intelligent Road Pothole Detection and Alert System.

The module validates the YOLO dataset structure and
provides basic image preprocessing functionality.
"""

import os
import cv2


def validate_dataset(images_dir, labels_dir):
    """Check whether image and label directories exist."""
    if not os.path.isdir(images_dir):
        raise FileNotFoundError(f"Images directory not found: {images_dir}")

    if not os.path.isdir(labels_dir):
        raise FileNotFoundError(f"Labels directory not found: {labels_dir}")

    image_files = [
        f for f in os.listdir(images_dir)
        if f.lower().endswith((".jpg", ".jpeg", ".png"))
    ]

    label_files = [
        f for f in os.listdir(labels_dir)
        if f.lower().endswith(".txt")
    ]

    print(f"Images found: {len(image_files)}")
    print(f"Labels found: {len(label_files)}")

    return len(image_files), len(label_files)


def preprocess_image(image_path, image_size=(640, 640)):
    """Resize an input road image for model processing."""
    image = cv2.imread(image_path)

    if image is None:
        raise FileNotFoundError(f"Unable to read image: {image_path}")

    resized_image = cv2.resize(image, image_size)

    return resized_image


if __name__ == "__main__":
    print("Road damage preprocessing module loaded successfully.")
