import cv2
import mediapipe as mp
import dc_motors
from lcd import write_lcd, clear_lcd

write_lcd(first_line=' FOLLOW-ME MODE', second_line='    ATIVATED')

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_pose = mp.solutions.pose

cam = cv2.VideoCapture(0)


def look_left():
    dc_motors.pl.ChangeDutyCycle(25)
    dc_motors.pr.ChangeDutyCycle(25)
    dc_motors.turn_left()
    
def look_right():
    dc_motors.pl.ChangeDutyCycle(25)
    dc_motors.pr.ChangeDutyCycle(25)
    dc_motors.turn_right()

def follow():
    dc_motors.pl.ChangeDutyCycle(80)
    dc_motors.pr.ChangeDutyCycle(80)
    dc_motors.forward()

with mp_pose.Pose(
min_detection_confidence=0.8,
min_tracking_confidence=0.8) as pose:

    while cam.isOpened():
        success, image = cam.read()
        image_height, image_width, _ = image.shape
        
        print(image_width)

        border_left = int((image_width/2) - ((image_width/2)/2) + (((image_width/2)/2)/2))
        border_right = int((image_width/2) + ((image_width/2)/2) - (((image_width/2)/2)/2))

        if not success:
            continue

        image.flags.writeable = False
        
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        results = pose.process(image)

        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        
        if results.pose_landmarks:
            x_coordinate = list()
            y_coordinate = list()
            for id, lm in enumerate(results.pose_landmarks.landmark):
                h, w, c = image.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                x_coordinate.append(cx)
                y_coordinate.append(cy)
                
            left_shoulder = results.pose_landmarks.landmark[11].x * image_width
            right_shoulder = results.pose_landmarks.landmark[12].x * image_width
            center = (right_shoulder + left_shoulder) / 2
            
            cv2.circle(img=image, 
                       center=(int(center),320),
                       radius=3,
                       color=(0,0,255),
                       thickness=-1)

            if center < border_right and center > border_left:
                dc_motors.stop()
                if results.pose_landmarks.landmark[15].y * image_height < results.pose_landmarks.landmark[13].y * image_height:
                    follow()
                    
            if center > border_right:
                look_right()
            
            if center < border_left:
                look_left()

        cv2.imshow("Camera", image)
        cv2.waitKey(1)
