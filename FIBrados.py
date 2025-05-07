from gpiozero import Servo
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep

# Usamos PiGPIOFactory para controlar los servos con precisión
factory = PiGPIOFactory()

# Subclase que invierte el valor del servo automáticamente
class InvertedServo(Servo):
    @property
    def value(self):
        return -super().value

    @value.setter
    def value(self, v):
        super(InvertedServo, self.__class__).value.fset(self, -v)

# Servo montado normalmente en GPIO12
servo1 = Servo(12, pin_factory=factory, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000)

# Servo montado al revés en GPIO13, usamos InvertedServo
servo2 = InvertedServo(13, pin_factory=factory, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000)

# Prueba de movimiento sincronizado

print("Moviendo a posición máxima")
servo1.value = 1
servo2.value = 1
sleep(1)

print("Moviendo a posición central")
servo1.value = 0
servo2.value = 0
sleep(1)

print("Moviendo a posición mínima")
servo1.value = -1
servo2.value = -1
sleep(1)
