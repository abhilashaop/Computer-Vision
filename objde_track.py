import numpy as np
import cv2
#w2@
def nothing(x):
    print(x)

cv2.namedWindow('track')
cv2.createTrackbar("LH","track",0,255,nothing)
cv2.createTrackbar("LS","track",0,255,nothing)
cv2.createTrackbar("LV","track",0,255,nothing)
cv2.createTrackbar("UH","track",255,255,nothing)
cv2.createTrackbar("US","track",255,255,nothing)
cv2.createTrackbar("UV","track",255,255,nothing)
while True:
    img = cv2.imread('cat.jpg')
    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    
    l_h = cv2.getTrackbarPos("LH" , "track")
    l_s = cv2.getTrackbarPos("LS" , "track")
    l_v = cv2.getTrackbarPos("LV" , "track")
    u_h = cv2.getTrackbarPos("UH" , "track")
    u_s = cv2.getTrackbarPos("US" , "track")
    u_v = cv2.getTrackbarPos("UV" , "track")
    
    l_b = np.array([l_h, l_s, l_v])
    u_b = np.array([u_h, u_s, u_v])
    
    mask = cv2.inRange(hsv,l_b,u_b)
    
    res =  cv2.bitwise_and(img,img,mask=mask)

cv2.imshow('track',res)
cv2.waitKey(27) 
cv2.destroyAllWindows()
