import cv2
import time

cap = cv2.VideoCapture(0) 
ret,frame = cap.read()
cv2.waitKey(delay=1000)
cv2.imwrite('images/photo.png',frame)
cap.release()