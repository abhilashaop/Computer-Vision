import numpy as np
import matplolib.pyplot as plt
import cv2 as cv

im  = cv.imread('poster.png')
img = cv.cvtcolor(im,cv.COLOR_BGR2RGB)

kernal = np.ones((5,5), np.float32)/25
dest = cv.filter2D(img,-1,kernal)
blur = cv.blur(img,(5,5))
gablur = cv.GaussianBlur(img, (5,5), 0)
median = cv.medianBlur(img,5)
bilateral_filter = cv.bilateralFilter(img,9,75,75)
images = [dest,blur,gablur,median,bilateral_filter]
titles = ['2D convulation','blur','Gaussian Blur', 'median', 'bilateral filter']
for i in range(4):
    plt.subplot(2,2,i+1)
    plt.imshow('blurring',images[i])
    plt.title(titles[i])
plt.show()    

