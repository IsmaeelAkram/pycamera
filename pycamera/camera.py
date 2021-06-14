import cv2
from .frame import Frame


class Camera:
    def __init__(self, device_index: int):
        self.device_index = device_index
        self.cap = cv2.VideoCapture(self.device_index)

    def snap(self, delay: float = 0, count: int = 30):
        """Snaps a picture from the camera. IF YOU ARE IN A LOOP, USE read(). THIS HAS A DELAY FOR LIGHTING"""
        ret, frame = None, None
        for i in range(count):
            ret, img = self.cap.read()
        return Frame(img)

    def read(self):
        """Snaps a picture from the camera. IF YOU ARE IN A LOOP, USE read(). THIS HAS A DELAY FOR LIGHTING"""
        ret, frame = self.cap.read()
        return Frame(frame)
