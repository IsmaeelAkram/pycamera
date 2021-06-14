import pycamera
from pycamera import camera

cam = camera.Camera(1)

while True:
    snap = cam.read()
    snap.show()
    pycamera.waitForKey()