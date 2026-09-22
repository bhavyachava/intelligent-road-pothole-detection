"""
Basic tests for the pothole severity assessment module.
"""

from detection.severity_assessment import calculate_severity


def test_low_severity():
    severity = calculate_severity(
        (0, 0, 100, 100),
        1000,
        1000
    )

    assert severity == "Low"


def test_medium_severity():
    severity = calculate_severity(
        (0, 0, 300, 300),
        1000,
        1000
    )

    assert severity == "Medium"


def test_high_severity():
    severity = calculate_severity(
        (0, 0, 500, 500),
        1000,
        1000
    )

    assert severity == "High"


if __name__ == "__main__":
    test_low_severity()
    test_medium_severity()
    test_high_severity()

    print("All severity assessment tests passed.")
