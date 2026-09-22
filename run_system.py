"""
Project runner for the
Intelligent Road Pothole Detection and Alert System Using AI.

This file provides a simple entry point for initializing
the project modules.
"""

from database.database import create_database


def main():
    print("=" * 60)
    print("INTELLIGENT ROAD POTHOLE DETECTION AND ALERT SYSTEM")
    print("=" * 60)

    # Initialize database
    create_database()

    print("\nSystem components:")
    print("✓ Camera input")
    print("✓ YOLO pothole detection")
    print("✓ Severity assessment")
    print("✓ GPS location")
    print("✓ Database storage")
    print("✓ Alert management")
    print("✓ Dashboard")

    print("\nSystem initialization completed.")
    print("\nNext stage:")
    print("Connect the trained YOLO model and physical hardware.")


if __name__ == "__main__":
    main()
