from pycamera import camera

cam = camera.Camera(1)

for i in range(5):
    snap = cam.snap()
    snap.save(f"output-{i}.jpg")
