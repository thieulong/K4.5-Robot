import cv2

cap = cv2.VideoCapture(0) 
ret,frame = cap.read()

cv2.imwrite('images/photo.png',frame)
cap.release()