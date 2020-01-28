import numpy as np
import cv2 as cv

vid = cv.VideoCapture(0)

_,frame = cv.imread()
_,frame3 = cv.imread()

while vid.isOpened():
    diff = cv.absdiff(frame,frame3)
    gray  = cv.cvtColor(diff,cv.COLOR_BGR2GRAY)
    blur = cv.GaussianBlur(gray, (5,5), 0)
    _,thresh = cv.threshold(blur,100,255,cv.THRESH_BINARY)
    dil = cv.dilate(thresh, None, iterations=3)
    _,contours = cv.findContours(dil, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    for contour in contours:
         (x,y,w,h) = cv.boundingRect(contours)
         if cv.ContourArea < 900:
             continue
         cv.rectangle(frame,(x,y), (x+w, y+h), (50,50,50), 2)
    cv.drawContours(frame, contours, -1, (90,90,90), 3 )
    cv.imshow('frame',frame)
    frame = frame3
    frame3 = vid.read()
    if  cv.waitKey(0) == 27:
        break
cv.destroyAllWindows()    
 
