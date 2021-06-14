import cv2
import frame


class Camera:
    def __init__(self, device_index: int):
        self.device_index = device_index
        self.cap = cv2.VideoCapture(self.device_index)

    def snap(self, delay: float = 0, count: int = 30):
        ret, frame = None, None
        for i in range(count):
            ret, frame = self.cap.read()
        return Frame(frame)
