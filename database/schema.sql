-- Database schema for the Intelligent Road Pothole
-- Detection and Alert System

CREATE TABLE IF NOT EXISTS potholes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    latitude REAL NOT NULL,
    longitude REAL NOT NULL,
    confidence REAL,
    severity TEXT,
    detected_at TEXT
);

-- Example fields:
-- latitude   : GPS latitude of detected pothole
-- longitude  : GPS longitude of detected pothole
-- confidence : YOLO detection confidence
-- severity   : pothole severity classification
-- detected_at: date and time of detection
