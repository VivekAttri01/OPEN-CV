import numpy as np
import cv2
cap=cv2.VideoCapture(0)
face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades +'haarcascade_frontalface_default.xml')
eye_cascade=cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
while True:
    ret, frame = cap.read()
    grey=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces=face_cascade.detectMultiScale(grey,1.3,5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),5)
        roigrey=grey[y:y+h,x:x+w]
        roicolor=frame[y:y+h,x:x+w]
        eyes=eye_cascade.detectMultiScale(roigrey,1.3,4)
        for (ex,ey,ew,eh) in eyes:
            cv2.rectangle(roicolor,(ex,ey),(ex+ew,ey+eh),(0,255,0),4)

    cv2.imshow('frame', frame)
    if cv2.waitKey(1)== ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
