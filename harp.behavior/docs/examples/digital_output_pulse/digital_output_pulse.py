from harp.devices.behavior import Behavior, DigitalOutputs

# Serial port corresponding to the Harp Behavior
SERIAL_PORT = "COM93"  # or "ttyUSBx" in Linux ("x" is the number of the serial port)

# Connect to a device
with Behavior(SERIAL_PORT) as device:
    # Activate the pulse feature for DO0
    device.write_output_pulse_enable(DigitalOutputs.DO0)

    # Set the pulse duration of DO0 to 1000 ms
    device.write_pulse_do0(1000)

    # Activate the DO0 (which will stay active for 1000 ms)
    device.write_output_set(DigitalOutputs.DO0)
