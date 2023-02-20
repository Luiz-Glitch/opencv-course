import cv2 as cv
import numpy as np

blank = np.zeros((400,400), dtype='uint8')

rectangle = cv.rectangle(blank.copy(), (30, 30), (370,370), 255, -1)

circle = cv.circle(blank.copy(), (200,200), 200, 255, -1)

cv.imshow("Rectangle", rectangle)
cv.imshow("Circle", circle)

# bitwise AND (returns the intersection)
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow('Bitwise AND', bitwise_and)

# bitwise OR (returns the union)
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow('Bitwise OR', bitwise_or)

# bitwise XOR (returns only non-intersecting regions)
# ie. if in the overlap a region is black in the circle, but white in the rectangle, it will turn white
# if in the overlap both are black or white, it will turn black
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('Bitwise XOR', bitwise_xor)

# bitwise NOT (inverts the values of the pixels)
bitwise_not = cv.bitwise_not(rectangle)
cv.imshow('Bitwise NOT', bitwise_not)

img = cv.imread("Resources\Photos\park.jpg")

# BITWISE Operators = AND, OR, XOR and NOT
# Pixel ON = 1; Pixel OFF = 0



cv.waitKey(0)