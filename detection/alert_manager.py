"""
Alert management module for the
Intelligent Road Pothole Detection and Alert System.
"""


def create_alert(severity, latitude, longitude, confidence):
    """Create a structured pothole alert."""

    return {
        "alert_type": "Pothole Detected",
        "severity": severity,
        "latitude": float(latitude),
        "longitude": float(longitude),
        "confidence": float(confidence),
    }


def display_alert(alert):
    """Display a pothole alert."""

    print("\nPOTHOLE ALERT")
    print("-" * 30)
    print(f"Alert: {alert['alert_type']}")
    print(f"Severity: {alert['severity']}")
    print(f"Location: ({alert['latitude']}, {alert['longitude']})")
    print(f"Confidence: {alert['confidence']:.2f}")


if __name__ == "__main__":
    # Example values for testing only.
    alert = create_alert(
        severity="Medium",
        latitude=16.5062,
        longitude=80.6480,
        confidence=0.85,
    )

    display_alert(alert)
