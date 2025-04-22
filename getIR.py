import os
import struct

LIRC_DEV = "/dev/lirc0"
PULSE_MASK = 0x01000000  # Bit que indica si es un pulso o un espacio
MAX_BYTES = 8  # Cada evento ocupa 8 bytes

with open(LIRC_DEV, "rb") as lirc:
    print("Escuchando señales IR...")
    while True:
        data = lirc.read(MAX_BYTES)
        if not data:
            continue
        duration, = struct.unpack("I", data[:4])  # Duración del pulso
        is_pulse = bool(struct.unpack("I", data[4:])[0] & PULSE_MASK)
        tipo = "pulse" if is_pulse else "space"
        print(f"{tipo} {duration} µs")

