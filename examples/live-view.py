import pycamera
from pycamera import camera

cam = camera.Camera(0)  # Choosing a camera

while True:
    snap = cam.read()  # (reading is better for loops)
    snap.show()
    pycamera.waitForKey()  # Wait until key is pressed (default key is Escape)
