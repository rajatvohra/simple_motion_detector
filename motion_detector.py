import cv2
import numpy as np

cap = cv2.VideoCapture('vtest.avi')


ret, frame1 =cap.read()
ret,frame2 =cap.read()

frame_width = int(cap.get(3)) 
frame_height = int(cap.get(4)) 
size = (frame_width, frame_height) 
result = cv2.VideoWriter('result_60_fps.avi',  cv2.VideoWriter_fourcc(*'MJPG'),  60, size) 

while cap.isOpened():
    if not ret:
        print("there seems to be a problem with the stream, Exiting......")
        break
    diff=cv2.absdiff(frame1,frame2)
    gray=cv2.cvtColor(diff,cv2.COLOR_BGR2GRAY)
    blur=cv2.GaussianBlur(gray,(7,7),0)
    thresh=cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
    dilated=cv2.dilate(thresh,(7,7),iterations=3)
    contours,_=cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    a=1
    for z in contours:
        x,y,w,h =cv2.boundingRect(z)
        if cv2.contourArea(z)>800 and cv2.contourArea(z)<44000:
            cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),3)
            cv2.putText(frame1,"Status:Movement detected",(10,20),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,0,255),1)

    #cv2.drawContours(frame1,contours,-1,(0,0,255),2)

    cv2.imshow("motion",frame1)
    result.write(frame1) 
    frame1=frame2
    ret,frame2=cap.read()
    if cv2.waitKey(25) & 0xFF == ord('q'):
      break



cv2.destroyAllWindows()
cap.release()
result.release()