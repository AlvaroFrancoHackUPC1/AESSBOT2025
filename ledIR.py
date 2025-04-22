import os
import struct
import RPi.GPIO as GPIO
from time import sleep

# Configuración
LED_PIN = 24
LIRC_DEV = "/dev/lirc0"
PULSE_MASK = 0x01000000
MAX_BYTES = 8

# Inicializar GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.output(LED_PIN, GPIO.LOW)  # LED inicialmente apagado

print("Escuchando señales IR...")


try:
    with open(LIRC_DEV, "rb") as lirc:
        while True:
            data = lirc.read(MAX_BYTES)
            if not data:
                continue

            duration, = struct.unpack("I", data[:4])
            is_pulse = bool(struct.unpack("I", data[4:])[0] & PULSE_MASK)

            if is_pulse:
                print(f"pulse {duration} µs")
                if not GPIO.input(LED_PIN):
                    GPIO.output(LED_PIN, GPIO.HIGH)
                    print("LED ENCENDIDO")
                else:
                    GPIO.output(LED_PIN, GPIO.LOW)
                    print("LED APAGADO")
                sleep(1)

except KeyboardInterrupt:
    print("\nPrograma interrumpido por el usuario.")
finally:
    GPIO.cleanup()

