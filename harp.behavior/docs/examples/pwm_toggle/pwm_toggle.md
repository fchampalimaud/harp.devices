# PWM Toggle

## Summary
This example demonstrates how to control a PWM signal to drive the brightness of a LED using the [Harp Behavior](https://harp-tech.org/api/Harp.Behavior.html) board (see hardware schematics below).

This example was inspired by the one that exists in the [CF.Bonsai](https://fchampalimaud.github.io/cf.bonsai/workflows/HarpExamples/BehaviorBoard/PWMToggle/PWMToggle.html) website.

## Requirements
This example requires the `harp.behavior` package to be installed. You can run one of the following commands to do so:
```
pip install harp.behavior==0.1.0a2
# or (for uv users)
uv add "harp.behavior==0.1.0a2"
```

## Code
<!--codeinclude-->
```python
[](./pwm_toggle.py)
```
<!--/codeinclude-->

!!! warning
    Don't forget to change the `SERIAL_PORT` to the one that corresponds to your device! The `SERIAL_PORT` must be denoted as `COMx` in Windows and `/dev/ttyUSBx` in Linux, where `x` is the number of the serial port.

## Schematics
The [Harp Behavior](https://harp-tech.org/api/Harp.Behavior.html) board can control four PWM sources in ports: DO0, DO1, DO2 and DO3. The DOs output voltage is 5V. In this example, the board controls the brightness of a LED connected to DO0. A resistor of $200\Omega$ is used to drop the current passing through the LED and prevent it from burning.

![pwm_toggle](./pwm_toggle.svg)
