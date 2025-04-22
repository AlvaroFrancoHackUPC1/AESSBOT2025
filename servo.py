from gpiozero import Servo
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep

# Usa GPIO 12 (PWM0) y GPIO 19 (PWM1)
factory = PiGPIOFactory()

servo1 = Servo(12, pin_factory=factory, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000)
servo2 = Servo(19, pin_factory=factory, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000)

print("Moviendo a 0° (mínimo)")
servo1.min()
servo2.max()
sleep(2)

print("Moviendo a 90° (centro)")
servo1.mid()
servo2.mid()
sleep(2)

print("Moviendo a 180° (máximo)")
servo1.max()
servo2.min()
sleep(2)

print("Volviendo a centro")
servo1.mid()
servo2.mid()

