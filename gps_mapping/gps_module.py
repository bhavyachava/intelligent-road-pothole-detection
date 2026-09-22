"""
GPS module for the Intelligent Road Pothole Detection
and Alert System.

This module stores GPS coordinates associated with
detected potholes.
"""

from dataclasses import dataclass
from datetime import datetime


@dataclass
class GPSLocation:
    latitude: float
    longitude: float
    timestamp: str


def create_location(latitude, longitude):
    """Create a GPS location record."""
    return GPSLocation(
        latitude=float(latitude),
        longitude=float(longitude),
        timestamp=datetime.now().isoformat(),
    )


def attach_location_to_detection(detection, location):
    """Attach GPS coordinates to a pothole detection."""
    return {
        "detection": detection,
        "latitude": location.latitude,
        "longitude": location.longitude,
        "timestamp": location.timestamp,
    }


if __name__ == "__main__":
    location = create_location(16.5062, 80.6480)

    print("GPS location created:")
    print(f"Latitude: {location.latitude}")
    print(f"Longitude: {location.longitude}")
    print(f"Timestamp: {location.timestamp}")
