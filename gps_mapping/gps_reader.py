"""
GPS reader module for the
Intelligent Road Pothole Detection and Alert System.

This module provides the structure for reading GPS
coordinates from a GPS receiver connected to the
prototype hardware.
"""

from dataclasses import dataclass
from datetime import datetime


@dataclass
class GPSData:
    latitude: float
    longitude: float
    timestamp: str


def create_gps_data(latitude, longitude):
    """Create a GPS data record."""
    return GPSData(
        latitude=float(latitude),
        longitude=float(longitude),
        timestamp=datetime.now().isoformat()
    )


def validate_coordinates(latitude, longitude):
    """Validate latitude and longitude ranges."""

    if not -90 <= float(latitude) <= 90:
        return False

    if not -180 <= float(longitude) <= 180:
        return False

    return True


if __name__ == "__main__":
    latitude = 16.5062
    longitude = 80.6480

    if validate_coordinates(latitude, longitude):
        gps_data = create_gps_data(latitude, longitude)

        print("GPS data created successfully.")
        print(f"Latitude: {gps_data.latitude}")
        print(f"Longitude: {gps_data.longitude}")
        print(f"Timestamp: {gps_data.timestamp}")
    else:
        print("Invalid GPS coordinates.")
