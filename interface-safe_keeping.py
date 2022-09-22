from lcd import write_lcd, clear_lcd
import message
import cv2
import mediapipe as mp
import play_sound
import threading
from sys import exit

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose

def safe_keeping_sound_effect():
    play_sound.play_sound_effect(sound=play_sound.safe_keeping)

cam = cv2.VideoCapture(0)
        
write_lcd(first_line='  SAFE-KEEPING', second_line='   ACTIVATED')
        
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
            safe_keeping_sound_thread = threading.Thread(target=safe_keeping_sound_effect)
            safe_keeping_sound_thread.start()
            write_lcd(first_line='     ALERT!', second_line='  PERSON LEFT!')
            cv2.imwrite('images/safe-keeping.png', image)
            message.telegram(chat_id=message.telegram_chat_id, status='safe-keeping mode')
            cam.release()
            exit()