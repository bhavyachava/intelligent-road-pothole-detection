"""
GPS and database integration module for the
Intelligent Road Pothole Detection and Alert System.

This module connects GPS location data with
pothole detection records for database storage.
"""

from gps_module import create_location
from database.database import create_database, add_pothole


def save_pothole_detection(
    latitude,
    longitude,
    confidence,
    severity,
    detected_at
):
    """
    Create a GPS location and store the pothole
    detection record in the database.
    """

    location = create_location(latitude, longitude)

    add_pothole(
        location.latitude,
        location.longitude,
        confidence,
        severity,
        detected_at
    )

    return location


if __name__ == "__main__":
    create_database()

    location = save_pothole_detection(
        latitude=16.5062,
        longitude=80.6480,
        confidence=0.85,
        severity="Medium",
        detected_at="2026-09-22T19:00:00"
    )

    print("Pothole detection saved successfully.")
    print(f"Location: {location.latitude}, {location.longitude}")
