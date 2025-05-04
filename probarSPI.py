import spidev
spi = spidev.SpiDev()
spi.open(0, 0)  # Bus 0, CE0 (GPIO 8)
spi.max_speed_hz = 50000

# Enviamos un byte
to_send = [0xAA]
response = spi.xfer2(to_send)

print("Enviado:", to_send)
print("Recibido:", response)
