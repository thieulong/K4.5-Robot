from pynput import keyboard
from lcd import write_lcd, clear_lcd
import os
import RPi.GPIO as GPIO  

def on_release(key):
    
    if key.char == 'f':
        print("Y Button pressed")
        write_lcd(first_line='SELECT MODE:', second_line=' ANTI-COLLISION')
        os.system('python3 ~/RPI-Project-Rover/anti_collision.py')
        
    if key.charh == 'g':
        print("X Button pressed")
        write_lcd(first_line='SELECT MODE:', second_line=' MANUAL CONTROL')
        os.system('python3 ~/RPI-Project-Rover/manual_control.py')
        
    if key.char == 'h':
        print("B Button pressed")
        write_lcd(first_line='SELECT MODE:', second_line=' VOICE COMMANDS')
        os.system('python3 ~/RPI-Project-Rover/voice_commands.py')
    if key.char == 'j':
        print("A Button pressed")
        write_lcd(first_line='SELECT MODE:', second_line='   FOLLOW-ME')

    if KeyboardInterrupt:
        write_lcd(first_line='SELECT MODE:', second_line='NO MODE SELECTED')
        GPIO.cleanup()
        os.system('python3 ~/RPI-Project-Rover/neutral.py')
        os.system('python3 ~/RPI-Project-Rover/main.py')
        
    if AttributeError:
        write_lcd(first_line='SELECT MODE:', second_line='NO MODE SELECTED')
        GPIO.cleanup()
        os.system('python3 ~/RPI-Project-Rover/neutral.py')
        os.system('python3 ~/RPI-Project-Rover/main.py')
        
with keyboard.Listener(
        on_release=on_release) as listener:
    listener.join()