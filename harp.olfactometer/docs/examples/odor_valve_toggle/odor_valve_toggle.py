import random
import time
from threading import Event, Thread

from harp.devices.olfactometer import Olfactometer, OlfactometerRegisters, Valves
from harp.protocol import OperationMode

# Serial port corresponding to the Harp Olfactometer
SERIAL_PORT = "COM93"  # or "ttyUSBx" in Linux ("x" is the number of the serial port)


# Print events that refer to the actual flows the Olfactometer reads for every channel
def print_events(device, stop_flag):
    while not stop_flag.is_set():
        for msg in device.get_events():
            if (
                msg.address == OlfactometerRegisters.CHANNEL0_ACTUAL_FLOW
                or msg.address == OlfactometerRegisters.CHANNEL1_ACTUAL_FLOW
                or msg.address == OlfactometerRegisters.CHANNEL2_ACTUAL_FLOW
                or msg.address == OlfactometerRegisters.CHANNEL3_ACTUAL_FLOW
                or msg.address == OlfactometerRegisters.CHANNEL4_ACTUAL_FLOW
            ):
                print(msg.address - OlfactometerRegisters.CHANNEL0_ACTUAL_FLOW)
                print(msg.payload)
                print()


with Olfactometer(SERIAL_PORT) as device:
    # Initialize event to be used in the events thread
    stop_flag = Event()

    # Set device to Active Mode to be able to read the device's events
    device.set_mode(OperationMode.ACTIVE)

    # Enable olfactometer flow
    device.write_enable_flow(True)

    # Initialize thread for events
    events_thread = Thread(
        target=print_events,
        args=(
            device,
            stop_flag,
        ),
    )
    events_thread.start()

    # Set valves to random flow values
    device.write_channel0_target_flow(random.random() * 100)
    device.write_channel1_target_flow(random.random() * 100)
    device.write_channel2_target_flow(random.random() * 100)
    device.write_channel3_target_flow(random.random() * 100)
    device.write_channel4_target_flow(random.random() * 100)

    # Open every odor valve, one at a time every 5 seconds
    device.write_valve_set(Valves.VALVE0)

    time.sleep(5)

    device.write_valve_clear(Valves.VALVE0)
    device.write_valve_set(Valves.VALVE1)

    time.sleep(5)

    device.write_valve_clear(Valves.VALVE1)
    device.write_valve_set(Valves.VALVE2)

    time.sleep(5)

    device.write_valve_clear(Valves.VALVE2)
    device.write_valve_set(Valves.VALVE3)

    time.sleep(5)

    device.write_valve_clear(Valves.VALVE3)

    time.sleep(5)

    # Disable flow
    device.write_enable_flow(False)

    time.sleep(1)

    # Stop reading events
    stop_flag.set()
    events_thread.join()
