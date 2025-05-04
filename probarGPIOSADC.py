import RPi.GPIO as GPIO
import time

# Pines usados por SPI (modo BCM)
spi_gpio = [10, 9, 11, 8]  # CE1, CE0, MISO, MOSI, SCLK

GPIO.setmode(GPIO.BCM)

try:
    for pin in spi_gpio:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.HIGH)
        print(f"\n⚡ Probando GPIO {pin} (SPI): SALIDA en HIGH")
        print(f"→ Mide con multímetro entre GPIO {pin} y GND.")
        input("🔧 Pulsa Enter para continuar al siguiente pin...")
        GPIO.output(pin, GPIO.LOW)
        GPIO.cleanup(pin)

except KeyboardInterrupt:
    print("Interrumpido por el usuario.")
finally:
    GPIO.cleanup()
    print("\nGPIOs liberados. Test SPI terminado.")
