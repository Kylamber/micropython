class Servo:
  def __init__(self, servo):
    """
    Initialize the servo.
    
    Args:
    -> servo: a PWM object of the servo
    """
    
    self._servo = servo
    self._servo.freq(50) # setting the frequency to 50 Hz to match the servo
    self.set_angle(0) # comment if you don't want to set the angle to 0 every init, might lead to some issues in my experience.
    
  
  def set_angle(self, angle):
    """
    Set the angle of the servo.
    """
    
    duty = int(341/1200 * angle + 3069/40) # since the duty can only be integers, int is used.
    self._servo.duty(duty)
