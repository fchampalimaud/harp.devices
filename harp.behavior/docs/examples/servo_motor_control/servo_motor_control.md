# Servo Motor Control

## Summary
This example demonstrates how to control a servo motor using the [Harp Behavior](https://harp-tech.org/api/Harp.Behavior.html) board (see hardware schematics below).

This example was inspired by the one that exists in the [CF.Bonsai](https://fchampalimaud.github.io/cf.bonsai/workflows/HarpExamples/BehaviorBoard/ServoMotorControl/ServoMotorControl.html) website.

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
[](./servo_motor_control.py)
```
<!--/codeinclude-->

!!! warning
    Don't forget to change the `SERIAL_PORT` to the one that corresponds to your device! The `SERIAL_PORT` must be denoted as `COMx` in Windows and `/dev/ttyUSBx` in Linux, where `x` is the number of the serial port.

## Schematics
The [Harp Behavior](https://harp-tech.org/api/Harp.Behavior.html) board can control two servo motors in ports DO2 and DO3. The DOs output voltage is 5V. In this example, the board controls controls the position of a servo motor connected to DO2.

![servo_motor_control](./servo_motor_control.svg)
