from dc_motors import forward, backward, stop, turn_left, turn_right
from servo import look_left, look_right, look_straight
from distance import get_distance
from lcd import write_lcd, clear_lcd
import time

write_lcd(first_line=' ANTI-COLLISION', second_line='     READY')
    
while True:
    front_distance = get_distance()
    print("Front distance: {}".format(front_distance))
    if front_distance <= 20:
        backward()
        time.sleep(0.5)
        stop()
        # Look on the left side and measure distance
        look_left()
        time.sleep(1)
        
        left_distance = get_distance()
        print("Left distance: {}".format(left_distance))
        # Look on the right side and measure distance
        look_right()
        time.sleep(1)
        right_distance = get_distance()
        print("Right distance: {}".format(right_distance))
        if left_distance > right_distance:
            look_left()
            turn_left()
            time.sleep(1)
        elif right_distance > left_distance:
            turn_right()
            time.sleep(1)
        look_straight()
        time.sleep(0.5)
    elif front_distance > 20:
        look_straight()
        forward()
    time.sleep(0.2)
        

