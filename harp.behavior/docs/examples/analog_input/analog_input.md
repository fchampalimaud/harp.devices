# Analog Input

## Summary
This example demonstrates how to read analog input values from a potentiometer using the [Harp Behavior](https://harp-tech.org/api/Harp.Behavior.html) board (see hardware schematics below).

This example was inspired by the one that exists in the [CF.Bonsai](https://fchampalimaud.github.io/cf.bonsai/workflows/HarpExamples/BehaviorBoard/AnalogInput/AnalogInput.html) website.

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
[](./analog_input.py)
```
<!--/codeinclude-->

!!! warning
    Don't forget to change the `SERIAL_PORT` to the one that corresponds to your device! The `SERIAL_PORT` must be denoted as `COMx` in Windows and `/dev/ttyUSBx` in Linux, where `x` is the number of the serial port.

## Schematics
The [Harp Behavior](https://harp-tech.org/api/Harp.Behavior.html) board has two analog input channels: AD0 and AD1. The maximum voltage allowed is 5V. In this example, the board receives an analog input signal from a potentiometer connected to AD0.

![analog_input](./analog_input.svg)
    