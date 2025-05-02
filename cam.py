from picamzero import Camera
import os

home_dir = os.environ['HOME']
cam = Camera()

cam.start_preview()
print(f"{home_dir}/Desktop/sequencce.jpg")
cam.capture_sequence(f"{home_dir}/Desktop/sequence.jpg")
cam.stop_preview()
