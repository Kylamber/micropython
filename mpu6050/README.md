# MPU6050 

This library is using the translated version from rfetick's MPU6050_light library, https://github.com/rfetick/MPU6050_light, and adamjezek98's MPU6050 code https://github.com/adamjezek98/MPU6050-ESP8266-MicroPython. Tested working on an ESP32 with Micropython firmware.

## Usage

```python
# Connecting to the I2C of the MPU6050.
i2c = I2C(scl=Pin(22), sda=Pin(21))
mpu = mpu6050(i2c)

# Calculating the offsets, True for gyro and True for accelerometer.
mpu.calcOffsets(1, 1)
time.sleep(1)

# Get the angles, returns a json with keys "x", "y", "z".
mpu.getAngles()

# Or if preferred, getting the raw values, returns a json with keys "AcX", "AcY", "AcZ", "Tmp", "GyX", "GyY", "GyZ".
mpu.getRawData()

# When looping the program, don't forget to update the values.
while True:
  mpu.update()
```

## Results
Using this library and getting the data to Godot, I managed to make this.
![Result](https://github.com/Kylamber/micropython/raw/main/mpu6050/IMG_0437.gif)

## Problems

The I2C connection and calibration code hasn't been tested yet. I do not know if that is the right code to do it. Feel free to correct the code.
