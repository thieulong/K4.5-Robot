import serial
from pynput import keyboard
from dc_motors import forward, backward, turn_left, turn_right, stop
from lcd import write_lcd
import os

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
ser.reset_input_buffer()

# while True:
#     ser.write(b'stop\n')
#     command = ser.readline().decode('utf-8').rstrip()
#     print(command)
#     time.sleep(1)
#     ser.write(b'stop\n')
    
    
    
    
def on_press(key):
    
    try:
        if key.char == 'w':
            forward()
            ser.write(b'forward\n')
        elif key.char == 's':
            backward()
            ser.write(b'backward\n')
        elif key.char == 'a':
            turn_left()
            ser.write(b'left\n')
        elif key.char == 'd':
            turn_right()
            ser.write(b'right\n')
        
    except AttributeError:
        pass

def on_release(key):

    try:
        if key.char == 'w':
            ser.write(b'stop\n')
            stop()
        elif key.char == 's':
            ser.write(b'stop\n')
            stop()
        elif key.char == 'a':
            ser.write(b'stop\n')
            stop()
        elif key.char == 'd':
            ser.write(b'stop\n')
            stop()
            
    except AttributeError:
        os.system('python3 ~/RPI-Project-Rover/main.py')
        
write_lcd(first_line='  SYNC CONTROL', second_line='     READY')

with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
