import cv2 as cv

img = cv.imread("Resources\Photos\park.jpg")
# A color space is a system of representing an array of pixel colors (RGB, HSV, Lab, etc.)

# BGR to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

# BGR TO HSV (human sensoritial value)
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# BGR to L+a+b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

# OpenCV = BGR. If you display an image in a python library different from
# OpenCV, you'll see an inversion of colors. So to prevent that, you'll
# need to convert BGR to RGB

rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)

cv.imshow()