"""
Main detection pipeline for the
Intelligent Road Pothole Detection and Alert System.

System flow:
Image Input
→ Pothole Detection
→ GPS Location
→ Database Storage
→ Alert Generation
"""

from pothole_detection import PotholeDetector
from gps_mapping.gps_module import create_location
from database.database import create_database, add_pothole
from alert_manager import create_alert, display_alert


def process_detection(
    image_path,
    model_path,
    latitude,
    longitude,
    severity="Unknown"
):
    """
    Run pothole detection and connect the result
    with GPS, database storage, and alert generation.
    """

    detector = PotholeDetector(model_path)

    results = detector.detect(image_path)

    location = create_location(
        latitude,
        longitude
    )

    detections = []

    for result in results:

        detection_record = {
            "result": result,
            "latitude": location.latitude,
            "longitude": location.longitude,
            "timestamp": location.timestamp,
        }

        detections.append(detection_record)

    return detections


def save_detection(
    latitude,
    longitude,
    confidence,
    severity,
    detected_at
):
    """
    Save a pothole detection to the database
    and generate an alert.
    """

    add_pothole(
        latitude,
        longitude,
        confidence,
        severity,
        detected_at
    )

    alert = create_alert(
        severity=severity,
        latitude=latitude,
        longitude=longitude,
        confidence=confidence
    )

    display_alert(alert)

    return alert


def initialize_pipeline():
    """Initialize the project database."""

    create_database()

    print("=" * 55)
    print("POTHOLE DETECTION PIPELINE")
    print("=" * 55)

    print("Detection module: Ready")
    print("GPS module: Ready")
    print("Database module: Ready")
    print("Alert module: Ready")

    print()
    print("Pipeline:")
    print("Image")
    print("  ↓")
    print("YOLO Detection")
    print("  ↓")
    print("GPS Location")
    print("  ↓")
    print("Database")
    print("  ↓")
    print("Alert")


if __name__ == "__main__":
    initialize_pipeline()
