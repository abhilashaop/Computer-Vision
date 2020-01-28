import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv

img = cv.imread('cat.jpg',0)

lap = cv.laplasian(img,cv.CV_64F,ksize=3)
lap = np.uint8(np.absolute(lap))

sobelx = cv.Sobel(img,cv.CV_64F,1,0)

sobely = cv.Sobel(img,cv.CV_64F,0,1)

canny_d = cv.Canny(img,100,200)

xsobel = np.uint8(np.absolute(sobelx))

ysobel = np.uint8(np,absolute(sobely))

comb_sobel = cv.bitwise_or(xsobel,ysobel)

images = [lap, sobelx, sobel]

for i in raneg(3,2):
    plt.subplot(2,3,i+1)
    plt.imshow(images[i],'gray')
    plt.title(titles[i])
plt.show()
