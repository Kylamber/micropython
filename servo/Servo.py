class Servo:
  def __init__(self, servo):
    """
    Args:
    -> servo: a PWM object of the servo
    """
    
    self.servo = servo
    self.servo.freq(50) # setting the frequency to 50 Hz to match the servo
    # self.set_angle(0) # uncomment if you want to set the angle to 0 every initialization
    
  
  def set_angle(self, angle):
    """
    The servo is controlled using PWM and from here
    https://en.wikipedia.org/wiki/Servo_control
    it is said that the PWM is using a 20 ms period or 50 Hz frequency (T = 1/f).
    
    Pulse widths and its corresponding angles 
    - 1 ms   = -90 deg
    - 1.5 ms = 0 deg
    - 2 ms   = 90 deg
    
    The duty method in PWM sets the ratio of the argument to 1023, e.g. PWM.duty(512)
    is 512/1023 which is roughly 50%. Since 1 ms in 20 ms period is 1/20 or 5% of the
    period, the duty is (1023 * 1/20). For 2 ms in 20 ms period is 2/20 or 10% of the
    period, the duty is (1023 * 2/20). (read more: 
    https://docs.micropython.org/en/latest/esp32/quickref.html#pwm-pulse-width-modulation)
    
    Assuming it's linear, the line equation given that -90 corresponds with a duty 
    of 1023/20 and 90 corresponds with a duty of 1023*2/20 is
    duty = 341/1200 * angle + 3069/40
    """
    
    duty = int(341/1200 * angle + 3069/40) # since the duty can only be integers, int is used.
    self.servo.duty(duty)
