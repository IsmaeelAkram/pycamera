from pycamera import camera
from PIL import ImageDraw

cam = camera.Camera(0)  # Choosing a camera
snap = cam.snap()  # Snap photo
image = snap.to_pillow()  # Convert pycamera image to Pillow image

draw = ImageDraw.Draw(image)
# Draw stuff here
image.show()