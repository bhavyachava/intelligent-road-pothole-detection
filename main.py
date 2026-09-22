"""
Main entry point for the
Intelligent Road Pothole Detection and Alert System Using AI.

System flow:
Image Input
→ Pothole Detection
→ Severity Assessment
→ GPS Location
→ Database Storage
"""

from detection.pothole_detection import PotholeDetector
from detection.severity_assessment import calculate_severity
from gps_mapping.gps_module import create_location
from database.database import create_database


def initialize_system():
    """Initialize the project database and core system modules."""

    create_database()

    print("=" * 55)
    print("INTELLIGENT ROAD POTHOLE DETECTION SYSTEM")
    print("=" * 55)
    print("System initialized successfully.")
    print()
    print("Pipeline:")
    print("1. Road image acquisition")
    print("2. YOLO-based pothole detection")
    print("3. Severity assessment")
    print("4. GPS location tagging")
    print("5. Database storage")
    print("6. Dashboard and alert generation")


if __name__ == "__main__":
    initialize_system()
