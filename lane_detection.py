import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np

img = cv.imread('road.jgp')
#img = cv.cvtColor(img3, cv.COLOR_BGR2RGB)

h = img.shape[0]
w = img.shape[1]

roi = [
   (0, h),
   (w/2,h/2),
   (w,h)
]
# the fucntion below will mask evry thing other than our region of interest
def region_of_interest(img,vertices):
    mask = np.zeros_like(img)
    # for retreiving the no. of channels of the image
    channel_count = img.shape[2]
    # this is 
    match_mask_color = (255,)*channel_count
    # now fill the polygon which is going to sill the region which is not of our interest
    cv.fillPoly(mask, vertices, match_mask_color)
    mask_img = cv.bitwise_and(img, mask)
    return masked_img


cropped_image = region_of_interest(img, np.array([roi], np.int32),)

# now we will draw the edges of the main lane , we will use hough transfrom for doing the same
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
edges = cv.Canny(gray, 100, 200)

plt.imshow(image)
plt.show()

