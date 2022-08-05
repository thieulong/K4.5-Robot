from pynput import keyboard
from lcd import write_lcd, clear_lcd
from dc_motors import forward, backward, turn_left, turn_right, stop

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
        
    except AttributeError:
        pass

def on_release(key):
    
    if key == keyboard.Key.esc:
        return False
    
    stop()
    write_lcd(first_line=' MODE: CONSOLE', second_line='     READY')
    
write_lcd(first_line=' MODE: CONSOLE', second_line='     READY')
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
    
    