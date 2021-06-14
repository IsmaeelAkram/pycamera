# pycamera

An easier solution to computer vision.

## What is pycamera?

Pycamera is a wrapper around OpenCV for people who, don't know how to use OpenCV, don't want to use OpenCV for such a simple project, or want something easier!

## Installation

```sh
pip3 install pycamera
```

This will install pycamera, NumPy, and OpenCV.

## Example Usage

```python
from pycamera import camera

cam = camera.Camera(1) # Choosing a camera
snap = cam.snap() # Snapping a picture from that camera

snap.save("output.jpg") # Save picture to output.jpg
```
