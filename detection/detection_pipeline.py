"""
Main detection pipeline for the
Intelligent Road Pothole Detection and Alert System.

The pipeline connects pothole detection with
GPS location information and database storage.
"""

from pothole_detection import PotholeDetector
from gps_mapping.gps_module import create_location, attach_location_to_detection
from database.database import create_database, add_pothole


def process_detection(image_path, model_path, latitude, longitude):
    """Run pothole detection and attach GPS information."""

    detector = PotholeDetector(model_path)
    results = detector.detect(image_path)

    location = create_location(latitude, longitude)

    detections = []

    for result in results:
        detections.append(
            attach_location_to_detection(result, location)
        )

    return detections


if __name__ == "__main__":
    create_database()

    print("Pothole detection pipeline initialized.")
    print("Modules: Detection → GPS → Database")
