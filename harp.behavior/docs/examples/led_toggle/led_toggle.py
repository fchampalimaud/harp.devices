import time

from harp.devices.behavior import Behavior, DigitalOutputs

# Serial port corresponding to the Harp Behavior
SERIAL_PORT = "COM93"  # or "ttyUSBx" in Linux ("x" is the number of the serial port)

# Connect to a device
with Behavior(SERIAL_PORT) as device:
    # Set the maximum allowed current of the LED0 terminal to 10 mV
    device.write_led0_max_current(10)

    # Set the current of the LED0 terminal to 1 mV
    device.write_led0_current(1)

    # Activate the LED0 terminal
    device.write_output_set(DigitalOutputs.LED0)

    # Wait 3 seconds
    time.sleep(3)

    # Deactivate the LED0 terminal
    device.write_output_clear(DigitalOutputs.LED0)
