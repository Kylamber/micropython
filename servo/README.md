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

## Explanations
### set_angle(angle)
The servo is controlled using PWM and it is said that the PWM is using a 20 ms period or 50 Hz frequency (T = 1/f). (read more: https://en.wikipedia.org/wiki/Servo_control)

Pulse widths and its corresponding angles:
- 1 ms   = -90 deg
- 1.5 ms = 0 deg
- 2 ms   = 90 deg

The duty method in PWM sets the ratio of the argument to 1023, e.g. PWM.duty(512) is 512/1023 which is roughly 50%. Since 1 ms in 20 ms period is 1/20 or 5% of the period, the duty is (1023 * 1/20). For 2 ms in 20 ms period is 2/20 or 10% of the period, the duty is (1023 * 2/20). (read more: https://docs.micropython.org/en/latest/esp32/quickref.html#pwm-pulse-width-modulation)

Assuming it's linear, the line equation given that -90 corresponds with a duty of 1023/20 and 90 degrees corresponds with a duty of 1023*2/20 is

`duty = 341/1200 * angle + 3069/40`

## Problems

Theoritically it should work wonderfully, but in my case the servo kinda only rotated 45 degrees when I inputted 90. After experimenting, the 90 lies in 150 and -90 in -180 for some reason. Also, the servo can go over the 180 degrees limit which makes them stutter, I kinda think that is a bad thing so move it back to 0 degrees immediately or cut off the power.
