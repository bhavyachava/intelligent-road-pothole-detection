"""
Database module for the Intelligent Road Pothole Detection
and Alert System.

Stores pothole detection records including location,
confidence, severity, and timestamp.
"""

import sqlite3


DATABASE_NAME = "pothole_detection.db"


def create_database():
    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS potholes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            latitude REAL NOT NULL,
            longitude REAL NOT NULL,
            confidence REAL,
            severity TEXT,
            detected_at TEXT
        )
    """)

    connection.commit()
    connection.close()


def add_pothole(latitude, longitude, confidence, severity, detected_at):
    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO potholes
        (latitude, longitude, confidence, severity, detected_at)
        VALUES (?, ?, ?, ?, ?)
    """, (
        latitude,
        longitude,
        confidence,
        severity,
        detected_at
    ))

    connection.commit()
    connection.close()


def get_potholes():
    connection = sqlite3.connect(DATABASE_NAME)

    cursor = connection.cursor()

    cursor.execute("""
        SELECT *
        FROM potholes
        ORDER BY detected_at DESC
    """)

    records = cursor.fetchall()

    connection.close()

    return records


if __name__ == "__main__":
    create_database()
    print("Pothole database initialized successfully.")
