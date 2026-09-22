# Model Results

This folder contains the evaluation results of the pothole detection
model used in the Intelligent Road Pothole Detection and Alert System.

## Evaluation Metrics

The following metrics will be recorded after model training and
validation are completed:

- Precision
- Recall
- mAP@0.5
- mAP@0.5:0.95
- Validation loss
- Inference performance

## Current Status

YOLO11n training was initiated using the RDD2022 road-damage dataset.

The training session reached an intermediate stage before the
Google Colab GPU became unavailable because of the applicable
usage limit.

Final evaluation values have not yet been recorded.

## Result Files

The following files may be added after training:

- Confusion matrix
- Training/validation curves
- Precision-recall curve
- Validation predictions
- Sample pothole detection images

Only results generated from the actual project training and
validation process will be documented here.
