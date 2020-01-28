import numpy as np
import cv2 as cv

# hough transform is a popular technique to detect any shape if you can represent that shape in a mathematical form. 
# It can detect the shape even if thr image is broken or distorted .
#steps of hough transform are:
# a. edge detection using canny mehtod
# b. mapping of edge points and storing it in an accumulator 
# c. Interpretation of the accumulator to yeild lines of infinite length, it is done by thresholding or other methods.
# d. conversion of infinite lines into finite lines
img = cv.imread('sudoko.png',0)
edges = cv.Canny(img,50,99,apertureSize=3)
#lines = cv.HoughLines(image,rho,theta,threshold)
lines = cv.HoughLinesP(edges, 1, np.pi/180, 200, minLineLength=100, maxLineGap=10)

for l in lines:
    x1,y1,x2,y2 = l[0]
    cv.drawline(img,(x1,y1), (x2,y2), (90,90,90), 2)
cv.imshow('image', img)
cv.waitKey(0)
cv.destroyAllWindows()



