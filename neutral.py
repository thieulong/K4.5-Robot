import dc_motors
from servo import look_left, look_right, look_straight
from distance import get_distance
from lcd import write_lcd, clear_lcd
import RPi.GPIO as GPIO  
from time import sleep

GPIO.cleanup()


