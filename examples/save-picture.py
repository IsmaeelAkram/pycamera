from pycamera import camera

cam = camera.Camera(0)  # Choosing a camera
snap = cam.snap()  # Snapping a picture from that camera

snap.save("output.jpg")  # Save picture to output.jpg
