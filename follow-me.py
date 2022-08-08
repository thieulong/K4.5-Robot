from lcd import write_lcd, clear_lcd
import dc_motors
import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose

dc_motors.pl.ChangeDutyCycle(80)
dc_motors.pr.ChangeDutyCycle(80
                             )

cam = cv2.VideoCapture(0)

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
        
        cv2.line(img = image, 
                 pt1 = (int(image_width/2), 0),
                 pt2 = (int(image_width/2), image_height),
                 color = (0, 255, 0),
                 thickness = 2)

        mp_drawing.draw_landmarks(
            image,
            results.pose_landmarks,
            mp_pose.POSE_CONNECTIONS,
            landmark_drawing_spec=mp_drawing_styles.get_default_pose_landmarks_style())

        if results.pose_landmarks:
            
            x_center = results.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].x * image_width
            y_center = results.pose_landmarks.landmark[mp_pose.PoseLandmark.NOSE].y * image_height

            if x_center > (image_width/2) + ((image_width/2)/2):
                dc_motors.turn_right()
            
            if x_center < (image_width/2) - ((image_width/2)/2):
                dc_motors.turn_left()
            
            if x_center < (image_width/2) + ((image_width/2)/2) and x_center > (image_width/2) - ((image_width/2)/2):
                dc_motors.stop()
            
        cv2.imshow('Camera', cv2.flip(image, 1))
        if cv2.waitKey(5) & 0xFF == 27:
            break
      
    cam.release()