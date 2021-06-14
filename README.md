# pycamera

An easier solution to computer vision.

## What is pycamera?

PyCamera is a computer vision library for people who, don't know how to use OpenCV, don't want to use OpenCV for such a simple project, or want something easier!

## Installation

```sh
pip3 install pycamera
```

This will install pycamera, NumPy, and OpenCV.

## Examples

### Save Picture
```python
from pycamera import camera

cam = camera.Camera(0) # Choosing a camera
snap = cam.snap() # Snapping a picture from that camera

snap.save("output.jpg") # Save picture to output.jpg
```

### Editing with Pillow

```python
from pycamera import camera
from PIL import ImageDraw

cam = camera.Camera(0) # Choosing a camera
snap = cam.snap() # Snap photo
image = snap.to_pillow() # Convert pycamera image to Pillow image

draw = ImageDraw.Draw(image)
# Draw stuff here
image.show()
```

### Live View

```python
import pycamera
from pycamera import camera

cam = camera.Camera(0) # Choosing a camera

while True:
    snap = cam.read() # (reading is better for loops)
    snap.show()
    pycamera.waitForKey() # Wait until key is pressed (default key is Escape)
```