import numpy as np
import cv2 as cv

img = cv.imread('cat.jpg')
img3 = cv.imread('cat.jpg',0)

_,thresh = cv.threshold(img3, 199,255, cv.THRESH_BINARY)
contours,_  =  cv.findcontours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
for contour in contours:
    # now we'll use the approxPolyDP method which approximates a polynomial curve with some precission
    approx = cv.approxPolyDP(contour,0.01*arcLength(contour,True),True )
    # episolon is the parameter specifieying the approximation accuracy
    # and the arcLength gives the contours parameter or the curve's length
    # The first parameters of the arcLength is the image of which we have to find the arclength of and the second one is a boolean value 
    #which is false if the shapes are open shapes and true if the shapes are closed 
    cv.drawContours(img, [approx], 0, (90,90,90), 3)
    x = approx.ravel()[0]
    y = approx.ravel()[1]
    if len(approx) == 3:
        putText(img, "Traingle",(x,y),cv.FONT_HERSHEY_COMPLEX, (0,0,0), 3)
    elif len(approx) == 4:
        putText(img, "Traingle",(x,y),cv.FONT_HERSHEY_COMPLEX, (0,0,0), 3)
    elif len(approx) == 5:
        putText(img, "Pentagon",(x,y),cv.FONT_HERSHEY_COMPLEX, (0,0,0), 3)
    elif len(approx) == 6:
        putText(img, "hexagon",(x,y),cv.FONT_HERSHEY_COMPLEX, (0,0,0), 3)
    else:
        putText(img, "circle",(x,y),cv.FONT_HERSHEY_COMPLEX, (0,0,0), 3)

cv.imshow('img',img)
cv,waitKey(0)
cv.destroyAllWindows()
