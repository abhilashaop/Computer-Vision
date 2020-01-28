import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('cat.jpg',0)

hist  = cv.calcHist([img],[0], None,  [256], [0,256])
plt.plot(hist)
plt.show()

