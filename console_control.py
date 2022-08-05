from pynput import keyboard
from lcd import write_lcd, clear_lcd
from dc_motors import forward, backward, turn_left, turn_right, stop
import cv2

cam = cv2.VideoCapture(0)

def on_press(key):
    
    try:
        if key.char == 'w':
            forward()
            write_lcd(first_line=' MODE: CONSOLE', second_line=' Going forward')
        elif key.char == 's':
            backward()
            write_lcd(first_line=' MODE: CONSOLE', second_line=' Going backward')
        elif key.char == 'a':
            turn_left()
            write_lcd(first_line=' MODE: CONSOLE', second_line='  Turning left')
        elif key.char == 'd':
            turn_right()
            write_lcd(first_line=' MODE: CONSOLE', second_line=' Turning right')
        elif key.char == 'z':
            check, frame = cam.read()
            cv2.imshow('video', frame)
            cv2.waitKey(1)
            cv2.waitKey(1)
            write_lcd(first_line=' MODE: CONSOLE', second_line='Observing mode')
        
    except AttributeError:
        pass

def on_release(key):
    
    cam.release()
    cv2.destroyAllWindows()
    
    if key == keyboard.Key.esc:
        return False
    
    stop()
    
    write_lcd(first_line=' MODE: CONSOLE', second_line='     READY')
    
write_lcd(first_line=' MODE: CONSOLE', second_line='     READY')

with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

