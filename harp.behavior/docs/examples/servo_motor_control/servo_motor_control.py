import time

from harp.devices.behavior import Behavior, ServoOutputs

# Serial port corresponding to the Harp Behavior
SERIAL_PORT = "COM93"  # or "ttyUSBx" in Linux ("x" is the number of the serial port)


# Convert the servo position in degrees to the respective pulse duration (ms)
def degrees_to_pulse_duration(pos: int):
    assert 0 <= pos <= 90, "The position must be between 0 and 90"

    # Calculate the parameters of the linear conversion from degrees to pulse duration
    slope = (2000 - 1000) / 90
    intercept = 1000

    return int(slope * pos + intercept)


# Connect to a device
with Behavior(SERIAL_PORT) as device:
    # Set the servo motor period to 20000 ms
    device.write_servo_motor2_period(20000)

    # Set the servo motor to the initial position
    init_pos = degrees_to_pulse_duration(0)
    device.write_servo_motor2_pulse(init_pos)

    # Enable the servo motor
    device.write_enable_servos(ServoOutputs.SERVO_OUTPUT2)

    # Wait for 3 seconds
    time.sleep(3)

    # Set the servo motor to a new position
    final_pos = degrees_to_pulse_duration(90)
    device.write_servo_motor2_pulse(final_pos)

    # Disable the servo motor
    device.write_disable_servos(ServoOutputs.SERVO_OUTPUT2)
