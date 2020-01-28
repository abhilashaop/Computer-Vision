import cv2
import numpy as np
import datetime
img = cv2.imread('cat.jpg')
#img = np.zeros((500,500,3), np.uint8)
font = cv2.FONT_HERSHEY_SIMPLEX
# mouse call back function which responds when mouse event takes place
def click_event(events,x,y,flags,param):
	if events == cv2.EVENT_LBUTTONDOWN:
		#text = 'time' + str(datetime.datetime.now()) 
		#cv2.putText(img,text,(50,50),font,.5,(255,0,0),2)
		#cv2.imshow('img.png',img)
	#elif event == cv2.EVENT_LBUTTONUP:
		text2 = str(x) + ',' + str(y)	
		cv2.putText(img,text2,(x,y),font,.5,(255,0,0),2)
	cv2.imshow('image.png',img)

cv2.namedWindow('image.png')
cv2.setMouseCallback('image.png', click_event)
cv2.waitKey(0)
cv2.destroyAllWindows()
