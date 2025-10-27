import time

from harp.devices.behavior import Behavior, PwmOutputs

# Serial port corresponding to the Harp Behavior
SERIAL_PORT = "COM93"  # or "ttyUSBx" in Linux ("x" is the number of the serial port)

# Connect to a device
with Behavior(SERIAL_PORT) as device:
    # Set the PWM frequency to 1 kHz
    device.write_pwm_frequency_do0(1000)

    # Set the PWM duty cycle to 50%
    device.write_pwm_duty_cycle_do0(50)

    # Start the PWM on the DO0
    device.write_pwm_start(PwmOutputs.PWM_DO0)

    # Wait 3 seconds
    time.sleep(3)

    # Set the PWM duty cycle to 10%
    device.write_pwm_duty_cycle_do0(10)

    # Wait another 3 seconds
    time.sleep(3)

    # Stop the PWM on the DO0
    device.write_pwm_stop(PwmOutputs.PWM_DO0)
