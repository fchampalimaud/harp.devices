from harp.devices.soundcard import SoundCard

# Serial port corresponding to the Harp SoundCard
SERIAL_PORT = "COM93"  # or "ttyUSBx" in Linux ("x" is the number of the serial port)

with SoundCard(SERIAL_PORT) as device:
    # Play the sound previously upload to the index 2 of the SoundCard
    device.write_play_sound_or_frequency(2)
