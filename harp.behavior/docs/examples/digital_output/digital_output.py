import time

from harp.devices.behavior import Behavior, DigitalOutputs

# Serial port corresponding to the Harp Behavior
SERIAL_PORT = "COM93"  # or "ttyUSBx" in Linux ("x" is the number of the serial port)

# Connect to a device
with Behavior(SERIAL_PORT) as device:
    # Activate DO0
    device.write_output_set(DigitalOutputs.DO0)
    print("DO0 activated!")

    # Wait 3 seconds
    time.sleep(3)

    # Deactivate DO0
    device.write_output_clear(DigitalOutputs.DO0)
    print("DO0 deactivated!")
