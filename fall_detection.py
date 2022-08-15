import cv2
import mediapipe as mp
import time
import threading
import numpy as np
from sklearn.linear_model import LinearRegression
import dc_motors
import play_sound

dc_motors.pl.ChangeDutyCycle(70)
dc_motors.pr.ChangeDutyCycle(70)

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose

model = LinearRegression()

cam = cv2.VideoCapture(0)

starting_time = time.time()
frame_id = 0

y_head_coords = []
label = "" 

def fall_detect_sound_effect():
    play_sound.play_sound_effect(sound=play_sound.fall_detect)

def fall_detect(y_head_coords):
    global label
    if all(i>0 for i in y_head_coords):
        x = np.array(range(0,len(y_head_coords))).reshape((-1,1))
        y = np.array(y_head_coords)

        model.fit(x, y)

        if model.coef_[0] > 25:
            label = "Fall Detected!"
            fall_detect_thread = threading.Thread(target=fall_detect_sound_effect)
            fall_detect_thread.start()
        else:
            label = ""
        
with mp_pose.Pose(
min_detection_confidence=0.8,
min_tracking_confidence=0.8) as pose:

    while cam.isOpened():
        success, image = cam.read()
        image_height, image_width, _ = image.shape

        border_left = int((image_width/2) - ((image_width/2)/2) + (((image_width/2)/2)/2))
        border_right = int((image_width/2) + ((image_width/2)/2) - (((image_width/2)/2)/2))

        frame_id += 1

        if not success:
            continue

        image.flags.writeable = False
        
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        results = pose.process(image)

        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        
        if results.pose_landmarks:
            x_cordinate = list()
            y_cordinate = list()
            for id, lm in enumerate(results.pose_landmarks.landmark):
                h, w, c = image.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                x_cordinate.append(cx)
                y_cordinate.append(cy)

            width = max(x_cordinate) - min(x_cordinate)
            height = max(y_cordinate) - min(y_cordinate)

            x_head = results.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].x * image_width
            if x_head < border_right and x_head > border_left:
                y_head = results.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].y * image_height
                y_head_coords.append(y_head)
                if len(y_head_coords) == 5:
                    thread = threading.Thread(target=fall_detect, args=(y_head_coords, ))
                    thread.start()
                    y_head_coords = []

                if width > height:
                    cv2.rectangle(img=image,
                                pt1=(min(x_cordinate), max(y_cordinate)),
                                pt2 =(max(x_cordinate), min(y_cordinate)-25),
                                color=(0,0,255),
                                thickness=1)

                else:
                    cv2.rectangle(img=image,
                                pt1=(min(x_cordinate), max(y_cordinate)),
                                pt2=(max(x_cordinate), min(y_cordinate)-25),
                                color=(0,255,0),
                                thickness=1)

            if x_head > border_right:
                dc_motors.turn_right()
            
            if x_head < border_left:
                dc_motors.turn_left()

        cv2.putText(img=image,
                    text=label,
                    org=(10,70),
                    fontFace=cv2.FONT_HERSHEY_COMPLEX,
                    fontScale=1,
                    color=(0,0,255),
                    thickness=1)

        elapsed_time = time.time() - starting_time
        fps = frame_id / elapsed_time
        cv2.putText(image, "FPS: " + str(round(fps, 2)), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)
        cv2.imshow("Camera", image)
        cv2.waitKey(1)
