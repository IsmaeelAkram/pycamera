import cv2
from .frame import Frame
import time


class ZeroFramesError(Exception):
    pass


class Camera:
    def __init__(self, device_index: int):
        self.device_index = device_index
        self.cap = cv2.VideoCapture(self.device_index)

    def set_resolution(self, w: int, h: int):
        """Set camera resolution"""
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, w)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, h)

    def set_fps(self, fps: int):
        """Set camera frames per second (FPS)"""
        if fps <= 0:
            raise ZeroFramesError(
                "Cannot show 0 FPS. If you want a single frame, use snap() instead"
            )
        self.cap.set(cv2.CAP_PROP_FPS, fps)

    def set(self, k: int, v):
        """Set a value from OpenCV"""
        self.cap.set(k, v)

    def snap(self, delay_seconds: float = 0, count: int = 30):
        """Snaps a picture from the camera. IF YOU ARE IN A LOOP, USE read(). THIS HAS A DELAY FOR LIGHTING"""
        time.sleep(delay_seconds)
        # ret, img = None, None
        for i in range(count):
            ret, img = self.cap.read()
        return Frame(img)

    def read(self):
        """Reads camera; better for loops. If taking a singular picture, use snap() to fix lighting/exposure."""
        ret, frame = self.cap.read()
        return Frame(frame)
