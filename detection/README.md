# Pothole Detection Module

This module implements the pothole detection component of the
Intelligent Road Pothole Detection and Alert System Using AI.

## Purpose

The module uses a YOLO-based object detection model to identify
potholes from road images.

## Processing Flow

Input Road Image
→ YOLO Object Detection
→ Pothole Bounding Box
→ Confidence Score
→ Severity Assessment

## Files

### pothole_detection.py
Provides the `PotholeDetector` class for loading the YOLO model
and performing pothole detection.

### detection_pipeline.py
Provides the initial integration structure for connecting
detection with GPS location and database storage.

### severity_assessment.py
Estimates pothole severity using the detected bounding-box area
relative to the image area.

## Model

The planned object detection model is YOLO11n trained using
the RDD2022 road-damage dataset.

## Current Status

The detection module has been implemented as part of the
project prototype. Model training, validation, and hardware
integration are being developed separately.
