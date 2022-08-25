from lcd import write_lcd, clear_lcd
import message
import cv2
import mediapipe as mp
import play_sound
import threading

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose

def safe_guard_sound_effect():
    play_sound.play_sound_effect(sound=play_sound.safe_guard)
    
cam = cv2.VideoCapture(0)
        
write_lcd(first_line='   SAFE-GUARD', second_line='   ACTIVATED')

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
            safe_guard_sound_thread = threading.Thread(target=safe_guard_sound_effect)
            safe_guard_sound_thread.start()
            write_lcd(first_line='     ALERT!', second_line='PERSON DETECTED!')
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
            
            cv2.imwrite('images/safe-guard.png', image)
            message.telegram(chat_id=message.telegram_chat_id, status='safe-guard mode')
            cam.release()
            break