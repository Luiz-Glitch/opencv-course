import cv2 as cv
import numpy as np 

img = cv.imread("Resources\Photos.park.jpg")
cv.imshow("Park", img)

# Spliting the channels
b, g, r = cv.split(img)

# Using cv.imshow to these channels, we're going to get 3 grayscaled images
# the regions more white represent a greater concentration of that channel

print(img.shape) # the last element in the tuple it's the number of color channels

# color channels doesn't have the third element, because it's 1 (which is grayscale)
print(b.shape)
print(g.shape)
print(r.shape)

# merge the channels using cv.merge
merged = cv.merge([b, g, r])
cv.imshow("Merged Image", merged)

# show the actual color of the channel
blank = np.zeros(img.shape[:2], dtype='uint8')

# blank just represents the height and the width
# put the channel in its respective compartment
blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])