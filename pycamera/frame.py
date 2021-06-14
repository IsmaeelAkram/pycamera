import cv2
import numpy as np


class Frame:
    def __init__(self, frame: np.ndarray):
        self.frame = frame

    def to_numpy(self) -> np.ndarray:
        return self.frame

    def rgb(self):
        return cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)

    def show(self):
        cv2.imshow("pycamera frame", self.frame)

    def save(self, fp: str):
        cv2.imwrite(fp, self.frame)
