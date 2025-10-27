from harp.devices.behavior import Behavior, BehaviorRegisters, DigitalInputs
from harp.protocol import OperationMode

# Serial port corresponding to the Harp Behavior
SERIAL_PORT = "COM93"  # or "ttyUSBx" in Linux ("x" is the number of the serial port)

# Connect to a device
with Behavior(SERIAL_PORT) as device:
    # Set device to Active Mode to be able to read the device's events
    device.set_mode(OperationMode.ACTIVE)

    # Read the device's events
    try:
        while True:
            for msg in device.get_events():
                if msg.address == BehaviorRegisters.DIGITAL_INPUT_STATE:
                    # Perform bitwise operation to filter only the state of the DI3 pin
                    print(bool(msg.payload & DigitalInputs.DI3))
                    print()
    except KeyboardInterrupt:
        # Capture Ctrl+C to exit gracefully
        print("\nTerminating...")
