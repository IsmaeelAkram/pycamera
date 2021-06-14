import cv2
import numpy as np


class Frame:
    def __init__(self, frame: np.ndarray):
        self.frame = frame

    def to_numpy(self) -> np.ndarray:
        """Returns raw NumPy array"""
        return self.frame

    def rgb(self):
        """Converts BGR frame to RGB"""
        return Frame(cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB))

    def pillow(self):
        """Returns a PIL (Pillow) compatible image. Alias of rgb()"""
        return self.rgb()

    def show(self):
        cv2.imshow("pycamera frame", self.frame)

    def save(self, fp: str):
        """Writes image to file"""
        cv2.imwrite(fp, self.frame)
