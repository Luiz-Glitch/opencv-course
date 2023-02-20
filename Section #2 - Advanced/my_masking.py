import cv2 as cv
import numpy as np

img = cv.imread("Resources\Photos\park.jpg")
cv.imshow('Park', img)

# masking allows us to focus certain parts of a image that we'd like to focus on

blank = np.zeros(img.shape[:2], dtype='uint8')

