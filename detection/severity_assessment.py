"""
Pothole severity assessment module.

This module classifies detected potholes into
Low, Medium, or High severity based on the
detected pothole area relative to the image area.
"""


def calculate_severity(bounding_box, image_width, image_height):
    """
    Calculate pothole severity using bounding-box area.

    bounding_box format:
    (x1, y1, x2, y2)
    """

    x1, y1, x2, y2 = bounding_box

    pothole_width = max(0, x2 - x1)
    pothole_height = max(0, y2 - y1)

    pothole_area = pothole_width * pothole_height
    image_area = image_width * image_height

    if image_area == 0:
        raise ValueError("Image dimensions cannot be zero.")

    area_ratio = pothole_area / image_area

    if area_ratio < 0.05:
        return "Low"

    elif area_ratio < 0.15:
        return "Medium"

    else:
        return "High"


if __name__ == "__main__":
    example_box = (100, 100, 300, 250)

    severity = calculate_severity(
        example_box,
        image_width=640,
        image_height=640
    )

    print(f"Example pothole severity: {severity}")
