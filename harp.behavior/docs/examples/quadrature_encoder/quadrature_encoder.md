# Quadrature Encoder

## Summary
This example demonstrates how to obtain the position values of a quadrature encoder using the [Harp Behavior](https://harp-tech.org/api/Harp.Behavior.html) board (see hardware schematics below).

This example was inspired by the one that exists in the [CF.Bonsai](https://fchampalimaud.github.io/cf.bonsai/workflows/HarpExamples/BehaviorBoard/QuadratureEncoder/QuadratureEncoder.html) website.

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
[](./quadrature_encoder.py)
```
<!--/codeinclude-->

!!! warning
    Don't forget to change the `SERIAL_PORT` to the one that corresponds to your device! The `SERIAL_PORT` must be denoted as `COMx` in Windows and `/dev/ttyUSBx` in Linux, where `x` is the number of the serial port.

## Schematics
The [Harp Behavior](https://harp-tech.org/api/Harp.Behavior.html) board can read the position value of one quadrature encoder connected to Port2. The encoder in the schematics is the [ENC1J-D28-L00128L](https://www.digikey.be/en/products/detail/bourns-inc/ENC1J-D28-L00128L/1089391).

![quadrature_encoder](./quadrature_encoder.svg)
