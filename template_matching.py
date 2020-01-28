# template matching is the method of searching and locating an template in a large image 
# the method used for template matching is called matchtemplate
import numpy as np 
import cv2 as cv

img = cv.imread('cat.jpg')
img3 = cv.imread('cat.jpng',0)
# load the template
temp = img[300:440,200:300]
temp3 = cv.cvtColor(temp,cv.COLOR_BGR2GRAY)
w,h = temp3.shape[::-1]
# res = cv.matchTemplate(large_image, template, meth d,result=None,mask=None)
res = cv.matchTemplate(img, temp3, cv.TM_CCOEFF_NORMED)
# res is the array ,in which there are some values which are equal to 1, these are the points which are the brigtest and match the template and the image .So, obviously we are only interested in those points and threrefore we need to filter them out of the result . Foir that we use
#the where method of numpy to do so

threshold = 0.8;
loc = np.where(res >= threshold)
print(loc)
for i in zip(*loc[::-1]):
    cv.rectangle(img, pt, (pt[0]+w, p[1]+h), (0,0,255), 2)
cv.imshow('original Image', img)
cv.waitKey(0)
