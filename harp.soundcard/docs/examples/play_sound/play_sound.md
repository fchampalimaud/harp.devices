# Play Sound

## Summary
This example demonstrates how to play a .wav file using the [Harp SoundCard](https://harp-tech.org/api/Harp.SoundCard.html) board (see hardware schematics below).

This example was inspired by the one that exists in the [CF.Bonsai](https://fchampalimaud.github.io/cf.bonsai/workflows/HarpExamples/SoundCard/PlaySound/PlaySound.html) website.

## Requirements
This example requires the `harp.soundcard` package to be installed. You can run one of the following commands to do so:
```
pip install harp.soundcard==0.1.0a2
# or (for uv users)
uv add "harp.soundcard==0.1.0a2"
```

## Code
<!--codeinclude-->
```python
[](./play_sound.py)
```
<!--/codeinclude-->

!!! warning
    Don't forget to change the `SERIAL_PORT` to the one that corresponds to your device! The `SERIAL_PORT` must be denoted as `COMx` in Windows and `/dev/ttyUSBx` in Linux, where `x` is the number of the serial port.

## Schematics
The [Harp SoundCard](https://harp-tech.org/api/Harp.SoundCard.html) board has 2 RCA ports (one for the left channel and the other for the right one) which allow the device to connect to a Harp Audio Amplifier on each side which, in turn, connect to a speaker.

!!! warning
    _Missing schematics!_
