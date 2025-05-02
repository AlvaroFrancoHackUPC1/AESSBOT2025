import os
import struct
import fcntl
import RPi.GPIO as GPIO
import time

# Configuración
LED_PIN = 25
LIRC_DEV = "/dev/lirc0"
PULSE_MASK = 0x01000000
MAX_BYTES = 8

# Inicializar GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.output(LED_PIN, GPIO.LOW)  # Comienza apagado

print("Escuchando señales IR...")

# Tiempo de espera mínimo entre pulsos válidos (antirrebote)
tiempo_entre_pulsos = 0.5  # segundos
ultimo_pulso = 0
led_encendido = False

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

                if not led_encendido:
                    GPIO.output(LED_PIN, GPIO.HIGH)
                    print("LED ENCENDIDO")
                    led_encendido = True

                ultimo_pulso = ahora

except KeyboardInterrupt:
    print("\nPrograma interrumpido por el usuario.")
finally:
    GPIO.cleanup()
