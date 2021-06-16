from pycamera import camera
from PIL import ImageDraw

cam = camera.Camera(0)  # Choosing a camera
snap = cam.snap()  # Snap photo
image = snap.to_pillow()  # Convert pycamera image to Pillow image

draw = ImageDraw.Draw(image)
white = (255, 255, 255)
draw.ellipse([(10, 10), (100, 100)], width=3, fill=white, outline=white)  # Draw circle
draw.rectangle([(140, 10), (240, 100)], fill=white, outline=white, width=3)
image.show()
