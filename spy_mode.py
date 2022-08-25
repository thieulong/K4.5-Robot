from pynput import keyboard
from lcd import write_lcd, clear_lcd
from dc_motors import forward, backward, turn_left, turn_right, stop
import cv2
import threading
import os

cam = cv2.VideoCapture(0)

def camera():

    while(True):
        
        ret, frame = cam.read()

        cv2.imshow('frame', frame)

        cv2.waitKey(1)
    
camera_thread = threading.Thread(target=camera)
camera_thread.start()


def on_press(key):
    
    try:
        if key.char == 'w':
            forward()
        elif key.char == 's':
            backward()
        elif key.char == 'a':
            turn_left()
        elif key.char == 'd':
            turn_right()
        
    except AttributeError:
        pass

def on_release(key):
    
    try:
        if key.char == 'w':
            stop()
        elif key.char == 's':
            stop()
        elif key.char == 'a':
            stop()
        elif key.char == 'd':
            stop()
            
    except AttributeError:
        cam.release()
        cv2.destroyAllWindows()
        os.system('python3 ~/RPI-Project-Rover/main.py')
        
        
write_lcd(first_line='    SPY MODE', second_line='     READY')

with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
    camera_thread.join()
