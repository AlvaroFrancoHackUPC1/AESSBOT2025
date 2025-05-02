import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)
GPIO.output(24, GPIO.HIGH)

print("GPIO 24 debería estar en HIGH (3.3 V).")
time.sleep(30)

GPIO.cleanup()
