from harp.devices.behavior import Behavior, BehaviorRegisters, EncoderInputs
from harp.protocol import OperationMode

# Serial port corresponding to the Harp Behavior
SERIAL_PORT = "COM93"  # or "ttyUSBx" in Linux ("x" is the number of the serial port)

# Connect to a device
with Behavior(SERIAL_PORT) as device:
    # Set device to Active Mode to be able to read the device's events
    device.set_mode(OperationMode.ACTIVE)

    # Enable the encoder
    device.write_enable_encoders(EncoderInputs.ENCODER_PORT2)

    # Reset the current encoder reading to be the new origin
    device.write_encoder_reset(EncoderInputs.ENCODER_PORT2)

    # Read the device's events
    try:
        while True:
            for msg in device.get_events():
                if msg.address == BehaviorRegisters.ANALOG_DATA:
                    # For this register, the first index (0) of the list corresponds to ADC0,
                    # the second index (1) to ADC1 and the third (2) to the Encoder
                    print(msg.payload[2])
                    print()
    except KeyboardInterrupt:
        # Capture Ctrl+C to exit gracefully
        print("\nTerminating...")
