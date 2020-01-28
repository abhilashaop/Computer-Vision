# We here are going to learn the concept of contours. So, the steps for doing soare mentioned below:
# s1: read a image in gray scale format 
# S2: get the thresholded image using the cv2.thresholad function
# S3: Then, find the contours of the image using the cv2.findContours method
# S4: Aftert finding the contours , draw the contours in the original image
# S5: Display the image
# contours is the curve(s) joining all teh continuos points (along the boundary)
import numpy as np
import cv2 as cv

img = cv.imread('balls.jpg')
img3 = cv.imread('balls.jpg',0)

ret,thresh = cv.threshold(img3,100,255,0)

contours,heirarchy = cv.findContours(thresh,cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

# Here, Contours is a list of all the countours in the image. Each indivisual contour is  a  numpy array of (x,y coordinates of boundary points of the object.
# The syntax and the parameters to be passed in the function are :
# contours,heirarchy = cv2.findContours(image, mode, method[contours[heirarchy[offset]]])
# let's display the number of the coordinates

print("no. of contours =" +str(len(contours)))

# Drawing the contours

cv.drawContours(img,contours,-1,(200,50,0),2)
cv.imshow('contours',img)
cv.imshow('gray-scale',img3)
cv.waitKey(0)
