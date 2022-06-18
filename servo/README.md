# Servo 

This is a library for controlling servo using Micropython. Tested working on ESP32 with Micropython v1.19 (Micropython 1.18 can't use PWM with frequencies lower than 611 Hz, be mindful of that because I got stuck searching for days on why this didn't work).

## Usage

```python
from machine import Pin, PWM
from Servo import Servo

# Create the Servo object
servo = Servo(PWM(Pin(13), freq=50)) # the frequency of 50 Hz is the default for servos.

# Set the angle
servo.set_angle(90)
```

## Problems

Theoritically it should work wonderfully, but in my case the servo kinda only rotated 45 degrees when I inputted 90. After experimenting, the 90 lies in 150 and -90 in -180 for some reason. Also, the servo can go over the 180 degrees limit which makes them stutter, I kinda think that is a bad thing so move it back to 0 degrees immediately or cut off the power.
