from gpiozero import Servo
from gpiozero.pins.pigpio import PiGPIOFactory    
import time

def set_angle(servo, angle):
    if angle >= 90:
        value = angle / 90 - 1
    elif angle < 90:
        value = - (1 - (angle/90))
    servo.value = value

factory = PiGPIOFactory()

servo = Servo(18, min_pulse_width=0.5/1000, max_pulse_width=2.5/1000, pin_factory=factory)

def look_left():
    set_angle(servo, angle = 145)
    
def look_right():
    set_angle(servo, angle = 35)
    
def look_straight():
    set_angle(servo, angle = 90)
    
# Servo test code
# look_left()
# time.sleep(1)
# look_straight()
# time.sleep(1)
# look_right()
# time.sleep(1)
# look_straight()