"""
Camera input module for the
Intelligent Road Pothole Detection and Alert System.
"""

import cv2


class CameraInput:
    def __init__(self, camera_index=0):
        self.camera_index = camera_index
        self.camera = None

    def start(self):
        """Start the camera."""
        self.camera = cv2.VideoCapture(self.camera_index)

        if not self.camera.isOpened():
            raise RuntimeError("Unable to open camera.")

        print("Camera started successfully.")

    def read_frame(self):
        """Read one frame from the camera."""

        if self.camera is None:
            raise RuntimeError("Camera has not been started.")

        success, frame = self.camera.read()

        if not success:
            raise RuntimeError("Unable to read camera frame.")

        return frame

    def stop(self):
        """Release the camera."""

        if self.camera is not None:
            self.camera.release()
            self.camera = None

        print("Camera stopped.")


if __name__ == "__main__":
    camera = CameraInput()

    try:
        camera.start()
        frame = camera.read_frame()

        print(f"Camera frame captured: {frame.shape}")

    finally:
        camera.stop()
