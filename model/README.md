# Pothole Detection Model

This folder contains the machine learning model implementation
for the Intelligent Road Pothole Detection and Alert System.

## Model

The project uses YOLO11n for road-damage object detection.

The initial training dataset is RDD2022, containing four road-damage
classes:

1. Longitudinal crack
2. Transverse crack
3. Alligator crack
4. Pothole

## Files

### train.py

Contains the YOLO11 training configuration, including:

- Dataset configuration
- Number of training epochs
- Image size
- Batch size
- GPU device selection

### predict.py

Provides the inference procedure for running the trained YOLO model
on a road image.

## Training Configuration

| Parameter | Value |
|---|---:|
| Model | YOLO11n |
| Dataset | RDD2022 |
| Epochs | 30 |
| Image size | 640 × 640 |
| Batch size | 16 |
| Device | GPU |

## Training Status

Model training was initiated using the RDD2022 dataset.

The training process reached an intermediate stage before the
available Google Colab GPU session became unavailable due to
a usage limit.

Final model performance metrics will be added after training
and validation are completed.

## Important

The trained model weights (`.pt` files) are excluded from GitHub
using the project's `.gitignore` file.
