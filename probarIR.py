import RPi.GPIO as GPIO
import time

PIN_OUT = 23  # Salida fija en HIGH
PIN_IN = 24   # Entrada que lee

GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN_OUT, GPIO.OUT)
GPIO.setup(PIN_IN, GPIO.IN)

# Ponemos GPIO 23 en HIGH
GPIO.output(PIN_OUT, GPIO.HIGH)
print("GPIO 23 fijado en HIGH. Leyendo GPIO 24 cada 0.5s...")

contador = 0

try:
    while True:
        estado = GPIO.input(PIN_IN)
        print(f"[{contador}] GPIO 24 detecta: {'HIGH' if estado else 'LOW'}")
        contador += 1
        time.sleep(0.5)

except KeyboardInterrupt:
    GPIO.cleanup()
    print("GPIO liberado. Fin de la prueba.")
