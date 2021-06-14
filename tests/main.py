from pycamera import camera
import pycamera
import cv2
import time

pycamera.disable_logging()
cam = camera.Camera(0)

i = 0
while True:
    snap = cam.snap()
    snap.save(f"output-{i}.jpg")
    time.sleep(1)
    i += 1
