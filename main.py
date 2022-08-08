from pynput import keyboard
from lcd import write_lcd, clear_lcd
import subprocess

def on_release(key):
    
    if key.char == 'f':
        print("Y Button pressed")
        write_lcd(first_line='SELECT MODE:', second_line=' ANTI-COLLISION')
        
    if key.char == 'g':
        print("X Button pressed")
        write_lcd(first_line='SELECT MODE:', second_line=' MANUAL CONTROL')
        import console_control
        
    if key.char == 'h':
        print("B Button pressed")
        write_lcd(first_line='SELECT MODE:', second_line=' VOICE COMMANDS')
        
    if key.char == 'j':
        print("A Button pressed")
        write_lcd(first_line='SELECT MODE:', second_line='   FOLLOW-ME')

    if key.char == 'z':
        write_lcd(first_line='SELECT MODE:', second_line='NO MODE SELECTED')
        
with keyboard.Listener(
        on_release=on_release) as listener:
    listener.join()