import cv2
import numpy as np
import os
import time
from collections import defaultdict

#os.chdir("/home/pi/opencv-3.4.1/data/haarcascades")
recognizer = cv2.face.LBPHFaceRecognizer_create()
#recognizer.read('/home/pi/FaceRecognition/trainer/trainer.yml')
recognizer.read('/home/pi/Project_HomeSec/trainer1.yml')
faceCascade = cv2.CascadeClassifier('/home/pi/Project_HomeSec/haarcascade_frontalface_default.xml');

font = cv2.FONT_HERSHEY_SIMPLEX

#iniciate id counter
id = 0

#names related to ids: example ==> KUNAL: id=1,  etc
names = ['None', 'Timothy', 'Manoj', 'Bibek']
face_dict = defaultdict(int)
# Initialize and start realtime video capture
cam = cv2.VideoCapture(0)
cam.set(3, 640) # set video widht
cam.set(4, 480) # set video height

# Define min window size to be recognized as a face
minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)

t0 = time.time()
while True:
    ret, img =cam.read()
    #img = cv2.flip(img, -1) # Flip vertically
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor = 1.2,
        minNeighbors = 5,
        minSize = (int(minW), int(minH)),
       )

    for(x,y,w,h) in faces:
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
        id, confidence = recognizer.predict(gray[y:y+h,x:x+w])

        # Check if confidence is less them 100 ==> "0" is perfect match
        if (confidence < 75):
            id = names[id]
            confidence = "  {0}%".format(round(100 - confidence))
            face_dict[id] += 1
        else:
            id = "unknown"
            confidence = "  {0}%".format(round(100 - confidence))
            face_dict[id] += 1
        time.sleep(0.8)


        cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
        cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)

    cv2.imshow('camera',img)
    if(time.time() - t0) >= 20:
        os.system("echo " + "Timothy " + str(face_dict["Timothy"]) + " Manoj " + str(face_dict["Manoj"]) + " Bibek " + str(face_dict["Bereket"]) + " unknown " + str(face_dict["unknown"])) 
        break
    k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break

cam.release()
cv2.destroyAllWindows()
