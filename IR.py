import os
import struct
import fcntl
import RPi.GPIO as GPIO
import time

# Configuración
LED_PIN = 24
LIRC_DEV = "/dev/lirc0"
PULSE_MASK = 0x01000000
MAX_BYTES = 8

# Inicializar GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.output(LED_PIN, GPIO.LOW)

print("Escuchando señales IR...")

# Tiempo de espera mínimo entre pulsos válidos (antirrebote)
tiempo_entre_pulsos = 0.5  # segundos
ultimo_pulso = 0

try:
    with open(LIRC_DEV, "rb") as lirc:
        fcntl.fcntl(lirc, fcntl.F_SETFL, os.O_NONBLOCK)

        while True:
            try:
                data = lirc.read(MAX_BYTES)
            except BlockingIOError:
                continue

            if not data or len(data) < 8:
                continue

            duration, = struct.unpack("I", data[:4])
            is_pulse = bool(struct.unpack("I", data[4:8])[0] & PULSE_MASK)

            ahora = time.time()
            if is_pulse and ahora - ultimo_pulso > tiempo_entre_pulsos:
                print(f"pulse {duration} µs")
                GPIO.output(LED_PIN, not GPIO.input(LED_PIN))
                print("LED ENCENDIDO" if GPIO.input(LED_PIN) else "LED APAGADO")
                ultimo_pulso = ahora

except KeyboardInterrupt:
    print("\nPrograma interrumpido por el usuario.")
finally:
    GPIO.cleanup()

