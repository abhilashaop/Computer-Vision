import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv
 
img = cv.imread('cat.jpg',0)

_,mask = cv.threshold(img,60,255,cv.THRESH_BINARY)
 
kernal = np.ones((5,5), np.uint8)

dilation = cv.dilate(mask,kernal,iterations=2)
erosion = cv.erode(mask,kernal,iterations=2)
opening = cv.morphologyEx(mask,cv.MORPH_OPEN,kernal)
closing = cv.morphologyEx(mask,cv.MORPH_CLOSE,kernal)
mor_gradient = cv.morphologyEx(mask,cv.MORPH_GRADIENT,kernal)
top_hat = cv.morphologyEx(mask,cv.MORPH_TOPHAT,kernal)

titles = ['orignal_image','dilation', 'erosion', 'opening', 'closing', 'mor_gradient' , 'top_hat']
images = [img, dilation , erosion, opening, closing, mor_gradient, top_hat]
for i in range(6):
 plt.subplot(2,3,i+1)
 plt.imshow(images[i],'images')
 plt.title(titles[i])
 #plt.xticks([])
 #plt.yticks([])
plt.show()

