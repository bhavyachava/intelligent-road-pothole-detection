"""
Basic dashboard module for the Intelligent Road Pothole
Detection and Alert System.

Displays stored pothole detection records.
"""

import sqlite3


DATABASE_NAME = "../database/pothole_detection.db"


def load_pothole_records():
    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, latitude, longitude, confidence, severity, detected_at
        FROM potholes
        ORDER BY detected_at DESC
    """)

    records = cursor.fetchall()

    connection.close()

    return records


def display_records():
    records = load_pothole_records()

    print("\nPOTHOLE DETECTION DASHBOARD")
    print("-" * 70)

    if not records:
        print("No pothole records available.")
        return

    for record in records:
        print(
            f"ID: {record[0]} | "
            f"Location: ({record[1]}, {record[2]}) | "
            f"Confidence: {record[3]} | "
            f"Severity: {record[4]} | "
            f"Detected: {record[5]}"
        )


if __name__ == "__main__":
    display_records()
