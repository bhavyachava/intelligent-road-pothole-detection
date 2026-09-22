"""
Camera configuration for the
Intelligent Road Pothole Detection and Alert System.
"""

CAMERA_INDEX = 0

FRAME_WIDTH = 1280
FRAME_HEIGHT = 720

FPS = 30

IMAGE_FORMAT = "jpg"


def get_camera_configuration():
    """Return the configured camera parameters."""

    return {
        "camera_index": CAMERA_INDEX,
        "frame_width": FRAME_WIDTH,
        "frame_height": FRAME_HEIGHT,
        "fps": FPS,
        "image_format": IMAGE_FORMAT,
    }


if __name__ == "__main__":
    configuration = get_camera_configuration()

    print("Camera configuration:")
    for key, value in configuration.items():
        print(f"{key}: {value}")
