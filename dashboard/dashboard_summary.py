"""
Pothole detection dashboard summary module.

This module reads stored pothole detection records
and generates basic project statistics.
"""

import sqlite3


DATABASE_NAME = "../database/pothole_detection.db"


def generate_summary():
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    cursor.execute("SELECT COUNT(*) FROM potholes")
    total_potholes = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM potholes WHERE severity = 'Low'"
    )
    low_count = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM potholes WHERE severity = 'Medium'"
    )
    medium_count = cursor.fetchone()[0]

    cursor.execute(
        "SELECT COUNT(*) FROM potholes WHERE severity = 'High'"
    )
    high_count = cursor.fetchone()[0]

    cursor.execute(
        "SELECT AVG(confidence) FROM potholes"
    )
    average_confidence = cursor.fetchone()[0]

    connection.close()

    print("\nPOTHOLE DETECTION SUMMARY")
    print("-" * 40)
    print(f"Total potholes: {total_potholes}")
    print(f"Low severity: {low_count}")
    print(f"Medium severity: {medium_count}")
    print(f"High severity: {high_count}")

    if average_confidence is not None:
        print(f"Average confidence: {average_confidence:.2f}")
    else:
        print("Average confidence: No data available")


if __name__ == "__main__":
    generate_summary()
