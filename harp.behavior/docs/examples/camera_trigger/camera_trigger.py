import time

from harp.devices.behavior import Behavior, CameraOutputs

# Serial port corresponding to the Harp Behavior
SERIAL_PORT = "COM93"  # or "ttyUSBx" in Linux ("x" is the number of the serial port)

# Connect to a device
with Behavior(SERIAL_PORT) as device:
    # Set the camera framerate to 100 FPS
    device.write_camera0_frequency(100)

    # Start the camera trigger
    device.write_start_cameras(CameraOutputs.CAMERA_OUTPUT0)

    # Wait 3 seconds
    time.sleep(3)

    # Stop the camera trigger
    device.write_stop_cameras(CameraOutputs.CAMERA_OUTPUT0)
