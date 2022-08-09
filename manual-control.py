from pynput import keyboard
from lcd import write_lcd, clear_lcd
from dc_motors import forward, backward, turn_left, turn_right, stop
import message
import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose



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
  
    cv2.destroyAllWindows()
    
    if key == keyboard.Key.esc:
        
        cam = cv2.VideoCapture(0)
        
        write_lcd(first_line='SAFE-KEEPER MODE', second_line='   ACTIVATED')
        
        with mp_pose.Pose(
            min_detection_confidence=0.8,
            min_tracking_confidence=0.8) as pose:
        
            while cam.isOpened():
                success, image = cam.read()
                image_height, image_width, _ = image.shape
            
                if not success:
                    continue

                image.flags.writeable = False
                
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    
                results = pose.process(image)

                image.flags.writeable = True
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
                
                if not results.pose_landmarks:
                    write_lcd(first_line='    ALERT!', second_line='  PERSON LEFT!')
                    cv2.imwrite('detection/safe-keeping.png', image)
                    message.telegram(chat_id=message.telegram_chat_id, status='safe-keeping mode')
                    cam.release()
                    break
    
    
    if key == keyboard.Key.enter:
        
        cam = cv2.VideoCapture(0)
        
        write_lcd(first_line='SAFE-GUARD MODE', second_line='   ACTIVATED')
        
        with mp_pose.Pose(
            min_detection_confidence=0.8,
            min_tracking_confidence=0.8) as pose:
        
            while cam.isOpened():
                success, image = cam.read()
                image_height, image_width, _ = image.shape
            
                if not success:
                    continue

                image.flags.writeable = False
                
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    
                results = pose.process(image)

                image.flags.writeable = True
                image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
                
                if results.pose_landmarks:
                    write_lcd(first_line='    ALERT!', second_line='PERSON DETECTED!')
                    x_cordinate = list()
                    y_cordinate = list()
                    for id, lm in enumerate(results.pose_landmarks.landmark):
                        h, w, c = image.shape
                        cx, cy = int(lm.x * w), int(lm.y * h)
                        x_cordinate.append(cx)
                        y_cordinate.append(cy)
                        
                    cv2.rectangle(img= image,
                                pt1= (min(x_cordinate), max(y_cordinate)),
                                pt2 = (max(x_cordinate), min(y_cordinate)-20),
                                color= (0,0,255),
                                thickness= 1)
                    
                    cv2.imwrite('detection/safe-guard.png', image)
                    message.telegram(chat_id=message.telegram_chat_id, status='safe-guard mode')
                    cam.release()
                    break
    
    stop()
    
    write_lcd(first_line=' MODE: CONSOLE', second_line='     READY')
    
write_lcd(first_line=' MODE: CONSOLE', second_line='     READY')

with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

