import RPi.GPIO as GPIO
import time

LED_PIN = 24  # GPIO donde está conectado el LED

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

print("Parpadeando LED en GPIO 24. Pulsa Ctrl+C para salir.")

try:
    while True:
        GPIO.output(LED_PIN, GPIO.HIGH)  # Enciende LED
        time.sleep(0.5)                  # Espera 0.5 segundos
        GPIO.output(LED_PIN, GPIO.LOW)   # Apaga LED
        time.sleep(0.5)                  # Espera 0.5 segundos
except KeyboardInterrupt:
    GPIO.cleanup()
    print("\nPrograma terminado. GPIO liberado.")

