# This is a program to display an image on which i have drawn some figures and also  added some functionalities like if we press s,ecs,t,h then it will save , close , show time and show dimension of the image respectively.
import cv2
import numpy as np
import datetime
img = cv2.imread('cat.jpg')
a,b,c  = np.shape(img)
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img,'save-s,quit-esc,time-t,shape-p',(500,550),font,3,(50,50,50),5,cv2.LINE_AA)
ttext = "time:" +str(datetime.datetime.now())
while True:
cv2.imshow('savedimg.jpg',img)
k = cv2.waitKey(0)

    if k == 27:
        break
    elif k == ord('s'):
	cv2.imwrite('savedimg.jpg', img)
    elif k == ord('l'):
	img = cv2.rectangle(img,(0,0), (54,90) , (200,0,0) , 2)
	img = cv2.circle(img, (250,250),200,(20,50,52) , 2)
    elif k == ord('t'):
	img  =cv2.putText(img,a,(0,0),font,2,(0,0,0),3)
	img  =cv2.putText(img,b,(10,0),font,2,(0,0,0),3)

    elif k == ord('d'):
	img = cv2.putText(img,hw,(250,0),font,3,(0,0,0),3)
#cv2.destroyAllWindows()
    
    #if k ==
